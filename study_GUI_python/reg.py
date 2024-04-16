import flet as f # Переименовываем библиотеку

def main(page: f.Page):
    page.title = "Регистрация" # Название
    page.theme_mode = "dark"  # light # Тема приложения
    page.vertical_alignment = f.MainAxisAlignment.CENTER #Отцентровка
    page.window_width = 350 #Ширина окна
    page.window_height = 400 #Высота окна
    page.window_resizable = False #Возможность растягивания

f.app(target=main)