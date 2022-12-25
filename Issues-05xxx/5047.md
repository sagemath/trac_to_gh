# Issue 5047: [with patch, positive review] comparing complex i raises error

archive/issues_005047.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: cmp(i,0)\n\nTypeError                                 Traceback (most recent call last)\n/home/burcin/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/functions/functions.pyc in __cmp__(self, right)\n    267             return 0\n    268         R = RealField()\n--> 269         c = cmp(R(self), R(right))\n    270         if c: return c\n    271         try:\n\n...\n/home/burcin/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/functions/constants.pyc in _mpfr_(self, R)\n    865             TypeError\n    866         \"\"\"\n--> 867         raise TypeError\n    868 \n    869     def _real_rqdf_(self, R):\n\nTypeError: \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5047\n\n",
    "closed_at": "2009-01-24T16:28:25Z",
    "created_at": "2009-01-21T07:57:23Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] comparing complex i raises error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5047",
    "user": "https://github.com/burcin"
}
```
Assignee: somebody

```
sage: cmp(i,0)

TypeError                                 Traceback (most recent call last)
/home/burcin/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/functions/functions.pyc in __cmp__(self, right)
    267             return 0
    268         R = RealField()
--> 269         c = cmp(R(self), R(right))
    270         if c: return c
    271         try:

