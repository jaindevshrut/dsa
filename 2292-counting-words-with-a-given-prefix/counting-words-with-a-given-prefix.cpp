class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int size_pref = pref.size();
        int ans = 0;
        for(auto i : words){
            if(i.size() < size_pref){
                continue;
            }
            if(i.substr(0,size_pref) == pref) ans ++;
        }
        return ans;
    }
};