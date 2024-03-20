#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: A PyObject
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, bsize;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		bsize = 10;
	else
		bsize = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", bsize);
	for (i = 0; i < bsize; i++)
		printf("%02hhx%s", bytes->ob_sval[i], i == bsize - 1 ? "\n" : " ");
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	int osize, allocate, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	osize = var->ob_size;
	allocate = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", osize);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < osize; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);

		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}

