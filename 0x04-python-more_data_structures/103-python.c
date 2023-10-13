#include <Python.h>
#include <listobject.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t list_size = PyList_Size(p);
		Py_ssize_t memory_allocated = ((PyListObject *)p)->allocated;
		Py_ssize_t idx;
		PyObject *list_item;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", memory_allocated);

		for (idx = 0; idx < list_size; idx++)
		{
			list_item = PyList_GET_ITEM(p, idx);
			printf("Element %ld: %s\n", idx, list_item->ob_type->tp_name);
		}

	}
	else
	{
		printf("This object is not a Python List.\n");
	}
}

void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t byte_size = PyBytes_Size(p);
		char *string = PyBytes_AsString(p);
		Py_ssize_t idx;
		Py_ssize_t max_idx = 10;

		if (byte_size < 10)
			max_idx = byte_size;

		printf("[.] bytes object info\n");
		printf("  size: %ld\n", byte_size);
		printf("  trying string: %s\n", string);
		printf("  first %ld bytes:", max_idx);

		for (idx = 0; idx < max_idx; idx++)
		{
			printf(" %02x", (unsigned char)string[idx]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
