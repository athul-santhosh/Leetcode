class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root : return 
        def connect_(node):
            left = node.left
            right = node.right
            while left:
                left.next = right
                left = left.right
                right = right.left
        connect_(root)
        
        # use a dfs:
        def dfs(node):
            if node is None:
                return 
            connect_(node)
            if node.left:
                dfs(node.left)
            if node.right:  
                dfs(node.right)
                
        dfs(root)
        return root