# MuscleGuard

Streamlit demo app for the MuscleGuard training feedback concept. It shows product info, short demos, and a contact form that saves leads to `leads.csv`.

## Requirements
- Python 3.9+ installed
- Internet access to install dependencies on first run
- (Optional) Git if you want to clone instead of downloading a ZIP

## Run via Git clone (recommended)
If you want the latest code and easy updates:
- macOS / Linux
  1) Open Terminal  
  2) Choose a folder to put the project in, e.g. `cd ~/Downloads`  
  3) Clone: `git clone https://github.com/<your-username>/MuscleGuard.git`  
  4) Enter the folder: `cd MuscleGuard`  
  5) Create & activate a venv:  
     `python3 -m venv .venv`  
     `source .venv/bin/activate`  
  6) Install deps: `pip install -r requirements.txt`  
  7) Run: `streamlit run app.py`
- Windows (PowerShell)
  1) Open PowerShell  
  2) Choose a folder, e.g. `cd $HOME\\Downloads`  
  3) Clone: `git clone https://github.com/<your-username>/MuscleGuard.git`  
  4) Enter the folder: `cd MuscleGuard`  
  5) Create & activate a venv:  
     `python -m venv .venv`  
     `.\\.venv\\Scripts\\Activate`  
  6) Install deps: `pip install -r requirements.txt`  
  7) Run: `streamlit run app.py`
After `streamlit` starts, open the URL it prints (usually http://localhost:8501).

If you downloaded a ZIP instead of cloning, follow the OS-specific steps below.

## macOS: run the app
1) Open Terminal  
2) Go to the project folder (for example)  
`cd /Users/<you>/Downloads/MuscleGuard`  
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

