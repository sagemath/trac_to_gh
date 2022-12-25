# Issue 9287: improving doctest coverage for elliptic curves

archive/issues_009287.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  wstein\n\nKeywords: doctest coverage\n\nThe bad files are\n\n* BSD.py 85% (6 of 7)\n* ell_egros.py 85% (6 of 7)\n* ell_modular_symbols.py 86% (13 of 15)\n* gp_cremona.py 85% (6 of 7)\n* gp_simon.py 50% (1 of 2)\n* mod5family.py 0% (0 of 1)\n* monsky_washnitzer.py 26% (28 of 107)\n* padic_height.py 0% (0 of 6) #deprecated\n* padic_lseries.py 59% (19 of 32)\n* padics.py 83% (10 of 12)\n* sea.py 0% (0 of 1)\n* sha_tate.py 80% (8 of 10)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9287\n\n",
    "created_at": "2010-06-20T23:40:48Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "improving doctest coverage for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9287",
    "user": "https://github.com/categorie"
}
```
Assignee: @JohnCremona

CC:  wstein

Keywords: doctest coverage

The bad files are

* BSD.py 85% (6 of 7)
* ell_egros.py 85% (6 of 7)
* ell_modular_symbols.py 86% (13 of 15)
* gp_cremona.py 85% (6 of 7)
* gp_simon.py 50% (1 of 2)
* mod5family.py 0% (0 of 1)
* monsky_washnitzer.py 26% (28 of 107)
* padic_height.py 0% (0 of 6) #deprecated
* padic_lseries.py 59% (19 of 32)
* padics.py 83% (10 of 12)
* sea.py 0% (0 of 1)
* sha_tate.py 80% (8 of 10)

Issue created by migration from https://trac.sagemath.org/ticket/9287





---

archive/issue_comments_087333.json:
```json
{
    "body": "So far I have dealt with \n\n* padic_lseries.py\n* modular_parametrization.py\n* padics.py\n\n... more to come",
    "created_at": "2010-06-20T23:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87333",
    "user": "https://github.com/categorie"
}
```

So far I have dealt with 

* padic_lseries.py
* modular_parametrization.py
* padics.py

... more to come



---

archive/issue_comments_087334.json:
```json
{
    "body": "Attachment [trac_9287.coverage_for_elliptic_curves_part1.patch](tarball://root/attachments/some-uuid/ticket9287/trac_9287.coverage_for_elliptic_curves_part1.patch) by @categorie created at 2010-06-20 23:45:24\n\nexported against 4.4.4.alpha0",
    "created_at": "2010-06-20T23:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87334",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9287.coverage_for_elliptic_curves_part1.patch](tarball://root/attachments/some-uuid/ticket9287/trac_9287.coverage_for_elliptic_curves_part1.patch) by @categorie created at 2010-06-20 23:45:24

exported against 4.4.4.alpha0



---

archive/issue_comments_087335.json:
```json
{
    "body": "also exported against 4.4.4.alpha0",
    "created_at": "2010-06-22T17:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87335",
    "user": "https://github.com/categorie"
}
```

also exported against 4.4.4.alpha0



---

archive/issue_comments_087336.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-22T17:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87336",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087337.json:
```json
{
    "body": "Attachment [trac_9287.coverage_for_elliptic_curves_part2.patch](tarball://root/attachments/some-uuid/ticket9287/trac_9287.coverage_for_elliptic_curves_part2.patch) by @categorie created at 2010-06-22 17:52:15\n\nThe second patch (indep of the first) takes care of\n\n* ell_modular_symbol\n* sha_tate\n* ell_torsion\n\nSee trac ticket #9313 of how to take care of padic_height.py\n\nThat is how far I will do improve the documentation so far. If someone else would like to improve it further either put it back to needs_work and continue the work here or (prefered by me) open a new ticket.",
    "created_at": "2010-06-22T17:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87337",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9287.coverage_for_elliptic_curves_part2.patch](tarball://root/attachments/some-uuid/ticket9287/trac_9287.coverage_for_elliptic_curves_part2.patch) by @categorie created at 2010-06-22 17:52:15

The second patch (indep of the first) takes care of

* ell_modular_symbol
* sha_tate
* ell_torsion

See trac ticket #9313 of how to take care of padic_height.py

That is how far I will do improve the documentation so far. If someone else would like to improve it further either put it back to needs_work and continue the work here or (prefered by me) open a new ticket.



---

archive/issue_comments_087338.json:
```json
{
    "body": "Patches apply fine to 4.4.4.alpha0, and test pass, and docs build and look fine!",
    "created_at": "2010-06-23T00:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87338",
    "user": "https://github.com/JohnCremona"
}
```

Patches apply fine to 4.4.4.alpha0, and test pass, and docs build and look fine!



---

archive/issue_comments_087339.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T00:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87339",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087340.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9287#issuecomment-87340",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
