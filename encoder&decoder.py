def encode(strs):
    result = ""
    for word in strs:
        result += str(len(word))+"#" + word
    return result


def decode(result):
    words = []
    i = 0
    while i < len(result):
        j = result.index("#", i)
        length = int(result[i:j])
        word = result[j+1:j+1+length]
        words.append(word)
        i = j+1+length
    return words
