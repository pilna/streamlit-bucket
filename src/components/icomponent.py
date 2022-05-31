from abc import ABCMeta, abstractmethod
from typing import Any

class IComponent(metaclass=ABCMeta):
    """
    IComponent class is an abstract base class that defines the interface for a component object
    """

    @abstractmethod
    def render(self, attach_to: Any) -> None:
        """
        render the component.

        Parameters:
            attach_to (streamlit.component.Component): The component to attach to.
        """
        raise NotImplementedError("render method must be implemented")