# Issue 535: Mismatched free() / delete / delete [] (from modular/dirichlet.py)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-30 18:53:30

Assignee: mabshoff

From Sage 2.8.3rc3:

```
==25034== Mismatched free() / delete / delete []
==25034==    at 0x4A05130: operator delete(void*) (vg_replace_malloc.c:244)
==25034==    by 0x923CCB6: del_charstar (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libcsage.so)
==25034==    by 0x17AC7793: __pyx_f_3ntl_string_delete (ntl.c:996)
==25034==    by 0x17AC7F88: __pyx_f_3ntl_9ntl_ZZ_pX___repr__ (ntl.c:6314)
==25034==    by 0x443C61: _PyObject_Str (object.c:406)
==25034==    by 0x443D0A: PyObject_Str (object.c:426)
==25034==    by 0x44EA8F: string_new (stringobject.c:3892)
==25034==    by 0x45A272: type_call (typeobject.c:422)
==25034==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==25034==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==25034==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==25034==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 18:53:36

Changing status from new to assigned.


---

Comment by malb created at 2007-08-30 19:28:22

This is caused because the char arrays in ntl_wrap.cc are created using 'new' and free'd in Cython using 'free'. This has been fixed before (i.e. it is a regression) by replacing the 'new' calls with 'malloc's. malloc is the correct memory allocator here because the string is returned to C land.


---

Comment by was created at 2007-09-13 15:26:32

Unfortunately at least in the code I'm looking at right now the array is freed using delete.  Could you
retest.  Here's all the relevant code (from ntl_wrap.cc, ntl.pyx and misc.pxi).  There's no malloc or free involved:

```
    def __repr__(self):
        _sig_on
        return string_delete(ZZ_pX_repr(self.x))

char* ZZ_pX_repr(struct ZZ_pX* x)
{
  ostringstream instore;
  instore << (*x);
  int n = strlen(instore.str().data());
  char* buf = new char[n+1];
  strcpy(buf, instore.str().data());
  return buf;
}

cdef object string_delete(char* s):
    """
    Takes a char* allocated using C++ new, and converts it to a Python
    string, then deletes the allocated memory.  Also unsets the signal
    handler, so you *must* call _sig_on right before calling this!
    """
    _sig_off
    t = str(s)
    del_charstar(s)
    return t

void del_charstar(char* a) {
  delete a;
}
```



---

Comment by mabshoff created at 2007-09-13 19:39:52

Resolution: fixed
