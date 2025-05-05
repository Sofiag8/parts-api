
# Parts API

A fully containerized Django REST API for managing parts. It supports standard CRUD operations, bulk creation/deletion, a custom analytical endpoint, and includes test coverage, input validation, and Postman documentation.

---

## Features

- CRUD operations on parts
- Bulk creation and deletion of parts
- Custom endpoint to return the 5 most common words in part descriptions
- Detailed field validation with clear error messages
- Automated tests using Django TestCase
- Dockerized setup with PostgreSQL
- Postman collection for easy testing

---

## Requirements

- Docker & Docker Compose
- Python 3.11+ 
- Git

---

## Running the Project with Docker

> This is the recommended method to run the project in a fully isolated environment.

1. Clone the repo:

```bash
git clone https://github.com/Sofiag8/parts-apil
cd parts-api
```

2. Create a `.env` file with:

```env
POSTGRES_DB=parts_db
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_PORT=8000

```

3. Build and run the containers:

```bash
docker compose up --build
```

4. Apply migrations and create superuser:

```bash
docker compose exec app python manage.py migrate
docker compose exec app python manage.py createsuperuser
```

Then visit: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## Running Tests

Tests are designed to run locally using SQLite in-memory, meaning **you do not need to run Docker or have PostgreSQL running** to validate functionality.

To run the test suite:

```bash
python manage.py test
```

This will:

- Automatically switch the database to in-memory SQLite
- Spin up a temporary schema
- Run full API test coverage
- Validate core functionality and error handling

This behavior is configured via `settings.py` by checking for the `test` command in `sys.argv`.

---

## API Endpoints

All endpoints are available under `/api/parts/`.

| Method | Endpoint                     | Description                          |
|--------|------------------------------|--------------------------------------|
| GET    | `/api/parts/`                | List all parts                       |
| POST   | `/api/parts/`                | Create a single part                 |
| PUT    | `/api/parts/<id>/`           | Update a part by ID                  |
| DELETE | `/api/parts/<id>/`           | Delete a part by ID                  |
| POST   | `/api/parts/bulk-create/`    | Create multiple parts at once        |
| DELETE | `/api/parts/bulk-delete/`    | Delete multiple parts by IDs         |
| GET    | `/api/parts/top-words/`      | Get 5 most common words in descriptions |

---

## Field Validation

All fields are required when creating or updating a part. The API will return meaningful errors if any are missing or empty:

```json
{
  "sku": ["The 'sku' field cannot be empty."],
  "weight_ounces": ["The 'weight_ounces' must be greater than 0."]
}
```

---

## Database Configuration

By default, the app connects to a PostgreSQL database via environment variables:

```env
POSTGRES_DB=parts_db
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

For local development, you can switch to SQLite by editing `settings.py` or by running tests without Docker.

To reset the database completely:

```bash
docker compose down -v
```

---

## Postman Collection

A complete [Postman collection](qventus-parts-api.postman_collection.json) is included to help you test all endpoints quickly.

To use it:

1. Open Postman
2. Import the file `qventus-parts-api.postman_collection.json`
3. Run each request (CRUD, bulk, top-words)

---

## Test Coverage

Unit tests are written using Django's `TestCase` framework and cover:

- Create Part
- Update Part
- Bulk Create
- Bulk Delete
- Top Words endpoint

To run:

```bash
python manage.py test
```

---

## Docker Architecture

This project includes a production-ready Docker setup:

- `Dockerfile`: builds a slim Python 3.11 Django image
- `docker-compose.yml`: runs Django + PostgreSQL together
- `volumes`: ensure data persistence for the DB
- `env_file`: centralizes credentials and config

---

## Notes

- The `scripts/populate.py` file is used to seed the database with example parts
- Unlike Django `manage.py` commands, standalone scripts like this require manual setup of Django’s environment using `os.environ['DJANGO_SETTINGS_MODULE']`
- During test runs, Django automatically creates and destroys a test database to avoid polluting local data

---

## Project Structure

```
parts-api/
├── parts/                  # Main app with models, views, serializers, tests
├── parts_api/              # Django project config
├── scripts/                # Seed scripts for local/dev
├── Dockerfile              # Docker app image
├── docker-compose.yml      # Compose file for Django + Postgres
├── requirements.txt        # Python dependencies
├── qventus-parts-api.postman_collection.json
└── README.md
```


Once `docker compose up` run, you can:

- Hit `localhost:8000/api/parts/` for the API
- Access `/admin/` with your superuser
- Import and test via Postman
- Run `manage.py test` and get validation & coverage



## Author

Sofia García  
Backend Developer · Node.js · Python · HubSpot Integrations  
[LinkedIn](https://www.linkedin.com/in/sofiagarciacaicedo/)