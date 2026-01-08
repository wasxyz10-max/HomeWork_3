
import flet as ft
import datetime 

dt_now = datetime.datetime.now()

def main(page: ft.Page):


    text_hello = ft.Text(value='Hello world!')

    def on_button(_):
        time_data = f'{dt_now.strftime('%Y:%m:%d - %H:%M')}:{str(dt_now.second)[:2]}'
        name = input_name.value.strip()

        if name:
            text_hello.value = f'{time_data} - Hello {name}'
            input_name.value = None
        else:
            text_hello.value = 'Введите корректное имя'

    def delete_value(_):
        text_hello.value=None


    scr_button = ft.ElevatedButton('Сохранить', icon=ft.Icons.SEND, on_click=on_button)
    clear_button = ft.ElevatedButton('Очистить', icon=ft.Icons.SEND, on_click=delete_value)
    input_name = ft.TextField(label='Введите имя')


    page.add(input_name, scr_button, clear_button, text_hello)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

