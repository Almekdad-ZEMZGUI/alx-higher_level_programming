#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: A PyObject byte object
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    unsigned char i, size;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", bytes->ob_sval);

    size = (bytes->ob_base.ob_size > 10) ? 10 : bytes->ob_base.ob_size;

    printf("  first %d bytes: ", size);
    for (i = 0; i < size; i++)
        printf("%02x%s", bytes->ob_sval[i], (i == size - 1) ? "\n" : " ");
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject list object
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    int i;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < PyList_Size(p); i++)
    {
        const char *type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
        printf("Element %d: %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(PyList_GetItem(p, i));
    }
}

