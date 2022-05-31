from abc import ABC, abstractmethod
from src.models.bucket import Bucket
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.context import Context

class Action:

    @abstractmethod
    def execute(self, context: 'Context', on_bucket: Bucket) -> List['Context']:
        raise NotImplementedError()
