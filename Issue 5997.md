# Issue 5997: deprecate the "order" method on elements of rings.

archive/issues_005997.json:
```json
{
    "body": "Assignee: tbd\n\nThere was a vote in sage-devel in the thread entitled \"order of elements in the field\" to deprecate the order method on ring elements, and keep just the additive_order and multiplicative_order methods.  The order method is too ambiguous in the context of rings, and does cause regular confusion.  \n\nThis should be officially deprecated, and only removed after >= 6 months. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5997\n\n",
    "created_at": "2009-05-06T17:55:43Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "deprecate the \"order\" method on elements of rings.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5997",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

There was a vote in sage-devel in the thread entitled "order of elements in the field" to deprecate the order method on ring elements, and keep just the additive_order and multiplicative_order methods.  The order method is too ambiguous in the context of rings, and does cause regular confusion.  

This should be officially deprecated, and only removed after >= 6 months. 

Issue created by migration from https://trac.sagemath.org/ticket/5997





---

archive/issue_comments_047625.json:
```json
{
    "body": "Here's a very simple patch.",
    "created_at": "2009-05-06T19:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47625",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a very simple patch.



---

archive/issue_comments_047626.json:
```json
{
    "body": "Shouldn't this patch add a doctest while adding the deprecation warning? Otherwise it isn't obvious that the function is depreacted from looking at \"order?\"\n\nCheers,\n\nMichael",
    "created_at": "2009-05-06T21:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Shouldn't this patch add a doctest while adding the deprecation warning? Otherwise it isn't obvious that the function is depreacted from looking at "order?"

Cheers,

Michael



---

archive/issue_comments_047627.json:
```json
{
    "body": "> Shouldn't this patch add a doctest while adding the deprecation warning?\n\nNo, I don't think so... Just kidding.  Here's a new patch with a doctest.",
    "created_at": "2009-05-07T05:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47627",
    "user": "https://github.com/jhpalmieri"
}
```

> Shouldn't this patch add a doctest while adding the deprecation warning?

No, I don't think so... Just kidding.  Here's a new patch with a doctest.



---

archive/issue_comments_047628.json:
```json
{
    "body": "Attachment [trac_5997-reviewer.patch](tarball://root/attachments/some-uuid/ticket5997/trac_5997-reviewer.patch) by mvngu created at 2009-05-08 00:14:53\n\nreviewer patch; fix trivial typo",
    "created_at": "2009-05-08T00:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5997-reviewer.patch](tarball://root/attachments/some-uuid/ticket5997/trac_5997-reviewer.patch) by mvngu created at 2009-05-08 00:14:53

reviewer patch; fix trivial typo



---

archive/issue_comments_047629.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch `trac_5997.patch` applies OK against the \"post-final\" sage-3.4.2 and all doctests pass with the options `-t -long`. Now say we create an element in `Z/12Z` like so:\n\n```\nsage: a = Integers(12)(5)\n```\n\nThen both `a.order()` and ` a.additive_order()` return the same result, but `a.order()` additionally gives a deprecation warning:\n\n```\nsage: a.order()\n/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: The function order is deprecated for ring elements; use additive_order or multiplicative_order instead.\n  exec code_obj in self.user_global_ns, self.user_ns\n12\n```\n\n\n\n\nHowever, there's one trivial typo in the patch. This is fixed in the reviewer patch `trac_5997-reviewer.patch`. Basically, I give positive review to John's patch. Only my patch needs to be reviewed.",
    "created_at": "2009-05-08T00:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



The patch `trac_5997.patch` applies OK against the "post-final" sage-3.4.2 and all doctests pass with the options `-t -long`. Now say we create an element in `Z/12Z` like so:

```
sage: a = Integers(12)(5)
```

Then both `a.order()` and ` a.additive_order()` return the same result, but `a.order()` additionally gives a deprecation warning:

```
sage: a.order()
/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: The function order is deprecated for ring elements; use additive_order or multiplicative_order instead.
  exec code_obj in self.user_global_ns, self.user_ns
12
```




However, there's one trivial typo in the patch. This is fixed in the reviewer patch `trac_5997-reviewer.patch`. Basically, I give positive review to John's patch. Only my patch needs to be reviewed.



---

archive/issue_comments_047630.json:
```json
{
    "body": "Rubber stamp. We don't need no stinkin' review for trivial review patches fixing an obvious typo ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-08T00:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Rubber stamp. We don't need no stinkin' review for trivial review patches fixing an obvious typo ;)

Cheers,

Michael



---

archive/issue_events_014087.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-13T18:27:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5997#event-14087"
}
```



---

archive/issue_events_014088.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-13T18:27:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5997#event-14088"
}
```



---

archive/issue_comments_047631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-13T18:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047632.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5997#issuecomment-47632",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
