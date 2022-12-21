# Issue 3491: slightly polish/improve how the cython pyx caching thing works

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-22 17:01:28

Assignee: mabshoff

Consider this unpleasant session.


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3119/sage-3119-part4.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3119/sage-3119-part4.patch?format=raw
Loading: [.]
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg import   "/Users/was/.sage/temp/teragon_2.local/2582/tmp_3.patch"
applying /Users/was/.sage/temp/teragon_2.local/2582/tmp_3.patch
sage: 
Exiting SAGE (CPU time 0m0.27s, Wall time 0m44.10s).
teragon-2:~ was$ sage -br

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
running install
running build
running build_py
copying sage/libs/mwrank/interface.py -> build/lib.macosx-10.3-i386-2.5/sage/libs/mwrank
copying sage/schemes/elliptic_curves/ell_rational_field.py -> build/lib.macosx-10.3-i386-2.5/sage/schemes/elliptic_curves
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.

teragon-2:~ was$ touch ~/d/sage/sage/libs/mwrank/mwrank.pyx
teragon-2:~ was$ sage -br

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
sage/libs/mwrank/mwrank.pyx --> /Users/was/s/local//lib/python/site-packages//sage/libs/mwrank/mwrank.pyx

Building sage/libs/mwrank/mwrank.c because it depends on sage/libs/mwrank/mwrank.pyx.
python2.5 `which cython` --embed-positions --incref-local-binop -I/Users/was/s/devel/sage-review -o sage/libs/mwrank/mwrank.c sage/libs/mwrank/mwrank.pyx
Finished updating Cython code (time = 5.777133 seconds)

```


So applying a patch introduced a .pyx file but the cache doesn't notice it because
it is new.  This is a big problem.   Maybe including the latest something from the
.hg directory in the cython .pyx hash that is computed in setup.py would very nicely
fix this. 

William


---

Comment by mabshoff created at 2008-08-14 22:49:01

Resolution: duplicate


---

Comment by mabshoff created at 2008-08-14 22:49:01

This is a dupe of #3310.

Cheers,

Michael
