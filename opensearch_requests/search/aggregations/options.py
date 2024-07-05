from typing import Optional

from pydantic import BaseModel, Field


class FieldOption(BaseModel):
    field: str = Field(...)
    """Name of the specific document field to aggregate."""


class FieldsOption(BaseModel):
    fields: list[str] = Field(...)
    """Fields to aggregate: ``["taxful_price", "base_price"]``."""


class PrecisionThresholdOption(BaseModel):
    precision_threshold: Optional[int] = Field(None)
    """Threshold below which counts are expected to be close to accurate."""


class SigmaOption(BaseModel):
    sigma: Optional[int] = Field(None)
    """Configure standard deviation for std_deviation_bounds."""


class SizeOption(BaseModel):
    """Number of top unique terms to request.
    
    Defaults to 10.
    """
    size: Optional[int] = Field(None)
