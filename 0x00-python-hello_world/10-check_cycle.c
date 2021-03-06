#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int check_cycle(listint_t *list)
{
  listint_t *i, *j;

  if (list == NULL || list->next == NULL)
    return (0);

  i = list;
  j = list;

  while (i && j && j->next)
    {

      i = i->next;
      j = j->next->next;

      if (i == j)
	return (1);

    }

  return (0);
}
