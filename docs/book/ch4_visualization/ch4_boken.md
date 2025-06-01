---
title: Boken
---



##  Bokeh server
Bokeh server is a advanced graphical tools for building the web visualization for the Python, R, etc and has capabilities for serving live-streaming, interactive visualizations that update with real-time data.

```python
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure, ColumnDataSource

def make_document(doc):
    fig = figure(title='Line plot!', sizing_mode='scale_width')
    fig.line(x=[1, 2, 3], y=[1, 4, 9])
    doc.title = "Hello, world!"
    doc.add_root(fig)

apps = {'/': Application(FunctionHandler(make_document))}

server = Server(apps, port=8003)
server.start()
IOLoop.current().start()
```


## Live 
```pyhton 
import random

def make_document(doc):
    source = ColumnDataSource({'x': [], 'y': [], 'color': []})
    def update():
        new = {'x': [random.random()],
               'y': [random.random()],
               'color': [random.choice(['red', 'blue', 'green'])]}
        source.stream(new)
    doc.add_periodic_callback(update, 100)
    fig = figure(title='Streaming Circle Plot!', sizing_mode='scale_width',
                 x_range=[0, 1], y_range=[0, 1])
    fig.circle(source=source, x='x', y='y', color='color', size=10)
    doc.title = "Now with live updating!"
    doc.add_root(fig)

apps = {'/': Application(FunctionHandler(make_document))}

server = Server(apps, port=5001)
server.start()
IOLoop.current().start()

```


