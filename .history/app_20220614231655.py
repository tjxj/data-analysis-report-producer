from imports import *
from functions import *

st.title("🖱️ Interactive table app")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
if uploaded_file:
    _df = pd.read_csv(uploaded_file)
    selection = aggrid_interactive_table(df=_df)

    st.write(_df.columns)
    color = st.sidebar.selectbox("columns", (_df.columns))


row9_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
# with row9_1:
#     st.markdown('test')    
#     plot_x_per_matchday_selected = st.selectbox ("Which aspect do you want to analyze?", list(label_attr_dict.keys()), key = 'attribute_matchday')
#     plot_x_per_matchday_type = st.selectbox ("?", types, key = 'measure_matchday')
# with row9_2:
#     if all_teams_selected != 'Select teams manually (choose below)' or selected_teams:
#         plot_x_per_matchday(plot_x_per_matchday_selected, plot_x_per_matchday_type)
#     else:
#         st.warning('Please select at least one team')
        

def pretty(s: str) -> str:
    try:
        return dict(js="JavaScript")[s]
    except KeyError:
        return s.capitalize()
        
#_df["lang"] = _df.columns.map(pretty)
all_names = _df.name.unique().tolist()
st.write(all_names)
names = st.multiselect(
    "Programming languages", options=all_names, default=all_names, format_func=pretty
)
st.write(names)

plot_df = _df[Names]
chart = (
    alt.Chart(
        plot_df,
        title="Static site generators popularity",
    )
    .mark_bar()
)


st.altair_chart(chart, use_container_width=True)