import streamlit as st
from agency import Agency  # Assuming the Agency class is defined as per your project's specifics

# Initialize the Agency class (adapt initialization as needed based on your script's logic)
agency = Agency()

# Streamlit UI setup
st.title("Agency Chatbot")

# Dropdown to select the recipient agent
recipient_agents = [agent.name for agent in agency.main_recipients]  # Assuming agency.main_recipients lists all agents
selected_agent_name = st.selectbox("Select Recipient Agent:", recipient_agents)

# Input for user message
user_message = st.text_area("Enter your message here:")

# File uploader
uploaded_files = st.file_uploader("Attach files", accept_multiple_files=True)

# Send button
send_button = st.button("Send")

if send_button:
    # Process and upload files, assuming agency has a method to handle this
    # This is a simplified example; adapt it based on your actual file handling logic
    uploaded_file_ids = [agency.upload_file(file) for file in uploaded_files] if uploaded_files else []

    # Sending the message and getting a response
    # Assuming get_completion can be adapted for synchronous operation in Streamlit
    response = agency.get_completion(
        message=user_message,
        message_files=uploaded_file_ids,
        recipient_agent=selected_agent_name,
        yield_messages=False  # Assuming adaptation for synchronous response
    )

    # Displaying the agent's response
    st.text_area("Response:", value=response, height=300, disabled=True)
