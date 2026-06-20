class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i + 1:]].append(word)

        q = deque([beginWord])
        visited = set()
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visited.add(word)
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            q.append(nei)
            res += 1
        
        return 0
