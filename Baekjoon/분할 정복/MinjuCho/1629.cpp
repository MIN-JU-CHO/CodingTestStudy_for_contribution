// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1629-곱셈-파이썬
// 실행 시간: 0ms 사용 메모리: 2020KB
#include <iostream>

using namespace std;

long long A, C;
long long multiply(long long B)
{
	if (B == 0)
	{
		return 1;
	}
	if (B == 1)
	{
		return A % C;
	}
	else
	{
		long long result = multiply(B / 2);
		if (B % 2 == 0)
		{
			return result * result % C;
		}
		else
		{
			return result * result % C * A % C;
		}
	}
}

int main(void)
{
	long long B;
	cin >> A >> B >> C;
	cout << multiply(B) % C << endl;
}