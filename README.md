# Module 2: Assignment 2 - Basic Flask Application

## Overview

This project demonstrates a simple Flask REST API that handles HTTP GET and POST requests, processes JSON data, and includes error handling and automated tests.

The application contains two endpoints:

- **GET /hello** – Returns a greeting message.
- **POST /sum** – Accepts a JSON payload containing a list of numbers and returns their sum.

---

## Requirements

- Python 3.x
- Flask
- pytest

---

## Setup Instructions

### 1. Create and Activate a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
python -m pip install Flask pytest
```

---

## Running the Application

Start the Flask server:

```powershell
python app.py
```

The application will run locally on:

```text
http://127.0.0.1:5000
```

---

## API Endpoints

### GET /hello

Returns a greeting.

#### Example Request

```text
http://127.0.0.1:5000/hello
```

#### Example Response

```json
{
  "message": "Hello, World!"
}
```

#### Example Request with Name

```text
http://127.0.0.1:5000/hello?name=Michael
```

#### Example Response

```json
{
  "message": "Hello, Michael!"
}
```

---

### POST /sum

Accepts a list of numbers and returns the sum.

#### Example Request

```json
{
  "numbers": [1, 2, 3]
}
```

#### Example Response

```json
{
  "sum": 6
}
```

---

## Error Handling

The API returns HTTP 400 responses for invalid requests, including:

- Missing JSON payload
- Missing `"numbers"` field
- Invalid data types
- Non-numeric values in the list

Example:

```json
{
  "error": "Missing 'numbers' field"
}
```

---

## Running Tests

Execute the test suite with:

```powershell
pytest test_app.py
```

Expected result:

```text
================ test session starts ================
collected tests

PASSED
```

---

## Project Files

```text
flask_api_assignment/
│
├── app.py
├── test_app.py
├── README.md
└── .gitignore
```

---

## Author Michael Moody

Module 2 Assignment 2
Basic Flask Application Using Flask and pytest
