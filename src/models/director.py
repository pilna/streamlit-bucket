from src.models.actions.action import Action
from src.models.context import Context
from src.models.bucket import Bucket
from graphviz import Digraph
from typing import List, Union
from os import getcwd, path


class Director:
    """
    The Director class is used to generate a context cluster from a given context

    Attributes:
        context_cluster: Set
            the set that represent all the context possible.
        objectif: Union[Context, Bucket]
            the objectif you want to retrieve

    Methods:
        set_objectif(new_objectif: Union[Context, Bucket])
            Set the objectif attribute to the new_objectif parameter

        get_result()
            Find results from the objectif of the director.

        add_context(context: Context)
            Add a context to the director

        find_context(target_context: Context)
            Given a target context, return the context in the context 
            cluster of the director that matches the target context.
        
        find_context_with_bucket(bucket: Bucket)
            Find the context that contains the bucket
        
        find_all_context_with_bucket(bucket: Bucket)
            Find all contexts that contain a bucket.

        context_exist(target_context: Context)
            True if the given context is in the context_cluster else False
        
        generate_graph_visualization(directory: str = path.join(getcwd(), "resources"))
            Generate a graph visualization of the context clusters.
    """ 

    def __init__(self) -> None:
        self.context_cluster = set()
        self.objectif = None


    def set_objectif(self, new_objectif: Union[Context, Bucket]) -> None:
        """
        Set the objectif attribute to the new_objectif parameter
        
        Parameter:
            new_objectif: Union[Context, Bucket]
                the objectif you want to retrieve.
        """
        self.objectif = new_objectif


    def get_result(self):
        """
        Find results from the objectif of the director.

        Error:
            ValueError:
                if the objective is not set previously, raise an error.
        """
        if self.objectif is None:
            raise ValueError("the goal was not set before")
        
        if isinstance(self.objectif, Bucket):
            return self.find_all_context_with_bucket(self.objectif)
        return [self.find_context(self.objectif)]


    def add_context(self, context: Context) -> None:
        """
        Add a context to the director
        
        Parameters:
            context: Context
                the context to be added to the director
        """
        self.context_cluster.add(context)
    

    @classmethod
    def generate(cls, initial_context: Context, applyable_actions: List[Action]) -> 'Director':
        """
        Given an initial context and a list of actions, generate a context cluster
        
        Parameters:
            initial_context: Context
                The initial context to create the cluster
            applyable_actions: List[Action]
                A list of actions that can evolve a contexte
        
        Return: Director
            A director class that represent the context cluster.
        """
        context_cluster = cls()
        context_cluster.add_context(initial_context)
        priority_file = [initial_context]

        while priority_file:
            current_context = priority_file.pop(0)
            
            for action in applyable_actions:
                for bucket in current_context.buckets:
                    for context in current_context.apply_action(action, bucket):
                        if context not in context_cluster.context_cluster:
                            context_cluster.add_context(context)
                            priority_file.append(context)
            
        return context_cluster
    

    def find_context(self, target_context: Context) -> Union[Context, None]:
        """
        Given a target context, return the context in the context cluster of the director that matches the target
        context.
        
        Parameters:
            target_context: Context
                The context we're looking for
        
        Returns: Union[Context, None]
            The context that matches the target context.
        """
        return next(
            (
                context
                for context in self.context_cluster
                if target_context == context
            ),
            None,
        )


    def find_context_with_bucket(self, bucket: Bucket) -> Union[Context, None]:
        """
        Find the context that contains the bucket
        
        Parameters:
            bucket: Bucket
                The bucket that we want to find the context for
        
        Returns: Union[Context, None]
            The context that contains the bucket.
        """
        return next(
            (
                context
                for context in self.context_cluster
                if context.contains_bucket(bucket)
            ),
            None,
        )
    

    def find_all_context_with_bucket(self, bucket: Bucket) -> List[Context]:
        """
        Find all contexts that contain a bucket.
        
        Parameters:
            bucket: Bucket
                The bucket that we want to find in context.
        
        Returns: List[Context]
            A list of contexts that contain the bucket.
        """
        return [
            context
            for context in self.context_cluster
            if context.contains_bucket(bucket)
        ]


    def context_exist(self, target_context: Context) -> bool:
        """
        Returns: bool
            True if the given context is in the context_cluster else False
        """
        return self.find_context(target_context) is not None
    

    def __str__(self) -> str:
        """
        The function is used to cast the object in string

        Return: str
            a string that represents the Director object.
        """
        return "\n==================\n".join(str(context) for context in self.context_cluster)


    def generate_graph_visualization(self, directory: str = path.join(getcwd(), "resources")) -> Digraph:
        """
        Generate a graph visualization of the context clusters.
        
        Parameters
            directory: str (optional)
                the directory where the graph will be saved
        """
        dot = Digraph(
            filename="graph", 
            directory=directory
        )

        sorted_context_by_history = sorted(self.context_cluster, key=lambda context: len(context.history))
        objectif_context = self.get_result() if self.objectif is not None else []

        for context in sorted_context_by_history:        
            color = ("red" if context in objectif_context else "black") if context.history else "blue"

            dot.node(
                context.get_representation(),
                color = color
            )

        for first_context in sorted_context_by_history:
            for second_context in sorted_context_by_history:
                if (
                    len(first_context.history) == len(second_context.history) - 1
                    and first_context.history == second_context.history[:-1]
                ):
                    dot.edge(
                        first_context.get_representation(),
                        second_context.get_representation(),
                        label=second_context.history[-1]
                    )

        return dot
