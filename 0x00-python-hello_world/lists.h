#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct address_list - singly linked list of node addresses
 * @node: pointer to node
 * @next: points to next node
 *
 * Description: address_list node structure
 */
typedef struct address_list
{
	listint_t *node;
	struct address_list *next;
} address_list_t;

int node_exists(address_list_t *head, listint_t *node);
address_list_t *add_node_address(address_list_t **head, listint_t *node);
void free_address_list(address_list_t *head);

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
