import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    vocab_index = {words : i for i , words in enumerate(vocab)}
    bow = np.zeros(len(vocab),dtype = int)
    for token in tokens:
        if token in vocab_index:
            bow[vocab_index[token]] += 1
    
    return bow