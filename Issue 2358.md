# Issue 2358: phi(I) for phi a ring morphism and I an ideal should work (IMHO); it used to and now it doesn't because of new-ish arithmetic architecture stuff

archive/issues_002358.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nWho rewrote the ring morphism code so that if phi is a\nring morphism, then phi(I) no longer works, for an ideal I?\nOh, David Roed in changeset 6772 (for me) from a few\nmonths ago did this:\n\n  \"Cython'ed sage/rings/morphism.py, actually added wrapper_parent (even though I claimed to in the previous commit).\"\n\nI think that feature, i.e., that phi(I) works, was very nice\nand is standard notation in mathematics, and I want\nit back.   Then the codepath that leads to the above weird\nbug wouldn't exist.\n\nI think the way to fix this is:\n  (1) Rethink the assumption you're forcing on morphisms that they\ncan only apply to elements in the domain.   This overloading of\ncalling a morphism on (sub)objects is very standard in mathematics.\n  (2) Change the architecture of __call__ as a result of (1).\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2358\n\n",
    "created_at": "2008-03-01T05:15:24Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "phi(I) for phi a ring morphism and I an ideal should work (IMHO); it used to and now it doesn't because of new-ish arithmetic architecture stuff",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2358",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
Who rewrote the ring morphism code so that if phi is a
ring morphism, then phi(I) no longer works, for an ideal I?
Oh, David Roed in changeset 6772 (for me) from a few
months ago did this:

  "Cython'ed sage/rings/morphism.py, actually added wrapper_parent (even though I claimed to in the previous commit)."

I think that feature, i.e., that phi(I) works, was very nice
and is standard notation in mathematics, and I want
it back.   Then the codepath that leads to the above weird
bug wouldn't exist.

I think the way to fix this is:
  (1) Rethink the assumption you're forcing on morphisms that they
can only apply to elements in the domain.   This overloading of
calling a morphism on (sub)objects is very standard in mathematics.
  (2) Change the architecture of __call__ as a result of (1).

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/2358





---

archive/issue_comments_015865.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2009-01-23T13:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2358#issuecomment-15865",
    "user": "https://github.com/roed314"
}
```

Resolution: worksforme



---

archive/issue_events_005562.json:
```json
{
    "actor": "https://github.com/roed314",
    "created_at": "2009-01-23T13:36:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2358",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2358#event-5562"
}
```



---

archive/issue_comments_015866.json:
```json
{
    "body": "This was previously fixed.  See sage.categories.map.Map.__call__",
    "created_at": "2009-01-23T13:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2358#issuecomment-15866",
    "user": "https://github.com/roed314"
}
```

This was previously fixed.  See sage.categories.map.Map.__call__



---

archive/issue_events_005563.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T15:33:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2358",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2358#event-5563"
}
```
