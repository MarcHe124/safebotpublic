import json
import random
import streamlit as st
import agent


st.title("💬 Report Generation Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OracleAI")

# Initialize agent and messages in session state
if "agent" not in st.session_state:
    st.session_state.agent = agent.SafetyAgent()

if "messages" not in st.session_state:
    # Get initial message from agent
    initial_response = st.session_state.agent(None)
    st.session_state.messages = [{"role": "assistant", "content": initial_response}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Get response from agent
        agent_response = st.session_state.agent(prompt)
        st.session_state.json_response = None

        st.session_state.messages.append({"role": "assistant", "content": agent_response})
        st.chat_message("assistant").write(agent_response)
    except StopIteration as data:
        msg = data.value
        st.session_state.json_response = msg
        
        summary_msg = "📋 Report Summary\n\n"
        
        # Format personal information
        demo_data = msg['demo']
        summary_msg += "👤 Personal Information\n\n"
        summary_msg += f"  Name: {demo_data['name']}\n\n"
        summary_msg += f"  Age: {demo_data['age']}\n\n"
        summary_msg += f"  Gender: {demo_data['gender']}\n\n"
        summary_msg += f"  Initial: {demo_data['initial']}\n\n"
        
        # Format adverse event information
        ae_data = msg['ae']
        summary_msg += "🏥 Adverse Event\n\n"
        summary_msg += f"  Event: {ae_data['event']}\n\n"
        summary_msg += f"  Onset: {ae_data['onset']}\n\n"
        summary_msg += f"  Duration: {ae_data['duration']}\n\n"



        ### another template for input
        # {'fullname': 'Jethalal Gada', 'dob': 'Feb 20, 2000', 'age': '25 years', 'events': ['backpain', 'itchy eyes'],
        #  'event_details': [{'onset': 'February 20, 2022', 'duration': '5 days', 'outcome': 'recovered'},
        #                    {'onset': 'February 22, 2022', 'duration': '5 days', 'outcome': 'recovered'}],
        #  'products': ['Topomax', 'Tylenol'], 'product_details': [
        #     {'dose': '2', 'dose_unit': 'mg', 'start_date': 'February 20, 2020', 'end_date': 'February 22, 2021',
        #      'frequency': 'Once a week.'},
        #     {'dose': '5', 'dose_unit': 'mg', 'start_date': 'February 22, 2023', 'end_date': 'February 22, 2024',
        #      'frequency': 'twice daily'}], 'gender': 'male'}

        # parsed_json = json.loads(msg)
        # st.session_state.json_response = parsed_json

        # summary_msg = "📋 Report Summary\n\n"
        # summary_msg += "👤 Personal Information\n\n"
        # summary_msg += f"  Full Name: {parsed_json['fullname']}\n\n"
        # summary_msg += f"  Date of Birth: {parsed_json['dob']}\n\n"
        # summary_msg += f"  Age: {parsed_json['age']}\n\n"
        # summary_msg += f"  Gender: {parsed_json['gender']}\n\n"

        # summary_msg += "🏥 Medical Events\n\n"
        # for i, (event, detail) in enumerate(zip(parsed_json['events'], parsed_json['event_details'])):
        #     summary_msg += f"Event {i+1}: {event}\n"
        #     summary_msg += f"  - Onset: {detail['onset']}\n"
        #     summary_msg += f"  - Duration: {detail['duration']}\n"
        #     summary_msg += f"  - Outcome: {detail['outcome']}\n"
        # summary_msg += "\n"

        # summary_msg += "💊 Product Information\n\n"
        # for i, (product, detail) in enumerate(zip(parsed_json['products'], parsed_json['product_details'])):
        #     summary_msg += f"Product {i+1}: {product}\n"
        #     summary_msg += f"  - Dosage: {detail['dose']} {detail['dose_unit']}\n"
        #     summary_msg += f"  - Frequency: {detail['frequency']}\n"
        #     summary_msg += f"  - Start Date: {detail['start_date']}\n"
        #     summary_msg += f"  - End Date: {detail['end_date']}\n"
        
        st.session_state.messages.append({"role": "assistant", "content": summary_msg})
        st.chat_message("assistant").write(summary_msg)

        with st.chat_message("assistant"):
            st.write("Ready to submit to generate report?")
            if st.button("Submit"):
                st.success("Report submitted successfully!")



