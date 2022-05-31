from src.components.icomponent import IComponent
from typing import Any
import streamlit as st

class BucketInput(IComponent):
    """
    A class that represents a bucket input component.

    Attributes:
        id: str
            the name of the bucket (that it be unique)
        current_volume: int
            The current volume of the bucket
        max_volume: int
            The maximum volume of the bucket
        key: str (optional)
            The key of the component
    
    Methods:
        render(self, attach_to: Any = None) -> None
            Render the component.
    """

    def __init__(
        self, 
        id: str = "", 
        current_volume: int = 0, 
        max_volume: int = 5, 
        key: str = None
    ) -> None:
        """
        Attributes:
            id: str
                the name of the bucket (that it be unique)
            current_volume: int
                The current volume of the bucket
            max_volume: int
                The maximum volume of the bucket
            key: str (optional)
                The key of the component
        """
        self.key = key
        self.id = id
        self.current_volume = current_volume
        self.max_volume = max_volume

    def render(self, attach_to: Any = st) -> None:
        """
        render the component.

        Parameters:
            attach_to (streamlit.component.Component): The component to attach to.
        """
        self.id = attach_to.text_input(
            'Bucket Name',
            value=self.id,
            key=self.id if self.key is None else self.key
        )

        self.current_volume = attach_to.number_input(
            "Insert current volume of bucket",
            min_value=0,
            value=0,
            step=1,
            key=self.id if self.key is None else self.key
        )

        self.max_volume = attach_to.number_input(
            "Insert max volume of bucket",
            min_value=0,
            step=1,
            key=self.id if self.key is None else self.key
        )