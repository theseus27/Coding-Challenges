#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

int solution(int T, vector<vector<int>> clips) {
    if(T==0)return 0;
    for(vector<int> &v:clips){
        int x = v[0]-v[1];
        int y = v[1]+v[0];
        v[0]=x>0?x:0;
        v[1]=y;
    }
    sort(begin(clips), end(clips));
    int res = 0;
    for (auto i = 0, st = 0, end = 0; st < T; st = end, ++res) {
        for (; i < clips.size() && clips[i][0] <= st; ++i)
            end = max(end, clips[i][1]);
        if (st == end) return -1;
    }
    return res;
}

int main() {
    vector<vector<int>> clips = {{1, 4, 7, 4, 8}, {2, 3, 4}, {4, 6, 7}};

    cout << solution(2, clips) << endl;
}