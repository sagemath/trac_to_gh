# Issue 3792: fix Sage build when there is a broken systemwide freetype library

archive/issues_003792.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe problem and fix is in this thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/d1c8996964802ab1\n\n\nwhat remains to be done is to extract this fix, create a patch and new spkgs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3792\n\n",
    "created_at": "2008-08-08T20:05:52Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "fix Sage build when there is a broken systemwide freetype library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3792",
    "user": "certik"
}
```
Assignee: mabshoff

The problem and fix is in this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/d1c8996964802ab1


what remains to be done is to extract this fix, create a patch and new spkgs.

Issue created by migration from https://trac.sagemath.org/ticket/3792





---

archive/issue_comments_026964.json:
```json
{
    "body": "Here are the fixed spkg:\n\nhttp://sage.math.washington.edu/home/ondrej/spkg/matplotlib-0.91.1.p5.spkg\nhttp://sage.math.washington.edu/home/ondrej/spkg/gd-2.0.33.p5.spkg\n\nPlease don't just copy them, you need to extract it and copy the sage-install script. With matplotlib, that's all that is needed, with gd, you need to get a new gd-2.0.35 from:\n\nhttp://www.libgd.org/releases/\n\nand copy it to the src.",
    "created_at": "2008-08-18T12:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3792#issuecomment-26964",
    "user": "certik"
}
```

Here are the fixed spkg:

http://sage.math.washington.edu/home/ondrej/spkg/matplotlib-0.91.1.p5.spkg
http://sage.math.washington.edu/home/ondrej/spkg/gd-2.0.33.p5.spkg

Please don't just copy them, you need to extract it and copy the sage-install script. With matplotlib, that's all that is needed, with gd, you need to get a new gd-2.0.35 from:

http://www.libgd.org/releases/

and copy it to the src.



---

archive/issue_comments_026965.json:
```json
{
    "body": "Review:\n\n* matplotlib-0.91.1.p5.spkg: this is the right fix and I will forward port it to the matplotlib-0.98.spkg.\n* gd-2.0.33.p5.spkg: this is also the correct fix and I will port it to the current gd-2.0.35.spkg\n\nAside from that everything else for a properly upgraded spkg is wrong, but I guess since nobody ever taught you you did not know :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T09:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3792#issuecomment-26965",
    "user": "mabshoff"
}
```

Review:

* matplotlib-0.91.1.p5.spkg: this is the right fix and I will forward port it to the matplotlib-0.98.spkg.
* gd-2.0.33.p5.spkg: this is also the correct fix and I will port it to the current gd-2.0.35.spkg

Aside from that everything else for a properly upgraded spkg is wrong, but I guess since nobody ever taught you you did not know :)

Cheers,

Michael



---

archive/issue_comments_026966.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T09:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3792#issuecomment-26966",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_026967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T09:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3792#issuecomment-26967",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026968.json:
```json
{
    "body": "Yes, I know, it was a quick hack to get things working, but just to be sure you don't just copy the spkg, I wrote literally, please don't copy it, extract it. :)\n\nThanks Michael!",
    "created_at": "2008-08-27T09:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3792#issuecomment-26968",
    "user": "certik"
}
```

Yes, I know, it was a quick hack to get things working, but just to be sure you don't just copy the spkg, I wrote literally, please don't copy it, extract it. :)

Thanks Michael!
