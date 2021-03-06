#include "lists.h"

int is_palindrome(listint_t **head)
{
	int size, index, buffer[2048];

	size = 0;
	index = 0;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/* copy list to buffer array */ 
	while (*head)
	{
	        buffer[size] = (*head)->n;
		*head = (*head)->next;
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
