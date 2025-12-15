import flet as ft 


# Pasos a realizar en UBUNTU:
# pip install flet
# sudo apt install libmpv-dev libmpv2 mpv
# ls /usr/lib/x86_64-linux-gnu/libmpv.so*  # para verificar la instalación de libmpv
# sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so.2 /usr/lib/x86_64-linux-gnu/libmpv.so.1  # crear enlace simbólico si es necesario


# Estructura básica de la aplicación y setup de la página
def main(page: ft.Page):
    page.title = "Conversor de temperatura"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 500
    page.window_height = 600
    page.window_resizable = True
    page.padding = 20
    
    # Elementos de la interfaz
    celsius_input = ft.TextField(
        label="Temperatura en Celsius", 
        hint_text="Ingresa la temperatura en º Celsius", 
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: convertir_a_celsius(e.control.value)
    )
    
    fahrenheit_input = ft.TextField(
        label="Temperatura en Fahrenheit", 
        hint_text="Ingresa la temperatura en º Fahrenheit", 
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: convertir_a_farenheit(e.control.value))
    
    kelvin_input = ft.TextField(
        label="Temperatura en Kelvin", 
        hint_text="Ingresa la temperatura en º Kelvin", 
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: convertir_a_kelvin(e.control.value)
        )
    
    # Función de conversión
    def convertir_a_celsius(valor):
        if valor and valor.strip():
            try:
                celsius = float(valor)
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15
                
                fahrenheit_input.value = f"{fahrenheit:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()
                
            except ValueError:
                celsius_input.value = f"Entrada inválida"
    
    def convertir_a_farenheit(valor):
        if valor and valor.strip():
            try:
                fahrenheit = float(valor)
                celsius = (fahrenheit - 32) * 5/9
                kelvin = celsius + 273.15
                
                celsius_input.value = f"{celsius:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()
                
            except ValueError:
                celsius_input.value = f"Entrada inválida"

    def convertir_a_kelvin(valor):
        if valor and valor.strip():
            try:
                kelvin = float(valor)
                celsius = kelvin - 273.15
                fahrenheit = (celsius * 9/5) + 32
                
                fahrenheit_input.value = f"{fahrenheit:.2f}"
                celsius_input.value = f"{celsius:.2f}"
                page.update()
                
            except ValueError:
                celsius_input.value = f"Entrada inválida"
    
    def borrar_campos(e):
        celsius_input.value = ""
        fahrenheit_input.value = ""
        kelvin_input.value = ""
        page.update()

    # Crear la UI principal
    page.add(
        ft.Column(
            [
                ft.Text(
                    "Conversor de Temperatura", 
                    size=24, 
                    weight="bold", 
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.BLUE_700
                    ),
                ft.Divider(height=20),
                celsius_input,
                ft.Divider(height=10),
                fahrenheit_input,
                ft.Divider(height=10),
                kelvin_input,
                ft.Divider(height=20),
                
                ft.ElevatedButton(
                    "Borrar",
                    icon = ft.Icons.DELETE,
                    on_click=borrar_campos,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.RED_400,
                        color=ft.Colors.WHITE,
                    ),
                ),
                
                ft.Divider(height=20),
                
                ft.Container(
                    content=ft.Column(
                        [
                         ft.Text("Fórmulas de conversión:", weight="bold"),
                         ft.Text("°F = (°C × 9/5) + 32"),
                         ft.Text("°C = (°F - 32) × 5/9"),
                         ft.Text("°K = °C + 273.15"),
                        ],
                        spacing=5),
                    padding=ft.padding.all(15),
                    bgcolor=ft.Colors.GREY_100,
                    border_radius=10,        
                )               
            ],
            scroll="auto",
            spacing=0,
        )
    )
        
    
# Ejecución de la aplicación
if __name__ == "__main__":
    ft.app(target=main)
    