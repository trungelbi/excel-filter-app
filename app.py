import streamlit as st
import pandas as pd

# Đọc file Excel có sẵn (cùng thư mục)
@st.cache_data
def load_data():
    return pd.read_excel("a.xlsx")

df = load_data()

st.title("🔍 Bộ lọc dữ liệu (3 cột)")

# Hiển thị dữ liệu gốc
st.subheader("📋 Dữ liệu gốc")
st.dataframe(df)

# Giả sử cột 1, 2 và 5 là tên cột thực tế
col_names = df.columns.tolist()

# Tạo 3 ô lọc theo cột 1, 2, 5
val1 = st.text_input(f"Lọc theo {col_names[0]}")
val2 = st.text_input(f"Lọc theo {col_names[1]}")
val5 = st.text_input(f"Lọc theo {col_names[4]}")

# Lọc dữ liệu
filtered_df = df.copy()
if val1:
    filtered_df = filtered_df[filtered_df[col_names[0]].astype(str).str.contains(val1, case=False, na=False)]
if val2:
    filtered_df = filtered_df[filtered_df[col_names[1]].astype(str).str.contains(val2, case=False, na=False)]
if val5:
    filtered_df = filtered_df[filtered_df[col_names[4]].astype(str).str.contains(val5, case=False, na=False)]

# Hiển thị kết quả lọc
st.subheader("📊 Kết quả sau khi lọc")
st.dataframe(filtered_df)

# Cho tải về
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Tải kết quả CSV", csv, "ketqua.csv", "text/csv")
