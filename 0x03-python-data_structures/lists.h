#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * struct node_stack_s - stack of nodes
 * @n: integer
 * @next: points to the next node
 *
 * Description: stack of traversed nodes
 */
typedef struct node_stack_s
{
	int n;
	struct node_stack_s *next;
} node_stack_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
node_stack_t *add_to_node_stack(node_stack_t **head, const int n);
int pop_node_stack(node_stack_t **head);
size_t print_node_stack(const node_stack_t *h);
void free_node_stack(node_stack_t *head);


#endif /* LISTS_H */
