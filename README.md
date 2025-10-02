# Lab Results Analyzer

A full-stack web application that uses Optical Character Recognition (OCR) to scan uploaded lab report documents, analyze the data, and display the results in a color-coded table.

This tool intelligently parses messy text from an image, identifies a wide range of common blood tests using a flexible alias system, and flags any values that fall outside of normal clinical ranges.

---

## Features

* **Document Scanning:** Extracts text from uploaded images using the Tesseract OCR engine.
* **Intelligent Parsing:** Uses regular expressions to find test results, even in complex, multi-column documents.
* **Flexible Test Recognition:** Recognizes multiple names for the same test (e.g., "WBC" and "Total Leucocyte Count") using an alias system.
* **Value Flagging:** Automatically flags results as **HIGH**, **LOW**, or **NORMAL**.
* **REST API:** A robust backend built with FastAPI to handle file uploads, OCR, and analysis.

---

## Tech Stack

* **Backend:** Python, FastAPI, Tesseract (via `pytesseract`)
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Database:** SQLite

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* **Tesseract OCR Engine:** You must install Tesseract on your system.
    * **Windows:** [Download the installer](https://github.com/UB-Mannheim/tesseract/wiki)
    * **Mac:** `brew install tesseract`
    * **Linux:** `sudo apt-get install tesseract-ocr`

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/DarthPeanut/lab-dashboard.git](https://github.com/DarthPeanut/lab-dashboard.git)
    cd lab-dashboard
    ```

2.  **Set up and activate the virtual environment:**

    * **On Windows:**
        ```sh
        python -m venv venv
        venv\Scripts\activate
        ```

    * **On Mac & Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

1.  **Configure Tesseract Path (Windows Only):**
    * Open the `app/main.py` file.
    * Update the `pytesseract.pytesseract.tesseract_cmd` path to match your Tesseract installation location (e.g., `r'C:\Program Files\Tesseract-OCR\tesseract.exe'`).

2.  **Start the backend server:**
    ```sh
    python -m uvicorn app.main:app --reload
    ```
    The API will be running at `http://127.0.0.1:8000`.

3.  **Launch the frontend:**
    * Navigate to the `frontend/` directory.
    * Open the `index.html` file in your web browser.

4.  **Analyze a document:**
    * Enter a Patient ID.
    * Click "Choose File" and select an image of a lab report.
    * Click the "Analyze Document" button to see the results.

---
