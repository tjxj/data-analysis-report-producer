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
all_names = _df.Name.unique().tolist()
st.write(all_names)
names = st.multiselect(
    "Programming languages", options=all_names, default=all_names, format_func=pretty
)
st.write(names)

plot_df = _df[_df.Name.isin(names)]
#plot_df["Sex"] = plot_df.Sex.divide(1000).round(1)

chart = (
    alt.Chart(
        plot_df,
        title="Static site generators popularity",
    )
    .mark_bar()
)


st.altair_chart(chart, use_container_width=True)


with st.expander('Plot Explanation'):
        st.write('Notice  inputs.')


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric('Glass transition',"{:0.0f} K".format(tg.mean()))
    st.metric('Configurational entropy',"{:0.1f} J/(mol K)".format(sctg.mean()))

with col2:
    st.metric('Softening point',"{:0.0f} K".format(SP_T.mean()))
    st.metric('Refractive index',"{:0.3f}".format(ri.mean()))
with col3:
    st.metric('Working point','{:0.0f} K'.format(WP_T.mean()))
    st.metric('Melt fragility','{:0.1f}'.format(fragility.mean()))

with col4:
    st.metric('Density',"{:0.2f} g/cm\u00b3".format(density.mean()))
    st.markdown("VFT equation")
    st.markdown("$$\\log_{{10}} \eta = {:0.2f} + \\frac{{{:0.1f}}}{{T-{:0.1f}}}$$".format(A_VFT.mean(),B_VFT.mean(),C_VFT.mean()))
