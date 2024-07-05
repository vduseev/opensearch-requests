from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class Shards(BaseModel):
    total: int = Field(...)
    successful: int = Field(...)
    skipped: int = Field(...)
    failed: int = Field(...)


class Relation(str, Enum):
    eq = "eq"
    gte = "gte"


class Total(BaseModel):
    value: int = Field(...)
    relation: Relation = Field(...)

    class Config:
        use_enum_values = True


class Hit(BaseModel):
    index: str = Field(..., alias="_index")
    id: str = Field(..., alias="_id")
    score: str = Field(..., alias="_score")
    source: Optional[dict[str, Any]] = Field(None, alias="_source")
    fields: Optional[dict[str, list[Any]]] = Field(None)


class Hits(BaseModel):
    total: Total = Field(...)
    max_score: Optional[float] = Field(None)
    hits: list[Hit] = Field(...)


class StdDeviationBounds(BaseModel):
    upper: Optional[float] = Field(None)
    lower: Optional[float] = Field(None)
    upper_population: Optional[float] = Field(None)
    lower_population: Optional[float] = Field(None)
    upper_sampling: Optional[float] = Field(None)
    lower_sampling: Optional[float] = Field(None)


class MatrixAggregation(BaseModel):
    name: Optional[str] = Field(None)
    count: Optional[int] = Field(None)
    mean: Optional[float] = Field(None)
    variance: Optional[float] = Field(None)
    skewness: Optional[float] = Field(None)
    kurtosis: Optional[float] = Field(None)
    covariance: Optional[dict[str, float]] = Field(None)
    correlation: Optional[dict[str, float]] = Field(None)


class BucketAggregation(BaseModel):
    key: str = Field(...)
    doc_count: int = Field(...)


class Aggregation(BaseModel):
    doc_count: Optional[int] = Field(None)
    value: Optional[Any] = Field(None)
    type: Optional[Any] = Field(None)

    count: Optional[int] = Field(None)
    min: Optional[float] = Field(None)
    max: Optional[float] = Field(None)
    avg: Optional[float] = Field(None)
    sum: Optional[float] = Field(None)

    sum_of_squares: Optional[float] = Field(None)
    variance: Optional[float] = Field(None)
    variance_population: Optional[float] = Field(None)
    variance_sampling: Optional[float] = Field(None)
    std_deviation: Optional[float] = Field(None)
    std_deviation_population: Optional[float] = Field(None)
    std_deviation_sampling: Optional[float] = Field(None)
    std_deviation_bounds: Optional[StdDeviationBounds] = Field(None)
    fields: Optional[list[MatrixAggregation]] = Field(None)

    doc_count_error_upper_bound: Optional[int] = Field(None)
    sum_other_doc_count: Optional[int] = Field(None)
    buckets: Optional[list[BucketAggregation]] = Field(None)


class Result(BaseModel):
    scroll_id_: Optional[str] = Field(None, alias="_scroll_id")
    took: int = Field(...)
    timed_out: bool = Field(...)
    shards: Shards = Field(..., alias="_shards")
    hits: Optional[Hits] = Field(None)
    aggregations: Optional[dict[str, Aggregation]] = Field(None)
