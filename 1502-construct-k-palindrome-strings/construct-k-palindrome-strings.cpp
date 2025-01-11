class Solution {
public:
    bool canConstruct(string s, int k) {
        if(s.size() < k){
            return false;
        }
        unordered_map<char,int> map;
        for(auto i: s){
            map[i] ++;
        }
        // number of 1st < k
        int one_count = 0;
        for(auto& [ch,freq] : map){
            if(freq % 2){
                one_count ++;
            }
        }
        if(one_count > k){
            return false;
        }
        return true;
    }
};