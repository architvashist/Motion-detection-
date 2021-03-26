from video import df

from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnarDataSource


# print(df)
p=figure(x_axis_type='datetime',height=500,width=1000,title="Motion graph")
p.yaxis.minor_tick_line_color = None
p.ygrid.grid_line_color = None



q=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")
output_file("Motion.html",title="Motion Graph")
show(p)