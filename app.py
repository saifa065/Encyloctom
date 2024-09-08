import streamlit as st
from PIL import Image



st.title("Encyloctom")
st.write("เป็นสารานุกรมสิ่งมีชีวิตที่ใช้ในการทำความรู้จักกับวิถีชีวิตของสิ่งมีชีวิตนั้นๆ")
st.write("ผ่านการเข้าใจวงจรและพฤติกรรมทางตามธรรมชาติและเปอเซ็นของจำนวนสิ่งมีชีวิตและความสำคัญทางระบบนิเวศ")
# Create a drag and drop file uploader
uploaded_file = st.file_uploader("ใส่ภาพลงไปในนี้เพื่อเริ่มทำความรู้จักกับสิ่งมีชีวิตนั้นๆ", type=["jpg","png"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Open the image file using PIL
    image = Image.open(uploaded_file)
    
    # Display the image with a caption
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Optionally, print out the image details
    st.write(f"Image format: {image.format}, Size: {image.size}, Mode: {image.mode}")
    st.title('นกกระจาบทอง')
    st.write('เพศเมีย')
    st.title('แหล่งที่อยู่')
    st.write('อยู่ในพื้นที่มีพื้นที่ลุ่มน้ำท่วมถึง ทุ่งหญ้า หนองบึง และพื้นที่เกษตรกรรม')
    st.title('ความสำคัญทางธรรมชาติ')
    st.write('1. **ตัวบ่งชี้คุณภาพสิ่งแวดล้อม**: นกกระจาบทองสามารถใช้เป็นตัวบ่งชี้ความสมบูรณ์ของพื้นที่ธรรมชาติ เนื่องจากพวกมันต้องการพื้นที่ที่มีทรัพยากรอาหารและที่อยู่อาศัยที่ดี การพบเห็นนกกระจาบทองในพื้นที่ใดบ่งชี้ถึงสุขภาพของระบบนิเวศในบริเวณนั้น')
    st.write('2. **ช่วยในการควบคุมประชากรแมลง**: นกกระจาบทองเป็นนกที่กินเมล็ดพืชเป็นหลัก แต่บางครั้งก็ยังกินแมลง ซึ่งช่วยลดจำนวนแมลงศัตรูพืช ทำให้เป็นประโยชน์ต่อการเกษตร')
    st.write('3. **ช่วยในการแพร่กระจายเมล็ดพืช**: นกกระจาบทองกินเมล็ดพืชหลายชนิด การที่มันบินไปที่ต่างๆ และถ่ายมูลที่มีเมล็ดพืชอยู่ ทำให้มีส่วนช่วยในการแพร่กระจายเมล็ดพืช ซึ่งมีผลต่อการขยายพันธุ์พืชในธรรมชาติ')
    st.write('4. **ส่งเสริมความหลากหลายทางชีวภาพ**: นกกระจาบทองช่วยในการสร้างความหลากหลายทางชีวภาพในพื้นที่ที่มันอาศัยอยู่ ด้วยการกินพืชและแมลงหลายชนิด จึงเป็นส่วนหนึ่งของห่วงโซ่อาหารที่สำคัญ')
    st.write('5. **การสร้างรังที่เป็นเอกลักษณ์**: นกกระจาบทองเป็นที่รู้จักกันดีในเรื่องการสร้างรังที่มีรูปแบบซับซ้อนและสวยงาม รังของนกกระจาบเป็นแหล่งที่อยู่อาศัยของสัตว์เล็กอื่นๆ เช่น แมลงหรือแมงมุม อีกทั้งยังเป็นส่วนหนึ่งของวัฒนธรรมและความงามของธรรมชาติ')





