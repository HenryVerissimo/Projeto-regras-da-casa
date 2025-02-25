from flet import Page
from src.views.interface_view import InterfaceView


class NavegationController:
    
    def __init__(self, page: Page) -> None:
        self.page = page
    
    def navegation_to(self, view: InterfaceView):
        self.page.controls.clear()
        self.page.controls.append(view.build())

        self.page.update()
