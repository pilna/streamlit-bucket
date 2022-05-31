from turtle import onclick
import streamlit as st

from src.components.bucket_input import BucketInput
from src.models.actions.drain import Drain
from src.models.actions.fill import Fill
from src.models.actions.pour import Pour
from src.models.director import Director
from src.models.context import Context
from src.models.bucket import Bucket
from src.pages.ipage import IPage

class DataPage(IPage):
    """
    A class that represent the data page.

    Attributes:
        actions: List[str]
            the list of the actions that can be applied
        active_actions: List[str]
            the list of the actions that are currently active
        buckets: List[BucketInput]
            the list of the buckets
        bucket_number: int
            the number of the buckets
        graphviz: str
            the graphviz representation of the solution
        objectif_bucket: Bucket
            the bucket that is the objectif

    methods:
        load_page:
            load the page.
    """

    def __init__(self) -> None:
        """
        Attributes:
            actions: List[str]
                the list of the actions that can be applied
            active_actions: List[str]
                the list of the actions that are currently active
            buckets: List[BucketInput]
                the list of the buckets
            bucket_number: int
                the number of the buckets
            graphviz: str
                the graphviz representation of the solution
            objectif_bucket: Bucket
                the bucket that is the objectif
        """
        self.objectif_bucket = BucketInput(key="objectif")
        self.actions = [Drain(), Fill(), Pour()]
        self.active_actions = []
        self.bucket_number = 1
        self.graphviz = None
        self.buckets = []


    def __calculate_solution(self) -> None:
        """
        calculate the solution of the bucket problem and generate 
        the graphviz of the visualization of it.
        """
        initial_context = Context(
            [
                Bucket(
                    bucket_input.id,
                    bucket_input.max_volume,
                    bucket_input.current_volume,
                )
                for bucket_input in self.buckets
            ]
        )

        director = Director.generate(
            initial_context,
            self.active_actions
        )

        director.set_objectif(
            Bucket(
                self.objectif_bucket.id,
                self.objectif_bucket.max_volume,
                self.objectif_bucket.current_volume
            )
        )

        self.graphviz = director.generate_graph_visualization()


    def __load_preset_input(self) -> None:
        """
        load the preset input of the page.
        """
        self.active_actions = st.multiselect(
            "Authorize actions",
            self.actions
        )

        self.bucket_number = st.number_input(
            "Insert number of bucket",
            min_value=0,
            value=1,
            step=1
        )


    def __load_bucket_input(self) -> None:
        """
        load the bucket input of the page.
        """
        columns = st.columns(3)

        self.buckets = [BucketInput(i) for i in range(self.bucket_number)]

        for i, bucket in enumerate(self.buckets):
            columns[bucket.id % 3].write(f"Bucket n°{i}:")
            bucket.render(columns[bucket.id % 3])


    def __load_graphviz(self) -> None:
        """
        display the graphviz of the solution if he was calculate.
        """
        if self.graphviz is not None:
            st.graphviz_chart(self.graphviz)


    def __load_objectif_bucket(self) -> None:
        """
        load the objectif bucket of the page.
        """
        _, col, _ = st.columns(3)
        col.write("Objectif bucket:")
        self.objectif_bucket.render(col)
        col.button("Calculate", on_click=self.__calculate_solution)


    def load_page(self) -> None:
        """
        load the page.
        """
        st.title("Data")

        self.__load_preset_input()

        st.markdown("----")

        self.__load_bucket_input()
        self.__load_objectif_bucket()
        self.__load_graphviz()
    