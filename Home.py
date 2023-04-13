import streamlit as st
import pandas
import time

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-name {
    font-size: 70px;
}
.brief-personal-info {
    font-size: 20px;
    font-weight: 500;
    background-color: #e6f1fb;
    padding: 20px;
    border-radius: 8px;
}
.projects-intro {
    font-size: 30px;
    font-weight: 700;
}
.project-desc, .project-src-code-url {
    font-size: 25px;
}
</style>
""", unsafe_allow_html=True)

now = time.strftime("%b %d, %Y %H:%M:%S %Z")
st.write(f"You're accessing this page at {now}")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    name_content = """<h1 class="big-name">Kesit Budi Kusumo</h1>"""
    st.markdown(name_content, unsafe_allow_html=True)
    brief_personal_info_content = """
    <p class="brief-personal-info">Hi, I am Kesit! I am a Python and JS programmer. <br/><br/>
    I graduated in 2020 with a bachelor of Computer Science from Brawijaya University in Indonesia. <br/><br/>
    I have worked with multiple companies, such as Consultant IT and E-commerce (Shopee), performing building apps 
    for both clients and internal usages.</p>
    """
    st.markdown(brief_personal_info_content, unsafe_allow_html=True)

projects_intro_content = """
<p class="projects-intro">Below you can find some of the apps I have built in Python/JS. Feel free to contact me!</p>
"""
st.markdown(projects_intro_content, unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")


def display_project_section(data):
    st.header(data["title"])
    project_desc_content = f"<p class='project-desc'>{data['description']}</p>"
    st.markdown(project_desc_content, unsafe_allow_html=True)
    st.image(f"images/{data['image']}")
    st.markdown(f"<a href='{data['url']}' class='project-src-code-url'>Source code</a>",
                unsafe_allow_html=True)


with col3:
    for index, row in df[:10].iterrows():
        display_project_section(row)

with col4:
    for index, row in df[10:].iterrows():
        display_project_section(row)



