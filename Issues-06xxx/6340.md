# Issue 6340: [with patch, positive review] var('x',ns=False)  -- should go boom but silently gives a new symbolic variable

archive/issues_006340.json:
```json
{
    "body": "Assignee: @burcin\n\n```\nsage: type(var('x',ns=False))\n<type 'sage.symbolic.expression.Expression'>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6340\n\n",
    "closed_at": "2009-09-24T08:29:46Z",
    "created_at": "2009-06-16T19:22:25Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] var('x',ns=False)  -- should go boom but silently gives a new symbolic variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6340",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin

```
sage: type(var('x',ns=False))
<type 'sage.symbolic.expression.Expression'>
```

Issue created by migration from https://trac.sagemath.org/ticket/6340





---

archive/issue_comments_050508.json:
```json
{
    "body": "The fix should be to raise a DeprecationError... or possibly just a NotImplementedError...",
    "created_at": "2009-06-16T19:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50508",
    "user": "https://github.com/williamstein"
}
```

The fix should be to raise a DeprecationError... or possibly just a NotImplementedError...



---

archive/issue_comments_050509.json:
```json
{
    "body": "This raises a NotImplementedError for ns=False, but still creates the variable for ns=1 or ns=True, with a verbose level 0 message.",
    "created_at": "2009-08-26T16:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50509",
    "user": "https://github.com/kcrisman"
}
```

This raises a NotImplementedError for ns=False, but still creates the variable for ns=1 or ns=True, with a verbose level 0 message.



---

archive/issue_comments_050510.json:
```json
{
    "body": "Patch at #6559 enhances symbolic variables definition. Unfortunately, the patch there\nwill conflict with the patch here.",
    "created_at": "2009-09-05T21:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50510",
    "user": "https://github.com/golam-m-hossain"
}
```

Patch at #6559 enhances symbolic variables definition. Unfortunately, the patch there
will conflict with the patch here.



---

archive/issue_comments_050511.json:
```json
{
    "body": "It looks like #6559 functionality is better to incorporate first.  What happens after its inclusion with the following?\n\n```\nsage: var('z',ns=False)\n```\n\n```\nsage: var('z',ns=True)\n```\nThe results of these will help create a new patch, though that may not happen for a bit.  \n\nAlternately, since this one is small, one could review it positively (if it deserves to be) :) and then base the bigger patch at #6559 on it.",
    "created_at": "2009-09-06T02:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50511",
    "user": "https://github.com/kcrisman"
}
```

It looks like #6559 functionality is better to incorporate first.  What happens after its inclusion with the following?

```
sage: var('z',ns=False)
```

```
sage: var('z',ns=True)
```
The results of these will help create a new patch, though that may not happen for a bit.  

Alternately, since this one is small, one could review it positively (if it deserves to be) :) and then base the bigger patch at #6559 on it.



---

