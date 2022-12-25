# Issue 3854: interact needs to use "notruncate"

archive/issues_003854.json:
```json
{
    "body": "Assignee: @itolkov\n\nToo many controls results in output truncated errors, but it's the length of the generated html that's tripping the warning... this should be trivial, just add \"<!--notruncate-->\" to the generated html.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3854\n\n",
    "created_at": "2008-08-14T18:32:40Z",
    "labels": [
        "component: interact",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "interact needs to use \"notruncate\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3854",
    "user": "https://github.com/rlmill"
}
```
Assignee: @itolkov

Too many controls results in output truncated errors, but it's the length of the generated html that's tripping the warning... this should be trivial, just add "<!--notruncate-->" to the generated html.

Issue created by migration from https://trac.sagemath.org/ticket/3854





---

archive/issue_comments_027389.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3854/sage.patch) by @itolkov created at 2008-08-14 19:24:35",
    "created_at": "2008-08-14T19:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27389",
    "user": "https://github.com/itolkov"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3854/sage.patch) by @itolkov created at 2008-08-14 19:24:35



---

archive/issue_comments_027390.json:
```json
{
    "body": "looks good, and from what I can see it does what it is supposed to do. I suppose, that it would be kinda hard to write a doctest for it.",
    "created_at": "2008-08-23T23:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27390",
    "user": "https://github.com/malb"
}
```

looks good, and from what I can see it does what it is supposed to do. I suppose, that it would be kinda hard to write a doctest for it.



---

archive/issue_comments_027391.json:
```json
{
    "body": "Doctesting could be easy: simply render the html, cut off the initial <html> and ending </html>, and put \"...notruncate...\" as the output...",
    "created_at": "2008-08-23T23:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27391",
    "user": "https://github.com/rlmill"
}
```

Doctesting could be easy: simply render the html, cut off the initial <html> and ending </html>, and put "...notruncate..." as the output...



---

archive/issue_comments_027392.json:
```json
{
    "body": "Sure, but it wouldn't test the feature that is in discussion, i.e. that notruncate works as expected.",
    "created_at": "2008-08-24T11:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27392",
    "user": "https://github.com/malb"
}
```

Sure, but it wouldn't test the feature that is in discussion, i.e. that notruncate works as expected.



---

archive/issue_comments_027393.json:
```json
{
    "body": "As is the patch does not apply:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_3854_sage.patch \npatching file sage/server/notebook/interact.py\nHunk #1 FAILED at 1397.\n1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej\n```\n\nIt should be trivial to rebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T02:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_027394.json:
```json
{
    "body": "Attachment [trac_3854.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854.patch) by @mwhansen created at 2008-08-27 00:38:20",
    "created_at": "2008-08-27T00:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27394",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3854.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854.patch) by @mwhansen created at 2008-08-27 00:38:20



---

archive/issue_comments_027395.json:
```json
{
    "body": "The new patch should apply.",
    "created_at": "2008-08-27T00:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27395",
    "user": "https://github.com/mwhansen"
}
```

The new patch should apply.



---

archive/issue_comments_027396.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T00:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27396",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_events_004077.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-27T00:48:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3854#event-4077"
}
```



---

archive/issue_comments_027397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T00:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027398.json:
```json
{
    "body": "Attachment [trac_3854_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854_doctest-fix.patch) by mabshoff created at 2008-08-27 01:47:45\n\nTrivial patch to fix two doctest failures",
    "created_at": "2008-08-27T01:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3854_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket3854/trac_3854_doctest-fix.patch) by mabshoff created at 2008-08-27 01:47:45

Trivial patch to fix two doctest failures



---

archive/issue_comments_027399.json:
```json
{
    "body": "For the future: please make dependencies between tickets clear. This ticket should have been applied after #3823. We ended up applying them in reverse order and had to rebase them each because the order was inverse.\n\nPlease also name the patches properly, i.e. trac_XXXX_description is that is expected.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T00:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27399",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the future: please make dependencies between tickets clear. This ticket should have been applied after #3823. We ended up applying them in reverse order and had to rebase them each because the order was inverse.

Please also name the patches properly, i.e. trac_XXXX_description is that is expected.

Cheers,

Michael



---

archive/issue_comments_027400.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> Please also name the patches properly, i.e. trac_XXXX_description is that is expected.\n\nHi there, did we definitely agree on this? I hardly use it and feel stupid if I've missed the point where I was supposed to switch.",
    "created_at": "2008-08-29T10:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3854#issuecomment-27400",
    "user": "https://github.com/malb"
}
```

Replying to [comment:8 mabshoff]:
> Please also name the patches properly, i.e. trac_XXXX_description is that is expected.

Hi there, did we definitely agree on this? I hardly use it and feel stupid if I've missed the point where I was supposed to switch.
