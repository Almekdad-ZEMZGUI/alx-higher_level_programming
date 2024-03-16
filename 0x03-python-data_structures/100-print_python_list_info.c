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

	printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
