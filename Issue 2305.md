# Issue 2305: Docstrings and doctests for rings/ideal.py

archive/issues_002305.json:
```json
{
    "body": "Assignee: @cswiercz\n\nKeywords: docstring, doctest\n\nProvide missing docstrings and doctests for all non-\"_\" functions in rings/ideal.py. These include:\n\nid_Ideal(x)\nbase_ring(self)\nis_maximal(self)\nis_prime(self)\nis_principal(self)\nis_principal(self)\ngen(self)\ngcd(self, other)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2305\n\n",
    "created_at": "2008-02-25T21:48:54Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Docstrings and doctests for rings/ideal.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2305",
    "user": "https://github.com/cswiercz"
}
```
Assignee: @cswiercz

Keywords: docstring, doctest

Provide missing docstrings and doctests for all non-"_" functions in rings/ideal.py. These include:

id_Ideal(x)
base_ring(self)
is_maximal(self)
is_prime(self)
is_principal(self)
is_principal(self)
gen(self)
gcd(self, other)

Issue created by migration from https://trac.sagemath.org/ticket/2305





---

archive/issue_comments_015304.json:
```json
{
    "body": "Attachment [ring.ideal.patch](tarball://root/attachments/some-uuid/ticket2305/ring.ideal.patch) by @cswiercz created at 2008-02-27 23:39:15\n\nRemaining docstrings and doctetst for rings/ideal.py",
    "created_at": "2008-02-27T23:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15304",
    "user": "https://github.com/cswiercz"
}
```

Attachment [ring.ideal.patch](tarball://root/attachments/some-uuid/ticket2305/ring.ideal.patch) by @cswiercz created at 2008-02-27 23:39:15

Remaining docstrings and doctetst for rings/ideal.py



---

archive/issue_comments_015305.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-27T23:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15305",
    "user": "https://github.com/cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015306.json:
```json
{
    "body": "The patch is mostly fine, but there are some formatting issues.\n\nThis looks wrong:\n\n```\n \t155\t        sage: R = ZZ\n \t156\t        sage: R; is_Ideal(R) \n \t157\t        Integer Ring \n \t158\t        False \n```\n\n\nPlease typeset sage's output all on one line.  So rather than\n\n\n```\n \t168\t        sage: I = R.ideal(x^2 + 1); I \n \t169\t        Principal ideal (x^2 + 1) of Univariate Polynomial Ring in x over \n \t170\t        Rational Field \n```\n\n\ngive me\n\n\n```\n \t168\t        sage: I = R.ideal(x^2 + 1); I \n \t169\t        Principal ideal (x^2 + 1) of Univariate Polynomial Ring in x over Rational Field \n```\n\n\nAlso, there are *tons* of typos.  'th' instead of 'the', incorrectly spelled words, etc.  I will work on some emacs code that will spell-check only sage comments, and ignore examples as appropriate, but until then you'll have to do it by hand :)",
    "created_at": "2008-02-28T20:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15306",
    "user": "https://github.com/ncalexan"
}
```

The patch is mostly fine, but there are some formatting issues.

This looks wrong:

```
 	155	        sage: R = ZZ
 	156	        sage: R; is_Ideal(R) 
 	157	        Integer Ring 
 	158	        False 
```


Please typeset sage's output all on one line.  So rather than


```
 	168	        sage: I = R.ideal(x^2 + 1); I 
 	169	        Principal ideal (x^2 + 1) of Univariate Polynomial Ring in x over 
 	170	        Rational Field 
```


give me


```
 	168	        sage: I = R.ideal(x^2 + 1); I 
 	169	        Principal ideal (x^2 + 1) of Univariate Polynomial Ring in x over Rational Field 
```


Also, there are *tons* of typos.  'th' instead of 'the', incorrectly spelled words, etc.  I will work on some emacs code that will spell-check only sage comments, and ignore examples as appropriate, but until then you'll have to do it by hand :)



---

archive/issue_comments_015307.json:
```json
{
    "body": "Attachment [rings.ideal.patch](tarball://root/attachments/some-uuid/ticket2305/rings.ideal.patch) by @cswiercz created at 2008-02-28 23:18:24\n\nCorrected docstring and doctest patch for rings/ideal.py",
    "created_at": "2008-02-28T23:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15307",
    "user": "https://github.com/cswiercz"
}
```

Attachment [rings.ideal.patch](tarball://root/attachments/some-uuid/ticket2305/rings.ideal.patch) by @cswiercz created at 2008-02-28 23:18:24

Corrected docstring and doctest patch for rings/ideal.py



---

archive/issue_comments_015308.json:
```json
{
    "body": "Accidentally renamed the patch. Be sure to review rings.ideal.patch and ignore ring.ideal.patch. Thanks!",
    "created_at": "2008-02-28T23:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15308",
    "user": "https://github.com/cswiercz"
}
```

Accidentally renamed the patch. Be sure to review rings.ideal.patch and ignore ring.ideal.patch. Thanks!



---

archive/issue_comments_015309.json:
```json
{
    "body": "Doctest-formatting looks good and typos are out. So I say apply!",
    "created_at": "2008-03-06T04:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15309",
    "user": "https://github.com/dfdeshom"
}
```

Doctest-formatting looks good and typos are out. So I say apply!



---

archive/issue_comments_015310.json:
```json
{
    "body": "Merged rings.ideal.patch in 2.10.3.rc3. The patch does add a single docstring in numerical/optimize.py, so I am not quite sure if that was intended for this patch.",
    "created_at": "2008-03-07T20:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15310",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged rings.ideal.patch in 2.10.3.rc3. The patch does add a single docstring in numerical/optimize.py, so I am not quite sure if that was intended for this patch.



---

archive/issue_comments_015311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-07T20:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015312.json:
```json
{
    "body": "Sorry for being late to the party, but please open another ticket to address the following minor issues:\n* `def ring` the docstring uses backslashes but is not treated raw: `r\"\"\"` missing\n* \"Note that \\code{self.ring()} is different from \\code{self.ring()}\" seems like a typo",
    "created_at": "2008-03-07T20:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2305#issuecomment-15312",
    "user": "https://github.com/malb"
}
```

Sorry for being late to the party, but please open another ticket to address the following minor issues:
* `def ring` the docstring uses backslashes but is not treated raw: `r"""` missing
* "Note that \code{self.ring()} is different from \code{self.ring()}" seems like a typo
