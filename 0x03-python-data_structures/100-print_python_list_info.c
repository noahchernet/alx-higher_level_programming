#include "Python.h"
#include "stdio.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: the list object from Python whose elements and length will be printed
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python list = %d\n", (int) PyList_Size(p));
	printf("[*] Allocated = %d\n", (int) PyList_GET_SIZE(p));

	for(i = 0; i < (int) PyList_Size(p); i++)
	{
		printf("Element 0: %s\n", (char *) Py_TYPE(PyList_GetItem(p, i)));
	}
}
