from typing import Any

from .base import BaseAggregation
from .options import FieldOption


class TermsAggregation(
    BaseAggregation,
    FieldOption,
):
    """Counts number of documents per each field value."""
    # def bare(self) -> dict[str, Any]:
    #     return {
    #         "terms": self.non_empty_dict(),
    #     }
