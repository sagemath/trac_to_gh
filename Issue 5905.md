# Issue 5905: [with patch, needs review (trivial)] minor fix to ReST markup in ell_rational_field.py

archive/issues_005905.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: elliptic curve docbuild\n\nThere are two glitches in the docstring for function has_good_reduction_outside_S() in sage/schemes/elliptic_curves/ell_rational_field.py .\n\nThe ptach fixes them.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5905\n\n",
    "created_at": "2009-04-26T20:05:06Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review (trivial)] minor fix to ReST markup in ell_rational_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5905",
    "user": "cremona"
}
```
Assignee: tba

Keywords: elliptic curve docbuild

There are two glitches in the docstring for function has_good_reduction_outside_S() in sage/schemes/elliptic_curves/ell_rational_field.py .

The ptach fixes them.


Issue created by migration from https://trac.sagemath.org/ticket/5905





---

archive/issue_comments_046680.json:
```json
{
    "body": "Attachment [ell-doctest.patch](tarball://root/attachments/some-uuid/ticket5905/ell-doctest.patch) by cremona created at 2009-04-26 20:05:27",
    "created_at": "2009-04-26T20:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5905#issuecomment-46680",
    "user": "cremona"
}
```

Attachment [ell-doctest.patch](tarball://root/attachments/some-uuid/ticket5905/ell-doctest.patch) by cremona created at 2009-04-26 20:05:27



---

archive/issue_comments_046681.json:
```json
{
    "body": "The patch successfully fixes two problems in the reference manual. This eliminates one of the warnings which occurs when building the reference manual.  (The only one I still see is\n\n```\nchecking consistency... WARNING: /Applications/sage_builds/sage-3.4.2.alpha0-upgrade/devel/sage-new/doc/en/reference/sage/combinat/family.rst:: document isn't included in any toctree\n```\n\nin case anyone knows what to do about that.  If so, open a new ticket.)",
    "created_at": "2009-04-27T04:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5905#issuecomment-46681",
    "user": "jhpalmieri"
}
```

The patch successfully fixes two problems in the reference manual. This eliminates one of the warnings which occurs when building the reference manual.  (The only one I still see is

```
checking consistency... WARNING: /Applications/sage_builds/sage-3.4.2.alpha0-upgrade/devel/sage-new/doc/en/reference/sage/combinat/family.rst:: document isn't included in any toctree
```

in case anyone knows what to do about that.  If so, open a new ticket.)



---

archive/issue_comments_046682.json:
```json
{
    "body": "I worked out what causes this sort of thing.  Suppose you add a file to the ref man by adding to the table of contents, in a branch, and rebuild the docs to test.  Then (after making a patch, say) you roll back that branch to a version where that file is no longer mentioned in the toc.  But the file *.rst (which was automatically created earlier) remains in the doc tree even after both \"sage -b\" and \"sage -docbuild ...\", and causes this warning.\n\nI don't know the right way to fix this.  Perhaps Sphinx could just delete such files (it seems too much for \"sage -b\" to do).",
    "created_at": "2009-04-27T08:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5905#issuecomment-46682",
    "user": "cremona"
}
```

I worked out what causes this sort of thing.  Suppose you add a file to the ref man by adding to the table of contents, in a branch, and rebuild the docs to test.  Then (after making a patch, say) you roll back that branch to a version where that file is no longer mentioned in the toc.  But the file *.rst (which was automatically created earlier) remains in the doc tree even after both "sage -b" and "sage -docbuild ...", and causes this warning.

I don't know the right way to fix this.  Perhaps Sphinx could just delete such files (it seems too much for "sage -b" to do).



---

archive/issue_comments_046683.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T01:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5905#issuecomment-46683",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046684.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T01:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5905#issuecomment-46684",
    "user": "mabshoff"
}
```

Resolution: fixed
