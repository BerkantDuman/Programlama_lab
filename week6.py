# Hırsız belli bir ağırlık taşıya biliyor bu ağırlık sınırında en fazla kaç eşyayla geri döndüğü durumu veren fonk.
class Item(object):

    def __init__(self, n, v, w):
        self.name = n
        self.weight = w
        self.value = v


def maximum_object(objects, weight):
    items = []
    miktar = 0

    for i in range(len(objects)):
        temp_items = []
        amount = weight
        j = i
        while (amount >= 0 and j >= 0):

            if (amount - objects[j].weight >= 0):
                amount -= objects[j].weight
                if objects[j] not in temp_items:
                    temp_items.append(objects[j])
                j -= 1

            else:
                j -= 1
        if (len(temp_items) > miktar):
            miktar = len(temp_items)
            items = temp_items
    return items

item_1 = Item("clock", 175, 10)
item_2 = Item("Painting", 90, 9)
item_3 = Item("Radio", 20, 4)
item_4 = Item("Vase", 50, 2)
item_5 = Item("Book", 10, 1)
item_6 = Item("Computer", 200, 20)

objects = [item_1, item_2, item_3, item_4, item_5, item_6]
result = maximum_object(objects, 20)


# for i in result:
#    print(i.name)

########################################################################################################################
# Tree Structure


import random


class myNode(object):
    def __init__(self, v=0):
        # previous --> left
        # next --> right
        self.previous = None
        self.next = None
        self.val = v


class myTree(object):
    def __init__(self):
        self.root = myNode(250)  # içine aldığı değer ağaç yapısının kökünü belirtir. değer belirtilmezse 0 olarak atar.


def inorder(root):
    if root:
        inorder(root.previous)
        print(root.val, end=' ')
        inorder(root.next)


def insert_1(root, node):
    if (root is None):
        root = node
    else:
        if (root.val < node.val):
            if (root.next is None):
                root.next = node
            else:
                insert_1(root.next, node)
        else:
            if (root.previous is None):
                root.previous = node
            else:
                insert_1(root.previous, node)
                import random


def test():
    numbers = []
    for x in range(5):
        numbers.append(random.randint(1, 101))
    numbers
    tree_1 = myTree()
    for n in numbers:
        insert_1(tree_1.root, myNode(n))
    inorder(tree_1.root)


test()