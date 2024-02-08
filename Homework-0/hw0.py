import collections
import math
from typing import List, Set, Tuple

############################################################
# Custom Type
# NOTE: You should not modify this.

Position = Tuple[int, int]


############################################################
# Problem 5a

def find_alphabetically_first_word(text: str) -> str:
    """
    Given a string `text`, return the word in `text` that comes first
    alphabetically (i.e., the word that would come first after sorting).
    A word is defined by a maximal sequence of characters without whitespaces.

    Hint: You might find min() handy here. If the input text is an empty string,
    it is acceptable to either return an empty string or throw an error.
    """
    # BEGIN_YOUR_CODE
    words = text.split()
    return min(words) if words else ''
    # END_YOUR_CODE


############################################################
# Problem 5b

def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., `loc1` could be (3, 5)).
    """
    # BEGIN_YOUR_CODE
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(loc1, loc2)))
    # END_YOUR_CODE


############################################################
# Problem 5c

def find_non_singleton_words(text: str) -> Set[str]:
    """
    Split the string `text` by whitespace and return the set of words that
    occur more than once.

    Hint: You might find it useful to use collections.Counter.
    """
    # BEGIN_YOUR_CODE
    word_counts = collections.Counter(text.split())
    return {word for word, count in word_counts.items() if count > 1}
    # END_YOUR_CODE


############################################################
# Problem 5d

def mutate_sentences(sentence: str) -> List[str]:
    """
    Given a sentence (string of space-separated words), return a list of all
    "similar" sentences.

    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
      - For sentences with less than 2 words, you may return an empty list.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 10 lines of code)
    words = sentence.split()
    if len(words) < 2:
        return []
    
    pairs = collections.defaultdict(list)
    for first, second in zip(words, words[1:]):
        pairs[first].append(second)
    
    results = set()
    for word in set(words):
        def dfs(word, path):
            if len(path) == len(words):
                results.add(' '.join(path))
                return
            for next_word in pairs.get(word, []):
                dfs(next_word, path + [next_word])
                
        dfs(word, [word])
    return list(results)
    # END_YOUR_CODE


if __name__ == "__main__":
    # feel free to modify this for testing purposes
    print(mutate_sentences('the cat and the mouse'))
