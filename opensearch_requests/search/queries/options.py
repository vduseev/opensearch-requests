from typing import Optional

from pydantic import BaseModel, Field

from .enums import Operator, Rewrite, QueryType, ZeroTermsQuery


class AllowLeadingWildcardOption(BaseModel):
    allow_leading_wildcard: Optional[bool] = Field(None)
    """Whether * and ? are allowed as the first character of a search term.
    
    The default is true.
    """


class AnalyzeWildcardOption(BaseModel):
    analyze_wildcard: Optional[
        bool
    ] = Field(None)
    """Whether OpenSearch should attempt to analyze wildcard terms.
    
    Some analyzers do a poor job at this task, so the default is false.
    """


class AutoGenerateSynonymsPhraseQueryOption(BaseModel):
    auto_generate_synonyms_phrase_query: Optional[
        bool
    ] = Field(None)
    """Automatically generate phrase queries for multiple term synonyms.

    For example, if you have the synonym "ba, batting average" and search
    for “ba," OpenSearch searches for ba OR "batting average" when the
    option is true or ba OR (batting AND average) when the option is false.
    By default it is set to true.
    """


class BoostOption(BaseModel):
    boost: Optional[float] = Field(None)
    """Boosts the clause by the given multiplier.
    Useful for weighing clauses in compound queries. The default is 1.0.
    """


class DefaultFieldOption(BaseModel):
    default_field: Optional[str] = Field(None)


class DefaultOperatorOption(BaseModel):
    default_operator: Optional[
        Operator
    ] = Field(None)


class EnablePositionIncrimentsOption(BaseModel):
    enable_position_incriments: Optional[bool] = Field(None)
    """When true, result queries are aware of position increments.
    
    This setting is useful when the removal of stop words leaves
    an unwanted “gap" between terms. The default is true.
    """


class FieldOption(BaseModel):
    field: str = Field(...)
    """Name of the specific document field to match."""


class FieldsOption(BaseModel):
    fields: Optional[list[str]] = Field(None)
    """Fields to search: ``["title^4", "description"]``.

    The ^ lets you "boost" certain fields. Boosts are multipliers that
    weigh matches in one field more heavily than matches in other fields.

    If unspecified, defaults to the index.query.default_field setting,
    which defaults to ["*"].
    """


class FlagsOption(BaseModel):
    flags: Optional[str] = Field(None)


class FuzzinessOption(BaseModel):
    fuzziness: Optional[
        int
    ] = Field(None)
    """The number of character edits to change one word into another.

    Number of inserts, deletes, or substitutes that it takes to change
    one word to another when determining whether a term matched a value.
    For example, the distance between wined and wind is 1.
    The default, AUTO (-1 or None), chooses a value based on the length
    of each term and is a good choice for most use cases.
    """


class FuzzyMaxExpansionsOption(BaseModel):
    fuzzy_max_expansions: Optional[
        int
    ] = Field(None)
    """Limit of expanded matching terms due to fuzziness.

    Fuzzy queries "expand to" a number of matching terms that are within
    the distance specified in fuzziness.
    Then OpenSearch tries to match those terms against its indexes.
    """


class FuzzyPrefixLengthOption(BaseModel):
    fuzzy_prefix_length: Optional[
        int
    ] = Field(None)


class FuzzyTransportationsOption(BaseModel):
    fuzzy_transportations: Optional[
        bool
    ] = Field(None)
    """If true, distance between ``wind`` and ``wnid`` is 1, otherwise it's 2.

    Setting fuzzy_transpositions to true (default) adds swaps of adjacent
    characters to the insert, delete, and substitute operations of the
    fuzziness option. For example, the distance between wind and wnid
    is 1 if fuzzy_transpositions is true (swap "n" and "i") and 2 if
    it is false (delete "n", insert "n"). If fuzzy_transpositions is false,
    rewind and wnid have the same distance (2) from wind, despite the more
    human-centric opinion that wnid is an obvious typo.
    The default is a good choice for most use cases.
    """


class LenientOption(BaseModel):
    lenient: Optional[
        bool
    ] = Field(None)
    """Ignore data type mismatches.

    Setting lenient to true lets you ignore data type mismatches between
    the query and the document field. For example, a query string
    of "8.2" could match a field of type float. The default is false.
    """


class LowFreqOperatorOption(BaseModel):
    low_freq_operator: Optional[Operator] = Field(None)
    """The operator for low-frequency terms.
    
    The default is OR.
    """


class MaxExpansionsOption(BaseModel):
    max_expansions: Optional[
        int
    ] = Field(None)
    """Specifies the maximum number of terms to which the query can expand.
    
    When set, value must be a positive integer. The default is 50.
    """


