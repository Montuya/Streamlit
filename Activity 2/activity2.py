import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(page_title="Excel DataFrame Viewer", page_icon="📊", layout="centered")

# Title and instructions
st.title("📊 Excel DataFrame Viewer")
st.markdown("Upload an `.xlsx` Excel file with at least **5 columns** to view and filter its data interactively.")

# File uploader
uploaded_file = st.file_uploader("📁 Upload your Excel file here", type=["xlsx"])

# Handle uploaded file
if uploaded_file is not None:
    try:
        # Try loading the Excel file
        data = pd.read_excel(uploaded_file)

        # Check column count
        if data.shape[1] < 5:
            st.error("❌ The uploaded file must contain at least **5 columns**.")
        else:
            st.success("✅ File uploaded and loaded successfully!")

            # Display raw data option
            with st.expander("🔍 Show Raw Data"):
                st.dataframe(data, use_container_width=True)

            # Column filtering interface
            st.subheader("🔎 Filter Data")

            selected_column = st.selectbox("Select a column to filter by:", data.columns)

            unique_values = data[selected_column].dropna().astype(str).unique()
            selected_value = st.selectbox(
                f"Filter rows where `{selected_column}` is:",
                sorted(unique_values)
            )

            # Filtered DataFrame
            filtered_data = data[data[selected_column].astype(str) == selected_value]

            st.subheader(f"📄 Filtered Data (where `{selected_column}` = {selected_value})")
            st.dataframe(filtered_data, use_container_width=True)

    except ImportError as e:
        st.error("📦 Required package not found. Please install `openpyxl` using `pip install openpyxl`.")
    except ValueError as e:
        st.error(f"⚠️ File read error: {e}")
    except Exception as e:
        st.error(f"🚨 Unexpected error: {e}")

else:
    st.info("📂 Awaiting file upload. Please upload an Excel `.xlsx` file to continue.")
