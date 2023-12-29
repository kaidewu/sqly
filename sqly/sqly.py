import reflex as rx

from sqly.pages.index import index
from sqly.pages.separator import separator
from sqly.pages.generator import generator

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(separator)
app.add_page(generator)
app.compile()
