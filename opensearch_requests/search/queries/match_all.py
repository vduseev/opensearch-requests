from typing import Any, Union

from .base import BaseQuery


class MatchAllQuery(BaseQuery):
    """Matches and returns all documents.

    This type can be useful in testing large document sets if you need
    to return the entire set.
    """

    def bare(self) -> dict[str, Any]:
        return {
            "match_all": {},
        }
