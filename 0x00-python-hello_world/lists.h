#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - Singly linked list structure
 * @n: Integer data
 * @next: Pointer to the next node
 *
 * Description: Defines a node structure for a singly linked list.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

#endif /* LISTS_H */