...
/home/burcin/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/functions/constants.pyc in _mpfr_(self, R)
    865             TypeError
    866         """
--> 867         raise TypeError
    868 
    869     def _real_rqdf_(self, R):

TypeError: 
```

Issue created by migration from https://trac.sagemath.org/ticket/5047





---

archive/issue_comments_038363.json:
```json
{
    "body": "I believe this ticket is close to being invalid, because Sage is nearly consistent with Python.\n\nIn Python, one gets\n\n```\n>>> cmp(1j,0)\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\nTypeError: no ordering relation is defined for complex numbers\n```\n\nOnly I would say that the error message in Sage could be clearer. So, I suggest to catch the error and reraise a TypeError with an appropriate error message.",
    "created_at": "2009-01-23T20:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38363",
    "user": "https://github.com/simon-king-jena"
}
```

I believe this ticket is close to being invalid, because Sage is nearly consistent with Python.

In Python, one gets

```
>>> cmp(1j,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: no ordering relation is defined for complex numbers
```

Only I would say that the error message in Sage could be clearer. So, I suggest to catch the error and reraise a TypeError with an appropriate error message.



---

archive/issue_comments_038364.json:
```json
{
    "body": "raise a proper error message when using cmp on non-real constants",
    "created_at": "2009-01-23T20:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38364",
    "user": "https://github.com/simon-king-jena"
}
```

raise a proper error message when using cmp on non-real constants



---

archive/issue_comments_038365.json:
```json
{
    "body": "Attachment [cmp_imaginary.patch](tarball://root/attachments/some-uuid/ticket5047/cmp_imaginary.patch) by @simon-king-jena created at 2009-01-23 20:27:37\n\nReplying to [comment:1 SimonKing]:\n> In Python, one gets\n> \n> ```\n> >>> cmp(1j,0)\n> Traceback (most recent call last):\n>   File \"<stdin>\", line 1, in <module>\n> TypeError: no ordering relation is defined for complex numbers\n> ```\n\n\nWith the patch, one gets\n\n```\nsage: cmp(i,0)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/.sage/temp/mpc739/25379/_home_king__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/home/king/SAGE/devel/sage-3.2.1/local/lib/python2.5/site-packages/sage/functions/functions.pyc in __cmp__(self, right)\n    270             c = cmp(R(self), R(right))\n    271         except TypeError:\n--> 272             raise TypeError, \"these objects are not comparable\"\n    273         if c: return c\n    274         try:\n\nTypeError: these objects are not comparable\n```\nwhich, I believe, is consistent with python.\n\nOther comparisons still work:\n\n```\nsage: cmp(i^2,0)\n-1\nsage: cmp(e,0)\n1\n```",
    "created_at": "2009-01-23T20:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38365",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [cmp_imaginary.patch](tarball://root/attachments/some-uuid/ticket5047/cmp_imaginary.patch) by @simon-king-jena created at 2009-01-23 20:27:37

Replying to [comment:1 SimonKing]:
> In Python, one gets
> 
> ```
> >>> cmp(1j,0)
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: no ordering relation is defined for complex numbers
> ```


With the patch, one gets

```
sage: cmp(i,0)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/.sage/temp/mpc739/25379/_home_king__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/king/SAGE/devel/sage-3.2.1/local/lib/python2.5/site-packages/sage/functions/functions.pyc in __cmp__(self, right)
    270             c = cmp(R(self), R(right))
    271         except TypeError:
--> 272             raise TypeError, "these objects are not comparable"
    273         if c: return c
    274         try:

TypeError: these objects are not comparable
```
which, I believe, is consistent with python.

Other comparisons still work:

```
sage: cmp(i^2,0)
-1
sage: cmp(e,0)
1
```



---

archive/issue_comments_038366.json:
```json
{
    "body": "I ran into this when testing new printing code in pynac. ATM, pynac uses the sign function, which is defined to be cmp(x, 0), to determine if it should print a minus sign. Thus, we have the following:\n\n```\nsage: var('x',ns=1)\nsage: i*x\n<boom>\n```\n\nI somehow thought that the cmp function was not supposed to raise exceptions, but googling shortly didn't turn up any evidence to support this argument.\n\nI would be ok to live with this fact, and try to figure out a better way to handle the sign function, or printing in pynac.\n\nBTW, the sign function is also mentioned here: #777\n\n\nI give the attached patch a positive review, provided that doctests are added to test for the new error message.",
    "created_at": "2009-01-23T21:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38366",
    "user": "https://github.com/burcin"
}
```

I ran into this when testing new printing code in pynac. ATM, pynac uses the sign function, which is defined to be cmp(x, 0), to determine if it should print a minus sign. Thus, we have the following:

```
sage: var('x',ns=1)
sage: i*x
<boom>
```

I somehow thought that the cmp function was not supposed to raise exceptions, but googling shortly didn't turn up any evidence to support this argument.

I would be ok to live with this fact, and try to figure out a better way to handle the sign function, or printing in pynac.

BTW, the sign function is also mentioned here: #777


I give the attached patch a positive review, provided that doctests are added to test for the new error message.



---

archive/issue_comments_038367.json:
```json
{
    "body": "Attachment [cmp_doc.patch](tarball://root/attachments/some-uuid/ticket5047/cmp_doc.patch) by @simon-king-jena created at 2009-01-23 22:34:18",
    "created_at": "2009-01-23T22:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38367",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [cmp_doc.patch](tarball://root/attachments/some-uuid/ticket5047/cmp_doc.patch) by @simon-king-jena created at 2009-01-23 22:34:18



---

archive/issue_comments_038368.json:
```json
{
    "body": "The second patch `cmp_doc.patch` (to be applied after the first patch) adds more documentation.\n\nReplying to [comment:3 burcin]:\n> I ran into this when testing new printing code in pynac. ATM, pynac uses the sign function, which is defined to be cmp(x, 0), to determine if it should print a minus sign. Thus, we have the following:\n> \n> \n> ```\n> sage: var('x',ns=1)\n> sage: i*x\n> <boom>\n> ```\n\n\nOk, but I think there should be a different approach for determining the sign when printing an imaginary number. \nHowever, personally I believe that `sign(I)` should raise an error.\n\n> I somehow thought that the cmp function was not supposed to raise exceptions, but googling shortly didn't turn up any evidence to support this argument.\n\n\n... and, as I mentioned above, `cmp` does raise an exception in Python.\n\n> BTW, the sign function is also mentioned here: #777\n\n\nThe `sign` function defined in #777 would simply return 0 on non-real constants, because it tests `bool(x > 0)`. Indeed, we have\n\n```\nsage: bool(I > 0)\nFalse\nsage: bool(I < 0)\nFalse\n```\nso, at least it does not go boom (which it *should*, though!).",
    "created_at": "2009-01-23T22:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38368",
    "user": "https://github.com/simon-king-jena"
}
```

The second patch `cmp_doc.patch` (to be applied after the first patch) adds more documentation.

Replying to [comment:3 burcin]:
> I ran into this when testing new printing code in pynac. ATM, pynac uses the sign function, which is defined to be cmp(x, 0), to determine if it should print a minus sign. Thus, we have the following:
> 
> 
> ```
> sage: var('x',ns=1)
> sage: i*x
> <boom>
> ```


Ok, but I think there should be a different approach for determining the sign when printing an imaginary number. 
However, personally I believe that `sign(I)` should raise an error.

> I somehow thought that the cmp function was not supposed to raise exceptions, but googling shortly didn't turn up any evidence to support this argument.


... and, as I mentioned above, `cmp` does raise an exception in Python.

> BTW, the sign function is also mentioned here: #777


The `sign` function defined in #777 would simply return 0 on non-real constants, because it tests `bool(x > 0)`. Indeed, we have

```
sage: bool(I > 0)
False
sage: bool(I < 0)
False
```
so, at least it does not go boom (which it *should*, though!).



---

archive/issue_comments_038369.json:
```json
{
    "body": "Positive review, both patches should be applied.",
    "created_at": "2009-01-23T23:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38369",
    "user": "https://github.com/burcin"
}
```

Positive review, both patches should be applied.



---

archive/issue_comments_038370.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T16:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38370",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_events_011639.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T16:28:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5047#event-11639"
}
```



---

archive/issue_comments_038371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T16:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5047#issuecomment-38371",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
