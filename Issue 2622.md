# Issue 2622: [with patches, need review] add PolyBoRi to reference manual

archive/issues_002622.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nThese patches depend on #2619 and basically add some babel to the top of `sage.rings.polynomial.pbori`\n\nIssue created by migration from https://trac.sagemath.org/ticket/2622\n\n",
    "created_at": "2008-03-20T23:57:57Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patches, need review] add PolyBoRi to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2622",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

These patches depend on #2619 and basically add some babel to the top of `sage.rings.polynomial.pbori`

Issue created by migration from https://trac.sagemath.org/ticket/2622





---

archive/issue_comments_017964.json:
```json
{
    "body": "Attachment [polybori-refman-doc.patch](tarball://root/attachments/some-uuid/ticket2622/polybori-refman-doc.patch) by mabshoff created at 2008-03-21 01:13:25\n\npolybori-refman-sage.patch looks good to me: One small typo did sneak in: \"This quptient ring\"\n\npolybori-refman-doc.patch ought to be rebased since it has some unrelated changes included:\n\n```\npatch -p1 --dry-run < polybori-refman-doc.patch\\?format\\=raw\npatching file .hgtags\nHunk #1 FAILED at 122.\n1 out of 1 hunk FAILED -- saving rejects to file .hgtags.rej\npatching file commontex/patchlevel.tex\nHunk #1 FAILED at 1.\n1 out of 1 hunk FAILED -- saving rejects to file commontex/patchlevel.tex.rej\npatching file ref/combinat.tex\nReversed (or previously applied) patch detected!  Assume -R? [n] n\nApply anyway? [n] n\nSkipping patch.\n2 out of 2 hunks ignored -- saving rejects to file ref/combinat.tex.rej\npatching file ref/files\nReversed (or previously applied) patch detected!  Assume -R? [n] n\nApply anyway? [n] n\nSkipping patch.\n4 out of 4 hunks ignored -- saving rejects to file ref/files.rej\npatching file ref/hecke.tex\nReversed (or previously applied) patch detected!  Assume -R? [n] n\nApply anyway? [n] n\nSkipping patch.\n1 out of 1 hunk ignored -- saving rejects to file ref/hecke.tex.rej\npatching file ref/polynomial-rings.tex\npatching file ref/update_script.py\nReversed (or previously applied) patch detected!  Assume -R? [n] n\nApply anyway? [n] n\nSkipping patch.\n2 out of 2 hunks ignored -- saving rejects to file ref/update_script.py.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T01:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17964",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [polybori-refman-doc.patch](tarball://root/attachments/some-uuid/ticket2622/polybori-refman-doc.patch) by mabshoff created at 2008-03-21 01:13:25

polybori-refman-sage.patch looks good to me: One small typo did sneak in: "This quptient ring"

polybori-refman-doc.patch ought to be rebased since it has some unrelated changes included:

```
patch -p1 --dry-run < polybori-refman-doc.patch\?format\=raw
patching file .hgtags
Hunk #1 FAILED at 122.
1 out of 1 hunk FAILED -- saving rejects to file .hgtags.rej
patching file commontex/patchlevel.tex
Hunk #1 FAILED at 1.
1 out of 1 hunk FAILED -- saving rejects to file commontex/patchlevel.tex.rej
patching file ref/combinat.tex
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
2 out of 2 hunks ignored -- saving rejects to file ref/combinat.tex.rej
patching file ref/files
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
4 out of 4 hunks ignored -- saving rejects to file ref/files.rej
patching file ref/hecke.tex
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
1 out of 1 hunk ignored -- saving rejects to file ref/hecke.tex.rej
patching file ref/polynomial-rings.tex
patching file ref/update_script.py
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
2 out of 2 hunks ignored -- saving rejects to file ref/update_script.py.rej
```


Cheers,

Michael



---

archive/issue_comments_017965.json:
```json
{
    "body": "That is odd because I started with a vanilla doc repository. But I'll rebase.",
    "created_at": "2008-03-21T01:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17965",
    "user": "https://github.com/malb"
}
```

That is odd because I started with a vanilla doc repository. But I'll rebase.



---

archive/issue_comments_017966.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> That is odd because I started with a vanilla doc repository. But I'll rebase.\n\nFor the record: That was my 2.11.alpha0 build on sage.math which has a binary in /home/mabshoff/release-cycles-2.11/. I can throw out the hunks from the patch that are already there. \n\nAnother small issue I forgot: Are we going with Gr\u00f6bner now or will be stick with Groebner. Since we merged your various UTF-8 patches all those should work. Umlaute \u00fcber alles!\n\nMike Hansen will be reviewing the other patches in this series, so they should be merged tonight assuming the get positive reviews.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T01:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 malb]:
> That is odd because I started with a vanilla doc repository. But I'll rebase.

For the record: That was my 2.11.alpha0 build on sage.math which has a binary in /home/mabshoff/release-cycles-2.11/. I can throw out the hunks from the patch that are already there. 

Another small issue I forgot: Are we going with Gröbner now or will be stick with Groebner. Since we merged your various UTF-8 patches all those should work. Umlaute über alles!

Mike Hansen will be reviewing the other patches in this series, so they should be merged tonight assuming the get positive reviews.

Cheers,

Michael



---

archive/issue_comments_017967.json:
```json
{
    "body": "Attachment [polybori-refman-sage.patch](tarball://root/attachments/some-uuid/ticket2622/polybori-refman-sage.patch) by @malb created at 2008-03-21 01:36:03\n\nfixed typo",
    "created_at": "2008-03-21T01:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17967",
    "user": "https://github.com/malb"
}
```

Attachment [polybori-refman-sage.patch](tarball://root/attachments/some-uuid/ticket2622/polybori-refman-sage.patch) by @malb created at 2008-03-21 01:36:03

fixed typo



---

archive/issue_comments_017968.json:
```json
{
    "body": "Attachment [trac_2622_polybori-refman-doc.patch](tarball://root/attachments/some-uuid/ticket2622/trac_2622_polybori-refman-doc.patch) by @malb created at 2008-03-21 02:16:13\n\ncleaned up version of the patch",
    "created_at": "2008-03-21T02:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17968",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2622_polybori-refman-doc.patch](tarball://root/attachments/some-uuid/ticket2622/trac_2622_polybori-refman-doc.patch) by @malb created at 2008-03-21 02:16:13

cleaned up version of the patch



---

archive/issue_comments_017969.json:
```json
{
    "body": "All issues I had have been resolved.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T02:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17969",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

All issues I had have been resolved.

Cheers,

Michael



---

archive/issue_comments_017970.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T02:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17970",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017971.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T02:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2622#issuecomment-17971",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_events_002811.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-21T02:22:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2622",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2622#event-2811"
}
```
