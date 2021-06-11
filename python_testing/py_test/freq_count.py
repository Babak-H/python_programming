# Frequency Counter (inside an String)
def freq_counter_a(s) -> str:
    '''
    function that finds most frequent letters, then joins it together in most common order and
    returns it as string
    '''
    try:
        # I assume that we are interested in characters, regardless of the capitalization
        s = s.lower()
        # sort s string based on repetition of each value from least repeated to most
        return ''.join(sorted(s, key=lambda c: s.count(c), reverse=True)).replace(" ", "")
    except (AttributeError, TypeError) as e:
        print(e)


def freq_counter_b(s) -> str:
    '''
    function that finds most frequent letters, returns them by most common order, without repetition
    '''
    try:
        s = s.lower()
        counter = Counter(s)
        return ''.join(char for char, freq in counter.most_common()).replace(" ", "")
    except (AttributeError, TypeError) as e:
        print(e)
