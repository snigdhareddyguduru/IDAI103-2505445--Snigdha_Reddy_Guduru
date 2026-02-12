# 🏋️ CoachBot AI – Smart Fitness Assistance Web Application

## CRS Artificial Intelligence – Generative AI Summative Assessment

**Student Name:** Snigdha Reddy Gudure  
**Candidate Registration Number:** 2505445  
**CRS Name:** Artificial Intelligence  
**Course Name:** Generative A.I  
**School Name:** [ENTER YOUR SCHOOL NAME HERE]  

---

# 1. Project Overview

CoachBot AI is a Generative AI-powered web application designed to provide personalized, structured, and injury-safe coaching guidance to youth athletes.

The system simulates a professional sports coach by dynamically generating:

- Position-specific workout plans  
- Injury-safe recovery programs  
- Tactical development strategies  
- 7-day nutrition guides  
- Hydration planning  
- Mental conditioning routines  
- Mobility and flexibility programs  
- Seasonal training roadmaps  

The application integrates OpenAI’s GPT-4o-mini model through a Python backend and is deployed using Streamlit Cloud.

---

# 2. Problem Statement

Many young athletes, particularly in under-resourced regions, lack access to:

- Certified professional coaching  
- Personalized training plans  
- Safe injury recovery guidance  
- Structured nutrition advice  
- Tactical development mentorship  

This gap results in:

- Increased injury risks  
- Improper conditioning  
- Poor match preparation  
- Slower long-term athletic development  

CoachBot AI addresses this challenge by democratizing access to intelligent coaching using Generative AI.

---

# 3. Research Foundations

The solution was designed based on core sports science principles:

## A. Position-Specific Conditioning
Each sport and position requires specialized training.
- A football striker requires acceleration and agility.
- A cricket fast bowler requires explosive power and joint care.
- A basketball point guard requires endurance and rapid decision-making.

## B. Youth Injury Risk Management
Common youth injuries include:
- Ankle sprains  
- Knee strain  
- Hamstring tightness  

Safe load adaptation and progressive training are essential.

## C. Nutrition & Recovery Science
Balanced macronutrients and hydration timing significantly influence performance and recovery.

## D. Mental Conditioning
Visualization routines and match-day preparation improve confidence and tactical awareness.

Generative AI enables dynamic personalization of these principles based on user inputs.

---

# 4. AI Model & Technical Architecture

**Model Used:** OpenAI GPT-4o-mini  
**Integration Method:** OpenAI Python SDK  
**Frontend Framework:** Streamlit  

## Backend Workflow
1. Athlete inputs collected  
2. Structured prompt generated  
3. API request sent to OpenAI  
4. AI-generated response formatted and displayed  
5. Prompt and model parameters shown for transparency  

---

# 5. Hyperparameter Tuning & Optimization

Extensive testing was conducted using different parameter configurations.

## Temperature Testing

| Temperature | Observed Output Behavior |
|------------|-------------------------|
| 0.3 | Conservative, structured, safety-focused |
| 0.5 | Balanced structure and creativity |
| 0.7 | Motivational and dynamic |
| 0.9 | Highly creative but slightly less precise |

**Max Tokens Tested:** 500 – 1200  

### Observations:
- Lower temperature produced safer recovery plans.
- Medium temperature balanced clarity and engagement.
- Higher temperature improved motivational tone.

Prompt refinements were implemented to:
- Enforce structured headings  
- Include safety instructions  
- Maintain age-appropriate guidance  
- Improve tactical clarity  

---

# 6. Core Features Implemented (10)

1. Position-Based Weekly Workout Generator  
2. Injury-Safe Recovery Training Plan  
3. Tactical Skill Development Guide  
4. Sport-Specific Warm-Up & Cooldown Routine  
5. 7-Day Nutrition Planner  
6. Hydration & Electrolyte Strategy  
7. Mental Conditioning & Visualization Routine  
8. Match-Day Tactical Strategy Guide  
9. Mobility & Flexibility Routine  
10. Seasonal / Pre-Season Training Roadmap  

Each feature dynamically constructs prompts using athlete profile inputs.

---

# 7. Prompt Engineering Strategy

Prompts were carefully engineered using:

- Age  
- Sport  
- Position  
- Injury history  
- Training goal  
- Diet preference  
- Safety instructions  
- Formatting constraints  

### Example Prompt Structure

```
You are a certified youth sports coach.

Athlete Details:
Age: 15
Sport: Football
Position: Striker
Injury History: Mild ankle sprain
Goal: Improve agility
Diet: Vegetarian

Generate a structured weekly workout plan.
Ensure injury-safe exercises.
Provide safety precautions.
Use clear headings and bullet points.
```

Prompt iterations improved personalization, injury awareness, and structural clarity.

---

# 8. Model Validation & Testing

Validation included:

- Testing across multiple sports  
- Injury edge case simulations  
- Position variation testing  
- Temperature comparison outputs  
- Output structure consistency checks  

Optimization steps:
- Added injury safety directives  
- Refined instruction clarity  
- Adjusted temperature per feature type  
- Improved tactical explanation depth  

---

# 9. Live Application Deployment

## Streamlit Cloud App Link
👉 https://snigdha-coachbot.streamlit.app/

The application was deployed using Streamlit Cloud and connected securely to the OpenAI API using environment variables.

---

# 10. Video Demonstration Evidence

Project Demonstration Video:  
https://drive.google.com/drive/folders/1Tzw2e9BAQlnfPGsm6jR5L1pvMgXUf2MF?usp=sharing

The video demonstrates:

- User input process  
- Feature selection  
- Prompt generation  
- Output comparison across temperature settings  
- Injury-safe recovery case testing  
- Full application workflow  

---

# 11. Installation Guide (Local Execution)

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"
streamlit run app.py
```

---

# 12. Security Practices

- API key stored using environment variables  
- No API keys committed to GitHub  
- Streamlit Cloud secrets used for deployment  
- Secure credential handling  

---

# 13. Social Impact

CoachBot AI promotes:

- Accessible youth coaching  
- Injury prevention awareness  
- Tactical skill development  
- Nutrition education  
- Inclusive sports technology  

The system demonstrates how Generative AI can address real-world challenges in youth sports development.

---

# 14. Conclusion

CoachBot AI successfully integrates Generative AI with sports science principles to deliver personalized, safe, and structured athletic guidance.

This project demonstrates:

- Strong problem understanding  
- Advanced prompt engineering  
- Model integration and tuning  
- Validation and optimization  
- Functional web deployment  
- Professional documentation  

CoachBot AI reflects the transformative potential of Generative AI in modern sports technology.

---

**CoachBot AI © 2026 – Developed by Snigdha Reddy Gudure**
