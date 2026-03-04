import reflex as rx

def header()-> rx.Component:
    return rx.vstack(
        rx.center(
            rx.image(src="/JPC_CARTOON.jpeg", width= "200px", height="auto"),
            rx.text("@jordipozo"),
            rx.text("""Hola me llamo Jordi Pozo.
                    Soy profesor de Ciclos Formativos
                """)
        )
    )