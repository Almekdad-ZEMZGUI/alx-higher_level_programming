#include <Python.h>
#include <listobject.h>
#include <object.h>

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

	printf("[*] Size of the Python List = %d\n", PyList_Size(p));
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", i, Py_TYPE(item)->tp_name);
	}
}
