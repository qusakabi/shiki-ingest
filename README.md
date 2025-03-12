# shiki-ingest

This project is an ETL pipeline for retrieving anime data from the Shikimori API, processing it, and loading it into a PostgreSQL database using SQLAlchemy.

## 📌 Features
- **Extract** (Extract): Fetches a list of popular anime from the Shikimori API.
- **Transform** (Transform): Formats the data for easy storage.
- **Load** (Load): Saves data into PostgreSQL. If a record already exists, it is updated.

## 📂 Project Structure
- `main.py` - The main script that runs the ETL process.
- `config.py` - Database connection settings (SQLAlchemy, .env).
- `extract.py` - Extracts data from the Shikimori API.
- `transform.py` - Transforms raw data into the required format.
- `models.py` - Defines the anime table model for the database.
- `utils.py` - Logging configuration.
- `requirements.txt` - List of dependencies.
- `docker-compose.yaml` - File for deploying PostgreSQL in a container.

## 🚀 Installation & Setup
### 1. Clone the repository
```bash
git clone https://github.com/qusakabi/shiki-ingest.git
cd shiki-ingest
```

### 2. Set up the environment
Create a `.env` file in the project root and specify the database connection parameters:
```
DB_HOST=localhost
DB_PORT=5432
DB_USER=
DB_PASS=
DB_NAME=
```

### 3. Start PostgreSQL with Docker
```bash
docker-compose up -d
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the ETL process
```bash
python main.py
```

## 🛠 Technologies
- **Python 3.8+**
- **PostgreSQL** (via Docker)
- **SQLAlchemy** (ORM for database interactions)
- **Shikimori API** (Data source)
- **Docker** (Containerization)

## 🔧 Configuration
Environment variables in the `.env` file:
- `DB_HOST` - Database host
- `DB_PORT` - Database port
- `DB_USER` - PostgreSQL user
- `DB_PASS` - PostgreSQL password
- `DB_NAME` - Database name

