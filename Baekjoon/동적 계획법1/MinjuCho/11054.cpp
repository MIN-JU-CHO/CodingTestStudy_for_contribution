#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int N = 0;
	cin >> N;

	vector<int> dt(N+2);
	dt[0] = 0;
	dt[N + 1] = 0;
	for (int i = 1; i < N+1; i++)
	{
		cin >> dt[i];
	}

	vector<int> LIS(N + 2, 0);
	vector<int> LISR(N + 2, 0);
	
	// 왼쪽 기준 누적 순위 구하기
	for (int i = 1; i < N + 1; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (dt[j] < dt[i])
			{
				LIS[i] = max(LIS[i], LIS[j] + 1);
			}
		}
	}

	// 오른쪽 기준 누적 순위 구하기
	for (int i = N; i > 0; i--)
	{
		for (int j = N + 1; j > i; j--)
		{
			if (dt[i] > dt[j])
			{
				LISR[i] = max(LISR[i], LISR[j] + 1);
			}
		}
	}

	// LR 더해서 가장 큰 값이 가장 긴 바이토닉 길이
	for (int i = 0; i < N + 2; i++)
	{
		LIS[i] += LISR[i];
	}

	// 자기 자신 원소 중복 빼기
	cout << *max_element(LIS.begin(), LIS.end())-1;
}