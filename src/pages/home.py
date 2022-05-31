import streamlit as st
import streamlit.components.v1 as components

from src.pages.ipage import IPage
from src.components.social import Social

class HomePage(IPage):
    """
    A class that represent the HomePage.

    Methods:
        load_page() -> None
            Load the page.
    """

    def __load_why_section(self) -> None:
        """ 
        This method is used to display the "Why" section of the HomePage.
        """
        st.subheader("🤔 Why i make this ?")

        st.markdown(
            "It all started when I was hanging out on twitch last night ✨. I \
            discovered a wonderful streamer [Datalgo](https://www.twitch.tv/datalgo) who was doing a wonderful \
            stream on streamlit. Having seen him having some difficulty with \
            it and liking challenges I thought why not try to propose my \
            vision of a streamlit application. So here it is 😁"
        )

    
    def __load_about_section(self) -> None:
        """
        This method is used to display the "About" section of the HomePage.
        """
        st.subheader("🧐 About me ?!")

        st.write(
            "I'm currently a student at University of Orléans improving my \
            skill in front-end and back-end development."
        )

        st.write(
            "As a software engineer, I enjoy writing beautiful lines of \
            code filled with many colors to create different kind of magic \
            applications. My goal is to build scalable applications that \
            are easy to maintain."
        )

        st.write(
            "When I'm not in front of my computer, I'm probably practicing \
            sports, eating some interesting food or talking with my friends."
        )

    
    def __load_contact_section(self) -> None:
        """
        this method is used to display the "Contact" section of the HomePage.
        """
        st.subheader("💌 Contact me !")

        col1, col2 = st.columns(2)

        with col1:
            Social(
                label = "Github", 
                redirect_url = "https://github.com/pilna", 
                image_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpluspng.com%2Fimg-png%2Fgithub-logo-png-white-github-11-icon-free-white-social-icons-512x512.png&f=1&nofb=1"
            ).render()
            

        with col2:
            Social(
                label = "LinkedIn",
                redirect_url = "https://www.linkedin.com/in/pilna/",
                image_url = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.vhv.rs%2Ffile%2Fmax%2F8%2F80786_linkedin-logo-white-png.png&f=1&nofb=1"
            ).render()


    def load_page(self) -> None:
        """
        this method is used to load the HomePage.
        """
        st.title("Home")
        st.header("🥳 Hey, nice to see you !")

        self.__load_why_section()
     
        st.markdown("----")

        self.__load_about_section()

        st.markdown("----")

        self.__load_contact_section()
    