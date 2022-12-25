# Issue 5112: generic Pollard lambda algorithm

archive/issues_005112.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mraum\n\nFollowing #5098, here is a generic implementation of Pollard lambda algorithm.\nThere is probably still lots of room for optimization, but it works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5112\n\n",
    "created_at": "2009-01-27T20:50:07Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "generic Pollard lambda algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5112",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: tbd

CC:  mraum

Following #5098, here is a generic implementation of Pollard lambda algorithm.
There is probably still lots of room for optimization, but it works.

Issue created by migration from https://trac.sagemath.org/ticket/5112





---

archive/issue_comments_038992.json:
```json
{
    "body": "patch needs #5098 to be applied first.",
    "created_at": "2009-01-27T20:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38992",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

patch needs #5098 to be applied first.



---

archive/issue_comments_038993.json:
```json
{
    "body": "patch updated. should be applied after #5098 trac-5098-alpha2based.patch",
    "created_at": "2009-01-29T12:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38993",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

patch updated. should be applied after #5098 trac-5098-alpha2based.patch



---

archive/issue_comments_038994.json:
```json
{
    "body": "Patch applies fine to 3.3.alpha2 + (from #5098) trac-5098-alpha2based.patch and tests pass.  Code looks good and docstring & doctests are fine.\n\nI think it is excellent to have more of these generic algorithms available.  Pass!",
    "created_at": "2009-02-01T15:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38994",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 3.3.alpha2 + (from #5098) trac-5098-alpha2based.patch and tests pass.  Code looks good and docstring & doctests are fine.

I think it is excellent to have more of these generic algorithms available.  Pass!



---

archive/issue_comments_038995.json:
```json
{
    "body": "John,\n\nplease make sure not to sneak extra spaces in between positive and review since the reports do not pick up such tickets. The reports should be fixed to ignore extra white space, but until then ....\n\nCheers,\n\nMichael",
    "created_at": "2009-02-01T15:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38995",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John,

please make sure not to sneak extra spaces in between positive and review since the reports do not pick up such tickets. The reports should be fixed to ignore extra white space, but until then ....

Cheers,

Michael



---

archive/issue_comments_038996.json:
```json
{
    "body": "Attachment [trac-5112.patch](tarball://root/attachments/some-uuid/ticket5112/trac-5112.patch) by ylchapuy created at 2009-02-11 10:19:29\n\npatch updated after trac-5098-doctest.patch",
    "created_at": "2009-02-11T10:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38996",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac-5112.patch](tarball://root/attachments/some-uuid/ticket5112/trac-5112.patch) by ylchapuy created at 2009-02-11 10:19:29

patch updated after trac-5098-doctest.patch



---

archive/issue_comments_038997.json:
```json
{
    "body": "Hi Yann,\n\nhow large are the changes? If it is \"just\" a rebase with no or minimal functional changes (i.e. some exception changed) the positive review can stand.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T10:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Yann,

how large are the changes? If it is "just" a rebase with no or minimal functional changes (i.e. some exception changed) the positive review can stand.

Cheers,

Michael



---

archive/issue_comments_038998.json:
```json
{
    "body": "yes, it's indeed strictly a rebase. I just wanted to be sure the patch applies cleanly.",
    "created_at": "2009-02-11T11:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38998",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

yes, it's indeed strictly a rebase. I just wanted to be sure the patch applies cleanly.



---

archive/issue_events_011824.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T03:00:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5112#event-11824"
}
```



---

archive/issue_comments_038999.json:
```json
{
    "body": "This is 3.3 material.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T03:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-38999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is 3.3 material.

Cheers,

Michael



---

archive/issue_comments_039000.json:
```json
{
    "body": "SECOND REVIEW:\n\n* Line 1 of docstring: \"Pollard Lambda algorithm for computing discrete logarithm.\"\nIt should be \"Pollard Lambda algorithm for computing discrete logarithms.\" or \"Pollard Lambda algorithm for computing the discrete logarithm.\"\n\n* The docstring has a typo in line 2: \"usefull\" \n\n* The sections in the docstring should have space between them (e.g., a blank line before EXAMPLES:).  This can be ignored because of the ReST/Sphinx transition, which will probably change that. \n\n* I noticed this line\n\n```\nN = width.isqrt()+1 \n```\n\nIf width is a Python int then that will fail.  This is easy to trigger and will accidentally happen in library code easily:\n\n```\nsage: F.<a> = GF(2^63) \nsage: g = F.gen()\nsage: pollard_lambda(g, g^1234567, (1200000,1250000)) \n1234567\nsage: pollard_lambda(g, g^1234567, (int(1200000), int(1250000))) \n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/space/wstein/sage-3.3.rc0/<ipython console> in <module>()\n\n/space/wstein/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/groups/generic.pyc in pollard_lambda(base, a, bounds, ord, operation, hash_function, memory)\n    649 \n    650     width = ub-lb\n--> 651     N = width.isqrt()+1\n    652 \n    653     M = dict()\n\nAttributeError: 'int' object has no attribute 'isqrt'\n```\n\n\n* the doctests are insufficient.  The function signature is\n\n```\ndef pollard_lambda(base, a, bounds, ord=None, operation='*', hash_function=hash, memory=None): \n```\n\nAt a bare minimum, there must be doctests that test use of all the inputs to the function.",
    "created_at": "2009-02-15T08:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39000",
    "user": "https://github.com/williamstein"
}
```

SECOND REVIEW:

* Line 1 of docstring: "Pollard Lambda algorithm for computing discrete logarithm."
It should be "Pollard Lambda algorithm for computing discrete logarithms." or "Pollard Lambda algorithm for computing the discrete logarithm."

* The docstring has a typo in line 2: "usefull" 

* The sections in the docstring should have space between them (e.g., a blank line before EXAMPLES:).  This can be ignored because of the ReST/Sphinx transition, which will probably change that. 

* I noticed this line

```
N = width.isqrt()+1 
```

If width is a Python int then that will fail.  This is easy to trigger and will accidentally happen in library code easily:

```
sage: F.<a> = GF(2^63) 
sage: g = F.gen()
sage: pollard_lambda(g, g^1234567, (1200000,1250000)) 
1234567
sage: pollard_lambda(g, g^1234567, (int(1200000), int(1250000))) 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/space/wstein/sage-3.3.rc0/<ipython console> in <module>()

/space/wstein/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/groups/generic.pyc in pollard_lambda(base, a, bounds, ord, operation, hash_function, memory)
    649 
    650     width = ub-lb
--> 651     N = width.isqrt()+1
    652 
    653     M = dict()

AttributeError: 'int' object has no attribute 'isqrt'
```


* the doctests are insufficient.  The function signature is

```
def pollard_lambda(base, a, bounds, ord=None, operation='*', hash_function=hash, memory=None): 
```

At a bare minimum, there must be doctests that test use of all the inputs to the function.



---

archive/issue_events_011825.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-16T05:00:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5112#event-11825"
}
```



---

archive/issue_events_011826.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-16T05:00:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5112#event-11826"
}
```



---

archive/issue_comments_039001.json:
```json
{
    "body": "I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T05:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael



---

archive/issue_comments_039002.json:
```json
{
    "body": "It should be quite similar to #5098.",
    "created_at": "2009-12-14T18:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39002",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

It should be quite similar to #5098.



---

archive/issue_comments_039003.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-14T18:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39003",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039004.json:
```json
{
    "body": "Attachment [trac-5112-rebased.patch](tarball://root/attachments/some-uuid/ticket5112/trac-5112-rebased.patch) by ylchapuy created at 2009-12-14 23:25:12\n\nbased on 4.3.alpha1 + #5098",
    "created_at": "2009-12-14T23:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39004",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac-5112-rebased.patch](tarball://root/attachments/some-uuid/ticket5112/trac-5112-rebased.patch) by ylchapuy created at 2009-12-14 23:25:12

based on 4.3.alpha1 + #5098



---

archive/issue_comments_039005.json:
```json
{
    "body": "Good point, it is similar.\n\nAccording to Micheal's comment, I added one doctest, testing the hash_function, too. Now, I think it's good.",
    "created_at": "2009-12-15T09:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Good point, it is similar.

According to Micheal's comment, I added one doctest, testing the hash_function, too. Now, I think it's good.



---

archive/issue_comments_039006.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T09:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039007.json:
```json
{
    "body": "Attachment [trac-5112-pollard_review.patch](tarball://root/attachments/some-uuid/ticket5112/trac-5112-pollard_review.patch) by mraum created at 2009-12-15 09:26:49",
    "created_at": "2009-12-15T09:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-5112-pollard_review.patch](tarball://root/attachments/some-uuid/ticket5112/trac-5112-pollard_review.patch) by mraum created at 2009-12-15 09:26:49



---

archive/issue_comments_039008.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T16:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5112#issuecomment-39008",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_011827.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T16:12:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5112#event-11827"
}
```



---

archive/issue_events_011828.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T17:16:06Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5112#event-11828"
}
```



---

archive/issue_events_011829.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T17:16:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5112",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5112#event-11829"
}
```
