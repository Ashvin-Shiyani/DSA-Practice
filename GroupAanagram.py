"""Given an array of strings strs, group the anagrams together. You can return the answer in any order."""


def groupAnagrams(self, strs):
    result = {}
    for words in strs:
        word = "".join(sorted(words))
        if word in result:
            result[word].append(words)
        else:
            result[word] = []
            result[word] = [words]
    return list(result.values())
