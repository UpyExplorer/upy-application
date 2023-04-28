# Installation

## Download

### Setting Variable

```bash
URL=https://github.com/UpyExplorer/upy-application.git
```

### Clone Repository

```bash
git clone $URL --branch master ~/upy-application
```

### Go to Folder

```bash
cd ~/upy-application
```

## Installation

### Install Requeriments

```bash
pip install -r requirements.txt --no-cache-dir
```

### Setup

```bash
python manage.py setup
```

## Execute

### Run

```bash
python manage.py runserver
```

### Access

```bash
http://127.0.0.1:8000/account/log-in/
```

### Login

- Email: `email@test.com`
- Password: `upyexplorer`
