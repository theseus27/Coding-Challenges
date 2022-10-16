#include <vector>
#include <iostream>
using namespace std;

bool canJump(vector<int>& nums) {
    int target = nums.size()-1;
    
    for(int i = nums.size()-1; i >= 0; i--) {
        if(nums[i] + i >= target)
            target = i;
    }
    return target == 0;
}

int main() {
    vector<int> nums = {1, 2, 3};
    cout << canJump(nums) << endl;
    return 0;
}

// vATTEMPT 1

// bool canJump(vector<int>& nums) {
//     if (nums.size() == 1) return true;
//     find_jumps(nums, nums.size()-1);
//     for (int i = 0; i < nums.size(); i++)
//         if (nums[i] != 0)   return true;
//     return false;
// }

// void find_jumps(vector<int> &nums, int target) {
//     for (int i = 0; i < target; i++) {
//         if (nums[i] != 0) {
//             if (i + nums[i] < target) nums[i] = 0;
//             else find_jumps(nums, i);
//         }
//     }
// }

//ATTEMPT 2

// bool canJump(vector<int>& nums) {
//         if (nums[0] >= nums.size()) return true;
//         find_jumps(nums, nums.size()-1);
        
//         for (int i = 1; i < nums.size()-1; i++) {
//             if (nums[i] != 0)   cout << i << endl;
//         }
        
//         for (int i = 1; i < nums.size()-1; i++)
//             if (nums[i] != 0)   return true;
//         return false;
//     }
    
//     bool find_jumps(vector<int> &nums, int target) {
//         if (nums[0] >= target) return true;
        
//         bool remaining = false;
//         for (int i = 0; i < nums.size(); i++) {
//             if (nums[i] != 0) remaining = true;
//         }
        
//         if (remaining) {
//             for (int i = 1; i < target; i++) {
//                 if (nums[i] != 0) {
//                     if (i + nums[i] < target) nums[i] = 0;
//                     else {
//                         if (!find_jumps(nums, i)) nums[i] = 0;
//                     }
//                 }
//             }
//         }
//     return false;
//     }
// };



// /*
//     bool jump(int curr, vector<int> nums) {
//         if (curr == nums.size() - 1) return true;
        
//         bool good_jump = false;
//         for (int i = curr+1; i <= curr+nums[curr]; i++) {
//             if (i < nums.size())
//                 if (jump(i, nums))  good_jump = true;
//         }
//         return good_jump;
//     }
// */
