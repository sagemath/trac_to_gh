# Issue 3854: interact needs to use "notruncate"

archive/issues_003854.json:
```json
{
    "body": "Assignee: @itolkov\n\nToo many controls results in output truncated errors, but it's the length of the generated html that's tripping the warning... this should be trivial, just add \"<!--notruncate-->\" to the generated html.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3854\n\n",
    "created_at": "2008-08-14T18:32:40Z",
    "labels": [
        "interact",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "interact needs to use \"notruncate\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3854",
    "user": "@rlmill"
}
```
Assignee: @itolkov

Too many controls results in output truncated errors, but it's the length of the generated html that's tripping the warning... this should be trivial, just add "<!--notruncate-->" to the generated html.

Issue created by migration from https://trac.sagemath.org/ticket/3854





---

archive/issue_comments_027447.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3854/sage.patch) by @itolkov created at 2008-08-14 19:24:35",
    "created_at": "2008-08-14T19:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27447",
    "user": "@itolkov"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3854/sage.patch) by @itolkov created at 2008-08-14 19:24:35



---

archive/issue_comments_027448.json:
```json
{
    "body": "looks good, and from what I can see it does what it is supposed to do. I suppose, that it would be kinda hard to write a doctest for it.",
    "created_at": "2008-08-23T23:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27448",
    "user": "@malb"
}
```

looks good, and from what I can see it does what it is supposed to do. I suppose, that it would be kinda hard to write a doctest for it.



---

archive/issue_comments_027449.json:
```json
{
    "body": "Doctesting could be easy: simply render the html, cut off the initial <html> and ending </html>, and put \"...notruncate...\" as the output...",
    "created_at": "2008-08-23T23:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27449",
    "user": "@rlmill"
}
```

Doctesting could be easy: simply render the html, cut off the initial <html> and ending </html>, and put "...notruncate..." as the output...



---

archive/issue_comments_027450.json:
```json
{
    "body": "Sure, but it wouldn't test the feature that is in discussion, i.e. that notruncate works as expected.",
    "created_at": "2008-08-24T11:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27450",
    "user": "@malb"
}
```

Sure, but it wouldn't test the feature that is in discussion, i.e. that notruncate works as expected.



---

archive/issue_comments_027451.json:
```json
{
    "body": "As is the patch does not apply:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_3854_sage.patch \npatching file sage/server/notebook/interact.py\nHunk #1 FAILED at 1397.\n1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej\n```\n\nIt should be trivial to rebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T02:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27451",
    "user": "mabshoff"
}
```

As is the patch does not apply:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_3854_sage.patch 
patching file sage/server/notebook/interact.py
Hunk #1 FAILED at 1397.
1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej
```

It should be trivial to rebase.

Cheers,

Michael



---

archive/issue_comments_027452.json:
```json
{
    "body": "Attachment [trac_3854.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854.patch) by @mwhansen created at 2008-08-27 00:38:20",
    "created_at": "2008-08-27T00:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27452",
    "user": "@mwhansen"
}
```

Attachment [trac_3854.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854.patch) by @mwhansen created at 2008-08-27 00:38:20



---

archive/issue_comments_027453.json:
```json
{
    "body": "The new patch should apply.",
    "created_at": "2008-08-27T00:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27453",
    "user": "@mwhansen"
}
```

The new patch should apply.



---

archive/issue_comments_027454.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T00:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27454",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_027455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T00:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27455",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027456.json:
```json
{
    "body": "Attachment [trac_3854_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854_doctest-fix.patch) by mabshoff created at 2008-08-27 01:47:45\n\nTrivial patch to fix two doctest failures",
    "created_at": "2008-08-27T01:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27456",
    "user": "mabshoff"
}
```

Attachment [trac_3854_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854_doctest-fix.patch) by mabshoff created at 2008-08-27 01:47:45

Trivial patch to fix two doctest failures



---

archive/issue_comments_027457.json:
```json
{
    "body": "For the future: please make dependencies between tickets clear. This ticket should have been applied after #3823. We ended up applying them in reverse order and had to rebase them each because the order was inverse.\n\nPlease also name the patches properly, i.e. trac_XXXX_description is that is expected.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T00:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27457",
    "user": "mabshoff"
}
```

For the future: please make dependencies between tickets clear. This ticket should have been applied after #3823. We ended up applying them in reverse order and had to rebase them each because the order was inverse.

Please also name the patches properly, i.e. trac_XXXX_description is that is expected.

Cheers,

Michael



---

archive/issue_comments_027458.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> Please also name the patches properly, i.e. trac_XXXX_description is that is expected.\n\nHi there, did we definitely agree on this? I hardly use it and feel stupid if I've missed the point where I was supposed to switch.",
    "created_at": "2008-08-29T10:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27458",
    "user": "@malb"
}
```

Replying to [comment:8 mabshoff]:
> Please also name the patches properly, i.e. trac_XXXX_description is that is expected.

Hi there, did we definitely agree on this? I hardly use it and feel stupid if I've missed the point where I was supposed to switch.
