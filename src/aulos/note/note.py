from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

from .._core import Object
from .._core.context import inject
from ._base import BaseNote

if TYPE_CHECKING:
    from scale import Scale


class Note(BaseNote, Object):

    @inject
    def __init__(
        self, identify: int | str, *, scale: t.Optional[Scale] = None, **kwargs
    ) -> None:
        super().__init__(**kwargs)

    def is_notenumber(self, notenumber: t.Any) -> t.TypeGuard[int]:
        return self.scheme.is_notenumber(notenumber)

    def is_notename(self, value: t.Any) -> t.TypeGuard[str]:
        return
