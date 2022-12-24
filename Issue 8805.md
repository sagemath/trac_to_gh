# Issue 8805: Bring doctest for sage/functions folder to 100%

archive/issues_008805.json:
```json
{
    "body": "Assignee: mvngu\n\nBring doctest for sage/functions folder to 100%.  Specifically:\n\n```\nfunctions/orthogonal_polys.py: 91% (11 of 12)\nfunctions/other.py: 92% (26 of 28)\nfunctions/piecewise.py: 93% (43 of 46)\nfunctions/special.py: 69% (30 of 43)\nfunctions/transcendental.py: 86% (13 of 15)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8805\n\n",
    "created_at": "2010-04-28T15:24:51Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Bring doctest for sage/functions folder to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8805",
    "user": "kcrisman"
}
```
Assignee: mvngu

Bring doctest for sage/functions folder to 100%.  Specifically:

```
functions/orthogonal_polys.py: 91% (11 of 12)
functions/other.py: 92% (26 of 28)
functions/piecewise.py: 93% (43 of 46)
functions/special.py: 69% (30 of 43)
functions/transcendental.py: 86% (13 of 15)
```


Issue created by migration from https://trac.sagemath.org/ticket/8805





---

archive/issue_comments_080792.json:
```json
{
    "body": "Based on 4.4",
    "created_at": "2010-04-30T11:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80792",
    "user": "kcrisman"
}
```

Based on 4.4



---

archive/issue_comments_080793.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T11:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80793",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080794.json:
```json
{
    "body": "Attachment [trac_8805-functions-dir-doctest.patch](tarball://root/attachments/some-uuid/ticket8805/trac_8805-functions-dir-doctest.patch) by kcrisman created at 2010-04-30 11:24:17\n\nThis only adds doctests, and does not address any TODOs in the files.",
    "created_at": "2010-04-30T11:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80794",
    "user": "kcrisman"
}
```

Attachment [trac_8805-functions-dir-doctest.patch](tarball://root/attachments/some-uuid/ticket8805/trac_8805-functions-dir-doctest.patch) by kcrisman created at 2010-04-30 11:24:17

This only adds doctests, and does not address any TODOs in the files.



---

archive/issue_comments_080795.json:
```json
{
    "body": "Attachment [trac_8805-reviewer.patch](tarball://root/attachments/some-uuid/ticket8805/trac_8805-reviewer.patch) by mvngu created at 2010-05-03 01:34:42\n\nApplying the patch [trac_8805-functions-dir-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-functions-dir-doctest.patch) and rebuilding the Sage library resulted in the following error:\n\n\n```sh\n[mvngu@sage sage-4.4.1.rc0-8805-functions]$ ./sage -b\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 1.69277191162e-05 seconds\nFinished compiling Cython code (time = 0.367266178131 seconds)\nrunning install\nrunning build\nrunning build_py\ncopying sage/functions/transcendental.py -> build/lib.linux-x86_64-2.6/sage/functions\ncopying sage/functions/special.py -> build/lib.linux-x86_64-2.6/sage/functions\ncopying sage/functions/piecewise.py -> build/lib.linux-x86_64-2.6/sage/functions\ncopying sage/functions/other.py -> build/lib.linux-x86_64-2.6/sage/functions\ncopying sage/functions/orthogonal_polys.py -> build/lib.linux-x86_64-2.6/sage/functions\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.0169429779053 seconds.\nrunning install_lib\ncopying build/lib.linux-x86_64-2.6/sage/functions/orthogonal_polys.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions\ncopying build/lib.linux-x86_64-2.6/sage/functions/other.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions\ncopying build/lib.linux-x86_64-2.6/sage/functions/piecewise.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions\ncopying build/lib.linux-x86_64-2.6/sage/functions/special.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions\ncopying build/lib.linux-x86_64-2.6/sage/functions/transcendental.py -> /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions\nbyte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/orthogonal_polys.py to orthogonal_polys.pyc\nbyte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/other.py to other.pyc\nbyte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/piecewise.py to piecewise.pyc\nbyte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/special.py to special.pyc\nbyte-compiling /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/transcendental.py to transcendental.pyc\nSorry: IndentationError: ('unindent does not match any outer indentation level', ('/dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage/functions/transcendental.py', 491, 25, '      self._cur_prec = 0\\n'))\nrunning install_egg_info\nRemoving /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /dev/shm/mvngu/sandbox/sage-4.4.1.rc0-8805-functions/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n\nreal\t0m1.411s\nuser\t0m1.120s\nsys\t0m0.290s\n```\n\n\nThis is due to bad indentation of the docstring in the constructor:\n\n\n```python\n    def __init__(self):\n        \"\"\"                                                                     \n        TESTS::                                                                 \n                                                                                \n            sage: dickman_rho(x)                                                \n            dickman_rho(x)                                                      \n            sage: dickman_rho(3)                                                \n            0.0486083882911316                                                  \n            sage: dickman_rho(pi)                                               \n            0.0359690758968463                                                  \n        \"\"\"\n      self._cur_prec = 0\n      BuiltinFunction.__init__(self, \"dickman_rho\", 1)\n```\n\n\nThe reviewer patch fixes this and also includes a little more documentation. Only my patch needs review. If it gets a positive review, the whole ticket is good to go.",
    "created_at": "2010-05-03T01:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80795",
    "user": "mvngu"
}
```

Attachment [trac_8805-reviewer.patch](tarball://root/attachments/some-uuid/ticket8805/trac_8805-reviewer.patch) by mvngu created at 2010-05-03 01:34:42

Applying the patch [trac_8805-functions-dir-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-functions-dir-doctest.patch) and rebuilding the Sage library resulted in the following error:


```sh
[mvngu@sage sage-4.4.1.rc0-8805-functions]$ ./sage -b
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

archive/issue_comments_080796.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-03T14:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80796",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080797.json:
```json
{
    "body": "Replying to [comment:2 mvngu]:\n\n> \n> This is due to bad indentation of the docstring in the constructor:\n> \nOr, rather, due to bad indentation of the original constructor, which I didn't notice.\n\n> \n> The reviewer patch fixes this and also includes a little more documentation. Only my patch needs review. If it gets a positive review, the whole ticket is good to go.\nThis is more than a reviewer patch, so changing to author as well.  Positive review on the whole 'reviewer' patch.",
    "created_at": "2010-05-03T14:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80797",
    "user": "kcrisman"
}
```

Replying to [comment:2 mvngu]:

> 
> This is due to bad indentation of the docstring in the constructor:
> 
Or, rather, due to bad indentation of the original constructor, which I didn't notice.

> 
> The reviewer patch fixes this and also includes a little more documentation. Only my patch needs review. If it gets a positive review, the whole ticket is good to go.
This is more than a reviewer patch, so changing to author as well.  Positive review on the whole 'reviewer' patch.



---

archive/issue_comments_080798.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80798",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_080799.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8805-functions-dir-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-functions-dir-doctest.patch)\n2. [trac_8805-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-reviewer.patch)",
    "created_at": "2010-05-08T21:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8805#issuecomment-80799",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8805-functions-dir-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-functions-dir-doctest.patch)
2. [trac_8805-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8805/trac_8805-reviewer.patch)
