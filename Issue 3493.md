# Issue 3493: Notes on Elliptic curves documentation

archive/issues_003493.json:
```json
{
    "body": "Assignee: tba\n\nIn part 37.8 of the Reference Manual (the Elliptic curves over finite fields section) there are some formatting issues. For instance, in the section on the frobenius_polynomial, we have the sentence:\n\n\n```\nThe Frobenius endomorphism of the elliptic curve has quadratic characteristic polynomial. \nIn most cases this is irreducible and defines an imaginary quadratic order; \nfor some supersingular curves, Frobenius is an integer a and the polynomial is 1703#326 .}}}\n\nI assume that the 1703#326 is some sort of broken formatting code.\n\nThere are similar examples throughout this page.\n\nOn a slightly different tack, in the documentation for cardinality and order, it would be helpful to say that \"sea\" (as in the algorithm) means Schoof-Elkies-Atkin.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3493\n\n",
    "created_at": "2008-06-23T09:07:08Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Notes on Elliptic curves documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3493",
    "user": "ljpk"
}
```
Assignee: tba

In part 37.8 of the Reference Manual (the Elliptic curves over finite fields section) there are some formatting issues. For instance, in the section on the frobenius_polynomial, we have the sentence:


```
The Frobenius endomorphism of the elliptic curve has quadratic characteristic polynomial. 
In most cases this is irreducible and defines an imaginary quadratic order; 
for some supersingular curves, Frobenius is an integer a and the polynomial is 1703#326 .}}}

I assume that the 1703#326 is some sort of broken formatting code.

There are similar examples throughout this page.

On a slightly different tack, in the documentation for cardinality and order, it would be helpful to say that "sea" (as in the algorithm) means Schoof-Elkies-Atkin.

Issue created by migration from https://trac.sagemath.org/ticket/3493





---

archive/issue_comments_024600.json:
```json
{
    "body": "The strange omission or garblings are all for pieces of docstrings in LaTeX format, i.e. between $...$.  But there are many other such parts of docstrings which display fine.  So I don't know why some don't come out right.",
    "created_at": "2008-08-01T02:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3493#issuecomment-24600",
    "user": "cremona"
}
```

The strange omission or garblings are all for pieces of docstrings in LaTeX format, i.e. between $...$.  But there are many other such parts of docstrings which display fine.  So I don't know why some don't come out right.



---

archive/issue_comments_024601.json:
```json
{
    "body": "The first issue doesn't seem to be a problem with the new documentation.  I'm attaching a patch for the second one ('sea').",
    "created_at": "2009-02-26T17:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3493#issuecomment-24601",
    "user": "jhpalmieri"
}
```

The first issue doesn't seem to be a problem with the new documentation.  I'm attaching a patch for the second one ('sea').



---

archive/issue_comments_024602.json:
```json
{
    "body": "Attachment [3493.patch](tarball://root/attachments/some-uuid/ticket3493/3493.patch) by jhpalmieri created at 2009-02-26 17:21:00",
    "created_at": "2009-02-26T17:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3493#issuecomment-24602",
    "user": "jhpalmieri"
}
```

Attachment [3493.patch](tarball://root/attachments/some-uuid/ticket3493/3493.patch) by jhpalmieri created at 2009-02-26 17:21:00



---

archive/issue_comments_024603.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T22:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3493#issuecomment-24603",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_024604.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T22:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3493#issuecomment-24604",
    "user": "mabshoff"
}
```

Resolution: fixed
