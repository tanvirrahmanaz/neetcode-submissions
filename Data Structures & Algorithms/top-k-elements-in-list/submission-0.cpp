class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int , int> map;
        for(auto x: nums){
            int key = x;
            map[key]++;
        }
        

        vector<pair<int, int>> freq_list;
        for(auto &p : map){
            freq_list.push_back({p.first, p.second});
        }

        sort(freq_list.begin(), freq_list.end(), [](auto& a, auto& b){   // ✅ Lambda expression
                return a.second > b.second;
            });

        vector<int> result;
        for(int i=0; i<k ; i++){
            result.push_back(freq_list[i].first);
        }
        return result;
    }
};