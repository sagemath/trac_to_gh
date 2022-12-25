# Issue 1567: zn_poly spkg

archive/issues_001567.json:
```json
{
    "body": "Assignee: @williamstein\n\nspkg for the `zn_poly` library:\n\nhttp://math.harvard.edu/~dmharvey/zn_poly/releases/zn_poly-0.4.1.spkg\n\nI've tested it on some platforms, but it needs to be tested on more.\n\nSee also\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/9844ce77400e7ed4\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1567\n\n",
    "created_at": "2007-12-19T15:18:45Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "zn_poly spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1567",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

spkg for the `zn_poly` library:

http://math.harvard.edu/~dmharvey/zn_poly/releases/zn_poly-0.4.1.spkg

I've tested it on some platforms, but it needs to be tested on more.

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/9844ce77400e7ed4


Issue created by migration from https://trac.sagemath.org/ticket/1567





---

archive/issue_events_003921.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-19T16:58:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1567#event-3921"
}
```



---

archive/issue_comments_009950.json:
```json
{
    "body": "Spkg builds and installs fine for me on 64-bit Ubuntu 7.10.",
    "created_at": "2007-12-22T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9950",
    "user": "https://github.com/mwhansen"
}
```

Spkg builds and installs fine for me on 64-bit Ubuntu 7.10.



---

archive/issue_comments_009951.json:
```json
{
    "body": "I would suggest to make this optional first and get some more build reports from a whole bunch of different compilers and build envs. Since a build failure of this spkg will cause problems for many people the reward doesn't outweigh the risk for 2.9.1 and maybe even 2.9.2. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-23T02:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9951",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I would suggest to make this optional first and get some more build reports from a whole bunch of different compilers and build envs. Since a build failure of this spkg will cause problems for many people the reward doesn't outweigh the risk for 2.9.1 and maybe even 2.9.2. 

Cheers,

Michael



---

archive/issue_comments_009952.json:
```json
{
    "body": "```\n[03:27] <dmharvey> i strongly recommend NOT putting zn_poly.spkg into 2.9.1\n[03:28] <mabshoff> :)\n[03:28] <dmharvey> agree with mabshoff it's too early\n```",
    "created_at": "2007-12-23T02:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9952",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
[03:27] <dmharvey> i strongly recommend NOT putting zn_poly.spkg into 2.9.1
[03:28] <mabshoff> :)
[03:28] <dmharvey> agree with mabshoff it's too early
```



---

archive/issue_comments_009953.json:
```json
{
    "body": "I have added zn_poly-0.4.1.spkg to the experimental spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-23T02:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9953",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have added zn_poly-0.4.1.spkg to the experimental spkg repo.

Cheers,

Michael



---

archive/issue_events_003922.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T04:59:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1567#event-3922"
}
```



---

archive/issue_events_003923.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T04:59:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1567#event-3923"
}
```



---

archive/issue_comments_009954.json:
```json
{
    "body": "Compiled fine on my server (debian / xeon).",
    "created_at": "2008-03-16T06:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9954",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Compiled fine on my server (debian / xeon).



---

archive/issue_comments_009955.json:
```json
{
    "body": "As the author of the spkg explicitly warns us not to put the spkg in Sage, shouldn't it be moved to another milestone like sage-feature?",
    "created_at": "2008-03-17T23:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9955",
    "user": "https://github.com/malb"
}
```

As the author of the spkg explicitly warns us not to put the spkg in Sage, shouldn't it be moved to another milestone like sage-feature?



---

archive/issue_comments_009956.json:
```json
{
    "body": "I should clarify. This spkg contains some gcc assembly macros. These are borrowed from GMP and NTL, so I think they should be fine, but I haven't personally tested them on all the platforms that they are supposed to support. This is the only reason I want to hold back. If we get positive build reports on all target platforms, then I have no further objections, unless any reviewer is unhappy with the code for some other reason.\n\nI'd like to point out that `zn_poly` has grown substantially since this release. There have been several releases (see http://math.harvard.edu/~dmharvey/zn_poly), all of which have been used in 'real life' by both myself and Andrew Sutherland on a variety of systems. As soon as this spkg is regularly shipped with Sage, I'll be providing constant updated spkgs for each new release. I'm going slow at the moment with the spkgs since this is the first spkg I have made.",
    "created_at": "2008-03-17T23:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9956",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I should clarify. This spkg contains some gcc assembly macros. These are borrowed from GMP and NTL, so I think they should be fine, but I haven't personally tested them on all the platforms that they are supposed to support. This is the only reason I want to hold back. If we get positive build reports on all target platforms, then I have no further objections, unless any reviewer is unhappy with the code for some other reason.

I'd like to point out that `zn_poly` has grown substantially since this release. There have been several releases (see http://math.harvard.edu/~dmharvey/zn_poly), all of which have been used in 'real life' by both myself and Andrew Sutherland on a variety of systems. As soon as this spkg is regularly shipped with Sage, I'll be providing constant updated spkgs for each new release. I'm going slow at the moment with the spkgs since this is the first spkg I have made.



---

archive/issue_comments_009957.json:
```json
{
    "body": "Builds, tunes, and installs fine for me with Gentoo on Intel P4 and Intel T2060.",
    "created_at": "2008-03-18T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9957",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Builds, tunes, and installs fine for me with Gentoo on Intel P4 and Intel T2060.



---

archive/issue_comments_009958.json:
```json
{
    "body": "Hi David, \n\nit looks like the time is right now to include this spkg in Sage. My understanding is that we also need this for #1568. So I can you start a thread on sage-devel that requests a vote for inclusion? You should do that by describing what the spkg does, how large it is and what the benefits are. I am sure it will be included, but that is the process we decided upon and I am sure you saw the SQLAlchemy vote a couple days ago.\n\nI will test this spkg and review its layout for conformance later today.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T20:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi David, 

it looks like the time is right now to include this spkg in Sage. My understanding is that we also need this for #1568. So I can you start a thread on sage-devel that requests a vote for inclusion? You should do that by describing what the spkg does, how large it is and what the benefits are. I am sure it will be included, but that is the process we decided upon and I am sure you saw the SQLAlchemy vote a couple days ago.

I will test this spkg and review its layout for conformance later today.

Cheers,

Michael



---

archive/issue_comments_009959.json:
```json
{
    "body": "The vote to get this spkg in is at\n\nhttps://groups.google.com/group/sage-devel/t/7a1b4a6979555524\n\nSince everybody voted to get it in and about 24 hours have elapsed I am considering this spkg voted in.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T02:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9959",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The vote to get this spkg in is at

https://groups.google.com/group/sage-devel/t/7a1b4a6979555524

Since everybody voted to get it in and about 24 hours have elapsed I am considering this spkg voted in.

Cheers,

Michael



---

archive/issue_comments_009960.json:
```json
{
    "body": "I posted a slightly updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha0/zn_poly-0.4.1.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T02:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9960",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I posted a slightly updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha0/zn_poly-0.4.1.p0.spkg

Cheers,

Michael



---

archive/issue_comments_009961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T02:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003924.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-20T02:52:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1567#event-3924"
}
```



---

archive/issue_comments_009962.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T02:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_comments_009963.json:
```json
{
    "body": "Oh yeah, positive review obviously :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T04:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9963",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oh yeah, positive review obviously :)

Cheers,

Michael
