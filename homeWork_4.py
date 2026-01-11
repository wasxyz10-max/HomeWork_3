
import flet as ft

def main(page: ft.Page):
    hello_text = ft.Text('Hello world')
    hello_history = ft.Text('История приветов:')
    history_hello = []

    def click_button(_):
        name = name_input.value

        if name:
            hello_text.value = None
            hello_text.value = f'Hello {name}'
            name_input.value = None
            history_hello.append(name)
            hello_history.value = f'История приветов: \n' + '\n'.join(history_hello)
        else:
            hello_text.value = None
            hello_text.value = 'Введите корректное имя'

    def del_button(_):
        if history_hello:
            history_hello.pop()

        if history_hello:
            hello_history.value = 'История приветов:\n' + '\n'.join(history_hello)
        else:
            hello_history.value = 'История пуста'
            hello_text.value = 'Hello world'


    dele_history = ft.ElevatedButton('Удалить последнее имя', icon=ft.icons.Icons.DELETE, on_click=del_button)
    name_input = ft.TextField(label='Введите имя', on_click=click_button, expand=True)
    save_button = ft.ElevatedButton('Сохранить имя', icon=ft.Icons.SEND, on_click=click_button)
    his_del = ft.Row([hello_history,dele_history], alignment=ft.MainAxisAlignment.SPACE_AROUND)
    group_input = ft.Row([name_input,save_button], alignment=ft.MainAxisAlignment.CENTER)
    hello_row = ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(hello_row, group_input,his_del)



ft.app(target=main, view=ft.AppView.WEB_BROWSER)