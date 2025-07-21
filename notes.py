import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
# Configure generative AI model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are a student tutor. Your task is to create optimized notes for different subjects and topics based on student needs. Each set of notes should be concise, clear, and tailored to the specific subject and level of understanding."
)

def generate_notes(topic, complexity):
    try:
        # Adjust prompt based on complexity
        if complexity == "hard":
            prompt = f"Generate advanced notes on {topic}. Title: {topic}. Overview: Provide an in-depth overview of {topic}. Description: Dive deep into {topic} with detailed explanations. Summary: Provide a comprehensive summary of {topic}."
        elif complexity == "smart":
            prompt = f"Generate smart notes on {topic}. Title: {topic}. Overview: Give a smart overview of {topic}. Description: Provide intelligent insights into {topic}. Summary: Summarize smartly about {topic}."
        elif complexity == "simple":
            prompt = f"Generate simple notes on {topic}. Title: {topic}. Overview: Give a simple overview of {topic}. Description: Describe {topic} in simple terms. Summary: Summarize key points about {topic} simply."

        # Generate the notes using the generative model
        response = model.generate_content(prompt)
        notes_text = response.text

        # Basic formatting (you can enhance this)
        notes = notes_text.strip()  # Remove leading/trailing whitespace

        return notes

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app definition
def main():
    st.title("Structured Notes Generator")
    st.write("This app generates structured notes based on a provided topic and complexity level.")

    # Input fields for user to enter the topic and complexity
topic = st.text_input("Enter the topic for structured notes:")
complexity = st.selectbox("Select complexity level:", ["hard", "smart", "simple"])

    # Button to trigger note generation
if st.button("Generate Notes"):
        # Check if topic is provided
    if topic:
            # Generate the structured notes based on the selected complexity
        notes = generate_notes(topic, complexity)
        if notes:
            st.subheader(f"Structured Notes on '{topic}' (Complexity: {complexity}):")
            st.write(notes)
        else:
            st.warning("Failed to generate notes. Please try again.")
    else:
            st.warning("Please enter a topic.")

if __name__ == "_main_":
    main()
