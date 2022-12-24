# Issue 5102: eisenstein_series_qexp broken over finite fields

archive/issues_005102.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  craigcitro\n\n\n```\nsage: eisenstein_series_qexp(10, 15, GF(17))\n15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 2*q^12 + 12*q^13 + 12*q^14 + O(q^15)\n```\n\n\nis wrong, whereas\n\n\n```\nsage: eisenstein_series_qexp(10, 15).change_ring(GF(17))\n15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 3*q^12 + 14*q^13 + 16*q^14 + O(q^15)\n```\n\n\nis right.  We tracked this down to a change in the polynomials over finite fields constructor when `check=False`.  We'll quickly fix this at the cost of making it slower; better fix will come soon.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5102\n\n",
    "created_at": "2009-01-26T04:45:32Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "eisenstein_series_qexp broken over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5102",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

CC:  craigcitro


```
sage: eisenstein_series_qexp(10, 15, GF(17))
15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 2*q^12 + 12*q^13 + 12*q^14 + O(q^15)
```


is wrong, whereas


```
sage: eisenstein_series_qexp(10, 15).change_ring(GF(17))
15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 3*q^12 + 14*q^13 + 16*q^14 + O(q^15)
```


is right.  We tracked this down to a change in the polynomials over finite fields constructor when `check=False`.  We'll quickly fix this at the cost of making it slower; better fix will come soon.


Issue created by migration from https://trac.sagemath.org/ticket/5102





---

archive/issue_comments_038965.json:
```json
{
    "body": "Attachment [trac_5102.patch](tarball://root/attachments/some-uuid/ticket5102/trac_5102.patch) by AlexGhitza created at 2009-01-26 04:55:21\n\nCredit to Craig Citro and Alex Ghitza.",
    "created_at": "2009-01-26T04:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5102#issuecomment-38965",
    "user": "AlexGhitza"
}
```

Attachment [trac_5102.patch](tarball://root/attachments/some-uuid/ticket5102/trac_5102.patch) by AlexGhitza created at 2009-01-26 04:55:21

Credit to Craig Citro and Alex Ghitza.



---

archive/issue_comments_038966.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-01-26T04:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5102#issuecomment-38966",
    "user": "AlexGhitza"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_038967.json:
```json
{
    "body": "This gets a positive review from William.",
    "created_at": "2009-01-30T23:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5102#issuecomment-38967",
    "user": "mhansen"
}
```

This gets a positive review from William.



---

archive/issue_comments_038968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T02:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5102#issuecomment-38968",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038969.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5102#issuecomment-38969",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael
