//Not in actual code, just to make it run externally
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result = {};
    for (int i = 0; i < nums.size(); i++) {
        int curr = nums[i];
        int key = target-curr;
        auto itr = find(nums.cbegin(), nums.cend(), key);
        if (itr != nums.cend()) {
            result.push_back(i);
            result.push_back(distance(nums.cbegin(), itr));
            return result;
        }
    }
    return result;
}

int main() {
    vector<int> problem = {3, 2, 4};
    vector<int> solution = twoSum(problem, 6);
    cout << solution[0] << " " << solution[1] << endl;

    return 0;
}