# Autogen Repository

This repository contains Jupyter Notebooks and code for various automation and inference tasks. The sensitive API keys have been replaced with placeholders and are expected to be stored securely in a `.env` file.

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Environment Creation](#environment-creation)
3. [Usage](#usage)
4. [Files](#files)
5. [Contributing](#contributing)

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sideshsundar/Autogen.git
   cd Autogen
   ```

2. **Create a Python Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File:**
   - Add the following to a `.env` file in the root directory:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     ```

5. **Sanity Check:**
   - Run the notebooks to ensure the setup is correct.

---

## Environment Creation

This repository uses `python-dotenv` to manage environment variables securely. Follow these steps:

1. Install `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```

2. Load the `.env` file in your Python scripts or notebooks as follows:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()

   OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
   ```

---

## Usage

1. Open the desired notebook in Jupyter:
   ```bash
   jupyter notebook
   ```

2. Replace placeholder API keys with values from the `.env` file as shown in the examples above.

---

## Files

- **`basic.ipynb`**: Basic automation tasks.
- **`code execution.ipynb`**: Code execution workflows.
- **`DOCKER_AUTOGEN.ipynb`**: Docker-related automation.
- **`Enhanced inference.ipynb`**: Enhanced inference mechanisms.
- **`groupchat.ipynb`**: Group chat automation.
- **`openai.ipynb`**: OpenAI API interactions.

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes and create a pull request.

Ensure all API keys are removed before committing to avoid push protection errors.

---

Feel free to explore and improve the project!
