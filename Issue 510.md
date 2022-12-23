# Issue 510: IPython crashes on "import sage.rings.real_mpfr"

Issue created by migration from https://trac.sagemath.org/ticket/510

Original creator: burcin

Original creation time: 2007-08-29 10:57:35

Assignee: was

Importing the module sage.rings.real_mpfr in IPython causes a segfault with the backtrace included below. SAGE itself doesn't report any errors in this case.

```
In [2]: import sage.rings.real_mpfr

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1210221920 (LWP 28996)]
0xb0d29b0e in __pyx_f_9real_mpfr_9RealField___init__ (__pyx_v_self=0xb0dc625c, 
    __pyx_args=0xb0ce242c, __pyx_kwds=0x0) at sage/rings/real_mpfr.c:1128
1128      Py_INCREF(__pyx_v_rnd);
(gdb) bt
#0  0xb0d29b0e in __pyx_f_9real_mpfr_9RealField___init__ (
    __pyx_v_self=0xb0dc625c, __pyx_args=0xb0ce242c, __pyx_kwds=0x0)
    at sage/rings/real_mpfr.c:1128
#1  0x0809c2f3 in type_call (type=0xb0d88d40, args=0xb0ce242c, kwds=0x0)
    at Objects/typeobject.c:436
#2  0x0805a0a7 in PyObject_Call (func=0x0, arg=0xb0ce242c, kw=0x0)
    at Objects/abstract.c:1860
#3  0x080c0c50 in PyEval_EvalFrameEx (f=0x83964ec, throwflag=0)
    at Python/ceval.c:3775
#4  0x080c564a in PyEval_EvalFrameEx (f=0x8392a9c, throwflag=0)
    at Python/ceval.c:3650
#5  0x080c639b in PyEval_EvalCodeEx (co=0xb0dd0ad0, globals=0xb0d9fc64, 
    locals=0x0, args=0xb0d963f8, argcount=2, kws=0x0, kwcount=0, 
    defs=0xb0ce2478, defcount=1, closure=0x0) at Python/ceval.c:2831
```


You can use the patch included in #509 to run IPython under gdb.



---

Comment by was created at 2007-08-31 20:09:10

This is not so much a bug as something that hasn't been implemented -- or even thought about yet.  It doesn't make sense to just load any random module into SAGE, since certain modules assume certain other modules have been imported first.  E.g., import sage.math first and the rest works fine:


```

In [1]: import sage.all

In [2]: import sage.rings.real_mpfr

```


In short, importing particular random modules without having import sage.all
first is *not* supported at present.  It would be a good enhancement to implement
something to force sage.all to be imported or something...


---

Comment by was created at 2007-08-31 20:09:10

Changing type from defect to enhancement.


---

Comment by craigcitro created at 2007-09-07 05:29:48

Changing component from algebraic geometry to interfaces.


---

Comment by mabshoff created at 2008-02-17 19:48:18

I would consider this bug report to be invalid - see the explanation by was above, so it should be closed as invalid. Any opinioins?

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 21:02:32


```
[21:42] <wstein> mabshoff -- close 510 as invalid.
[21:42] <mabshoff> ok
```



---

Comment by mabshoff created at 2008-02-17 21:02:32

Resolution: invalid


---

Comment by burcin created at 2008-02-18 08:48:33

I think this should still remain as an enhancement request, maybe in the sage-wishlist target.

The reason we get a segfault by importing `sage.rings.real_mpfr` before `sage.all` is that `sage.all` calls some initialization function for this library. From a software design point of view, this initialization should be handled closer to the place the library is used, possibly in the `__init__.py` of the corresponding wrapper. Then users will be able to import this module without worrying about importing `sage.all` and waiting to initialize many components they don't care about.

Even the fact that we don't know which initialization function needs to be called to fix the segfault is enough to regard this as a bug in the wrapper. Since nobody cares enough to look into this at the moment, we should at least keep note of it as an enhancement request which we could take up, once we have the time.

So I suggest we reopen this, and maybe resolve to `wontfix` instead of `invalid` next time.


---

Comment by mabshoff created at 2008-02-18 13:14:46

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-02-18 13:14:46

ok, I am convinced for now. If you can come up with a better summary for the bug please change it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-18 13:14:46

Resolution changed from invalid to 


---

Comment by burcin created at 2008-05-10 19:17:47

fix some circular imports in sage.rings.real_mpfr


---

Attachment

attachment:510_real_mpfr_imports.patch fixes the problem reported in the original report. With this patch, 

```
import sage.rings.complex_field
```

still fails because of similar errors. I'll write a script which imports each file in the tree individually and see if I can fix the errors.


---

Comment by mabshoff created at 2008-09-30 11:49:00

This ticket should be renamed and the patch that currently exists should be reviewed and hopefully merged. Since the patch is a little old it might have gone stale, but hopefully not.

If a test script exists we should definitely fix all the problems that it detects, but those problems should be handled via new tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 12:22:29

Amazingly this patch still applies with some fuzz to my current 3.1.3.alpha2 merge tree:

```
age-3.1.3.alpha2/devel/sage$ patch -p1 --dry-run < 510_real_mpfr_imports.patch\?format\=raw 
patching file sage/rings/real_double.pxd
patching file sage/rings/real_double.pyx
Hunk #2 succeeded at 1088 (offset 9 lines).
patching file sage/rings/real_mpfr.pyx
Hunk #1 succeeded at 132 (offset 6 lines).
Hunk #2 succeeded at 158 (offset 6 lines).
Hunk #3 succeeded at 237 with fuzz 2 (offset 18 lines).
Hunk #4 succeeded at 468 (offset 63 lines).
Hunk #5 succeeded at 1879 (offset 191 lines).
patching file sage/rings/real_rqdf.pxd
patching file sage/rings/real_rqdf.pyx
Hunk #3 succeeded at 1263 (offset 4 lines).
```

I did not try to compile, but I consider this encouraging.


---

Attachment

script to test if importing a random module from the sage library returns an error


---

Comment by burcin created at 2008-10-15 16:48:26

Changing component from interfaces to misc.


---

Comment by burcin created at 2008-10-15 16:48:26

attachment:sage-test-import imports all modules in the given source tree, and prints out those which raise an error.


---

Comment by burcin created at 2008-10-15 17:09:45

I just tried attachment:510_real_mpfr_imports.patch. It still applies, and fixes the original problem reported, as I wrote in comment:7 previously.

The script attachment:sage-test-import lists many other problems of this kind, but feel free to apply this patch, and move the script to another ticket.


---

Comment by mabshoff created at 2008-10-27 03:38:09

Positive review on the patch. I also added the sage-test-import script to the local/bin repo. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 03:40:31

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 03:40:31

Merged in Sage 3.2.alpha1
