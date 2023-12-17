# 定義 tree 類別，表示二元樹的節點
class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

# 定義一個函數 create，用於在樹中插入新節點
def create(root, val):
    newnode = tree()  # 創建一個新的節點
    newnode.data = val
    newnode.left = None
    newnode.right = None
    
    if root == None:
        root = newnode  # 如果根節點是空的，將新節點設為根節點
        return root
    
    else:
        current = root
        while current != None:
            backup = current
            
            # 根據值大小決定往左還是往右移動
            if current.data > val:
                current = current.left
            else:
                current = current.right
                
        # 根據值大小插入新節點
        if backup.data > val:
            backup.left = newnode
        else:
            backup.right = newnode
            
    return root

# 一個數值列表，代表要插入樹中的值
data = [5, 8, 19, 7, 13, 2, 16, 1, 9]

# 初始化指標和根節點
ptr = None
root = None

# 使用 create 函數建立樹
for i in range(9):
    ptr = create(ptr, data[i])
    
# 列印左子樹
print('左子樹建立')
root = ptr.left
while root != None:
    print('%d' % (root.data))
    root = root.left

# 列印右子樹
print("*"*30)
print('右子樹建立')
root = ptr.right
while root != None:
    print('%d' % (root.data))
    root = root.right
