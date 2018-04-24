"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email
that is common to both accounts. Note that even if tow accounts have the same name, they may belong to different people
as people could have the same name. A person can have any number of accounts initially, but all of their accounts
definitely have the same name.

After merging the accounts, return teh accounts in the following format: the first element of each account is the name,
and the rest of teh elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John",
"johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"],
["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John',
'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be
accepted.

Note:
    - The length of accounts will be in the range [1, 1000]
    - The length of accounts[i] will be in the range [1, 10]
    = The length of accounts[i][i] will be in the range [1, 30]


Approach 1: Depth-first search

Intuition

Draw an edge between tow emails if they occur in the same account. The problem comes down to finding the connected
components of this graph.

Algorithm
for each account, draw the edge from the first email to all other emails. Additionally, we'll remember a map from
emails to name on the side. After finding each connected components, using a depth-first search, we'll add that to
our answer.
"""
import collections
from queue import Queue


class Solution(object):
    def accounts_merge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph(node):
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


"""
Approach 2: Union-Find 

Intuition 

As in approach 1, our problem comes down to finding the connected components of a graph. This is a natural fit for a
Disjoint Set Union (DSU) structure.

Algorithm

As in approach 1, draw edges between emails if they occur in the same account. For easier interoperability between our 
DSU template, we will map each email to some integer index by using emailToID. Then, dsu,find(email) will tell us a 
unique id representing what component that email is in.

For more information on DSU, please took at approach 2 in the article here. For brevity the solution showcase below do 
not use union by rank.
"""


class DSU:
    def __init__(self):
        self.p = range(10001)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution1(object):
    def accounts_merge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)

        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


"""
4. Trees and graphs

Many interviewees find tree and graph leetcode to be some of the trickiest. Searching a tree is more complicated than 
searching in a linearly organized data structure such as an array or linked list. Additionally, the worst case and 
average case time may vary wildly, and we must evaluate both aspects of any algorithm. Fluency in implementing a tree
or graph from scratch will prove essential.

Because most people are more familiar with trees than graph (and they're a bit simpler), we'll discuss trees first. 
This is a bit out of order thought, as a tree is actually a type of graph.

Note: Some of items in this chapter can vary slightly across different textbooks and other source. If you're used to a 
different definition, that's fine. Make sure to clear up any ambiguity with your interviewer.

Types of trees

A nice way to understand a trees is with a recursive explanation. A tree is a data structure composed of nodes.

- Each tee has a root node (Actually, this isn't strictly necessary in graph theory, but it's usually how we use trees
in programming, and especially programming interviews.)

- The root node has zero or more child nodes.

- EAch child node has zero or more child nodes and so on.

The tree can not contains cycles. The nodes may or may not be in a particular order, they could have any data type as
values, and they may or may not have links back to their parent nodes.

A very simple class definition for Node is:
"""


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


"""
You might also have a Tree class to wrap this node. For the purposes of interview questions, we typically do not sue a 
Tree class, you can if you feel it makes your code simple or better, but it rarely does.
"""


class Tree:
    def __init__(self):
        self.root = Node()


"""
Tree and graph questions are rife with ambiguous details and incorrect assumptions. Be sure to watch our for the 
following issues and seek clarification when necessary.

Trees vs. Binary Trees

A binary tree is a tree in which each node has up to 2 children. Not all trees are binary tree. For example, this is not
a binary tree, you can call it ternary tree.

There are occasions when you might have a tree that is not a binary tree. For example, suppose you were using a tree to
represents a bunch of phone numbers. In this case, you might use a 10-ary tree, with each node having up to 10 children
(one for each digit).

A node is called a 'leaf' node if it has no children.

Binary tree vs. Binary search tree

A binary search tree is a binary tree in which every node fits a specific ordering property: all left descendents <= n
< all right descendents. This must be true for each node n.

The definition of binary search tree can very slightly with respect to equality. Under some definitions, the tree cannot 
have duplicate values, In others, the duplicate values will be on the right or can be either in the side. All are valid 
definitions, but you should clarify this with your interviewer.

Note that this inequality must be true for all of a node's descendents, not just its immediate children. The following 
tree on the left below is a binary search tree. The tree on the right is not, since 12 is to the left of 8.

When given a tree question, many candidates assume the interviewer means a binary search tree. Be sure to ask. A binary
search tree imposes the condition that, for each node, its left descendents are less than or equal to the current node,
which is less than the right descendents.

Balanced vs. Unbalanced

While many trees are balanced, not all are. Ask your interviewer for clarification here. Note that balanced a tree does
not mean the left and right subtrees are exactly the same size (like you see under "perfect binary trees" in the 
following diagram).

One way to think about it is that a "balanced" tree really means something more like "not terribly imbalanced." It's 
balanced enough to ensure O(log n) times for insert and find. But it's not necessarily as balanced as it could be.

Two common types of balanced trees are red-black tree and AVL trees. These are discussed in more detail in the 
Advanced Topics section.

Complete binary trees

A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last
level. To the extend that the last level is filled, it is filled left to right.

Full Binary tree

A full binary tree is a binary tree in which every node has either zero or two children. That is , no nodes have only 
one child. 

Prefect binary trees

Perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has
maximum number of nodes.

Note that perfect trees are rare in interviews and in real life, as a perfect tree must have exactly 2**k - 1 nodes 
(where k is the number of levels). In an interview, do not assume a binary tree is perfect.

Binary tree traversal

Prior to your interview, you should be comfortable implementing in-order, post-order, and pre-order traversal. The 
most common of these is in-order traversal.

In-order traversal

In order traversal means to 'visit'. (often,  print) the left branch, then the current node, and finally, the right 
branch.
"""


def in_order(node):
    if node:
        in_order(node.left)
        visit(node)
        in_order(node.right)


def visit():
    pass


"""
When preformed on a binary search tree, it visits the node in ascending order (hence the name 'in-order').

Pre-order traversal

Pre-order traversal visits the current mode before its child nodes (hence teh name "pre-order").
"""


def pre_order(node):
    if node:
        visit(node)
        pre_order(node.left)
        pre_order(node.right)


"""
In a pre-order traversal, the root is always the first node visited.

Post-order traversal

Post-order traversal visits the current node after its child node (hence the name 'post-order').
"""


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        visit(node)


"""
In a post-order traversal, the root is always the last node visited.

Binary Heap (Min-heaps and Max-heaps)

We'll just discuss min-heaps here. Max-heaps are essentially equivalent, but the elements are in descending order 
rather than ascending order.

A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last level) 
where each node is smaller than its children. The root, therefore, is the minimum element in the tree.

We have two key operations on a min-heap: insert and extract_min.

insert
When we insert into a min-heap, we always start by inserting the element at the bottom. We insert at the rightmost spot
so as to maintain the complete tree property.

Then, we fix the tree by swapping the new element with its parent, until we find an appropriate spot for the element. 
We essentially bubble up the minimum element.

This takes O(log n) time, where n is the number of nodes in the heap.

Extract minimum element

Finding the minimum element of a min-heap is easy: it's always at the top. The trickier part is how to remove it. (In
fact, this isn't that tricky.)

First, we remove the minimum element and swap it with the last in the heap (the bottommost, rightmost element). Then we 
bubble down this element, swapping it with one of this children, until the min-heap property is restored. 

Do we swap it with the left child or the right child? that depends on their values, There's no inherent ordering 
between the left and right element, but you'll need to take the smaller one in order to maintain the min-heap ordering.

This algorithm will also take O(log n) time.

Tries (Prefix trees)

A trie (sometimes called a prefix tree) is a funny data structure. It comes up a lot in interview questions, but 
algorithm textbooks don't spend much time on this data structure.

A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent
a word.

The * node (sometimes called 'null nodes') are often used to indicate complete words. For example, the fact that there 
is a * node under MANY indicates that MANY is complete word. The existence of the MA path indicates there are words 
that start with MA.

The actual implementation of these * nodes might be a special type of child (such as a TerminatingTrieNode, which 
inherits from TrieNode). Or, we could use just a boolean flag terminates within the parent node.

A node in a trie could have anywhere from 1 through ALPHABET_SIZE + 1 children (or, 0 through ALPHABET_SIZE if a 
boolean flag is used instead of a * node).

Very commonly, a trie is used to store the entire language for quick prefix lookups. While a hash table can quickly look
up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid words. A trie can do this 
very quickly.

How quickly? A trie can check a string is a valid prefix in O(k) time, where k is the length of the string. This is 
actually the same runtime as a hash table will take. Although we often refer to hash table lookups as being O(1) time, 
this isn't entirely true. A hash table must read through all the characters in the input, which takes O(k) time in the
case of a word lookup.

Many problem involving lists of valid words leverage a trie as an optimization. In situations when we search through the
tree on related prefixes repeatedly (e.g, looking up M, then MA, then MAN, then MANY), we might pass around a reference
to the current node in the tree. This will allow us to just check if Y is a child of MAN, rather than starting from the 
root each time.

Graphs

A tree is actually a type of graph, but not all graphs are trees. Simply put, a tree is a connected graph without cycles.

A graph is simply a collection of nodes with edges between (some of) them.

- Graph can be either directed (like the following graph) or undirected. While directed edges are like a one-way street,
undirected edges are like a two-way street.

- The graph might consist of multiple isolated subgraphs. if there is a path between every pair of vertices. It is 
called a "connected graph".

- The graph can also have cycles (or not). An "acyclic graph" is one without cycle.

Usually, you gould draw a graph like this. In terms of programming, there are common ways to represent a graph.

Adjacency list

This is the most common way to represent a graph. Every vertex (or node) stores a list of adjacency vertices. In an 
undirected graph, an edge like (a, b) would be stored twice: once in a's adjacent vertices and once in b's adjacency
vertices.

A simple class definition for a graph node could look essentially the same as a tree node.
"""


class Graph:
    def __init__(self):
        self.nodes = Node()


"""
The graph class is used because, unlike in a tree, you can't necessarily reach all the nodes from a single node.

You dont' necessarily need any additional classes to represent a graph. an array (or a hash table) of lists (arrays,
arraylists, linked lists, etc) can store the adjacency list. The graph above could be represented as:

