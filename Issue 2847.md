# Issue 2847: [with patch, needs review] more speedups to cyclotomic polynomials

archive/issues_002847.json:
```json
{
    "body": "Assignee: somebody\n\nUse some data provided by Michael Monagan, as well as take advantage of the fact (mentioned in the previous ticket by John Cremona) that $\\Phi_{pn}(x) = \\Phi_n(x^p)$ for $p|n$.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2847\n\n",
    "created_at": "2008-04-07T19:32:03Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] more speedups to cyclotomic polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2847",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

Use some data provided by Michael Monagan, as well as take advantage of the fact (mentioned in the previous ticket by John Cremona) that $\Phi_{pn}(x) = \Phi_n(x^p)$ for $p|n$.

Issue created by migration from https://trac.sagemath.org/ticket/2847





---

archive/issue_comments_019493.json:
```json
{
    "body": "Attachment [2847-cyclo-radical.patch](tarball://root/attachments/some-uuid/ticket2847/2847-cyclo-radical.patch) by @robertwb created at 2008-04-07 19:33:26",
    "created_at": "2008-04-07T19:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19493",
    "user": "https://github.com/robertwb"
}
```

Attachment [2847-cyclo-radical.patch](tarball://root/attachments/some-uuid/ticket2847/2847-cyclo-radical.patch) by @robertwb created at 2008-04-07 19:33:26



---

archive/issue_comments_019494.json:
```json
{
    "body": "Code looks fine to me.  I haven't checked it yet as my machine is tied up doing --testall on 3.0.alpha2.",
    "created_at": "2008-04-07T19:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19494",
    "user": "https://github.com/JohnCremona"
}
```

Code looks fine to me.  I haven't checked it yet as my machine is tied up doing --testall on 3.0.alpha2.



---

archive/issue_comments_019495.json:
```json
{
    "body": "The patch currently does not apply against my tree:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2847-cyclo-limits.patch\npatching file sage/rings/polynomial/cyclotomic.pyx\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2847-cyclo-radical.patch\npatching file sage/rings/polynomial/cyclotomic.pyx\nHunk #1 FAILED at 72.\n1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/cyclotomic.pyx.rej\n```\n\nFeel free to rebase against /scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T20:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch currently does not apply against my tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2847-cyclo-limits.patch
patching file sage/rings/polynomial/cyclotomic.pyx
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2847-cyclo-radical.patch
patching file sage/rings/polynomial/cyclotomic.pyx
Hunk #1 FAILED at 72.
1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/cyclotomic.pyx.rej
```

Feel free to rebase against /scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage

Cheers,

Michael



---

archive/issue_comments_019496.json:
```json
{
    "body": "Attachment [2847-cyclo-radical-rebased.patch](tarball://root/attachments/some-uuid/ticket2847/2847-cyclo-radical-rebased.patch) by @robertwb created at 2008-04-09 03:39:41",
    "created_at": "2008-04-09T03:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19496",
    "user": "https://github.com/robertwb"
}
```

Attachment [2847-cyclo-radical-rebased.patch](tarball://root/attachments/some-uuid/ticket2847/2847-cyclo-radical-rebased.patch) by @robertwb created at 2008-04-09 03:39:41



---

archive/issue_comments_019497.json:
```json
{
    "body": "It was just a conflict with a random doctest. I rebased it against 3.0.alpha3. Apply 2847-cyclo-limits.patch and 2847-cyclo-radical-rebased.patch.",
    "created_at": "2008-04-09T03:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19497",
    "user": "https://github.com/robertwb"
}
```

It was just a conflict with a random doctest. I rebased it against 3.0.alpha3. Apply 2847-cyclo-limits.patch and 2847-cyclo-radical-rebased.patch.



---

archive/issue_comments_019498.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-09T03:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19498",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_003037.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-09T04:07:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2847#event-3037"
}
```



---

archive/issue_comments_019499.json:
```json
{
    "body": "Merged 2847-cyclo-limits.patch and 2847-cyclo-radical-rebased.patch in Sage 3.0.alpha3",
    "created_at": "2008-04-09T04:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2847-cyclo-limits.patch and 2847-cyclo-radical-rebased.patch in Sage 3.0.alpha3



---

archive/issue_comments_019500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T04:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19500",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019501.json:
```json
{
    "body": "Hmm, after merging those two patches I get a new doctest failure:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/polynomial_ring.py\", line 582:\n    sage: S.cyclotomic_polynomial(12)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_18[5]>\", line 1, in <module>\n        S.cyclotomic_polynomial(Integer(12))###line 582:\n    sage: S.cyclotomic_polynomial(12)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 600, in cyclotomic_polynomial\n        return self(cyclotomic.cyclotomic_coeffs(n), check=True)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 1058, in __call__\n        return polynomial_modn_dense_ntl.Polynomial_dense_mod_p(self, x, check, is_gen,construct=construct)\n      File \"polynomial_modn_dense_ntl.pyx\", line 101, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.__init__\n        x = self._dict_to_list(x, R(0))\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_18\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/.doctest_polynomial_ring.py\n\n         [3.3 s]\n\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 3.3 seconds\n```\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T04:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, after merging those two patches I get a new doctest failure:

```
sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/polynomial_ring.py", line 582:
    sage: S.cyclotomic_polynomial(12)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[5]>", line 1, in <module>
        S.cyclotomic_polynomial(Integer(12))###line 582:
    sage: S.cyclotomic_polynomial(12)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 600, in cyclotomic_polynomial
        return self(cyclotomic.cyclotomic_coeffs(n), check=True)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 1058, in __call__
        return polynomial_modn_dense_ntl.Polynomial_dense_mod_p(self, x, check, is_gen,construct=construct)
      File "polynomial_modn_dense_ntl.pyx", line 101, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.__init__
        x = self._dict_to_list(x, R(0))
    TypeError: 'NoneType' object is not callable
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/.doctest_polynomial_ring.py

         [3.3 s]

The following tests failed:

        sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 3.3 seconds
```

Thoughts?

Cheers,

Michael



---

archive/issue_comments_019502.json:
```json
{
    "body": "Attachment [2847-Zn_x-fix.patch](tarball://root/attachments/some-uuid/ticket2847/2847-Zn_x-fix.patch) by @robertwb created at 2008-04-09 04:39:46\n\nLooks like this exposed a bug in the (Z/nZ)[x] __init__ method, which I have fixed in the attached patch.",
    "created_at": "2008-04-09T04:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19502",
    "user": "https://github.com/robertwb"
}
```

Attachment [2847-Zn_x-fix.patch](tarball://root/attachments/some-uuid/ticket2847/2847-Zn_x-fix.patch) by @robertwb created at 2008-04-09 04:39:46

Looks like this exposed a bug in the (Z/nZ)[x] __init__ method, which I have fixed in the attached patch.



---

archive/issue_comments_019503.json:
```json
{
    "body": "Thanks Robert. 2847-Zn_x-fix.patch fixes the issue. Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-09T05:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2847#issuecomment-19503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks Robert. 2847-Zn_x-fix.patch fixes the issue. Merged in Sage 3.0.alpha3
