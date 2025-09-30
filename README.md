# Lab Results Analyzer

A simple web app that takes raw lab report text, analyzes it, and displays the results in a color-coded table.

---

## How to Run This Project

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/lab-dashboard.git](https://github.com/YOUR_USERNAME/lab-dashboard.git)
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
        *(Note: On some systems, you might use `python` instead of `python3`)*

3.  **Install the necessary libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Start the backend server:**
    ```sh
    uvicorn main:app --reload
    ```

5.  **Open the application:**
    * Go into the `frontend` folder.
    * Open the `index.html` file in your web browser.

---
