# Issue 2109: the maxima interface doesn't recognize a syntax error (and then hangs)

archive/issues_002109.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: maxima.eval('sage0: x == x;')\ndisplay2d : false; \n(%o2) false\n\n0; \n(%o4) 0\n```\n\n\nIt hangs there.  If doing the same thing in Maxima, we get the following results:\n\n\n```\n(%i1) sage0: x==x;\nIncorrect syntax: = is not a prefix operator\nsage0: x==\n        ^\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2109\n\n",
    "created_at": "2008-02-08T10:44:29Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "the maxima interface doesn't recognize a syntax error (and then hangs)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2109",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein


```
sage: maxima.eval('sage0: x == x;')
display2d : false; 
(%o2) false

0; 
(%o4) 0
```


It hangs there.  If doing the same thing in Maxima, we get the following results:


```
(%i1) sage0: x==x;
Incorrect syntax: = is not a prefix operator
sage0: x==
        ^

```


Issue created by migration from https://trac.sagemath.org/ticket/2109





---

archive/issue_comments_013723.json:
```json
{
    "body": "Here is what happens in sage-4.1.1:\n\n\n```\nsage: maxima.eval('sage0: x == x;')\n'x'\n```\n",
    "created_at": "2009-08-24T09:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13723",
    "user": "https://github.com/aghitza"
}
```

Here is what happens in sage-4.1.1:


```
sage: maxima.eval('sage0: x == x;')
'x'
```




---

archive/issue_comments_013724.json:
```json
{
    "body": "So at least it doesn't hang anymore.  I will change the summary.",
    "created_at": "2009-12-17T21:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13724",
    "user": "https://github.com/kcrisman"
}
```

So at least it doesn't hang anymore.  I will change the summary.



---

archive/issue_comments_013725.json:
```json
{
    "body": "Attachment [trac_2109.patch](tarball://root/attachments/some-uuid/ticket2109/trac_2109.patch) by @mwhansen created at 2010-01-17 04:16:27",
    "created_at": "2010-01-17T04:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13725",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_2109.patch](tarball://root/attachments/some-uuid/ticket2109/trac_2109.patch) by @mwhansen created at 2010-01-17 04:16:27



---

archive/issue_comments_013726.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T04:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13726",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013727.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T15:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13727",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013728.json:
```json
{
    "body": "Passes relevant tests, catches several different types of incorrect input errors, and helped me learn a little more about pexpect.  Positive review, and thanks! \n\nUnfortunately, it doesn't catch when someone does something like this, but I'm not sure this is really an \"error\", as it's intended that Maxima can handle this sort of thing... yet it could easily come as a result of an error by the user.  Oh well.\n\n```\nintegrate(f,\nx,1,\n2)\n```\n",
    "created_at": "2010-01-18T15:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13728",
    "user": "https://github.com/kcrisman"
}
```

Passes relevant tests, catches several different types of incorrect input errors, and helped me learn a little more about pexpect.  Positive review, and thanks! 

Unfortunately, it doesn't catch when someone does something like this, but I'm not sure this is really an "error", as it's intended that Maxima can handle this sort of thing... yet it could easily come as a result of an error by the user.  Oh well.

```
integrate(f,
x,1,
2)
```




---

archive/issue_comments_013729.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2109#issuecomment-13729",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
