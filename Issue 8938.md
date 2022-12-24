# Issue 8938: Multivariate polynomials can be incorrectly formatted in LaTeX

archive/issues_008938.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: Multivariate polynomials latex\n\n\n```\nsage: C5.<z> = CyclotomicField(5)\nsage: P.<s, t> = C5[]\nsage: f = (z^2 + z)*s\nsage: f\n(z^2 + z)*s\nsage: latex(f)\nz^{2} + z s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8938\n\n",
    "created_at": "2010-05-09T20:46:29Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "Multivariate polynomials can be incorrectly formatted in LaTeX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8938",
    "user": "fwclarke"
}
```
Assignee: @aghitza

Keywords: Multivariate polynomials latex


```
sage: C5.<z> = CyclotomicField(5)
sage: P.<s, t> = C5[]
sage: f = (z^2 + z)*s
sage: f
(z^2 + z)*s
sage: latex(f)
z^{2} + z s
```


Issue created by migration from https://trac.sagemath.org/ticket/8938





---

archive/issue_comments_082296.json:
```json
{
    "body": "Attachment [trac_8938.patch](tarball://root/attachments/some-uuid/ticket8938/trac_8938.patch) by fwclarke created at 2010-05-09 20:58:36\n\nThe patch solves this problem, providing latex code which is modelled on that used for single-variable polynomials. \u00a0A few doctests have had to be adjusted and LaTeX output provided for elements of QQbar.",
    "created_at": "2010-05-09T20:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82296",
    "user": "fwclarke"
}
```

Attachment [trac_8938.patch](tarball://root/attachments/some-uuid/ticket8938/trac_8938.patch) by fwclarke created at 2010-05-09 20:58:36

The patch solves this problem, providing latex code which is modelled on that used for single-variable polynomials.  A few doctests have had to be adjusted and LaTeX output provided for elements of QQbar.



---

archive/issue_comments_082297.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-09T20:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82297",
    "user": "fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082298.json:
```json
{
    "body": "Applies cleanly, doctests pass, reads good.",
    "created_at": "2010-06-24T08:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82298",
    "user": "@malb"
}
```

Applies cleanly, doctests pass, reads good.



---

archive/issue_comments_082299.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T08:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82299",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082300.json:
```json
{
    "body": "I'm getting doctest failures with this under 4.5.alpha1:\n\n```\nsage -t  \"devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py\"\n**********************************************************************           \nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py\", line 379:                                                                                                    \n    sage: latex(-I*y+I*x^2)                                                                                   \nExpected:                                                                                                     \n    \\sqrt{-1} x^{2} - \\sqrt{-1} y                                                                             \nGot:                                                                                                          \n    \\left(\\sqrt{-1}\\right) x^{2} + \\left(-\\sqrt{-1}\\right) y                                                  \n**********************************************************************                                        \n1 items had failures:                                                                                         \n   1 of   7 in __main__.example_15                                                                            \n***Test Failed*** 1 failures.                                                                                 \nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_multi_polynomial_element.py              \n         [3.7 s]                                                                                              \nsage -t  \"devel/sage-reviewing/sage/rings/qqbar.py\"                                                           \n**********************************************************************                           File \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/qqbar.py\", line 2223:\n    sage: latex(-QQbar.zeta(4) + 5)\nExpected:\n    -i + 5\nGot:\n    -\\sqrt{-1} + 5\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_42\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_qqbar.py\n         [19.5 s]\nsage -t  \"devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py\"\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py\", line 595:\n    sage: S._latex_()\nExpected:\n    '\\\\text{Closed subscheme of } {\\\\mathbf P}_{\\\\Bold{F}_{11}}^2 \\\\text{ defined by } x^{2} - y z'\nGot:\n    '\\\\text{Closed subscheme of } {\\\\mathbf P}_{\\\\Bold{F}_{11}}^2 \\\\text{ defined by } x^{2} + 10 y z'\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py\", line 602:\n    sage: S._latex_()\nExpected:\n    '\\\\text{Closed subscheme of } {\\\\mathbf P}_{\\\\Bold{F}_{11}}^2 \\\\text{ defined by } x^{2} - y z, x^{5}'\nGot:\n    '\\\\text{Closed subscheme of } {\\\\mathbf P}_{\\\\Bold{F}_{11}}^2 \\\\text{ defined by } x^{2} + 10 y z, x^{5}'\n**********************************************************************\n1 items had failures:\n   2 of   9 in __main__.example_23\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_algebraic_scheme.py\n         [5.4 s]\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py\"\n        sage -t  \"devel/sage-reviewing/sage/rings/qqbar.py\"\n        sage -t  \"devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py\"\nTotal time for all tests: 28.6 seconds\n```\n",
    "created_at": "2010-07-01T07:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82300",
    "user": "@loefflerd"
}
```

I'm getting doctest failures with this under 4.5.alpha1:

```
sage -t  "devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py"
**********************************************************************           
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py", line 379:                                                                                                    
    sage: latex(-I*y+I*x^2)                                                                                   
