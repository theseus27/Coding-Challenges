//Copy vector to set
set <int> s;
copy(nums.begin(), nums.end(), inserter(s, s.end()));

int idx = 0;
for (int x:nums) {
    if (s.find(target-x) != s.end()) {
        vector<int>iterator first = find(nums.begin(), nums.end(), x);
        vector<int>iterator second = find(nums.begin(), nums.end(), target-x);
        if (first != second) {
            result.push_back(first);
            result.push_back(second);
            return result;
        }
    }
    idx += 1
}
return result; 
