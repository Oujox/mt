import typing as t

from .._core import ObjectMT
from ._base import BaseTuner
from .processing.frequency_ratio import (fivelimit_tuning_table,
                                         meantone_tuning_table,
                                         pythagorean_tuning_table)


class JustIntonationTuner(BaseTuner, ObjectMT):

    ratios: t.Final[tuple[float]] = fivelimit_tuning_table()

    def __init__(self, root: float) -> None:
        self.root = root

    def hz(self, notenumber: int) -> float:
        relative_number = notenumber - self.origin_notenumber
        return self.root * (notenumber - self.origin_notenumber)


class MeantoneTuner(BaseTuner, ObjectMT):

    ratios: t.Final[tuple[int]] = meantone_tuning_table()

    def __init__(self, root: float) -> None:
        self.root = root

    def hz(self, note_number: int) -> float:
        return self.root * (note_number - 69)


class PythagoreanTuner(BaseTuner, ObjectMT):

    def __init__(self, root: float) -> None:
        self.root = root

    def hz(self, note_number: int) -> float:
        return self.root * (note_number - 69)


class EqualTuner(BaseTuner, ObjectMT):

    def __init__(self, root: float) -> None:
        self.root = root

    def hz(self, note_number: int) -> float:
        return self.root * 2 ** (
            (note_number - self.setting.notenumber.origin) / self.semitone
        )