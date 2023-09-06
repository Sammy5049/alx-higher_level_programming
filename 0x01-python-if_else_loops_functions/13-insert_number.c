#include "lists.h"

/**
 * insert_node - func to insert node to orgnized list
 *	@head: the node list head
 * @number: postion on list to add the node
 * Return: NULL If the function fails and point to node if not
 */
listint_t *insert_node(listint_t **head, int number)
{
 listint_t *nPosition = *head, *added;

 added = malloc(sizeof(listint_t));
 if (added == NULL)
		return (NULL);
 added->n = number;

 if (nPosition == NULL || number < nPosition->n)
 {
		added->next = nPosition;
		*head = added;
		return (added);
 }

 while (nPosition && nPosition->next && nPosition->next->n < number)
		nPosition = nPosition->next;

 added->next = nPosition->next;
 nPosition->next = added;

 return (added);
}