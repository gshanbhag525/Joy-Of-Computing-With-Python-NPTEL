str=input()
def isOneFlip(str): 
  
    sum = 0
    n = len(str)  
    for i in range( 0, n ): 
        sum += int(str[i]) - int('0') 
   
    return (sum==n-1 or sum==1) 
  

(print("YES",end='') if isOneFlip(str)  
                        else print("NO",end=''))
