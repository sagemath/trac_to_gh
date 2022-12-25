# Issue 6514: Boolean function for cryptography

archive/issues_006514.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @malb mvngu\n\nThis module provides a class to study properties such as nonlinearity, resiliency, correlation immunity, algebraic immunity and other cryptographic properties of Boolean functions.\n\nSome of these are still missing, but I think it is a good start.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6514\n\n",
    "created_at": "2009-07-11T18:09:13Z",
    "labels": [
        "component: cryptography"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Boolean function for cryptography",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6514",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: somebody

CC:  @malb mvngu

This module provides a class to study properties such as nonlinearity, resiliency, correlation immunity, algebraic immunity and other cryptographic properties of Boolean functions.

Some of these are still missing, but I think it is a good start.

Issue created by migration from https://trac.sagemath.org/ticket/6514





---

archive/issue_comments_052961.json:
```json
{
    "body": "Changing keywords from \"\" to \"boolean function, cryptography\".",
    "created_at": "2009-07-11T18:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52961",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing keywords from "" to "boolean function, cryptography".



---

archive/issue_comments_052962.json:
```json
{
    "body": "**Review**\n\n* typo: \"This module allow\" -> allows\n* it would be nice to have docs for `walsh`, `yellow_code`, `reed_muller`\n* maybe replace \"BooleanPolynomial\" with \":class:`sage.rings.polynomial.pbori.BooleanPolynomial`\" which adds a link in the reference manual\n* `if isinstance(x, list)` could be changed to `if isinstance(x, (list,tuple,GeneratorType)` to be less dependent on the type, you'll need to `from types import GeneratorType`\n* is it wanted that these don't have a type? `cdef _walsh_transform, _nvariables, _big_endian, _nonlinearity`\n* typo: \"table truth\" -> \"truth table\"\n* cmp doesn't have a proper doctest\n* Maybe put the world \"True\" in  \"``True``\" ?\n* Should() popcount() really return a Python int instead of a Sage integer?\n\n* Patch applies without error but with some fuzz against 4.1 (this isn't an issue)\n* Doctests pass.\n* Reference manual builds without warning.\n* Reference manual looks good.",
    "created_at": "2009-07-15T14:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52962",
    "user": "https://github.com/malb"
}
```

**Review**

* typo: "This module allow" -> allows
* it would be nice to have docs for `walsh`, `yellow_code`, `reed_muller`
* maybe replace "BooleanPolynomial" with ":class:`sage.rings.polynomial.pbori.BooleanPolynomial`" which adds a link in the reference manual
* `if isinstance(x, list)` could be changed to `if isinstance(x, (list,tuple,GeneratorType)` to be less dependent on the type, you'll need to `from types import GeneratorType`
* is it wanted that these don't have a type? `cdef _walsh_transform, _nvariables, _big_endian, _nonlinearity`
* typo: "table truth" -> "truth table"
* cmp doesn't have a proper doctest
* Maybe put the world "True" in  "``True``" ?
* Should() popcount() really return a Python int instead of a Sage integer?

* Patch applies without error but with some fuzz against 4.1 (this isn't an issue)
* Doctests pass.
* Reference manual builds without warning.
* Reference manual looks good.



---

archive/issue_comments_052963.json:
```json
{
    "body": "Is there any movement on this patch, it shouldn't go wasted?",
    "created_at": "2009-08-25T22:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52963",
    "user": "https://github.com/malb"
}
```

Is there any movement on this patch, it shouldn't go wasted?



---

archive/issue_comments_052964.json:
```json
{
    "body": "I've been quite busy, but I'll send a new patch in the very next few days...",
    "created_at": "2009-08-26T07:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52964",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I've been quite busy, but I'll send a new patch in the very next few days...



---

archive/issue_comments_052965.json:
```json
{
    "body": "Attachment [trac_6514_BooleanFunction.patch](tarball://root/attachments/some-uuid/ticket6514/trac_6514_BooleanFunction.patch) by ylchapuy created at 2009-08-28 13:54:48\n\nbased on 4.1.1",
    "created_at": "2009-08-28T13:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52965",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_6514_BooleanFunction.patch](tarball://root/attachments/some-uuid/ticket6514/trac_6514_BooleanFunction.patch) by ylchapuy created at 2009-08-28 13:54:48

based on 4.1.1



---

archive/issue_comments_052966.json:
```json
{
    "body": "Hi,\nhere is an updated patch. I addressed most of Martin's remarks.\npopcount now returns an int, because it's what nbits does.\n\nIf someone wants to try some Boolean functions, he can have a look at http://www.ii.uib.no/~mohamedaa/odbf/search.html and compare the results.",
    "created_at": "2009-08-28T14:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52966",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Hi,
here is an updated patch. I addressed most of Martin's remarks.
popcount now returns an int, because it's what nbits does.

If someone wants to try some Boolean functions, he can have a look at http://www.ii.uib.no/~mohamedaa/odbf/search.html and compare the results.



---

archive/issue_comments_052967.json:
```json
{
    "body": "Hi, even I don't get some of my earlier comments. Sorry, I was in a rush.\n\n* it would be nice to have docs for walsh, yellow_code, reed_muller\n* wouldn't it be more appropriate if `cdef _walsh_transform` was a tuple instead of a list?\n* the patch applies cleanly\n* doctests pass\n* you could consider breaking lines at 80 or 120 characters in the docstrings maybe",
    "created_at": "2009-09-01T10:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52967",
    "user": "https://github.com/malb"
}
```

Hi, even I don't get some of my earlier comments. Sorry, I was in a rush.

* it would be nice to have docs for walsh, yellow_code, reed_muller
* wouldn't it be more appropriate if `cdef _walsh_transform` was a tuple instead of a list?
* the patch applies cleanly
* doctests pass
* you could consider breaking lines at 80 or 120 characters in the docstrings maybe



---

archive/issue_comments_052968.json:
```json
{
    "body": "Hi,\n\nthe last patch\n\n- adds docs to walsh, yellow_code, reed_muller \n- uses tuples instead of lists\n- cuts some long lines\n\nYann",
    "created_at": "2009-09-01T19:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52968",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Hi,

the last patch

- adds docs to walsh, yellow_code, reed_muller 
- uses tuples instead of lists
- cuts some long lines

Yann



---

archive/issue_comments_052969.json:
```json
{
    "body": "Attachment [trac_6514_review.patch](tarball://root/attachments/some-uuid/ticket6514/trac_6514_review.patch) by ylchapuy created at 2009-09-01 19:15:58",
    "created_at": "2009-09-01T19:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52969",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_6514_review.patch](tarball://root/attachments/some-uuid/ticket6514/trac_6514_review.patch) by ylchapuy created at 2009-09-01 19:15:58



---

archive/issue_comments_052970.json:
```json
{
    "body": "Great! Positive review.",
    "created_at": "2009-09-01T19:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52970",
    "user": "https://github.com/malb"
}
```

Great! Positive review.



---

archive/issue_comments_052971.json:
```json
{
    "body": "Attachment [doctest-6514.log](tarball://root/attachments/some-uuid/ticket6514/doctest-6514.log) by mvngu created at 2009-09-02 08:01:06\n\nfull log of doctest failures",
    "created_at": "2009-09-02T08:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52971",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-6514.log](tarball://root/attachments/some-uuid/ticket6514/doctest-6514.log) by mvngu created at 2009-09-02 08:01:06

full log of doctest failures



---

archive/issue_events_006751.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T08:02:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6514#event-6751"
}
```



---

archive/issue_comments_052972.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6514_BooleanFunction.patch`\n2. `trac_6514_review.patch`\n \nRunning the test suite gave me some doctest failures:\n\n```\nsage -t -long devel/sage-main/sage/server/simple/twist.py # 3 doctests failed\nsage -t -long devel/sage-main/sage/server/notebook/notebook.py # 1 doctests failed\n```\n\nA full log is attached. These doctest failures have nothing to do with the above patches; they have been reported before in Sage 4.1.1.",
    "created_at": "2009-09-02T08:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52972",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac_6514_BooleanFunction.patch`
2. `trac_6514_review.patch`
 
Running the test suite gave me some doctest failures:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py # 3 doctests failed
sage -t -long devel/sage-main/sage/server/notebook/notebook.py # 1 doctests failed
```

A full log is attached. These doctest failures have nothing to do with the above patches; they have been reported before in Sage 4.1.1.



---

archive/issue_comments_052973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T08:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6514#issuecomment-52973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
