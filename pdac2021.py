import streamlit as st
import exercises.about_course as about_course
import exercises.db_ex as db_ex
import exercises.capping_ex as capping_ex
import exercises.variograms as variograms
import exercises.block_modelling as block_modelling

max_width = 1200

padding_top = 0
padding_right = 0
padding_left = 0
padding_bottom = 0
COLOR = '#180c52'
BACKGROUND_COLOR = 'white'

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
        unsafe_allow_html=True,
    )


st.sidebar.image("..//pdac2021_res_est_course//055CF2A4-98DC-488C-B5A6-15CC02C9974E.png", width=100)

# Capping Exercise - interactive
# Compositing - Q&A
# Variograms - interactive
# Interpolation - interactive
# Compositing - Q&A

radio_options = ["01 About the Course", 
                 "02 Database", 
                 "03 Capping", 
                 "04 Compositing", 
                 "05 Variograms", 
                 "06 Interpolation", 
                 "07 Cut-Off Grade", 
                 "08 Classification"]

exercise=st.sidebar.radio("", 
                          options=radio_options, 
                          index=0, 
                          key=None)

if exercise == radio_options[0]:
  about_course.about_course()
if exercise == radio_options[1]:
  db_ex.db_ex()
if exercise == radio_options[2]:
  capping_ex.capping_ex()
if exercise == radio_options[4]:
  variograms.variograms()
if exercise == radio_options[5]:
  block_modelling.block_modelling()
