from abc import abstractmethod

from ..note._base import BaseNote


class BaseScale:
    __slots__ = ()

    @property
    @abstractmethod
    def diatonics(self) -> list[BaseNote]: ...
