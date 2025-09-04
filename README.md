# FastAPI Example Project

This repository provides a simple **FastAPI** application that demonstrates basic API features, including routing, request validation, and middleware setup.  
It is intended for learning and experimenting with FastAPI.

## Features

- `GET /` – Root endpoint with a welcome message and available routes.  
- `GET /hello/{name}` – Returns a personalized greeting.  
- `GET /status` – Returns the current API status, uptime, and version.  
- `POST /send-message` – Accepts a message payload with sender, content, and optional importance flag.  
- `GET /getAPI` – Generates a random API key and returns both the raw key and its SHA-256 hash.  
- `GET /about` – Example endpoint returning static information.  

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/) – web framework  
- [Pydantic](https://docs.pydantic.dev/) – data validation  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/IbrokhimN/FastAPI.git
cd FastAPI
pip install -r requirements.txt
````

## Running the application

Run the app with **Uvicorn**:

```bash
uvicorn main:app --reload
```

The API will be available at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive API documentation:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## License

This project is provided for **educational and demonstration purposes only**.
Feel free to use and modify it for your own learning.

