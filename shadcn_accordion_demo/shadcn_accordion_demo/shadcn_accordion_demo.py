"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_shadcn_accordion import *

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
        accordion(
            accordion_item(
                accordion_trigger("Item 1"),
                accordion_content("Content 1"),
                value="item-1"
            ),
            accordion_item(
                accordion_trigger("Item 2"), 
                accordion_content("Content 2"),
                value="item-2"
            ),
            type="single",
            is_collapsible=True
        )
    ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
