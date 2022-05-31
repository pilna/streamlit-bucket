from src.models.actions.action import Action
from src.models.bucket import Bucket
from typing import List, Union


class Context:
    """
    A class that represent a context.

    Attributes:
        buckets: List[Bucket]
            the bucket of the context.
        history: List[str]
            the history of the previous actions of the context.

    Methods:
        get_bucket(target_bucket: Bucket)
            Return the bucket from this list of buckets that matches the given bucket, 
            or return None if no such bucket exists
        
        contains_bucket(target_bucket: Bucket)
            Return True if the target bucket is in the list of buckets of the current context.
        
        apply_action(action: Action, on_bucket: Bucket)
            Given an action, apply it to the bucket and return the resulting contexts
        
        clone()
            Return a new context object that is a clone of the current one.
        
        get_representation()
            Return a string representation of the buckets in the context
    """

    def __init__(self, buckets: List[Bucket]) -> None:
        """
        Parameters:
            buckets: List[Bucket]
                the list of buckets who is contained by the context
        """
        buckets.sort(key=lambda bucket: bucket.max_volume)
        self.buckets = buckets
        self.history = []
    

    def __eq__(self, context: 'Context') -> bool:
        """
        The function is used to compare two Context objects.
        
        Parameter:
            other_context: Context
                the context you want to compare.
        """
        if not isinstance(context, Context):
            raise TypeError(f"the context type is expected but type {type(context)} is given")

        return all(
            bucket_current_context == bucket_other_context
            for bucket_current_context, bucket_other_context in zip(
                self.buckets, context.buckets
            )
        )


    def get_bucket(self, target_bucket: Bucket) -> Union[Bucket, None]:
        """
        Return the bucket from this list of buckets that matches the given bucket, 
        or return None if no such bucket exists
        
        Parameters:
            target_bucket: Bucket
                The bucket we're looking for
        
        Returns:
            The bucket that matches the target bucket.
        """
        return next(
            (bucket for bucket in self.buckets if target_bucket == bucket), None
        )


    def contains_bucket(self, target_bucket: Bucket) -> bool:
        """
        Return True if the target bucket is in the list of buckets of the current context.
        
        Parameters:
            target_bucket: Bucket
                The bucket to search for
        
        Return: bool
            True if the target bucket is in the list of buckets of the current context else False
        """
        return self.get_bucket(target_bucket) is not None


    def apply_action(self, action: Action, on_bucket: Bucket) -> List['Context']:
        """
        Given an action, apply it to the bucket and return the resulting contexts
        
        Parameters:
            action: Action
                The action that we want to apply to the context
            on_bucket: Bucket
                The bucket who perform the action

        Return: List[Context]
            A list of contexts that have been created from this action.
        """
        return action.execute(self.clone(), on_bucket)
    

    def __hash__(self):
        """
        The __hash__ method is called when we try to convert an object to a hash value. 
        In this case, we want to make sure that when we create a Stock object, 
        the hash value is based on the list of bucket.

        Return: int
            The hash value of the list of bucket.
        """
        return hash(tuple(self.buckets))


    def __str__(self):
        """
        The function is used to cast the object in string

        Return: str
            a string that represents the Context object.
        """
        return ("\n".join(f"{bucket.name} -> {bucket}" for bucket in self.buckets)
            + "\npath to obtain this context: " + " -> ".join(self.history))


    def clone(self) -> 'Context':
        """
        Return a new context object that is a clone of the current one.

        Return: Context
            a new context object that is a clone of the current one.
        """
        clone_context = Context([bucket.clone() for bucket in self.buckets])
        clone_context.history = self.history.copy()
        return clone_context


    def get_representation(self) -> str:
        """
        Return a string representation of the buckets in the context

        Return: str
            A string representation of the buckets of the context.
        """
        return "\n".join(
            f"{bucket.name} = {bucket.current_volume} / {bucket.max_volume}" 
            for bucket in self.buckets
        )