archive/issue_comments_050512.json:
```json
{
    "body": "Based on 4.1.1 and #6559",
    "created_at": "2009-09-21T15:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50512",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.1.1 and #6559



---

archive/issue_comments_050513.json:
```json
{
    "body": "Attachment [trac_6340-var-ns-based-6559.patch](tarball://root/attachments/some-uuid/ticket6340/trac_6340-var-ns-based-6559.patch) by @kcrisman created at 2009-09-21 15:16:20\n\nDepending on which one is reviewed first, here's a patch on top of #6559.  Should work identically.",
    "created_at": "2009-09-21T15:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50513",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6340-var-ns-based-6559.patch](tarball://root/attachments/some-uuid/ticket6340/trac_6340-var-ns-based-6559.patch) by @kcrisman created at 2009-09-21 15:16:20

Depending on which one is reviewed first, here's a patch on top of #6559.  Should work identically.



---

archive/issue_comments_050514.json:
```json
{
    "body": "This should use the deprecation function instead of the verbose function.\n\nFor example (from matrix_rational_dense.pyx)\n\n```\n        from sage.misc.misc import deprecation\n        deprecation(\"'invert' is deprecated; use 'inverse' instead.\")\n```",
    "created_at": "2009-09-22T15:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50514",
    "user": "https://github.com/jasongrout"
}
```

This should use the deprecation function instead of the verbose function.

For example (from matrix_rational_dense.pyx)

```
        from sage.misc.misc import deprecation
        deprecation("'invert' is deprecated; use 'inverse' instead.")
```



---

archive/issue_comments_050515.json:
```json
{
    "body": "I think `NotImplementedError` is OK for `ns=False`, but we should use a deprecation warning for `ns=1`.",
    "created_at": "2009-09-22T17:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50515",
    "user": "https://github.com/burcin"
}
```

I think `NotImplementedError` is OK for `ns=False`, but we should use a deprecation warning for `ns=1`.



---

archive/issue_comments_050516.json:
```json
{
    "body": "This makes sense.  I've updated the first patch as per Burcin's idea, which seems most appropriate.",
    "created_at": "2009-09-22T18:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50516",
    "user": "https://github.com/kcrisman"
}
```

This makes sense.  I've updated the first patch as per Burcin's idea, which seems most appropriate.



---

archive/issue_comments_050517.json:
```json
{
    "body": "Sorry for not pointing this out earlier, but I suggest changing the block:\n\n```\n    if ('ns', False) in kwds.items(): \n        raise NotImplementedError, \"The new (Pynac) symbolics are now the only symbolics; please do not use keyword `ns` any longer.\" \n    if ('ns', True) in kwds.items(): \n        from sage.misc.misc import deprecation \n        deprecation(\"The new (Pynac) symbolics are now the only symbolics; please do not use keyword 'ns' any longer.\") \n```\n\nwith\n\n```\n    if kwds.has_key('ns'):\n        if kwds['ns']:\n            from sage.misc.misc import deprecation \n            deprecation(\"The new (Pynac) symbolics are now the only symbolics; please do not use keyword 'ns' any longer.\") \n        else:\n            raise NotImplementedError, \"The new (Pynac) symbolics are now the only symbolics; please do not use keyword `ns` any longer.\" \n```\n\nEven if `kwds` is expected to be empty, it is a waste to call `.items()`.\n\nPutting a check that `*args` is empty would also help. Dropping arguments silently is not very user friendly.",
    "created_at": "2009-09-22T18:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50517",
    "user": "https://github.com/burcin"
}
```

Sorry for not pointing this out earlier, but I suggest changing the block:

```
    if ('ns', False) in kwds.items(): 
        raise NotImplementedError, "The new (Pynac) symbolics are now the only symbolics; please do not use keyword `ns` any longer." 
    if ('ns', True) in kwds.items(): 
        from sage.misc.misc import deprecation 
        deprecation("The new (Pynac) symbolics are now the only symbolics; please do not use keyword 'ns' any longer.") 
```

with

```
    if kwds.has_key('ns'):
        if kwds['ns']:
            from sage.misc.misc import deprecation 
            deprecation("The new (Pynac) symbolics are now the only symbolics; please do not use keyword 'ns' any longer.") 
        else:
            raise NotImplementedError, "The new (Pynac) symbolics are now the only symbolics; please do not use keyword `ns` any longer." 
```

Even if `kwds` is expected to be empty, it is a waste to call `.items()`.

Putting a check that `*args` is empty would also help. Dropping arguments silently is not very user friendly.



---

archive/issue_comments_050518.json:
```json
{
    "body": "Yes, I knew there was a more elegant way to do it, but didn't have time to look it up.  As for *args, I think I can safely get rid of that completely, since there are no args, only keywords.  Patch coming up.",
    "created_at": "2009-09-22T19:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50518",
    "user": "https://github.com/kcrisman"
}
```

Yes, I knew there was a more elegant way to do it, but didn't have time to look it up.  As for *args, I think I can safely get rid of that completely, since there are no args, only keywords.  Patch coming up.



---

archive/issue_comments_050519.json:
```json
{
    "body": "Based on 4.1.2.alpha2",
    "created_at": "2009-09-22T19:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50519",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.1.2.alpha2



---

archive/issue_comments_050520.json:
```json
{
    "body": "Attachment [trac_6340-var-ns.patch](tarball://root/attachments/some-uuid/ticket6340/trac_6340-var-ns.patch) by @kcrisman created at 2009-09-22 19:45:49\n\nThis should take care of it, I hope.",
    "created_at": "2009-09-22T19:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50520",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6340-var-ns.patch](tarball://root/attachments/some-uuid/ticket6340/trac_6340-var-ns.patch) by @kcrisman created at 2009-09-22 19:45:49

This should take care of it, I hope.



---

archive/issue_comments_050521.json:
```json
{
    "body": "Attachment [trac_6340-missing_bits.patch](tarball://root/attachments/some-uuid/ticket6340/trac_6340-missing_bits.patch) by @burcin created at 2009-09-22 22:42:47\n\nmore doctest fixes",
    "created_at": "2009-09-22T22:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50521",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6340-missing_bits.patch](tarball://root/attachments/some-uuid/ticket6340/trac_6340-missing_bits.patch) by @burcin created at 2009-09-22 22:42:47

more doctest fixes



---

archive/issue_comments_050522.json:
```json
{
    "body": "Looks good to me. AFAICT, there were two more places using the `ns=1` option. attachment:trac_6340-missing_bits.patch should take care of them.\n\nApply only\n\n* attachment:trac_6340-var-ns.patch\n* attachment:trac_6340-missing_bits.patch",
    "created_at": "2009-09-22T22:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50522",
    "user": "https://github.com/burcin"
}
```

Looks good to me. AFAICT, there were two more places using the `ns=1` option. attachment:trac_6340-missing_bits.patch should take care of them.

Apply only

* attachment:trac_6340-var-ns.patch
* attachment:trac_6340-missing_bits.patch



---

archive/issue_comments_050523.json:
```json
{
    "body": "To release manager:  the \"missing bits\" may be covered in other patches reviewed related to symbolics, so do not merge if that one won't merge (simple enough!).",
    "created_at": "2009-09-23T00:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50523",
    "user": "https://github.com/kcrisman"
}
```

To release manager:  the "missing bits" may be covered in other patches reviewed related to symbolics, so do not merge if that one won't merge (simple enough!).



---

archive/issue_comments_050524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T08:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50524",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050525.json:
```json
{
    "body": "Merged `trac_6340-var-ns.patch`.",
    "created_at": "2009-09-24T08:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50525",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6340-var-ns.patch`.



---

archive/issue_events_014909.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T08:29:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6340#event-14909"
}
```



---

archive/issue_comments_050526.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6340#issuecomment-50526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
