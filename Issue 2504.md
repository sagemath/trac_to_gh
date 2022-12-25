# Issue 2504: number field .units() method caches proof=False result and returns it for proof=True

archive/issues_002504.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following was reported by Luis Finotti on sage-support, here: http://groups.google.com/group/sage-support/browse_thread/thread/f01e8661743d36d4#\n\nThe following commands return an error:\n\n```\n   P.<x>=PolynomialRing(QQ)\n   f=x^17+3\n   K=NumberField(f,'a')\n   K.units(proof=True) # default\n```\n\nbecause Sage is incapable of performing the computation with proof=True.\n(The error ends with \"not enough precomputed primes, need primelimit ~  (35)\".)\n\nIf you then do\n\n```\n   K.units(proof=False)\n```\n\nyou get an answer immediately; then repeating the original\n\n```\n   K.units(proof=True)\n```\n\ngives you the unproved answer again even though proof=True is specified.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2504\n\n",
    "created_at": "2008-03-13T03:14:46Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "number field .units() method caches proof=False result and returns it for proof=True",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2504",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

The following was reported by Luis Finotti on sage-support, here: http://groups.google.com/group/sage-support/browse_thread/thread/f01e8661743d36d4#

The following commands return an error:

```
   P.<x>=PolynomialRing(QQ)
   f=x^17+3
   K=NumberField(f,'a')
   K.units(proof=True) # default
```

because Sage is incapable of performing the computation with proof=True.
(The error ends with "not enough precomputed primes, need primelimit ~  (35)".)

If you then do

```
   K.units(proof=False)
```

you get an answer immediately; then repeating the original

```
   K.units(proof=True)
```

gives you the unproved answer again even though proof=True is specified.

Issue created by migration from https://trac.sagemath.org/ticket/2504





---

archive/issue_comments_016927.json:
```json
{
    "body": "Attachment [2504-units_cache.patch](tarball://root/attachments/some-uuid/ticket2504/2504-units_cache.patch) by @aghitza created at 2008-04-13 02:27:55\n\nThe attached patch fixes this and adds doctests illustrating the correct behavior.",
    "created_at": "2008-04-13T02:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2504#issuecomment-16927",
    "user": "https://github.com/aghitza"
}
```

Attachment [2504-units_cache.patch](tarball://root/attachments/some-uuid/ticket2504/2504-units_cache.patch) by @aghitza created at 2008-04-13 02:27:55

The attached patch fixes this and adds doctests illustrating the correct behavior.



---

archive/issue_comments_016928.json:
```json
{
    "body": "Wait -- if you ask for units with proof, the value is cached.  If you then ask for it without proof, shouldn't we return the cached value?  The code doesn't look like it does that.",
    "created_at": "2008-04-15T16:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2504#issuecomment-16928",
    "user": "https://github.com/ncalexan"
}
```

Wait -- if you ask for units with proof, the value is cached.  If you then ask for it without proof, shouldn't we return the cached value?  The code doesn't look like it does that.



---

archive/issue_comments_016929.json:
```json
{
    "body": "Attachment [2504-units_cache.2.patch](tarball://root/attachments/some-uuid/ticket2504/2504-units_cache.2.patch) by @aghitza created at 2008-04-15 20:18:32\n\nYou are completely right.  I've replaced the patch and reorganized the code so it looks a bit cleaner.",
    "created_at": "2008-04-15T20:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2504#issuecomment-16929",
    "user": "https://github.com/aghitza"
}
```

Attachment [2504-units_cache.2.patch](tarball://root/attachments/some-uuid/ticket2504/2504-units_cache.2.patch) by @aghitza created at 2008-04-15 20:18:32

You are completely right.  I've replaced the patch and reorganized the code so it looks a bit cleaner.



---

archive/issue_comments_016930.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-26T17:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2504#issuecomment-16930",
    "user": "https://github.com/ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_016931.json:
```json
{
    "body": "Merged 2504-units_cache.2.patch in Sage 3.0.1.alpha1",
    "created_at": "2008-04-26T21:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2504#issuecomment-16931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2504-units_cache.2.patch in Sage 3.0.1.alpha1



---

archive/issue_events_005886.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-26T21:58:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2504#event-5886"
}
```



---

archive/issue_comments_016932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T21:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2504#issuecomment-16932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
