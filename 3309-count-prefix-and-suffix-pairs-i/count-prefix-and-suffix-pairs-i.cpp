class Solution {
public:
    int isPrefixAndSuffix(string &str1,string& str2){
        if(str1.size() > str2.size()){
            return 0;
        }
        int x = str1.size();
        for(int i =0; i< x;i++){
            if(str2[i] != str1[i]){
                return 0;
            }
        }
        int j = 0;
        int t = str2.size();
        for(int i = t - x; i < t;i++){
            if(str2[i] != str1[j]){
                return 0;
            }
            j ++;
        }
        return 1;
    }
    int countPrefixSuffixPairs(vector<string>& words) {
        int x = words.size();
        int ans=0; 
        for(int i = 0; i < x-1;i++){
            for(int j = i+1;j<x;j++){
            ans += isPrefixAndSuffix(words[i],words[j]);
            }
        }
        return ans;
    }
};