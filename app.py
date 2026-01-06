import os
import base64
from datetime import datetime

import pandas as pd
import streamlit as st

# ================== CONFIG ==================
st.set_page_config(page_title="MuscleGuard", page_icon="💪", layout="wide")

LEADS_FILE = "leads.csv"

BG_IMAGE_PATH = "assets/images/bg.png"

VIDEOS = [
    ("🏋️ Strength Training", "assets/videos/demo_muscleguard.mp4"),
    ("🏃 Endurance / Repetitive Movement", "assets/videos/demo_muscleguard2.mp4"),
    ("🤸 Training Under Load", "assets/videos/demo_muscleguard3.mp4"),
]


# ================== THEME (BACKGROUND + UI) ==================
def _img_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def apply_theme_with_bg(bg_path: str):
    if os.path.exists(bg_path):
        bg_b64 = _img_to_base64(bg_path)
        bg_css = f'url("data:image/png;base64,{bg_b64}")'
    else:
        bg_css = "none"

    st.markdown(
        f"""
        <style>
        /* Hide sidebar completely */
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{
            display: none !important;
        }}

        /* Background */
        .stApp {{
            background:
                linear-gradient(90deg, rgba(5,8,18,0.94) 0%, rgba(5,8,18,0.75) 45%, rgba(5,8,18,0.35) 100%),
                radial-gradient(1200px 650px at 18% 18%, rgba(122,162,255,0.16), transparent 60%),
                radial-gradient(900px 550px at 85% 25%, rgba(90,220,180,0.10), transparent 55%),
                {bg_css};
            background-size: cover;
            background-position: right center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #e9edf7;
        }}

        /* Main content width */
        section.main > div {{
            max-width: 1250px;
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }}

        /* Card style */
        .card {{
            background: linear-gradient(180deg, rgba(255,255,255,0.11), rgba(255,255,255,0.04));
            border: 1px solid rgba(255,255,255,0.16);
            border-radius: 22px;
            padding: 24px 26px;
            box-shadow:
                0 18px 40px rgba(0,0,0,0.45),
                inset 0 1px 0 rgba(255,255,255,0.08);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
        }}

        /* Small muted text */
        .muted {{
            color: rgba(233,237,247,0.78);
            font-size: 0.98rem;
            line-height: 1.55;
        }}

        /* Section headers */
        .section-title {{
            margin-top: 0.3rem;
            margin-bottom: 0.2rem;
            font-weight: 750;
            letter-spacing: 0.2px;
        }}

        /* Top nav buttons */
        .nav button {{
            width: 100%;
            border-radius: 999px !important;
            padding: 0.72rem 1.1rem !important;
            border: 1px solid rgba(255,255,255,0.20) !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.18), rgba(255,255,255,0.07)) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            box-shadow: 0 8px 20px rgba(0,0,0,0.35);
        }}
        .nav button:hover {{
            background: linear-gradient(180deg, rgba(255,255,255,0.30), rgba(255,255,255,0.10)) !important;
            transform: translateY(-1px);
        }}

        /* Active nav button */
        .nav-active button {{
            border: 1px solid rgba(122,162,255,0.55) !important;
            background: linear-gradient(180deg, rgba(122,162,255,0.32), rgba(255,255,255,0.08)) !important;
        }}

        /* Inputs */
        .stTextInput input, .stTextArea textarea {{
            border-radius: 14px !important;
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.18) !important;
            color: #ffffff !important;
        }}

        /* Primary CTA buttons (inside pages) */
        div.stButton > button {{
            border-radius: 999px !important;
            padding: 0.70rem 1.1rem !important;
            font-weight: 700 !important;
        }}

        /* Reduce extra spacing */
        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


apply_theme_with_bg(BG_IMAGE_PATH)


# ================== NAV STATE ==================
if "page" not in st.session_state:
    st.session_state.page = "Home"


def go(page_name: str):
    st.session_state.page = page_name


# ================== TOP NAV ==================
st.markdown("<div class='card'>", unsafe_allow_html=True)

n1, n2, n3, n4 = st.columns(4)


def nav_button(col, label, page_name):
    active_class = "nav-active" if st.session_state.page == page_name else "nav"
    with col:
        st.markdown(f"<div class='{active_class}'>", unsafe_allow_html=True)
        if st.button(label, use_container_width=True):
            go(page_name)
        st.markdown("</div>", unsafe_allow_html=True)


nav_button(n1, "Home", "Home")
nav_button(n2, "About", "About")
nav_button(n3, "Demo", "Demo")
nav_button(n4, "Contact", "Contact")

st.markdown("</div>", unsafe_allow_html=True)
st.write("")


# ================== PAGES ==================
def page_home():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    left, right = st.columns([1.35, 1])

    # ---------- LEFT: TEXT ----------
    with left:
        st.title("💪 MuscleGuard")
        st.subheader("Real-time training feedback to help prevent muscle overload.")

        st.markdown(
            """
<div class="muted">
MuscleGuard is a smart sleeve concept designed to support safer, more consistent training by spotting signs of overload early and giving you clear feedback during the workout.
<br><br>
Instead of realizing you pushed too hard only after pain appears, you get an early signal when it’s time to slow down, adjust, or rest — so you can keep training without unnecessary setbacks.
</div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        st.markdown("#### How it works")
        st.markdown(
            """
- You wear the sleeve during training  
- It monitors muscle effort and strain patterns  
- You receive simple signals when overload risk rises  
            """
        )

        st.write("")
        st.markdown("#### Who it’s for")
        st.markdown(
            """
- Gym & strength training  
- Repetitive movement sports (running, cycling, etc.)  
- People returning after injury or long breaks  
- Anyone who tends to “push through pain”  
            """
        )

        st.write("")
        st.markdown("#### What you’ll get from it")
        b1, b2, b3 = st.columns(3)
        with b1:
            st.markdown(
                """
<div class="card" style="padding:16px 16px; border-radius:18px;">
<b>Early warnings</b><br>
<span class="muted">Know when overload is rising—before it becomes a problem.</span>
</div>
                """,
                unsafe_allow_html=True,
            )
        with b2:
            st.markdown(
                """
<div class="card" style="padding:16px 16px; border-radius:18px;">
<b>Smarter decisions</b><br>
<span class="muted">Adjust form, pace, or rest with confidence in the moment.</span>
</div>
                """,
                unsafe_allow_html=True,
            )
        with b3:
            st.markdown(
                """
<div class="card" style="padding:16px 16px; border-radius:18px;">
<b>Consistency</b><br>
<span class="muted">Reduce setbacks and stay on track with your training plan.</span>
</div>
                """,
                unsafe_allow_html=True,
            )

        st.write("")
        st.markdown("#### Quick questions (FAQ)")
        st.markdown(
            """
**Does it replace a coach or doctor?**  
No — it’s meant to support day-to-day training decisions, not diagnose medical conditions.

**Will it distract me during workouts?**  
The goal is simple, minimal feedback — quick signals when something needs attention.

**What kind of feedback will I get?**  
Clear alerts that suggest *slow down, adjust, or rest* when overload risk increases.
            """
        )

        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🎥 Watch the demo", use_container_width=True):
                go("Demo")
        with c2:
            if st.button("✉️ Get updates", use_container_width=True):
                go("Contact")

    # ---------- RIGHT: VIDEO ----------
    with right:
        video_path = "assets/videos/demo_muscleguard3.mp4"

        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.warning("Demo video not found.")

        st.caption("Example scenario showing how early feedback can help reduce overload risk.")

    st.markdown("</div>", unsafe_allow_html=True)


def page_about():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("📘 About MuscleGuard")

    st.markdown(
        """
<div class="muted">
Training progress is built on consistency — but overload injuries can interrupt that progress for weeks or months.
MuscleGuard was designed to give people a clearer understanding of what their body is telling them during workouts.
</div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### The idea")
    st.markdown(
        """
MuscleGuard focuses on one simple goal:  
**help you recognize overload early — before it becomes an injury.**
"""
    )

    st.write("")
    a1, a2 = st.columns(2)

    with a1:
        st.markdown("### What makes it different")
        st.markdown(
            """
- Feedback happens **during** the workout  
- Signals are designed to be easy to understand  
- A prevention-first approach (not a recovery tool)  
            """
        )

    with a2:
        st.markdown("### What we’re building for users")
        st.markdown(
            """
- A sleeve that feels comfortable and lightweight  
- Feedback you can trust (clear, not overwhelming)  
- A smooth experience that fits any training style  
            """
        )

    st.write("")
    st.markdown("### Who it’s for")
    st.markdown(
        """
MuscleGuard is for anyone who trains regularly and wants to reduce unnecessary injury risk —  
from beginners learning good habits to athletes pushing their limits.
"""
    )

    st.markdown("</div>", unsafe_allow_html=True)


def page_demo():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("🎥 Demo")
    st.markdown(
        """
These short videos show example training scenarios where real-time feedback could help reduce overload risk.
"""
    )

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    for title, path in VIDEOS:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(title)

        if os.path.exists(path):
            st.video(path)
        else:
            st.warning(f"Video not found: {path}")

        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(
        """
Want to hear when we add more scenarios and updates?
"""
    )
    if st.button("✉️ Get updates", use_container_width=True):
        go("Contact")
    st.markdown("</div>", unsafe_allow_html=True)


def page_contact():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("✉️ Get updates")
    st.markdown(
        """
Leave your details and we’ll send updates about MuscleGuard.
"""
    )

    with st.form("contact_form"):
        first = st.text_input("First name")
        last = st.text_input("Last name")
        email = st.text_input("Email")
        message = st.text_area("Message (optional)")
        consent = st.checkbox("I agree to be contacted about MuscleGuard")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not (first and last and email and consent):
            st.error("Please enter first name, last name, email, and consent.")
        else:
            row = {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "first_name": first.strip(),
                "last_name": last.strip(),
                "email": email.strip(),
                "message": (message or "").strip(),
            }
            df_new = pd.DataFrame([row])

            if os.path.exists(LEADS_FILE):
                df_old = pd.read_csv(LEADS_FILE)
                df = pd.concat([df_old, df_new], ignore_index=True)
            else:
                df = df_new

            df.to_csv(LEADS_FILE, index=False)
            st.success("Thanks! ✅ We’ll keep you updated.")

    st.markdown("</div>", unsafe_allow_html=True)


# ================== ROUTER ==================
if st.session_state.page == "Home":
    page_home()
elif st.session_state.page == "About":
    page_about()
elif st.session_state.page == "Demo":
    page_demo()
elif st.session_state.page == "Contact":
    page_contact()
