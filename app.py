import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# B.Radhepa,
##### *Resume* 
''')

image = Image.open('dp.png.jpg')
st.image(image, width=150)

st.markdown('## Objective', unsafe_allow_html=True)
st.info('''
- To make sincere and continuous effort towards building a promising career. 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand MY RESUME" target="_blank">My Profile </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')


txt('**B E Electronics & Communication Engineering** (Engineering), *Karpagam Institute of technology*, coimbatore',
'Currently Pursuing(1st Year)')


txt('**12th Standard** (computer science), *National Model Matric H.S.S, *, coimbatore',
'2021-2022')
st.markdown('''
- percentage :69.5
''')


txt('**10th Standard**, *Alard Public School *, pune',
'2019-2020')
st.markdown('''
- percentage :63
''')


#####################
st.markdown('''
## Strengths
''')
st.markdown('''
- Hardworking.
-Strong determination.
-Punctuality.
-Soft Skills.
-Eloquent.
''')

#####################
st.markdown('''
## extra curricular activities
''')
st.markdown('''
-Singing 
-Dancing
-Reading Novels
''')



#####################
st.markdown('''
## personal & contact info
''')
txt2('Father’s Name :','R. Baskaran')
txt2('Date of Birth','18-05-2004')
txt2('Mobile number:', ' 91-74186 50423')
txt2('Email ID', 'radhepa.baskaran@gmail.com')
txt2('Adrdress:', 'D8A, No 5/174, Vasubas Nivas,Airwin Garden, Kadampadi, Sulur,Coimbatore – 641401')

st.markdown('## Declaration:', unsafe_allow_html=True)
st.info('''
- I hereby declare that the statements made are true, complete and correct to the best of my knowledge and belief.
'With Regards/n'
B.Radhepa 
''')
