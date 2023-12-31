import reflex as rx

from sqly.pages.index import index

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
