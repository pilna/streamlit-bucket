from src.pages.data import DataPage
from src.pages.home import HomePage
from src.pages.ipage import IPage
from src.utils.singleton import SingletonMeta


class Router(metaclass=SingletonMeta):
    """
    A class that represent a routing system.

    Attributes:
        current_page (IPage): The current page.

    Methods:
        go_to_page(new_page: str) -> None
            Take string representation of the page you want to go to and
            set the current page to the new page.
        get_current_page() -> IPage
            Return the current page.
    """

    def __init__(self, initial_page: IPage)  -> None:
        """
        Parameters:
            initial_page (IPage): The initial page.
        """
        self.current_page = initial_page

    def go_to_page(self, new_page: str) -> None:
        """
        Take string representation of the page you want to go to and 
        set the current page to the new page.

        Parameters:
            new_page (str): String representation of the page you want to go to.
        
        Errors:
            ValueError: If the new page is not a valid page.
        """
        match new_page:
            case "home":
                self.current_page = HomePage()
            case "data":
                self.current_page = DataPage()
            case _:
                raise ValueError(f"Unknown page {new_page}")
                

    def get_current_page(self)  -> IPage:
        """
        Return the current page.
        
        Returns:
            IPage: The current page.
        """
        return self.current_page