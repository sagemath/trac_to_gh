# Issue 7341: [with patch, positive review] major tab completion issue in notebook (?)

archive/issues_007341.json:
```json
{
    "body": "Assignee: boothby\n\nTry this in the notebook:\n\n```\nK.<a> = QuadraticField(-7)\nb = K.pari_bnf()\nb.bnf<tab>\n```\n\nThen compare to the command line.  For some reason the last thing, \"b.bnfunit\" is missing in the notebook.\n\nScreenshot: http://wstein.org/home/wstein/patches/7341.png\n\nIssue created by migration from https://trac.sagemath.org/ticket/7341\n\n",
    "closed_at": "2009-11-09T17:17:55Z",
    "created_at": "2009-10-28T22:17:40Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch, positive review] major tab completion issue in notebook (?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7341",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Try this in the notebook:

```
K.<a> = QuadraticField(-7)
b = K.pari_bnf()
b.bnf<tab>
```

Then compare to the command line.  For some reason the last thing, "b.bnfunit" is missing in the notebook.

Screenshot: http://wstein.org/home/wstein/patches/7341.png

Issue created by migration from https://trac.sagemath.org/ticket/7341





---

archive/issue_comments_061324.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-10-29T01:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61324",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_061325.json:
```json
{
    "body": "Attachment [trac_sagenb-7341.patch](tarball://root/attachments/some-uuid/ticket7341/trac_sagenb-7341.patch) by @williamstein created at 2009-10-29 06:42:32",
    "created_at": "2009-10-29T06:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61325",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_sagenb-7341.patch](tarball://root/attachments/some-uuid/ticket7341/trac_sagenb-7341.patch) by @williamstein created at 2009-10-29 06:42:32



---

archive/issue_comments_061326.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T06:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61326",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061327.json:
```json
{
    "body": "Bug confirmed, and patch works. I've also added a new test in #7343 to confirm that the patch does the fix. Perhaps we should require any patch to SageNB to add a Selenium test?",
    "created_at": "2009-10-29T12:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61327",
    "user": "https://github.com/TimDumol"
}
```

Bug confirmed, and patch works. I've also added a new test in #7343 to confirm that the patch does the fix. Perhaps we should require any patch to SageNB to add a Selenium test?



---

archive/issue_comments_061328.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T12:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61328",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017371.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-09T17:17:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7341#event-17371"
}
```



---

archive/issue_comments_061329.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-09T17:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7341#issuecomment-61329",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
