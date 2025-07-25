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

st.markdown(
    "<h1 style='color: #8B0000;'>🔎 QUẢN LÝ DỮ LIỆU HÓA ĐƠN RỦI RO</h1>",
    unsafe_allow_html=True
)


# Tạo layout ngang cho 3 ô nhập
col1, col2, col3 = st.columns(3)

with col1:
    # Label
    st.markdown(
        f"<div style='font-weight:bold; font-size:22px'>{col_names[0]}</div>",
        unsafe_allow_html=True
    )

    # Tạo khoảng trắng phía trên ô tìm kiếm
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # Ô tìm kiếm
    val1 = st.text_input("", placeholder="Lọc...", key="filter1", label_visibility="collapsed")


with col2:
    # Label cột 2
    st.markdown(
        f"<div style='font-weight:bold; font-size:22px'>{col_names[1]}</div>",
        unsafe_allow_html=True
    )
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    val2 = st.text_input("", placeholder="Lọc...", key="filter2", label_visibility="collapsed")

with col3:
    # Label cột 3
    st.markdown(
        f"<div style='font-weight:bold; font-size:22px'>{col_names[2]}</div>",
        unsafe_allow_html=True
    )
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    val5 = st.text_input("", placeholder="Lọc...", key="filter5", label_visibility="collapsed")



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
csv = filtered_df.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')

st.download_button("📥 Kết xuất toàn bộ dữ liệu", csv, "ketqua.csv", "text/csv")
