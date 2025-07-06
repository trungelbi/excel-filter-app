import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản lý dữ liệu hoá đơn rủi ro", layout="wide")
st.image("banner.jpg", use_container_width=True)

# Đọc dữ liệu từ file có sẵn
@st.cache_data
def load_data():
    return pd.read_excel("a.xlsx")

df = load_data()
col_names = df.columns.tolist()

st.title("🔎 QUẢN LÝ DỮ LIỆU HÓA ĐƠN RỦI RO")

# Tạo layout ngang cho 3 ô nhập
col1, col2, col3 = st.columns(3)
with col1:
    val1 = st.text_input("", placeholder=f"{col_names[0]} - lọc...", key="filter1")

with col2:
    val2 = st.text_input("", placeholder=f"{col_names[1]} - lọc...", key="filter2")

with col3:
    val5 = st.text_input("", placeholder=f"{col_names[2]} - lọc...", key="filter5")

# Lọc dữ liệu realtime
filtered_df = df.copy()
if val1:
    filtered_df = filtered_df[filtered_df[col_names[0]].astype(str).str.contains(val1, case=False, na=False)]
if val2:
    filtered_df = filtered_df[filtered_df[col_names[1]].astype(str).str.contains(val2, case=False, na=False)]
if val5:
    filtered_df = filtered_df[filtered_df[col_names[2]].astype(str).str.contains(val5, case=False, na=False)]

# Hiển thị kết quả với phân trang
st.subheader("📊 Dữ liệu")
def render_html_table(df):
    html = """
    <div style='max-height: 400px; overflow-y: auto; border: 1px solid #ddd;'>
        <table style='width:100%; border-collapse: collapse;'>
            <thead>
                <tr>
    """
    for col in df.columns:
        html += f"<th style='border: 1px solid #ccc; padding: 8px; font-weight: bold; background-color: #f2f2f2'>{col}</th>"
    html += "</tr></thead><tbody>"

    for _, row in df.iterrows():
        html += "<tr>"
        for val in row:
            html += f"<td style='border: 1px solid #ccc; padding: 8px'>{val}</td>"
        html += "</tr>"

    html += """
            </tbody>
        </table>
    </div>
    """
    return html

st.markdown(render_html_table(filtered_df), unsafe_allow_html=True)

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
# Tải kết quả về CSV
csv = filtered_df.to_csv(index=False).encode("utf-8-sig")

st.download_button("📥 Tải kết quả CSV", csv, "ketqua.csv", "text/csv")
