# SprintSync

An intelligent sprint tracking and task management platform powered by AI-driven task assignment and daily planning recommendations. Built with FastAPI, PostgreSQL, and OpenAI embeddings for optimal team productivity.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Database Migrations](#database-migrations)
- [Docker Deployment](#docker-deployment)
- [Architecture](#architecture)


## 🎯 Overview

SprintSync is an internal sprint tracking tool designed for AI consultancy teams. It streamlines task management, automates intelligent task assignment based on team member skills, and provides AI-powered daily work plan suggestions. The platform leverages vector embeddings to match tasks with team members whose expertise best aligns with project requirements.

**Current Version:** 1.0.0  
**Last Updated:** February 26, 2026

## ✨ Features

### Core Functionality
- 🔐 **Secure Authentication**: JWT-based user authentication with bcrypt password hashing
- 📋 **Task Management**: Full CRUD operations for task creation, assignment, and tracking
- 👥 **User Management**: User profiles with skill-based resume embeddings
- 🤖 **AI Task Assignment**: Automatic task-to-user matching using vector similarity
- 📊 **Daily Planning**: AI-generated daily work suggestions based on assigned tasks
- 📈 **Performance Analytics**: Track team metrics and top performer statistics
- 🔢 **System Metrics**: Request tracking, latency monitoring, and performance insights
- 🏥 **Health Monitoring**: System health check endpoints

### Advanced Capabilities
- 🧠 **Vector Embeddings**: pgvector-based semantic matching for intelligent assignments
- 📍 **Resume-Based Matching**: Skills extracted from resume text for better task alignment
- 📝 **Structured Logging**: Comprehensive request/response logging with latency tracking
- 🔍 **Flexible Search**: Query parameters for workspace-based searches
- ✅ **Status Management**: Task workflow with TODO, IN_PROGRESS, and DONE states

## 🛠 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend Framework** | FastAPI | 0.104+ |
| **Database** | PostgreSQL | 15+ |
| **Vector Extension** | pgvector | 0.5+ |
| **ORM** | SQLAlchemy | 2.0+ |
| **Migrations** | Alembic | 1.12+ |
| **Authentication** | JWT + Passlib | - |
| **Password Hashing** | Bcrypt | - |
| **AI Embeddings** | OpenAI API | - |
| **Testing** | Pytest | 7.4+ |
| **Package Manager** | Poetry | 1.6+ |
| **Containerization** | Docker & Docker Compose | - |
| **Python Version** | 3.11+ | - |

## 📁 Project Structure

```
sprintsync/
├── app/
│   ├── core/
│   │   ├── config.py              # Application configuration constants
│   │   ├── security.py            # JWT token and password utilities
│   │   ├── logging_middleware.py  # HTTP request/response logging
│   │   └── metrics.py             # Metrics collection and aggregation
│   ├── db/
│   │   └── session.py             # Database session and connection setup
│   ├── models/
│   │   ├── user.py                # User model with resume embeddings
│   │   ├── task.py                # Task model
│   │   └── __init__.py
│   ├── routers/
│   │   ├── auth.py                # Authentication endpoints (register, login)
│   │   ├── tasks.py               # Task CRUD endpoints
│   │   ├── ai.py                  # AI suggestion generation
│   │   ├── metrics.py             # System metrics endpoint
│   │   ├── stats.py               # User performance statistics
│   │   ├── health.py              # Health check endpoint
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py                # User Pydantic schemas
│   │   ├── task.py                # Task Pydantic schemas
│   │   └── __init__.py
│   ├── services/
│   │   ├── embedding_service.py   # OpenAI embedding generation
│   │   ├── ai_service.py          # AI planning logic
│   │   └── __init__.py
│   ├── dependencies.py            # Dependency injection setup
│   ├── main.py                    # FastAPI application entry point
│   └── __init__.py
├── alembic/
│   ├── env.py                     # Alembic environment configuration
│   ├── script.py.mako             # Migration script template
│   ├── versions/                  # Migration files (auto-generated)
│   │   └── xxxxx_*.py             # Individual migration versions
│   └── alembic.ini                # Alembic configuration
├── tests/
│   ├── conftest.py                # Pytest configuration and fixtures
│   ├── test_auth.py               # Authentication tests
│   ├── test_tasks.py              # Task management tests
│   ├── test_ai.py                 # AI feature tests
│   ├── test_metrics.py            # Metrics tests
│   └── __init__.py
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD pipeline
├── docker-compose.yml             # Multi-container Docker configuration
├── Dockerfile                     # Docker image definition
├── pyproject.toml                 # Poetry dependencies and metadata
├── pytest.ini                     # Pytest configuration
├── .env                           # Environment variables (local development)
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
└── LICENSE                        # Project license

```

## 📋 Prerequisites

Before setting up SprintSync, ensure you have the following installed:

- **Python**: 3.11 or higher ([Download](https://www.python.org/downloads/))
- **PostgreSQL**: 15 or higher ([Download](https://www.postgresql.org/download/))
- **Poetry**: 1.6 or higher ([Installation Guide](https://python-poetry.org/docs/#installation))
- **Docker** & **Docker Compose**: Latest versions ([Download](https://www.docker.com/products/docker-desktop))
- **Git**: For version control ([Download](https://git-scm.com/))
- **OpenAI API Key**: For embedding generation ([Get Key](https://platform.openai.com/api-keys))

### System Requirements

- **OS**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Disk**: Minimum 2GB free space
- **Network**: Internet connection for OpenAI API calls

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-organization/sprintsync.git
cd sprintsync
```

### Step 2: Set Up Python Environment

Using Poetry (recommended):

```bash
# install / sync dependencies
poetry install

# this creates/uses the virtual environment defined by Poetry
# and installs everything from [pyproject.toml](http://_vscodecontentref_/0)
```

### Step 3: Configure Environment Variables

1. Copy the example environment file:

```bash
copy .env.example .env
# On macOS/Linux:
cp .env.example .env
```

2. Edit `.env` with your configuration (see [Configuration](#configuration) section)

### Step 4: Set Up PostgreSQL Database

#### Option A: Using Docker Compose (Recommended)

```bash
# Start PostgreSQL container
docker-compose up -d db

# Wait for PostgreSQL to be ready (typically 10-15 seconds)
```

#### Option B: Local PostgreSQL Installation

```bash
# Ensure PostgreSQL is running
# Windows: Start PostgreSQL service
# macOS: brew services start postgresql
# Linux: sudo systemctl start postgresql

# Create database and user
psql -U postgres
CREATE DATABASE sprintsync;
CREATE USER sprintuser WITH PASSWORD 'sprintpass';
ALTER ROLE sprintuser SET client_encoding TO 'utf8';
ALTER ROLE sprintuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE sprintuser SET default_transaction_deferrable TO on;
ALTER ROLE sprintuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sprintsync TO sprintuser;
\q
```

### Step 5: Enable pgvector Extension

```bash
# Connect to the database
psql -U sprintuser -d sprintsync -h localhost

# Create pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

# Verify installation
SELECT * FROM pg_extension WHERE extname = 'vector';

# Exit
\q
```

### Step 6: Run Database Migrations

```bash
poetry run alembic upgrade head
```

This initializes all database tables and schemas required by the application.

> **Demo data:**
> When using the Docker setup (or running the seed script manually), the database will be pre-populated with two users and two tasks. You can log in using the following credentials:
>
> - **Admin**: `admin@sprintsync.com` / `admin123`
> - **User**: `user1@sprintsync.com` / `password123`
>
> These accounts are provided for testing purposes only and are recreated whenever the seed script runs on an empty database. Change or remove them in production deployments.

### Step 7: Verify Installation

```bash
# Test the setup by running tests
poetry run pytest -v

# If all tests pass, your installation is complete!
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration
DATABASE_URL=postgresql://sprintuser:sprintpass@localhost:5432/sprintsync

# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# JWT Configuration
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Application Configuration
DEBUG=True
ENVIRONMENT=development
LOG_LEVEL=INFO

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

### Configuration Details

| Variable | Description | Default Value | Example |
|----------|-------------|----------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | - | `postgresql://user:pass@localhost:5432/db` |
| `OPENAI_API_KEY` | Your OpenAI API key | - | `sk-...` |
| `OPENAI_EMBEDDING_MODEL` | Model for text embeddings | `text-embedding-3-small` | `text-embedding-3-large` |
| `SECRET_KEY` | JWT signing secret | `dev-secret` | Use strong random string in production |
| `ALGORITHM` | JWT algorithm | `HS256` | Do not change unless required |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | `60` | Adjust based on security policy |
| `DEBUG` | Debug mode | `False` | Set to `True` only in development |
| `ENVIRONMENT` | Application environment | `production` | `development`, `staging`, `production` |
| `LOG_LEVEL` | Logging level | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |

### Production Configuration

For production deployment:

```env
DEBUG=False
ENVIRONMENT=production
SECRET_KEY=<generate-strong-random-key>
DATABASE_URL=<hardened-database-url>
LOG_LEVEL=WARNING
```

Generate a strong secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## ▶️ Running the Application

### Development Mode

Using Poetry:

```bash
poetry run uvicorn app.main:app --reload
```

The `--reload` flag enables hot-reloading on code changes.

### Production Mode

```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Container

```bash
# Build the Docker image
docker build -t sprintsync:latest .

# Run the container
docker run -p 8000:8000 --env-file .env sprintsync:latest
```

### Using Docker Compose

```bash
# Start all services (API + PostgreSQL)
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

### Accessing the Application

Once running, access the application at:

- **API Server**: `http://localhost:8000`
- **API Docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative Docs (ReDoc)**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## 📚 API Documentation

### Authentication Endpoints

#### Register User

```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword123",
  "resume_text": "Senior Software Engineer with 5 years of experience..."
}
```

**Response:**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "is_admin": false,
  "resume_embedding": [0.123, 0.456, ...],
  "created_at": "2026-02-26T10:30:00Z"
}
```

#### Login

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

### Task Management Endpoints

#### List Tasks

```http
GET /tasks/
Authorization: Bearer {access_token}
```

**Query Parameters:**
- `skip` (int): Number of tasks to skip (pagination)
- `limit` (int): Maximum tasks to return
- `status` (str): Filter by status (TODO, IN_PROGRESS, DONE)

#### Create Task

```http
POST /tasks/
Content-Type: application/json
Authorization: Bearer {access_token}

{
  "title": "Implement user authentication",
  "description": "Add JWT-based authentication with role-based access control",
  "total_minutes": 480,
  "priority": "high"
}
```

#### Get Task Details

```http
GET /tasks/{task_id}
Authorization: Bearer {access_token}
```

#### Update Task

```http
PUT /tasks/{task_id}
Content-Type: application/json
Authorization: Bearer {access_token}

{
  "title": "Updated title",
  "description": "Updated description",
  "total_minutes": 360
}
```

#### Update Task Status

```http
PATCH /tasks/{task_id}/status
Content-Type: application/json
Authorization: Bearer {access_token}

{
  "status": "IN_PROGRESS"
}
```

#### Delete Task

```http
DELETE /tasks/{task_id}
Authorization: Bearer {access_token}
```

### AI & Analytics Endpoints

#### Get Daily Plan Suggestions

```http
GET /ai/suggest
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "suggestions": [
    {
      "task_id": "uuid",
      "title": "Task Title",
      "priority": "high",
      "estimated_time": 120,
      "reason": "Aligns with your backend expertise"
    }
  ],
  "generated_at": "2026-02-26T10:30:00Z"
}
```

#### Get Top Performers

```http
GET /stats/top-users?limit=10
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "top_users": [
    {
      "user_id": "uuid",
      "email": "topuser@example.com",
      "total_minutes": 1200,
      "completed_tasks": 15
    }
  ]
}
```

#### Get System Metrics

```http
GET /metrics
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "total_requests": 1523,
  "error_count": 12,
  "avg_response_time_ms": 85.5,
  "requests_by_endpoint": {
    "POST /auth/login": 243,
    "GET /tasks/": 521
  }
}
```

#### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-26T10:30:00Z",
  "database": "connected",
  "version": "1.0.0"
}
```

### Current User Endpoint

```http
GET /me
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "is_admin": false,
  "created_at": "2026-02-26T10:00:00Z"
}
```

## ✅ Testing

### Running Tests

Run all tests:

```bash
poetry run pytest -v
```

Run specific test file:

```bash
poetry run pytest tests/test_auth.py -v
```

Run tests matching a pattern:

```bash
poetry run pytest -k "test_login" -v
```

### Test Coverage

Generate coverage report:

```bash
poetry run pytest --cov=app --cov-report=html
```

View the HTML report:

```bash
# On Windows
start htmlcov/index.html

# On macOS
open htmlcov/index.html

# On Linux
xdg-open htmlcov/index.html
```

### Test Structure

```
tests/
├── conftest.py        # Pytest fixtures and configuration
├── test_auth.py       # Authentication tests
├── test_tasks.py      # Task management tests
├── test_ai.py         # AI features tests
└── test_metrics.py    # Metrics and monitoring tests
```

### Sample Test Execution

```bash
# Run all tests with verbose output
poetry run pytest tests/ -v --tb=short

# Run with coverage and html report
poetry run pytest tests/ --cov=app --cov-report=html:coverage

# Run only unit tests, excluding integration tests
poetry run pytest tests/ -m "not integration" -v
```

## 🗄️ Database Migrations

### Understanding Migrations

Migrations are version-controlled database schema changes. The project uses Alembic for migration management.

### Creating a New Migration

After modifying models in `app/models/`, create a migration:

```bash
poetry run alembic revision --autogenerate -m "Add new_column to users table"
```

This generates a new file in `alembic/versions/` with the changes.

### Reviewing a Migration

```bash
# Show all migrations and their status
poetry run alembic history

# Show current migration version
poetry run alembic current
```

### Applying Migrations

```bash
# Apply all pending migrations
poetry run alembic upgrade head

# Apply specific number of migrations
poetry run alembic upgrade +2

# Rollback to previous version
poetry run alembic downgrade -1

# Rollback to specific revision
poetry run alembic downgrade 1975ea83b712
```

### Migration Workflow

1. Modify model in `app/models/`
2. Generate migration: `alembic revision --autogenerate -m "description"`
3. Review generated migration file
4. Apply migration: `alembic upgrade head`
5. Commit migration file to version control

### Custom Migration

If autogenerate doesn't capture your changes:

```bash
poetry run alembic revision -m "Custom migration description"
```

Then edit the generated file in `alembic/versions/` manually with your SQL changes.

## 🐳 Docker Deployment

### Building Docker Image

```bash
docker build -t sprintsync:latest .
docker build -t sprintsync:1.0.0 .  # With version tag
```

### Docker Compose

The `docker-compose.yml` file includes:
- **api**: FastAPI application service
- **db**: PostgreSQL database service with pgvector

Start all services:

```bash
docker-compose up -d
docker-compose logs -f
```

### Environment-Specific Deployment

Development:

```bash
docker-compose -f docker-compose.yml up -d
```

Production:

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Container Management

```bash
# View running containers
docker-compose ps

# View logs
docker-compose logs -f api

# Execute command in container
docker-compose exec api poetry run pytest

# Stop containers
docker-compose stop

# Remove containers and volumes
docker-compose down -v

# Rebuild images
docker-compose build --no-cache
```

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Applications                      │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP/REST
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   FastAPI Application                        │
├─────────────────────────────────────────────────────────────┤
│ • Authentication (JWT)                                       │
│ • Task Management (CRUD)                                     │
│ • AI Services                                                │
│ • Metrics & Logging                                          │
└──────────────┬──────────────────────────────┬────────────────┘
               │                              │
               ▼                              ▼
    ┌─────────────────────┐      ┌────────────────────┐
    │ PostgreSQL Database │      │  OpenAI API        │
    │ + pgvector          │      │  (Embeddings)      │
    │                     │      │                    │
    │ • Users             │      │ • Task embeddings  │
    │ • Tasks             │      │ • Resume embeddings│
    │ • Embeddings        │      │                    │
    └─────────────────────┘      └────────────────────┘
```

### Request Flow

1. **Authentication**: Client sends credentials → JWT token issued
2. **Task Creation**: User creates task → Description embedded → User matched via similarity
3. **Daily Planning**: User requests suggestions → Relevant tasks processed → AI suggestions generated
4. **Metrics**: All requests tracked → Latency monitored → Aggregated metrics returned

### Key Components

**Security Layer:**
- JWT token validation
- Password hashing (bcrypt)
- Role-based access control

**Data Layer:**
- SQLAlchemy ORM
- PostgreSQL with pgvector extension
- Alembic migrations

**Business Logic:**
- Embedding generation service
- AI planning service
- Task assignment engine

**API Layer:**
- FastAPI routing
- Pydantic validation
- Exception handling


docker --version

# View container logs
docker-compose logs db

# Rebuild and restart
docker-compose down -v && docker-compose up --build
```

#### OpenAI API Issues

```bash
# Validate API key format
echo $OPENAI_API_KEY

# Test API connectivity
curl -H "Authorization: Bearer $OPENAI_API_KEY" https://api.openai.com/v1/models
```

#### Test Failures

```bash
# Run with verbose output
poetry run pytest -v --tb=long

# Run single test
poetry run pytest tests/test_auth.py::test_register -v

# Clear cache and rerun
poetry run pytest --cache-clear tests/
```

### Performance Optimization

- Enable query result caching for frequently accessed data
- Use database connection pooling (configured in SQLAlchemy)
- Monitor metrics endpoint for bottlenecks
- Consider read replicas for scaling read operations

## 📊 Monitoring & Logging

### Access Logs

All HTTP requests are logged with:
- Request method and path
- Response status code
- User ID (if authenticated)
- Response latency

Logs are written to console and can be redirected to files.

### Metrics Collection

The `/metrics` endpoint provides:
- Total request count
- Error count
- Average response time
- Requests per endpoint breakdown

### Health Monitoring

Regular health checks available at `/health` endpoint.

## 📝 License

This repository contains a **sample/prototype implementation** of SprintSync.  
It is provided for demonstration and internal evaluation only; no commercial
use, redistribution or modification is permitted without express authorization
from the owning organisation.  Consult your team’s licensing policy for
details.


## 🎓 Version History

| Version | Release Date | Notable Changes |
|---------|-------------|-----------------|
| 1.0.0 | Feb 26, 2026 | Initial release - Core functionality complete |

---


