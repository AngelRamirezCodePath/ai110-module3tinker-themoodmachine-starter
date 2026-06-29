# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Steps:
          1. Strip leading/trailing whitespace and lowercase.
          2. Split on whitespace.
          3. Strip punctuation from each token so "happy!" matches "happy".

        Skipped for now (not worth the complexity on this dataset):
          - Emoji detection: no emojis in current posts.
          - Repeated-char normalization ("soooo"): posts use clean spelling.
        """
        import string

        cleaned = text.strip().lower()
        raw_tokens = cleaned.split()

        # Strip leading/trailing punctuation from each token.
        # .strip(chars) only touches the ends, so mid-word apostrophes
        # in contractions like "don't" are preserved.
        tokens = [t.strip(string.punctuation) for t in raw_tokens]
        tokens = [t for t in tokens if t]  # drop tokens that were pure punctuation

        print(f"[preprocess] input  : {text!r}")
        print(f"[preprocess] tokens : {tokens}")

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Base rule:
          - Positive word → +1
          - Negative word → -1

        Enhancement — negation:
          If the token immediately before a sentiment word is a negation word
          ("not", "never", "don't", etc.), the score delta is flipped.
          Example: "not happy" scores -1 instead of +1.

        Skipped: word frequency, weighting, emoji signals — the current
        dataset is too small and clean to benefit from those yet.
        """
        NEGATION_WORDS = {"not", "never", "no", "don't", "doesn't", "didn't", "can't", "won't"}
        # Negation stays active for this many tokens after the negation word.
        # Window of 3 handles "not feel tired" (gap of 2) without over-reaching.
        NEGATION_WINDOW = 3

        tokens = self.preprocess(text)
        score = 0
        negation_remaining = 0

        for token in tokens:
            if token in NEGATION_WORDS:
                negation_remaining = NEGATION_WINDOW
                continue  # negation word itself carries no sentiment score

            negated = negation_remaining > 0
            negation_remaining = max(0, negation_remaining - 1)

            if token in self.positive_words:
                delta = -1 if negated else +1
                score += delta
                print(f"[score_text] '{token}' → {delta:+d}  (negated={negated})")
            elif token in self.negative_words:
                delta = +1 if negated else -1
                score += delta
                print(f"[score_text] '{token}' → {delta:+d}  (negated={negated})")

        print(f"[score_text] final score = {score}")
        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        Thresholds (intentional choice: ±1, not ±2):
          - All non-zero scores in this dataset are ±1, so raising the bar
            would collapse most predictions to "neutral". Not worth it yet.

        Mixed detection:
          - Score == 0 can mean two things: no sentiment words fired (neutral),
            or positive and negative words fired and cancelled out (mixed).
          - We distinguish them by checking whether both sides had hits.
        """
        score = self.score_text(text)

        if score > 0:
            return "positive"
        if score < 0:
            return "negative"

        # Score is 0: check whether signals cancelled out (mixed) or nothing fired (neutral).
        tokens = self.preprocess(text)
        has_positive = any(t in self.positive_words for t in tokens)
        has_negative = any(t in self.negative_words for t in tokens)
        if has_positive and has_negative:
            return "mixed"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
