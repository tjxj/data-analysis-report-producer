from imports import *
from functions import *

st.title("🖱️ Interactive table app")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
if uploaded_file:
    Loaded_dataframe = pd.read_csv(uploaded_file)
    selection = aggrid_interactive_table(df=Loaded_dataframe)

st.write(Loaded_dataframe.columns)
color = st.sidebar.selectbox("columns", (Loaded_dataframe.columns))


row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
with row8_1:
    st.subheader('Analysis per Matchday')
    
with row8_spacer1:
    st.subheader('row8_spacer1')