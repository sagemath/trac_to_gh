# Issue 4571: merge sage's numpy.pxd with the cython numpy.pxd

archive/issues_004571.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  robertwb dagss\n\n\n```\n[15:53] <robertwb> yep, we should merge them\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4571\n\n",
    "created_at": "2008-11-20T21:56:56Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "merge sage's numpy.pxd with the cython numpy.pxd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4571",
    "user": "jason"
}
```
Assignee: mabshoff

CC:  robertwb dagss


```
[15:53] <robertwb> yep, we should merge them
```




Issue created by migration from https://trac.sagemath.org/ticket/4571





---

archive/issue_comments_034240.json:
```json
{
    "body": "See http://trac.cython.org/cython_trac/ticket/339",
    "created_at": "2009-06-28T09:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34240",
    "user": "robertwb"
}
```

See http://trac.cython.org/cython_trac/ticket/339



---

archive/issue_comments_034241.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-28T09:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34241",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_034242.json:
```json
{
    "body": "Preliminary patch, need a new Cython spkg for it to work all the way.",
    "created_at": "2009-06-28T09:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34242",
    "user": "robertwb"
}
```

Preliminary patch, need a new Cython spkg for it to work all the way.



---

archive/issue_comments_034243.json:
```json
{
    "body": "Attachment\n\nHere are some more fixes. With this, and the latest state of the\n\nhttp://hg.cython.org/cython\n\nrepo, all the relevant tests seem to pass. I do get two failures (due to Cython upgrade? something else?), see test.log in\n\n/home/dagss/sage-4.0.2-sage.math.washington.edu-x86_64-Linux\n\nOnce this works let's tag http://hg.cython.org/cython as 0.11.2.1 for #6438?",
    "created_at": "2009-07-07T15:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34243",
    "user": "dagss"
}
```

Attachment

Here are some more fixes. With this, and the latest state of the

http://hg.cython.org/cython

repo, all the relevant tests seem to pass. I do get two failures (due to Cython upgrade? something else?), see test.log in

/home/dagss/sage-4.0.2-sage.math.washington.edu-x86_64-Linux

Once this works let's tag http://hg.cython.org/cython as 0.11.2.1 for #6438?



---

archive/issue_comments_034244.json:
```json
{
    "body": "Note (re: discussion on Cython ML) that shape in numpy.pxd is still a field, long story (well, it is performance critical), and I shouldn't change it.",
    "created_at": "2009-07-07T15:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34244",
    "user": "dagss"
}
```

Note (re: discussion on Cython ML) that shape in numpy.pxd is still a field, long story (well, it is performance critical), and I shouldn't change it.



---

archive/issue_comments_034245.json:
```json
{
    "body": "Another quick comment: With this, full Cython/NumPy functionality is available from the notebook and works well.",
    "created_at": "2009-07-07T16:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34245",
    "user": "dagss"
}
```

Another quick comment: With this, full Cython/NumPy functionality is available from the notebook and works well.



---

archive/issue_comments_034246.json:
```json
{
    "body": "Those errors seem completely unrelated, I'll see if I get them too. Other than that, it looks really good. \n\nI've used Cython + NumPy from the notebook before, as long as you weren't in sage.ext then \"cimport numpy\" worked as expected (though there was a point where it didn't).",
    "created_at": "2009-07-09T08:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34246",
    "user": "robertwb"
}
```

Those errors seem completely unrelated, I'll see if I get them too. Other than that, it looks really good. 

I've used Cython + NumPy from the notebook before, as long as you weren't in sage.ext then "cimport numpy" worked as expected (though there was a point where it didn't).



---

archive/issue_comments_034247.json:
```json
{
    "body": "Hmm... I also got \n\n\n```\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/rings/polynomial/polynomial_template.pxi # 1 doctests failed\n        sage -t -long devel/sage-main/sage/interfaces/sage0.py # 1 doctests failed\n\n```\n",
    "created_at": "2009-07-21T20:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34247",
    "user": "robertwb"
}
```

Hmm... I also got 


```
The following tests failed:

        sage -t -long devel/sage-main/sage/rings/polynomial/polynomial_template.pxi # 1 doctests failed
        sage -t -long devel/sage-main/sage/interfaces/sage0.py # 1 doctests failed

