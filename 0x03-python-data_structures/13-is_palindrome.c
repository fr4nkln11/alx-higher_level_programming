#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_traverse - traverse the nodes in reverse
 * @head: pointer to pointer to head node
 * @node: the cursor node
 *
 * Return: 1 for palindrome, 0 for no palindrome
 */

int reverse_traverse(listint_t **head, listint_t *node)
{
	int status;
	listint_t *temp;

	if (node == NULL)
		return (1);

	status = reverse_traverse(head, node->next);

	if (status == 0)
		return (0);

	if (node->n != (*head)->n)
		return (0);

	temp = *head;
	*head = (*head)->next;
	free(temp);

	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer pointing to the head node
 *
 * Return: 1 palindrome found, 0 palindrome not found
 */

int is_palindrome(listint_t **head)
{
	if (head && *head)
	{
		if ((*head)->next == NULL)
			return (1);

		return (reverse_traverse(head, *head));
	}

	return (1);
}
