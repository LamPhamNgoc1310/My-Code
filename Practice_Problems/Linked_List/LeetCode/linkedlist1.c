#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int val;
    struct Node *next;
}Node;
void createNode(Node** head, int data)
{
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = data;
    newnode->next = *head;
    *head = newnode;
}
void display(Node * head)
{
    if (head == NULL)
    {
        printf("List is empty");
        return;
    }
    Node* current = head;
    while(current != NULL)
    {
        printf("Value is: %d \n ", current->val);
        current = current -> next;
    }
}

int main()
{
    Node* head = NULL;
    int value;

    for(int i = 0; i < 5; i++)
    {
        printf("Enter the value for node %d: ", i+1);
        scanf("%d", &value);
        createNode(&head, value);
    }
    printf("The contents of this list: \n");
    display(head);

    return 0;
}
