import streamlit as st
from google import genai
from google.genai import types
import json

# 1. Initialize Gemini Client (Ensure GEMINI_API_KEY is set in your environment variables)
# For Streamlit, you can set it via st.secrets or local env
client = genai.Client()

# 2. Define the Mock API Tool
def register_volunteer(name: str, email: str, interest_area: str) -> str:
    """
    Registers a new volunteer into the NayePankh Foundation database.
    Use this tool ONLY when a user explicitly expresses a desire to join or volunteer.
    """
    # Simulating an API call
    mock_db_entry = {
        "status": "Success",
        "volunteer_id": "NP-2026-XYZ",
        "data": {"name": name, "email": email, "interest": interest_area}
    }
    return f"Successfully registered {name} in the NayePankh database! ID: {mock_db_entry['volunteer_id']}."

# 3. Streamlit UI Setup
st.set_page_config(page_title="PankhAssist Agent", page_icon="🌱")
st.title("🌱 PankhAssist: NayePankh AI Agent")
st.caption("A smart workflow designed to assist NayePankh Foundation volunteers and donors.")

# 4. Initialize Session State (Chat Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []
    # System instructions to give the agent its persona and knowledge base
    st.session_state.system_instruction = """
    You are PankhAssist, an enthusiastic AI Agent for NayePankh Foundation (an NGO).
    Your goal is to welcome users, answer queries about the NGO, and help them register as volunteers.
    
    NGO Info:
    - Mission: To empower youth, support underprivileged children, and drive social change.
    - Focus Areas: Education, health, and women empowerment.
    
    Be extremely polite, encouraging, and warm. 
    If someone wants to volunteer, use the `register_volunteer` tool to register them. Ask for their name, email, and interest area if they haven't provided it.
    """

# Display chat history from memory
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input & Agent Execution Loop
if user_input := st.chat_input("How can I help NayePankh Foundation today?"):
    # Render user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Format history for the API
    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    # Configure the Agent with tools and system instructions
    config = types.GenerateContentConfig(
        system_instruction=st.session_state.system_instruction,
        tools=[register_volunteer], # Connecting the API tool
        temperature=0.7
    )

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # Call the Gemini Model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contents,
            config=config
        )
        
        # Handle Function/Tool Calling automatically if triggered
        if response.function_calls:
            for call in response.function_calls:
                if call.name == "register_volunteer":
                    # Extract arguments passed by the model
                    args = call.args
                    # Execute the local python function (The Mock API)
                    api_result = register_volunteer(
                        name=args.get("name", "Unknown"),
                        email=args.get("email", "Not provided"),
                        interest_area=args.get("interest_area", "General")
                    )
                    
                    # Provide the tool output back to the model to get a final natural response
                    # For simplicity in a basic prototype, we can also display the result directly:
                    agent_final_text = f"⚙️ *[Agent Action: Tool Triggered]*\n\n{api_result}\n\n Thank you for stepping forward to make a change!"
                    response_placeholder.markdown(agent_final_text)
        else:
            # Regular text response
            agent_final_text = response.text
            response_placeholder.markdown(agent_final_text)
            
        # Save Agent response to memory
        st.session_state.messages.append({"role": "assistant", "content": agent_final_text})