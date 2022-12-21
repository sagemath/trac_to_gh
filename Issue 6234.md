# Issue 6234: make parallel GCC'ing of Sage library not experimental

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-06 16:47:27

Assignee: craigcitro

CC:  mhansen ncalexan

Just get rid of the SAGE_PARALLEL_DIST check here in `devel/sage/setup.py`:


```
        # See if we're trying out the experimental parallel build
        # code.
        if ncpus > 1 and os.environ.has_key('SAGE_PARALLEL_DIST'):
```



---

Comment by craigcitro created at 2009-06-09 09:53:58

I've added a patch that removes the check for the `SAGE_PARALLEL_DIST` flag, and adds a few comments at the top. This should be pretty easy to review; if it makes anyone feel better, I'll probably be using it while merging tickets, and I can report back.


---

Attachment


---

Comment by craigcitro created at 2009-06-10 00:39:57

Fixed patch to correct a silly typo noted by Nick.


---

Comment by davidloeffler created at 2009-06-10 10:32:49

This wasn't showing up in the "needs review" list, because that does a text search for "needs review" and thus misses "needs easy review".


---

Comment by ncalexan created at 2009-06-11 20:31:11

I can't say for certain that this is at fault, but this was from the build of 4.0.2.alpha0 on sage.math:


```
...
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\
tch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\
eleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix2.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix2.o -w
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pEX.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lcsage \
-lntl -lgmp -lgmpxx -lm -lstdc++ -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pEX.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local/lib/python2.5/si\
te-packages/numpy/core/include -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//inc\
lude/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local/include/python2.5 \
-c sage/matrix/matrix_complex_double_dense.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.o -w
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/action.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lstdc++ -lntl\
 -o build/lib.linux-x86_64-2.5/sage/matrix/action.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\
tch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\
eleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix_cyclo_dense.cpp -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_cyclo_dense.\
o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -\
lcsage -lcblas -latlas -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\
tch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\
eleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix_dense.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_dense.o -w
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pX.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lcsage -\
lntl -lgmp -lgmpxx -lm -lstdc++ -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pX.so
error: could not create 'build/temp.linux-x86_64-2.5/sage/matrix': File exists
sage: There was an error installing modified sage library code.

ERROR installing SAGE
...
```



---

Attachment


---

Comment by craigcitro created at 2009-06-12 02:14:09

I think that's a race condition -- I suspect two calls to build_ext simultaneously realize that there's no directory to store a file and try to create it at the same time. The first is okay, but the second gets an error and bails.

The attached patch should fix this, as long as that's what's going on -- it creates all the appropriate directories in `build/` while processing files in serial, thereby eliminating the potential race problem.


---

Comment by ncalexan created at 2009-06-12 06:54:16

Real test will sage-4.0.2.alpha1.


---

Comment by craigcitro created at 2009-06-12 08:07:11

Resolution: fixed
