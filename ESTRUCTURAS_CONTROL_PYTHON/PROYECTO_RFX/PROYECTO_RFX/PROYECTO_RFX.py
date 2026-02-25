"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from PROYECTO_RFX.components.navbar import navbar
from PROYECTO_RFX.views.header.header import header
from PROYECTO_RFX.views.links.links import links


class State(rx.State):  # Para gestionar el estado de la aplicación (control de datos, variables, etc.)
    """The app state."""
    pass


def index()-> rx.Component:
    return rx.vstack(
        navbar(),
        rx.center(
            header(),
            links()
        )
    ) 


app = rx.App() # Crear una instancia de la aplicación
app.add_page(index) # Agregar la página principal a la aplicación
# app.compile() # Compilar la aplicación para que pueda ser ejecutada
