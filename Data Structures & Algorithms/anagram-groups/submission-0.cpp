class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        for (string word: strs){
            string key = word;
            sort(key.begin(), key.end());
            map[key].push_back(word);
        }

        vector<vector<string>> ans;

        for(auto item: map){
            ans.push_back(item.second);
        }

        return ans;
    }
};
