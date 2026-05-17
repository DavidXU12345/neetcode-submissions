class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> counter{};
        priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> minHeap{};
        int currentTime = 0;
        for (char t : tasks)
        {
            counter[t]++;
        }

        for (auto iter = counter.begin(); iter != counter.end(); iter++)
        {
            minHeap.push({INT_MIN, iter->first});
        }

        while (!counter.empty())
        {
            currentTime++;
            auto [time, task] = minHeap.top();
            if (currentTime <= n + time)
            {
                continue;
            }
            
            minHeap.pop();
            if (--counter[task] <= 0)
            {
                counter.erase(task);
            }
            else
            {
                minHeap.push({currentTime, task});
            }
        }
        return currentTime;
    }
};