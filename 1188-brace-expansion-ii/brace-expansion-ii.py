class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def distribute(L1, L2):
            if L1 and L2:
                output = set()
                for elem1 in L1:
                    for elem2 in L2:
                        output.add(elem1 + elem2)
                return output
            else:
                return L1 or L2
        
        def build_set():
            nonlocal i
            output = set()
            while i < len(expression):
                if expression[i].isalpha():
                    prev = expression[i-1] if i != 0 else None
                    word = ""
                    while i < len(expression) and expression[i].isalpha():
                        word += expression[i]
                        i += 1
                    if prev == "}":
                        output = distribute(output, {word})
                    else:
                        output.add(word)
                elif expression[i] == ",":
                    i += 1
                    return output | build_set()
                elif expression[i] == "{":
                    i += 1
                    output = distribute(output, build_set())
                else:
                    i += 1
                    return output
            return output
        
        i = 0
        return sorted(list(build_set()))