def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.
    """
    indices = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword
    Принимает список документов (каждый документ представляет собой строку) и список ключевых слов.
     Возвращает словарь, в котором каждый ключ является ключевым словом, а значение - списком индексов.
     (из doc_list) документов, содержащих это ключевое слово
    """
    dic = dict()
    for word in keywords:
        dic[word] = word_search(doc_list, word)
    print(dic)


doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
multi_word_search(doc_list, keywords)
    # {'casino': [0, 1], 'they': [1]}