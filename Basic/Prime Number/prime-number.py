#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        # code here
        if N==2 or N==3:
            return 1
        else:
            if N%2==0 or N==1:
                return 0
            else:
                Numdivisible=1
                for i in range(1,int(math.sqrt(N))+1):
                    if N%i==0:
                        Numdivisible +=1
                    
                if Numdivisible==2:
                    return 1
                else:
                    return 0
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends