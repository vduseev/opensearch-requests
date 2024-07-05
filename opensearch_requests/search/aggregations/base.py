import logging
from typing import Any, Optional, Union

from pydantic import BaseModel, Field

from ..result import Result
from ..queries import BaseQuery


logger = logging.getLogger("opensearch_requests")


class BaseAggregation(BaseModel):
    """Base class for all aggregations."""
    size: Optional[int] = Field(None)
    """Maximum number of results to return in the aggregation."""
    name: str = Field(...)
    """Name of the aggregation."""
    filter: Optional[BaseQuery] = Field(None)
    """Filter to apply."""
    aggs: Optional[list["BaseAggregation"]] = Field(None)
    """Nested aggregations."""

    def bare(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        if self.filter:
            result["filter"] = self.filter.bare()
        if self.aggs:
            aggs: dict[str, Any] = {}
            for a in self.aggs:
                aggs[a.name] = a.bare()
            result["aggs"] = aggs
        other_fields = self.non_empty_dict()
        result.update(**other_fields)
        return result
    
    def body(self) -> dict[str, Any]:
        """Serialize aggregations to dict suitable for API request."""
        b = {
            "aggs": {
                self.name: self.bare()
            }
        }
        if self.size is not None:
            b["size"] = self.size
        return b

    def non_empty_dict(
        self, exclude: Optional[Union[set, dict]] = None
    ) -> dict[str, Any]:
        if exclude is None:
            exclude: set[str] = set()
        if isinstance(exclude, set):
            exclude = exclude.union({"size", "name"})
        elif isinstance(exclude, dict):
            exclude["size"] = True
            exclude["name"] = True

        return self.dict(
            exclude=exclude,
            exclude_none=True,
            exclude_unset=True,
        )

    def search(self, index: str, client) -> Result:
        # Make sure client object has search function as an
        # attribute that is callable
        if not (hasattr(client, "search") and callable(client.search)):
            raise RuntimeError("Wrong OpenSearch client object passed")

        body = self.body()
        logger.info(f"Aggregation body for search: {body}")

        response = client.search(
            index=index,
            body=self.body()
        )

        return Result(**response)

