from enum import Enum


class Analyzer(str, Enum):
    standard = "standard"
    """Parses strings into terms at word boundaries, removes punctuation.
    
    Parsing is per the Unicode text segmentation algorithm. It removes most,
    but not all, punctuation. It converts strings to lowercase.
    You can remove stop words if you turn on that option, but it does
    not remove stop words by default.
    """
    simple = "simple"
    """Splits a string into tokens on any non-letter character.

    Removes non-letter characters. Converts strings to lowercase.
    """
    whitespace = "whitespace"
    """Parses strings into terms between each whitespace."""
    stop = "stop"
    """Splits strings into tokens at each non-letter character.
    
    It also removes stop words (e.g., “but” or “this”) from strings.
    Removes non-letter characters. Converts strings to lowercase.
    """
    keyword = "keyword"
    """Outputs the entire string as one term."""
    pattern = "pattern"
    """Splits strings into terms using regular expressions.
    
    Supports converting strings to lowercase. It also supports
    removing stop words.
    """
    language = "language"
    """Provides analyzers specific to multiple languages."""
    fingerprint = "fingerprint"
    """Creates a fingerprint to use as a duplicate detector."""


class Operator(str, Enum):
    AND = "and"
    OR = "or"


class ZeroTermsQuery(str, Enum):
    NONE = "none"
    ALL = "all"


class Rewrite(str, Enum):
    ConstantScore = "constant_score"
    ScoringBoolean = "scoring_boolean"
    ConstantScoreBoolean = "constant_score_boolean"
    TopTermsN = "top_terms_N"
    TopTermsBoostN = "top_terms_bost_N"
    TopTermsBlendedFreqsN = "top_terms_blended_freqs_N"


class QueryType(str, Enum):
    BestFields = "best_fields"
    MostFields = "most_fields"
    CrossFields = "cross_fields"
    Phrase = "phrase"
    PhrasePrefix = "phrase_prefix"
