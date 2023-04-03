from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Bar, WordCloud, Timeline, Page
from math import log, sqrt

name = ['', '', '', '']
name[0] = '三体'
name[1] = '三体1地球往事'
name[2] = '三体2黑暗森林'
name[3] = '三体3死神永生'

node_file_name = ['', '', '', '']
for i in range(0, 4) :
    node_file_name[i] = './' + name[i] + '-人物节点.csv'
out_file_name = './三体人物统计图.html'

node_line_list = [[], [], [], []]
for i in range(0, 4) :
    node_file = open(node_file_name[i], 'r')
    node_line_list[i] = node_file.readlines()
    node_file.close()
    del node_line_list[i][0]  # 删除标题行

name_fic = [[], [], [], []]
freq_fic = [[], [], [], []]
for i in range(0, 4) :
    for one_line in node_line_list[i]:
        one_line = one_line.strip('\n')
        one_line_list = one_line.split(',')
        name_fic[i].append(one_line_list[0])
        freq_fic[i].append(one_line_list[1])

color = ['', '', '', '']
color[0] = '#00BFFF'
color[1] = '#9370DB'
color[2] = '#00FF7F'
color[3] = '#FFB6C1'

wordcloud = (
    WordCloud(
        opts.InitOpts(
        page_title = '三体人物统计图',
        width = "100%", 
        height = "640px", 
    )
    )
    .add("三体人物统计", data_pair = list(zip(name_fic[0], freq_fic[0])), word_size_range = [40, 120])
    .set_global_opts(title_opts = opts.TitleOpts(title = "三体人物统计"))
)

bar = []
for i in range(0, 4) :
    bar.append(Bar())
    bar[i].add_xaxis(name_fic[i])
    bar[i].add_yaxis(
        '出现次数',
        freq_fic[i],
        color = color[i]
    )
    bar[i].set_global_opts(
        title_opts = opts.TitleOpts(title = name[i] + ' 人物统计'),
        toolbox_opts = opts.ToolboxOpts()
    )

timeline = Timeline(
    opts.InitOpts(
        page_title = '三体人物统计图',
        width = "100%", 
        height = "640px", 
    )
)

for i in range(0, 4) :
    timeline.add(bar[i], name[i])
    
page = (
    Page(
        page_title = '三体人物统计图',
        layout = Page.SimplePageLayout,
        interval = 40
    )
    .add(wordcloud)
    .add(timeline)
)
page.render(out_file_name)