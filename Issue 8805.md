# Issue 8805: Bring doctest for sage/functions folder to 100%

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-04-28 15:24:51

Assignee: mvngu

Bring doctest for sage/functions folder to 100%.  Specifically:

```
functions/orthogonal_polys.py: 91% (11 of 12)
functions/other.py: 92% (26 of 28)
functions/piecewise.py: 93% (43 of 46)
functions/special.py: 69% (30 of 43)
functions/transcendental.py: 86% (13 of 15)
```



---

Comment by kcrisman created at 2010-04-30 11:22:33

Based on 4.4


---

Comment by kcrisman created at 2010-04-30 11:24:17

Changing status from new to needs_review.


---

Attachment

This only adds doctests, and does not address any TODOs in the files.


---

Attachment

Applying the patch [trac_8805-functions-dir-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-functions-dir-doctest.patch) and rebuilding the Sage library resulted in the following error:


```sh
[mvngu`@`sage sage-4.4.1.rc0-8805-functions]$ ./sage -b
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 1.69277191162e-05 seconds
Finished compiling Cython code (time = 0.367266178131 seconds)
running install
running build
running build_py
copying sage/functions/transcendental.py -> build/lib.linux-x86_64-2.6/sage/functions
copying sage/functions/special.py -> build/lib.linux-x86_64-2.6/sage/functions
copying sage/functions/piecewise.py -> build/lib.linux-x86_64-2.6/sage/functions
copying sage/functions/other.py -> build/lib.linux-x86_64-2.6/sage/functions
copying sage/functions/orthogonal_polys.py -> build/lib.linux-x86_64-2.6/sage/functions
running build_ext
Total time spent compiling C/C++ extensions:  0.0169429779053 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/functions/orthogonal_polys.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions
copying build/lib.linux-x86_64-2.6/sage/functions/other.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions
copying build/lib.linux-x86_64-2.6/sage/functions/piecewise.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions
copying build/lib.linux-x86_64-2.6/sage/functions/special.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions
copying build/lib.linux-x86_64-2.6/sage/functions/transcendental.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions
byte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/orthogonal_polys.py to orthogonal_polys.pyc
byte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/other.py to other.pyc
byte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/piecewise.py to piecewise.pyc
byte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/special.py to special.pyc
byte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/transcendental.py to transcendental.pyc
Sorry: IndentationError: ('unindent does not match any outer indentation level', ('/dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/transcendental.py', 491, 25, '      self._cur_prec = 0\n'))
running install_egg_info
Removing /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m1.411s
user	0m1.120s
sys	0m0.290s
```


This is due to bad indentation of the docstring in the constructor:


```python
    def __init__(self):
        """                                                                     
        TESTS::                                                                 
                                                                                
            sage: dickman_rho(x)                                                
            dickman_rho(x)                                                      
            sage: dickman_rho(3)                                                
            0.0486083882911316                                                  
            sage: dickman_rho(pi)                                               
            0.0359690758968463                                                  
        """
      self._cur_prec = 0
      BuiltinFunction.__init__(self, "dickman_rho", 1)
```


The reviewer patch fixes this and also includes a little more documentation. Only my patch needs review. If it gets a positive review, the whole ticket is good to go.


---

Comment by kcrisman created at 2010-05-03 14:38:31

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-05-03 14:38:31

Replying to [comment:2 mvngu]:

> 
> This is due to bad indentation of the docstring in the constructor:
> 
Or, rather, due to bad indentation of the original constructor, which I didn't notice.

> 
> The reviewer patch fixes this and also includes a little more documentation. Only my patch needs review. If it gets a positive review, the whole ticket is good to go.
This is more than a reviewer patch, so changing to author as well.  Positive review on the whole 'reviewer' patch.


---

Comment by mvngu created at 2010-05-08 21:50:53

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 21:50:53

Merged in this order:

 1. [trac_8805-functions-dir-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-functions-dir-doctest.patch)
 1. [trac_8805-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-reviewer.patch)
