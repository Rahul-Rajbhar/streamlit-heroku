import streamlit as st
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

def app():
    
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#-----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_stastics = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_evpfhziw.json")

st_lottie(lottie_stastics, height=300, key="stastics")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_graph = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_lglwitrl.json")

st_lottie(lottie_graph, height=300, key="graph")

  
# --- Loading Assets---

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_9dpbs7iq.json")
lottie_olympics = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0rigkcku.json")

# ---- Header Section ---
with st.container():
    st.subheader("Welcome to our projects :wave:")
    st.title("Analysis of Data about Olympics with Gdp all countries :blush:")
    st.write("We are putting a some unique ideas. :eyes:")
#---- What we do----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do ⛷️")
        st.write("##")   
        st.subheader("Content🏌️‍♂️")
        st.write(
    """
    
    - The file athlete_events.csv contains 271116 rows and 15 columns. Each row corresponds to an individual athlete competing in an individual Olympic event (athlete-events). The columns are:

    - ID - Unique number for each athlete
    - Name - Athlete's name
    - Sex - Male(M) or Female(F)
    - Age - Integer
    - Height - In centimeters
    - Weight - In kilograms
    - Team - Team name
    - NOC - National Olympic Committee 3-letter code
    - Games - Year and season
    - Year - Integer
    - Season - Summer or Winter
    - City - Host city
    - Sport - Sport
    - Event - Event
    - Medal - Gold, Silver, Bronze, or NA
    """
    )


with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
with right_column:
        st_lottie(lottie_olympics, height=300, key="olympic") 


#-----Dataset-----
with st.container():
    st.write("---")
    st.title("Athlete Events Dataset🏃🚴‍♂️")
    st.write("1st Data frame")    
    dfa = pd.read_csv('athlete_events.csv')
    dfa
with st.container():
    st.write(       )

    st.write(
    """
         - Rows = 271116
         - Columns = 15
    """
    )
    dfa.info()
    st.subheader("Null Value")
    st.write(dfa.isnull().sum())
    st.subheader("Describe about Data")
    st.write(dfa.describe())
with st.container():
     st.write("Second DataFrame")
     dfr = pd.read_csv('noc_regions.csv')
     dfr.drop('notes', axis=1, inplace=True)
     st.write(dfr.head(5))
with st.container():
    st.write("New DataFrame")
    df = dfa.merge(dfr, how='left',on='NOC')
    st.write(df)
    # Viewing missing value with help of heatmap
    import plotly.express as px


with st.container():
     st.write("---")
     st.title("Data Visualization")
     st.subheader("Display Null Value using Heatmap")
    #fig = px.imshow(df.isnull(), text_auto=True, aspect="auto")
    #fig.show()
     
     fig, ax = plt.subplots()
     sns.heatmap(df.isnull(), ax=ax)
     st.write(fig)
with st.container():
     st.write("---")
     st.title("Data Cleaning")
     st.write(
         """
         - Age contains null values.
         - Height contains nulll values.
         - Weight contains null values.
         - Medal has null values.
         """
     )