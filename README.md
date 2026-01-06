# MuscleGuard

Streamlit demo app for the MuscleGuard training feedback concept. It shows product info, short demos, and a contact form that saves leads to `leads.csv`.

For cloning with Git:  
`git clone https://github.com/adandaxa/MuscleGuard.git` then follow the steps below from “go to the project folder.”

## Requirements
- Python 3.9+ installed
- Internet access to install dependencies on first run
- (Optional) Git if you want to clone instead of downloading a ZIP

## macOS: run the app
1) Open Terminal  
2) Go to the project folder  
3) Create and activate a virtual environment (recommended)  
`python3 -m venv .venv`  
`source .venv/bin/activate`
4) Install dependencies  
`pip install -r requirements.txt`
5) Start the app  
`streamlit run app.py`
6) Open the URL that Streamlit prints (usually http://localhost:8501).

## Windows (PowerShell): run the app
1) Open PowerShell  
2) Go to the project folder  
`cd C:\Users\<you>\Downloads\MuscleGuard`
3) Create and activate a virtual environment (recommended)  
`python -m venv .venv`  
`.\.venv\Scripts\Activate`
4) Install dependencies  
`pip install -r requirements.txt`
5) Start the app  
`streamlit run app.py`
6) Open the URL that Streamlit prints (usually http://localhost:8501).

## Stopping and cleanup
- Stop the app: press `Ctrl+C` in the terminal window running Streamlit.
- Leave the virtual environment: type `deactivate`.

## Notes
- The contact form appends submissions to `leads.csv` in the project root. Keep that file if you want to preserve collected leads; add it to `.gitignore` if you don’t want to commit user data.
- Background image and demo videos live in `assets/`; keep paths intact so the UI renders correctly.
