# Issue 6937: Fixed cached_function to handle defaults better.

archive/issues_006937.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @craigcitro\n\nWe expect the following example to take about 10 seconds:\n\n\n```\nsage: @cached_function\nsage: def foo(x = 5):\n...       print \"computing foo(%s)\"%x\n...       sleep(10)\n...       return 0\nsage: w = walltime()\nsage: foo()\ncomputing foo(5)\nsage: foo(5)\ncomputing foo(5)\nsage: foo(x=5)\ncomputing foo(5)\nsage: print \"that took %s seconds!\"%walltime(w)\nthat took 29.9967029095 seconds!\n```\n\n\n... but that obviously isn't the case.  fix it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/6937\n\n",
    "created_at": "2009-09-15T20:06:23Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Fixed cached_function to handle defaults better.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6937",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

CC:  @craigcitro

We expect the following example to take about 10 seconds:


```
sage: @cached_function
sage: def foo(x = 5):
...       print "computing foo(%s)"%x
...       sleep(10)
...       return 0
sage: w = walltime()
sage: foo()
computing foo(5)
sage: foo(5)
computing foo(5)
sage: foo(x=5)
computing foo(5)
sage: print "that took %s seconds!"%walltime(w)
that took 29.9967029095 seconds!
```


... but that obviously isn't the case.  fix it!

Issue created by migration from https://trac.sagemath.org/ticket/6937





---

archive/issue_comments_057234.json:
```json
{
    "body": "Here's a problem:\n\n\n```\nsage: class Foo:\n    def bar(self, a, b, c=0, d=None):\n        return a\nsage: A = Foo()\nsage: A.bar(1,2,3,4)\n1\nsage: from sage.misc.function_mangling import ArgumentFixer\nsage: AA = ArgumentFixer(A.bar)\nsage: AA.fix_to_named(1,2,3,4)\n((), (('self', 1), ('a', 2), ('b', 3), ('c', 4), ('d', None)))\n\n```\n\n\nHere, self isn't 1. a should be 1.",
    "created_at": "2009-09-19T20:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6937#issuecomment-57234",
    "user": "https://github.com/rlmill"
}
```

Here's a problem:


```
sage: class Foo:
    def bar(self, a, b, c=0, d=None):
        return a
sage: A = Foo()
sage: A.bar(1,2,3,4)
1
sage: from sage.misc.function_mangling import ArgumentFixer
sage: AA = ArgumentFixer(A.bar)
sage: AA.fix_to_named(1,2,3,4)
((), (('self', 1), ('a', 2), ('b', 3), ('c', 4), ('d', None)))

```


Here, self isn't 1. a should be 1.



---

archive/issue_comments_057235.json:
```json
{
    "body": "Sorry, my gripe should be that \"classmethod\" is undocumented.",
    "created_at": "2009-09-19T20:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6937#issuecomment-57235",
    "user": "https://github.com/rlmill"
}
```

Sorry, my gripe should be that "classmethod" is undocumented.



---

archive/issue_comments_057236.json:
```json
{
    "body": "Attachment [6937-improve_cache_with_defaults.patch](tarball://root/attachments/some-uuid/ticket6937/6937-improve_cache_with_defaults.patch) by boothby created at 2009-09-20 03:44:48",
    "created_at": "2009-09-20T03:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6937#issuecomment-57236",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [6937-improve_cache_with_defaults.patch](tarball://root/attachments/some-uuid/ticket6937/6937-improve_cache_with_defaults.patch) by boothby created at 2009-09-20 03:44:48



---

archive/issue_comments_057237.json:
```json
{
    "body": "Bing!",
    "created_at": "2009-09-20T05:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6937#issuecomment-57237",
    "user": "https://github.com/rlmill"
}
```

Bing!



---

archive/issue_events_007162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T20:02:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6937#event-7162"
}
```



---

archive/issue_comments_057238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-22T20:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6937#issuecomment-57238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057239.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.",
    "created_at": "2009-09-27T09:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6937#issuecomment-57239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
