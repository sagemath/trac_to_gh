# Issue 3604: zlib: Conditional jump or move depends on uninitialised value(s)

Issue created by migration from https://trac.sagemath.org/ticket/3604

Original creator: mabshoff

Original creation time: 2008-07-08 11:41:58

Assignee: mabshoff

Valgrind says:

```
==10847== Conditional jump or move depends on uninitialised value(s)
==10847==    at 0x7D39F9D: longest_match (deflate.c:1121)
==10847==    by 0x7D3B368: deflate_slow (deflate.c:1595)
==10847==    by 0x7D39462: deflate (deflate.c:790)
==10847==    by 0x7C2D96A: PyZlib_compress (zlibmodule.c:166)
==10847==    by 0x4F0F28: PyCFunction_Call (methodobject.c:73)
==10847==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==10847==    by 0x7B0C9A9: __pyx_pf_4sage_9structure_11sage_object_10SageObject_dumps (sage_object.c:1591)
==10847==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)
==10847==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==10847==    by 0x7B197E8: __pyx_pf_4sage_9structure_11sage_object_dumps (sage_object.c:5184)
==10847==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)
==10847==    by 0x494A6E: call_function (ceval.c:3573)
```

This corresponds to:

```
def dumps(obj, compress=True):
    """
    dumps(obj):

    Dump obj to a string s.  To recover obj, use loads(s).

    EXAMPLES:
        sage: a = 2/3
        sage: s = dumps(a)
        sage: print len(s)
        49
        sage: loads(s)
        2/3
    """
    if make_pickle_jar:
        picklejar(obj)
    try:
        return obj.dumps(compress) [this is sage_object.c:5184]
    except (AttributeError, RuntimeError, TypeError):
        if compress:
            return comp.compress(cPickle.dumps(obj, protocol=2))
        else:
            return cPickle.dumps(obj, protocol=2)
```

And

```
    def dumps(self, compress=True):
        """
        Dump self to a string s, which can later be reconstituted
        as self using loads(s).
        """
        # the protocol=2 is very important -- this enables
        # saving extensions classes (with no attributes).
        s = cPickle.dumps(self, protocol=2)
        if compress:
            return comp.compress(s) [sage_object.c:1591]
        else:
            return s
```



---

Comment by mabshoff created at 2008-07-08 11:42:32

I suspect the underlying issue to be in zlib itself.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-08 11:42:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-08 11:48:08

This happens in many cases, the specific valgrind log is from elementary.py.

Cheers,

Michael


---

Comment by cwitty created at 2008-07-10 03:12:02

The zlib people say this isn't an actual problem, and fixing it would slow things down, so they won't fix it:
http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=270070


---

Comment by mabshoff created at 2008-08-19 01:09:11

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 01:09:11

This is wontfix, but I have added a suppression for this issue in the latest valgrind.spkg.

Cheers,

Michael
