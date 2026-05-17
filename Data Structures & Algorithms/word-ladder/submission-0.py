class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        pattern_to_words = defaultdict(set)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_to_words[pattern].add(word)
        
        q = deque()
        visited = set()
        q.append(beginWord)
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                visited.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in pattern_to_words[pattern]:
                        if nei in visited:
                            continue
                        q.append(nei)
        return 0
