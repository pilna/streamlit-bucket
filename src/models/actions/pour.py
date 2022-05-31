from src.models.actions.action import Action
from src.models.context import Context
from src.models.bucket import Bucket
from typing import List


class Pour(Action):

    def add_trace_to_history(self, context: Context, on_bucket: Bucket, target_bucket: Bucket) -> None:
        """
        Add a trace to the history of the context
        
        Parameters: 
            context: Context
                the context that we want to update the history
            on_bucket: Bucket
                The bucket that is being poured out
            target_bucket: Bucket
                The bucket that is being pour into
        """
        context.history.append(
            f"bucket {on_bucket.name} pour in bucket {target_bucket.name}"
        )


    def _execute(self, context: Context, on_bucket: Bucket, target_bucket: Bucket) -> Context:
        """
        Pour the contents of the on_bucket into the target_bucket and 
        add the trace to the context's history
        
        Parameters:
            context: Context
                the context in which the action is applied
            on_bucket: Bucket
                The bucket that is being poured out
            target_bucket: Bucket
                the bucket to pour into
        
        Return: Context
            The new context that is created by applying the action.
        """
        on_bucket = context.get_bucket(on_bucket)
        target_bucket = context.get_bucket(target_bucket)
        on_bucket.pour_volume_in(target_bucket)
        self.add_trace_to_history(context, on_bucket, target_bucket)
        return context


    def execute(self, context: Context, on_bucket: Bucket) -> List[Context]:
        """
        Applies all ways to perform the action to the current context and return
        all the new context
        
        Parameters:
            context: Context
                the context in which the action is applied
            on_bucket: Bucket
                The bucket that is being poured out
        
        Return: List[Context]
            the new context that is created by applying the action
        """
        return [
            self._execute(context.clone(), on_bucket.clone(), target_bucket.clone())
            for target_bucket in context.buckets
            if target_bucket != on_bucket
        ]

    def __str__(self) -> str:
        return "Pour"
