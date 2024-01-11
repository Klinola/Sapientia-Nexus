# Sapientia Nexus - Blockchain News Recon System

## Introduction
Sapientia Nexus is a blockchain news reconnaissance system designed to automatically collect, process, and analyze news articles from various blockchain-related news websites. This system aims to provide insights into the latest trends and developments in the blockchain industry.

## Features
- Automated news collection from multiple sources.
- News data storage in PostgreSQL database.
- Duplication detection and removal.
- Integration of AI for advanced data analysis (future feature).

## Requirements
- Python 3.x
- Django
- Celery
- Redis or RabbitMQ
- PostgreSQL

A complete list of requirements is available in `requirements.txt`.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Klinola/Sapientia-Nexus.git
cd Sapientia-Nexus
```

### 2. Virtual Environment
It's recommended to create a virtual environment for the project:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Ensure PostgreSQL is installed and running. Create a new database for the project.

### 5. Configuration
Configure the `settings.py` file in the Django project with your database settings and other preferences. Update the `config.ini` file with the list of news sources.

### 6. Run Migrations
```bash
python manage.py migrate
```

## Running the Application

### 1. Start Django Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/news/` for a raw view.

### 2. Celery Worker and Beat
In separate terminal windows, start Celery worker and beat:
```bash
celery -A Sapientia_Nexus worker -l info --pool=solo
celery -A Sapientia_Nexus beat -l info
```

## Usage

### Collecting and Processing News
To manually trigger news collection and processing:
```bash
python manage.py save_articles
python manage.py remove_duplicates
```

To manually analyse news using GPT-4
```bash
python manage.py analyze_articles
```
This will take 5 unanalyzed stories in the database and analyze them, you can modify the number of stories analyzed at a time by modifying `for article in articles[0:5]:` in this `analyse_articles.py`.

### Viewing the Data
Access the Django admin panel or use pgAdmin to view the collected news data in the PostgreSQL database.

## License
[MIT License](LICENSE)

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/Sapientia-Nexus/issues) for open issues or create a new one.
