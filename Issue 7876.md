# Issue 7876: symbolic expression displayed wrong

archive/issues_007876.json:
```json
{
    "body": "Assignee: @burcin\n\nIt appears that the internal representation is correct since further calculations give correct answers, but the answer is displayed incorrectly.\n\n\n```\nsage: f=(1/2-1/2*I )*sqrt(2)\nsage: f\n-(1/2*I + 1/2)*sqrt(2)\nsage: f+1/2*sqrt(2)\n-(1/2*I + 1)*sqrt(2)\nsage: f-1/2*sqrt(2)\n-1/2*I*sqrt(2)\nsage: latex(f)\n-\\left(\\frac{1}{2} I + \\frac{1}{2}\\right) \\, \\sqrt{2}\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7876\n\n",
    "created_at": "2010-01-09T13:57:28Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "symbolic expression displayed wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7876",
    "user": "https://github.com/gvol"
}
```
Assignee: @burcin

It appears that the internal representation is correct since further calculations give correct answers, but the answer is displayed incorrectly.


```
sage: f=(1/2-1/2*I )*sqrt(2)
sage: f
-(1/2*I + 1/2)*sqrt(2)
sage: f+1/2*sqrt(2)
-(1/2*I + 1)*sqrt(2)
sage: f-1/2*sqrt(2)
-1/2*I*sqrt(2)
sage: latex(f)
-\left(\frac{1}{2} I + \frac{1}{2}\right) \, \sqrt{2}
sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/7876





---

archive/issue_comments_068303.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-17T06:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68303",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068304.json:
```json
{
    "body": "I fixed this in pynac. attachment:trac_7876-pynac_print.patch contains doctest fixes.\n\nI will post a pynac package with the fix in the next few days.\n\nThanks a lot for the report.",
    "created_at": "2010-01-17T06:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68304",
    "user": "https://github.com/burcin"
}
```

I fixed this in pynac. attachment:trac_7876-pynac_print.patch contains doctest fixes.

I will post a pynac package with the fix in the next few days.

Thanks a lot for the report.



---

