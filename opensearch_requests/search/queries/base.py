import logging
from typing import Any, Optional, Union

from pydantic import BaseModel, Field

from ..result import Result


logger = logging.getLogger("opensearch_requests")


class BaseQuery(BaseModel):
    """Base class for all queries."""
    size: Optional[int] = Field(None)
    """Maximum number of results to return in the query."""

    def bare(self) -> dict[str, Any]:
        raise NotImplementedError
    
    def body(self) -> dict[str, Any]:
        """Serialize query to dict suitable for API request.
        """
        b = { "query": self.bare() }
        if self.size is not None:
            b["size"] = self.size
        return b

    def non_empty_dict(
        self, exclude: Optional[Union[set, dict]] = None
    ) -> dict[str, Any]:
        if exclude is None:
            exclude: set[str] = set()
        if isinstance(exclude, set):
            exclude = exclude.union({"size"})
        elif isinstance(exclude, dict):
            exclude["size"] = True
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
        logger.info(f"Query body for search: {body}")

        response = client.search(
            index=index,
            body=self.body()
        )

        return Result(**response)


class BaseTextQuery(BaseQuery):
    """Base class for full text queries."""
    query: str = Field(...)
    """Value to match."""
