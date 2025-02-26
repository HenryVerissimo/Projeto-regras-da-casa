from src.views.create_cont_view import CreateContView
from flet import Page



class LoginNavegationController:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.view = CreateContView(page)
    
    def navegation(self) -> None:
        self.page.controls.clear()
        self.page.controls.append(self.view.build())

        self.page.update()