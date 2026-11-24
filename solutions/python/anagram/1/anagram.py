def find_anagrams(word: str, candidates: tuple) -> list:
    word = word.lower()
    anagram = []
    for candidate in candidates:
        if len(word) == len(candidate) and word != candidate.lower():
            if sorted(word) == sorted(candidate.lower()):
                anagram.append(candidate)
    return anagram
