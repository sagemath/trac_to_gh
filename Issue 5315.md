# Issue 5315: Fix MPIR.spkg build on more OSX MacIntel boxen

archive/issues_005315.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere is a known problem with PIC enabled MPIR code on 32 bit OSX when the CPU is capable of 64 bits. To work around that we delete some files, but there are some left that are used on older Macs:\n\n```\np6/mode1o.asm\np6/dive_1.asm\npentium/hamdist.asm\npentium/mod_1.asm\npentium/popcount.asm\npentium/mode1o.asm\npentium/dive_1.asm\n```\n\nDeleting them on demand will fix the build. See also the thread at\n\n http://groups.google.com/group/sage-devel/browse_thread/thread/88c084b8cd828ac6\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5315\n\n",
    "created_at": "2009-02-20T05:33:37Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Fix MPIR.spkg build on more OSX MacIntel boxen",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5315",
    "user": "mabshoff"
}
```
Assignee: mabshoff

There is a known problem with PIC enabled MPIR code on 32 bit OSX when the CPU is capable of 64 bits. To work around that we delete some files, but there are some left that are used on older Macs:

```
p6/mode1o.asm
p6/dive_1.asm
pentium/hamdist.asm
pentium/mod_1.asm
pentium/popcount.asm
pentium/mode1o.asm
pentium/dive_1.asm
```

Deleting them on demand will fix the build. See also the thread at

 http://groups.google.com/group/sage-devel/browse_thread/thread/88c084b8cd828ac6

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5315





---

archive/issue_comments_040938.json:
```json
{
    "body": "The spkg at \n\n http://sage.math.washington.edu/home/mabshoff/SPKG/gmp-mpir-0.9.spkg\n\nought to fix the problem. I have asked the reported of the original issue to test and report back.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T13:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5315#issuecomment-40938",
    "user": "mabshoff"
}
```

The spkg at 

 http://sage.math.washington.edu/home/mabshoff/SPKG/gmp-mpir-0.9.spkg

ought to fix the problem. I have asked the reported of the original issue to test and report back.

Cheers,

Michael



---

archive/issue_comments_040939.json:
```json
{
    "body": "Positive review by proxy from Mark:\n\n```\n> I had a class this morning and have only just started the build.\n> It is running now and I can tell you that it has definitely made it\n> past this specific problem.\n\nOk, this is a positive review from you in my eyes for this problem and\nwe can merge the spkg. I will ask someone else to take another look,\nbut I can assure you I did a very clean checkin :)\n\n>  It should still take a couple of hours\n> to complete.  I'll report back when I've got the finished product.\n\nCool, let me know if anything else blows up for you. I would assume\n3.3.rc3 is out before your build finishes.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T16:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5315#issuecomment-40939",
    "user": "mabshoff"
}
```

Positive review by proxy from Mark:

```
> I had a class this morning and have only just started the build.
> It is running now and I can tell you that it has definitely made it
> past this specific problem.

Ok, this is a positive review from you in my eyes for this problem and
we can merge the spkg. I will ask someone else to take another look,
but I can assure you I did a very clean checkin :)

>  It should still take a couple of hours
> to complete.  I'll report back when I've got the finished product.

Cool, let me know if anything else blows up for you. I would assume
3.3.rc3 is out before your build finishes.
```


Cheers,

Michael



---

archive/issue_comments_040940.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T16:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5315#issuecomment-40940",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_040941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T16:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5315#issuecomment-40941",
    "user": "mabshoff"
}
```

Resolution: fixed
