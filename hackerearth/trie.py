import sys

sys.stdin = open('in', 'r')
_ = int(input())
nums = list(map(int, input().split()))


class Trie():

    def __init__(self):
        self._end = '*'
        self.trie = dict()
        self.count = 0

    def __repr__(self):
        return repr(self.trie)

    def make_trie(self, *words):
        trie = dict()
        for word in words:
            temp_dict = trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, {})
            temp_dict[self._end] = self._end
        return trie

    def find_word(self, word):
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]

            else:
                return False
        else:
            if self._end in sub_trie:
                return True
            else:
                return False

    def add_word(self, word):
        if self.find_word(word):
            print("Word Already Exists")
            return self.trie

        temp_trie = self.trie
        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]

            else:
                temp_trie = temp_trie.setdefault(letter, {})
                if letter == "1":
                    self.count += 1

        temp_trie[self._end] = self._end
        return temp_trie

    def get_count(self):
        return self.count


my_trie = Trie()

for i in nums:
    my_trie.add_word(bin(i)[2:])

count = my_trie.get_count()
str_count = str(my_trie.trie).count("1")
