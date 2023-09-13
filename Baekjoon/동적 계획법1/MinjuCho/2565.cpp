#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	int N;
	cin >> N;

	// B 배열 0 ~ 500 전부 501로 초기화
	int a, b, B[501];
	fill_n(B, 501, 501);
	for (int i = 0; i < N; ++i)
	{
		cin >> a >> b;
		B[a] = b;
	}

	// dp 배열 0 ~ 500 전부 1로 초기화
	int dp[501];
	fill_n(dp, 501, 1);
	for (int a = 1; a < 501; ++a)
	{
		for (int j = 1; j < a; ++j)
		{
			if (B[j] < B[a] && B[a] != 501)
			{
				// 안겹치는 경우 찾기
				dp[a] = max(dp[j] + 1, dp[a]);
			}
		}
	}
	cout << N - *max_element(dp, dp + 501);
}