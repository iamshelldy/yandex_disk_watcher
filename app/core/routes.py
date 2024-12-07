import json

from flask import render_template, request
from flask_login import login_required

from . import bp
from .. import redis
from ..service import parse_files


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('base.html')


@bp.route('/faq')
def faq():
    return 'faq'


@bp.route('/files', methods=['GET', 'POST'])
@login_required
async def files():
    files_types = set()

    url = request.args.get("public_url")
    path = request.args.get("path")

    cached_data = redis.get(url)
    if cached_data:
        data_deserialized = json.loads(cached_data)

        if path:
            data_deserialized = [
                item for item in data_deserialized if path in item["path"]
            ]

        for item in data_deserialized:
            files_types.add(item["type"])

        return render_template(
            "files.html",
            files=data_deserialized,
            types=files_types,
        )

    data = await parse_files(url)
    data.sort(key=lambda x: x["path"])

    serialized_data = json.dumps(data)
    redis.set(url, serialized_data, ex=3600)

    for item in data:
        files_types.add(item["type"])

    if path:
        data = [
            item for item in data if path in item["path"]
        ]

    return render_template(
        "files.html",
        files=data,
        types=files_types,
    )
