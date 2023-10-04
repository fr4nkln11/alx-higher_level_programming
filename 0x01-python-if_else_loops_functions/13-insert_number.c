#include "lists.h"

/**
 * traverse_insert - traverse the linked list to find a position to insert
 * @head: the head node of the linked list
 * @new_node: the new node to insert
 *
 * Return: if successful, the new node
 * on failure, NULL
 */

listint_t *traverse_insert(listint_t *head, listint_t *new_node)
{
	listint_t *current = head;
	listint_t *temp = current;

	while (current)
	{
		if (current->n < new_node->n)
		{
			temp = current;
			current = current->next;
		}
		else if (current->n >= new_node->n)
		{
			temp->next = new_node;
			new_node->next = current;
			return (new_node);
		}
		else if (current->next == NULL)
		{
			current->next = new_node;
			return (new_node);
		}
	}

	free(new_node);
	return (NULL);
}

/**
 * insert_node - insert a node in a sorted linked list
 * @head: double pointer to head node
 * @number: the number value of the node to insert
 *
 * Return: on success, a pointer to new node
 * on failure, a pointer to NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!head)
	{
		free(new_node);
		return (NULL);
	}

	if (*head)
	{
		if (new_node->n < (*head)->n)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
		else
		{
			return (traverse_insert(*head, new_node));
		}
	}
	else
	{
		*head = new_node;
		return (new_node);
	}
}
