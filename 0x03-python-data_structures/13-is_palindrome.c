#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double ptr to the head of linkedlist
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
        listint_t *temp = *head;
        unsigned int length = 0, i;
        int arr[10240];
        
        if (!*head)
                return (0);
        
        for (i = 0; temp; i++)
        {
                arr[i] = temp->n;
                temp = temp->next;
                length++;
        }
        if (length == 1)
                return (1);

        for (i = 0; i <= length / 2; i++)
        {
                if (arr[i] != arr[length - i - 1])
                        return (0);
        }
        return (1);
}
