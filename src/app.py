from src.router import Router
from src.pages.home import HomePage
from src.components.navbar import NavBar

class Application:
    """
    A class that represent the application.

    Attributes:
        router (Router): The router of the application.

    Methods:
        run() -> None
            Run the application.
    """

    def __init__(self) -> None:
        self.router = Router(HomePage())

    def run(self) -> None:
        """
        run the application.
        """
        NavBar().render()
        self.router.get_current_page().load_page()

