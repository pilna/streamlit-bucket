from abc import ABCMeta, abstractmethod


class IPage(metaclass=ABCMeta):
    """
    Ipage class is an abstract base class that defines the interface for a page object

    Methods:
        load_page(self) -> None
            Load the page.
    """

    @abstractmethod
    def load_page(self) -> None:
        """
        load the page.
        """
        raise NotImplementedError("load_page method must be implemented")
