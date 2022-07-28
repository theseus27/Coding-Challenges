//Testing
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> problem = {2, 0, 2, 1, 1, 0};
    sortColors(problem);
    for (int i = 0; i < problem.size(); i++) {
        cout << problem[i];
    }
}

//Time Limit Exceeded
void sortColors(vector<int>& nums) {
    //Count occurences of each number
        int red, white, blue = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) red += 1;
            else if (nums[i] == 1) white += 1;
            else if (nums[i] == 2) blue += 1;
            else cerr << "Invaild number" << endl;
        }
        
        //Create new ordered vector
        vector<int> newNums;
        for (int i = 0; i < red; i++) newNums.push_back(0);
        for (int i = 0; i < white; i++) newNums.push_back(1);
        for (int i = 0; i < blue; i++) newNums.push_back(2);
        
        nums = newNums;
}

//Works in Reverse
void sortColors(vector<int>& nums) {
    for (int i = 0; i < nums.size()-1; i++) {
        int start = i;
        int next = 0;
        while (nums[start+next] < nums[start+next+1]) {
            int hold = nums[start+next];
            nums[start+next] = nums[start+next+1];
            nums[start+next+1] = hold;
            next += 1;
        }
}

//Doesn't work bc goes iteratively and skips things that get 
void sortColors(vector<int>& nums) {
    for (int i = 0; i < nums.size()-1; i++) {
        cout << endl << "I   " << i << endl;
        int first = i;
        int second = i+1;
        while (nums[first] >= nums[second] && (second < nums.size())) {
            int hold = nums[first];
            nums[first] = nums[second];
            nums[second] = hold;
            //cout << "Ind1: " << first << "  Ind2: " << second << endl;
            //cout << "1.    " << nums[first] << "   2.   " << nums[second] << endl;
            
            for (int j = 0; j < nums.size(); j++) {
                cout << nums[j];
            }
            cout << endl;
            
            first += 1;
            second += 1;
        }
    }
}