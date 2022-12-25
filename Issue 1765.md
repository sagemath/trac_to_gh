# Issue 1765: allow list of variables as second input to solve command (very easy to implement)

archive/issues_001765.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @dfdeshom\n\n\n```\nsage: var(\"s,i,b,m,g\");\nsage: sys = [ m*(1-s) - b*s*i, b*s*i-g*i ];\nsage: equilibria = solve(sys,s,i);\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n\n> solve's\n> syntax seems assymetric as used here.  Shouldn't the second argument\n> be a sequence of variables?\n\nYou mean like this:\n\nsage: solve(sys, [s, i])              # this is not implemented\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n\nThat seems like a really good idea.\nNote that right now at least you can do the following\n(note the *) and it will work:\n\nsage: solve(sys, *[s, i])\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n\n```\n\n\nThis would be very easy to implement. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1765\n\n",
    "created_at": "2008-01-13T05:24:26Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "allow list of variables as second input to solve command (very easy to implement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1765",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @dfdeshom


```
sage: var("s,i,b,m,g");
sage: sys = [ m*(1-s) - b*s*i, b*s*i-g*i ];
sage: equilibria = solve(sys,s,i);
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]

> solve's
> syntax seems assymetric as used here.  Shouldn't the second argument
> be a sequence of variables?

You mean like this:

sage: solve(sys, [s, i])              # this is not implemented
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]

That seems like a really good idea.
Note that right now at least you can do the following
(note the *) and it will work:

sage: solve(sys, *[s, i])
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]

```


This would be very easy to implement. 

Issue created by migration from https://trac.sagemath.org/ticket/1765





---

archive/issue_comments_011117.json:
```json
{
    "body": "Attachment [1765.patch](tarball://root/attachments/some-uuid/ticket1765/1765.patch) by @dfdeshom created at 2008-03-04 03:19:13",
    "created_at": "2008-03-04T03:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11117",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [1765.patch](tarball://root/attachments/some-uuid/ticket1765/1765.patch) by @dfdeshom created at 2008-03-04 03:19:13



---

archive/issue_events_004282.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:00:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1765#event-4282"
}
```



---

archive/issue_comments_011118.json:
```json
{
    "body": "The patch doesn't actually do what the description asks for; more precisely, instead of the desired behavior\n\n\n```\nsage: solve(sys, [s, i])              # this is not implemented\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n```\n\n\nthis still throws a ValueError.",
    "created_at": "2008-03-13T12:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11118",
    "user": "https://github.com/aghitza"
}
```

The patch doesn't actually do what the description asks for; more precisely, instead of the desired behavior


```
sage: solve(sys, [s, i])              # this is not implemented
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]
```


this still throws a ValueError.



---

archive/issue_comments_011119.json:
```json
{
    "body": "Attachment [1765.hg](tarball://root/attachments/some-uuid/ticket1765/1765.hg) by @dfdeshom created at 2008-03-13 15:03:58",
    "created_at": "2008-03-13T15:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11119",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [1765.hg](tarball://root/attachments/some-uuid/ticket1765/1765.hg) by @dfdeshom created at 2008-03-13 15:03:58



---

archive/issue_comments_011120.json:
```json
{
    "body": "Should be corrected now so ` solve(sys, [s, i]) ` should now work. The correct changes are in 1765.hg, not the patch file (wish there was a way to delete files...)",
    "created_at": "2008-03-13T15:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11120",
    "user": "https://github.com/dfdeshom"
}
```

Should be corrected now so ` solve(sys, [s, i]) ` should now work. The correct changes are in 1765.hg, not the patch file (wish there was a way to delete files...)



---

archive/issue_comments_011121.json:
```json
{
    "body": "Attachment [1765_new.patch](tarball://root/attachments/some-uuid/ticket1765/1765_new.patch) by @aghitza created at 2008-03-15 17:41:33\n\nuse instead of the above",
    "created_at": "2008-03-15T17:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11121",
    "user": "https://github.com/aghitza"
}
```

Attachment [1765_new.patch](tarball://root/attachments/some-uuid/ticket1765/1765_new.patch) by @aghitza created at 2008-03-15 17:41:33

use instead of the above



---

archive/issue_comments_011122.json:
```json
{
    "body": "I applied this to sage-2.10.3 and it looks good.  Since we tend to like patches rather than bundles, I've uploaded a patch that has the changes from the bundle.",
    "created_at": "2008-03-15T17:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11122",
    "user": "https://github.com/aghitza"
}
```

I applied this to sage-2.10.3 and it looks good.  Since we tend to like patches rather than bundles, I've uploaded a patch that has the changes from the bundle.



---

archive/issue_comments_011123.json:
```json
{
    "body": "Merged 1765.hg in Sage 2.10.4.rc0. Credit-wise it was the cleanest solution, but I am sure that Didier will post Mercurial patches in the future.",
    "created_at": "2008-03-16T01:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1765.hg in Sage 2.10.4.rc0. Credit-wise it was the cleanest solution, but I am sure that Didier will post Mercurial patches in the future.



---

archive/issue_comments_011124.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T01:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004283.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T01:07:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1765#event-4283"
}
```
