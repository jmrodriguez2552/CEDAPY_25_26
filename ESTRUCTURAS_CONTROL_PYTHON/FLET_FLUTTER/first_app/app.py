import flet as ft

def main(page: ft.Page):
    page.title = "Flet First App"
    page.window.width = 200
    page.window.height = 100
    page.add(ft.Text("Hola, Mundo!"))

ft.app(target=main)