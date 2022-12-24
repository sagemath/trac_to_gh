# Issue 2903: [with spkg + patch, needs review] make NTL error messages propagate to RuntimeError messages

archive/issues_002903.json:
```json
{
    "body": "Assignee: cwitty\n\nThe spkg and patch achieve the following:\n\n* add a mechanism to NTL for setting a callback, so that when NTL calls its `Error()` function, the callback is called instead of printing an error message to stderr and abort()-ing\n\n* use this mechanism in Sage to propagate NTL's error messages back to a `RuntimeError` with a message. This means that instead of crashing to the command line, the user lands back at the sage prompt.\n\nIt would be nice if the NTL modifications were accepted upstream.\n\nObviously this solution is suboptimal, since it will very likely cause memory leaks. But memory leaks are better than crashing to the command line (well, that's debatable I suppose....). But the only way to fix this would be a major rewrite of lots of NTL to implement saner error propagation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2903\n\n",
    "created_at": "2008-04-13T02:55:37Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with spkg + patch, needs review] make NTL error messages propagate to RuntimeError messages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2903",
    "user": "dmharvey"
}
```
Assignee: cwitty

The spkg and patch achieve the following:

* add a mechanism to NTL for setting a callback, so that when NTL calls its `Error()` function, the callback is called instead of printing an error message to stderr and abort()-ing

* use this mechanism in Sage to propagate NTL's error messages back to a `RuntimeError` with a message. This means that instead of crashing to the command line, the user lands back at the sage prompt.

It would be nice if the NTL modifications were accepted upstream.

Obviously this solution is suboptimal, since it will very likely cause memory leaks. But memory leaks are better than crashing to the command line (well, that's debatable I suppose....). But the only way to fix this would be a major rewrite of lots of NTL to implement saner error propagation.


Issue created by migration from https://trac.sagemath.org/ticket/2903





---

archive/issue_comments_020015.json:
```json
{
    "body": "spkg was too big, trac didn't like it.\n\nHere it is instead:\n\nhttp://sage.math.washington.edu/home/dmharvey/ntl-5.4.2.p1.spkg",
    "created_at": "2008-04-13T02:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2903#issuecomment-20015",
    "user": "dmharvey"
}
```

spkg was too big, trac didn't like it.

Here it is instead:

http://sage.math.washington.edu/home/dmharvey/ntl-5.4.2.p1.spkg



---

archive/issue_comments_020016.json:
```json
{
    "body": "Attachment [ntl-error.patch](tarball://root/attachments/some-uuid/ticket2903/ntl-error.patch) by mabshoff created at 2008-04-13 03:03:36",
    "created_at": "2008-04-13T03:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2903#issuecomment-20016",
    "user": "mabshoff"
}
```

Attachment [ntl-error.patch](tarball://root/attachments/some-uuid/ticket2903/ntl-error.patch) by mabshoff created at 2008-04-13 03:03:36



---

archive/issue_comments_020017.json:
```json
{
    "body": "The spkg as well as the patch looks good to me. I added patches of the changed files to the patches directory, so that external packages have an easier time updating the source.\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-17T19:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2903#issuecomment-20017",
    "user": "mabshoff"
}
```

The spkg as well as the patch looks good to me. I added patches of the changed files to the patches directory, so that external packages have an easier time updating the source.

Positive review.

Cheers,

Michael



---

archive/issue_comments_020018.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T20:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2903#issuecomment-20018",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_020019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T20:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2903#issuecomment-20019",
    "user": "mabshoff"
}
```

Resolution: fixed
