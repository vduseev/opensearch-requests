from typing import Any

from pydantic import Field

from .base import BaseTextQuery
from .options import *


class TermQuery(
    BaseTextQuery,
    FieldOption,
):
    """Search for exact 1:1 match.

    Term-level queries do not produce score. Results of term query
    will have the same score.

    Such queries are well suited for filtration.
    
    Term-level queries are not analyzed. When working with term-level
    queries on text data, only use them for fields mapped as keywords
    or arrays of strings that are explicitly ``not_analyzed``.
    """

    def bare(self) -> dict[str, Any]:
        return {
            "term": {
                self.field: self.query,
            }
        }
