# Issue 4275: [with patch, needs review] improved doctest for elliptic curves (part 2)

archive/issues_004275.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nThis patch adds missing doctests to ell_modular_symbols.py, ell_number_field.py and\nell_padic_field.py. The conversion to Pari in ell_padic_field.py was broken, and still\nfails in some cases (see example in file), but I don't know if this is a bug in Pari, or\nan invalid input.\n\nI also removed some unused functions in ell_modular_symbols.py, it would be good to check they\nare not needed elsewhere.\n\nNote that some internal functions could not be tested, thus the coverage is not 100%.\n\n```\nbash-3.00$ sage -coverage ell_modular_symbols.py ell_number_field.py ell_padic_field.py\n----------------------------------------------------------------------\nell_modular_symbols.py\nSCORE ell_modular_symbols.py: 100% (6 of 6)\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nell_number_field.py\nSCORE ell_number_field.py: 90% (19 of 21)\n\nMissing documentation:\n         * _proot(x, e):\n         * _pquadroots (a, b, c):\n\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nell_padic_field.py\nSCORE ell_padic_field.py: 80% (4 of 5)\n\nMissing documentation:\n         * _frob(P):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4275\n\n",
    "created_at": "2008-10-13T15:58:25Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] improved doctest for elliptic curves (part 2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4275",
    "user": "@zimmermann6"
}
```
Assignee: @williamstein

CC:  @JohnCremona

This patch adds missing doctests to ell_modular_symbols.py, ell_number_field.py and
ell_padic_field.py. The conversion to Pari in ell_padic_field.py was broken, and still
fails in some cases (see example in file), but I don't know if this is a bug in Pari, or
an invalid input.

I also removed some unused functions in ell_modular_symbols.py, it would be good to check they
are not needed elsewhere.

Note that some internal functions could not be tested, thus the coverage is not 100%.

```
bash-3.00$ sage -coverage ell_modular_symbols.py ell_number_field.py ell_padic_field.py
----------------------------------------------------------------------
ell_modular_symbols.py
SCORE ell_modular_symbols.py: 100% (6 of 6)
----------------------------------------------------------------------

----------------------------------------------------------------------
ell_number_field.py
SCORE ell_number_field.py: 90% (19 of 21)

Missing documentation:
         * _proot(x, e):
         * _pquadroots (a, b, c):

----------------------------------------------------------------------

----------------------------------------------------------------------
ell_padic_field.py
SCORE ell_padic_field.py: 80% (4 of 5)

Missing documentation:
         * _frob(P):
