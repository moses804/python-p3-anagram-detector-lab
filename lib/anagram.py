class Anagram:
    """Class to find anagrams of a given word.

    Usage:
        a = Anagram("listen")
        a.match(['enlists', 'google', 'inlets', 'banana'])  # -> ['inlets']

    Behavior notes (compatible with common anagram katas):
    - Matching is case-insensitive (uses casefold for robust case folding).
    - Identical words (ignoring case) are NOT considered anagrams and are excluded.
    - Returns the matching candidates in the same order they were provided.
    """

    def __init__(self, word: str):
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        # store original and a normalized (casefolded) sorted-letter representation
        self.word = word
        self._normalized = self._normalize(word)
        # store sorted letters value without overriding the method
        self._sorted_letters_value = self._sorted_letters(self._normalized)

    @staticmethod
    def _normalize(s: str) -> str:
        """Normalize a string for comparisons: strip whitespace and casefold."""
        return s.strip().casefold()

    @staticmethod
    def _sorted_letters(s: str) -> list:
        """Return the sorted list of characters for the string s."""
        return sorted(list(s))

    def match(self, candidates: list) -> list:
        """Return a list with all candidates that are anagrams of the initialized word.

        Args:
            candidates: iterable of strings to test.

        Returns:
            A list containing the candidates (in original form) that are anagrams.
        """
        if candidates is None:
            return []

        matches = []
        for cand in candidates:
            # skip non-strings silently (keeps behaviour simple for tests)
            if not isinstance(cand, str):
                continue

            cand_norm = self._normalize(cand)
            # identical words (case-insensitive) are not anagrams
            if cand_norm == self._normalized:
                continue

            if self._sorted_letters(cand_norm) == self._sorted_letters_value:
                matches.append(cand)

        return matches
