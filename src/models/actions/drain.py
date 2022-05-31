from src.models.actions.action import Action
from src.models.context import Context
from src.models.bucket import Bucket
from typing import List


class Drain(Action):
    
    def add_trace_to_history(self, context: Context, on_bucket: Bucket) -> None:
        """
        Add a trace to the history of the context
        
        Parameters: 
            context: Context
                the context that we want to update the history
            on_bucket: Bucket
                The bucket that is being Drain
        """
        context.history.append(
            f"Drain the bucket {on_bucket.name}"
        )

    def execute(self, context: Context, on_bucket: Bucket) -> List[Context]:
        """
        Drain the bucket and add the trace to the history
        
        Parameters:
            context: Context
                the context in which the action is applied
            on_bucket: Bucket
                the bucket to drain
        
        Return: List[Context]
            the list of the new context
        """
        on_bucket = context.get_bucket(on_bucket)
        on_bucket.drain()
        self.add_trace_to_history(context, on_bucket)
        return [context]

    def __str__(self) -> str:
        return "Drain"
