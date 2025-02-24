from flet import Page
from abc import ABC, abstractmethod

class IThemePage(ABC):

    @abstractmethod
    def _background_color(self, page: Page):
        pass
    
    @abstractmethod
    def _widgets_colors(self):
        pass


class LightTheme(IThemePage):

    def _background_color(self, page: Page) -> None:
        page.bgcolor= "#ffffff"

    def _widgets_colors(self):
        pass


class DarkTheme(IThemePage):

    def _background_color(self, page: Page) -> None:
        page.bgcolor= "#1c1f1d"

    def _widgets_colors(self):
        pass


class AddTheme:
    def __init__(self, page: Page, theme_page: IThemePage) -> None:
        self.theme_page = theme_page
        self.page = page

    def theme(self) -> None:
        self.theme_page._background_color(self.page)
        self.theme_page._widgets_colors()
