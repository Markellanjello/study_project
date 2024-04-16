import flet as f
import requests

def main(page: f.Page):
    page.title = "Погода"
    page.theme_mode = "dark"  # light
    page.vertical_alignment = f.MainAxisAlignment.CENTER

    user_data = f.TextField(label='Введите город', width=400)
    weather_data = f.Text('')
    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = '3d9de74844d28377e81415151cbe6a66'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value ='Погода: ' + str(temp)
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        f.Row(
            [
                f.IconButton(f.icons.SUNNY, on_click=change_theme),
                f.Text('Погодная программа')
            ],
            alignment=f.MainAxisAlignment.CENTER
        ),
        f.Row([user_data], alignment=f.MainAxisAlignment.CENTER),
        f.Row([weather_data], alignment=f.MainAxisAlignment.CENTER),
        f.Row([f.ElevatedButton(text='Получить', on_click=get_info)], alignment=f.MainAxisAlignment.CENTER)
    )


f.app(target=main)
