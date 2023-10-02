#include "lists.h"
#include <stdlib.h>

address_list_t *add_node_address(address_list_t **head, listint_t *node)
{
	address_list_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->node = node;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

void free_address_list(address_list_t *head)
{
	address_list_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

int node_exists(address_list_t *head, listint_t *node)
{
	if (head)
	{
		address_list_t *current = head;

		while (current != NULL)
		{
			if (current->node == node)
			{
				return (1);
			}

			current = current->next;
		}
	}

	return (0);
}

int check_cycle(listint_t *list)
{
	listint_t *current;
	address_list_t *a_head;

	a_head = NULL;

	current = list;

	while (current)
	{
		if (node_exists(a_head, current))
		{
			free_address_list(a_head);
			return (1);
		}
		else
		{
			add_node_address(&a_head, current);
			current = current->next;
		}
	}

	free_address_list(a_head);
	return (0);
}
