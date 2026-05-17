/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
    unordered_map<Node*, Node*>oldToNew{};
    
    Node* dfs(Node* node)
    {
        if (!node)
        {
            return nullptr;
        }

        auto iter = oldToNew.find(node);
        if (iter != oldToNew.end())
        {
            return iter->second;
        }

        Node* clone = new Node(node->val);
        oldToNew[node] = clone;
        for (Node* nei : node->neighbors)
        {
            clone->neighbors.push_back(dfs(nei));
        }
        return clone;
    }
public:
    Node* cloneGraph(Node* node) 
    {
        return dfs(node);
    }
};
