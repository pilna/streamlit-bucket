from src.models.actions.action import Action
from src.models.context import Context
from src.models.bucket import Bucket
from typing import List

class Fill(Action):

    def add_trace_to_history(self, context: Context, on_bucket: Bucket) -> None:
        """
        Add a trace to the history of the context
        
        Parameters: 
            context: Context
                the context that we want to update the history
            on_bucket: Bucket
                The bucket that is being Fill
        """
        context.history.append(
            f"Fill the bucket {on_bucket.name}"
        )

    def execute(self, context: Context, on_bucket: Bucket) -> List[Context]:
        """
        Fill the bucket on_bucket and add the trace to the context's history
        
        Parameters:
            context: Context
                the context in which the action is applied
            on_bucket: Bucket
                the bucket to fill
        
        Return: List[Context]
            the list of the new context
        """
        on_bucket = context.get_bucket(on_bucket)
        on_bucket.fill()
        self.add_trace_to_history(context, on_bucket)
        return [context]

    def __str__(self) -> str:
        return "Fill"
