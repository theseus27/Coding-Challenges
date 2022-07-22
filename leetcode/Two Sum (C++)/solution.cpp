class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>solution = {};
        
        //Create hash map (value, index)
        map<int, int>m;
        for (int i = 0; i < nums.size(); i++) {
            m.insert({nums[i], i});
        }
        
        //Check match for each number
        for (int i = 0; i < nums.size(); i++) {
            int match = target-nums[i];
            cout << "Curr: " << nums[i] << endl;
            cout << "Match: " << match << endl;
            auto iter = m.find(match);
            if (iter != m.end() && iter->second != i) {
                solution.push_back(iter->second);
                solution.push_back(i);
                return solution;
            }
            cout << endl;
        }
        
        return solution;

    }
};