This is a bit more compact, but it isn't quite as clean. We tend to use node classes unless there's a compelling
reason not to.

Adjacency matrices

An adjacency matrix is an NxN boolean matrix (where N is the number of nodes), where a true value at matrix[i][j]
indicates an edge from node i to node j. (You can also use an integer matrix with 0s and 1s.)

In an undirected graph, an adjacency matrix will be symmetric. In a directed graph, it will not (necessarily) be.

The same graph algorithms that are used on adjacency lists (breadth first search, etc) can be performed with adjacency
matrices, but they may be somewhat less efficient. In the adjacency list representation, you can easily iterate through 
the neighbors of a node. In the adjacency matrix representation, you will need to iterate through all the nodes to 
identify a node's neighbors.

Graph search

The two most common ways to search a graph are depth first search and breadth first search.

In depth first search, we start at the root (or another arbitrarily selected node) and explore each branch completely
before moving on to the next branch. That is, we go deep first (hence the name depth first search) before we go wide.

In breadth first search (BFS), we start at the root (or another arbitrarily selected node) and explore each neighbor 
before going on to any of their children. That is, we go wide (hence breadth-first search) before we go deep.

See the below depiction of a graph and its depth-first search and breadth-first search (assuming neighbors are iterated
in numerical order).

Breadth-first search and depth-first search tend to be used in different scenarios. DFS is often preferred if we want 
to visit every node in the graph. Both will work just fine, but depth-first search is a bit simple.

