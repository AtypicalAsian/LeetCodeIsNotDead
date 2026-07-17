class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx=max(nums)

        freq=[0]*(mx+1)

        for x in nums:
            freq[x]+=1

        exact=[0]*(mx+1)

        for g in range(mx,0,-1):
            cnt=0

            for m in range(g,mx+1,g):
                cnt+=freq[m]

            exact[g]=cnt*(cnt-1)//2

            for m in range(2*g,mx+1,g):
                exact[g]-=exact[m]

        pref=[0]*(mx+1)

        for g in range(1,mx+1):
            pref[g]=pref[g-1]+exact[g]

        ans=[]

        for x in queries:
            q=x+1

            l,r=1,mx

            while l<r:
                mid=(l+r)//2

                if pref[mid]>=q:
                    r=mid
                else:
                    l=mid+1

            ans.append(l)

        return ans