from src.views.login_user_view import LoginUserView
from flet import Page

class CreateContController:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.view = LoginUserView(page)
    
    def navegation(self) -> None:
        self.page.controls.clear()
        self.page.controls.append(self.view.build())

        self.page.update()