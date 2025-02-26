import flet as ft
from main_imports import *

def main(page: ft.Page):
    
    config = DefaultConfig()
    AddConfigPage(page, config).settings()

    theme = DarkTheme()
    AddTheme(page, theme).theme()

    page.controls.append(LoginUserView(page).build())

    page.update()
    
if __name__ == "__main__":

    ft.app(target=main)
