#include <stdio.h>
#include <stdlib.h>


struct Node
{
    int data;
    struct Node *next;
};

void traversal(struct Node * ptr)
{
    while(ptr != NULL)
    {
        printf("Element: %d\n", ptr->data); //pointer pointing to the data of the node
        ptr = ptr->next;
    }

}

struct Node * insertFirst(struct Node *head, int data)
{
    struct Node *ptr = (struct Node * )malloc(sizeof(struct Node));
    ptr->next = head;
    ptr->data = data;
    return ptr;
}

struct Node * insertBetween(struct Node *head, int data, int index) 
{
    struct Node *ptr = (struct Node * )malloc(sizeof(struct Node));
    struct Node *p = head;
    int i = 0;

    while (i != index-1) //
    {
        p = p->next;
        i++;
    }

    ptr->data = data; //store the value of the inserting node into ptr
    ptr->next = p->next; 
    //pointer of the node you want to insert is equal to the value that p points 
    //to at that time, and then when the code below is executed, the chain will be broken
    //and p will point to the node you inserted.
    p->next = ptr;
    return head;
}

int main()
{
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    //Allocate memory for node in linked list in heap
    head = (struct Node *) malloc(sizeof(struct Node));
    second = (struct Node *) malloc(sizeof(struct Node));
    third = (struct Node *) malloc(sizeof(struct Node));
    fourth = (struct Node *) malloc(sizeof(struct Node));

    //Link first and second nodes
    head->data = 7;
    head->next = second;
    //Link second and third nodes
    second->data = 31;
    second->next = third;
    //Link third and fourth nodes
    third->data = 4;
    third->next = fourth;
    //terminate at 4th node
    fourth->data = 10;
    fourth->next = NULL;

    traversal(head); //Travesal starting from head node

    // head = insertFirst(head, 2004); //insert at beginning so we have to make it the new head
    insertBetween(head, 11, 3);
    traversal(head); //Traverse and print out to clarify the insertion

    return 0;
}
