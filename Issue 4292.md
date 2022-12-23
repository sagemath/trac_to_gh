# Issue 4292: [with patch; needs trivial review] graphics_array -- stupid bug introduced by somebody cleaning up the code

archive/issues_004292.json:
```json
{
    "body": "Assignee: was\n\nIf you do\n\n```\n   graphics_array([[plot(sin)]]).show(axes=False)\n```\n\nthe axes still get shown!  This horrendously sucks, e.g. ,for my talk today, and this was not a problem in Sage a few months ago. \n\nFortunately, it's a trivial 1-line fix, which I've attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4292\n\n",
    "created_at": "2008-10-15T11:11:36Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "[with patch; needs trivial review] graphics_array -- stupid bug introduced by somebody cleaning up the code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4292",
    "user": "was"
}
```
Assignee: was

If you do

```
   graphics_array([[plot(sin)]]).show(axes=False)
```

the axes still get shown!  This horrendously sucks, e.g. ,for my talk today, and this was not a problem in Sage a few months ago. 

Fortunately, it's a trivial 1-line fix, which I've attached.

Issue created by migration from https://trac.sagemath.org/ticket/4292





---

archive/issue_comments_031414.json:
```json
{
    "body": "Attachment\n\nThis seems fixed in 3.1.3.final. Which version did you use?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T15:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4292#issuecomment-31414",
    "user": "mabshoff"
}
```

Attachment

This seems fixed in 3.1.3.final. Which version did you use?

Cheers,

Michael



---

archive/issue_comments_031415.json:
```json
{
    "body": "I checked the source and the patch still applies, but it seems that the doctest posted does not test that particular code path, so I would suggest that the patch should be applied anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T15:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4292#issuecomment-31415",
    "user": "mabshoff"
}
```

I checked the source and the patch still applies, but it seems that the doctest posted does not test that particular code path, so I would suggest that the patch should be applied anyway.

Cheers,

Michael



---

archive/issue_comments_031416.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> I checked the source and the patch still applies, but it seems that the doctest posted does not test that particular code path, so I would suggest that the patch should be applied anyway.\n> \n> Cheers,\n> \n> Michael\n\nOk, after testing it with the command line version it becomes clear that the bug remains unfixed and that William's fix is the correct one. In the end I learned something about the plotting code :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T16:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4292#issuecomment-31416",
    "user": "mabshoff"
}
```

Replying to [comment:2 mabshoff]:
> I checked the source and the patch still applies, but it seems that the doctest posted does not test that particular code path, so I would suggest that the patch should be applied anyway.
> 
> Cheers,
> 
> Michael

Ok, after testing it with the command line version it becomes clear that the bug remains unfixed and that William's fix is the correct one. In the end I learned something about the plotting code :)

Cheers,

Michael



---

archive/issue_comments_031417.json:
```json
{
    "body": "Merged in Sage 3.1.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T16:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4292#issuecomment-31417",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.4.

Cheers,

Michael



---

archive/issue_comments_031418.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-15T16:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4292#issuecomment-31418",
    "user": "mabshoff"
}
```

Resolution: fixed
