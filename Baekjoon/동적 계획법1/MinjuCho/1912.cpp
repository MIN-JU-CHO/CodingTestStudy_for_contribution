#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	int N;
	cin >> N;

	vector<int> nums(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> nums[i];
	}

	int maximum = nums[0];
	for (int i = 1; i < N; ++i)
	{
		nums[i] = max(nums[i - 1] + nums[i], nums[i]);
		if (maximum < nums[i])
		{
			maximum = nums[i];
		}
	}

	cout << maximum << endl;
}