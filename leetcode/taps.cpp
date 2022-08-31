int minTaps(int n, vector<int> &ranges) {
        vector<vector<int>> coverage;
        for (int i = 0; i < ranges.size(); i++) {
            coverage.push_back({i - ranges[i], i + ranges[i]});
        }
        sort(coverage.begin(), coverage.end());
        
        int i = 0, start = 0, end = 0, taps = 0;
        while (start < n) {
            while (i < ranges.size() && coverage[i][0] <= start) {
                end = max(end, coverage[i][1]);
                i++;
                if (start == end) return -1;
            }
            start = end;
            taps++;
        }
        return taps;
}