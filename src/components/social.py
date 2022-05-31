import streamlit
import streamlit.components.v1 as components

from src.components.icomponent import IComponent
from typing import Any

class Social(IComponent):
    """
    A class that represents a social media component.

    Attributes:
        label: str
            the label of the social media
        redirect_url: str
            the url to redirect to
        image_url: str
            the url of the image
    
    Methods:
        render(self, attach_to: Any = None) -> None
            render the component.
    """

    def __init__(self, label, redirect_url, image_url):
        """
        Attributes:
            label: str
                the label of the social media
            redirect_url: str
                the url to redirect to
            image_url: str
                the url of the image
        """
        self.label = label
        self.redirect_url = redirect_url
        self.image_url = image_url

    def render(self, attach_to: Any = None) -> None:
        """
        render the component.

        Parameters:
            attach_to (streamlit.component.Component): The component to attach to.
        """
        components.html(
                f'<a target="_blank" style="color: white; text-decoration: none; font-size: 1.3rem; font-weight: bold" href="{self.redirect_url}"> \
                    <div style="text-align: center; display: flex; flex-direction: column; align-items: center">\
                        <img src="{self.image_url}" width="120" />\
                            {self.label} \
                    </div>\
                </a>'
            )