# Issue 2440: Doctests for rings/quotient_ring.py

archive/issues_002440.json:
```json
{
    "body": "Assignee: cswiercz\n\nKeywords: docstring, doctest\n\nProvide missing docstrings and doctests for rings/quotient_ring.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2440\n\n",
    "created_at": "2008-03-09T18:38:38Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Doctests for rings/quotient_ring.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2440",
    "user": "cswiercz"
}
```
Assignee: cswiercz

Keywords: docstring, doctest

Provide missing docstrings and doctests for rings/quotient_ring.py.

Issue created by migration from https://trac.sagemath.org/ticket/2440





---

archive/issue_comments_016506.json:
```json
{
    "body": "When testing QuotientRing_generic.cover_ring, I ran into an issue with evaluating the cover ring of a polynomial quotient ring. Apparently, the PolynomialQuotientRings_field object doesn't have a \"cover_ring\" function! Can the class just \"borrow\" from the QuotientRing_generic class?",
    "created_at": "2008-03-09T19:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16506",
    "user": "cswiercz"
}
```

When testing QuotientRing_generic.cover_ring, I ran into an issue with evaluating the cover ring of a polynomial quotient ring. Apparently, the PolynomialQuotientRings_field object doesn't have a "cover_ring" function! Can the class just "borrow" from the QuotientRing_generic class?



---

archive/issue_comments_016507.json:
```json
{
    "body": "The above observation was written as a TODO in rings/quotient_ring.py under the cover_ring function.",
    "created_at": "2008-03-09T19:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16507",
    "user": "cswiercz"
}
```

The above observation was written as a TODO in rings/quotient_ring.py under the cover_ring function.



---

archive/issue_comments_016508.json:
```json
{
    "body": "Looking at the code for QuotientRing_generic.ideal, it seems that this is not the \"general\" code for creating an ideal in a ring. There are several Singular related calls. I'm not sure what some of these things mean so hopefully someone will be willing to take a look and provide some documentation.",
    "created_at": "2008-03-09T19:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16508",
    "user": "cswiercz"
}
```

Looking at the code for QuotientRing_generic.ideal, it seems that this is not the "general" code for creating an ideal in a ring. There are several Singular related calls. I'm not sure what some of these things mean so hopefully someone will be willing to take a look and provide some documentation.



---

archive/issue_comments_016509.json:
```json
{
    "body": "Docstrings and doctests for non-underscore functions in rings/quotient_ring.py. Some functions returning NotImplementedError have been documented as TODO items.",
    "created_at": "2008-03-09T19:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16509",
    "user": "cswiercz"
}
```

Docstrings and doctests for non-underscore functions in rings/quotient_ring.py. Some functions returning NotImplementedError have been documented as TODO items.



---

archive/issue_comments_016510.json:
```json
{
    "body": "Attachment [rings.quotient_ring.patch](tarball://root/attachments/some-uuid/ticket2440/rings.quotient_ring.patch) by cswiercz created at 2008-03-09 19:38:43",
    "created_at": "2008-03-09T19:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16510",
    "user": "cswiercz"
}
```

Attachment [rings.quotient_ring.patch](tarball://root/attachments/some-uuid/ticket2440/rings.quotient_ring.patch) by cswiercz created at 2008-03-09 19:38:43



---

archive/issue_comments_016511.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-09T19:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16511",
    "user": "cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016512.json:
```json
{
    "body": "Review:\n\nExcellent.\n\nAbout characteristic():  should not be hard to implement in at least one case:  Set c = self.base_ring().characteristic().  If c is prime then self's char is also p.  If c>0 but is not prime one could loop through divisors d of c to see if self(d)==self(0).   But if c==0 I cannot see an easy way of doing this.\n\nAbout gens(): I agree that it is not nice having 0 in the list of gens, but deleting them would break the correspondance between the gens of R and the gens of R/I, which the user will probably expect.\n\nI also noticed one thing which is not purely a docstring/test:  when R is a field you inserted a short-cut.  That looks fine to me.\n\nPositive review, should be accepted.",
    "created_at": "2008-03-09T20:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16512",
    "user": "cremona"
}
```

Review:

Excellent.

About characteristic():  should not be hard to implement in at least one case:  Set c = self.base_ring().characteristic().  If c is prime then self's char is also p.  If c>0 but is not prime one could loop through divisors d of c to see if self(d)==self(0).   But if c==0 I cannot see an easy way of doing this.

About gens(): I agree that it is not nice having 0 in the list of gens, but deleting them would break the correspondance between the gens of R and the gens of R/I, which the user will probably expect.

I also noticed one thing which is not purely a docstring/test:  when R is a field you inserted a short-cut.  That looks fine to me.

Positive review, should be accepted.



---

archive/issue_comments_016513.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-09T21:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16513",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc4



---

archive/issue_comments_016514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-09T21:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2440#issuecomment-16514",
    "user": "mabshoff"
}
```

Resolution: fixed
