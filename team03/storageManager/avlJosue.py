import subprocess
def addChr(string):
    number=0
    for x in string:
        print("caracter: " + x + ",   ASCII: " + str(ord(x)))
        number+=ord (x)
    print("la suma ASCII: " +  str(number))
    return number

class node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree
        self.height = 1  # height of node in tree (max dist to leaf)NEW FOR AVL
    
    def __str__(self):
        string = "desde NODO: " + str(self.value)
        return string



class AVLTree:
    TREE_COMPLETE = 0
    TREE_INORDER = 1
    TREE_PREORDER = 2
    TREE_POSORDER = 3

    # variables contains txt data for generated the graphic
    txt_nodes = ""
    txt_link = ""
    txt_json = ""

    def __init__(self):
        self.root = None


    def getSide(self, node):
        if node.parent is None:
            return "<--Root-->"
        else:
            if node.key > node.parent.key:
                return "--Right--"
            else:
                return "--Left--"

    def insert(self, key, value):
        if self.root is None:
            self.root = node(key, value)
        else:
            self._insert(key, value, self.root)

    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child is None:
                current_node.left_child = node(key, value)
                current_node.left_child.parent = current_node  # set parent
                self._inspect_insertion(current_node.left_child)
            else:
                self._insert(key, value, current_node.left_child)
        elif key > current_node.key:
            if current_node.right_child is None:
                current_node.right_child = node(key, value)
                current_node.right_child.parent = current_node  # set parent
                self._inspect_insertion(current_node.right_child)
            else:
                self._insert(key, value, current_node.right_child)
        else:
            # The key doesn't insert in the tree, because already exist in tree
            print("key already in tree!")

    def find(self, key):
        if self.root != None:
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, current_node):
        if key == current_node.key:
            return current_node
        elif key < current_node.key and current_node.left_child != None:
            return self._find(key, current_node.left_child)
        elif key > current_node.key and current_node.right_child != None:
            return self._find(key, current_node.right_child)

    def search(self, key):
        if self.root is not None:
            return self._search(key, self.root)
        else:
            return False

    def _search(self, key, cur_node):
        if key == cur_node.key:
            return True
        elif key < cur_node.key and cur_node.left_child is not None:
            return self._search(key, cur_node.left_child)
        elif key > cur_node.key and cur_node.right_child is not None:
            return self._search(key, cur_node.right_child)
        return False

    
    def delete_value(self,key):
	    return self.delete_node(self.find(key))

    def delete_node(self,node):

		## -----
		# Improvements since prior lesson

		# Protect against deleting a node not found in the tree
        if node==None or self.find(node.key)==None:
            print("Node to be deleted not found in the tree!")
            return None 
		## -----

		# returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current

		# returns the number of children for the specified node
        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children

		# get the parent of the node to be deleted
        node_parent=node.parent

		# get the number of children of the node to be deleted
        node_children=num_children(node)

		# break operation into different cases based on the
		# structure of the tree & node to be deleted

		# CASE 1 (node has no children)
        if node_children==0:

            if node_parent!=None:
				# remove reference to the node from the parent
                if node_parent.left_child==node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root=None

		# CASE 2 (node has a single child)
        if node_children==1:

			# get the single child node
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child

            if node_parent!=None:
				# replace the node to be deleted with its child
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child

			# correct the parent pointer in node
            child.parent=node_parent

		# CASE 3 (node has two children)
        if node_children==2:

			# get the inorder successor of the deleted node
            successor=min_value_node(node.right_child)

			# copy the inorder successor's value to the node formerly
			# holding the value we wished to delete
            node.value=successor.value

			# delete the inorder successor now that it's value was
			# copied into the other node
            self.delete_node(successor)

			# exit function so we don't call the _inspect_deletion twice
            return

        if node_parent!=None:
			# fix the height of the parent of current node
            node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))

			# begin to traverse back up the tree checking if there are
			# any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)
    # ###################################  METHODS FOR AVL TREE ################################
    def get_height(self, current_node):
        if current_node is None:
            return 0
        return current_node.height

    def taller_child(self, current_node):
        left = self.get_height(current_node.left_child)
        right = self.get_height(current_node.right_child)
        return current_node.left_child if left >= right else current_node.right_child
    
    def _inspect_deletion(self,cur_node):
        if cur_node==None: return

        left_height =self.get_height(cur_node.left_child)
        right_height=self.get_height(cur_node.right_child)

        if abs(left_height-right_height)>1:
            y=self.taller_child(cur_node)
            x=self.taller_child(y)
            self._rebalance_node(cur_node,y,x)

        self._inspect_deletion(cur_node.parent)

    def _inspect_insertion(self, current_node, path=[]):
        if current_node.parent is None:
            return
        path = [current_node]+path

        left_height = self.get_height(current_node.parent.left_child)
        right_height = self.get_height(current_node.parent.right_child)

        if abs(left_height-right_height) > 1:
            path = [current_node.parent]+path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1+current_node.height
        if new_height > current_node.parent.height:
            current_node.parent.height = new_height

        self._inspect_insertion(current_node.parent, path)

    def _rebalance_node(self, z, y, x):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)
        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)
        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            # Exception is not posible rebalance the tree
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3 is not None:
            t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1+max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1+max(self.get_height(y.left_child), self.get_height(y.right_child))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1+max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1+max(self.get_height(y.left_child), self.get_height(y.right_child))

    # ###################################  PRINT METHODS ################################
    # -------------------------------- Inorder Print --------------------------

    def print_inorder(self):
        if self.root is not None:
            self._inorder(self.root)
            print("\n")
        else:
            print("Inorder - Empty tree\n")

    def _inorder(self, current):
        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self._inorder(current.left_child)
        # imprimir el valor actual de la raiz
        print(str(current.key) + " -> ", end='')
        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self._inorder(current.right_child)

    # -------------------------------- Preorder Print --------------------------
    def print_preorder(self):
        if self.root is not None:
            self._preorder(self.root)
            print("\n")
        else:
            print("Preorder - Empty tree\n")

    def _preorder(self, current):
        # imprimir el valor actual de la raiz
        print(str(current.key) + " -> ", end='')
        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self._preorder(current.left_child)
        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self._preorder(current.right_child)

    # -------------------------------- Posorder Print --------------------------
    def print_posorder(self):
        if self.root is not None:
            self._posorder(self.root)
            print("\n")
        else:
            print("Posorder - Empty tree\n")

    def _posorder(self, current):
        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self._posorder(current.left_child)
        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self._posorder(current.right_child)
        # imprimir el valor actual de la raiz
        print(str(current.key) + " -> ", end='')

    # ###################################  GRAPHIC WITH GRAPHVIZ ################################

    def graph(self, file_name, graphic_type):
        name_txt = file_name + ".txt"
        name_img = file_name + ".jpg"

        try:
            f = open(name_txt, "w")
            f.write("digraph G {\n")
            # f.write("graph[nodesep = 0.5];\n")

            # Create nodes here
            if graphic_type == AVLTree.TREE_COMPLETE and self.root is not None:
                self.txt_tree(self.root)
            elif graphic_type == AVLTree.TREE_INORDER and self.root is not None:
                f.write("rankdir = LR;\n")
                self.txt_inorder(self.root)
                self.txt_link = self.txt_link[: len(self.txt_link)-2]
                self.txt_link += ";"
            elif graphic_type == AVLTree.TREE_POSORDER and self.root is not None:
                f.write("rankdir = LR;\n")
                self.txt_posorder(self.root)
                self.txt_link = self.txt_link[: len(self.txt_link)-2]
                self.txt_link += ";"
            elif graphic_type == AVLTree.TREE_PREORDER and self.root is not None:
                f.write("rankdir = LR;\n")
                self.txt_preorder(self.root)
                self.txt_link = self.txt_link[: len(self.txt_link)-2]
                self.txt_link += ";"

            f.write("node[shape=box ];\n")
            f.write(self.txt_nodes)
            f.write(self.txt_link)
            f.write("}\n")
            f.close()
            self.txt_nodes = ""
            self.txt_link = ""
            # Execute the command to create the imagen file
            command = ["dot", "-Tjpg", name_txt, "-o", name_img]
            subprocess.call(command)

            # Open the imagen file
            # startfile(img)

            return 1
        except:
            print("Error: .")
            #f.close()
            return 0

    def txt_tree(self, current):
        """
            STEPS TO GENERATE *.txt FILE GRAPHVIZ CODE
            CREATE NODE:
            <id Node>  [shape = record label = "{ <data node> |  <side of node> }"]
            LINK NODE:
            <id Node> -> <id Node2>
        """
        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self.txt_tree(current.left_child)

        # imprimir el valor actual de la raiz
        self.txt_nodes += "n" + str(hex(id(current))) + "  [label = \" " + self.getSide(current) +\
            " \\n " + str(current.value) + "\\nHeight: " + \
            str(current.height) + " \" ];\n"

        if current.right_child is not None:
            self.txt_link += "n" + str(hex(id(current))) + " ->  n" +\
                str(hex(id(current.right_child))) + "   ;\n"

        if current.left_child is not None:
            self.txt_link += "n" + str(hex(id(current))) + " ->  n" +\
                str(hex(id(current.left_child))) + " ;\n"

        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self.txt_tree(current.right_child)

    def txt_inorder(self, current):
        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self.txt_inorder(current.left_child)

        # imprimir el valor actual de la raiz
        self.txt_nodes += "n" + str(hex(id(current))) + " [label = \" " +\
            str(current.value) + " \" ];\n"
        # enlazar al siguiente nodo
        self.txt_link += " n" + str(hex(id(current))) + " ->"

        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self.txt_inorder(current.right_child)

    def txt_preorder(self, current):
        # imprimir el valor actual de la raiz
        self.txt_nodes += "n" + str(hex(id(current))) + " [label = \" " +\
            str(current.value) + " \" ];\n"

        self.txt_link += " n" + str(hex(id(current))) + " ->"

        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self.txt_preorder(current.left_child)

        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self.txt_preorder(current.right_child)

    def txt_posorder(self, current):
        # llamar recursivamente al sub-arbol izquierdo
        if current.left_child is not None:
            self.txt_posorder(current.left_child)

        # llamar recursivamente al sub-arbol derecho
        if current.right_child is not None:
            self.txt_posorder(current.right_child)
        # imprimir el valor actual de la raiz
        self.txt_nodes += "n" + str(hex(id(current))) + " [label = \" " +\
            str(current.value) + " \" ];\n"

        self.txt_link += " n" + str(hex(id(current))) + " ->"

  
