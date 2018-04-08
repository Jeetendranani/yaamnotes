"""
10.2 Linked lists

A linked list is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in
which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in
each object. Linked lists provide a simple, flexible representation for dynamic sets, supporting (though not necessarily
efficiently) all the operations listed on the page 230.

As show in figure 10.3, each element of doubly linked list L is an object with a attribute key and two other pointer
attributes: next and prev. The object may also contain other satellite data. Given an element x in the list, x.next
points to its successor in the linked list, and x.prev points to its predecessor. If x.prev = Nil,the element x has no
predecessor and is therefore the first element, or head, of the list. If x.next = Nil, the element x has no successor
and it therefore the last element, or tail, of the list. An attribute L.head points to the first element of the list.
If L.head = Nil, the list is empty.

A list may have one of several forms. It may be either singly linked or doubly linked, it may be sorted or not, and it
may be circular or not. If a list is singly linked, we omit the prev pointer in the each element. If a list is sorted,
the linear order of the list corresponds to hte linear order of keys stored in elements of the list; the minimum
element is then the head of hte list, and the maximum element is the tail. If the list is unsorted, the elements can
appear in any order. In a circular list, the prev pointer of the head of the list points to the tail, and the next
pointer of the tail of the list points to the head. We can think of a circular list as a ring of the elements. In the
remainder of this section, we assume that the lists with which we are working are unsorted and doubly linked.

Searching a linked list

The procedure List-search(L, k) finds the first element with key k in list L by a simple linear search, returning a
pointer to this element. If no object with key k appears in the list, then the procedure results Nil. For the linked
list in Figure 10.3(a), the call ilst-search(L, 4) returns a pointer to the third element, and the
call list-search(L, 7) returns Nil

list-search(L, k)
    x = L.head
    while x != Nil and x.key != k
        x = x.next
    return x

To search a list of n objects, the list-search procedure takes O1(n) time in the worst case, since it may have to search
the entire list.

Inserting into a linked list

Given an element x whose key attribute has already been set, the list-insert procedure 'splices' x onto the front of
the linked list, as shown in Figure 10.3(b).

list-insert(L, x)
    x.next = L.head
    if L.head != Nil
        L.head.prev = x
    L.head = x
    x.prev = Nil

(Recall tht our attribute notation can cascade, so that L.head.prev denotes the prev attribute of the object that L.head
points to.) The running time for List-insert on a list of n elements is O(1).

Deleting from a linked list

The procedure list-delete removes an element x from a linked list L. It must be given a pointer to x, and it then
'splices' x out of the list by updating pointers. If we wish to delete an element with a given key, we must first call
list-search to retrieve a pointer to the element.

list-delete(L, x)
    if x.prev != Nil
        x.prev.next = x.next
    else
        L.head = x.next
    if x.next != Nil
        x.next.prev = x.prev

Figure 10.3(c) shows how an element is deleted from a linked list. List-delete runs O(1) time, but if we wish to delete
an element with a given key, O1(n) time is required in the worst case, because we must fist call list-search to find the
element.

Sentinels

The code for list-delete would be simpler if we could ignore the boundary conditions at the head and tail of the list:
A sentinel is a dummy object that allows us to simplify boundary conditions. For example, suppose that we provide with
list L an object L.nil that represents Nil but has all the attributes of the other objects in the list. Wherever we have
reference to Nil in list code, we replace it by a reference to the sentinel L.nil, as show in figure 10.4, this change
turns a regular double linked list into a circular, doubly linked list with a sentinel, in which the sentinel L.nil lies
between the head and tail. Similarly, both the next attribute of the tail and hte prev attribute of the head point to
L.nil, Since L.nil.next points to head, we can eliminate the attribute L.head altogether, replacing references to it
by reference to L.nil.next and L.nil.prev point to L.nil.

The code for list-search remains the same as before, but with the reference to nil and L.head changed as specified
above:

list-search(L, k)
    x = L.nii.next
    while x != L.nil and x.key != k
        x = x.next
    return x

We sue the two-line procedure list-delete from before to delete an element from the list. The following procedure
inserts an element into the list:

list-insert(L, x)
    x.next = L.nil.next
    L.nil.next.prev = x
    L.nil.next = x
    x.prev = L.nil

Figure 10.4 shows the effects of list-insert and list-delete on a sample list.

Sentinels rarely reduce the asymptotic time bounds of data structure operations, but they can reduce constant factors.
The gain from using sentinels within loops is usually a matter of clarity of code rather than speed; the linked list
code, for example, becomes simpler when we sue sentinels, but we save only O(1) time in the list-insert and list-delete
procedures. In other situations, however the use of sentinels helps to tighten the code in a loop, thus reducing the
coefficient of, say, n or n2 the running time.

We should use sentinels judiciously. When there are many small lists, the extra storage used by their sentinel can
represent significant wasted memory. In this book, we use sentinels only when they truly simplify the code.
"""