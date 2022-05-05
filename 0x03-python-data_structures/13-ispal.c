#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *reverse_list = *head;
	int size, index, buffer[2048];

	size = 0;
	index = 0;
	if (*head == NULL || reverse_list->next == NULL)
		return (1);
	/* copy list to buffer array */ 
	while (reverse_list)
	{
		buffer[size] = reverse_list->n;
		reverse_list = reverse_list->next;
		size++;
	}
	/* compare from the end to the middle of the list */
	while (size >= index)
	{
		if (buffer[index] != buffer[size - 1])
			return (0);
		size--;
		index++;
	}
	return (1);
}
