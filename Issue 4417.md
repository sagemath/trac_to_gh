# Issue 4417: [with patch, positive review] fix steenrod algebra 'optional' doctest

archive/issues_004417.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nKeywords: steenrod algebra\n\nIn [response to mabshoff](http://groups.google.com/group/sage-devel/browse_frm/thread/be920ff2cef4a376), here is a patch to fix the failed 'optional' doctest in steenrod_algebra.py.  I don't actually know why this was only caught with optional; perhaps because the words 'package', 'long', and 'optional' appear somewhere in the file (although they're nowhere near each other or this test)?  Anyway, I fixed the doctest to be what it should be (i.e., what Sage was computing, which is also what I get by hand), and I changed 'package' to 'module' everywhere so that sage -t will test the same things as sage -t -optional.\n\n  John\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4417\n\n",
    "closed_at": "2008-11-01T21:06:07Z",
    "created_at": "2008-11-01T02:39:53Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] fix steenrod algebra 'optional' doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4417",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Keywords: steenrod algebra

In [response to mabshoff](http://groups.google.com/group/sage-devel/browse_frm/thread/be920ff2cef4a376), here is a patch to fix the failed 'optional' doctest in steenrod_algebra.py.  I don't actually know why this was only caught with optional; perhaps because the words 'package', 'long', and 'optional' appear somewhere in the file (although they're nowhere near each other or this test)?  Anyway, I fixed the doctest to be what it should be (i.e., what Sage was computing, which is also what I get by hand), and I changed 'package' to 'module' everywhere so that sage -t will test the same things as sage -t -optional.

  John



Issue created by migration from https://trac.sagemath.org/ticket/4417





---

archive/issue_comments_032422.json:
```json
{
    "body": "Attachment [steenrod-optional.patch](tarball://root/attachments/some-uuid/ticket4417/steenrod-optional.patch) by mabshoff created at 2008-11-01 02:47:34\n\nHi John,\n\nthis one was a really strange doctest failure and I am glad you fixed it.\n\nOne thing I noticed while looking at the file was that you use constructs like\n\n```\nsage: B = SteenrodAlgebra(2, 'adem')\n```\nwhich seem very un-Sagish, i.e. one would use some (optional) keyword in the constructor like\n\n```\nsage: B = SteenrodAlgebra(2, foo=adem)\n```\nThis certainly should not addressed via this ticket, but might be something that should be discussed on [sage-devel].\n\nCheers,\n\nMichael\n\nPS: I will test and review this patch shortly.",
    "created_at": "2008-11-01T02:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4417#issuecomment-32422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [steenrod-optional.patch](tarball://root/attachments/some-uuid/ticket4417/steenrod-optional.patch) by mabshoff created at 2008-11-01 02:47:34

Hi John,

this one was a really strange doctest failure and I am glad you fixed it.

One thing I noticed while looking at the file was that you use constructs like

```
sage: B = SteenrodAlgebra(2, 'adem')
```
which seem very un-Sagish, i.e. one would use some (optional) keyword in the constructor like

```
sage: B = SteenrodAlgebra(2, foo=adem)
```
This certainly should not addressed via this ticket, but might be something that should be discussed on [sage-devel].

Cheers,

Michael

PS: I will test and review this patch shortly.



---

archive/issue_comments_032423.json:
```json
{
    "body": "```\nSteenrodAlgebra(5, 'adem')\n```\ncould be changed to\n\n```\nSteenrodAlgebra(5, basis='adem')\n```\n(These both work right now; it would just be a matter of changing the documentation to reflect the preferred choice, if the second choice is better.)  I don't know how to implement something like\n\n```\nSteenrodAlgebra(5, basis=adem)\n```\nthough, without importing `adem` into the global name space.\n\n  John",
    "created_at": "2008-11-01T03:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4417#issuecomment-32423",
    "user": "https://github.com/jhpalmieri"
}
```

```
SteenrodAlgebra(5, 'adem')
```
could be changed to

```
SteenrodAlgebra(5, basis='adem')
```
(These both work right now; it would just be a matter of changing the documentation to reflect the preferred choice, if the second choice is better.)  I don't know how to implement something like

```
SteenrodAlgebra(5, basis=adem)
```
though, without importing `adem` into the global name space.

  John



---

archive/issue_comments_032424.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> {{{\n> SteenrodAlgebra(5, 'adem')\n> }}}\n> could be changed to\n> \n> ```\n> SteenrodAlgebra(5, basis='adem')\n> ```\n> (These both work right now; it would just be a matter of changing the documentation to reflect the preferred choice, if the second choice is better.)  \n\n\nThat sounds good to me. I would also prefer \"foo\" and not 'foo' for strings, but that is probably personal preference.\n\n> I don't know how to implement something like\n> \n> ```\n> SteenrodAlgebra(5, basis=adem)\n> ```\n> though, without importing `adem` into the global name space.\n> \n>   John\n> \n\n\nOk.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-01T21:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4417#issuecomment-32424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 jhpalmieri]:
> {{{
> SteenrodAlgebra(5, 'adem')
> }}}
> could be changed to
> 
> ```
> SteenrodAlgebra(5, basis='adem')
> ```
> (These both work right now; it would just be a matter of changing the documentation to reflect the preferred choice, if the second choice is better.)  


That sounds good to me. I would also prefer "foo" and not 'foo' for strings, but that is probably personal preference.

> I don't know how to implement something like
> 
> ```
> SteenrodAlgebra(5, basis=adem)
> ```
> though, without importing `adem` into the global name space.
> 
>   John
> 


Ok.

Cheers,

Michael



---

archive/issue_comments_032425.json:
```json
{
    "body": "Positive review, the patch fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-01T21:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4417#issuecomment-32425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review, the patch fixes the issue.

Cheers,

Michael



---

archive/issue_comments_032426.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-01T21:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4417#issuecomment-32426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_events_009984.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-01T21:06:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4417#event-9984"
}
```



---

archive/issue_comments_032427.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-01T21:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4417#issuecomment-32427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
