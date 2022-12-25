# Issue 2815: docstring errors in coding/pbori

archive/issues_002815.json:
```json
{
    "body": "Assignee: tba\n\nThe attached patch fixes some latex docstring errors. No code is modified or added.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2815\n\n",
    "created_at": "2008-04-05T21:30:38Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "docstring errors in coding/pbori",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2815",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: tba

The attached patch fixes some latex docstring errors. No code is modified or added.

Issue created by migration from https://trac.sagemath.org/ticket/2815





---

archive/issue_comments_019284.json:
```json
{
    "body": "docstring patch based on sage-3.0.alpha0",
    "created_at": "2008-04-05T21:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19284",
    "user": "https://github.com/wdjoyner"
}
```

docstring patch based on sage-3.0.alpha0



---

archive/issue_comments_019285.json:
```json
{
    "body": "Attachment [9217.patch](tarball://root/attachments/some-uuid/ticket2815/9217.patch) by mabshoff created at 2008-04-05 21:34:24",
    "created_at": "2008-04-05T21:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [9217.patch](tarball://root/attachments/some-uuid/ticket2815/9217.patch) by mabshoff created at 2008-04-05 21:34:24



---

archive/issue_comments_019286.json:
```json
{
    "body": "Attachment [511.patch](tarball://root/attachments/some-uuid/ticket2815/511.patch) by @wdjoyner created at 2008-04-05 21:35:37\n\ndoc patch based on sage-3.0.alpha0 which adds sections to ref.tex",
    "created_at": "2008-04-05T21:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19286",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [511.patch](tarball://root/attachments/some-uuid/ticket2815/511.patch) by @wdjoyner created at 2008-04-05 21:35:37

doc patch based on sage-3.0.alpha0 which adds sections to ref.tex



---

archive/issue_comments_019287.json:
```json
{
    "body": "Looks good.\n\nI wonder if this could be an issue though, but I doubt it.\n\n\n``` \n- \\setshortversion{2.11} \n+ \\setshortversion{3.0.alpha0} \n```\n",
    "created_at": "2008-04-05T21:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19287",
    "user": "https://github.com/malb"
}
```

Looks good.

I wonder if this could be an issue though, but I doubt it.


``` 
- \setshortversion{2.11} 
+ \setshortversion{3.0.alpha0} 
```




---

archive/issue_comments_019288.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> Looks good.\n> \n> I wonder if this could be an issue though, but I doubt it.\n> \n> {{{ \n> - \\setshortversion{2.11} \n> + \\setshortversion{3.0.alpha0} \n> }}}\n\nI will delete that bit from the patch. Thanks for the review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T21:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 malb]:
> Looks good.
> 
> I wonder if this could be an issue though, but I doubt it.
> 
> {{{ 
> - \setshortversion{2.11} 
> + \setshortversion{3.0.alpha0} 
> }}}

I will delete that bit from the patch. Thanks for the review.

Cheers,

Michael



---

archive/issue_comments_019289.json:
```json
{
    "body": "David: I do not see any fixes to PolyBoRi. There are changes to the crystal code and the other patch adds the documentation of coding/sd-codes and coding/code-constructions to the manual. Is there anything coming for PolyBori?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T22:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19289",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David: I do not see any fixes to PolyBoRi. There are changes to the crystal code and the other patch adds the documentation of coding/sd-codes and coding/code-constructions to the manual. Is there anything coming for PolyBori?

Cheers,

Michael



---

archive/issue_comments_019290.json:
```json
{
    "body": "mmmh, the crystals patch does not apply at all:\n\n```\npatch -p1 --dry-run < trac_2815_9217.patch\npatching file sage/combinat/crystals/letters.py\nHunk #1 FAILED at 197.\nHunk #2 FAILED at 213.\nHunk #3 FAILED at 234.\nHunk #4 FAILED at 243.\nHunk #5 FAILED at 267.\n```\n\n\nI changed the summary to \"dd more coding theory to the reference manual\" since that patch does apply. Please open another ticket for any new patches.\n\nThoughts?",
    "created_at": "2008-04-05T22:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

mmmh, the crystals patch does not apply at all:

```
patch -p1 --dry-run < trac_2815_9217.patch
patching file sage/combinat/crystals/letters.py
Hunk #1 FAILED at 197.
Hunk #2 FAILED at 213.
Hunk #3 FAILED at 234.
Hunk #4 FAILED at 243.
Hunk #5 FAILED at 267.
```


I changed the summary to "dd more coding theory to the reference manual" since that patch does apply. Please open another ticket for any new patches.

Thoughts?



---

archive/issue_comments_019291.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T22:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003006.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-05T22:30:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2815#event-3006"
}
```



---

archive/issue_comments_019292.json:
```json
{
    "body": "Merged 511.patch in Sage 3.0.alpha2",
    "created_at": "2008-04-05T22:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2815#issuecomment-19292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 511.patch in Sage 3.0.alpha2
