//Result:100/100

#include <bits/stdc++.h>
using namespace std;

#define lli long long int 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t;
	cin>> t;
	while(t--)
	{
	    int n, k;
	    cin >> n >> k;
	    lli total1 = 0;
	    lli total2 = 0;
	    
	    for(int i = 0; i < n; ++i)
	    {
	        int entry;
	        cin >> entry;
	        if(entry > k)
	        {
	            total2+=k;
	        }
	        else
	        {
	            total2+=entry;
	        }
	        
	        total1+=entry;
	        
	    }
	    
	    cout << abs(total1-total2) << '\n';
	    
	}
	return 0;
}