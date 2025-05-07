# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:32:14 2025
@author: Administrator
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Data Warehousing & Enterprise Data Management",
    page_icon="🏢",
    layout="wide"
)

# Sidebar Filters
st.sidebar.title("🔍 Filters & Options")
topic = st.sidebar.selectbox(
    "📌 Choose a Topic:",
    ["Data Warehousing", "ETL Processes", "Enterprise Data Management", "Data Governance"]
)
filter_value = st.sidebar.slider("⚙️ Importance Level:", 0, 100, 50)

# Main Title & Info
st.title("🏢 Data Warehousing & Enterprise Data Management")
st.markdown(f"**Topic:** `{topic}` &nbsp; | &nbsp; **Importance Level:** `{filter_value}`")

# Optional intro text based on topic
topic_descriptions = {
    "Data Warehousing": "A central system that consolidates large volumes of structured data for analysis and business intelligence.",
    "ETL Processes": "ETL (Extract, Transform, Load) pipelines move and reshape data from raw sources to structured destinations.",
    "Enterprise Data Management": "EDM is about aligning data processes, governance, and architecture with enterprise goals.",
    "Data Governance": "Focuses on data ownership, integrity, privacy, and compliance across the organization."
}
st.info(topic_descriptions[topic])

# Two-column Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏗️ Data Warehousing Architecture")
    st.markdown("""
    - Central repository built for **analytics** and **reporting**.
    - Relies on **OLAP** systems for fast multi-dimensional queries.
    - Includes **staging**, **integration**, and **access** layers.
    """)

with col2:
    st.subheader("🔄 ETL: Extract, Transform, Load")
    st.markdown("""
    - **Extract**: Pull data from operational systems, files, or APIs.  
    - **Transform**: Clean, standardize, and validate data.  
    - **Load**: Insert into target data warehouse tables.  
    - Ensures **data consistency** and **traceability**.
    """)

# Tabs for detailed content
tab1, tab2 = st.tabs(["📚 Core Concepts", "📊 Business Applications"])

with tab1:
    st.markdown("### 📖 Definitions & Frameworks")
    st.markdown("""
    - **Enterprise Data Management (EDM)**: Coordinates data policies and practices across an organization.  
    - **Metadata Management**: Documents the structure, meaning, and lineage of data assets.  
    - **Master Data Management (MDM)**: Harmonizes critical data (e.g., products, customers) across systems.
    """)

with tab2:
    st.markdown("### 💼 Use Cases in Industry")
    st.markdown("""
    - **Retail**: Unified customer profiles and targeted promotions.  
    - **Healthcare**: Interoperable records and regulatory compliance.  
    - **Finance**: Real-time fraud detection and audit trails.  
    """)

# Expander for additional insights
with st.expander("📖 More Information"):
    st.write("""
    Data Warehousing and EDM are critical to modern data strategies.  
    As organizations transition to cloud and hybrid data architectures, real-time insights and governance become increasingly vital.  
    They help ensure **accuracy**, **security**, and **strategic alignment** of all enterprise data assets.
    """)

# Footer
st.markdown("---")
st.caption("💡 Built with Streamlit · Last updated May 2025")
