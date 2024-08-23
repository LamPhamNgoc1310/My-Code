#include <stdio.h>
#include <stdlib.h>


struct Node
{
    int data;
    struct Node * next;
};

void traversal(struct Node * ptr)
{
    while(ptr != NULL)
    {
        printf("Element: %d\n", ptr->data); //pointer pointing to the data of the node
        ptr = ptr->next;
    }

}
int main()
{
    int n[100];
    printf("The number of nodes: ");
    scanf("%d", &n);

    // for(int i = 0; i < n; i++)
    // {
    //     n[i] = (struct Node *) malloc(sizeof(struct Node));
    // }
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

    return 0;
}