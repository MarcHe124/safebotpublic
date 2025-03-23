import streamlit as st


# Main Page Content
st.title("PFIZER ADVERSE EVENT REPORTING")

# Country & Language Selection
st.markdown("""
    <style>
    .selection-container {
        width: 100%;
        margin: 20px auto;
        padding: 20px;
        background: white;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .selection-select {
        width: 100%;
        padding: 8px;
        margin: 10px 0;
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    .required-field {
        color: red;
        font-size: 12px;
        margin-top: 5px;
    }
    </style>
    <div class="selection-container">
        <p>Please select the following to continue:</p>
        <select id="country" class="selection-select" required>
            <option value="">Select Country *</option>
            <option value="USA">USA</option>
            <option value="Canada">Canada</option>
            <option value="UK">UK</option>
            <option value="Germany">Germany</option>
            <option value="France">France</option>
        </select>
        <select id="language" class="selection-select" required>
            <option value="English">English</option>
            <option value="French">French</option>
            <option value="German">German</option>
            <option value="Spanish">Spanish</option>
        </select>
        <p class="required-field">* Required field</p>
    </div>
""", unsafe_allow_html=True)

# Handle the component value change
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if st.session_state.submitted:
    st.session_state.selected_country = st.session_state.country
    st.session_state.selected_language = st.session_state.language
    st.rerun()

st.markdown("""
    Whether you are a patient, caregiver, or healthcare professional, it is important to report adverse events for Pfizer products.  
    If you have a medical question/general enquiry on a Pfizer product, please visit  
    [https://www.pfizer.com/products/product-contact-information](https://www.pfizer.com/products/product-contact-information)  
    and choose your location.
""")

st.markdown("### Which best describes you?")

# CSS for Styling
st.markdown("""
    <style>
        .report-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
        }
        .report-card {
            width: 200px;
            background: white;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            text-align: center;
            padding-bottom: 15px;
            cursor: pointer;
            transition: 0.3s;
        }
        .report-card:hover {
            transform: scale(1.05);
        }
        .report-image {
            width: 100%;
            height: auto;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        }
        .report-title {
            font-size: 16px;
            font-weight: bold;
            color: #1A237E;
            margin-top: 5px;
        }
    </style>
    <style>
        .role-container {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin: 30px 0;
        }
        .role-card {
            flex: 1;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }
        .role-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
        }
        .role-image {
            width: 100%;
            object-fit: cover;
        }
        .role-title {
            padding: 15px;
            text-align: center;
            font-size: 16px;
            font-weight: 600;
            color: #1A237E;
        }
    </style>
    <div class="role-container">
        <form action="/Chatbot" method="get" style="flex: 1;">
            <input type="hidden" name="role" value="Patient">
            <button type="submit" class="role-card" style="width: 100%; border: none; background: none; padding: 0;">
                <img src="https://genaes.pfizersafetyreporting.com/images/patient.jpg?769020243a899b3fe0574666ad4c33aa" class="role-image" alt="Patient">
                <div class="role-title">Patient</div>
            </button>
        </form>
        <form action="/Chatbot" method="get" style="flex: 1;">
            <input type="hidden" name="role" value="Non-Healthcare Professional">
            <button type="submit" class="role-card" style="width: 100%; border: none; background: none; padding: 0;">
                <img src="https://genaes.pfizersafetyreporting.com/images/nhcp.jpg?58106498436426c9d329824135e992e0" class="role-image" alt="Non-Healthcare Professional">
                <div class="role-title">Non-Healthcare Professional</div>
            </button>
        </form>
        <form action="/Chatbot" method="get" style="flex: 1;">
            <input type="hidden" name="role" value="Healthcare Professional">
            <button type="submit" class="role-card" style="width: 100%; border: none; background: none; padding: 0;">
                <img src="https://genaes.pfizersafetyreporting.com/images/hcp.jpg?7579fb5793dbf0a27b313d20abefebed" alt="Healthcare Professional">
                <div class="role-title">Healthcare Professional</div>
            </button>
        </form>
        <form action="/Chatbot" method="get" style="flex: 1;">
            <input type="hidden" name="role" value="Pfizer Employee">
            <button type="submit" class="role-card" style="width: 100%; border: none; background: none; padding: 0;">
                <img src="https://genaes.pfizersafetyreporting.com/images/pfizer_employee.jpg?aa5cc0d5d59f3cf9df5c7f6859fde526" alt="Pfizer Employee">
                <div class="role-title">Pfizer Employee</div>
            </button>
        </form>
    </div>
""", unsafe_allow_html=True)

# Handle role selection
if 'user_type' not in st.session_state:
    st.session_state.user_type = None

