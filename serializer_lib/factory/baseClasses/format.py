from abc import ABC, abstractmethod
from typing import Any


class Format(ABC):
    """Abstract parent class for all formats."""
    @abstractmethod
    def dump(self, obj: Any, fp: str):
        """Abstract method for dump"""
        pass

    @abstractmethod
    def dumps(self, obj: Any):
        """Abstract method for dumps"""
        pass

    @abstractmethod
    def load(self, fp: str):
        """Abstract method for load"""
        pass

    @abstractmethod
    def loads(self, s: str):
        """Abstract method for loads"""
        pass
