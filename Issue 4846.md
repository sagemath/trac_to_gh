# Issue 4846: Doctesting should create an empty init.sage if it doesn't exist

archive/issues_004846.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  craigcitro\n\nOften when we do fix IPython related problems things break when init.sage is present. So make doctesting create an empty init.sage so that this is potentially caught.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4846\n\n",
    "created_at": "2008-12-21T09:25:01Z",
    "labels": [
        "doctest coverage",
        "critical",
        "bug"
    ],
    "title": "Doctesting should create an empty init.sage if it doesn't exist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4846",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  craigcitro

Often when we do fix IPython related problems things break when init.sage is present. So make doctesting create an empty init.sage so that this is potentially caught.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4846





---

archive/issue_comments_036746.json:
```json
{
    "body": "There are doctests in 3.2.2 that fail with an init.sage, so all we need to do is to add the check if it is missing in sage-sage when running doctests and then create an empty one to detect this particular bug.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T11:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36746",
    "user": "mabshoff"
}
```

There are doctests in 3.2.2 that fail with an init.sage, so all we need to do is to add the check if it is missing in sage-sage when running doctests and then create an empty one to detect this particular bug.

Cheers,

Michael



---

archive/issue_comments_036747.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-26T23:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36747",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036748.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-26T23:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36748",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_036749.json:
```json
{
    "body": "After pestering mabshoff on IRC about this a little, I am convinced this is a good quick solution to avoid most init.sage problems we missed during some of the recent releases. Positive review. :)",
    "created_at": "2008-12-26T23:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36749",
    "user": "burcin"
}
```

After pestering mabshoff on IRC about this a little, I am convinced this is a good quick solution to avoid most init.sage problems we missed during some of the recent releases. Positive review. :)



---

archive/issue_comments_036750.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-26T23:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36750",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036751.json:
```json
{
    "body": "Merged in Sage 3.2.3.final",
    "created_at": "2008-12-26T23:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36751",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.final
