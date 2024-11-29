# JSON Validator Web App

This is a simple web application built using Python (Flask) and HTML/CSS. It allows users to input JSON code, validate whether it's valid or not, and provides feedback. The application runs on a local server and automatically opens a webpage where users can interact with the JSON validator.

## Features

- Input a JSON string into a text box.
- Validate the JSON by clicking a button.
- Display whether the JSON is valid or not.
- A clear button to reset the input box.
- If no JSON is entered, users are prompted to input JSON before validation.
- A GitHub icon links to the project repository.

## Requirements

- Python 3.x
- Flask
- HTML, CSS (for styling and layout)

## Setup

1. Clone or download this repository to your local machine.
2. Install the required Python packages by running:
    ```bash
    pip install Flask
    ```

3. Run the Python application:
    ```bash
    python JsonValidator.py
    ```

4. The application will automatically open your default browser with the local server (usually at `http://127.0.0.1:5000/`).
   
5. You can now input JSON data in the provided text box and click the "Validate" button to check if the JSON is valid.

## Usage

- **Validate**: Enter JSON into the box and click the "Validate" button. The app will tell you if the JSON is valid or not.
- **Clear**: Click the "Clear Box" button to clear the input field.
- **JSON Status**: After validation, the app will display whether the JSON is valid or not below the text box.
- **GitHub Link**: A GitHub icon is displayed at the bottom of the page, linking to the project repository.

## GitHub

- [GitHub Repository](https://github.com/or1z/json-validator-web)

## License

This project is open source and available under the MIT License.
