# FastAPI Orders API Assessment

## Task Overview

You are given a partially implemented FastAPI backend application for asynchronous order processing. Your tasks are:

- Implement an asynchronous order API with endpoints organized using routers
- Persist orders in a database using SQLAlchemy
- Trigger a background task to (mock) send an order confirmation email on successful creation
- Validate inputs/outputs with Pydantic schemas
- Structure errors using custom exception handlers for consistent JSON error responses
- Write at least one integration-level test to confirm that order creation works and triggers the background task

## Directory Structure

- `app/` — FastAPI app code: routers, models, schemas, background task, and error handling
- `tests/` — Integration test(s), run via pytest
- `requirements.txt` — Python dependencies
- `Dockerfile` and `docker-compose.yml` — Containerization/configuration

## Setup Instructions

### 1. Build and Start the Environment

Run the following scripts from the project root:

```bash
chmod +x install.sh run.sh
./run.sh
```

This will:
- Build the Docker image and set up dependencies
- Start the FastAPI app at http://localhost:8000

### 2. Running Tests

To run tests inside the Docker container, open a new terminal and execute:

```bash
docker-compose run api pytest
```

## Your Tasks

- Complete implementation as needed so that all described features are functional and meet the requirements.
- Ensure structured, consistent error handling and data validation.
- Confirm that on creating an order, a mocked email is sent in a background task (visible in container logs/output).
- The provided integration test should pass and may be improved/expanded.

## Verifying Your Solution

- API should expose `/orders/` POST (create), GET (list), and `/orders/{id}/status` (check status) routes.
- Order creation persists to the DB and dispatches a (mock) confirmation email via background task.
- Error payloads are structured and consistent.
- Integration test(s) confirm both order creation and background task execution.

---

**No sample solutions are included. Complete any missing or marked sections as required.**
