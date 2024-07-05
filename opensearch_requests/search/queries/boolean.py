from typing import Any, Optional

from pydantic import Field

from .base import BaseQuery


class BooleanQuery(BaseQuery):
    must: Optional[list[BaseQuery]] = Field(None)
    should: Optional[list[BaseQuery]] = Field(None)
    minimum_should_match: Optional[int] = Field(None, example=1)
    must_not: Optional[list[BaseQuery]] = Field(None)
    filter: Optional[list[BaseQuery]] = Field(None)

    def bare(self) -> dict[str, Any]:
        result = {
            "bool": {},
        }

        if self.must:
            result["bool"]["must"] = [q.bare() for q in self.must]
        if self.should:
            result["bool"]["should"] = [q.bare() for q in self.should]
        if self.must_not:
            result["bool"]["must_not"] = [q.bare() for q in self.must_not]
        if self.filter:
            result["bool"]["filter"] = [q.bare() for q in self.filter]
        if self.minimum_should_match is not None:
            result["bool"]["minimum_should_match"] = self.minimum_should_match

        return result
