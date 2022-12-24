# Issue 6223: Remove ext/python_*.pxi

archive/issues_006223.json:
```json
{
    "body": "Assignee: tbd\n\nCython ships them all now, no need to have them here.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6223\n\n",
    "created_at": "2009-06-05T09:41:06Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.10",
    "title": "Remove ext/python_*.pxi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6223",
    "user": "robertwb"
}
```
Assignee: tbd

Cython ships them all now, no need to have them here.

Issue created by migration from https://trac.sagemath.org/ticket/6223





---

archive/issue_comments_049682.json:
```json
{
    "body": "Removing `include \"../ext/python_list.pxi\"` from `sage/structure/coerce_dict.pyx` gives trouble:\n\n\n```\npython `which cython` --embed-positions --directive cdivision=True,autotestdict=False -I/usr/local/src/sage-4.6.alpha3/devel/sage-test -o sage/structure/coerce_dict.c sage/structure/coerce_dict.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef get(self, k1, k2, k3):\n        cdef Py_ssize_t h = (<Py_ssize_t><void *>k1 + 13*<Py_ssize_t><void *>k2 ^ 503*<Py_ssize_t><void *>k3)\n        if h < 0: h = -h\n        cdef Py_ssize_t i\n        bucket = <object>PyList_GET_ITEM(self.buckets, h % PyList_GET_SIZE(self.buckets))\n                                       ^\n------------------------------------------------------------\n\n/usr/local/src/sage-4.6.alpha3/devel/sage-test/sage/structure/coerce_dict.pyx:225:40: undeclared name not builtin: PyList_GET_ITEM\n```\n",
    "created_at": "2010-10-12T13:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49682",
    "user": "jdemeyer"
}
```

Removing `include "../ext/python_list.pxi"` from `sage/structure/coerce_dict.pyx` gives trouble:


```
python `which cython` --embed-positions --directive cdivision=True,autotestdict=False -I/usr/local/src/sage-4.6.alpha3/devel/sage-test -o sage/structure/coerce_dict.c sage/structure/coerce_dict.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef get(self, k1, k2, k3):
        cdef Py_ssize_t h = (<Py_ssize_t><void *>k1 + 13*<Py_ssize_t><void *>k2 ^ 503*<Py_ssize_t><void *>k3)
        if h < 0: h = -h
        cdef Py_ssize_t i
        bucket = <object>PyList_GET_ITEM(self.buckets, h % PyList_GET_SIZE(self.buckets))
                                       ^
------------------------------------------------------------

/usr/local/src/sage-4.6.alpha3/devel/sage-test/sage/structure/coerce_dict.pyx:225:40: undeclared name not builtin: PyList_GET_ITEM
```




---

archive/issue_comments_049683.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-10-12T13:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49683",
    "user": "jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_049684.json:
```json
{
    "body": "Attachment [6223_ext_python_part1.patch](tarball://root/attachments/some-uuid/ticket6223/6223_ext_python_part1.patch) by jdemeyer created at 2013-04-12 21:52:24",
    "created_at": "2013-04-12T21:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49684",
    "user": "jdemeyer"
}
```

Attachment [6223_ext_python_part1.patch](tarball://root/attachments/some-uuid/ticket6223/6223_ext_python_part1.patch) by jdemeyer created at 2013-04-12 21:52:24



---

archive/issue_comments_049685.json:
```json
{
    "body": "Attachment [6223_remove_pxi.patch](tarball://root/attachments/some-uuid/ticket6223/6223_remove_pxi.patch) by jdemeyer created at 2013-04-13 15:47:35",
    "created_at": "2013-04-13T15:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49685",
    "user": "jdemeyer"
}
```

Attachment [6223_remove_pxi.patch](tarball://root/attachments/some-uuid/ticket6223/6223_remove_pxi.patch) by jdemeyer created at 2013-04-13 15:47:35



---

archive/issue_comments_049686.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-04-13T15:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49686",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_049687.json:
```json
{
    "body": "Attachment [6223_ext_python_manual.patch](tarball://root/attachments/some-uuid/ticket6223/6223_ext_python_manual.patch) by jdemeyer created at 2013-04-15 11:48:13",
    "created_at": "2013-04-15T11:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49687",
    "user": "jdemeyer"
}
```

Attachment [6223_ext_python_manual.patch](tarball://root/attachments/some-uuid/ticket6223/6223_ext_python_manual.patch) by jdemeyer created at 2013-04-15 11:48:13



---

archive/issue_comments_049688.json:
```json
{
    "body": "Great!",
    "created_at": "2013-04-18T17:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49688",
    "user": "vbraun"
}
```

Great!



---

archive/issue_comments_049689.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-18T17:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49689",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049690.json:
```json
{
    "body": "Thanks!",
    "created_at": "2013-04-19T08:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49690",
    "user": "jdemeyer"
}
```

Thanks!



---

archive/issue_comments_049691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-04-23T09:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6223#issuecomment-49691",
    "user": "jdemeyer"
}
```

Resolution: fixed