However, if we want to find the shortest path (or just any path) between two nodes, BFS is generally better. consider 
representing all the friendships in the entire world in a graph and typing to find a path of friendship between Ash and
Vanessa.

In depth-first search, we could take a path like Ash - > Brian -> Carleton -> Davis -> Eric -> Farah -> Gayle -> Harry 
-> Isabella -> John -> Kari ... and then find ourselves very far away. We could go through most of the would without 
realizing that, in fact, Vanessa is Ash's friend. We will still eventually find the path. But it may take long time. It 
also won't find us the shotest path.

In breadth-first search, we would stay close to Ash for as long as possible. We might iterate through many of Ash's 
friends, but we couldn't go to his more distant connections until absolutely necessary. If Vanessa is Ash's friend, or
his friend of a friend, we'll find this our relatively quickly.

Depth-first search (DFS)

In DFS, we visit a node a and then iterate through each of a's neighbors. When visiting a node b that is a neighbors of
a, we visit all of b's neighbors before going on to a's other neighbors. That is, a exhaustively searches b's branch
before any of its other neighbors.

Note that pre-order and other forms of tree traversal are a form of DFS. The key difference is that when implementing
this algorithm for a graph, we must check if the node has been visited. If we dont' we risk getting stack in an 
infinite loop.

The pseudocode below implement DFS.
"""


def dfs(root):
    if not root:
        return
    visit(root)
    root.visited = True
    for node in root.adjacency:
        if node.visited == False:
            dfs(node)


"""
BFS is a bit less intuitive, and many interviewees struggle with the implementation unless they are already familiar 
with it. the main tripping point is the assumption that BFS is recursive. It's not, instead of use a queue.

In BFS, node a visits each of a's neighbors before visiting any of their neighbors. You can think of this as searching
level by level out from a. An iterative solution involving a queue usually works best.
"""


def bfs(root):
    q = Queue()
    root.marked = True
    q.put(root)

    while q:
        node = q.get()
        visit(node)
        for n in node.adjacency:
            n.mared = True
            q.put(n)
