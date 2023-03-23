from pyecharts import options as opts
from pyecharts.charts import Bar, Line

data_name = '中国各省GDP数据.csv'
data_file = open(data_name, 'r')
data_list = data_file.readlines()
data_file.close()
del data_list[0]

provinces = []
data_GDP = []
data_GDPpc = []
data_rate = []
for data in data_list :
    data = data.strip('\n')
    data_line_list = data.split(',')
    provinces.append(data_line_list[0])
    data_GDP.append(data_line_list[1])
    data_rate.append(data_line_list[2])
    data_GDPpc.append(data_line_list[3])

line = (
    Line(
        init_opts = opts.InitOpts(
            width ="90%",
            height ="640px",
        )
    )
    .add_xaxis(provinces)
    .add_yaxis(
        '增长率',
        data_rate,
        linestyle_opts = {
            "normal": {
                "color": "#9966FF",  #线条颜色
                "width": 3   # 线条粗细
            }
        }
    )
    .set_global_opts(
        yaxis_opts = opts.AxisOpts(
            name = "增长率",
            type_ = "value",
            min_ = -2,
            max_ = 5,
            position = "left",
            axisline_opts = opts.AxisLineOpts(
                linestyle_opts = opts.LineStyleOpts(color = "#9966FF")
            ),
            axislabel_opts = opts.LabelOpts(formatter = "{value}%"),
        ),
        title_opts = opts.TitleOpts(title = "中国各省GDP"),
        datazoom_opts = [opts.DataZoomOpts()],
        tooltip_opts = opts.TooltipOpts(
            trigger = "item",
            axis_pointer_type = "cross"
        ),
    )
    .extend_axis(
        yaxis = opts.AxisOpts(
            name = "人均GDP",
            min_ = 0,
            max_ = 20,
            position = "right",
            offset = 75,
            axisline_opts = opts.AxisLineOpts(
                linestyle_opts = opts.LineStyleOpts(color = "#5793f3")
            ),
            axislabel_opts = opts.LabelOpts(formatter = "{value}万元"),
        )
    )
    .extend_axis(
        yaxis = opts.AxisOpts(
            name = "GDP",
            min_ = 0,
            max_ = 150,
            position = "right",
            axisline_opts = opts.AxisLineOpts(
                linestyle_opts = opts.LineStyleOpts(color = "#d14a61")
            ),
            axislabel_opts = opts.LabelOpts(formatter = "{value}千亿元"),
        )
    )
)

bar = (
    Bar()
    .add_xaxis(provinces)
    .add_yaxis(
        "GDP",
        data_GDP,
        yaxis_index = 2,
        itemstyle_opts = opts.ItemStyleOpts(
            color = "rgba(209, 74, 97, 0.8)"
        ),
        label_opts = opts.LabelOpts(is_show = False)
    )
    .add_yaxis(
        "人均GDP",
        data_GDPpc,
        yaxis_index = 1,
        itemstyle_opts = opts.ItemStyleOpts(
            color = "rgba(87, 147, 243, 0.8)"
        ),
        label_opts = opts.LabelOpts(is_show = False)
    )
)

line.overlap(bar)
line.render("中国各省GDP图1.html")