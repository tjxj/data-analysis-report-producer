from imports import *
from functions import *


st.title("🖱️ Interactive table app")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
if uploaded_file:
    Loaded_dataframe = pd.read_csv(uploaded_file)
    selection = aggrid_interactive_table(df=Loaded_dataframe)

