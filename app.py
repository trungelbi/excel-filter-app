import streamlit as st
import pandas as pd

# Cấu hình giao diện Streamlit
st.set_page_config(page_title="Quản lý dữ liệu thuế", layout="wide")

# Đọc dữ liệu từ file Excel có sẵn
@st.cache_data
def load_data():
    return pd.read_excel("a.xlsx")  # Đảm bảo file a.xlsx có trong cùng thư mục

df = load_data()
col_names = df.columns.tolist()

st.title("🔎 Quản lý dữ liệu thuế")

# Tạo layout ngang gồm 3 ô nhập liệu
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input(f"{col_names[0]}", placeholder="Lọc...", key="filter1", on_change=st.experimental_rerun)
with col2:
    st.text_input(f"{col_names[1]}", placeholder="Lọc...", key="filter2", on_change=st.experimental_rerun)
with col3:
    st.text_input(f"{col_names[4]}", placeholder="Lọc...", key="filter5", on_change=st.experimental_rerun)

# Lấy giá trị đã nhập từ session_state
val1 = st.session_state.get("filter1", "")
val2 = st.session_state.get("filter2", "")
val5 = st.session_state.get("filter5", "")

# Lọc dữ liệu
filtered_df = df.copy()
if val1:
    filtered_df = filtered_df[filtered_df[col_names[0]].astype(str).str.contains(val1, case=False, na=False)]
if val2:
    filtered_df = filtered_df[filtered_df[col_names[1]].astype(str).str.contains(val2, case=False, na=False)]
if val5:
    filtered_df = filtered_df[filtered_df[col_names[4]].astype(str).str.contains(val5, case=False, na=False)]

# Hiển thị kết quả lọc
st.subheader("📊 Dữ liệu sau khi lọc")
st.dataframe(filtered_df, use_container_width=True)

# Tải dữ liệu lọc về CSV
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Tải kết quả CSV", csv, "ketqua.csv", "text/csv")