class A:
    def __init__(self, indice, valor):
        self.indice=indice
        self.valor=valor
  

    def __indice(self):
        return self.indice

    def __str__(self):
        string = "indice: " + str(self.indice)
        #string += "valor: "+ str(self.valor)
        string+="\n"
        string += "BD: "+ str(self.valor)
        return string


#addChr convert string to ascii

a = A(addChr("a"), "a")
b = A(addChr("b"), "b")
c = A(addChr("c"), "c")
d = A(addChr("d"), "d")
e = A(addChr("e"), "e")
f = A(addChr("f"), "f")
g = A(addChr("g"), "g")
h = A(addChr("h"), "h")
i = A(addChr("i"), "i")
j = A(addChr("j"), "j")
k = A(addChr("k"), "k")


tree = AVLTree()

tree.insert(a.indice, a)
tree.insert(b.indice, b)
tree.insert(c.indice, c)
tree.insert(d.indice, d)
tree.insert(e.indice, e)
tree.insert(f.indice, f)
tree.insert(g.indice, g)
tree.insert(h.indice, h)
tree.insert(i.indice, i)
tree.insert(j.indice, j)
tree.insert(k.indice, k)
tree.graph("complete", AVLTree.TREE_COMPLETE)
#print(tree.find(addChr("a")))




tree.delete_value(addChr("d"))
tree.delete_value(addChr("a"))
tree.delete_value(addChr("h"))


#segunda grafica
tree.graph("completeSIN", AVLTree.TREE_COMPLETE)


