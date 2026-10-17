def can_construct(ransomNote: str, magazine: str) -> bool:
    """Return True if ransomNote can be built from the letters in magazine.

    Each letter in magazine can only be used once.
    """
    # hash table (dictionary) that stores how many times each letter
    # appears in the magazine
    letter_counts = {}
    for letter in magazine:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # go through the ransom note and use up letters from the magazine
    for letter in ransomNote:
        # letter is missing or already used up, so the note can't be built
        if letter_counts.get(letter, 0) == 0:
            return False
        # use one copy of this letter
        letter_counts[letter] -= 1

    # every letter in the note was found
    return True