archive/issue_comments_068305.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-01-17T06:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68305",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_068306.json:
```json
{
    "body": "add doctests",
    "created_at": "2010-01-17T06:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68306",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_comments_068307.json:
```json
{
    "body": "Attachment [trac_7876-pynac_print.patch](tarball://root/attachments/some-uuid/ticket7876/trac_7876-pynac_print.patch) by @burcin created at 2010-01-17 11:14:43\n\nadd one more doctest fix - apply only this patch",
    "created_at": "2010-01-17T11:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68307",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7876-pynac_print.patch](tarball://root/attachments/some-uuid/ticket7876/trac_7876-pynac_print.patch) by @burcin created at 2010-01-17 11:14:43

add one more doctest fix - apply only this patch



---

archive/issue_comments_068308.json:
```json
{
    "body": "Attachment [trac_7876-pynac_print.take2.patch](tarball://root/attachments/some-uuid/ticket7876/trac_7876-pynac_print.take2.patch) by @burcin created at 2010-01-19 14:09:15\n\nNew pynac package available here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n\nThe package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. Apart from this ticket, #7363 contains printing changes. Doctests should be run with the patch from that ticket applied as well.",
    "created_at": "2010-01-19T14:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68308",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7876-pynac_print.take2.patch](tarball://root/attachments/some-uuid/ticket7876/trac_7876-pynac_print.take2.patch) by @burcin created at 2010-01-19 14:09:15

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. Apart from this ticket, #7363 contains printing changes. Doctests should be run with the patch from that ticket applied as well.



---

archive/issue_comments_068309.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-01-19T14:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68309",
    "user": "https://github.com/burcin"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_068310.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T14:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68310",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068311.json:
```json
{
    "body": "I get a single reject from the patch, in symbolic/random_tests.py on sage.math.  Here is what I have in random_tests.py:\n\n\n```\n        sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)\n        sinh(sinh(-coth(v2)/erf(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + csch(-(0.708874026302 - 0.954135400334*I)*v3)))^coth(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))\n\n```\n\n\nwhereas the patch has:\n\n\n```\n         sage: from sage.symbolic.random_tests import *\n         sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)\n-        arctanh(sinh(-coth(v2)/erf(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + erf(-(0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))\n+        arctanh(sinh(-coth(v2)/erf((-0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + erf((-0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^((-0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin((-0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))\n```\n",
    "created_at": "2010-01-21T00:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68311",
    "user": "https://github.com/jasongrout"
}
```

I get a single reject from the patch, in symbolic/random_tests.py on sage.math.  Here is what I have in random_tests.py:


```
        sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
        sinh(sinh(-coth(v2)/erf(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + csch(-(0.708874026302 - 0.954135400334*I)*v3)))^coth(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))

```


whereas the patch has:


```
         sage: from sage.symbolic.random_tests import *
         sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
-        arctanh(sinh(-coth(v2)/erf(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + erf(-(0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))
+        arctanh(sinh(-coth(v2)/erf((-0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + erf((-0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^((-0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin((-0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))
```




---

archive/issue_comments_068312.json:
```json
{
    "body": "See #6559 for the correct order of patches to avoid the reject.",
    "created_at": "2010-01-21T01:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68312",
    "user": "https://github.com/jasongrout"
}
```

See #6559 for the correct order of patches to avoid the reject.



---

archive/issue_comments_068313.json:
```json
{
    "body": "The following now displays correctly using Sage Version 4.3.1 (Release Date: 2010-01-20)\nwith pynac 0.1.11 (and also without any patches mentioned in this ticket)\n\n\n```\nsage: f=(1/2-1/2*I )*sqrt(2)\n\nsage: f\n(-1/2*I + 1/2)*sqrt(2)\n\nsage: f-1/2*sqrt(2)\n-1/2*I*sqrt(2)\n\nsage: f+1/2*sqrt(2)\n(-1/2*I + 1)*sqrt(2)\n\nsage: f-I*1/2*sqrt(2)\n(-I + 1/2)*sqrt(2)\n\nsage: f-I/2*sqrt(2)\n(-I + 1/2)*sqrt(2)\n\nsage: f+I/2*sqrt(2)\n1/2*sqrt(2)\n\nsage: latex(f)\n\\left(-\\frac{1}{2} I + \\frac{1}{2}\\right) \\, \\sqrt{2}\n\nsage: latex(f+I/2*sqrt(2))\n\\frac{1}{2} \\, \\sqrt{2}\n\nsage: (1-I)^2\n-2*I\n\nsage: (1+I)^2\n2*I\n\nsage: (1+I*sqrt(2))^2\n(I*sqrt(2) + 1)^2\n\nsage: expand((1+I*sqrt(2))^2)\n2*I*sqrt(2) - 1\n```\n",
    "created_at": "2010-01-25T08:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68313",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

The following now displays correctly using Sage Version 4.3.1 (Release Date: 2010-01-20)
with pynac 0.1.11 (and also without any patches mentioned in this ticket)


```
sage: f=(1/2-1/2*I )*sqrt(2)

sage: f
(-1/2*I + 1/2)*sqrt(2)

sage: f-1/2*sqrt(2)
-1/2*I*sqrt(2)

sage: f+1/2*sqrt(2)
(-1/2*I + 1)*sqrt(2)

sage: f-I*1/2*sqrt(2)
(-I + 1/2)*sqrt(2)

sage: f-I/2*sqrt(2)
(-I + 1/2)*sqrt(2)

sage: f+I/2*sqrt(2)
1/2*sqrt(2)

sage: latex(f)
\left(-\frac{1}{2} I + \frac{1}{2}\right) \, \sqrt{2}

sage: latex(f+I/2*sqrt(2))
\frac{1}{2} \, \sqrt{2}

sage: (1-I)^2
-2*I

sage: (1+I)^2
2*I

sage: (1+I*sqrt(2))^2
(I*sqrt(2) + 1)^2

sage: expand((1+I*sqrt(2))^2)
2*I*sqrt(2) - 1
```




---

archive/issue_comments_068314.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-25T08:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68314",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_068316.json:
```json
{
    "body": "Merged [trac_7876-pynac_print.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7876/trac_7876-pynac_print.take2.patch).",
    "created_at": "2010-02-18T21:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7876#issuecomment-68316",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_7876-pynac_print.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7876/trac_7876-pynac_print.take2.patch).



---

archive/issue_events_008091.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-18T21:40:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7876",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7876#event-8091"
}
```
