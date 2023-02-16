import openai
import streamlit as st

# 设置API密钥
openai.api_key = "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"

# 设置模型ID
model_engine = "text-davinci-003"

# 定义生成求职信的函数
def generate_cover_letter(name, job_title, company, skills, tone, length):
    prompt = (f"Write a cover letter for {name} applying for the {job_title} position at {company}. "
              f"The candidate should highlight their skills in {skills}. "
              f"The tone of the cover letter should be {tone}. "
              f"Generate a {length} word letter.")

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=length,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text

# 创建网页界面
st.title("Cover Letter Generator")

st.write("Please enter your personal information and job description below:")

name = st.text_input("Full Name")
job_title = st.text_input("Job Title")
company = st.text_input("Company")
skills = st.text_input("Skills")
tone = st.selectbox("Tone", ["Formal", "Friendly"])
length = st.slider("Length (in words)", 50, 500, 200)

if st.button("Generate Cover Letter"):
    cover_letter = generate_cover_letter(name, job_title, company, skills, tone, length)

    st.write("Here is your cover letter:")
    st.write(cover_letter)

    save_file = st.button("Save cover letter to file")

    if save_file:
        with open(f"{name.replace(' ', '_')}_cover_letter.txt", "w") as f:
            f.write(cover_letter)
            st.write("Cover letter saved!")