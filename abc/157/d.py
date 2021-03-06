class UFNode:
    def __init__(self, ID):
        self.ID = ID
        self.parent = None
        # size of connected component
        self.cc_size = 1

class UFTree:
    def __init__(self, N):
        self.N = N
        self.nodes = [ UFNode(i) for i in range(N) ]

    def get_root(self, node):
        if node.parent is None:
            return node
        root = self.get_root(node.parent)
        node.parent = root
        return root

    def same(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)
        return root1.ID == root2.ID

    def merge(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)

        if root1.ID == root2.ID:
            return

        if root1.cc_size <= root2.cc_size:
            root1.parent = root2
            root2.cc_size += root1.cc_size
        else:
            root2.parent = root1
            root1.cc_size += root2.cc_size

    def get_cc_size(self, node):
        root = self.get_root(node)
        return root.cc_size

def main():
    N, M, K = map(int, input().split())

    friend_list = [set([]) for i in range(N) ]
    block_list = [set([]) for i in range (N)]

    tree = UFTree(N)

    # friend
    for i in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        friend_list[a].add(b)
        friend_list[b].add(a)
        tree.merge(tree.nodes[a], tree.nodes[b])

    # blocked
    for i in range(K):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        if not tree.same(tree.nodes[a], tree.nodes[b]):
            continue

        # 同じ連結成分であれば後の排除処理のためにリストに追加する
        block_list[a].add(b)
        block_list[b].add(a)

    result = ""
    for i in range(N):
        n = tree.nodes[i]
        result += str(tree.get_cc_size(n) - (len(friend_list[i]) + len(block_list[i]) + 1)) + " "

    print(result[:-1])

main()
