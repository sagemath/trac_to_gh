# Issue 7341: major tab completion issue in notebook (?)

archive/issues_007341.json:
```json
{
    "body": "Assignee: boothby\n\nTry this in the notebook:\n\n```\nK.<a> = QuadraticField(-7)\nb = K.pari_bnf()\nb.<tab>\n```\n\n\nThen compare to the command line.  For some reason the last thing, \"b.bnfunit\" is missing in the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7341\n\n",
    "created_at": "2009-10-28T22:17:40Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "major tab completion issue in notebook (?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7341",
    "user": "was"
}
```
Assignee: boothby

Try this in the notebook:

```
K.<a> = QuadraticField(-7)
b = K.pari_bnf()
b.<tab>
```


Then compare to the command line.  For some reason the last thing, "b.bnfunit" is missing in the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/7341





---

archive/issue_comments_061437.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-10-29T01:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61437",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_061438.json:
```json
{
    "body": "Attachment [trac_sagenb-7341.patch](tarball://root/attachments/some-uuid/ticket7341/trac_sagenb-7341.patch) by was created at 2009-10-29 06:42:32",
    "created_at": "2009-10-29T06:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61438",
    "user": "was"
}
```

Attachment [trac_sagenb-7341.patch](tarball://root/attachments/some-uuid/ticket7341/trac_sagenb-7341.patch) by was created at 2009-10-29 06:42:32



---

archive/issue_comments_061439.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T06:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61439",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061440.json:
```json
{
    "body": "Bug confirmed, and patch works. I've also added a new test in #7343 to confirm that the patch does the fix. Perhaps we should require any patch to SageNB to add a Selenium test?",
    "created_at": "2009-10-29T12:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61440",
    "user": "timdumol"
}
```

Bug confirmed, and patch works. I've also added a new test in #7343 to confirm that the patch does the fix. Perhaps we should require any patch to SageNB to add a Selenium test?



---

archive/issue_comments_061441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T12:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61441",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-09T17:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61442",
    "user": "was"
}
```

Resolution: fixed
