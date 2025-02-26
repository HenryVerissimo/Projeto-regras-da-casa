from flet import Page
from src.controllers import LoginNavegationController

def login_for_create_cont_constructor(page: Page):

    LoginNavegationController(page).navegation()


