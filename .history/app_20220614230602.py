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
all_langs = _df.columns.unique().tolist()
st.write(all_langs)
langs = st.multiselect(
    "Programming languages", options=all_langs, default=all_langs, format_func=pretty
)
st.write(langs)

plot_df = _df[langs]
chart = (
    alt.Chart(
        plot_df,
        title="Static site generators popularity",
    )
    .mark_bar()
    .encode(
        x=alt.X("stars", title="'000 stars on Github"),
        y=alt.Y(
            "name",
            sort=alt.EncodingSortField(field="stars", order="descending"),
            title="",
        ),
        color=alt.Color(
            "lang",
            legend=alt.Legend(title="Language"),
            scale=alt.Scale(scheme="category10"),
        ),
        tooltip=["name", "stars", "lang"],
    )
)


st.altair_chart(chart, use_container_width=True)