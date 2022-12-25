# Issue 115: study alternatives to PyType_IsSubtype

archive/issues_000115.json:
```json
{
    "body": "Assignee: cwitty\n\nLots of our Pyrex code is going to be using `PyObject_TypeCheck` as a replacement for isinstance. This is a C macro (defined in python's object.h file), HOWEVER if the types don't match exactly it has to call the API PyType_IsSubType. The code for that function is shown below. Probably we can write something somewhat faster that covers many of the situations we need, because we don't need to worry about the MRO (method resolution order) stuff.\n\n```\n/* type test with subclassing support */\n\nint\nPyType_IsSubtype(PyTypeObject *a, PyTypeObject *b)\n{\n        PyObject *mro;\n\n        if (!(a->tp_flags & Py_TPFLAGS_HAVE_CLASS))\n                return b == a || b == &PyBaseObject_Type;\n\n        mro = a->tp_mro;\n        if (mro != NULL) {\n                /* Deal with multiple inheritance without recursion\n                   by walking the MRO tuple */\n                Py_ssize_t i, n;\n                assert(PyTuple_Check(mro));\n                n = PyTuple_GET_SIZE(mro);\n                for (i = 0; i < n; i++) {\n                        if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)\n                                return 1;\n                }\n                return 0;\n        }\n        else {\n                /* a is not completely initilized yet; follow tp_base */\n                do {\n                        if (a == b)\n                                return 1;\n                        a = a->tp_base;\n                } while (a != NULL);\n                return b == &PyBaseObject_Type;\n        }\n}\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/115\n\n",
    "closed_at": "2010-08-26T20:22:44Z",
    "created_at": "2006-10-07T17:47:44Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "study alternatives to PyType_IsSubtype",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/115",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: cwitty

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


Issue created by migration from https://trac.sagemath.org/ticket/115





---

archive/issue_events_000227.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T03:31:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/115#event-227"
}
```



---

archive/issue_comments_000540.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2009-06-07T13:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/115#issuecomment-540",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_000541.json:
```json
{
    "body": "Changing component from basic arithmetic to misc.",
    "created_at": "2009-06-07T13:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/115#issuecomment-541",
    "user": "https://github.com/loefflerd"
}
```

Changing component from basic arithmetic to misc.



---

archive/issue_events_000228.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-08-26T20:22:44Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/115#event-228"
}
```



---

archive/issue_events_000229.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-08-26T20:22:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/115#event-229"
}
```



---

archive/issue_comments_000542.json:
```json
{
    "body": "I'm going to close this as invalid.  I made a copy of this ticket on the Cython Trac site: http://trac.cython.org/cython_trac/ticket/572",
    "created_at": "2010-08-26T20:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/115#issuecomment-542",
    "user": "https://github.com/mwhansen"
}
```

I'm going to close this as invalid.  I made a copy of this ticket on the Cython Trac site: http://trac.cython.org/cython_trac/ticket/572



---

archive/issue_events_000230.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-08-26T20:22:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/115#event-230"
}
```



---

archive/issue_comments_000543.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-08-26T20:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/115#issuecomment-543",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
