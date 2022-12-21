# Issue 1222: cvxopt import trouble on PPC OSX 10.4 with 2.8.13.rc0

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 22:51:10

Assignee: mabshoff


```
michael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$ ./sage -
t  devel/sage-main/sage/numerical/test.py
sage -t  devel/sage-main/sage/numerical/test.py
**********************************************************************
File "test.py", line 4:
    : from cvxopt.base import *
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/Desktop/sage-2.8.13.rc0/local/lib/
python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[0]>", line 1, in <module>
        from cvxopt.base import *###line 4:
    : from cvxopt.base import *
    ImportError: dlopen(/Users/mabshoff/Desktop/sage-2.8.13.rc0/local/
lib/python/site-packages/cvxopt/base.so, 2): Symbol not found:
__g95_ioparm
      Referenced from: /Users/mabshoff/Desktop/sage-2.8.13.rc0/local/
lib/python/site-packages/cvxopt/base.so
      Expected in: dynamic lookup

**********************************************************************
File "test.py", line 5:
    : from cvxopt import umfpack
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/Desktop/sage-2.8.13.rc0/local/lib/
python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[1]>", line 1, in <module>
        from cvxopt import umfpack###line 5:
    : from cvxopt import umfpack
    ImportError: dlopen(/Users/mabshoff/Desktop/sage-2.8.13.rc0/local/
lib/python/site-packages/cvxopt/umfpack.so, 2): Symbol not found:
__g95_st_write_done
      Referenced from: /Users/mabshoff/Desktop/sage-2.8.13.rc0/local/
lib/python/site-packages/cvxopt/umfpack.so
      Expected in: dynamic lookup

**********************************************************************
1 items had failures:
   2 of   6 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_test.py
         [13.2 s]
exit code: 256
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 22:51:18

Changing status from new to assigned.


---

Comment by jkantor created at 2007-11-21 06:03:28

This should be easy to fix. I would do it myself, except I don't have access to a ppc machine so its probably easier to explain what to do. 
In the /patches/ directory of the spkg the file setup_f95.py is the setup.py used if they are compiling with g95. Near the top there is a block.

if os.uname()[0].startswith('Linux'):
    if os.uname()[-1]!='x86_64':
        GCC_LIB_DIR= SAGE_LOCAL+'/lib/gcc-lib/i686-pc-linux-gnu/4.0.3'
    else:
        GCC_LIB_DIR= SAGE_LOCAL+'/lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3'
    library_dirs = [ ATLAS_LIB_DIR,GCC_LIB_DIR]

If that error is showing up then this should be changed to 

if os.uname()[0].startswith('Linux'):
    if os.uname()[-1]!='x86_64':
        GCC_LIB_DIR= SAGE_LOCAL+'/lib/gcc-lib/i686-pc-linux-gnu/4.0.3'
    else:
        GCC_LIB_DIR= SAGE_LOCAL+'/lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3'
    if <we are on OSX ppc >:
        GCC_LIB_DIR= 'lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3'
    library_dirs = [ ATLAS_LIB_DIR,GCC_LIB_DIR]

Strangely, explicitly specifying the directory of the libf95.a does not appear to be necessary on 
OSX intel.


---

Comment by jkantor created at 2007-11-23 21:31:42

Hopefully this spkg fixes this, however I have not tested it since I don't have a ppc

http://sage.math.washington.edu/home/jkantor/spkgs/cvxopt-0.9.p2.spkg


---

Comment by jkantor created at 2007-11-27 04:26:43

New package fixing the ppc problem. 

http://sage.math.washington.edu/home/jkantor/cvxopt-0.9.p3.spkg


---

Comment by mabshoff created at 2007-11-27 13:39:03

Hmm, does cvxopt assume that ATLAS is installed now? On sage.math without ATLAS I now get:

```
Using g95Traceback (most recent call last):
  File "setup.py", line 56, in <module>
    if os.path.exists(ATLAS_LIB_DIR+'/libatlas.a') or os.path.exists(ATLAS_LIB_DIR+'/libatlas.dylib') or os.path.exits(ATLAS_LIB_DIR+'/libatlas.so'):
AttributeError: 'module' object has no attribute 'exits'
```

Cheers,

Michael


---

Comment by jkantor created at 2007-11-28 04:29:19

You must have been too quick. I had an os.exits, instead of os.exists. I changed it a moment after I posted the package. But you must have grabbed the old one first.


---

Comment by jkantor created at 2007-11-28 06:04:46

The current cvxopt.p3 has the above problem fixed, as well as correctly links against atlas (when present).


---

Comment by jkantor created at 2007-11-28 10:15:17

New version that will use our local libatlas on osx intel. 

http://sage.math.washington.edu/home/jkantor/spkgs/cvxopt-0.9.p4.spkg


---

Comment by jkantor created at 2007-11-29 10:53:35

the package above (.p4) was recently changed to reflect the fact that we won't be building libff7blas on OSX yet.


---

Comment by mabshoff created at 2007-12-01 22:39:07

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 22:39:07

Merged in 2.8.15.alpha2.
