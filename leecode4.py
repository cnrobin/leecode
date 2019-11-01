

#def findMedianSortedArrays(nums1, nums2) -> float:
def findMedianSortedArrays(nums1, nums2) :
    
    nums3=sorted(nums1+nums2)
    l=len(nums3)
    s=int(l/2)
    y=l%2
    print(nums3)
    if y==0 :
        #return  float(nums3[l/2-1]+nums3[l/2])/2
        
        return float(nums3[s-1]+nums3[s])/2
    else:
        #return float(nums3[l/2-1])
        return float(nums3[s])


anums1=[1,2]
anums2=[3,4]

print (findMedianSortedArrays(anums1,anums2))