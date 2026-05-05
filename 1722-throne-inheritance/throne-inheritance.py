class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = set()
        self.king = kingName
        self.family_tree = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.family_tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # DFS on family tree to get inheritance order
        def dfs(person):
            if person not in self.dead:
                inh_order.append(person)
            for child in self.family_tree[person]:
                dfs(child)
        inh_order = []
        dfs(self.king)
        return inh_order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()