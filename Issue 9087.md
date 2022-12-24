# Issue 9087: implement supersingular/ordinary testing for elliptic curves over finite fields

archive/issues_009087.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  kohel alexghitza\n\nKeywords: super singular ordinary elliptic curves\n\nI have implemented methods is_ordinary() and is_supersingular() for elliptic curves over finite fields, together with functions supersingular_j_polynomial(p) returning a polynomial over GF(p) whose roots are the supersingular j-invariants in characteristic p, a dict storing the precomputed output of this for p<300, and a function is_j_supersingular(j) testing whether a finite field element j is a supersingular j-invariant.\n\nA patch will be ready shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9087\n\n",
    "created_at": "2010-05-29T19:30:54Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "title": "implement supersingular/ordinary testing for elliptic curves over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9087",
    "user": "cremona"
}
```
Assignee: cremona

CC:  kohel alexghitza

Keywords: super singular ordinary elliptic curves

I have implemented methods is_ordinary() and is_supersingular() for elliptic curves over finite fields, together with functions supersingular_j_polynomial(p) returning a polynomial over GF(p) whose roots are the supersingular j-invariants in characteristic p, a dict storing the precomputed output of this for p<300, and a function is_j_supersingular(j) testing whether a finite field element j is a supersingular j-invariant.

A patch will be ready shortly.

Issue created by migration from https://trac.sagemath.org/ticket/9087





---

archive/issue_comments_084386.json:
```json
{
    "body": "Apply after #9052 patches, to 4.4.3.alpha0",
    "created_at": "2010-05-30T11:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84386",
    "user": "cremona"
}
```

Apply after #9052 patches, to 4.4.3.alpha0



---

archive/issue_comments_084387.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-30T11:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84387",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084388.json:
```json
{
    "body": "Attachment [trac_9087-supersingular.patch](tarball://root/attachments/some-uuid/ticket9087/trac_9087-supersingular.patch) by cremona created at 2010-05-30 11:29:44\n\nNote that this implementation is independent of the related patch #9052 which implements Hasse invariants.  It is also independent of related functions in modular/ssmod.  I am CC'ing David Kohel sine he wrote similar functions for Magma (I believe;  of course the code here has been written completely independently of that!)",
    "created_at": "2010-05-30T11:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84388",
    "user": "cremona"
}
```

Attachment [trac_9087-supersingular.patch](tarball://root/attachments/some-uuid/ticket9087/trac_9087-supersingular.patch) by cremona created at 2010-05-30 11:29:44

Note that this implementation is independent of the related patch #9052 which implements Hasse invariants.  It is also independent of related functions in modular/ssmod.  I am CC'ing David Kohel sine he wrote similar functions for Magma (I believe;  of course the code here has been written completely independently of that!)



---

archive/issue_comments_084389.json:
```json
{
    "body": "I have run the tests on it. They all passed (apart from an unrelated problem) so I am willing to give a positive review.\n\nI had a look at the code and I am confident that it computes what it claims, although I have not checked every little detail (such as the list of polynomials).",
    "created_at": "2010-06-15T12:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84389",
    "user": "wuthrich"
}
```

I have run the tests on it. They all passed (apart from an unrelated problem) so I am willing to give a positive review.

I had a look at the code and I am confident that it computes what it claims, although I have not checked every little detail (such as the list of polynomials).



---

archive/issue_comments_084390.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T12:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84390",
    "user": "wuthrich"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084391.json:
```json
{
    "body": "Thanks.  As part of my testing, I (a) compared the polynomials individually with the ones printed in Antwerp IV, and (b) for all p in the precomputed range and for every j mod p, I constructed an elliptic curve with that j and counted its points and made sure that the supersingular j were exactly the ones which this function said were supersingular!",
    "created_at": "2010-06-15T12:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84391",
    "user": "cremona"
}
```

Thanks.  As part of my testing, I (a) compared the polynomials individually with the ones printed in Antwerp IV, and (b) for all p in the precomputed range and for every j mod p, I constructed an elliptic curve with that j and counted its points and made sure that the supersingular j were exactly the ones which this function said were supersingular!



---

archive/issue_comments_084392.json:
```json
{
    "body": "... and I totally agree that this should be enough !\nThanks John.",
    "created_at": "2010-06-15T13:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84392",
    "user": "wuthrich"
}
```

... and I totally agree that this should be enough !
Thanks John.



---

archive/issue_comments_084393.json:
```json
{
    "body": "Attachment [trac_9087-supersingular-untabified.patch](tarball://root/attachments/some-uuid/ticket9087/trac_9087-supersingular-untabified.patch) by davidloeffler created at 2010-06-30 17:29:41\n\nVersion without tabs - apply only this patch",
    "created_at": "2010-06-30T17:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84393",
    "user": "davidloeffler"
}
```

Attachment [trac_9087-supersingular-untabified.patch](tarball://root/attachments/some-uuid/ticket9087/trac_9087-supersingular-untabified.patch) by davidloeffler created at 2010-06-30 17:29:41

Version without tabs - apply only this patch



---

archive/issue_comments_084394.json:
```json
{
    "body": "The patch `trac_9087-supersingular.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.",
    "created_at": "2010-06-30T17:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84394",
    "user": "davidloeffler"
}
```

The patch `trac_9087-supersingular.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.



---

archive/issue_comments_084395.json:
```json
{
    "body": "Very sorry, I was sure that I had fixed up my .emacs on all machines I ever use so this would never happen.  But obviously not...",
    "created_at": "2010-06-30T17:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84395",
    "user": "cremona"
}
```

Very sorry, I was sure that I had fixed up my .emacs on all machines I ever use so this would never happen.  But obviously not...



---

archive/issue_comments_084396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9087#issuecomment-84396",
    "user": "mpatel"
}
```

Resolution: fixed
