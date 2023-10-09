#include <Python.h>
#include <listobject.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t list_size = PyList_Size(p);
		Py_ssize_t memory_allocated = ((PyListObject *)p)->allocated;
		Py_ssize_t idx;
		PyObject *list_item;

		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", memory_allocated);

		for (idx = 0; idx < list_size; idx++)
		{
			list_item = PyList_GetItem(p, idx);
			printf("Element %ld: %s\n", idx, list_item->ob_type->tp_name);
		}

	}
	else
	{
		printf("This object is not a Python List.\n");
	}
}
