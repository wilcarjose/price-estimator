# Housing Price Predictor API 🔮

![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Framework](https://img.shields.io/badge/framework-FastAPI-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

An high-performance REST API built with FastAPI to predict median house values using a Scikit-learn regression model. This project serves as a demonstration of best practices in building and serving machine learning models.

---

## 📖 About The Project

This project takes a trained Scikit-learn `RandomForestRegressor` model and makes it available through a production-ready API. It showcases a complete workflow from a trained model artifact to a fully functional, versioned, and interactive web service.

The architecture is designed following SOLID principles, emphasizing separation of concerns, dependency injection, and clear data contracts to ensure the application is robust, scalable, and maintainable.

### ✨ Key Features

* **Modern API Framework:** Built with **FastAPI** for high performance and asynchronous capabilities.
* **Data Validation:** Uses **Pydantic** models to define clear, validated data contracts for all requests and responses.
* **Clean Architecture:** Employs a **Service Layer** to separate business logic from the API framework, following the Single Responsibility Principle.
* **Dependency Injection:** Leverages FastAPI's DI system to manage resources like the ML model, making the code decoupled and highly testable.
* **Centralized Configuration:** Manages settings like model paths and app metadata through a single configuration object.
* **Structured Logging:** Implements structured logging for effective monitoring and debugging.
* **Automatic Interactive Documentation:** Provides a rich, interactive API documentation endpoint powered by Swagger UI.

###  API Documentation Preview

The API includes self-generated, interactive documentation available at the `/docs` endpoint.

![API Docs Preview](https://i.imgur.com/Wt2bL17.png) 
---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.10 or higher
* pip & venv

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/wilcarjose/price-estimator.git
    cd price-estimator
    ```
    
2. **Configure Git LFS**
   - **Install Git LFS (only if you don't have it already installed)**
       - **macOS (con Homebrew):** `brew install git-lfs`
       - **Debian/Ubuntu:** `sudo apt-get install git-lfs`
       - **Windows:** Descargar el instalador desde https://git-lfs.github.com/
   - **Pull LFS file**
     ```
     git lfs pull
     ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Crete `.env` file**
    ```bash
    cp .env.example .env
    ```

6.  **Run the API server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

---

## 💻 Usage

You can interact with the API via the automatic documentation at `http://127.0.0.1:8000/docs` or send requests directly to the endpoint.

### Prediction Endpoint

* **URL:** `/api/v1/predict`
* **Method:** `POST`
* **Body (JSON):**

    ```json
    {
      "median_income": 8.3,
      "house_age": 41.0,
      "average_rooms": 6.9,
      "average_bedrooms": 1.0,
      "population": 322.0,
      "average_occupancy": 2.5,
      "latitude": 37.88,
      "longitude": -122.23
    }
    ```

* **Example `curl` Request:**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/v1/predict \
    -H "Content-Type: application/json" \
    -d '{ "median_income": 8.3, "house_age": 41.0, "average_rooms": 6.9, "average_bedrooms": 1.0, "population": 322.0, "average_occupancy": 2.5, "latitude": 37.88, "longitude": -122.23 }'
    ```

---

## 🏗️ Project Structure
The project is organized with a clean, scalable architecture:
```
price-estimator/
├── api/              # API versioning and endpoints
├── config/           # Logging setup and application configuration
├── logs/             # Log files (ignored by git)
├── models/           # Trained ML model artifacts
├── schemas/          # Pydantic data models (contracts)
├── services/         # Core business logic
└── main.py           # Main FastAPI app instance 
```

---

## 🗺️ Roadmap

* [ ] Add comprehensive automated tests (unit and integration)
* [ ] Implement a more robust error handling middleware
* [ ] Dockerize the application for containerized deployment
* [ ] Set up a CI/CD pipeline for automated testing and deployment

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/wilcarjose/price-estimator/blob/main/LICENSE.md) file for details.