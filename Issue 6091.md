# Issue 6091: [with patch, needs review] syntax extended for subfields of number fields

archive/issues_006091.json:
```json
{
    "body": "Assignee: tbd\n\nAt present\n\n```\nsage: C.<z> = CyclotomicField(20)\nsage: D.<w>, phi = C.subfield(z^4)\n```\nfails.\n\nThis is simply because the code uses the name `name` instead of the name `names`.  The patch fixes this, and does the same for `change_generator` (with doctests).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6091\n\n",
    "created_at": "2009-05-20T06:41:06Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] syntax extended for subfields of number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6091",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: tbd

At present

```
sage: C.<z> = CyclotomicField(20)
sage: D.<w>, phi = C.subfield(z^4)
```
fails.

This is simply because the code uses the name `name` instead of the name `names`.  The patch fixes this, and does the same for `change_generator` (with doctests).

Issue created by migration from https://trac.sagemath.org/ticket/6091





---

archive/issue_comments_048444.json:
```json
{
    "body": "Attachment [trac_6091.patch](tarball://root/attachments/some-uuid/ticket6091/trac_6091.patch) by @loefflerd created at 2009-05-29 10:46:30\n\nPositive review. Patch applies fine to 4.0.rc1, all tests in sage/rings/number_field and doc/en/bordeaux_2008 pass; and the new syntax is a very useful thing to have.\n\nDavid",
    "created_at": "2009-05-29T10:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48444",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6091.patch](tarball://root/attachments/some-uuid/ticket6091/trac_6091.patch) by @loefflerd created at 2009-05-29 10:46:30

Positive review. Patch applies fine to 4.0.rc1, all tests in sage/rings/number_field and doc/en/bordeaux_2008 pass; and the new syntax is a very useful thing to have.

David



---

archive/issue_comments_048445.json:
```json
{
    "body": "Changing component from algebra to number theory.",
    "created_at": "2009-05-29T10:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48445",
    "user": "https://github.com/loefflerd"
}
```

Changing component from algebra to number theory.



---

archive/issue_comments_048446.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2009-05-29T10:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48446",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_events_014307.json:
```json
{
    "actor": "https://github.com/loefflerd",
    "created_at": "2009-05-29T10:46:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "milestone": "sage-4.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6091#event-14307"
}
```



---

archive/issue_comments_048447.json:
```json
{
    "body": "This will break all old code that uses the name= syntax.\n\nThere is a decorator at sage.plot.misc.rename_keyword that could be use to rename a 'name' keyword argument to 'names'.  A useful thing to do would be to add a flag to that decorator so that a deprecation warning would be thrown whenever a rename is done.",
    "created_at": "2009-06-01T00:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48447",
    "user": "https://github.com/mwhansen"
}
```

This will break all old code that uses the name= syntax.

There is a decorator at sage.plot.misc.rename_keyword that could be use to rename a 'name' keyword argument to 'names'.  A useful thing to do would be to add a flag to that decorator so that a deprecation warning would be thrown whenever a rename is done.



---

archive/issue_comments_048448.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> This will break all old code that uses the name= syntax.\n\nPoint taken.\n\n> There is a decorator at sage.plot.misc.rename_keyword that could be use to rename a 'name' keyword argument to 'names'.  A useful thing to do would be to add a flag to that decorator so that a deprecation warning would be thrown whenever a rename is done.\n\n\nI think in this case there's a simpler solution,  already used in the `NumberField`function, which allows either `name` or `names`; see the replacement patch.",
    "created_at": "2009-06-01T21:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48448",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:2 mhansen]:
> This will break all old code that uses the name= syntax.

Point taken.

> There is a decorator at sage.plot.misc.rename_keyword that could be use to rename a 'name' keyword argument to 'names'.  A useful thing to do would be to add a flag to that decorator so that a deprecation warning would be thrown whenever a rename is done.


I think in this case there's a simpler solution,  already used in the `NumberField`function, which allows either `name` or `names`; see the replacement patch.



---

archive/issue_comments_048449.json:
```json
{
    "body": "Attachment [trac_6091_revised.patch](tarball://root/attachments/some-uuid/ticket6091/trac_6091_revised.patch) by fwclarke created at 2009-06-01 21:41:17\n\nreplaces previous",
    "created_at": "2009-06-01T21:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48449",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_6091_revised.patch](tarball://root/attachments/some-uuid/ticket6091/trac_6091_revised.patch) by fwclarke created at 2009-06-01 21:41:17

replaces previous



---

archive/issue_events_014308.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T19:08:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6091#event-14308"
}
```



---

archive/issue_comments_048450.json:
```json
{
    "body": "While it is a solution, I think it's a bit more hackish.  We should really clean these things up a bit.  But, I'm okay with this going in.\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48450",
    "user": "https://github.com/mwhansen"
}
```

While it is a solution, I think it's a bit more hackish.  We should really clean these things up a bit.  But, I'm okay with this going in.

Merged in 4.0.1.rc1.



---

archive/issue_comments_048451.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6091#issuecomment-48451",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
