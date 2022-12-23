# Issue 9750: Document that PARI no longer assumes more than GRH

archive/issues_009750.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  cremona\n\nEarlier versions of PARI assumed something stronger than GRH (in Sage, this is referred to as GRH++).  As of PARI 2.4.0, \"only\" the GRH is assumed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9750\n\n",
    "created_at": "2010-08-14T19:15:17Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Document that PARI no longer assumes more than GRH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9750",
    "user": "jdemeyer"
}
```
Assignee: mvngu

CC:  cremona

Earlier versions of PARI assumed something stronger than GRH (in Sage, this is referred to as GRH++).  As of PARI 2.4.0, "only" the GRH is assumed.

Issue created by migration from https://trac.sagemath.org/ticket/9750





---

archive/issue_comments_095481.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T19:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95481",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095482.json:
```json
{
    "body": "Attachment\n\nLooks good (apart from one Sphinx warning which my reviewer patch fixes).\n\nIs there a good reference, say in the PARI reference manual, for the GRH assumptions?",
    "created_at": "2010-08-15T17:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95482",
    "user": "cremona"
}
```

Attachment

Looks good (apart from one Sphinx warning which my reviewer patch fixes).

Is there a good reference, say in the PARI reference manual, for the GRH assumptions?



---

archive/issue_comments_095483.json:
```json
{
    "body": "Attachment\n\nApply after previous (and both depend on #9343)",
    "created_at": "2010-08-15T17:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95483",
    "user": "cremona"
}
```

Attachment

Apply after previous (and both depend on #9343)



---

archive/issue_comments_095484.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-15T17:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95484",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095485.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> Is there a good reference, say in the PARI reference manual, for the GRH assumptions?\n\nGood point, I added a reference to the PARI/GP User's Guide in the bnfcertify() documentation.  The new patch replaces the previous two patches.  John, can you re-review?",
    "created_at": "2010-08-15T19:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95485",
    "user": "jdemeyer"
}
```

Replying to [comment:4 cremona]:
> Is there a good reference, say in the PARI reference manual, for the GRH assumptions?

Good point, I added a reference to the PARI/GP User's Guide in the bnfcertify() documentation.  The new patch replaces the previous two patches.  John, can you re-review?



---

archive/issue_comments_095486.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-15T19:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95486",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095487.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-15T19:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95487",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095488.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-15T21:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95488",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095489.json:
```json
{
    "body": "Includes previous 2 patches, adds reference to PARI's User's Guide",
    "created_at": "2010-08-16T13:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95489",
    "user": "jdemeyer"
}
```

Includes previous 2 patches, adds reference to PARI's User's Guide



---

archive/issue_comments_095490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-10T10:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95490",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_095491.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-10T10:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9750#issuecomment-95491",
    "user": "mpatel"
}
```

Attachment
