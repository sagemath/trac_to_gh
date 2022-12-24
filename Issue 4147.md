# Issue 4147: Upgrade to linbox-1.1.6

archive/issues_004147.json:
```json
{
    "body": "Assignee: cpernet\n\nUpgrade the linbox spkg to upstream latest version, that will be released as v1.1.6.\nThis is a defect since the current 1.1.6rc1 version does not compile under cygwin (linker and gcc-3.4 related issues).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4147\n\n",
    "created_at": "2008-09-19T00:37:38Z",
    "labels": [
        "linbox",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Upgrade to linbox-1.1.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4147",
    "user": "cpernet"
}
```
Assignee: cpernet

Upgrade the linbox spkg to upstream latest version, that will be released as v1.1.6.
This is a defect since the current 1.1.6rc1 version does not compile under cygwin (linker and gcc-3.4 related issues).

Issue created by migration from https://trac.sagemath.org/ticket/4147





---

archive/issue_comments_030098.json:
```json
{
    "body": "The proposed spkg is here: [http://sage.math.washington.edu/home/pernet/linbox-1.1.6.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.6.spkg)\n\nAlready succesfully tested on sage.math and on my x86_32 Linux box.",
    "created_at": "2008-09-19T00:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4147#issuecomment-30098",
    "user": "cpernet"
}
```

The proposed spkg is here: [http://sage.math.washington.edu/home/pernet/linbox-1.1.6.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.6.spkg)

Already succesfully tested on sage.math and on my x86_32 Linux box.



---

archive/issue_comments_030099.json:
```json
{
    "body": "Changing priority from trivial to major.",
    "created_at": "2008-09-19T00:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4147#issuecomment-30099",
    "user": "cpernet"
}
```

Changing priority from trivial to major.



---

archive/issue_comments_030100.json:
```json
{
    "body": "Spkg looks good to me. I added some code to touch the extensions linked against LinBox so they are automatically rebuild when doing a \"sage -b\". The updated spkg is in\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/linbox-1.1.6.spkg\n\nPositive review, but I am doing some more build testing to be sure the spkg actually works.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T01:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4147#issuecomment-30100",
    "user": "mabshoff"
}
```

Spkg looks good to me. I added some code to touch the extensions linked against LinBox so they are automatically rebuild when doing a "sage -b". The updated spkg is in

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/linbox-1.1.6.spkg

Positive review, but I am doing some more build testing to be sure the spkg actually works.

Cheers,

Michael



---

archive/issue_comments_030101.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-20T02:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4147#issuecomment-30101",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha0



---

archive/issue_comments_030102.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-20T02:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4147#issuecomment-30102",
    "user": "mabshoff"
}
```

Resolution: fixed
