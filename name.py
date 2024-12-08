import google.generativeai as genai
import streamlit as st

# Set up API Key (replace with your actual API key for Google Generative AI)
api_key = "AIzaSyAvJZUwWbs1PKcnhEQm89SaeIF3CDbNv80"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to generate recommendations based on user input
def get_event_recommendations(event_type, date, location, guest_count, budget, special_requirements):
    # Format the prompt based on user inputs
    prompt = f"""
    You are an expert event planner. Help plan a {event_type}.
    Here are the event details:
    - Date: {date}
    - Location: {location}
    - Number of Guests: {guest_count}
    - Budget: {budget}
    - Special Requirements: {special_requirements}

    Provide recommendations for the following:
    1. Venue options
    2. Catering ideas
    3. Entertainment suggestions
    4. Decoration and theme ideas
    5. Logistic suggestions (transportation, accommodations)
    6. Budget optimization tips
    """

    # Call the API to get a response
    response = model.generate_content(prompt)

    
    # Extract and return the response text
    return response.text

# Streamlit App Layout
st.title("Event Planner with AI (Google Generative AI)")

st.sidebar.header("Event Details")
event_type = st.sidebar.selectbox("Event Type", ["Wedding", "Party", "Conference", "Birthday", "Other"])
date = st.sidebar.date_input("Event Date")
location = st.sidebar.text_input("Location (City or Venue)")
guest_count = st.sidebar.number_input("Guest Count", min_value=1, step=1)
budget = st.sidebar.number_input("Budget (USD)", min_value=100, step=100)
special_requirements = st.sidebar.text_area("Special Requirements (optional)")

if st.sidebar.button("Generate Recommendations"):
    # Display loading spinner while getting recommendations
    with st.spinner("Planning your event..."):
        recommendations = get_event_recommendations(event_type, date, location, guest_count, budget, special_requirements)
    
    # Display recommendations
    st.subheader("Event Recommendations")
    st.write(recommendations)

    # Option to save or export recommendations
    if st.button("Save Recommendations as Text"):
        with open("event_recommendations.txt", "w") as f:
            f.write(recommendations)
        st.success("Recommendations saved as event_recommendations.txt")

# Example Usage Instructions
st.markdown("""
*How to Use This App:*
1. Fill in your event details in the sidebar.
2. Click "Generate Recommendations" to see AI-powered event planning suggestions.
3. Save the recommendations by clicking "Save Recommendations as Text."
""")