from typing import Any

from .base import BaseAggregation
from .options import *


class SumAggregation(
    BaseAggregation,
    FieldOption,
):
    """Returns sum value of a field."""
    # def bare(self) -> dict[str, Any]:
    #     return = super().bare()
    #     result["sum"]
    #      {
    #         "sum": self.non_empty_dict(),
    #     }


class MinAggregation(
    BaseAggregation,
    FieldOption,
):
    """Returns minimum value of a field."""
    def bare(self) -> dict[str, Any]:
        return {
            "min": self.non_empty_dict(),
        }


class MaxAggregation(
    BaseAggregation,
    FieldOption,
):
    """Returns maximum value of a field."""
    def bare(self) -> dict[str, Any]:
        return {
            "max": self.non_empty_dict(),
        }


class AvgAggregation(
    BaseAggregation,
    FieldOption,
):
    """Returns average value of a field."""
    def bare(self) -> dict[str, Any]:
        return {
            "avg": self.non_empty_dict(),
        }


class CardinalityAggregation(
    BaseAggregation,
    FieldOption,
    PrecisionThresholdOption,
):
    """Counts number of unique values in a field."""
    def bare(self) -> dict[str, Any]:
        return {
            "cardinality": self.non_empty_dict(),
        }


class ValueCountAggregation(
    BaseAggregation,
    FieldOption,
):
    """Calculates number of values that this aggregation is based on."""
    def bare(self) -> dict[str, Any]:
        return {
            "value_count": self.non_empty_dict(),
        }


class StatsAggregation(
    BaseAggregation,
    FieldOption,
):
    """Returns all basic metrics in one aggregation query.
    
    Includes: min, max, sum, avg, and value_count.
    """
    def bare(self) -> dict[str, Any]:
        return {
            "stats": self.non_empty_dict(),
        }


class ExtendedStatsAggregation(
    BaseAggregation,
    FieldOption,
    SigmaOption,
):
    """Returns extended metrics in one aggregation query.
    
    Apart from basic stats (min, max, sum, avg, value_count) also returns
    stats such as sum_of_squares, variance, and std_deviation.
    """
    def bare(self) -> dict[str, Any]:
        return {
            "extended_stats": self.non_empty_dict(),
        }


class MatrixStatsAggregation(
    BaseAggregation,
    FieldsOption,
):
    """Generates advanced stats for multiple fields."""
    def bare(self) -> dict[str, Any]:
        return {
            "matrix_stats": self.non_empty_dict(),
        }