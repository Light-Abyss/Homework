from pyecharts import options as opts
from pyecharts.charts import Map, Timeline

data_name = '部分省份人口数据.csv'
data_file = open(data_name, 'r')
data_list = data_file.readlines()
data_file.close()
del data_list[0]

data_province = []
data_population = []
data_rate = []

for data in data_list :
    data = data.strip('\n')
    data_line_list = data.split(',')
    data_province.append(data_line_list[0])
    data_rate.append(data_line_list[1])
    data_population.append(data_line_list[2])

map_population = (
    Map(
        init_opts = opts.InitOpts(
            width ="100%",
            height ="640px",
        )
    )
    .add(
        "常住人口(万人)",
        [list(z) for z in zip(data_province, data_population)],
        "china",
        label_opts = opts.LabelOpts(is_show = False),
    )
    .set_global_opts(
        title_opts = opts.TitleOpts(title = "中国部分省份常住人口数量图"),
        visualmap_opts = opts.VisualMapOpts(
            min_ = 0,
            max_ = 12000,
            split_number = 20
        ),
    )
)
map_rate = (
    Map(
        init_opts = opts.InitOpts(
            width ="100%",
            height ="640px",
        )
    )
    .add(
        "自然增长率(‰)",
        [list(z) for z in zip(data_province, data_rate)],
        "china",
        label_opts = opts.LabelOpts(is_show = False),
    )
    .set_global_opts(
        title_opts = opts.TitleOpts(title = "中国部分省份人口自然增长率图"),
        visualmap_opts = opts.VisualMapOpts(
            min_ = -5,
            max_ = 5,
            split_number = 20,
        ),
    )
)
timeline = Timeline(
    opts.InitOpts(
        page_title = '中国部分省份人口图',
        width = "100%", 
        height = "640px", 
    )
)
timeline.add(map_population, '常住人口数量')
timeline.add(map_rate, '自然增长率')
timeline.render("中国部分省份人口图.html")