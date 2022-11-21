import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Website",
                   page_icon=":clubs:", layout="wide")

st.header(":clubs: BRIDGE")

#st.write("<h6 style='text-align: center;'>You want to find curious, creative and talented people but just have a pre-formatted paper to do so</h6>", unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

df = pd.read_csv('final.csv')


with st.container():
    st.write("---")
    #st.write("<h1 style='text-align: center;'>Looking for curious and active college students, here's how you can find them.</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align: center;'>If you want to find curious, creative and talented people but just have a pre-formatted paper to do so</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align: center;'>We're here to help you out </h1>",
             unsafe_allow_html=True)

    st.write("---")
    st.write("<h2 style='color:black;'>TARGET MARKET</h2>",
             unsafe_allow_html=True)
    st.write("<h3 style='color:black;'> - Companies looking for enthusiasts in a particular field</h3>",
             unsafe_allow_html=True)
    st.write("<h3 style='color:black;'> - Companies whose target market are college students</h3>",
             unsafe_allow_html=True)
    st.write("<h3 style='color:black;'> - Companies looking for candidates with tested soft skills</h3>",
             unsafe_allow_html=True)


with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            "<h2>                                                              </h2>", unsafe_allow_html=True)
        st.write(
            "<h2>                                                             </h2>", unsafe_allow_html=True)
        st.write(
            "<h3 > You want to hire trailblazers and wait till interviewing them to know a candidate is one</h3>", unsafe_allow_html=True)

        st.write("<h2>Less than 5% of your candidates are who you want</h2>",
                 unsafe_allow_html=True)
    with right_column:
        img = Image.open("pie-chart(1).png")
        new_image = img.resize((500, 300))
        st.image(new_image)

with st.container():
    st.write("---")
    st.write(
        "<h3 style='color:black;text-align: center;'> Need to market your product to a particular audience</h3>", unsafe_allow_html=True)

    st.write("<h2 style='color:black;text-align: center;'>Check when your chances of reaching them is the highest</h2>",
             unsafe_allow_html=True)

    col1, left_column, right_column, col2 = st.columns([1, 2, 2, 1])
    with col1:
        st.empty()
    with col2:
        st.empty()
    with right_column:
        img = Image.open("pie-chart(2).png")
        new_image = img.resize((350, 200))
        st.image(new_image)

    with left_column:
        img = Image.open("pie-chart.png")
        new_image = img.resize((350, 200))
        st.image(new_image)

with st.container():
    st.write("---")
    st.write("<h1>We Match If You :</h1>",
             unsafe_allow_html=True)
    st.write("<h4> - Want a college representative team? </h4>",
             unsafe_allow_html=True)
    st.write("<h4> - Need to find leaders to hire? </h4>",
             unsafe_allow_html=True)
    st.write("<h4> - Looking for the next generation of innovators in a particular field? </h4>",
             unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("<h1 style='text-align: center;color:black;'>We’re basically Tinder</h1>",
             unsafe_allow_html=True)
    st.write("<h4 style='text-align: center;'> Without the creeps, no-shows, or catfishes </h4>",
             unsafe_allow_html=True)
    st.write("<h3 style='text-align: center;color:black;'> We know 'We are basically a millennial teenage dream' </h3>",
             unsafe_allow_html=True)


with st.container():

    st.sidebar.header("Please Filter Here:")

    st.write("---")
    st.write("<h1 style='text-align: center;color:black;'>How our product works? </h1>",
             unsafe_allow_html=True)
    col1, left_column, right_column,  = st.columns([1, 2, 1])
    with col1:
        st.empty()
    with left_column:
        img = Image.open("how.png")
        new_image = img.resize((700, 500))
        st.image(new_image)

    with col2:
        st.empty()

    st.write("<h1 style='text-align: center;color:black;'>For Example </h1>",
             unsafe_allow_html=True)
    Name = st.sidebar.multiselect(
        "Select the Name",
        options=df["Name"].unique()
    )
    Role = st.sidebar.multiselect(
        "Select the role",
        options=df["Role"].unique()
    )
    Fest_Name_x = st.sidebar.multiselect(
        "Select the Fest",
        options=df["Fest_Name_x"].unique()
    )

    df_selection = df.query(
        "Name == @Name | Role == @Role & Fest_Name_x == @Fest_Name_x")
    st.dataframe(df_selection)


with st.container():
    st.write("---")
    st.write("<h1>Why we work?</h1>",
             unsafe_allow_html=True)
    st.write("<h4> - On average, each corporate job offer attracts 250 resumes. Of those candidates, 4 to 6 will get called for an interview, and only one will get the job.(Glassdoor) </h4>", unsafe_allow_html=True)
    st.write("<h5>That is just a waste of time and resources, with our data you will </h5>",
             unsafe_allow_html=True)
    st.write("<h4> - Up to 85% of jobs are filled via networking out of which 60% is through headhunters. (LinkedIn) </h4>", unsafe_allow_html=True)
    st.write("<h5>Our solution simplifies the job of a headhunter </h5>",
             unsafe_allow_html=True)
    st.write("<h4> - Average college fests and clubs budgets are upwards of  25Lpa+ and 10Lpa+ . They have multiple events and numerous companies sponsoring them with sponsorship amounts ranging from 50k to 10L </h4>", unsafe_allow_html=True)
    st.write("<h5>Upon partnering with us companies will know which event to sponsor to actually get the required impressions and will be able to make decisions with verified and valid data.</h5>",
             unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.markdown("<h1 style='color:black;'>Get in touch with us!</h1>",
                unsafe_allow_html=True)
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/sanjanaskoheda@gmail.com" method="POST">
    <input type = "hidden" name="_captcha" value = "false">
    <input type="text" name="name" required>
    <input type="email" name="email" required>
    <textarea name="message" placeholder = "Your message here" required></textarea>
    <button type="submit">Send</button>
    </form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    st.write('##')
    st.write(
        "[Github](https://github.com/Sanjana86/MindGraph_Hackathon)")
