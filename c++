
class Solution {
public:
    long long minimumMaxValue(int n, int index, int value) {

        if (value == 1) {
            return -1;
        }

        int p = value;

        // Find smallest prime factor
        for (int i = 2; 1LL * i * i <= value; i++) {
            if (value % i == 0) {
                p = i;
                break;
            }
        }

        if (value - p < 2LL * index) {
            return -1;
        }

        if (index == n - 1) {
            return value;
        }

        long long ans = value + p + 2LL * (n - index - 2);

        return ans;
    }
};
