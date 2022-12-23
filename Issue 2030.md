# Issue 2030: hg_[doc|extcode|scripts] docstring is wrong about the repo

archive/issues_002030.json:
```json
{
    "body": "Assignee: tba\n\n\n```\n[05:58] <mabshoff> The docstring for hg_scripts also seems to be wrong, i.e.\n[05:58] <mabshoff>         Most commands are directly provided as member functions.  However,\n[05:58] <mabshoff>         you can use the full functionality of hg, i.e.,\n[05:58] <mabshoff>                 hg_sage(\"command line arguments\")\n[05:58] <mabshoff>         is *exactly* the same as typing\n[05:58] <mabshoff>                 cd <SAGE_ROOT>/devel/sage/ && hg command line arguments\n[05:59] <mabshoff> Same for hg_extcode and hg_doc\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2030\n\n",
    "created_at": "2008-02-02T05:17:15Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "hg_[doc|extcode|scripts] docstring is wrong about the repo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2030",
    "user": "mabshoff"
}
```
Assignee: tba


```
[05:58] <mabshoff> The docstring for hg_scripts also seems to be wrong, i.e.
[05:58] <mabshoff>         Most commands are directly provided as member functions.  However,
[05:58] <mabshoff>         you can use the full functionality of hg, i.e.,
[05:58] <mabshoff>                 hg_sage("command line arguments")
[05:58] <mabshoff>         is *exactly* the same as typing
[05:58] <mabshoff>                 cd <SAGE_ROOT>/devel/sage/ && hg command line arguments
[05:59] <mabshoff> Same for hg_extcode and hg_doc
```


Issue created by migration from https://trac.sagemath.org/ticket/2030





---

archive/issue_comments_013136.json:
```json
{
    "body": "\n```\n22:24 < wstein> #2030 - what's wrong with the hg docstrig?\n22:25 < wstein> I couldn't figure that out from the ticket desc.\n22:25 < mabshoff> All of them say to cd into $SAGE_LOCAL/deve/sage\n22:25 < mabshoff> while the repos are in different places.\n22:25 < wstein> I think it's a \"generic\" docstring.\n22:25 < wstein> All the hg_* objects are instances of a generic hg object.\n22:25 < mabshoff> Ok, so is it fixable? Or is it invalid?\n22:26 < wstein> It should be fixed.\n22:26 < wstein> It might be kind of hard / unnatural.\n22:26 < wstein> However, if it is really confusing it should be changed.\n22:26 < mabshoff> Well, we could list all four repos in the generic docstring.\n22:26 < wstein> Or at least the docstring could be made much clearer to emphasize this subtle point.\n22:26 < wstein> Exactly\n```\n",
    "created_at": "2008-02-02T06:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13136",
    "user": "was"
}
```


```
22:24 < wstein> #2030 - what's wrong with the hg docstrig?
22:25 < wstein> I couldn't figure that out from the ticket desc.
22:25 < mabshoff> All of them say to cd into $SAGE_LOCAL/deve/sage
22:25 < mabshoff> while the repos are in different places.
22:25 < wstein> I think it's a "generic" docstring.
22:25 < wstein> All the hg_* objects are instances of a generic hg object.
22:25 < mabshoff> Ok, so is it fixable? Or is it invalid?
22:26 < wstein> It should be fixed.
22:26 < wstein> It might be kind of hard / unnatural.
22:26 < wstein> However, if it is really confusing it should be changed.
22:26 < mabshoff> Well, we could list all four repos in the generic docstring.
22:26 < wstein> Or at least the docstring could be made much clearer to emphasize this subtle point.
22:26 < wstein> Exactly
```




---

archive/issue_comments_013137.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-19T07:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13137",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013138.json:
```json
{
    "body": "Changing assignee from tba to mhansen.",
    "created_at": "2008-09-19T07:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13138",
    "user": "mhansen"
}
```

Changing assignee from tba to mhansen.



---

archive/issue_comments_013139.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-02T07:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13139",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_013140.json:
```json
{
    "body": "Hmmm, the second patch seems to be the same as the first one, but I would guess you accidentally did not post the second one.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T11:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13140",
    "user": "mabshoff"
}
```

Hmmm, the second patch seems to be the same as the first one, but I would guess you accidentally did not post the second one.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_013141.json:
```json
{
    "body": "Patch looks good (and is fun/clever).    Maybe Mike just hit submit twice by accident.",
    "created_at": "2008-12-06T22:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13141",
    "user": "was"
}
```

Patch looks good (and is fun/clever).    Maybe Mike just hit submit twice by accident.



---

archive/issue_comments_013142.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha1",
    "created_at": "2008-12-08T11:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13142",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha1



---

archive/issue_comments_013143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-08T11:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2030#issuecomment-13143",
    "user": "mabshoff"
}
```

Resolution: fixed
