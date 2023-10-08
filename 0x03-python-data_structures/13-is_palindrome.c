#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer pointing to the head node
 *
 * Return: 1 palindrome found, 0 palindrome not found
 */

int is_palindrome(listint_t **head)
{
	listint_t *cursor;
	listint_t *front;
	listint_t *back;

	if (head && *head)
	{
		/* check if linked list is empty */
		if ((*head)->next == NULL)
			return (1);

		front = *head;
		cursor = front;
		back = NULL;

		while (front)
		{
			cursor = front;
			while (cursor->next != back)
				cursor = cursor->next;
			back = cursor;

			/* check if front and back nodes are different */
			if (front->n != back->n)
				return (0);

			/* check if mid-point has been reached */
			if (front == back || front->next == back)
				break;

			front = front->next;
		}
	}
	return (1);
}
