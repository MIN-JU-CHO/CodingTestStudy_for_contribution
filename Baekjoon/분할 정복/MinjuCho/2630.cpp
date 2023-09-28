// 문제 풀이 링크: https://velog.io/@cuppizza/백준-2630-색종이-만들기-파이썬-C
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> paper;
int counts[2] = { 0, 0 };

void div_half(int x, int y, int n)
{
	if (n == 1)
	{
		++counts[paper[x][y]];
	}
	else
	{
		int pivot = paper[x][y];
		bool isPivot = true;
		for (int i = x; i < x + n; ++i)
		{
			for (int j = y; j < y + n; ++j)
			{
				if (paper[i][j] != pivot)
				{
					isPivot = false;
					break;
				}
			}
			if (!isPivot)
			{
				break;
			}
		}
		if (isPivot)
		{
			++counts[paper[x][y]];
			return;
		}
		else
		{
			div_half(x, y, n / 2);
			div_half(x + n / 2, y, n / 2);
			div_half(x, y + n / 2, n / 2);
			div_half(x + n / 2, y + n / 2, n / 2);
		}
	}
}

int main(void)
{
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		vector<int> input(N);
		for (int j = 0; j < N; ++j)
		{
			cin >> input[j];
		}
		paper.push_back(input);
	}
	div_half(0, 0, N);
	cout << counts[0] << endl << counts[1] << endl;
}