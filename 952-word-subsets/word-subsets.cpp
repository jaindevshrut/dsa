class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<string> ans;
        int flag = 1;
        unordered_map<char,int> maxx;
        for(auto i : words2){
            unordered_map<char,int> x1;
            for(auto x:i){
                x1[x]++;
            }
            for(auto& [ch,freq]:x1){
                maxx[ch] = max(maxx[ch],freq);
            }
        }
        for(auto i : words1){
            unordered_map<char,int> x1;
            for(auto x:i){
                x1[x]++;
            }
            for(auto& [ch,freq]:maxx){
                if(x1[ch] < maxx[ch]){
                    flag = 0;
                    break;
                }
            }
            if(flag){
                ans.push_back(i);
            }
            else{
                flag = 1;
            }
        }
        return ans;
    }
};