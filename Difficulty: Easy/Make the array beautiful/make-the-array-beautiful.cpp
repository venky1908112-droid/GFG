class Solution {
  public:
    bool diff_sign(int a, int b){
            if(a < 0 && b < 0) return false;
            if(a >= 0 && b >= 0) return false;
            return true;
        }
        
    vector<int> makeBeautiful(vector<int> a) {
        // code here
        
        stack<int>st;
        int n=a.size();
        for(auto x: a){
            if(st.empty()) st.push(x);
            
            else if(diff_sign(st.top(), x)) st.pop();
            
            else st.push(x);
        }
        vector<int>res;
        
        while(!st.empty())
        {
            res.push_back(st.top());
            st.pop();
        }
        
        reverse(res.begin(), res.end());
        
        return res;
        
    }
};