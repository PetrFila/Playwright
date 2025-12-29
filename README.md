# Playwright Test Automation Framework

This repository contains an automated test suite for the [SauceDemo](https://www.saucedemo.com/) e-commerce website, built with **Python**, **Playwright**, and **Pytest**.

## 🚀 Features

* **Page Object Model (POM):** Maintainable and readable codebase.
* **Global Authentication:** Uses `storage_state` to log in once per session, speeding up execution.
* **CI/CD Integration:** GitHub Actions workflow runs tests on every push.
* **Artifacts:** Automatically captures traces and screenshots on test failure.

## 🛠️ Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
    cd REPO_NAME
    ```

2.  **Install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install pytest-playwright
    playwright install
    ```

## 🏃‍♂️ Running Tests

**Run all tests:**
```bash
python -m pytest
