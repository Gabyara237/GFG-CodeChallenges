//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public:
    int evenlyDivides(int N){
        //code here
        int digito=0;
        int evenlyD=0;
        int copyN=N;
        while(N>0){
            digito= N%10;
            if (digito!=0 && copyN%digito==0){
                evenlyD++;
            }
            N/= 10;
        }
        
        return evenlyD;
        
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.evenlyDivides(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends