# Issue 3255: Add support for generic backtracking algorithms

archive/issues_003255.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3255\n\n",
    "created_at": "2008-05-19T13:31:44Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "Add support for generic backtracking algorithms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3255",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/3255





---

archive/issue_comments_022470.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-19T13:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22470",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022471.json:
```json
{
    "body": "This patch should be refereed by someone else but it seems like an extremely useful direction of work, so I wanted to help out in a small way. I applied this to sage 3.0.2.alpha1. It applies cleanly and has the same sage -testall failures that the unpatched build has (doctest failures). In other words, this patch \"passed\" sage -testall.",
    "created_at": "2008-05-19T17:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22471",
    "user": "https://github.com/wdjoyner"
}
```

This patch should be refereed by someone else but it seems like an extremely useful direction of work, so I wanted to help out in a small way. I applied this to sage 3.0.2.alpha1. It applies cleanly and has the same sage -testall failures that the unpatched build has (doctest failures). In other words, this patch "passed" sage -testall.



---

archive/issue_comments_022472.json:
```json
{
    "body": "From http://blog.phasing.org/?p=6, i.e. Mike Hansen's new blog:\n\nAnother place that the comes in handy is in the generation of non-attacking fillings of augmented lattice diagrams. These are used to compute the non-symmetric Macdonald polynomials in type A.\n\nHere are some timings of the new code.\n\nBefore:\n\n```\nsage: time Permutations(8, avoiding=[[1,3,2],[2,1,3]]).count()\nCPU times: user 11.44 s, sys: 0.01 s, total: 11.45 s\nWall time: 12.35\n128\nsage: time NonattackingFillings([3,2,1,2]).count() \nCPU times: user 17.02 s, sys: 0.02 s, total: 17.04 s\nWall time: 17.36\n4\nsage: time NonattackingFillings([1,2,3,2]).count() \nCPU times: user 16.78 s, sys: 0.00 s, total: 16.78 s\nWall time: 16.80\n24\n```\n\nAfter:\n\n```\nsage: time Permutations(8, avoiding=[[1,3,2],[2,1,3]]).count()\nCPU times: user 1.58 s, sys: 0.00 s, total: 1.58 s\nWall time: 1.58\n128\nsage: sage: time NonattackingFillings([3,2,1,2]).count() \nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n4\nsage: sage: time NonattackingFillings([1,2,3,2]).count() \nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n24\n```\n",
    "created_at": "2008-05-19T19:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

From http://blog.phasing.org/?p=6, i.e. Mike Hansen's new blog:

Another place that the comes in handy is in the generation of non-attacking fillings of augmented lattice diagrams. These are used to compute the non-symmetric Macdonald polynomials in type A.

Here are some timings of the new code.

Before:

```
sage: time Permutations(8, avoiding=[[1,3,2],[2,1,3]]).count()
CPU times: user 11.44 s, sys: 0.01 s, total: 11.45 s
Wall time: 12.35
128
sage: time NonattackingFillings([3,2,1,2]).count() 
CPU times: user 17.02 s, sys: 0.02 s, total: 17.04 s
Wall time: 17.36
4
sage: time NonattackingFillings([1,2,3,2]).count() 
CPU times: user 16.78 s, sys: 0.00 s, total: 16.78 s
Wall time: 16.80
24
```

After:

```
sage: time Permutations(8, avoiding=[[1,3,2],[2,1,3]]).count()
CPU times: user 1.58 s, sys: 0.00 s, total: 1.58 s
Wall time: 1.58
128
sage: sage: time NonattackingFillings([3,2,1,2]).count() 
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
4
sage: sage: time NonattackingFillings([1,2,3,2]).count() 
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
24
```




---

archive/issue_comments_022473.json:
```json
{
    "body": "I'm giving this a tentative positive review. Tentative only because my knowledge of these algorithms and methods isn't complete. Someone else should look this over!\n\nThat said, the basic backtracker class is very simple and looks good. Fast algorithms for pattern avoidance in permutations are very desirable.",
    "created_at": "2008-05-23T05:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22473",
    "user": "https://github.com/dandrake"
}
```

I'm giving this a tentative positive review. Tentative only because my knowledge of these algorithms and methods isn't complete. Someone else should look this over!

That said, the basic backtracker class is very simple and looks good. Fast algorithms for pattern avoidance in permutations are very desirable.



---

archive/issue_comments_022474.json:
```json
{
    "body": "Attachment [3255.patch](tarball://root/attachments/some-uuid/ticket3255/3255.patch) by @dandrake created at 2008-05-26 03:17:15\n\nI'm changing this to a positive review because I now understand this patch well enough to have written code which uses it, and it makes things super easy and fast. This should get into Sage right away.\n\nHere's the code for making Dyck paths. It may not be the fastest or best way to do it, but it literally worked the very first time I loaded it.\n\n```\nclass DyckPaths(GenericBacktracker):\n  def __init__(self, n):\n    GenericBacktracker.__init__(self, [], (0, 0))\n    self._n = n\n\n  def _rec(self, path, state):\n    if is_odd(self._n):\n      return\n\n    len, ht = state\n\n    if len < self._n:\n      # if length is less than n, we need to keep building the path, so\n      # new length will be 1 longer, and we don't yield the path yet.\n      newlen = len + 1\n\n      # if we're not touching the x-axis, we can yield a path with a\n      # downstep at the end\n      if ht > 0:\n        yield path + [-1], (newlen, ht - 1), False\n\n      # if the path isn't too high, it can also take an upstep\n      if ht < (self._n - len):\n        yield path + [1], (newlen, ht + 1), False\n    else:\n      # if length is n, set state to None so we stop trying to make new\n      # paths, and yield what we've got\n      yield path, None, True\n```\n\n\nNow, let's say you want Dyck paths with no peaks at even height. (This is an example I came up with off the top off my head in IRC; unsurprisingly, [the number of such paths is already known](http://www.ams.org/mathscinet-getitem?mr=2004242).) You only need to change the \"`if ht > 0`\" block to the following:\n\n```\n      # if we're not touching the x-axis, we can yield a path with a\n      # downstep at the end, provided we don't make a peak at even\n      # height\n      if ht > 0:\n        if is_odd(ht) or (path[-1] != 1):\n          yield path + [-1], (newlen, ht - 1), False\n```\n\nThis also worked the very first time I tried it!",
    "created_at": "2008-05-26T03:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22474",
    "user": "https://github.com/dandrake"
}
```

Attachment [3255.patch](tarball://root/attachments/some-uuid/ticket3255/3255.patch) by @dandrake created at 2008-05-26 03:17:15

I'm changing this to a positive review because I now understand this patch well enough to have written code which uses it, and it makes things super easy and fast. This should get into Sage right away.

Here's the code for making Dyck paths. It may not be the fastest or best way to do it, but it literally worked the very first time I loaded it.

```
class DyckPaths(GenericBacktracker):
  def __init__(self, n):
    GenericBacktracker.__init__(self, [], (0, 0))
    self._n = n

  def _rec(self, path, state):
    if is_odd(self._n):
      return

    len, ht = state

    if len < self._n:
      # if length is less than n, we need to keep building the path, so
      # new length will be 1 longer, and we don't yield the path yet.
      newlen = len + 1

      # if we're not touching the x-axis, we can yield a path with a
      # downstep at the end
      if ht > 0:
        yield path + [-1], (newlen, ht - 1), False

      # if the path isn't too high, it can also take an upstep
      if ht < (self._n - len):
        yield path + [1], (newlen, ht + 1), False
    else:
      # if length is n, set state to None so we stop trying to make new
      # paths, and yield what we've got
      yield path, None, True
