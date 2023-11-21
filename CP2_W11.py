class TreeNode():
  def __init__(self):
    self.data = None
    self.left = None
    self.right = None

class BinarySearchTree():
  def __init__(self, root):
    self.root = root

  def insert(self, in_data):  # 삽입
    current = self.root
    node = TreeNode()
    node.data = in_data
    while True:
      if in_data < current.data:
        if current.left == None:
          current.left = node
          break
        current = current.left
      else:
        if current.right == None:
          current.right = node
          break
        current = current.right

  def find(self, find_data): # 탐색
    current = self.root
    while True:
      if find_data == current.data:
        print(find_data, '을(를) 찾음. ')
        break
      elif find_data < current.data:
        if current.left == None:
          print(find_data, "이(가) 트리에 없음")
          break
        current = current.left

      else:
        if current.right == None:
          print(find_data, "이(가) 트리에 없음")
          break

        current = current.right

  def delete(self, del_data): # 삭제
    current = self.root
    parent = None
    while True:
      if del_data == current.data:
        if current.left == None and current.right == None:
          if parent.left == current:
            parent.left = None
          else:
            parent.right = None
          del(current)

        elif current.left != None and current.right == None: # 1개의 자식이 왼쪽
          if parent.left == current:
            parent.left = current.left
          else:
            parent.right = current.left
          del(current)

        elif current.left == None and current.right != None: # 1개의 자식이 오른쪽
          if parent.left == current:
            parent.left = current.right
          else:
            parent.right = current.right
          del(current)

        elif current.left != None and current.right != None: # 2개의 자식이 있는 부모 노드 삭제
          tmp_parent = current
          tmp_current = current.right

          while tmp_current.left != None: # 오른쪽에서 가장 작은 값 
            tmp_parent = tmp_current
            tmp_current = tmp_current.left
          current.data = tmp_current.data

          if tmp_parent.left == tmp_current:
            tmp_parent.left = tmp_current.right
          else:
            tmp_parent.right = tmp_current.right


        print(del_data,"이(가) 삭제됨")
        break

      elif del_data < current.data: #삭제해야 할 값이 현재 값보다 작을 때
        if current.left == None:
          print(del_data, "이(가) 트리에 없음")
          break
        parent = current
        current = current.left

      else:                        #삭제해야 할 값이 현재 값보다 클 때
        if current.right == None:
          print(del_data, "이(가) 트리에 없음")
          break
        parent = current
        current = current.right

def preorder(node):
    if node == None:
      return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
  if node == None:
    return
  inorder(node.left)
  print(node.data, end='->')
  inorder(node.right)

def postorder(node):
  if node == None:
    return
  postorder(node.left)
  postorder(node.right)
  print(node.data,end='->')



root = None
nameAry = [8,15,3,9,6]

node = TreeNode()
node.data = 10
root = node

bst = BinarySearchTree(root)
for i in nameAry:
  bst.insert(i)


preorder(root)
print('끝')
bst.delete(8)
preorder(root)
print('끝')
bst.delete(9)
preorder(root)
print('끝')


G1 = None
nameAry = ['A','B','C','D']
A, B, C, D = 0, 1, 2, 3

class Graph():
  def __init__(self,size):
    self.SIZE = size
    self.graph = [[0 for _ in range(size)] for _ in range(size)]

gSize = 4
G1 = Graph(gSize)

G1.graph[A][C] = 1
G1.graph[A][D] = 1

G1.graph[B][C] = 1

G1.graph[C][A] = 1
G1.graph[C][B] = 1
G1.graph[C][D] = 1

G1.graph[D][A] = 1
G1.graph[D][C] = 1

def DFS(graph):
    stack = []
    visitedAry = []
    current = 0

    stack.append(current)
    visitedAry.append(current)

    while stack:
        next = None
        for vertex in range(4):
            if G1.graph[current][vertex] == 1:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break

        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    for i in range(len(visitedAry)):
      visitedAry[i] = chr(ord('A')+visitedAry[i])

    return visitedAry

DFS(G1)