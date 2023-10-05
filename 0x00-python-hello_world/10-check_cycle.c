#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *cursor;
	cursor = list;

	while (cursor)
	{
		if (cursor->flag == 1)
			return (1);

		cursor->flag = 1;
		cursor = cursor->next;
	}

	return (0);
}
