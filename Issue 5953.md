# Issue 5953: sage/modular/modform/vm_basis.py is missing verbatim areas for doctests

archive/issues_005953.json:
```json
{
    "body": "Assignee: tba\n\nThis is what the ReST documentation looks like:\n\n```\nEXAMPLES:\nsage: victor_miller_basis(1, 6) [] sage: victor_miller_basis(0, 6) [ 1 + O(q^6) ] sage: victor_miller_basis(2, 6) [] sage: victor_miller_basis(4, 6) [ 1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6) ]\n\nsage: victor_miller_basis(6, 6, var=\u2019w\u2019) [ 1 - 504*w - 16632*w^2 - 122976*w^3 - 532728*w^4 - 1575504*w^5 + O(w^6) ]\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5953\n\n",
    "created_at": "2009-05-01T05:03:46Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "sage/modular/modform/vm_basis.py is missing verbatim areas for doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5953",
    "user": "mabshoff"
}
```
Assignee: tba

This is what the ReST documentation looks like:

```
EXAMPLES:
sage: victor_miller_basis(1, 6) [] sage: victor_miller_basis(0, 6) [ 1 + O(q^6) ] sage: victor_miller_basis(2, 6) [] sage: victor_miller_basis(4, 6) [ 1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6) ]

sage: victor_miller_basis(6, 6, var=’w’) [ 1 - 504*w - 16632*w^2 - 122976*w^3 - 532728*w^4 - 1575504*w^5 + O(w^6) ]
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5953





---

archive/issue_comments_047087.json:
```json
{
    "body": "Attachment [trac_5953.patch](tarball://root/attachments/some-uuid/ticket5953/trac_5953.patch) by mabshoff created at 2009-05-01 05:34:49",
    "created_at": "2009-05-01T05:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47087",
    "user": "mabshoff"
}
```

Attachment [trac_5953.patch](tarball://root/attachments/some-uuid/ticket5953/trac_5953.patch) by mabshoff created at 2009-05-01 05:34:49



---

archive/issue_comments_047088.json:
```json
{
    "body": "I think that in INPUT and AUTHOR blocks, the lines shouldn't be indented. I'm attaching a referee's patch changing this, and also changing an instance of `$blah$` to ``blah``.  If you're happy with my patch, I'm happy with yours.",
    "created_at": "2009-05-01T05:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47088",
    "user": "jhpalmieri"
}
```

I think that in INPUT and AUTHOR blocks, the lines shouldn't be indented. I'm attaching a referee's patch changing this, and also changing an instance of `$blah$` to ``blah``.  If you're happy with my patch, I'm happy with yours.



---

archive/issue_comments_047089.json:
```json
{
    "body": "referee's patch",
    "created_at": "2009-05-01T05:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47089",
    "user": "jhpalmieri"
}
```

referee's patch



---

archive/issue_comments_047090.json:
```json
{
    "body": "Attachment [ref_5953.patch](tarball://root/attachments/some-uuid/ticket5953/ref_5953.patch) by mabshoff created at 2009-05-01 05:50:23\n\nFor the record: Reviewer patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-01T05:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47090",
    "user": "mabshoff"
}
```

Attachment [ref_5953.patch](tarball://root/attachments/some-uuid/ticket5953/ref_5953.patch) by mabshoff created at 2009-05-01 05:50:23

For the record: Reviewer patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_047091.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-01T05:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47091",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047092.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2009-05-01T05:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47092",
    "user": "mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_047093.json:
```json
{
    "body": "Merged both patches in Sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-01T05:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47093",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.2.final.

Cheers,

Michael



---

archive/issue_comments_047094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-01T05:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5953#issuecomment-47094",
    "user": "mabshoff"
}
```

Resolution: fixed
