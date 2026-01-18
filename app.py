import streamlit as st

# --- Hàm Tạo Prompt ---
def generate_prompt(name, age, gender, traits, outfit, action, setting, style, lighting, camera):
    base = f"{name}, {age} years old, {gender}, {traits}"
    outfit_part = f", wearing {outfit}" if outfit else ""
    action_part = f", {action}" if action else ""
    setting_part = f" in {setting}" if setting else ""
    style_part = f", {style}" if style else ""
    lighting_part = f", {lighting}" if lighting else ""
    camera_part = f", {camera}" if camera else ""
    return f"{base}{outfit_part}{action_part}{setting_part}{style_part}{lighting_part}{camera_part}"

# --- Streamlit UI ---
st.title("🔥 Prompt Generator cho Nhân Vật Đồng Nhất")

with st.form("prompt_form"):
    st.subheader("Thông tin nhân vật")
    name = st.text_input("Tên nhân vật", "Alex")
    age = st.text_input("Tuổi", "25")
    gender = st.selectbox("Giới tính", ["Male", "Female", "Non-binary", "Other"])
    traits = st.text_area("Các nét đặc trưng (hair, eyes, build, style)", "short black hair, piercing green eyes")

    st.subheader("Chi tiết prompt")
    outfit = st.text_input("Trang phục", "black leather jacket")
    action = st.text_input("Hành động / Pose", "standing confidently")
    setting = st.text_input("Bối cảnh / Background", "futuristic cityscape at night")

    st.subheader("Phong cách tạo ảnh")
    style = st.text_input("Phong cách nghệ thuật", "cyberpunk, cinematic")
    lighting = st.text_input("Chiếu sáng", "neon lights, dramatic shadows")
    camera = st.text_input("Camera / Angle", "35mm cinematic shot")

    submitted = st.form_submit_button("🎨 Tạo Prompt")

if submitted:
    prompt = generate_prompt(
        name, age, gender, traits,
        outfit, action, setting,
        style, lighting, camera
    )
    st.markdown("### 📋 Prompt đã tạo:")
    st.code(prompt, language="text")
    st.download_button("📥 Tải Prompt (.txt)", prompt, file_name="prompt.txt")
