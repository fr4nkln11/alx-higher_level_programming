#include "lists.h"
#include <stdio.h>

/**
 * print_node_stack - prints all elements of a node_stack_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_node_stack(const node_stack_t *h)
{
	const node_stack_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * free_node_stack - frees a node_stack_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_node_stack(node_stack_t *head)
{
	node_stack_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * add_to_node_stack - a function that adds
 * a new node at the beginning of a node_stack_t list.
 * @head: a pointer to the pointer to the head node
 * @n: integer value stored in new node
 *
 * Return: the address of the new node, or NULL if it failed
 */

node_stack_t *add_to_node_stack(node_stack_t **head, const int n)
{
	node_stack_t *new_node;

	new_node = (node_stack_t *)malloc(sizeof(node_stack_t));

	if (!new_node)
	{
		return (NULL);
	}

	if (!head)
	{
		return (NULL);
	}

	new_node->n = n;
	new_node->next = *head;

	*head = new_node;

	return (*head);
}

/**
 * pop_node_stack - a function that deletes
 * the head node of a node_stack_t linked list,
 * and returns the head node’s data (n).
 * @head: a pointer to the pointer pointing to the head node
 *
 * Return: integer value stored in the deleted node
 */

int pop_node_stack(node_stack_t **head)
{
	node_stack_t *temp_node;
	int data = 0;

	if (head)
	{
		if (*head)
		{
			temp_node = (*head)->next;
			data = (*head)->n;
			free(*head);
			*head = temp_node;
		}
	}

	return (data);
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
		listint_t *slow = *head;
		listint_t *fast = *head;
		node_stack_t *node_stack_head = NULL;

		if ((*head)->next == NULL)
			return (1);

		add_to_node_stack(&node_stack_head, slow->n);
		while (slow)
		{
			if (fast->next)
				fast = fast->next->next;
			else
			{
				fast = fast->next;
				pop_node_stack(&node_stack_head);
			}
			if (!fast)
				break;

			slow = slow->next;
			add_to_node_stack(&node_stack_head, slow->n);
		}
		slow = slow->next;
		while (slow)
		{
			if (slow->n != node_stack_head->n)
			{
				free_node_stack(node_stack_head);
				return (0);
			}
			slow = slow->next;
			pop_node_stack(&node_stack_head);
		}

		free_node_stack(node_stack_head);
	}
	return (1);
}
