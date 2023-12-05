import reflex as rx

from sqly.pages.index import index
from sqly.pages.separator import separator

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(separator)
app.compile()
