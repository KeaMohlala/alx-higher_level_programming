#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: linked linst to check
 * Return: 1 if there is a cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *current = list;

	while (current != NULL)
	{
		temp = list;
		while (temp != current)
		{
			if (temp == current->next)
			{
				return (1);
			}
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