```


Issue created by migration from https://trac.sagemath.org/ticket/4275





---

archive/issue_comments_031215.json:
```json
{
    "body": "Attachment [10554.patch](tarball://root/attachments/some-uuid/ticket4275/10554.patch) by @JohnCremona created at 2008-10-13 16:53:19\n\nPaul, can you say which version (exactly) your patch should apply to?  I failed to apply it to 3.1.3.alpha3, and suspect that some of the changes I made between 3.1.2 and that one conflict with yours.  (For example, I thought I had already converted some \"internal functions\" to lambda functions!)  It is a habit of mine that when I work on a file I try to improve its doctest coverage at the same time, so this is not so surprising!  John",
    "created_at": "2008-10-13T16:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31215",
    "user": "@JohnCremona"
}
```

Attachment [10554.patch](tarball://root/attachments/some-uuid/ticket4275/10554.patch) by @JohnCremona created at 2008-10-13 16:53:19

Paul, can you say which version (exactly) your patch should apply to?  I failed to apply it to 3.1.3.alpha3, and suspect that some of the changes I made between 3.1.2 and that one conflict with yours.  (For example, I thought I had already converted some "internal functions" to lambda functions!)  It is a habit of mine that when I work on a file I try to improve its doctest coverage at the same time, so this is not so surprising!  John



---

archive/issue_comments_031216.json:
```json
{
    "body": "John, my patch should apply to 3.1.2 (I always use the latest release).\nIn the meantime, I have worked on ell_point.py, I hope this will be no duplicate work,\nI will submit it soon.",
    "created_at": "2008-10-13T19:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31216",
    "user": "@zimmermann6"
}
```

John, my patch should apply to 3.1.2 (I always use the latest release).
In the meantime, I have worked on ell_point.py, I hope this will be no duplicate work,
I will submit it soon.



---

archive/issue_comments_031217.json:
```json
{
    "body": "Attachment [10556.patch](tarball://root/attachments/some-uuid/ticket4275/10556.patch) by @zimmermann6 created at 2008-10-14 10:42:34\n\nThe second patch (to be applied after the first one) adds some documentation and one test for the\nPari conversion (thanks Karim Belabas).",
    "created_at": "2008-10-14T10:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31217",
    "user": "@zimmermann6"
}
```

Attachment [10556.patch](tarball://root/attachments/some-uuid/ticket4275/10556.patch) by @zimmermann6 created at 2008-10-14 10:42:34

The second patch (to be applied after the first one) adds some documentation and one test for the
Pari conversion (thanks Karim Belabas).



---

archive/issue_comments_031218.json:
```json
{
    "body": "Attachment [trac_4275_part3.patch](tarball://root/attachments/some-uuid/ticket4275/trac_4275_part3.patch) by @zimmermann6 created at 2008-10-14 19:05:30\n\nThe 3rd patch (to be applied after the first 2) re-enable two methods that were unused in\nell_modular_symbols.py, but one was used elsewhere, and the other one might be useful.",
    "created_at": "2008-10-14T19:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31218",
    "user": "@zimmermann6"
}
```

Attachment [trac_4275_part3.patch](tarball://root/attachments/some-uuid/ticket4275/trac_4275_part3.patch) by @zimmermann6 created at 2008-10-14 19:05:30

The 3rd patch (to be applied after the first 2) re-enable two methods that were unused in
ell_modular_symbols.py, but one was used elsewhere, and the other one might be useful.



---

archive/issue_comments_031219.json:
```json
{
    "body": "Attachment [sage-trac4275.patch](tarball://root/attachments/some-uuid/ticket4275/sage-trac4275.patch) by @JohnCremona created at 2008-10-18 08:54:14\n\nReplaces the three earlier patches",
    "created_at": "2008-10-18T08:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31219",
    "user": "@JohnCremona"
}
```

Attachment [sage-trac4275.patch](tarball://root/attachments/some-uuid/ticket4275/sage-trac4275.patch) by @JohnCremona created at 2008-10-18 08:54:14

Replaces the three earlier patches



---

archive/issue_comments_031220.json:
```json
{
    "body": "The new patch sage-trac4275.patch merges the three previous ones and rebases them on 3.1.4.  Essentially the same as Paul's 3.  I am happy with these being merged.",
    "created_at": "2008-10-18T08:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31220",
    "user": "@JohnCremona"
}
```

The new patch sage-trac4275.patch merges the three previous ones and rebases them on 3.1.4.  Essentially the same as Paul's 3.  I am happy with these being merged.



---

archive/issue_comments_031221.json:
```json
{
    "body": "Thanks John. A quick summary of my (unfinished) doctest work on elliptic curves:\n\n#4271 -> merged in 3.1.3\n\n#4275 (this one): needs review\n\n#4277 positive review, ready to merge\n\n#4281 needs review\n\n#4287 needs review + fix loads/dump problem\n\nI put you in cc to be sure you get this. Feel free to remove yourself.",
    "created_at": "2008-10-18T09:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31221",
    "user": "@zimmermann6"
}
```

Thanks John. A quick summary of my (unfinished) doctest work on elliptic curves:

#4271 -> merged in 3.1.3

#4275 (this one): needs review

#4277 positive review, ready to merge

#4281 needs review

#4287 needs review + fix loads/dump problem

I put you in cc to be sure you get this. Feel free to remove yourself.



---

archive/issue_comments_031222.json:
```json
{
    "body": "Sorry, one should read #4275 (this one): positive review, ready to merge instead of what I wrote\nabove.",
    "created_at": "2008-10-18T09:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31222",
    "user": "@zimmermann6"
}
```

Sorry, one should read #4275 (this one): positive review, ready to merge instead of what I wrote
above.



---

archive/issue_comments_031223.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T19:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31223",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha0



---

archive/issue_comments_031224.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T19:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4275#issuecomment-31224",
    "user": "mabshoff"
}
```

Resolution: fixed
