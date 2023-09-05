#include "lists.h"



/**
 * check_cycle - confirms if there is cycle in linked list
 * @list: the list to be checked
 *
 * Return: 1 if cycle and 0 if not cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *quickList = list;
	listint_t *slowList = list;

	if (!list)
		return (0);

	while (quickList && quickList->next && slowList)
	{
		slowList = slowList->next;
		quickList = quickList->next->next;

		if (slowList == quickList)
			return (1);
	}
	return (0);
}
