import reflex as rx

config = rx.Config(
    app_name="PROYECTO_RFX",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)