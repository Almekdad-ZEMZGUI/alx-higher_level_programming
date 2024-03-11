#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if(!list)
	    return (0);

	for (;;)
	{
		if (fast->next && fast->next->next)
		{
			if (slow == fast)
				return (1);
			
			slow = slow->next;
			fast = (fast->next)->next;
		}
	}
	return (0);
}
