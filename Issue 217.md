# Issue 217: optimize matrix permanents

archive/issues_000217.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/217\n\n",
    "created_at": "2007-01-25T18:58:54Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "optimize matrix permanents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/217",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/217





---

archive/issue_events_000437.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-27T05:19:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/217#event-437"
}
```



---

archive/issue_comments_000961.json:
```json
{
    "body": "There was some work done for QQ and Jaap seems to be working on this for ZZ, so what is the status of this?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-27T05:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There was some work done for QQ and Jaap seems to be working on this for ZZ, so what is the status of this?

Cheers,

Michael



---

archive/issue_comments_000962.json:
```json
{
    "body": "There was track #931 and there is more optimization in the pipeline.\n\nThis will not only work for ZZ, but for all base rings.\n\nI will send a patch (relative to sage-2.8.9) shortly.\n\nJaap",
    "created_at": "2007-10-27T11:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-962",
    "user": "https://github.com/jaapspies"
}
```

There was track #931 and there is more optimization in the pipeline.

This will not only work for ZZ, but for all base rings.

I will send a patch (relative to sage-2.8.9) shortly.

Jaap



---

archive/issue_comments_000963.json:
```json
{
    "body": "With patches:\n\n```\nsage: time dance(7)\nh^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840\nCPU times: user 18.85 s, sys: 0.18 s, total: 19.04 s\nWall time: 19.48\n\n```\n\nin sage-2.8.9:\n\n```\nsage: time dance(7)\nh^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840\nCPU times: user 47.02 s, sys: 1.12 s, total: 48.14 s\nWall time: 48.96\n\n```",
    "created_at": "2007-10-27T11:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-963",
    "user": "https://github.com/jaapspies"
}
```

With patches:

```
sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 18.85 s, sys: 0.18 s, total: 19.04 s
Wall time: 19.48

```

in sage-2.8.9:

```
sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 47.02 s, sys: 1.12 s, total: 48.14 s
Wall time: 48.96

```



---

archive/issue_comments_000964.json:
```json
{
    "body": "optimization relative to #931",
    "created_at": "2007-10-27T12:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-964",
    "user": "https://github.com/jaapspies"
}
```

optimization relative to #931



---

archive/issue_comments_000965.json:
```json
{
    "body": "Attachment [patch_trac217.hg](tarball://root/attachments/some-uuid/ticket217/patch_trac217.hg) by @jaapspies created at 2007-10-27 12:44:21",
    "created_at": "2007-10-27T12:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-965",
    "user": "https://github.com/jaapspies"
}
```

Attachment [patch_trac217.hg](tarball://root/attachments/some-uuid/ticket217/patch_trac217.hg) by @jaapspies created at 2007-10-27 12:44:21



---

archive/issue_events_000438.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-27T19:13:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/217#event-438"
}
```



---

archive/issue_comments_000966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T19:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-966",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_comments_000967.json:
```json
{
    "body": "```\n> As I wrote, I see a lot of cdef Py_ssize_t in for example matrix2.pyx\n> that should be cdef int.\n\n\n> I did change some of them in trac #217, but I think a new trac\n> ticket should be created.\n\n\nAre you sure?    I just had a look at trac #217, and your changing Py_ssize_t\ninto int specifically *introduces* bugs into that code.  E.g., suppose the input\nwere a 1 x 2^33 matrix.  Then you did this in your patch:\n\n-        cdef Py_ssize_t m, n, r\n+        cdef int m, n, r\n\nLower down one has:\n        m = self._nrows\n\tn = self._ncols\n\nNow, instead if the code working like it used to, there will be an overflow,\nand one will get total nonsense.\n\nWilliam\n```",
    "created_at": "2007-10-29T01:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-967",
    "user": "https://github.com/williamstein"
}
```

```
> As I wrote, I see a lot of cdef Py_ssize_t in for example matrix2.pyx
> that should be cdef int.


> I did change some of them in trac #217, but I think a new trac
> ticket should be created.


Are you sure?    I just had a look at trac #217, and your changing Py_ssize_t
into int specifically *introduces* bugs into that code.  E.g., suppose the input
were a 1 x 2^33 matrix.  Then you did this in your patch:

-        cdef Py_ssize_t m, n, r
+        cdef int m, n, r

Lower down one has:
        m = self._nrows
	n = self._ncols

Now, instead if the code working like it used to, there will be an overflow,
and one will get total nonsense.

William
```



---

archive/issue_comments_000968.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-29T01:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-968",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000439.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-29T01:19:23Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/217#event-439"
}
```



---

archive/issue_comments_000969.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-29T01:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-969",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_000970.json:
```json
{
    "body": "This patch is likely fine if the int's are changed back to Py_ssize_t.",
    "created_at": "2007-10-29T01:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-970",
    "user": "https://github.com/williamstein"
}
```

This patch is likely fine if the int's are changed back to Py_ssize_t.



---

archive/issue_comments_000971.json:
```json
{
    "body": "```\nOn 10/29/07, Jaap Spies <j.spies@hccnet.nl> wrote:\n> > Now, instead if the code working like it used to, there will be an overflow,\n> > and one will get total nonsense.\n> >\n> \n> In your example the permanent is just the product of the entries.\n> \n> You deserve to get total nonsense when you try to calculate the permanent\n> of matrices of that size! In practice you know that m and n are small ints.\n> \n> The permanent is a really hard problem. For example the calculation of a 40 x 40\n> (0,1)-matrix with the implemented Ryser algorithm will take forever. Let alone\n> a general matrix of that size! This best known Ryser algorithm is of time O(n^2*2^n).\n> The best we can hope is doing better for certain types of (0,1) matrices.\n\nI am of course well aware of the fact that it would be impractical to compute permanents of large matrices.  But still, writing code that\noverflows and gives nonsense on \"impractical input\" is bad coding\nstyle.  Especially because such code my give nonsense quite quickly.\nThis is almost exactly the same situation in spirit as the situation\nthat leads to people writing insecure code that leads to buffer overflows,\nbecause they don't bother doing proper error checking, since \"nobody\nwould give input like that...\". \n```",
    "created_at": "2007-10-29T14:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-971",
    "user": "https://github.com/williamstein"
}
```

```
On 10/29/07, Jaap Spies <j.spies@hccnet.nl> wrote:
> > Now, instead if the code working like it used to, there will be an overflow,
> > and one will get total nonsense.
> >
> 
> In your example the permanent is just the product of the entries.
> 
> You deserve to get total nonsense when you try to calculate the permanent
> of matrices of that size! In practice you know that m and n are small ints.
> 
> The permanent is a really hard problem. For example the calculation of a 40 x 40
> (0,1)-matrix with the implemented Ryser algorithm will take forever. Let alone
> a general matrix of that size! This best known Ryser algorithm is of time O(n^2*2^n).
> The best we can hope is doing better for certain types of (0,1) matrices.

