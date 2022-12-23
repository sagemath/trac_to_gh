# Issue 115: study alternatives to PyType_IsSubtype

Issue created by migration from https://trac.sagemath.org/ticket/115

Original creator: dmharvey

Original creation time: 2006-10-07 17:47:44

Assignee: somebody

Lots of our Pyrex code is going to be using `PyObject_TypeCheck` as a replacement for isinstance. This is a C macro (defined in python's object.h file), HOWEVER if the types don't match exactly it has to call the API PyType_IsSubType. The code for that function is shown below. Probably we can write something somewhat faster that covers many of the situations we need, because we don't need to worry about the MRO (method resolution order) stuff.


```
/* type test with subclassing support */

int
PyType_IsSubtype(PyTypeObject *a, PyTypeObject *b)
{
        PyObject *mro;

        if (!(a->tp_flags & Py_TPFLAGS_HAVE_CLASS))
                return b == a || b == &PyBaseObject_Type;

        mro = a->tp_mro;
        if (mro != NULL) {
                /* Deal with multiple inheritance without recursion
                   by walking the MRO tuple */
                Py_ssize_t i, n;
                assert(PyTuple_Check(mro));
                n = PyTuple_GET_SIZE(mro);
                for (i = 0; i < n; i++) {
                        if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                                return 1;
                }
                return 0;
        }
        else {
                /* a is not completely initilized yet; follow tp_base */
                do {
                        if (a == b)
                                return 1;
                        a = a->tp_base;
                } while (a != NULL);
                return b == &PyBaseObject_Type;
        }
}
```




---

Comment by davidloeffler created at 2009-06-07 13:18:31

Changing assignee from somebody to cwitty.


---

Comment by davidloeffler created at 2009-06-07 13:18:31

Changing component from basic arithmetic to misc.


---

Comment by mhansen created at 2010-08-26 20:22:44

I'm going to close this as invalid.  I made a copy of this ticket on the Cython Trac site: http://trac.cython.org/cython_trac/ticket/572


---

Comment by mhansen created at 2010-08-26 20:22:44

Resolution: invalid
