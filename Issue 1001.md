# Issue 1001: "Use of uninitialised value of size 4" in pari.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-26 02:20:40

Assignee: was

Just by doing a sage start + immediate quit under valgrind leads to:

```
==12979== Conditional jump or move depends on uninitialised value(s)
==12979==    at 0x8088C18: PyObject_Free (obmalloc.c:920)
==12979==    by 0x8106892: code_dealloc (codeobject.c:270)
==12979==    by 0x810C769: frame_dealloc (frameobject.c:444)
==12979==    by 0x80EBB0B: tb_dealloc (traceback.c:34)
==12979==    by 0x5764226: __Pyx_GetExcValue (gen.c:30664)
==12979==    by 0x5788110: __pyx_f_py_3gen_12PariInstance___call__ (gen.c:23295)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
==12979==    by 0x80BE7CB: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12979==    by 0x805A48F: PyObject_CallObject (abstract.c:1851)
==12979==    by 0x5791B62: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21789)
==12979==    by 0x809C412: type_call (typeobject.c:436)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
==12979==
==12979== Use of uninitialised value of size 4
==12979==    at 0x8088C23: PyObject_Free (obmalloc.c:920)
==12979==    by 0x8106892: code_dealloc (codeobject.c:270)
==12979==    by 0x810C769: frame_dealloc (frameobject.c:444)
==12979==    by 0x80EBB0B: tb_dealloc (traceback.c:34)
==12979==    by 0x5764226: __Pyx_GetExcValue (gen.c:30664)
==12979==    by 0x5788110: __pyx_f_py_3gen_12PariInstance___call__ (gen.c:23295)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
==12979==    by 0x80BE7CB: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12979==    by 0x805A48F: PyObject_CallObject (abstract.c:1851)
==12979==    by 0x5791B62: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21789)
==12979==    by 0x809C412: type_call (typeobject.c:436)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
```

I tracked this down to gen.pyx:5566:

```
        self.ONE = self(1)
```

but I have no clue how to fix this.

Cheers,

Michael



---

Comment by craigcitro created at 2007-10-28 06:04:35

this is likely fixed by the fix for #875, since the offending line in gen.pyx has been changed.


---

Comment by mabshoff created at 2007-10-28 06:47:53

Resolution: invalid


---

Comment by mabshoff created at 2007-10-28 06:48:16


```
[07:35] <cwitty> Whenever you pass an address to PyObject_Free, it will read the first 4 bytes of the 4096-byte page containing that address.  If Python allocated that memory, then those 4 bytes will be valid to read.  But if the system malloc allocated them, then there may or may not be valid (according to valgrind) data there.
[07:35] <cwitty> It just depends on the particular history of allocations/frees in the program so far.
```



---

Comment by cwitty created at 2007-10-28 06:50:34

For more details, read the comment describing Py_ADDRESS_IN_RANGE, in Objects/obmalloc.c in the Python source code.
