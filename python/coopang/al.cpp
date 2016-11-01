#include <algorithm>
#include <cstdio>

using namespace std;

char str[2501];
int dp[2500], n;

int main() {
    scanf("%s", str);
    n = strlen(str);
    fill_n(dp, n, -1);
    for(int i=0; i < n; i++){
        printf("%d", dp[i]);
    }
}

