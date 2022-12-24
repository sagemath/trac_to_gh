# Issue 1765: allow list of variables as second input to solve command (very easy to implement)

archive/issues_001765.json:
```json
{
    "body": "Assignee: was\n\nCC:  dfdeshom\n\n\n```\nsage: var(\"s,i,b,m,g\");\nsage: sys = [ m*(1-s) - b*s*i, b*s*i-g*i ];\nsage: equilibria = solve(sys,s,i);\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n\n> solve's\n> syntax seems assymetric as used here.  Shouldn't the second argument\n> be a sequence of variables?\n\nYou mean like this:\n\nsage: solve(sys, [s, i])              # this is not implemented\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n\nThat seems like a really good idea.\nNote that right now at least you can do the following\n(note the *) and it will work:\n\nsage: solve(sys, *[s, i])\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n\n```\n\n\nThis would be very easy to implement. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1765\n\n",
    "created_at": "2008-01-13T05:24:26Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "allow list of variables as second input to solve command (very easy to implement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1765",
    "user": "was"
}
```
Assignee: was

CC:  dfdeshom


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

archive/issue_comments_011144.json:
```json
{
    "body": "Attachment [1765.patch](tarball://root/attachments/some-uuid/ticket1765/1765.patch) by dfdeshom created at 2008-03-04 03:19:13",
    "created_at": "2008-03-04T03:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11144",
    "user": "dfdeshom"
}
```

Attachment [1765.patch](tarball://root/attachments/some-uuid/ticket1765/1765.patch) by dfdeshom created at 2008-03-04 03:19:13



---

archive/issue_comments_011145.json:
```json
{
    "body": "The patch doesn't actually do what the description asks for; more precisely, instead of the desired behavior\n\n\n```\nsage: solve(sys, [s, i])              # this is not implemented\n[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]\n```\n\n\nthis still throws a ValueError.",
    "created_at": "2008-03-13T12:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11145",
    "user": "AlexGhitza"
}
```

The patch doesn't actually do what the description asks for; more precisely, instead of the desired behavior


```
sage: solve(sys, [s, i])              # this is not implemented
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]
```


this still throws a ValueError.



---

archive/issue_comments_011146.json:
```json
{
    "body": "Attachment [1765.hg](tarball://root/attachments/some-uuid/ticket1765/1765.hg) by dfdeshom created at 2008-03-13 15:03:58",
    "created_at": "2008-03-13T15:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11146",
    "user": "dfdeshom"
}
```

Attachment [1765.hg](tarball://root/attachments/some-uuid/ticket1765/1765.hg) by dfdeshom created at 2008-03-13 15:03:58



---

archive/issue_comments_011147.json:
```json
{
    "body": "Should be corrected now so ` solve(sys, [s, i]) ` should now work. The correct changes are in 1765.hg, not the patch file (wish there was a way to delete files...)",
    "created_at": "2008-03-13T15:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11147",
    "user": "dfdeshom"
}
```

Should be corrected now so ` solve(sys, [s, i]) ` should now work. The correct changes are in 1765.hg, not the patch file (wish there was a way to delete files...)



---

archive/issue_comments_011148.json:
```json
{
    "body": "Attachment [1765_new.patch](tarball://root/attachments/some-uuid/ticket1765/1765_new.patch) by AlexGhitza created at 2008-03-15 17:41:33\n\nuse instead of the above",
    "created_at": "2008-03-15T17:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11148",
    "user": "AlexGhitza"
}
```

Attachment [1765_new.patch](tarball://root/attachments/some-uuid/ticket1765/1765_new.patch) by AlexGhitza created at 2008-03-15 17:41:33

use instead of the above



---

archive/issue_comments_011149.json:
```json
{
    "body": "I applied this to sage-2.10.3 and it looks good.  Since we tend to like patches rather than bundles, I've uploaded a patch that has the changes from the bundle.",
    "created_at": "2008-03-15T17:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11149",
    "user": "AlexGhitza"
}
```

I applied this to sage-2.10.3 and it looks good.  Since we tend to like patches rather than bundles, I've uploaded a patch that has the changes from the bundle.



---

archive/issue_comments_011150.json:
```json
{
    "body": "Merged 1765.hg in Sage 2.10.4.rc0. Credit-wise it was the cleanest solution, but I am sure that Didier will post Mercurial patches in the future.",
    "created_at": "2008-03-16T01:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11150",
    "user": "mabshoff"
}
```

Merged 1765.hg in Sage 2.10.4.rc0. Credit-wise it was the cleanest solution, but I am sure that Didier will post Mercurial patches in the future.



---

archive/issue_comments_011151.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T01:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1765#issuecomment-11151",
    "user": "mabshoff"
}
```

Resolution: fixed
