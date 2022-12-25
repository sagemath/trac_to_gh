# Issue 1801: [with spkg] Update cython package to 0.9.6.11

archive/issues_001801.json:
```json
{
    "body": "Assignee: mabshoff\n\nhttp://sage.math.washington.edu/home/robertwb/cython/\n\neverything passes with sage -testall \n\nMain improvements:\n* `PyObject_CallObject -> PyObject_Call` (up to 5% speed increase for python function calls)\n* More correct .pyx file annotation (the click-able yellow lines)\n* Better support for non-GC objects\n* Optimized tp_new/dealloc/traverse/clear slots (similar to our first attempt to speed up  integers, but globally)\n* Re-enable pre-import (e.g. from sage.all import *)\n* `__cinit__` (a.k.a `__new__`) can have optimized signature `__new__(self)` regardless of `__init__` params\n* correct overflow error handling for all c int types (before just long was handled correctly)\n* (optional) for i in range(...) -> for i from ... conversion\n* several minor bug fixes\n* cleaned up spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/1801\n\n",
    "created_at": "2008-01-17T18:52:55Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with spkg] Update cython package to 0.9.6.11",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1801",
    "user": "https://github.com/robertwb"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/1801





---

archive/issue_comments_011363.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-01-17T19:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11363",
    "user": "https://github.com/robertwb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_011364.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-17T19:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11364",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011365.json:
```json
{
    "body": "Changing assignee from mabshoff to @robertwb.",
    "created_at": "2008-01-17T19:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11365",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from mabshoff to @robertwb.



---

archive/issue_comments_011366.json:
```json
{
    "body": "With Sage 2.10 [more or less final] I get:\n\n```\ngcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/local//include -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/local//include/csage -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/devel//sage/sage/ext -I/scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/include/python2.5 -c sage/libs/pari/gen.c -o build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w\nsage/libs/pari/gen.c: In function \u2018__pyx_tp_clear_4sage_4libs_4pari_3gen_PariInstance\u2019:\nsage/libs/pari/gen.c:33063: error: invalid lvalue in assignment\nsage/libs/pari/gen.c:33066: error: invalid lvalue in assignment\nsage/libs/pari/gen.c:33069: error: invalid lvalue in assignment\nerror: command 'gcc' failed with exit status 1\nsage: There was an error installing modified sage library code.\n```\n\nThis corresponds to:\n\n```\nstatic int __pyx_tp_clear_4sage_4libs_4pari_3gen_PariInstance(PyObject *o) {\n  struct __pyx_obj_4sage_4libs_4pari_3gen_PariInstance *p = (struct __pyx_obj_4sage_4libs_4pari_3gen_PariInstance *)o;\n  PyObject* tmp;\n  if (__pyx_ptype_4sage_9structure_11parent_base_ParentWithBase->tp_clear) {\n    __pyx_ptype_4sage_9structure_11parent_base_ParentWithBase->tp_clear(o);\n  }\n  tmp = ((PyObject*)p->ZERO);\n  ((PyObject*)p->ZERO) = Py_None; Py_INCREF(Py_None); [line 33063]\n  Py_XDECREF(tmp);\n  tmp = ((PyObject*)p->ONE);\n  ((PyObject*)p->ONE) = Py_None; Py_INCREF(Py_None);\n  Py_XDECREF(tmp);\n  tmp = ((PyObject*)p->TWO);\n  ((PyObject*)p->TWO) = Py_None; Py_INCREF(Py_None);\n  Py_XDECREF(tmp);\n  return 0;\n}\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-18T05:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11366",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_011367.json:
```json
{
    "body": "New Cython package up at the same url which should resolve this issue.",
    "created_at": "2008-01-18T06:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11367",
    "user": "https://github.com/robertwb"
}
```

New Cython package up at the same url which should resolve this issue.



---

archive/issue_comments_011368.json:
```json
{
    "body": "I can confirm that the latest cython.spkg completes a `sage -ba` without issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-18T06:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11368",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I can confirm that the latest cython.spkg completes a `sage -ba` without issues.

Cheers,

Michael



---

archive/issue_comments_011369.json:
```json
{
    "body": "Merged cython-0.9.6.11b.spkg in Sage 2.10.1.alpha0",
    "created_at": "2008-01-19T18:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11369",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged cython-0.9.6.11b.spkg in Sage 2.10.1.alpha0



---

archive/issue_comments_011370.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T18:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1801#issuecomment-11370",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
