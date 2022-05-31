from streamlit import sidebar, markdown
from typing import Any

from src.components.icomponent import IComponent
import src.router as router

class NavBar(IComponent):
    """
    A class that represents a navbar component.

    Methods:
        render(self, attach_to: Any = None) -> None
            Render the component.
    """

    def __load_css(self) -> None:
        """
        load the css of the component.
        """
        markdown(
            '<style>section[data-testid*="stSidebar"] div[data-testid*="stVerticalBlock"] button {width: 300px !important}</style>',
            unsafe_allow_html=True
        )
    
    def render(self, attach_to: Any = None) -> None:
        """
        render the component.

        Parameters:
            attach_to (streamlit.component.Component): The component to attach to.
        """
        sidebar.header("🚀 Navigation")

        with sidebar.container():
            sidebar.button(
                "🏠 Home", 
                on_click = lambda : router.Router().go_to_page("home"),
            )

            sidebar.button(
                "📈 Data",
                on_click = lambda : router.Router().go_to_page("data")
            )

        self.__load_css()