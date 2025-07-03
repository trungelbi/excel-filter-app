import streamlit as st
import pandas as pd

st.title("🧮 Bộ lọc dữ liệu Excel")

uploaded_file = st.file_uploader("📂 Chọn file Excel", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Xem trước dữ liệu", df.head())

    columns = st.multiselect("Chọn cột để lọc", df.columns)
    filtered_df = df.copy()
    for col in columns:
        options = filtered_df[col].dropna().unique().tolist()
        selected = st.multiselect(f"Lọc {col}", options)
        if selected:
            filtered_df = filtered_df[filtered_df[col].isin(selected)]

    st.subheader("📊 Kết quả lọc")
    st.dataframe(filtered_df)

    # Tải về file kết quả
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Tải kết quả CSV", csv, "ketqua.csv", "text/csv")
