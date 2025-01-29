class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        # Inserção BST normal
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Chaves iguais não são permitidas

        # Atualiza a altura do nó atual
        self.update_height(root)

        # Obtém o fator de balanceamento
        balance = self.balance_factor(root)

        # Casos de balanceamento
        # Caso Esquerda-Esquerda
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Caso Direita-Direita
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Caso Esquerda-Direita
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Direita-Esquerda
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder_traversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.key] + self.inorder_traversal(root.right)

    def print_tree(self):
        return self.inorder_traversal(self.root)

# Exemplo de uso
if __name__ == "__main__":
    avl_tree = AVLTree()
    
    # Inserindo alguns valores
    valores = [10, 20, 30, 40, 50, 25]
    for valor in valores:
        avl_tree.insert_key(valor)
    
    print("Árvore AVL em ordem crescente:", avl_tree.print_tree())
