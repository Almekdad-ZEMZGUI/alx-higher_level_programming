#include <Python.h>

/**
* print_python_list_info - prints some basic info about Python lists.
* @p: PyObject list
*
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	int i;

	printf("[*] Size of the Python List = %zd\n", Py_SIZE(p));
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}

