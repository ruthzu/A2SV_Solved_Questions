class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        set_responses=[]
        for response in responses:
            response=list(set(response))
            for word in response:
                set_responses.append(word)

        set_responses.sort()
        freq=Counter(set_responses)
        

        maxi=0
        for k,v in freq.items():
            if maxi<v:
                ans=k
                maxi=v
                
        return ans