from imports import *


def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection



# df = px.data.gapminder()
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#            size="pop", color="continent", hover_name="country",
#            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90],height=800)
        
# fig2= px.bar(df, x="continent", y="pop", color="continent",
#   animation_frame="year", animation_group="country", range_y=[0,4000000000],height=800)

# report = dp.Report(
# "# GDP分析报告",
# "##  公众号：数据如琥珀",
#     dp.Group(dp.BigNumber(
#          heading="中国", 
# value=2
#       ),
#       dp.BigNumber(
#          heading="GDP", 
# value="17.7万亿"),columns=2,
#    ),
#      dp.Group(
#     dp.Plot(fig, caption="GDP增长动画"),
#     dp.Plot(fig2, caption="GDP柱形图"),columns=2),
#     dp.DataTable(df, caption="原始数据"),

# )

# report.save(path='report.html', open=True,formatting=dp.ReportFormatting(width=dp.ReportWidth.FULL))


