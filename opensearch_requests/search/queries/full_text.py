from typing import Any, Optional

from .base import BaseTextQuery
from .enums import Analyzer
from .options import *


class BaseFullTextQuery(BaseTextQuery):
    """Base class for full text queries."""
    analyzer: Optional[
        Analyzer
    ] = None
    """Type of analyzer to split text into structured text."""

    class Config:
        use_enum_values = True


class MatchQuery(
    BaseFullTextQuery,
    FieldOption,
    FuzzinessOption,
    FuzzyTransportationsOption,
    OperatorOption,
    MinimumShouldMatchOption,
    ZeroTermsQueryOption,
    LenientOption,
    PrefixLengthOption,
    MaxExpansionsOption,
    BoostOption,
):
    """Full-text search of a specific document field.

    The match query analyzes the provided search string and returns
    documents that match any of the string's terms.
    """
    class Config:
        use_enum_values = True

    def bare(self) -> dict[str, Any]:
        return {
            "match": {
                self.field: self.non_empty_dict(exclude={"field"}),
            }
        }


class MultiMatchQuery(
    BaseFullTextQuery,
    FieldsOption,
    TypeOption,
    OperatorOption,
    MinimumShouldMatchOption,
    TieBreakerOption,
    BoostOption,
    FuzzinessOption,
    FuzzyTransportationsOption,
    LenientOption,
    PrefixLengthOption,
    MaxExpansionsOption,
    AutoGenerateSynonymsPhraseQueryOption,
    ZeroTermsQueryOption,
    SlopOption,
):
    """Search multiple fields.

    Multi-match operation functions similarly to the match operation.
    """
    class Config:
        use_enum_values = True

    def bare(self) -> dict[str, Any]:
        return {
            "multi_match": self.non_empty_dict(),
        }


class MatchBoolPrefixQuery(
    BaseFullTextQuery,
    FieldOption,
    FuzzinessOption,
    FuzzyTransportationsOption,
    MaxExpansionsOption,
    PrefixLengthOption,
    OperatorOption,
    MinimumShouldMatchOption,
):
    """Constructs a bool query with the last term used as prefix.

    Each term except the last is used in a ``term`` query. The last term is
    used as a ``prefix`` query. 

    An important difference between the ``match_bool_prefix`` query and
    ``match_phrase_prefix`` is that the ``match_phrase_prefix`` query
    matches its terms as a phrase, but the match_bool_prefix query can
    match its terms in any position.

    Example:

        The query ``quick brown f`` could match with a field containing
        ``quick brown fox``, but it could also match ``brown fox quick``.
        It could also match a field containing the term ``quick``, the term
        ``brown`` and a term starting with ``f``, appearing in any position.

    """
    class Config:
        use_enum_values = True
    
    def bare(self) -> dict[str, Any]:
        return {
            "match_bool_prefix": {
                self.field: self.non_empty_dict(exclude={"field"}),
            }
        }


class MatchPhraseQuery(
    BaseFullTextQuery,
    FieldOption,
    SlopOption,
    ZeroTermsQueryOption,
):
    """Match documents that contain an exact phrase in a specified order.
    
    You can add flexibility to phrase matching by providing the ``slop``
    parameter.
    """
    class Config:
        use_enum_values = True
    
    def bare(self) -> dict[str, Any]:
        return {
            "match_phrase": {
                self.field: self.non_empty_dict(exclude={"field"}),
            }
        }


class MatchPhrasePrefixQuery(
    BaseFullTextQuery,
    FieldOption,
    MaxExpansionsOption,
    SlopOption,
):
    """Match a phrase in specified order.

    The documents that contain the phrase you specify will be returned.
    The last partial term in the phrase is interpreted as a prefix, so
    any documents that contain phrases that begin with the phrase and
    prefix of the last term will be returned.

    Example:

        The query ``quick brown f`` would match ``quick brown fox`` or
        ``two quick brown ferrets``, but not ``the fox is quick and brown``.

    """
    class Config:
        use_enum_values = True
    
    def bare(self) -> dict[str, Any]:
        return {
            "match_phrase_prefix": {
                self.field: self.non_empty_dict(exclude={"field"}),
            }
        }


class QueryStringQuery(
    BaseFullTextQuery,
    DefaultFieldOption,
    TypeOption,
    FuzzinessOption,
    FuzzyTransportationsOption,
    FuzzyMaxExpansionsOption,
    FuzzyPrefixLengthOption,
    MinimumShouldMatchOption,
    DefaultOperatorOption,
    LenientOption,
    BoostOption,
    AllowLeadingWildcardOption,
    EnablePositionIncrimentsOption,
    PhraseSlopOption,
    MaxDeterminedStatesOption,
    TimeZoneOption,
    QuoteFieldSuffixOption,
    QuoteAnalyzerOption,
    AnalyzeWildcardOption,
    AutoGenerateSynonymsPhraseQueryOption,
):
    """Search using a query language with operators.

    The query string query splits text based on operators and analyzes
    each individually.

    When you search using the HTTP request parameters (i.e.
    ``_search?q=wind``), OpenSearch creates a query string query.

    Example:

        ``the wind AND (rises OR rising)``

    """

    class Config:
        use_enum_values = True
    
    def bare(self) -> dict[str, Any]:
        return {
            "query_string": self.non_empty_dict(),
        }


class SimpleQueryStringQuery(
    BaseFullTextQuery,
    FieldsOption,
    FlagsOption,
    FuzzyTransportationsOption,
    FuzzyMaxExpansionsOption,
    FuzzyPrefixLengthOption,
    MinimumShouldMatchOption,
    DefaultOperatorOption,
    LenientOption,
    QuoteFieldSuffixOption,
    AnalyzeWildcardOption,
    AutoGenerateSynonymsPhraseQueryOption,
):
    """Specify multiple arguments delineated by regular expressions.

    Example:

        ``\"rises wind the\"~4 | *ising~2``

    Searches with this type will discard any invalid portions of the string.

    Syntax:
    * `+`:  `and` operator
    * `|`:  `or` operator
    * `*`:  Wildcard
    * `""`: Wrap several words (terms) into a phrase
    * `()`: Wrap a clause for precedense
    * `~n`: Set fuzziness (for example, `wnid~3`)
    * `-`:  Negate term
    """

    class Config:
        use_enum_values = True
    
    def bare(self) -> dict[str, Any]:
        return {
            "simple_query_string": self.non_empty_dict(),
        }
