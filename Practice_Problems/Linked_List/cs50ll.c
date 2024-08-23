#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *next;   
}node;

void unload(node *list);
void visualize(node *list);

#define LIST_SIZE 5

int main(void)
{
    node *list = NULL;
    //ADD ITEMS TO LIST
    for (int i = 0; i < LIST_SIZE; i++)
    {
        printf("Enter your number: ");
        int data;
        scanf("%d", &data);
        //ADD DATA TO NEW NODE
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Couldn't allocate memory for node\n");
            return 1;
        }
        n->data = data;
        n->next = NULL;

        list = n; //UPDATE LIST AS THE FIRST NODE OF THE LIST

        //VISUALIZING THE LIST
    }
        visualize(list);
    unload(list);
}

void unload(node *list)
{
    while (list != NULL)
    {
        node *ptr = list->next;
        free(list);
        list = ptr;
    }
}

void visualize(node *list)
{
    while(list != NULL)
    {
        printf("%d\n", list->data);
        list = list->next;
    }
}