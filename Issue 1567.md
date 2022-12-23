# Issue 1567: zn_poly spkg

archive/issues_001567.json:
```json
{
    "body": "Assignee: was\n\nspkg for the `zn_poly` library:\n\nhttp://math.harvard.edu/~dmharvey/zn_poly/releases/zn_poly-0.4.1.spkg\n\nI've tested it on some platforms, but it needs to be tested on more.\n\nSee also\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/9844ce77400e7ed4\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1567\n\n",
    "created_at": "2007-12-19T15:18:45Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "zn_poly spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1567",
    "user": "dmharvey"
}
```
Assignee: was

spkg for the `zn_poly` library:

http://math.harvard.edu/~dmharvey/zn_poly/releases/zn_poly-0.4.1.spkg

I've tested it on some platforms, but it needs to be tested on more.

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/9844ce77400e7ed4


Issue created by migration from https://trac.sagemath.org/ticket/1567





---

archive/issue_comments_009976.json:
```json
{
    "body": "Spkg builds and installs fine for me on 64-bit Ubuntu 7.10.",
    "created_at": "2007-12-22T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9976",
    "user": "mhansen"
}
```

Spkg builds and installs fine for me on 64-bit Ubuntu 7.10.



---

archive/issue_comments_009977.json:
```json
{
    "body": "I would suggest to make this optional first and get some more build reports from a whole bunch of different compilers and build envs. Since a build failure of this spkg will cause problems for many people the reward doesn't outweigh the risk for 2.9.1 and maybe even 2.9.2. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-23T02:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9977",
    "user": "mabshoff"
}
```

I would suggest to make this optional first and get some more build reports from a whole bunch of different compilers and build envs. Since a build failure of this spkg will cause problems for many people the reward doesn't outweigh the risk for 2.9.1 and maybe even 2.9.2. 

Cheers,

Michael



---

archive/issue_comments_009978.json:
```json
{
    "body": "\n```\n[03:27] <dmharvey> i strongly recommend NOT putting zn_poly.spkg into 2.9.1\n[03:28] <mabshoff> :)\n[03:28] <dmharvey> agree with mabshoff it's too early\n```\n",
    "created_at": "2007-12-23T02:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9978",
    "user": "mabshoff"
}
```


```
[03:27] <dmharvey> i strongly recommend NOT putting zn_poly.spkg into 2.9.1
[03:28] <mabshoff> :)
[03:28] <dmharvey> agree with mabshoff it's too early
```




---

archive/issue_comments_009979.json:
```json
{
    "body": "I have added zn_poly-0.4.1.spkg to the experimental spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-23T02:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9979",
    "user": "mabshoff"
}
```

I have added zn_poly-0.4.1.spkg to the experimental spkg repo.

Cheers,

Michael



---

archive/issue_comments_009980.json:
```json
{
    "body": "Compiled fine on my server (debian / xeon).",
    "created_at": "2008-03-16T06:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9980",
    "user": "boothby"
}
```

Compiled fine on my server (debian / xeon).



---

archive/issue_comments_009981.json:
```json
{
    "body": "As the author of the spkg explicitly warns us not to put the spkg in Sage, shouldn't it be moved to another milestone like sage-feature?",
    "created_at": "2008-03-17T23:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9981",
    "user": "malb"
}
```

As the author of the spkg explicitly warns us not to put the spkg in Sage, shouldn't it be moved to another milestone like sage-feature?



---

archive/issue_comments_009982.json:
```json
{
    "body": "I should clarify. This spkg contains some gcc assembly macros. These are borrowed from GMP and NTL, so I think they should be fine, but I haven't personally tested them on all the platforms that they are supposed to support. This is the only reason I want to hold back. If we get positive build reports on all target platforms, then I have no further objections, unless any reviewer is unhappy with the code for some other reason.\n\nI'd like to point out that `zn_poly` has grown substantially since this release. There have been several releases (see http://math.harvard.edu/~dmharvey/zn_poly), all of which have been used in 'real life' by both myself and Andrew Sutherland on a variety of systems. As soon as this spkg is regularly shipped with Sage, I'll be providing constant updated spkgs for each new release. I'm going slow at the moment with the spkgs since this is the first spkg I have made.",
    "created_at": "2008-03-17T23:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9982",
    "user": "dmharvey"
}
```

I should clarify. This spkg contains some gcc assembly macros. These are borrowed from GMP and NTL, so I think they should be fine, but I haven't personally tested them on all the platforms that they are supposed to support. This is the only reason I want to hold back. If we get positive build reports on all target platforms, then I have no further objections, unless any reviewer is unhappy with the code for some other reason.

I'd like to point out that `zn_poly` has grown substantially since this release. There have been several releases (see http://math.harvard.edu/~dmharvey/zn_poly), all of which have been used in 'real life' by both myself and Andrew Sutherland on a variety of systems. As soon as this spkg is regularly shipped with Sage, I'll be providing constant updated spkgs for each new release. I'm going slow at the moment with the spkgs since this is the first spkg I have made.



---

archive/issue_comments_009983.json:
```json
{
    "body": "Builds, tunes, and installs fine for me with Gentoo on Intel P4 and Intel T2060.",
    "created_at": "2008-03-18T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9983",
    "user": "jbmohler"
}
```

Builds, tunes, and installs fine for me with Gentoo on Intel P4 and Intel T2060.



---

archive/issue_comments_009984.json:
```json
{
    "body": "Hi David, \n\nit looks like the time is right now to include this spkg in Sage. My understanding is that we also need this for #1568. So I can you start a thread on sage-devel that requests a vote for inclusion? You should do that by describing what the spkg does, how large it is and what the benefits are. I am sure it will be included, but that is the process we decided upon and I am sure you saw the SQLAlchemy vote a couple days ago.\n\nI will test this spkg and review its layout for conformance later today.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T20:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9984",
    "user": "mabshoff"
}
```

Hi David, 

it looks like the time is right now to include this spkg in Sage. My understanding is that we also need this for #1568. So I can you start a thread on sage-devel that requests a vote for inclusion? You should do that by describing what the spkg does, how large it is and what the benefits are. I am sure it will be included, but that is the process we decided upon and I am sure you saw the SQLAlchemy vote a couple days ago.

I will test this spkg and review its layout for conformance later today.

Cheers,

Michael



---

archive/issue_comments_009985.json:
```json
{
    "body": "The vote to get this spkg in is at\n\nhttps://groups.google.com/group/sage-devel/t/7a1b4a6979555524\n\nSince everybody voted to get it in and about 24 hours have elapsed I am considering this spkg voted in.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T02:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9985",
    "user": "mabshoff"
}
```

The vote to get this spkg in is at

https://groups.google.com/group/sage-devel/t/7a1b4a6979555524

Since everybody voted to get it in and about 24 hours have elapsed I am considering this spkg voted in.

Cheers,

Michael



---

archive/issue_comments_009986.json:
```json
{
    "body": "I posted a slightly updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha0/zn_poly-0.4.1.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T02:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9986",
    "user": "mabshoff"
}
```

I posted a slightly updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha0/zn_poly-0.4.1.p0.spkg

Cheers,

Michael



---

archive/issue_comments_009987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T02:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9987",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009988.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T02:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9988",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_comments_009989.json:
```json
{
    "body": "Oh yeah, positive review obviously :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T04:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1567#issuecomment-9989",
    "user": "mabshoff"
}
```

Oh yeah, positive review obviously :)

Cheers,

Michael
