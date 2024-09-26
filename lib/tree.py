class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        """Find a node with the specified id using depth-first traversal."""
        return self._dfs(self.root, id)

    def _dfs(self, node, element_id):
        """Helper method to perform depth-first traversal."""
        if node is None:
            return None
        
        # Check if the current node matches the desired id
        if node.get('id') == element_id:
            return node
        
        # Traverse the children
        for child in node.get('children', []):
            result = self._dfs(child, element_id)
            if result is not None:
                return result
        
        return None  # Return None if the id is not found
