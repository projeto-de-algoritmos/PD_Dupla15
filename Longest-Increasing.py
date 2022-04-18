class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        # Lista pd com elementos = 1, desde 0 a N
        pd = [1 for k in range(0, n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and pd[i] < pd[j] + 1:
                    pd[i] = pd[j] + 1

        # Ordenamos para pegar o maior elemento do pd (será o tamanho que procuramos)
        pd.sort(reverse=True)
        return pd[0]