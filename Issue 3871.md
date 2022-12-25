# Issue 3871: crap in SAGE_ROOT; extending #3759

archive/issues_003871.json:
```json
{
    "body": "Assignee: mabshoff\n\nThese are still left in SAGE_ROOT after testlong:\n\n`sage.png, sage0.png, sage1.png, sage2.png, sage3.png, sage4.png, sage5.png and sage6.png`\n\nSee #3759\n\nIssue created by migration from https://trac.sagemath.org/ticket/3871\n\n",
    "created_at": "2008-08-15T10:04:25Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "crap in SAGE_ROOT; extending #3759",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3871",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

These are still left in SAGE_ROOT after testlong:

`sage.png, sage0.png, sage1.png, sage2.png, sage3.png, sage4.png, sage5.png and sage6.png`

See #3759

Issue created by migration from https://trac.sagemath.org/ticket/3871





---

archive/issue_comments_027532.json:
```json
{
    "body": "I didn't testlong, but I did a full test, and found that /rings/polynomial/polynomial_element.pyx creates two images around line 228\n\n\n```\n        EXAMPLES:\n            sage: x = polygen(GF(389))\n            sage: plot(x^2 + 1, rgbcolor=(0,0,1)).save()\n            sage: x = polygen(QQ)\n            sage: plot(x^2 + 1, rgbcolor=(1,0,0)).save()\n```\n",
    "created_at": "2009-01-22T18:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27532",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I didn't testlong, but I did a full test, and found that /rings/polynomial/polynomial_element.pyx creates two images around line 228


```
        EXAMPLES:
            sage: x = polygen(GF(389))
            sage: plot(x^2 + 1, rgbcolor=(0,0,1)).save()
            sage: x = polygen(QQ)
            sage: plot(x^2 + 1, rgbcolor=(1,0,0)).save()
```




---

archive/issue_comments_027533.json:
```json
{
    "body": "Attachment [trac_3871.patch](tarball://root/attachments/some-uuid/ticket3871/trac_3871.patch) by @williamstein created at 2009-01-24 08:33:30\n\nThe attached patches just fix all the cases of saving images to a file that I could find using search_src('...').  I applied it and ran --long doctests, and everything passes.",
    "created_at": "2009-01-24T08:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27533",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3871.patch](tarball://root/attachments/some-uuid/ticket3871/trac_3871.patch) by @williamstein created at 2009-01-24 08:33:30

The attached patches just fix all the cases of saving images to a file that I could find using search_src('...').  I applied it and ran --long doctests, and everything passes.



---

archive/issue_comments_027534.json:
```json
{
    "body": "Attachment [trac_3871-part2.patch](tarball://root/attachments/some-uuid/ticket3871/trac_3871-part2.patch) by @williamstein created at 2009-01-24 08:35:30",
    "created_at": "2009-01-24T08:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27534",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3871-part2.patch](tarball://root/attachments/some-uuid/ticket3871/trac_3871-part2.patch) by @williamstein created at 2009-01-24 08:35:30



---

archive/issue_comments_027535.json:
```json
{
    "body": "Positive review. Hopefully this will be the last of the annoying code that dumps pngs into $SAGE_ROOT.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T12:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. Hopefully this will be the last of the annoying code that dumps pngs into $SAGE_ROOT.

Cheers,

Michael



---

archive/issue_comments_027536.json:
```json
{
    "body": "Note that the last hunk from the second patch in sage/schemes/elliptic_curves/lseries_ell.py is also in the first patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T12:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27536",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that the last hunk from the second patch in sage/schemes/elliptic_curves/lseries_ell.py is also in the first patch.

Cheers,

Michael



---

archive/issue_events_004092.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-24T13:16:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3871#event-4092"
}
```



---

archive/issue_comments_027537.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T13:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_027538.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T13:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3871#issuecomment-27538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