I am of course well aware of the fact that it would be impractical to compute permanents of large matrices.  But still, writing code that
overflows and gives nonsense on "impractical input" is bad coding
style.  Especially because such code my give nonsense quite quickly.
This is almost exactly the same situation in spirit as the situation
that leads to people writing insecure code that leads to buffer overflows,
because they don't bother doing proper error checking, since "nobody
would give input like that...". 
```



---

archive/issue_comments_000972.json:
```json
{
    "body": "Canged back",
    "created_at": "2007-10-29T20:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-972",
    "user": "https://github.com/jaapspies"
}
```

Canged back



---

archive/issue_comments_000973.json:
```json
{
    "body": "Attachment [patch_trac217_2.hg](tarball://root/attachments/some-uuid/ticket217/patch_trac217_2.hg) by @jaapspies created at 2007-10-29 20:06:17\n\nLesson learned! I hope.\n\nJaap",
    "created_at": "2007-10-29T20:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-973",
    "user": "https://github.com/jaapspies"
}
```

Attachment [patch_trac217_2.hg](tarball://root/attachments/some-uuid/ticket217/patch_trac217_2.hg) by @jaapspies created at 2007-10-29 20:06:17

Lesson learned! I hope.

Jaap



---

archive/issue_comments_000974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000440.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T09:31:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/217#event-440"
}
```



---

archive/issue_comments_000975.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/217#issuecomment-975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0
