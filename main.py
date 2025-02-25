import flet as ft
from main_imports import *

def main(page: ft.Page):
    
    config = DefaultConfig()
    AddConfigPage(page, config).settings()

    theme = DarkTheme()
    AddTheme(page, theme).theme()

    view = LoginUserView(page)
    NavegationController(page).navegation_to(view)

    page.add()
if __name__ == "__main__":

    ft.app(target=main)
