#include "lists.h"

/**
 * insert_node - inserts a node with value @number in the sorted linked list
 * @head
 * @head: the sorted linked list
 * @number: the value of the new node that'll be inserted in @head
 *
 * Return: the new node on success or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *next;
	listint_t *head_copy = *head;
	int node_inserted = 0;

	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}

	while (!node_inserted)
	{
		if (((*head)->n < number))
		{
			if ((*head)->next && ((*head)->next)->n > number)
			{
				next = (*head)->next;
				(*head)->next = new_node;
				new_node->next = next;
				node_inserted = 1;
			}
			else if (!(*head)->next)
			{
				(*head)->next = new_node;
				node_inserted = 1;
			}
			else
				*head = (*head)->next;
		}
		else if (*head == head_copy)
		{
			*head = new_node;
			new_node->next = head_copy;
			return (new_node);
		}
		else if ((*head)->n == number)
		{
			*head = head_copy;
			free(new_node);
			return (NULL);
		}
	}
	*head = head_copy;

	return (new_node);
}
