import streamlit as st
from openai import OpenAI
from datetime import datetime

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="CoachBot AI",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ CoachBot AI - Smart Fitness Assistant")
st.markdown("AI-powered personalized coaching for youth athletes")

# ===============================
# OPENAI CONFIGURATION
# ===============================
client = OpenAI(api_key="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")  # <-- Replace this

# ===============================
# SIDEBAR SETTINGS
# ===============================
st.sidebar.header("⚙️ Model Settings")

temperature = st.sidebar.slider(
    "Creativity Level (Temperature)",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Max Output Tokens",
    min_value=300,
    max_value=1500,
    value=800,
    step=100
)

st.sidebar.info("""
Lower temperature → Safer, structured plans  
Higher temperature → Creative, motivational responses  
""")

# ===============================
# USER INPUT SECTION
# ===============================
st.header("📋 Athlete Profile")

col1, col2 = st.columns(2)

with col1:
    sport = st.selectbox(
        "Select Sport",
        ["Football", "Cricket", "Basketball", "Athletics", "Badminton", "Tennis"]
    )

    position = st.text_input("Position (e.g., Striker, Fast Bowler, Point Guard)")
    age = st.number_input("Age", min_value=10, max_value=40, value=15)

with col2:
    injury = st.text_input("Injury History (if any)")
    goal = st.selectbox(
        "Training Goal",
        [
            "Build Strength",
            "Increase Stamina",
            "Improve Agility",
            "Post-Injury Recovery",
            "Tactical Improvement",
            "Pre-Season Conditioning"
        ]
    )
    diet = st.selectbox(
        "Diet Preference",
        ["Vegetarian", "Non-Vegetarian", "Vegan", "No Preference"]
    )

# ===============================
# FEATURE SELECTION
# ===============================
st.header("🎯 Choose Coaching Feature")

feature = st.selectbox(
    "Select Feature",
    [
        "Position-Based Workout Plan",
        "Injury-Safe Recovery Program",
        "Tactical Skill Development",
        "Warm-Up & Cooldown Routine",
        "7-Day Nutrition Plan",
        "Hydration & Electrolyte Strategy",
        "Mental Conditioning Routine",
        "Match-Day Strategy Guide",
        "Mobility & Flexibility Routine",
        "Seasonal Training Plan"
    ]
)

# ===============================
# PROMPT BUILDER
# ===============================
def build_prompt():
    base_context = f"""
You are a certified professional youth sports coach and sports science expert.

Athlete Details:
Age: {age}
Sport: {sport}
Position: {position}
Injury History: {injury}
Goal: {goal}
Diet Preference: {diet}

Instructions:
- Provide structured headings.
- Ensure safety for injury conditions.
- Give clear bullet points.
- Be motivational but realistic.
"""

    feature_prompts = {
        "Position-Based Workout Plan": "Generate a detailed weekly workout plan tailored to the athlete's position.",
        "Injury-Safe Recovery Program": "Create a safe recovery training schedule considering the injury.",
        "Tactical Skill Development": "Provide tactical drills and positional improvement strategies.",
        "Warm-Up & Cooldown Routine": "Design a complete warm-up and cooldown routine.",
        "7-Day Nutrition Plan": "Generate a structured 7-day meal plan.",
        "Hydration & Electrolyte Strategy": "Provide hydration and electrolyte recommendations.",
        "Mental Conditioning Routine": "Create a mental focus and visualization routine.",
        "Match-Day Strategy Guide": "Provide a match-day tactical preparation guide.",
        "Mobility & Flexibility Routine": "Generate mobility and flexibility exercises.",
        "Seasonal Training Plan": "Design a structured seasonal training roadmap."
    }

    return base_context + "\n\n" + feature_prompts[feature]

# ===============================
# GENERATE RESPONSE
# ===============================
def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional youth sports coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# ===============================
# BUTTON
# ===============================
if st.button("🚀 Generate Coaching Plan"):

    if not position:
        st.warning("Please enter position for better personalization.")
    else:
        with st.spinner("Generating AI Coaching Plan..."):
            prompt = build_prompt()
            output = generate_response(prompt)

        st.markdown("## 📊 AI Coaching Output")
        st.markdown(output)

        st.success("Plan Generated Successfully!")

        with st.expander("📂 View Prompt Used"):
            st.code(prompt)

        with st.expander("⚙️ Model Parameters Used"):
            st.write(f"Temperature: {temperature}")
            st.write(f"Max Tokens: {max_tokens}")
            st.write(f"Generated On: {datetime.now()}")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.markdown("Developed for CRS Generative AI Summative Assessment")
st.markdown("CoachBot AI © 2026")


