# Issue 2095: Simplification sometimes is wrong in Sage

archive/issues_002095.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n```\nsage: plot(arcsin(sin(x)))\n```\n\nplots a straight line.\n\n```\nsage: x/x\n1\n```\n\n\n```\nsage: assume(x<0)\nsage: sqrt(x)^2\nx\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2095\n\n",
    "closed_at": "2008-03-16T20:56:08Z",
    "created_at": "2008-02-08T01:36:44Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Simplification sometimes is wrong in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2095",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @garyfurnish

```
sage: plot(arcsin(sin(x)))
```

plots a straight line.

```
sage: x/x
1
```


```
sage: assume(x<0)
sage: sqrt(x)^2
x
```


Issue created by migration from https://trac.sagemath.org/ticket/2095





---

archive/issue_comments_013525.json:
```json
{
    "body": "Which is \"sometimes wrong\"?  The first two examples look fine to me.  For the third, we're totally screwed -- or -- we just don't understand Maxima, since it's just the\nnative behavior of Maxima:\n\n```\n\nsage: !maxima\nMaxima 5.13.0 http://maxima.sourceforge.net\nUsing Lisp CLISP 2.41 (2006-10-13)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) assume(x<0);\n(%o1)                               [x < 0]\n(%i2) sqrt(x)^2;\n(%o2)                                  x\n\n```",
    "created_at": "2008-02-08T04:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2095#issuecomment-13525",
    "user": "https://github.com/williamstein"
}
```

Which is "sometimes wrong"?  The first two examples look fine to me.  For the third, we're totally screwed -- or -- we just don't understand Maxima, since it's just the
native behavior of Maxima:

```

sage: !maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x<0);
(%o1)                               [x < 0]
(%i2) sqrt(x)^2;
(%o2)                                  x

```



---

archive/issue_comments_013526.json:
```json
{
    "body": "These are examples pointed out by Peter Jipsen... the second one I think is okay. The first one could be problematic, but Robert pointed out that it works fine if you use fast_eval. For the third, I think we are screwed. There is the command\n\n```\ndomain:real;\nreal\n\ndomain:complex;\ncomplex\n```\n\nin maxima, however the *only* effect that this seems to have on Maxima is if domain is real, sqrt(x^2) returns abs(x).\n\nPerhaps this should be changed to an enhancement. Assume() is currently only there as a workaround to Maxima's interactive behavior; it would be nice if Sage were smarter about assumptions on symbolic variables.",
    "created_at": "2008-02-08T21:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2095#issuecomment-13526",
    "user": "https://github.com/bobmoretti"
}
```

These are examples pointed out by Peter Jipsen... the second one I think is okay. The first one could be problematic, but Robert pointed out that it works fine if you use fast_eval. For the third, I think we are screwed. There is the command

```
domain:real;
real

domain:complex;
complex
```

in maxima, however the *only* effect that this seems to have on Maxima is if domain is real, sqrt(x^2) returns abs(x).

Perhaps this should be changed to an enhancement. Assume() is currently only there as a workaround to Maxima's interactive behavior; it would be nice if Sage were smarter about assumptions on symbolic variables.



---

archive/issue_events_005030.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-08T22:27:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2095#event-5030"
}
```



---

archive/issue_comments_013527.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2095#issuecomment-13527",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013528.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-16T20:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2095#issuecomment-13528",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_events_005031.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-16T20:56:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2095#event-5031"
}
```



---

archive/issue_comments_013529.json:
```json
{
    "body": "We're being stupid.  Clearly `sqrt(x)^2` should equal x NO MATTER what x is.  Period.  No matter what you assume about x it has to be the case the \"sqrt(x)\" is\nsomething that when squared gives x. That's the definition of \"square root\".",
    "created_at": "2008-03-16T20:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2095#issuecomment-13529",
    "user": "https://github.com/williamstein"
}
```

We're being stupid.  Clearly `sqrt(x)^2` should equal x NO MATTER what x is.  Period.  No matter what you assume about x it has to be the case the "sqrt(x)" is
something that when squared gives x. That's the definition of "square root".



---

archive/issue_comments_013530.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-16T20:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2095#issuecomment-13530",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_events_005032.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T21:06:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2095",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2095#event-5032"
}
```
