class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        for num in range(low,high+1):
            x=str(num)
            n=len(x)
            if n%2==0 :
                mid=n//2
                left_sum=sum(map(int,x[mid:]))
                right_sum=sum(map(int,x[:mid]))
                if left_sum==right_sum :
                    count+=1
        return count

        


        