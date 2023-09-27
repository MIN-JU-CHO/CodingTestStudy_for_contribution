// 풀이 참고 링크: https://velog.io/@cuppizza/백준-9251-LCS-파이썬-C
#include <string>
#include <vector>
#include <iostream>

using namespace std;
int main(void)
{
	string A, B;
	cin >> A;
	cin >> B;
	
	A = ' ' + A;
	B = ' ' + B;
	vector<vector<int>> dp (A.length(), vector<int>(B.length(), 0));
	
	// Bottom Up
	for (int i = 1; i < A.length(); ++i)
	{
		for (int j = 1; j < B.length(); ++j)
		{
			if (A.at(i) == B.at(j))
			{
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}

			else
			{
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}

	cout << dp[A.length() - 1][B.length() - 1] << endl;
}