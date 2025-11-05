# automamated_testing_with_pytest

This repository demonstrates how to build and organize automated tests using **[pytest](https://docs.pytest.org/)** for different layers of a Python project — including unit, integration, API, and UI testing.

## 📁 Project Structure

tau-intro-to-pytest/

│

├── stuff/

│ └── accum.py # Accumulator class for accumulator tests

│

├── inventory/

│ └── account.py # UserAccount class for account tests

│

├── tests/

│ ├── test_math.py # Unit tests for math operations

│ ├── test_accum.py # Unit tests for the Accumulator class

│ ├── test_account.py # Unit tests for the UserAccount class

│ ├── test_api.py # Integration test for DuckDuckGo API

│ └── test_ui.py # UI test for Acme Bank demo site

│

├── requirements.txt

└── README.md


---

## ⚙️ Setup Instructions

**1. Clone the repository**

git clone https://github.com/your-username/automated_testing_with_pytest.git

cd automated_testing_with_pytest

**2. Create and activate a virtual environment**
   
python -m venv venv

source venv/bin/activate    # on macOS/Linux

venv\Scripts\activate       # on Windows

**3. Install dependencies**

pip install -r requirements.txt

* Example requirements.txt:

pytest
requests
pytest-playwright
playwright

* Then install Playwright browsers:

playwright install

## 🧩 Test Overview

**1️⃣ test_math.py**

Purpose: Verify basic mathematical operations and Python exceptions.

Tests:

* ✅ test_one_plus_one → Checks 1 + 1 == 2
* ✅ test_one_plus_two → Verifies variable addition
* ✅ test_devide_by_zero → Ensures ZeroDivisionError is raised correctly
* ✅ test_recursion_depth → Confirms RuntimeError raised for infinite recursion

Marker: @pytest.mark.math

**2️⃣ test_accum.py**

Purpose: Unit tests for the Accumulator class in stuff/accum.py.

Fixtures:

accum, accum2 — sample Accumulator instances

Tests:

* ✅ test_accumulator_init → Starts with count = 0
* ✅ test_accumulator_add_one → Increments count by 1
* ✅ test_accumulator_add_three → Increments count by 3
* ✅ test_accumulator_add_twice → Adds twice
* ✅ test_accumulator_cannot_set_count_directly → Ensures count is read-only

Marker: @pytest.mark.accumulator

**3️⃣ test_account.py**

Purpose: Tests for UserAccount class in inventory/account.py.

Fixture:

sample_user → Creates a UserAccount("Alice", "Johnson")

Tests:

* ✅ Username generation (first initial + last 3 letters)
* ✅ Handles short last names
* ✅ Password length = 10
* ✅ No repeated consecutive characters
* ✅ Password contains only valid characters
* ✅ Different users get unique passwords

**4️⃣ test_api.py**

Purpose: Integration test verifying DuckDuckGo’s public API response.

Test:

✅ test_duckduckgo_instant_answer_api

Sends GET request to DuckDuckGo Instant Answer API

Asserts JSON structure and content

Markers: @pytest.mark.api, @pytest.mark.duckduckgo

**5️⃣ test_ui.py**

Purpose: UI automation test using Playwright.

Test:

✅ test_acme_bank_login

Navigates to Applitools Demo Bank

Logs in with demo credentials

Verifies key dashboard elements are visible

Markers: @pytest.mark.ui, @pytest.mark.acme_bank

## 🧭 Running Tests

* Run **all tests**:

pytest -v

* Run tests by **marker**:

pytest -m math          # only math tests

pytest -m accumulator   # only accumulator tests

pytest -m api           # only API tests

pytest -m ui            # only UI tests

* Run **a specific test file**:

pytest tests/test_account.py -v

* Run with **Playwright UI preview**:

pytest tests/test_ui.py --headed

## 📊 Test Reporting

* Generate a simple test report:

pytest --html=report.html --self-contained-html

## 🧠 Key Concepts Demonstrated

* ✅ Unit testing with pytest
* ✅ Test organization using markers and fixtures
* ✅ API testing with requests
* ✅ UI testing with pytest-playwright
* ✅ Exception handling verification
* ✅ Test-driven validation of class behaviors
