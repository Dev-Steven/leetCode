def rangeSumBST(self, root, L, R):
    def dfs(root):
        if not root:
            return
        if L <= root.val <= R:
            self.res += root.val
        if L <= root.val:
            dfs(root.left)
        if R >= root.val:
            dfs(root.right)
    self.res = 0
    dfs(root)
    return self.res