```




---

archive/issue_comments_034248.json:
```json
{
    "body": "Changing component from build to numerical.",
    "created_at": "2009-07-22T14:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34248",
    "user": "robertwb"
}
```

Changing component from build to numerical.



---

archive/issue_comments_034249.json:
```json
{
    "body": "Looks good. The single doctest failure was minor, fixed in #6438.",
    "created_at": "2009-07-22T14:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34249",
    "user": "robertwb"
}
```

Looks good. The single doctest failure was minor, fixed in #6438.



---

archive/issue_comments_034250.json:
```json
{
    "body": "Replying to [comment:4 dagss]:\n> Here are some more fixes. With this, and the latest state of the\n<SNIP>\n\n\nThe patch `4571-more-fixes.patch` doesn't contain a commit message and your username is not on the patch. Your username should follow the format:\n\n```\nFull Name <email@somewhere.com>\n```\n\nThe username makes it easy to identify the patch, when it is committed, as your contribution.",
    "created_at": "2009-07-22T16:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34250",
    "user": "mvngu"
}
```

Replying to [comment:4 dagss]:
> Here are some more fixes. With this, and the latest state of the
<SNIP>


The patch `4571-more-fixes.patch` doesn't contain a commit message and your username is not on the patch. Your username should follow the format:

```
Full Name <email@somewhere.com>
```

The username makes it easy to identify the patch, when it is committed, as your contribution.



---

archive/issue_comments_034251.json:
```json
{
    "body": "With both patches applied in the following order:\n1. `4571-numpy-pxd.patch`\n2. `4571-more-fixes.patch`\nI see the following build failure:\n\n```\n[mvngu@sage sage-4.1.1.alpha0]$ ./sage -br main\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nBuilding modified file sage/finance/time_series.pyx.\nBuilding modified file sage/matrix/change_ring.pyx.\nBuilding modified file sage/matrix/matrix_complex_double_dense.pyx.\nBuilding modified file sage/matrix/matrix_double_dense.pyx.\nBuilding modified file sage/matrix/matrix_real_double_dense.pyx.\nBuilding modified file sage/modules/vector_complex_double_dense.pyx.\nBuilding modified file sage/modules/vector_double_dense.pyx.\nBuilding modified file sage/modules/vector_real_double_dense.pyx.\nBuilding sage/rings/polynomial/real_roots.pyx because it depends on sage/modules/vector_double_dense.pxd.\nBuilding sage/stats/hmm/chmm.pyx because it depends on sage/matrix/matrix_double_dense.pxd.\nBuilding sage/stats/hmm/hmm.pyx because it depends on sage/matrix/matrix_double_dense.pxd.\npython `which cython` --embed-positions --incref-local-binop -I/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main -o sage/finance/time_series.c sage/finance/time_series.pyx\nwarning: /scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1722:24: cdef variable 'j' declared after it is used\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            [20.0000, -3.0000, 4.5000, -2.0000]\n        \"\"\"\n        cnumpy.import_array() #This must be called before using the numpy C/api or you will get segfault\n        cdef cnumpy.npy_intp dims[1]\n        dims[0] = self._length\n        cdef cnumpy.ndarray n = cnumpy.PyArray_SimpleNewFromData(1, dims, cnumpy.NPY_DOUBLE, self._values)\n                                                                       ^\n------------------------------------------------------------\n\n/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1862:72: Cannot convert 'numpy.npy_intp [1]' to Python object\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            [20.0000, -3.0000, 4.5000, -2.0000]\n        \"\"\"\n        cnumpy.import_array() #This must be called before using the numpy C/api or you will get segfault\n        cdef cnumpy.npy_intp dims[1]\n        dims[0] = self._length\n        cdef cnumpy.ndarray n = cnumpy.PyArray_SimpleNewFromData(1, dims, cnumpy.NPY_DOUBLE, self._values)\n                                                                                                ^\n------------------------------------------------------------\n\n/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1862:97: Cannot convert 'double *' to Python object\nError running command, failed with status 256.\nsage: There was an error installing modified sage library code.\n```\n",
    "created_at": "2009-07-23T02:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34251",
    "user": "mvngu"
}
```

With both patches applied in the following order:
1. `4571-numpy-pxd.patch`
2. `4571-more-fixes.patch`
I see the following build failure:

```
[mvngu@sage sage-4.1.1.alpha0]$ ./sage -br main

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/finance/time_series.pyx.
Building modified file sage/matrix/change_ring.pyx.
Building modified file sage/matrix/matrix_complex_double_dense.pyx.
Building modified file sage/matrix/matrix_double_dense.pyx.
Building modified file sage/matrix/matrix_real_double_dense.pyx.
Building modified file sage/modules/vector_complex_double_dense.pyx.
Building modified file sage/modules/vector_double_dense.pyx.
Building modified file sage/modules/vector_real_double_dense.pyx.
Building sage/rings/polynomial/real_roots.pyx because it depends on sage/modules/vector_double_dense.pxd.
Building sage/stats/hmm/chmm.pyx because it depends on sage/matrix/matrix_double_dense.pxd.
Building sage/stats/hmm/hmm.pyx because it depends on sage/matrix/matrix_double_dense.pxd.
python `which cython` --embed-positions --incref-local-binop -I/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main -o sage/finance/time_series.c sage/finance/time_series.pyx
warning: /scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1722:24: cdef variable 'j' declared after it is used

