from collections import defaultdict
def group_anagrams(words):
  anagram_map=defaultdict(list)
  for word in words:
    key=''.join(sorted(word))
    anagram_map[key].append(word)
  return list(anagram_map.values())
words=["eat","tea","silent","listen","bat","tab","sky"]
print(group_anagrams(words))