class MaxDeterminedStatesOption(BaseModel):
    max_determined_states: Optional[int] = Field(None)
    """Maximum number of states for regex.

    The maximum number of “states" (a measure of complexity) that Lucene
    can create for query strings that contain regular expressions
    (e.g. "query": "/wind.+?/").
    Larger numbers allow for queries that use more memory.
    The default is 10 000.
    """


class MinimumShouldMatchOption(BaseModel):
    minimum_should_match: Optional[
        int
    ] = Field(None)
    """Number of terms that should match if OR operator is set.

    If the query string contains multiple search terms and you used
    the OR operator, the number of terms that need to match for the
    document to be considered a match.
    For example, if minimum_should_match is 2, "wind often rising"
    does not match "The Wind Rises." If minimum_should_match is 1,
    it matches.

    When set, value must be positive or negative integer, positive or
    negative percentage, or combination.
    """


class OperatorOption(BaseModel):
    operator: Optional[
        Operator
    ] = Field(None)
    """Match all terms in query (AND) or at least one (OR).

    If the query string contains multiple search terms, whether all terms
    need to match (and) or only one term needs to match (or) for a document
    to be considered a match.
    """


class PhraseSlopOption(BaseModel):
    phrase_slop: Optional[int] = Field(None)
    """Slop value for the phrase."""


class PrefixLengthOption(BaseModel):
    prefix_length: Optional[
        int
    ] = Field(None)
    """The number of leading characters that are not considered in fuzziness.
    
    The default is 0.
    """


class QuoteAnalyzerOption(BaseModel):
    quote_analyzer: Optional[str] = Field(None)


class QuoteFieldSuffixOption(BaseModel):
    quote_field_suffix: Optional[
        str
    ] = Field(None)
    """Search exact sub-field if terms are wrapped in quotes.

    This option lets you search different fields depending on whether terms
    are wrapped in quotes.
    For example, if ``quote_field_suffix`` is ``".exact"`` and you search for
    ``"lightly"`` (in quotes) in the ``title`` field, OpenSearch searches the
    ``title.exact`` field. This second field might use a different type
    (e.g. keyword rather than text) or a different analyzer.

    The default is null.
    """


class RewriteOption(BaseModel):
    rewrite: Optional[Rewrite] = Field(None)
    """Determines how OpenSearch rewrites and scores multi-term queries.
    
    The default is ``ConstantScore``.
    """


class SlopOption(BaseModel):
    slop: Optional[int] = Field(None)
    """How far words in a query can be misordered and still be a match.
    
    From the Lucene documentation: "The number of other words permitted
    between words in query phrase. For example, to switch the order
    of two words requires two moves (the first move places the words
    atop one another), so to permit re-orderings of phrases, the slop
    must be at least two. A value of zero requires an exact match."

    The default is 0. If set, value must be a postitive integer.
    """


class TieBreakerOption(BaseModel):
    tie_breaker: Optional[float] = Field(None)
    """Changes the way OpenSearch scores searches.
    
    For example, a ``type`` of ``best_fields`` typically uses the highest
    score from any one field. If you specify a ``tie_breaker`` value
    between 0.0 and 1.0, the score changes to highest
    score + ``tie_breaker`` * score for all other matching fields. If you
    specify a value of 1.0, OpenSearch adds together the scores for all
    matching fields (effectively defeating the purpose of best_fields).
    """


class TimeZoneOption(BaseModel):
    time_zone: Optional[str] = Field(None)
    """Number of hours to offset the derired time zone from UTC.

    Specifies the number of hours to offset the desired time zone
    from UTC. You need to indicate the time zone offset number
    if the query string contains a date range. For example, set
    ``time_zone: "-08:00"`` for a query with a date range such as
    "query": "wind rises release_date[2012-01-01 TO 2014-01-01]").
    
    The default time zone format used to specify number of offset
    hours is UTC.
    """


class TypeOption(BaseModel):
    type: Optional[QueryType] = Field(None)
    """Determines how OpenSearch executes the query and scores the results.

    The default is BestFields.
    """


class ZeroTermsQueryOption(BaseModel):
    zero_terms_query: Optional[
        ZeroTermsQuery
    ] = Field(None)
    """Match NONE or ALL documents, if analyzer removes all terms from query.

    If the analyzer removes all terms from a query string, whether
    to match no documents (default) or all documents.
    For example, the stop analyzer removes all terms from the string
    "an but this."
    """

    class Config:
        use_enum_values = True
