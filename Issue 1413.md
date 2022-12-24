# Issue 1413: added _sig_on/_sig_off to mpolynomial_libsingular

archive/issues_001413.json:
```json
{
    "body": "Assignee: was\n\nA few of these were annoying me so I tried to do all the obvious ones.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1413\n\n",
    "created_at": "2007-12-06T20:34:55Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "added _sig_on/_sig_off to mpolynomial_libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1413",
    "user": "jbmohler"
}
```
Assignee: was

A few of these were annoying me so I tried to do all the obvious ones.

Issue created by migration from https://trac.sagemath.org/ticket/1413





---

archive/issue_comments_009109.json:
```json
{
    "body": "I don't like this approach because it slows down small examples a lot. At least some heuristic when to apply `_sig_on`/`_sig_off` should be used, e.g. the number of monomials of the polynomials involved.",
    "created_at": "2007-12-07T11:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9109",
    "user": "malb"
}
```

I don't like this approach because it slows down small examples a lot. At least some heuristic when to apply `_sig_on`/`_sig_off` should be used, e.g. the number of monomials of the polynomials involved.



---

archive/issue_comments_009110.json:
```json
{
    "body": "here's a new patch to review after was' comments.  I've checked the lengths and required polys to be 10-15 monomials in length before kicking in the _sig_on",
    "created_at": "2007-12-19T02:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9110",
    "user": "jbmohler"
}
```

here's a new patch to review after was' comments.  I've checked the lengths and required polys to be 10-15 monomials in length before kicking in the _sig_on



---

archive/issue_comments_009111.json:
```json
{
    "body": "I don't like this patch since I assume that libSingular offers some function that provides the length of a polynomial instantly. The patch now iterates over up to 15 monomials for each polynomial which just seems wrong. If I have some time I will check how much of a performance impact this has, but multiplying polynomials with 15 terms or so should be instant anyway, so I don't see the need for sig_on & sig_off. \n\nJoel: what is the motivation behind this patch? Are there actual cases where you need this? I also thing that sending signals to libSingular while it is multiplying polynomials won't be very beneficial and might leave us with some sort of potential corruption. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-22T15:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9111",
    "user": "mabshoff"
}
```

I don't like this patch since I assume that libSingular offers some function that provides the length of a polynomial instantly. The patch now iterates over up to 15 monomials for each polynomial which just seems wrong. If I have some time I will check how much of a performance impact this has, but multiplying polynomials with 15 terms or so should be instant anyway, so I don't see the need for sig_on & sig_off. 

Joel: what is the motivation behind this patch? Are there actual cases where you need this? I also thing that sending signals to libSingular while it is multiplying polynomials won't be very beneficial and might leave us with some sort of potential corruption. 

Cheers,

Michael



---

archive/issue_comments_009112.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2008-01-24T09:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9112",
    "user": "AlexGhitza"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_009113.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-01-24T09:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9113",
    "user": "AlexGhitza"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_009114.json:
```json
{
    "body": "I'm attaching another patch in response to mabshoff's review.  There is, in fact, a pLength singular API.\n\nNote that this does the _sig_xx stuff for the code in these methods:\n__pow__,__floordiv__,factor,gcd,lcm,quo_rem,resultant\nObviously, it would be trivial to make data large enough so that any of these take an eternity to compute.\n\nAs to the corruption issues with a signal.  Huh?  It's the same story with virtually every other _sig_on/_sig_off in the sage code.  One should *expect* memory leaks and tolerate corruption with any of them.",
    "created_at": "2008-01-31T18:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9114",
    "user": "jbmohler"
}
```

I'm attaching another patch in response to mabshoff's review.  There is, in fact, a pLength singular API.

Note that this does the _sig_xx stuff for the code in these methods:
__pow__,__floordiv__,factor,gcd,lcm,quo_rem,resultant
Obviously, it would be trivial to make data large enough so that any of these take an eternity to compute.

As to the corruption issues with a signal.  Huh?  It's the same story with virtually every other _sig_on/_sig_off in the sage code.  One should *expect* memory leaks and tolerate corruption with any of them.



---

