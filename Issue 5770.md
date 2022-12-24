# Issue 5770: [with patch, needs review] Bring doctests of modular/modsym/p1list.py up to 100%

archive/issues_005770.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @loefflerd\n\nKeywords: modular form documentation\n\nThe attached patch completes all docstrings and doctests for the file modular/modsym/p1list.py.  I also checked that the html and pdf output in the reference manual look good.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5770\n\n",
    "created_at": "2009-04-12T17:25:24Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Bring doctests of modular/modsym/p1list.py up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5770",
    "user": "@JohnCremona"
}
```
Assignee: @craigcitro

CC:  @loefflerd

Keywords: modular form documentation

The attached patch completes all docstrings and doctests for the file modular/modsym/p1list.py.  I also checked that the html and pdf output in the reference manual look good.

Issue created by migration from https://trac.sagemath.org/ticket/5770





---

archive/issue_comments_045130.json:
```json
{
    "body": "Attachment [p1list-doc.patch](tarball://root/attachments/some-uuid/ticket5770/p1list-doc.patch) by @JohnCremona created at 2009-04-12 17:25:57\n\nBased on 3.4.1.rc2",
    "created_at": "2009-04-12T17:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5770#issuecomment-45130",
    "user": "@JohnCremona"
}
```

Attachment [p1list-doc.patch](tarball://root/attachments/some-uuid/ticket5770/p1list-doc.patch) by @JohnCremona created at 2009-04-12 17:25:57

Based on 3.4.1.rc2



---

archive/issue_comments_045131.json:
```json
{
    "body": "Patch applies fine to 3.4.1.rc2, all doctests pass, and reference manual builds happily. There is just one tiny typo: in the docstring for \"apply_S\", it has \"[-0,1;1,0]\" instead of \"[0,-1;1,0]\". I have uploaded a patch that corrects this.",
    "created_at": "2009-04-13T12:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5770#issuecomment-45131",
    "user": "@loefflerd"
}
```

Patch applies fine to 3.4.1.rc2, all doctests pass, and reference manual builds happily. There is just one tiny typo: in the docstring for "apply_S", it has "[-0,1;1,0]" instead of "[0,-1;1,0]". I have uploaded a patch that corrects this.



---

archive/issue_comments_045132.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2009-04-13T12:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5770#issuecomment-45132",
    "user": "@loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_045133.json:
```json
{
    "body": "Attachment [trac_5770-reviewer_fix.patch](tarball://root/attachments/some-uuid/ticket5770/trac_5770-reviewer_fix.patch) by @JohnCremona created at 2009-04-13 13:16:28\n\nThanks, David.  Getting the documentation to build & look ok takes a long time!  As you can imagine there was a lot of cutting and pasting.  Much more of the same to com with manin_symbols.py, where there are about 5 classes each of which has a very similar set of methods (but not quite identical).",
    "created_at": "2009-04-13T13:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5770#issuecomment-45133",
    "user": "@JohnCremona"
}
```

Attachment [trac_5770-reviewer_fix.patch](tarball://root/attachments/some-uuid/ticket5770/trac_5770-reviewer_fix.patch) by @JohnCremona created at 2009-04-13 13:16:28

Thanks, David.  Getting the documentation to build & look ok takes a long time!  As you can imagine there was a lot of cutting and pasting.  Much more of the same to com with manin_symbols.py, where there are about 5 classes each of which has a very similar set of methods (but not quite identical).



---

archive/issue_comments_045134.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T22:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5770#issuecomment-45134",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_045135.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T22:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5770#issuecomment-45135",
    "user": "mabshoff"
}
```

Resolution: fixed
