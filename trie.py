def make_trie(*args):
    """
    Make a trie by given words.
    """
    trie = {}
 
    for word in args:
        if type(word) != str:
            raise TypeError("Trie only works on str!")
        temp_trie = trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, {})
        temp_trie = temp_trie.setdefault('_end_', '_end_')
 
    return trie
 
 
def in_trie(trie, word):
    """
    Detect if word in trie.
    """
    if type(word) != str:
        raise TypeError("Trie only works on str!")
 
    temp_trie = trie
    for letter in word:
        if letter not in temp_trie:
            return False
        temp_trie = temp_trie[letter]
    return True
 
 
def remove_from_trie(trie, word, depth):
    """
    Remove certain word from trie.
    """
    if word and word[depth] not in trie:
        return False
 
    if len(word) == depth + 1:
        del trie[word[depth]]
        if not trie:  # Node becomes a leaf, indicate its parent to delete it.
            return True
        return False
    else:
        temp_trie = trie
 
        # Recursively climb up to delete.
        if remove_from_trie(temp_trie[word[depth]], word, depth + 1):
            if temp_trie:
                del temp_trie[word[depth]]
            return not temp_trie
    return False
 
 
# if __name__ == '__main__':
#     trie = make_trie('hello', 'abc', 'baz', 'bar', 'barz')
#     print trie
 
#     print in_trie(trie, 'hello')
#     print in_trie(trie, 'bar')
#     print in_trie(trie, 'bab')
#     print in_trie(trie, 'zzz')
 
    