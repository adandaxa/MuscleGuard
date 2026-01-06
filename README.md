# MuscleGuard

Streamlit demo app for the MuscleGuard training feedback concept. It shows product info, short demos, and a contact form that saves leads to `leads.csv`.

## Quickstart
1) Go to the project folder  
`cd /Users/adandaxa/Downloads/MuscleGuard`

2) (Recommended) Create & activate a virtual environment  
`python3 -m venv .venv`  
`source .venv/bin/activate`

3) Install dependencies  
`pip install -r requirements.txt`

4) Run the app  
`streamlit run app.py`

5) Open the URL that Streamlit prints (usually http://localhost:8501).

## Notes
- The contact form appends submissions to `leads.csv` in the project root. Keep that file if you want to preserve collected leads.
- Background image and demo videos are in `assets/`; keep those paths intact so the UI renders correctly.
- To stop the app, press `Ctrl+C` in the terminal. To leave the virtual env, run `deactivate`.

