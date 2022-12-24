# Issue 5971: fix dumb error message when modding out by 0: Mod(10,0)

archive/issues_005971.json:
```json
{
    "body": "Assignee: somebody\n\nWhen doing Mod(n,0), either there should be a useful error message, or one should get n back.  The following is no good at all -- one shouldn't get an AttributeError, which is surely due to a bug. \n\n\n```\nsage: a = Mod(10,0)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n    115     cdef IntegerMod_abstract x\n--> 116     x = IntegerMod(integer_mod_ring.IntegerModRing(m), n)\n    117     if parent is None:\n    118         return x\n\n/Users/wstein/build/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2730)()\n    132     cdef NativeIntStruct modulus\n    133     cdef Py_ssize_t res\n--> 134     modulus = parent._pyx_order\n    135     if modulus.table is not None:\n    136         if PY_TYPE_CHECK(value, sage.rings.integer.Integer) or PY_TYPE_CHECK(value, int) or PY_TYPE_CHECK(value, long):\n\nAttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_pyx_order'\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5971\n\n",
    "created_at": "2009-05-03T19:09:55Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "fix dumb error message when modding out by 0: Mod(10,0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5971",
    "user": "was"
}
```
Assignee: somebody

When doing Mod(n,0), either there should be a useful error message, or one should get n back.  The following is no good at all -- one shouldn't get an AttributeError, which is surely due to a bug. 


```
sage: a = Mod(10,0)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

    115     cdef IntegerMod_abstract x
--> 116     x = IntegerMod(integer_mod_ring.IntegerModRing(m), n)
    117     if parent is None:
    118         return x

/Users/wstein/build/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2730)()
    132     cdef NativeIntStruct modulus
    133     cdef Py_ssize_t res
--> 134     modulus = parent._pyx_order
    135     if modulus.table is not None:
    136         if PY_TYPE_CHECK(value, sage.rings.integer.Integer) or PY_TYPE_CHECK(value, int) or PY_TYPE_CHECK(value, long):

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_pyx_order'

```


Issue created by migration from https://trac.sagemath.org/ticket/5971





---

archive/issue_comments_047361.json:
```json
{
    "body": "Attachment [trac_5971.patch](tarball://root/attachments/some-uuid/ticket5971/trac_5971.patch) by mvngu created at 2009-06-26 03:57:35\n\nbased on Sage 4.1.alpha1",
    "created_at": "2009-06-26T03:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5971#issuecomment-47361",
    "user": "mvngu"
}
```

Attachment [trac_5971.patch](tarball://root/attachments/some-uuid/ticket5971/trac_5971.patch) by mvngu created at 2009-06-26 03:57:35

based on Sage 4.1.alpha1



---

archive/issue_comments_047362.json:
```json
{
    "body": "Applies fine to 4.1.alpha1 and does what it says.  I like the second doctest.  Unless something goes wrong with docbuild due to the #, all is well.",
    "created_at": "2009-06-26T14:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5971#issuecomment-47362",
    "user": "kcrisman"
}
```

Applies fine to 4.1.alpha1 and does what it says.  I like the second doctest.  Unless something goes wrong with docbuild due to the #, all is well.



---

archive/issue_comments_047363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T23:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5971#issuecomment-47363",
    "user": "boothby"
}
```

Resolution: fixed
