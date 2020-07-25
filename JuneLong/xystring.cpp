//Result: 100/100 Accepted
//C++ solution
#include <bits/stdc++.h>
using namespace std;

#define str string
#define lli long long int
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t;
	cin >> t;
	
	while(t--)
	{
	    str s;
	    cin >> s;
	    lli count = 0;
	    int index = 0;
	    
	    while(index < s.length()-1)
	    {
	        if(s[index] != s[index+1])
	        {
	            count+=1;
	            index+=2;
	        }
	        else
	        {
	            index+=1;
	        }
	    }
	    cout << count << '\n';
	    
	}
	return 0;
}
