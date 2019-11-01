class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        l=len(s)        
        if s==None or l==0:
            return 0
        start_pos=0
        next_pos=1
        if l==1:
            return 1
        for j in range(1,l):
            start_next=start_pos
            for k in range(start_next,j):
                #print (j)
                #print (s[k])
                #print (s[j])
                #print ('--')
                if s[k]==s[j] :
                    start_pos=k+1
                    #print ('start_next='+str(start_next))
                    if j-start_next>max_len:
                        #print ('before max_len='+str(max_len))    
                        #print (start_next)
                        #print (j)                    
                        max_len=j-start_next
                        #print ('after max_len='+str(max_len))
        if l-start_pos>max_len:
            max_len=l-start_pos

        return max_len