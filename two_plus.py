'''
����һ���������� nums ��һ��Ŀ��ֵ target�������ڸ��������ҳ���ΪĿ��ֵ���� ���� ���������������ǵ������±ꡣ

����Լ���ÿ������ֻ���Ӧһ���𰸡����ǣ��㲻���ظ��������������ͬ����Ԫ�ء�

ʾ��:

���� nums = [2, 7, 11, 15], target = 9

��Ϊ nums[0] + nums[1] = 2 + 7 = 9
���Է��� [0, 1]

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/two-sum
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        rl=[]
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    rl.append(i)
                    rl.append(j)
        return rl


nums=[2,7,11,15]
target=9
s=Solution() 
print(s.twoSum(nums,target))