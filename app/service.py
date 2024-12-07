import asyncio

import aiohttp


async def parse_files(public_url: str, path: str = "") -> list[dict]:
    """
    Asynchronously fetches a list of files and folders from a Yandex.Disk public URL.

    This function interacts with the Yandex.Disk API to retrieve information about files
    and folders from a public link, including their names, types (file or folder),
    paths, and download URLs. It handles nested folders recursively.

    :param public_url: The public URL key of the Yandex.Disk resource.
    :param path: The specific path to fetch files from within the public resource.
                          Defaults to an empty string, which fetches the root folder.

    :return: A list of dictionaries containing metadata about each file or folder.
             Each dictionary includes:
                 - "name" (str): The name of the file or folder.
                 - "type" (str): The type of the resource, either 'file' or 'folder'.
                 - "path" (str): The path to the resource.
                 - "url" (str or None): The download URL if it's a file, None if it's a folder.

    Raises:
        ValueError: If the API response status is not 200 (OK).
    """
    api_base_url = "https://cloud-api.yandex.net/v1/disk/public/resources"

    async def fetch_data(session: aiohttp.ClientSession, url: str) -> dict:
        """Makes a GET request and returns JSON data."""
        async with session.get(url) as resp:
            if resp.status != 200:
                raise ValueError(f"Ошибка API: {resp.status}")
            return await resp.json()

    async def get_items(session: aiohttp.ClientSession, path: str) -> list[dict]:
        """Gets a list of files and folders for a given path.."""
        api_url = f"{api_base_url}?public_key={public_url}"
        if path:
            api_url += f"&path={path}"
        data = await fetch_data(session, api_url)
        if "_embedded" in data:
            return data.get("_embedded", {}).get("items", [])
        else:
            return [data]

    async with aiohttp.ClientSession() as session:
        items = await get_items(session, path)
        result = []

        tasks = []
        for item in items:
            name = item.get("name")
            media_type = item.get("media_type", "folder")
            current_path = f"/{name}" if item.get("path") == "/" else item.get("path")
            download_url = item.get("file", None)

            # Append element to result.
            result.append({"name": name, "type": media_type, "path": current_path, "url": download_url})

            if media_type == "folder":
                task = parse_files(public_url, current_path)
                tasks.append(asyncio.create_task(task))

        # Collecting results asynchronously.
        children = await asyncio.gather(*tasks)
        for child_list in children:
            result.extend(child_list)

        return result
