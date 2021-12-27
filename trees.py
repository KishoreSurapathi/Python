class Treenode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def addchild(self, child):
        child.parent = self
        self.children.append(child)

    def node_level(self):
        level = 0
        while self.parent:
            level = level + 1
            self = self.parent
        return level


    def print_tree(self, hierarchy):
        for key in self.data:
            level = self.node_level()

            space = '   ' * level + '|--' if self.parent else ""

            if hierarchy == "name":
                print(space +self.data[key])
                if self.children:
                    for child in self.children:
                        child.print_tree("name")
            elif hierarchy == "designation":
                print(space + key)
                if self.children:
                    for child in self.children:
                        child.print_tree("designation")
            else:
                print(space + self.data[key] + '(' + key + ')')
                if self.children:
                    for child in self.children:
                        child.print_tree("both")

root = Treenode({"CEO" : "Nilpiul"})

cto = Treenode({"CTO":"Chinmay"})
cto.addchild(Treenode({"Infrastructure Head" : "Vishwa"}))
cto.addchild(Treenode({"Application  Head":"Aamir"}))

hr = Treenode({"HR head" : "Gels"})
hr.addchild(Treenode({"Recruitment manager" : "Peter"}))
hr.addchild(Treenode({"Policy manager":"Waqas"}))

root.addchild(cto)
root.addchild(hr)
root.print_tree("both")
