class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        seen = dict()
        for k in range(len(knowledge)):
            seen[knowledge[k][0]] = knowledge[k][1]

        res = []
        flag = False
        for j in range(len(s)):
            cb = False
            if s[j] == '(':
                i=j
                flag = True
            
            if s[j] == ')':
                cb = True
                if s[i+1:j] in seen:
                    res.append(seen[s[i+1:j]])
                else:
                    res.append('?')
                flag = False
            
            if flag:
                continue
            
            else:
                if cb:
                    continue
                res.append(s[j])
            
            j+=1
        
        return "".join(res)