Error converting Pyrex file to C:
------------------------------------------------------------
...
            [20.0000, -3.0000, 4.5000, -2.0000]
        """
        cnumpy.import_array() #This must be called before using the numpy C/api or you will get segfault
        cdef cnumpy.npy_intp dims[1]
        dims[0] = self._length
        cdef cnumpy.ndarray n = cnumpy.PyArray_SimpleNewFromData(1, dims, cnumpy.NPY_DOUBLE, self._values)
                                                                       ^
------------------------------------------------------------

/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1862:72: Cannot convert 'numpy.npy_intp [1]' to Python object

Error converting Pyrex file to C:
------------------------------------------------------------
...
            [20.0000, -3.0000, 4.5000, -2.0000]
        """
        cnumpy.import_array() #This must be called before using the numpy C/api or you will get segfault
        cdef cnumpy.npy_intp dims[1]
        dims[0] = self._length
        cdef cnumpy.ndarray n = cnumpy.PyArray_SimpleNewFromData(1, dims, cnumpy.NPY_DOUBLE, self._values)
                                                                                                ^
------------------------------------------------------------

/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1862:97: Cannot convert 'double *' to Python object
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.
```




---

archive/issue_comments_034252.json:
```json
{
    "body": "Looks like it'll have to be rebased, worked fine on vanilla 4.1. Where's the .tar on sage.math?",
    "created_at": "2009-07-23T08:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34252",
    "user": "robertwb"
}
```

Looks like it'll have to be rebased, worked fine on vanilla 4.1. Where's the .tar on sage.math?



---

archive/issue_comments_034253.json:
```json
{
    "body": "Replying to [comment:13 robertwb]:\n> Looks like it'll have to be rebased, worked fine on vanilla 4.1. Where's the .tar on sage.math? \nSource and binary versions are up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha0.tar\n\n\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux.tar.gz",
    "created_at": "2009-07-23T08:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34253",
    "user": "mvngu"
}
```

Replying to [comment:13 robertwb]:
> Looks like it'll have to be rebased, worked fine on vanilla 4.1. Where's the .tar on sage.math? 
Source and binary versions are up at

http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha0.tar


http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux.tar.gz



---

archive/issue_comments_034254.json:
```json
{
    "body": "Works fine form me. sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux.tar.gz + #6438 + #4571. Are you sure applied the latest Cython spkg first? 4.1.1.alpha0 doesn't seem to have it.",
    "created_at": "2009-07-25T12:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34254",
    "user": "robertwb"
}
```

Works fine form me. sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux.tar.gz + #6438 + #4571. Are you sure applied the latest Cython spkg first? 4.1.1.alpha0 doesn't seem to have it.



---

archive/issue_comments_034255.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-25T15:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34255",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_034256.json:
```json
{
    "body": "dagss: The patch `4571-more-fixes.patch` doesn't contain your username. I'm committing it in your name. Merged in this order\n1. the SPKG at #6438\n2. `4571-numpy-pxd.patch`\n3. `4571-more-fixes.patch`",
    "created_at": "2009-07-25T15:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4571#issuecomment-34256",
    "user": "mvngu"
}
```

dagss: The patch `4571-more-fixes.patch` doesn't contain your username. I'm committing it in your name. Merged in this order
1. the SPKG at #6438
2. `4571-numpy-pxd.patch`
3. `4571-more-fixes.patch`
