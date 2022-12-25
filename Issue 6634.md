# Issue 6634: biopython 1.49b broken with python-2.6

archive/issues_006634.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: biopython, bioinformatics\n\nBiopython 1.49b doesn't install with python-2.6, so we should update the package.  Currently biopython is at 1.51-beta, for which a spkg is provided, but we should switch to 1.51 as soon as it comes out since it will have significant improvements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6634\n\n",
    "created_at": "2009-07-27T02:44:06Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "biopython 1.49b broken with python-2.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6634",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: tbd

Keywords: biopython, bioinformatics

Biopython 1.49b doesn't install with python-2.6, so we should update the package.  Currently biopython is at 1.51-beta, for which a spkg is provided, but we should switch to 1.51 as soon as it comes out since it will have significant improvements.

Issue created by migration from https://trac.sagemath.org/ticket/6634





---

archive/issue_comments_054256.json:
```json
{
    "body": "Temporary spkg to fix this, until 1.51 comes out, is at:\nhttp://www.d.umn.edu/~mhampton/biopython-1.51b.spkg",
    "created_at": "2009-07-27T02:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Temporary spkg to fix this, until 1.51 comes out, is at:
http://www.d.umn.edu/~mhampton/biopython-1.51b.spkg



---

archive/issue_comments_054257.json:
```json
{
    "body": "1.51b spkg installs cleanly and works fine with sage 4.1 on my linux kubuntu 9.04",
    "created_at": "2009-07-27T17:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54257",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkeller"
}
```

1.51b spkg installs cleanly and works fine with sage 4.1 on my linux kubuntu 9.04



---

archive/issue_comments_054258.json:
```json
{
    "body": "I have made a spkg for biopython-1.51, which was released today:\n\nhttp://sage.math.washington.edu/home/mhampton/biopython-1.51.spkg\n\nRunning the test suite gives some errors, but some of these are due to missing optional components.  I am inquiring about these on the biopython development list, but I don't think any of them are important enough to block this as an optional spkg.",
    "created_at": "2009-08-17T15:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54258",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I have made a spkg for biopython-1.51, which was released today:

http://sage.math.washington.edu/home/mhampton/biopython-1.51.spkg

Running the test suite gives some errors, but some of these are due to missing optional components.  I am inquiring about these on the biopython development list, but I don't think any of them are important enough to block this as an optional spkg.



---

archive/issue_comments_054259.json:
```json
{
    "body": "tkeller,\n\nCan you review this new package?  Besides testing installation, if you check that the spkg-install and SPKG.txt make sense then you can change the heading to [with spkg, positive review] and this can go into the optional packages.\n\nIn case you don't know, spkgs are just .tar.bz files with the extension renamed.  I usually unpack a temporary copy somewhere other than my sage folder in order to take a look when reviewing.\n\n-Marshall",
    "created_at": "2009-08-18T14:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

tkeller,

Can you review this new package?  Besides testing installation, if you check that the spkg-install and SPKG.txt make sense then you can change the heading to [with spkg, positive review] and this can go into the optional packages.

In case you don't know, spkgs are just .tar.bz files with the extension renamed.  I usually unpack a temporary copy somewhere other than my sage folder in order to take a look when reviewing.

-Marshall



---

archive/issue_comments_054260.json:
```json
{
    "body": "Marshall,\n\nI had started looking at this yesterday, so I just finished it now.  It builds successfully on sage.math, 32-bit Linux and 32-bit OSX 10.5.  Let's get it in!\n\nOne comment: if you happen to have some toy (or serious) Sage code using biopython, I strongly encourage you to get it into Sage so that we have at least some examples.",
    "created_at": "2009-08-19T12:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54260",
    "user": "https://github.com/aghitza"
}
```

Marshall,

I had started looking at this yesterday, so I just finished it now.  It builds successfully on sage.math, 32-bit Linux and 32-bit OSX 10.5.  Let's get it in!

One comment: if you happen to have some toy (or serious) Sage code using biopython, I strongly encourage you to get it into Sage so that we have at least some examples.



---

archive/issue_comments_054261.json:
```json
{
    "body": "Is there a reason why biopython-1.51.spkg is not under revision control?\n\n```\n[mvngu@mod mvngu]$ tar -jxf biopython-1.51.spkg \n[mvngu@mod mvngu]$ cd biopython-1.51/\n[mvngu@mod biopython-1.51]$ hg st\nabort: There is no Mercurial repository here (.hg not found)!\n```\n",
    "created_at": "2009-09-02T09:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54261",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Is there a reason why biopython-1.51.spkg is not under revision control?

```
[mvngu@mod mvngu]$ tar -jxf biopython-1.51.spkg 
[mvngu@mod mvngu]$ cd biopython-1.51/
[mvngu@mod biopython-1.51]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
```




---

archive/issue_events_006872.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-11T18:13:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6634#event-6872"
}
```



---

archive/issue_comments_054262.json:
```json
{
    "body": "Merged in the optional packages repository at\n\nhttp://www.sagemath.org/packages/optional/\n\nThe updated spkg is available at\n\nhttp://www.sagemath.org/packages/optional/biopython-1.51.spkg",
    "created_at": "2009-09-11T18:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in the optional packages repository at

http://www.sagemath.org/packages/optional/

The updated spkg is available at

http://www.sagemath.org/packages/optional/biopython-1.51.spkg



---

archive/issue_comments_054263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-11T18:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6634#issuecomment-54263",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
