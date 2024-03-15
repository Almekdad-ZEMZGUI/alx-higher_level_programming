#include "lists.h"

/**
* len - counts length of linkedlist
* @head: head of linkedlist
*
* Return: length
*/
unsigned int len(listint_t *head)
{
        unsigned int length;

        for (length = 0; head; length++)
                head = head->next;

        return (length);
}
/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double ptr to the head of linkedlist
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
        listint_t *temp = *head;
        unsigned int length, i;
        int arr[1000];
        
        if (!*head)
                return (0);
        
        length = len(temp);
        
        if (length == 1)
                return (1);
        
        for (i = 0; temp; i++)
        {
                arr[i] = temp->n;
                temp = temp->next;
        }
        for (i = 0; i <= length / 2; i++)
        {
                if (arr[i] != arr[length - i - 1])
                        return (0);
        }
        return (1);
}