```


Now, let's say you want Dyck paths with no peaks at even height. (This is an example I came up with off the top off my head in IRC; unsurprisingly, [the number of such paths is already known](http://www.ams.org/mathscinet-getitem?mr=2004242).) You only need to change the "`if ht > 0`" block to the following:

```
      # if we're not touching the x-axis, we can yield a path with a
      # downstep at the end, provided we don't make a peak at even
      # height
      if ht > 0:
        if is_odd(ht) or (path[-1] != 1):
          yield path + [-1], (newlen, ht - 1), False
```

This also worked the very first time I tried it!



---

archive/issue_comments_022475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-26T05:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22475",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003473.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-26T05:19:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3255#event-3473"
}
```



---

archive/issue_comments_022476.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-26T05:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22476",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_022477.json:
```json
{
    "body": "Hello sage-combinat-devel, \n\nI see that the CC notification works. So if you open/see a ticket that is relevant to sage-combinat please add \"sage-combinat\" in the CC field at the bottom of the ticket page. In case there already are other accounts listed just append it and separate entries by a comma. If you want to remove notification from a ticket just remove \"sage-combinat\" form the CC field. \n\nAs is you will get email notifications on all changes, including comments, status changes and so on. The only action not resulting in an email is the attachment of a patch.\n\nThis specific ticket is Mike Hansen's generic backtracking code which has been merged into Sage 3.0.3.alpha0.\n\nLet me know if there are any questions.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-26T05:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello sage-combinat-devel, 

I see that the CC notification works. So if you open/see a ticket that is relevant to sage-combinat please add "sage-combinat" in the CC field at the bottom of the ticket page. In case there already are other accounts listed just append it and separate entries by a comma. If you want to remove notification from a ticket just remove "sage-combinat" form the CC field. 

As is you will get email notifications on all changes, including comments, status changes and so on. The only action not resulting in an email is the attachment of a patch.

This specific ticket is Mike Hansen's generic backtracking code which has been merged into Sage 3.0.3.alpha0.

Let me know if there are any questions.

Cheers,

Michael



---

archive/issue_comments_022478.json:
```json
{
    "body": "Ok, this message should show up on sage-combinat-commits.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-26T05:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, this message should show up on sage-combinat-commits.

Cheers,

Michael



---

archive/issue_comments_022479.json:
```json
{
    "body": "Testing sage-combinat-commits.",
    "created_at": "2008-05-26T06:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3255#issuecomment-22479",
    "user": "https://github.com/mwhansen"
}
```

Testing sage-combinat-commits.
