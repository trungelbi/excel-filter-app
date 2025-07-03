import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản lý dữ liệu hoá đơn rủi ro", layout="wide")
st.markdown(
    """
    <style>
    .stApp img:first-of-type {
        width: 100% !important;
        height: 1200px !important;
        object-fit: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("banner.jpg", use_container_width=True)


# Đọc dữ liệu từ file có sẵn
@st.cache_data
def load_data():
    return pd.read_excel("a.xlsx")

df = load_data()
col_names = df.columns.tolist()

st.title("🔎 QUẢN LÝ DỮ LIỆU HOÁ ĐƠN RỦI RO")

# Tạo layout ngang cho 3 ô nhập
col1, col2, col3 = st.columns(3)
with col1:
    val1 = st.text_input(f"{col_names[0]}", placeholder="Lọc...", key="filter1")
with col2:
    val2 = st.text_input(f"{col_names[1]}", placeholder="Lọc...", key="filter2")
with col3:
    val5 = st.text_input(f"{col_names[2]}", placeholder="Lọc...", key="filter5")

# Lọc dữ liệu realtime
filtered_df = df.copy()

if val1:
    filtered_df = filtered_df[filtered_df[col_names[0]].astype(str).str.contains(val1, case=False, na=False)]
if val2:
    filtered_df = filtered_df[filtered_df[col_names[1]].astype(str).str.contains(val2, case=False, na=False)]
if val5:
    filtered_df = filtered_df[filtered_df[col_names[2]].astype(str).str.contains(val5, case=False, na=False)]

# Hiển thị kết quả
st.subheader("📊 Dữ liệu")
st.dataframe(filtered_df, use_container_width=True)

# Tải kết quả về CSV
csv = filtered_df.to_csv(index=False).encode("utf-8-sig")

st.download_button("📥 Tải kết quả CSV", csv, "ketqua.csv", "text/csv")
