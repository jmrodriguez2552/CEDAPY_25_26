import reflex as rx

def header()-> rx.Component:
    return rx.vstack(
        rx.center(
            rx.avatar(src="/home/jordi/Documentos/Ribera/Curso_25_26/CEDAPY/REPOS/CEDAPY_25_26/ESTRUCTURAS_CONTROL_PYTHON/PROYECTO_RFX/assets/JPC_CARTOON.jpeg", radius="medium"),
            rx.text("@jordipozo"),
            rx.text("""Hola me llamo Jordi Pozo.
                    Soy profesor de Ciclos Formativos
                """)
        )
    )