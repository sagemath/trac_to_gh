# Issue 4407: magma -- painful scalability issue with parser and interface

archive/issues_004407.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: a = magma('\"%s\"'%('n'*1000000))\n[[works instantly, uses almost no memeory]]\nsage: magma.GetMemoryUsage()\n15728664\n```\nNow do the same, but with just 10 times as much input (be ready to kill magma processes).  This will uses several GIGABYTES.\n\n```\nsage: a = magma('\"%s\"'%('n'*10000000))\n^C^Z\n```\n\nThis is probably some major magma parser issue.  We should nail down the bound, then either:\n   (1) find some clever way to program around it,\n   (2) report it as a bug to Allan Steel,\n   (3) give an error message instead of blowing up people's computers\n\nIssue created by migration from https://trac.sagemath.org/ticket/4407\n\n",
    "closed_at": "2008-10-31T00:20:53Z",
    "created_at": "2008-10-31T00:01:27Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "magma -- painful scalability issue with parser and interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4407",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: a = magma('"%s"'%('n'*1000000))
[[works instantly, uses almost no memeory]]
sage: magma.GetMemoryUsage()
15728664
```
Now do the same, but with just 10 times as much input (be ready to kill magma processes).  This will uses several GIGABYTES.

```
sage: a = magma('"%s"'%('n'*10000000))
^C^Z
```

This is probably some major magma parser issue.  We should nail down the bound, then either:
   (1) find some clever way to program around it,
   (2) report it as a bug to Allan Steel,
   (3) give an error message instead of blowing up people's computers

Issue created by migration from https://trac.sagemath.org/ticket/4407





---

archive/issue_comments_032346.json:
```json
{
    "body": "```\n17:11 < wstein-4399> so this happens on OS X in magma 2.14\n17:12 < wstein-4399> it does *not* happen on magma 2.13 on linux\n17:12 < mhansen> If only you had a control group :-)\n17:13 < mabshoff> Interesting\n17:13 < mhansen> I'd guess it's probably the OS X vs. Linux as opposed to the \n                 version though.\n17:13 < mabshoff> Well, the issue has also popped up on Linux boxen IIRC.\n17:13 < mabshoff> mhansen: can you review #2462?\n17:13 < wstein-4399> On magma 2.14 on my linux laptop (that tiny acer) it \n                     doesn't happen.\n17:14 < wstein-4399> so I'm thinking it is yet another bug in magma on osx.\n\n17:15 < wstein-4399> and definitely just a bug in magma.\n17:15 < wstein-4399> Let's close the ticket as invalid.  There's nothing to be \n                     done\n17:15 < mabshoff> I am surprised their OSX version is so buggy.\n17:15 < mabshoff> ok\n17:15 < wstein-4399> from the point of sage, and magma isn't (yet) a component \n                     of sage.\n17:15 < mabshoff> :)\n```",
    "created_at": "2008-10-31T00:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4407#issuecomment-32346",
    "user": "https://github.com/williamstein"
}
```

```
17:11 < wstein-4399> so this happens on OS X in magma 2.14
17:12 < wstein-4399> it does *not* happen on magma 2.13 on linux
17:12 < mhansen> If only you had a control group :-)
17:13 < mabshoff> Interesting
17:13 < mhansen> I'd guess it's probably the OS X vs. Linux as opposed to the 
                 version though.
17:13 < mabshoff> Well, the issue has also popped up on Linux boxen IIRC.
17:13 < mabshoff> mhansen: can you review #2462?
17:13 < wstein-4399> On magma 2.14 on my linux laptop (that tiny acer) it 
                     doesn't happen.
17:14 < wstein-4399> so I'm thinking it is yet another bug in magma on osx.

17:15 < wstein-4399> and definitely just a bug in magma.
17:15 < wstein-4399> Let's close the ticket as invalid.  There's nothing to be 
                     done
17:15 < mabshoff> I am surprised their OSX version is so buggy.
17:15 < mabshoff> ok
17:15 < wstein-4399> from the point of sage, and magma isn't (yet) a component 
                     of sage.
17:15 < mabshoff> :)
```



---

archive/issue_comments_032347.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-10-31T00:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4407#issuecomment-32347",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_events_009956.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-10-31T00:20:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4407",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4407#event-9956"
}
```



---

archive/issue_events_009957.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T00:22:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4407",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4407#event-9957"
}
```



---

archive/issue_comments_032348.json:
```json
{
    "body": "cantfix :)",
    "created_at": "2008-10-31T00:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4407#issuecomment-32348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

cantfix :)
