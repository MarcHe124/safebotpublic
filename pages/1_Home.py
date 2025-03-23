import streamlit as st



st.markdown("<h2 style='text-align: center; font-size: 28px;'>What would you like to report?</h2>", unsafe_allow_html=True)

# Inject CSS styles
st.markdown("""
    <style>
        .report-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
        }
        .report-card {
            width: 350px;
            background: white;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            text-align: center;
            padding-bottom: 20px;
        }
        .report-image {
            width: 100%;
            height: auto;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        }
        .report-text {
            padding: 20px;
            font-size: 16px;
            color: #333;
        }
        .report-title {
            font-size: 20px;
            font-weight: bold;
            color: #1A237E;
            margin-top: 5px;
        }
        .report-button {
            width: 80%;
            background-color: #0057B7;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            padding: 12px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
        }
        .report-button:hover {
            background-color: #003E8A;
        }
    </style>
""", unsafe_allow_html=True)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="report-card">
            <img src="https://www.pfizersafetyreporting.com/images/genaes_tile.jpg?361d42d2ffaac5f2c0e26d32bdf4b23d" class="report-image">
            <div class="report-text">
                <div>Adverse event associated with:</div>
                <div class="report-title">All Products</div>
                <form action="/Role_Selection" method="get">
                    <input type="submit" value="REPORT" class="report-button">
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="report-card">
            <img src="https://www.pfizersafetyreporting.com/images/csp_tile.jpg?88fa477249b5e5842c6f051be81589e8" class="report-image">
            <div class="report-text">
                <div>Adverse event reporting from:</div>
                <div class="report-title">Company Sponsored Programs</div>
                <form action="/Role_Selection" method="get">
                    <input type="submit" value="REPORT" class="report-button">
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)
