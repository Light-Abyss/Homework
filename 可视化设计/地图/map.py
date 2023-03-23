from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

geo = (
    Geo()
    .add_schema(maptype="世界")
    .render("geo_chart_countries_js.html")
)
