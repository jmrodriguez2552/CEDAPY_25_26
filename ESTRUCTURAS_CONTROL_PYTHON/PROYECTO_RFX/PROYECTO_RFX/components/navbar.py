import reflex as rx


def navbar()-> rx.Component:
    return rx.hstack(
        rx.text(
            "JPC Classroom",
            height="40px",
        ),
        bg = "blue",
        position="sticky",
        padding="4px",
        z_index="999" # indice máximo para mantenerlo siempre encima
        )