archive/issue_comments_009115.json:
```json
{
    "body": "Replying to [comment:8 jbmohler]:\n> I'm attaching another patch in response to mabshoff's review.  There is, in fact,\n> a pLength singular API.\n\nThis function also loops through the polynomial:\n\n\n```\nPINLINE0 int pLength(poly a)\n{\n  int l = 0;\n  while (a!=NULL) {\n    pIter(a);\n    l++;\n  }\n  return l;\n}\n```\n\n\nHowever, I'd say we should still apply this patch and see if something gets too slow. Also, all algorithms which involve `_sig_on`/`_sig_off` should be at least quadratic in the number of monomials so this linear operation shouldn't matter anyway, right?\n\n> Note that this does the _sig_xx stuff for the code in these methods:\n> __pow__,__floordiv__,factor,gcd,lcm,quo_rem,resultant\n> Obviously, it would be trivial to make data large enough so that any of these take an eternity to compute.\n\n> As to the corruption issues with a signal.  Huh?  It's the same story with\n> virtually every other _sig_on/_sig_off in the sage code.  One should *expect*\n> memory leaks and tolerate corruption with any of them.\n\nI second that.\n\nHowever, the patch fails to apply to 2.10.1.rc2\n\n\n```\napplying /home/malb/_sig_on_libsingular.patch\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #2 succeeded at 3105 with fuzz 1 (offset 0 lines).\nHunk #3 FAILED at 3167\n1 out of 7 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-01-31T21:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9115",
    "user": "malb"
}
```

Replying to [comment:8 jbmohler]:
> I'm attaching another patch in response to mabshoff's review.  There is, in fact,
> a pLength singular API.

This function also loops through the polynomial:


```
PINLINE0 int pLength(poly a)
{
  int l = 0;
  while (a!=NULL) {
    pIter(a);
    l++;
  }
  return l;
}
```


However, I'd say we should still apply this patch and see if something gets too slow. Also, all algorithms which involve `_sig_on`/`_sig_off` should be at least quadratic in the number of monomials so this linear operation shouldn't matter anyway, right?

> Note that this does the _sig_xx stuff for the code in these methods:
> __pow__,__floordiv__,factor,gcd,lcm,quo_rem,resultant
> Obviously, it would be trivial to make data large enough so that any of these take an eternity to compute.

> As to the corruption issues with a signal.  Huh?  It's the same story with
> virtually every other _sig_on/_sig_off in the sage code.  One should *expect*
> memory leaks and tolerate corruption with any of them.

I second that.

However, the patch fails to apply to 2.10.1.rc2


```
applying /home/malb/_sig_on_libsingular.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #2 succeeded at 3105 with fuzz 1 (offset 0 lines).
Hunk #3 FAILED at 3167
1 out of 7 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_009116.json:
```json
{
    "body": "To make my statement more precise: In case the merge conflict gets resolved I am happy to give this patch a positive review.",
    "created_at": "2008-02-13T13:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9116",
    "user": "malb"
}
```

To make my statement more precise: In case the merge conflict gets resolved I am happy to give this patch a positive review.



---

archive/issue_comments_009117.json:
```json
{
    "body": "Here's another patch against 2.10.2.  In the name of being anal, I added a polyLengthBounded cdef function which caps the monomial counting for speed.  Although, I agree with malb that this is probably irrelevant given that these algorithms are probably quadratic (certainly not linear).",
    "created_at": "2008-02-14T18:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9117",
    "user": "jbmohler"
}
```

Here's another patch against 2.10.2.  In the name of being anal, I added a polyLengthBounded cdef function which caps the monomial counting for speed.  Although, I agree with malb that this is probably irrelevant given that these algorithms are probably quadratic (certainly not linear).



---

archive/issue_comments_009118.json:
```json
{
    "body": "patch against 2.10.1",
    "created_at": "2008-02-14T18:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9118",
    "user": "jbmohler"
}
```

patch against 2.10.1



---

archive/issue_comments_009119.json:
```json
{
    "body": "Attachment [_sig_on_libsingular.patch](tarball://root/attachments/some-uuid/ticket1413/_sig_on_libsingular.patch) by jbmohler created at 2008-02-14 18:17:55",
    "created_at": "2008-02-14T18:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9119",
    "user": "jbmohler"
}
```

Attachment [_sig_on_libsingular.patch](tarball://root/attachments/some-uuid/ticket1413/_sig_on_libsingular.patch) by jbmohler created at 2008-02-14 18:17:55



---

archive/issue_comments_009120.json:
```json
{
    "body": "`_sig_on_libsingular.patch` applies cleanly against my 2.10.2.alpha0, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T18:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9120",
    "user": "mabshoff"
}
```

`_sig_on_libsingular.patch` applies cleanly against my 2.10.2.alpha0, so positive review.

Cheers,

Michael



---

archive/issue_comments_009121.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T18:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9121",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_009122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T18:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1413#issuecomment-9122",
    "user": "mabshoff"
}
```

Resolution: fixed
