#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        auxA= max(A,B)
        auxB= min(A,B)
        residuo=1;
        if A >= 1 and A <= 10**18 and B >= 1 and B <= 10**18:
        
            while residuo!=0:
                residuo=auxA%auxB
                if residuo==0:
                    GCD=auxB
                else:
                    auxA=auxB
                    auxB=residuo
            LCM= (A*B)//GCD
            return [LCM, GCD]
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends