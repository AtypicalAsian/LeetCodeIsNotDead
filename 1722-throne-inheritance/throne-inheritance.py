class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = set()
        self.family_tree = defaultdict(list)
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.family_tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        #DFS Pre-Order to get inheritance order
        inheritance_order = []
        def dfs(node,res):
            if node not in self.dead:
                res.append(node)
            for child in self.family_tree[node]:
                dfs(child,res)
        dfs(self.king, inheritance_order)
        return inheritance_order



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()