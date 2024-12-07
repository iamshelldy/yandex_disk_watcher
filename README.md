# Yandex Disk Watcher

Yandex Disk Watcher is a web application designed to manage public Yandex Disk links. The application allows users to browse, filter, and download files and folders shared via Yandex Disk public links.

## Features

- **Public Link Parsing**: Extract files and folders from a public Yandex Disk link.
- **File Filtering**: Filter files by type directly in the UI.
- **Folder Navigation**: Navigate through nested folders.
- **Download Functionality**: Download selected files or entire folders.
- **Authentication**: Secure access with user login.

## Tech Stack

- **Backend**: Flask, Gunicorn, asyncio
- **Frontend**: Jinja2, HTML, CSS, JavaScript
- **Containerization**: Docker
- **API Integration**: Yandex Disk Public Resources API

## Installation

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized deployment)

### Clone the Repository

```bash
git clone https://github.com/iamshelldy/yandex_disk_watcher.git
cd yandex_disk_watcher
```

Next u have two options:
* [Use Python Virtual Environment](#local-setup)
* [Use Docker](#docker-deployment)

### Local Setup

#### Create a Virtual Environment:
```bash
python3 -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

#### Initialize and upgrade Database:
```bash
flask db upgrade
```

#### Run the Application:
```bash
gunicorn -b 0.0.0.0:8000 manage:app
```

### Docker Deployment
#### Build the Docker Image:
```bash
docker build -t yandex_disk_watcher .
```

#### Run the Docker Container:
```bash
docker run -p 8000:8000 yandex_disk_watcher
```

### Usage
1. Open the application in your browser.
2. Allow browser to open pop-up windows (guidelines can be found on the FAQ page).
3. Enter a Yandex Disk public link in the search field and submit.
4. Register an account in the form that opens to continue.
5. Browse the file structure, filter files, or navigate folders.
6. Select files or folders for download.
7. Click "Download" button.
