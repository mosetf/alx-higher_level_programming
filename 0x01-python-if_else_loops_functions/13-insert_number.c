#include "lists.h"

/**
 * insert_node - inserts number in a linked list
 * @head: double pointer to the list
 * @number: number to be inserted in the new node
 * Return: address of new node else null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;
	listint_t *prev_node = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		while (current && current->n < number)
		{
			prev_node = current;
			current = current->next;
		}
		prev_node->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
