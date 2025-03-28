import streamlit as st
import pandas as pd

# Streamlit App Title
st.title("📊 Smart Data Insights Dashboard")

# File Upload Section
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"], key="file_uploader")

# State management to track file upload
if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = False

# Check if a file is uploaded
if uploaded_file:
    try:
        # Read Excel File
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.session_state.file_uploaded = True  # Mark as uploaded

        # Success message
        st.success("✅ File Uploaded Successfully!")

        # Display Data Overview
        st.subheader("📊 Dataset Overview")

        # Total Rows & Columns
        st.write(f"**Total Rows × Columns:** {df.shape[0]} × {df.shape[1]}")

        # Missing Data Percentage
        total_missing = df.isnull().sum().sum()
        missing_percent = (total_missing / df.size) * 100
        st.write(f"**Missing Data:** {missing_percent:.2f}% of total data")

        # Duplicate Entries
        duplicate_count = df.duplicated().sum()
        st.write(f"**Duplicate Rows:** {duplicate_count}")

        # Statistical Summary
        st.subheader("📈 Quick Statistics for Numerical Columns")
        st.write(df.describe())

        # Remove File Button
        if st.button("❌ Remove File"):
            st.session_state.file_uploaded = False
            st.experimental_rerun()  # Refresh the page

    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

# Show upload option again if file is removed
if not st.session_state.file_uploaded:
    st.warning("Upload a file to proceed.")