Expected:                                                                                                     
    \sqrt{-1} x^{2} - \sqrt{-1} y                                                                             
Got:                                                                                                          
    \left(\sqrt{-1}\right) x^{2} + \left(-\sqrt{-1}\right) y                                                  
**********************************************************************                                        
1 items had failures:                                                                                         
   1 of   7 in __main__.example_15                                                                            
***Test Failed*** 1 failures.                                                                                 
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_multi_polynomial_element.py              
         [3.7 s]                                                                                              
sage -t  "devel/sage-reviewing/sage/rings/qqbar.py"                                                           
**********************************************************************                           File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/qqbar.py", line 2223:
    sage: latex(-QQbar.zeta(4) + 5)
Expected:
    -i + 5
Got:
    -\sqrt{-1} + 5
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_42
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_qqbar.py
         [19.5 s]
sage -t  "devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py", line 595:
    sage: S._latex_()
Expected:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} - y z'
Got:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} + 10 y z'
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py", line 602:
    sage: S._latex_()
Expected:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} - y z, x^{5}'
Got:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} + 10 y z, x^{5}'
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_23
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_algebraic_scheme.py
         [5.4 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py"
        sage -t  "devel/sage-reviewing/sage/rings/qqbar.py"
        sage -t  "devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py"
Total time for all tests: 28.6 seconds
```




---

archive/issue_comments_082301.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T07:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82301",
    "user": "@loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082302.json:
```json
{
    "body": "It looks like the new failures are caused by\u00a0#9017\u00a0and\u00a0#9108, both of which overtook this patch. \u00a0I'll try to make a new patch compatible with the changes introduced by the other two.",
    "created_at": "2010-07-02T07:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82302",
    "user": "fwclarke"
}
```

It looks like the new failures are caused by #9017 and #9108, both of which overtook this patch.  I'll try to make a new patch compatible with the changes introduced by the other two.



---

archive/issue_comments_082303.json:
```json
{
    "body": "See also #9394.",
    "created_at": "2010-07-02T20:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82303",
    "user": "fwclarke"
}
```

See also #9394.



---

archive/issue_comments_082304.json:
```json
{
    "body": "See also #9478.",
    "created_at": "2010-11-08T15:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82304",
    "user": "@novoselt"
}
```

See also #9478.



---

archive/issue_comments_082305.json:
```json
{
    "body": "In Sage 4.7.1.rc0 I get for the last line\n\n```\n\\left(z^{2} + z\\right) s\n```\n\nso this bug has been fixed along the way.",
    "created_at": "2011-07-22T16:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82305",
    "user": "@novoselt"
}
```

In Sage 4.7.1.rc0 I get for the last line

```
\left(z^{2} + z\right) s
```

so this bug has been fixed along the way.



---

archive/issue_comments_082306.json:
```json
{
    "body": "Attachment [trac_8938_latex_test_for_cyclotomic_fields.patch](tarball://root/attachments/some-uuid/ticket8938/trac_8938_latex_test_for_cyclotomic_fields.patch) by @novoselt created at 2011-07-22 16:41:33",
    "created_at": "2011-07-22T16:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82306",
    "user": "@novoselt"
}
```

Attachment [trac_8938_latex_test_for_cyclotomic_fields.patch](tarball://root/attachments/some-uuid/ticket8938/trac_8938_latex_test_for_cyclotomic_fields.patch) by @novoselt created at 2011-07-22 16:41:33



---

archive/issue_comments_082307.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-22T16:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82307",
    "user": "@novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082308.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-07-22T20:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82308",
    "user": "@jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_082309.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-07-22T20:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82309",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082310.json:
```json
{
    "body": "Looks good to me.  (There are probably other doctests verifying this from whatever ticket originally fixed it, but having another one can't hurt.)",
    "created_at": "2011-07-22T20:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82310",
    "user": "@jhpalmieri"
}
```

Looks good to me.  (There are probably other doctests verifying this from whatever ticket originally fixed it, but having another one can't hurt.)



---

archive/issue_comments_082311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-08-03T14:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8938#issuecomment-82311",
    "user": "@jdemeyer"
}
```

Resolution: fixed
