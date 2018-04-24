//
// Created by Yunpeng Li on 4/23/18.
//

struct SingleLinkedListNode {
    int data = NULL;
    struct SingleLinkedListNode* next = NULL;
};

void fun1(struct SingleLinkedListNode* head)
{
    if (head == NULL)
        return;

    fun1(head->next);
    printf("%d ", head->data);
}

