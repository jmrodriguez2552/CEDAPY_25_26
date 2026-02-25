import reflex as rx
from PROYECTO_RFX.components.link_button import link_button


def links()-> rx.Component:
    return rx.vstack(
        link_button("Instagram"),
        link_button("GitHub")
    )