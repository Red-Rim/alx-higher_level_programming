#include "lists.h"

/**
 * insert_node - inert an number in sorted list
 * @head: head
 * @number: number
 * Return: pointer or Null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd;
	listint_t *h;
	listint_t *n_prv;

	h = *head;
	nd = malloc(sizeof(listint_t));

	if (!nd)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		n_prv = h;
		h = h->next;
	}

	nd->n = number;

	if (!*head)
	{
		nd->next = NULL;
		*head = nd;
	}
	else
	{
		nd->next = h;
		if (h == *head)
			*head = nd;
		else
			n_prv->next = nd;
	}

	return (nd);
}
