# Issue 4036: [with patch, needs review] minor improvements to the Axiom interface

Issue created by migration from https://trac.sagemath.org/ticket/4036

Original creator: mhansen

Original creation time: 2008-09-01 23:34:49

Assignee: was




---

Attachment


---

Attachment


---

Attachment

patches apply to 3.1.2.rc1 and doctests pass in `sage/interfaces`, with the following exceptions:

```
sage -t  devel/sage/sage/interfaces/psage.py
End Of File (EOF) in read_nonblocking(). Empty string style platform.
<pexpect.spawn instance at 0x7550f80>
version: 2.0 ($Revision: 1.151 $)
command: /Users/rlmill/sage-3.1.2.rc1/sage
args: ['/Users/rlmill/sage-3.1.2.rc1/sage']
patterns:
    sage: 
buffer (last 100 chars): 
before (last 100 chars): 
after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 27789
child_fd: 5
timeout: 30
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 100000
searchwindowsize: None
delaybeforesend: 0
	 [14.6 s]
```

This one passes, but...

And this one:

```
sage -t  devel/sage/sage/interfaces/lisp.py
**********************************************************************
File "/Users/rlmill/sage-3.1.2.rc1/tmp/lisp.py", line 282:
    sage: lisp.version()
Expected:
    GNU CLISP ... (...) (built ...) (memory ...)
    ...
Got:
    GNU CLISP 2.46 (2008-07-02) (built on robert-millers-macbook-pro-15.local [192.168.0.101])
    Software: GNU C 4.0.1 (Apple Inc. build 5465) 
    gcc -O0 -g -I/Users/rlmill/sage-3.1.2.rc1/local/include/ -L/Users/rlmill/sage-3.1.2.rc1/local/lib/ -W -Wswitch -Wcomment -Wpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-sign-compare -O0 -fexpensive-optimizations -falign-functions=4 -DUNIX_BINARY_DISTRIB -DUNICODE -DNO_GETTEXT -DNO_SIGSEGV -I. -x none -lreadline -lncurses  -liconv  -L/usr/X11/lib -R/usr/X11/lib
    SAFETY=0 HEAPCODES STANDARD_HEAPCODES SPVW_BLOCKS SPVW_MIXED TRIVIALMAP_MEMORY
    libiconv 1.11
    libreadline 5.2
    Features: 
    (REGEXP SYSCALLS I18N LOOP COMPILER CLOS MOP CLISP ANSI-CL COMMON-LISP LISP=CL
     INTERPRETER SOCKETS GENERIC-STREAMS LOGICAL-PATHNAMES SCREEN UNICODE
     BASE-CHAR=CHARACTER UNIX MACOS)
    C Modules: (clisp i18n syscalls regexp)
    Installation directory: /Users/rlmill/sage-3.1.2.rc1/local/lib/clisp-2.46/
    User language: ENGLISH
    Machine: I386 (I386) D-69-91-148-44.dhcp4.washington.edu [69.91.148.44]
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_14
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/rlmill/sage-3.1.2.rc1/tmp/.doctest_lisp.py

	 [3.2 s]
```



---

Comment by rlm created at 2008-09-15 00:59:14

...both of which failed before applying too. Looks good to me!


---

Comment by mabshoff created at 2008-09-15 03:05:08

This patch introduces the following problem:

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/parent.py", line 13:
    sage: gp(2) + gap(3)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        gp(Integer(2)) + gap(Integer(3))###line 13:
    sage: gp(2) + gap(3)
      File "element.pyx", line 718, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5748)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 662, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6364)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'GP/PARI interpreter' and 'Gap'
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-15 03:28:55

And this one, too:

```
sage -t -long devel/sage/sage/matrix/matrix_symbolic_dense.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/matrix_symbolic_dense.py", line 185:
    sage: print "ignore this";  hash(maxima(m)) #random due to architecture dependence
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[5]>", line 1, in <module>
        print "ignore this";  hash(maxima(m)) #random due to architecture dependence###line 185:
    sage: print "ignore this";  hash(maxima(m)) #random due to architecture dependence
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 984, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1008, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "matrix_symbolic_dense.pyx", line 383, in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._maxima_ (sage/matrix/matrix_symbolic_dense.c:3536)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 977, in __call__
        return self(x._sage_())
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 1440, in _sage_
        return symbolic_expression_from_maxima_string(repr(self))
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 8515, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in SAGE"%s
    TypeError: unable to make sense of Maxima expression 'matrix([sqrt(2),3],[pi,e])' in SAGE
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/matrix_symbolic_dense.py", line 377:
    sage: m._maxima_(maxima)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[4]>", line 1, in <module>
        m._maxima_(maxima)###line 377:
    sage: m._maxima_(maxima)
      File "matrix_symbolic_dense.pyx", line 383, in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._maxima_ (sage/matrix/matrix_symbolic_dense.c:3536)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 977, in __call__
        return self(x._sage_())
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 1440, in _sage_
        return symbolic_expression_from_maxima_string(repr(self))
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 8515, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in SAGE"%s
    TypeError: unable to make sense of Maxima expression 'matrix([sqrt(2),3],[pi,e])' in SAGE
**********************************************************************
```



---

Attachment

This patch should fix the issues.


---

Comment by mabshoff created at 2008-10-28 14:46:24

We need a review for the four patches together. The issue rlm saw is unrelated to this patch.

Cheers,

Michael


---

Comment by was created at 2008-11-27 17:17:13

This needs to be rebased against sage-3.2.1.*:

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4036/trac_4036.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4036/trac_4036.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/10714/tmp_0.patch"
applying /home/was/.sage/temp/sage/10714/tmp_0.patch
patching file sage/rings/integer_mod.pyx
Hunk #1 FAILED at 361
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/integer_mod.pyx.rej
abort: patch failed to apply
```



---

Attachment

add fricas tests to axiom.py


---

Comment by awebb created at 2009-08-17 15:15:42

The content of these patches seems to have already been applied. In fact, most have been expanded with tests for fricas. I added some more tests for fricas, if desired. 

Adam


---

Comment by awebb created at 2009-08-27 13:13:12

Thinking about it. I think it would be less confusing if this ticket is just closed and anything new for fricas put into a new one.  ~ Adam


---

Comment by mhansen created at 2009-10-05 06:53:58

Resolution: duplicate


---

Comment by mhansen created at 2009-10-05 06:53:58

This was indeed fixed as part of #5111.  I'm going ahead and closing it.
