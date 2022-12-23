# Issue 4778: [with patch, needs review] Creates Scilab pexpect interface

Issue created by migration from https://trac.sagemath.org/ticket/4778

Original creator: ronanpaixao

Original creation time: 2008-12-13 02:53:25

Assignee: ronanpaixao

Keywords: scilab

Creates an interface to Scilab numerical math software, available at www.scilab.org

Tested with Scilab version 5.0.3


---

Comment by jsp created at 2008-12-15 15:26:13

Changing component from optional packages to interfaces.


---

Comment by jsp created at 2008-12-15 15:26:13

Installed scilab-5.0.3 with ./configure --without-javasci --without-gui

Had to install matio



```
[jaap@paix scilab-5.0.3]$ bin/scilab -nogui
Warning: Localization issue: Error while binding the domain from /home/jaap/downloads/scilab-5.0.3/../locale/ or /home/jaap/downloads/scilab-5.0.3/locale/: Switch to the default language (English).
        ___________________________________________        
                       scilab-5.0.3

                 Consortium Scilab (DIGITEO)
               Copyright (c) 1989-2008 (INRIA)
               Copyright (c) 1989-2007 (ENPC)
        ___________________________________________        
 
 
Startup execution:
  loading initial environment
 
-->

```


Running ./sage -t -optional -verbose devel/sage/sage/interfaces/scilab.py

1 failure:


```
Trying:
    a**Integer(10)                              # optional - scilab###line 19:_sage_    >>> a**10                              # optional - scilab
Expecting:
       1.000D+10
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha2/devel/sage/sage/interfaces/scilab.py", line 106, in __main__.example_0
Failed example:
    a**Integer(10)                              # optional - scilab###line 19:_sage_    >>> a**10                              # optional - scilab
Expected:
       1.000D+10
Got:
    <BLANKLINE>
    <BLANKLINE>
        1.000E+10

```


See: [http://sage.math.washington.edu/home/jsp/tests/scilabtest.log](http://sage.math.washington.edu/home/jsp/tests/scilabtest.log)

No failures in matrix1.pyx

So no positive review yet.

Jaap


---

Comment by ronanpaixao created at 2008-12-15 17:40:23

Strangely, this test passes here, since Scilab uses D notation here. This looks like a localization issue, specially since I don't get this warning in the beginning of the console session. I also found it strange to use this D instead of E, but since those french guys love breaking standards, I didn't mind. I'll see if I can set this up though.


---

Comment by jsp created at 2008-12-15 23:36:09

Substitute:

s/1.000D/1.000E/

and most people will be happy :-)! For instance you with a positive review.

Jaap


---

Comment by jsp created at 2008-12-15 23:40:52

Replying to [comment:3 jsp]:
> Substitute:
> 
> s/1.000D/1.000E/
> 
> and most people will be happy :-)! For instance you with a positive review.
> 
> Jaap
> 

[jaap`@`paix sage-3.2.2.alpha2]$ ./sage -t -optional devel/sage/sage/interfaces/scilab.py 
sage -t -optional "devel/sage/sage/interfaces/scilab.py"    
	 [9.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.9 seconds


---

Comment by ronanpaixao created at 2008-12-16 00:34:23

patch file, with preliminary E notation fix for doctest


---

Attachment

Looks good to me:



```
137 tests in 24 items.
137 passed and 0 failed.
Test passed.
	 [8.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.0 seconds

```



---

Comment by mabshoff created at 2008-12-17 14:51:19

Ronan,

for future references: The name of the patch ought to be trac_XXXX_description.patch, not the commit number from the hg repo.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 15:06:39

This patch needs two simple one line fixes to make more doctests optional:

```
sage -t -long "devel/sage/sage/interfaces/scilab.py"        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/devel/sage/sage/interfaces/scilab.py", line 269:
    sage: scilab.eval("5")
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[2]>", line 1, in <module>
        scilab.eval("5")###line 269:
    sage: scilab.eval("5")
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/scilab.py", line 274, in eval
        s = Expect.eval(self, command).replace("\x1b[?1l\x1b>","").strip()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 937, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 633, in _eval_line
        self._start()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/scilab.py", line 261, in _start
        Expect._start(self)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 470, in _start
        raise RuntimeError, "Unable to start %s"%self.__name
    RuntimeError: Unable to start scilab
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/devel/sage/sage/interfaces/scilab.py", line 271:
    sage: scilab.eval("d=44")
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        scilab.eval("d=44")###line 271:
    sage: scilab.eval("d=44")
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/scilab.py", line 274, in eval
        s = Expect.eval(self, command).replace("\x1b[?1l\x1b>","").strip()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 937, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 633, in _eval_line
        self._start()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/scilab.py", line 261, in _start
        Expect._start(self)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 470, in _start
        raise RuntimeError, "Unable to start %s"%self.__name
    RuntimeError: Unable to start scilab
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.rc1/tmp/.doctest_scilab.py
	 [2.3 s]
exit code: 1024
```


Reviewer patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 15:08:00

By the way:

```
        EXAMPLES:
            sage: scilab.eval("5")                      # optional - scilab
            'ans  =\n \n    5.'
            sage: scilab.eval("d=44")                   # optional - scilab
            'd  =\n \n    44.'
```

This is plain ugly and needs to be fixed, i.e. stripping out the newlines and spaces.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 15:11:36

Merged in Sage 3.2.2.rc1. I fixed the issue in the patch itself.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 15:11:36

Resolution: fixed


---

Comment by ronanpaixao created at 2008-12-19 16:49:46

I know the newlines are ugly, but I left it as-is because correcting those would require a lot of strips which could truncate output in unexpected ways. I believe the principle of eval is to return whatever the program outputs to the user and let him do the processing. Imagine, for example, if one strips all newlines: the output of whos() would then be all rendered in one line, completely breaking the tables.

Then, I thought about stripping at least the output of get() but then I ran into a problem with matrix formatting, in which the first line of a matrix would be misaligned, not to mention that taking newlines off would display matrices in a single line.

Ronan
