# Issue 6420: Maxima integration error with 1/x^3

archive/issues_006420.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: maxima integral\n\n\n```\nsage: integrate(1/x^3,x,1,infinity)\nValueError: Integral is divergent.\n```\n\n\nBut it's NOT!\n\nThe problem comes from Maxima. I could check four versions:\n\n\n```\nMaxima 5.13.0: it's ok\nMaxima 5.16.3: it gives wrong result, Sage 4.0.2 uses this\nMaxima 5.17.1: it gives wrong result\nMaxima 5.18.1: it's ok\n```\n\n\nAn example for wrong result:\n\n```\npetya@desktop:~/download/sage/sage-4.0.2-linux-Ubuntu_9.04-i686-Linux/local/bin$ ./maxima\nMaxima 5.16.3 http://maxima.sourceforge.net\nUsing Lisp ECL 9.4.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) integrate(1/x^3,x,1,inf);\n\nIntegral is divergent\n -- an error.  To debug this try debugmode(true);\n```\n\n\nWe would like to teach undergradute students with Sage, and this bug is quite annoying. It would be helpful, if someone could update Maxima in Sage.\n\n\n Thanks,\n  Peter\n\nIssue created by migration from https://trac.sagemath.org/ticket/6420\n\n",
    "created_at": "2009-06-26T07:33:08Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Maxima integration error with 1/x^3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```
Assignee: @mwhansen

Keywords: maxima integral


```
sage: integrate(1/x^3,x,1,infinity)
ValueError: Integral is divergent.
```


But it's NOT!

The problem comes from Maxima. I could check four versions:


```
Maxima 5.13.0: it's ok
Maxima 5.16.3: it gives wrong result, Sage 4.0.2 uses this
Maxima 5.17.1: it gives wrong result
Maxima 5.18.1: it's ok
```


An example for wrong result:

```
petya@desktop:~/download/sage/sage-4.0.2-linux-Ubuntu_9.04-i686-Linux/local/bin$ ./maxima
Maxima 5.16.3 http://maxima.sourceforge.net
Using Lisp ECL 9.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) integrate(1/x^3,x,1,inf);

Integral is divergent
 -- an error.  To debug this try debugmode(true);
```


We would like to teach undergradute students with Sage, and this bug is quite annoying. It would be helpful, if someone could update Maxima in Sage.


 Thanks,
  Peter

Issue created by migration from https://trac.sagemath.org/ticket/6420





---

archive/issue_comments_051449.json:
```json
{
    "body": "Changing assignee from @mwhansen to @aghitza.",
    "created_at": "2009-08-24T09:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51449",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @mwhansen to @aghitza.



---

archive/issue_comments_051450.json:
```json
{
    "body": "This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest here when #6699 gets merged.",
    "created_at": "2009-08-24T09:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51450",
    "user": "https://github.com/aghitza"
}
```

This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest here when #6699 gets merged.



---

archive/issue_comments_051451.json:
```json
{
    "body": "A temporary workaround is to use sympy:\n\n```\nsage: integrate(1/x**3,x,1,infinity,algorithm=\"sympy\")\n1/2\nsage: integrate(1/x**10,x,1,infinity,algorithm=\"sympy\")\n1/9\n```\n",
    "created_at": "2009-09-10T01:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51451",
    "user": "https://github.com/johnperry-math"
}
```

A temporary workaround is to use sympy:

```
sage: integrate(1/x**3,x,1,infinity,algorithm="sympy")
1/2
sage: integrate(1/x**10,x,1,infinity,algorithm="sympy")
1/9
```




---

archive/issue_comments_051452.json:
```json
{
    "body": "Patch is now up.",
    "created_at": "2009-09-29T14:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51452",
    "user": "https://github.com/kcrisman"
}
```

Patch is now up.



---

archive/issue_comments_051453.json:
```json
{
    "body": "Attachment [trac_6420-integrate-one-over-cube.patch](tarball://root/attachments/some-uuid/ticket6420/trac_6420-integrate-one-over-cube.patch) by @mwhansen created at 2009-10-05 04:57:06\n\nI updated the patch to remove some excess blank lines and to remove the \".. note::\" which didn't make sense.  Otherwise, your change is good by me.\n\nkcrisman, could you okay these changes and mark it as a positive review?",
    "created_at": "2009-10-05T04:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51453",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6420-integrate-one-over-cube.patch](tarball://root/attachments/some-uuid/ticket6420/trac_6420-integrate-one-over-cube.patch) by @mwhansen created at 2009-10-05 04:57:06

I updated the patch to remove some excess blank lines and to remove the ".. note::" which didn't make sense.  Otherwise, your change is good by me.

kcrisman, could you okay these changes and mark it as a positive review?



---

archive/issue_comments_051454.json:
```json
{
    "body": "Yup, those are fine.  I should have noticed that, actually, but was just fixing on the item in the ticket.  Strange that the comment was even still in there.\n\nIncidentally, I'm going to post on sage-devel about when to use ::, because just recently I remember a thread where it sounded like some doctests didn't happen if you didn't use it on a separate line (I encountered one recently in an __init__ method), so it would be good to have that on record and easily searchable.",
    "created_at": "2009-10-05T12:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51454",
    "user": "https://github.com/kcrisman"
}
```

Yup, those are fine.  I should have noticed that, actually, but was just fixing on the item in the ticket.  Strange that the comment was even still in there.

Incidentally, I'm going to post on sage-devel about when to use ::, because just recently I remember a thread where it sounded like some doctests didn't happen if you didn't use it on a separate line (I encountered one recently in an __init__ method), so it would be good to have that on record and easily searchable.



---

archive/issue_comments_051455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T07:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6420#issuecomment-51455",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006663.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-10-15T07:07:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6420",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6420#event-6663"
}
```
