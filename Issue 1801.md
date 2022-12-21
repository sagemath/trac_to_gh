# Issue 1801: [with spkg] Update cython package to 0.9.6.11

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-01-17 18:52:55

Assignee: mabshoff

http://sage.math.washington.edu/home/robertwb/cython/

everything passes with sage -testall 

Main improvements:
 * `PyObject_CallObject -> PyObject_Call` (up to 5% speed increase for python function calls)
 * More correct .pyx file annotation (the click-able yellow lines)
 * Better support for non-GC objects
 * Optimized tp_new/dealloc/traverse/clear slots (similar to our first attempt to speed up  integers, but globally)
 * Re-enable pre-import (e.g. from sage.all import *)
 * `__cinit__` (a.k.a `__new__`) can have optimized signature `__new__(self)` regardless of `__init__` params
 * correct overflow error handling for all c int types (before just long was handled correctly)
 * (optional) for i in range(...) -> for i from ... conversion
 * several minor bug fixes
 * cleaned up spkg


---

Comment by robertwb created at 2008-01-17 19:01:58

Changing type from defect to enhancement.


---

Comment by robertwb created at 2008-01-17 19:01:58

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-17 19:01:58

Changing assignee from mabshoff to robertwb.


---

Comment by mabshoff created at 2008-01-18 05:20:00

With Sage 2.10 [more or less final] I get:

```
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/local//include -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/local//include/csage -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/devel//sage/sage/ext -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/include/python2.5 -c sage/libs/pari/gen.c -o build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w
sage/libs/pari/gen.c: In function ‘__pyx_tp_clear_4sage_4libs_4pari_3gen_PariInstance’:
sage/libs/pari/gen.c:33063: error: invalid lvalue in assignment
sage/libs/pari/gen.c:33066: error: invalid lvalue in assignment
sage/libs/pari/gen.c:33069: error: invalid lvalue in assignment
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

This corresponds to:

```
static int __pyx_tp_clear_4sage_4libs_4pari_3gen_PariInstance(PyObject *o) {
  struct __pyx_obj_4sage_4libs_4pari_3gen_PariInstance *p = (struct __pyx_obj_4sage_4libs_4pari_3gen_PariInstance *)o;
  PyObject* tmp;
  if (__pyx_ptype_4sage_9structure_11parent_base_ParentWithBase->tp_clear) {
    __pyx_ptype_4sage_9structure_11parent_base_ParentWithBase->tp_clear(o);
  }
  tmp = ((PyObject*)p->ZERO);
  ((PyObject*)p->ZERO) = Py_None; Py_INCREF(Py_None); [line 33063]
  Py_XDECREF(tmp);
  tmp = ((PyObject*)p->ONE);
  ((PyObject*)p->ONE) = Py_None; Py_INCREF(Py_None);
  Py_XDECREF(tmp);
  tmp = ((PyObject*)p->TWO);
  ((PyObject*)p->TWO) = Py_None; Py_INCREF(Py_None);
  Py_XDECREF(tmp);
  return 0;
}
```


Cheers,

Michael


---

Comment by robertwb created at 2008-01-18 06:06:38

New Cython package up at the same url which should resolve this issue.


---

Comment by mabshoff created at 2008-01-18 06:35:56

I can confirm that the latest cython.spkg completes a `sage -ba` without issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-19 18:03:13

Merged cython-0.9.6.11b.spkg in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-19 18:03:13

Resolution: fixed
