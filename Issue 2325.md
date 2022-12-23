# Issue 2325: segfault in p-adic extension() method

archive/issues_002325.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan\n\nKeywords: p-adic extension crash segfault ntl\n\n\n```\nsage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]\nsage: L = Qp(19).extension(F, names='a')\nfatal error:\n   internal error: can't grow this _ntl_gbigint\nexit...\n/Users/ncalexan/sage-2.10.2.alpha0/local/bin/sage-sage: line 220: 21707 Abort trap              sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n\nProcess SAGE exited abnormally with code 134\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2325\n\n",
    "created_at": "2008-02-26T23:05:17Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "segfault in p-adic extension() method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2325",
    "user": "ncalexan"
}
```
Assignee: was

CC:  ncalexan

Keywords: p-adic extension crash segfault ntl


```
sage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]
sage: L = Qp(19).extension(F, names='a')
fatal error:
   internal error: can't grow this _ntl_gbigint
exit...
/Users/ncalexan/sage-2.10.2.alpha0/local/bin/sage-sage: line 220: 21707 Abort trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"

Process SAGE exited abnormally with code 134
```


Issue created by migration from https://trac.sagemath.org/ticket/2325





---

archive/issue_comments_015466.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-15T02:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15466",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_015467.json:
```json
{
    "body": "Nick,\n\nI cannot reproduce this with 2.10.3 on sage.math. Can you verify on your 2.10.3 build that this is still a problem?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T02:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15467",
    "user": "mabshoff"
}
```

Nick,

I cannot reproduce this with 2.10.3 on sage.math. Can you verify on your 2.10.3 build that this is still a problem?

Cheers,

Michael



---

archive/issue_comments_015468.json:
```json
{
    "body": "I am getting the same segfault under sage-2.10.3 and sage-2.10.4.alpha0, on two different machines running Gentoo Linux.",
    "created_at": "2008-03-16T01:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15468",
    "user": "AlexGhitza"
}
```

I am getting the same segfault under sage-2.10.3 and sage-2.10.4.alpha0, on two different machines running Gentoo Linux.



---

archive/issue_comments_015469.json:
```json
{
    "body": "Still crashes for me, 2.10.4.alpha0 (I think).",
    "created_at": "2008-03-16T19:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15469",
    "user": "ncalexan"
}
```

Still crashes for me, 2.10.4.alpha0 (I think).



---

archive/issue_comments_015470.json:
```json
{
    "body": "This now works. I assume it was fixed by #2843:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.alpha3, Release Date: 2008-04-09                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]\nsage: L = Qp(19).extension(F, names='a')\nsage: L\nUnramified Extension of 19-adic Field with capped relative precision 20 in a defined \nby (1 + O(19^20))*x^2 + (5 + 2*19 + 10*19^2 + 14*19^3 + 7*19^4 + 13*19^5 + 5*19^6 + \n12*19^7 + 8*19^8 + 4*19^9 + 14*19^10 + 6*19^11 + 5*19^12 + 13*19^13 + 16*19^14 + \n4*19^15 + 17*19^16 + 8*19^18 + 4*19^19 + O(19^20))*x + (1 + O(19^20))\nsage:\n```\n\n\nCan anybody confirm?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-11T20:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15470",
    "user": "mabshoff"
}
```

This now works. I assume it was fixed by #2843:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha3, Release Date: 2008-04-09                  |
| Type notebook() for the GUI, and license() for information.        |
sage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]
sage: L = Qp(19).extension(F, names='a')
sage: L
Unramified Extension of 19-adic Field with capped relative precision 20 in a defined 
by (1 + O(19^20))*x^2 + (5 + 2*19 + 10*19^2 + 14*19^3 + 7*19^4 + 13*19^5 + 5*19^6 + 
12*19^7 + 8*19^8 + 4*19^9 + 14*19^10 + 6*19^11 + 5*19^12 + 13*19^13 + 16*19^14 + 
4*19^15 + 17*19^16 + 8*19^18 + 4*19^19 + O(19^20))*x + (1 + O(19^20))
sage:
```


Can anybody confirm?

Cheers,

Michael



---

archive/issue_comments_015471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-11T21:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15471",
    "user": "kedlaya"
}
```

Resolution: fixed



---

archive/issue_comments_015472.json:
```json
{
    "body": "This is fixed for me also, by applying the patch from #2843 against 3.0alpha3 (which was merged in alpha4). The general problem that was fixed by #2843 was passing NTL objects by value rather than reference, which triggered an NTL copy operation using the wrong context.",
    "created_at": "2008-04-11T21:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15472",
    "user": "kedlaya"
}
```

This is fixed for me also, by applying the patch from #2843 against 3.0alpha3 (which was merged in alpha4). The general problem that was fixed by #2843 was passing NTL objects by value rather than reference, which triggered an NTL copy operation using the wrong context.



---

archive/issue_comments_015473.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-18T13:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15473",
    "user": "kedlaya"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_015474.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-18T13:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15474",
    "user": "kedlaya"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_015475.json:
```json
{
    "body": "Further investigation shows that this fails on my 32-bit laptop (and not on my 64-bit desktop), so I'm reopening. I think this is the same issue as #2928, so fixing one should fix the other. (It is indeed related to #2843, but the fix there seems insufficient to treat this.)",
    "created_at": "2008-04-18T13:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15475",
    "user": "kedlaya"
}
```

Further investigation shows that this fails on my 32-bit laptop (and not on my 64-bit desktop), so I'm reopening. I think this is the same issue as #2928, so fixing one should fix the other. (It is indeed related to #2843, but the fix there seems insufficient to treat this.)



---

archive/issue_comments_015476.json:
```json
{
    "body": "The fix for 2928 fixes this as well.",
    "created_at": "2008-04-20T22:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15476",
    "user": "roed"
}
```

The fix for 2928 fixes this as well.



---

archive/issue_comments_015477.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-21T19:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15477",
    "user": "kedlaya"
}
```

Attachment



---

archive/issue_comments_015478.json:
```json
{
    "body": "Since #2928 seems to fix this, but does not itself add any doctests, I propose to add a doctest here. See attached patch.",
    "created_at": "2008-04-21T19:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15478",
    "user": "kedlaya"
}
```

Since #2928 seems to fix this, but does not itself add any doctests, I propose to add a doctest here. See attached patch.



---

archive/issue_comments_015479.json:
```json
{
    "body": "Merged 9596.patch in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T03:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15479",
    "user": "mabshoff"
}
```

Merged 9596.patch in Sage 3.0.1.alpha0



---

archive/issue_comments_015480.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T03:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2325#issuecomment-15480",
    "user": "mabshoff"
}
```

Resolution: fixed
