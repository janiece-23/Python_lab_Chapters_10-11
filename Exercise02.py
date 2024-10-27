def value_counts_efficient(word):
    counter = {}
    for l in word:
        counter[1] = counter.get(1, 0) + 1
    return counter

if __name__ == '__main--':
    print(value_counts_efficient("hello"))

