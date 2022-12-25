# Issue 6559: Real domain for symbolic variables

archive/issues_006559.json:
```json
{
    "body": "In new symbolics, the default symbolic variables are complex.\nHowever, sometime it is useful/desirable to make the domain of\nvariables to be real.\n\n\nCurrently, there are no way to specify the domain of variables\nin Sage although underlying Ginac allows it.  For example: following\nwould to be good to have.\n\n```\nsage: var('x,y,z', domain='real')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6559\n\n",
    "created_at": "2009-07-19T11:10:52Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Real domain for symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6559",
    "user": "https://github.com/golam-m-hossain"
}
```
In new symbolics, the default symbolic variables are complex.
However, sometime it is useful/desirable to make the domain of
variables to be real.


Currently, there are no way to specify the domain of variables
in Sage although underlying Ginac allows it.  For example: following
would to be good to have.

```
sage: var('x,y,z', domain='real')
```


Issue created by migration from https://trac.sagemath.org/ticket/6559





---

archive/issue_comments_053378.json:
```json
{
    "body": "#6802 is a duplicate of this ticket.",
    "created_at": "2009-08-22T14:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53378",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

#6802 is a duplicate of this ticket.



---

archive/issue_comments_053379.json:
```json
{
    "body": "Attachment [trac_6559-domain-and-latex_name-for-variable.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-domain-and-latex_name-for-variable.patch) by @golam-m-hossain created at 2009-09-05 21:29:20",
    "created_at": "2009-09-05T21:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53379",
    "user": "https://github.com/golam-m-hossain"
}
```

Attachment [trac_6559-domain-and-latex_name-for-variable.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-domain-and-latex_name-for-variable.patch) by @golam-m-hossain created at 2009-09-05 21:29:20



---

archive/issue_comments_053380.json:
```json
{
    "body": "How does this relate to pynac 0.1.9 which is in Sage 4.2.1? ~ Adam",
    "created_at": "2009-11-19T17:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53380",
    "user": "https://github.com/maxthemouse"
}
```

How does this relate to pynac 0.1.9 which is in Sage 4.2.1? ~ Adam



---

archive/issue_comments_053381.json:
```json
{
    "body": "Applied patch and the following errors were returned:\n\n\n```\napplying trac_6559-domain-and-latex_name-for-variable.patch\npatching file sage/calculus/var.pyx\nHunk #1 FAILED at 0\nHunk #2 FAILED at 8\nHunk #4 FAILED at 81\n3 out of 4 hunks FAILED -- saving rejects to file sage/calculus/var.pyx.rej\npatching file sage/symbolic/pynac.pyx\nHunk #1 FAILED at 454\nHunk #2 FAILED at 504\n2 out of 2 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej\npatching file sage/symbolic/ring.pyx\nHunk #6 succeeded at 769 with fuzz 1 (offset -2 lines).\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_6559-domain-and-latex_name-for-variable.patch\n```\n",
    "created_at": "2010-01-14T03:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53381",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Applied patch and the following errors were returned:


```
applying trac_6559-domain-and-latex_name-for-variable.patch
patching file sage/calculus/var.pyx
Hunk #1 FAILED at 0
Hunk #2 FAILED at 8
Hunk #4 FAILED at 81
3 out of 4 hunks FAILED -- saving rejects to file sage/calculus/var.pyx.rej
patching file sage/symbolic/pynac.pyx
Hunk #1 FAILED at 454
Hunk #2 FAILED at 504
2 out of 2 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej
patching file sage/symbolic/ring.pyx
Hunk #6 succeeded at 769 with fuzz 1 (offset -2 lines).
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6559-domain-and-latex_name-for-variable.patch
```




---

archive/issue_comments_053382.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-14T03:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53382",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053383.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T02:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53383",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053384.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-18T02:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053385.json:
```json
{
    "body": "Attachment [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch) by @burcin created at 2010-01-19 13:56:13\n\nrebased to 4.3.1.rc0",
    "created_at": "2010-01-19T13:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53385",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch) by @burcin created at 2010-01-19 13:56:13

rebased to 4.3.1.rc0



---

archive/issue_comments_053386.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-01-19T14:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53386",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_053387.json:
```json
{
    "body": "Attachment [trac_6559-referee.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-referee.patch) by @burcin created at 2010-01-19 14:38:15\n\nI uploaded a revised version of Golam's patch at attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch, and a referee patch at attachment:trac_6559-referee.patch.\n\nThe changes in the revised patch over Golam's version are\n* rebased to 4.3.rc0\n* removed `sage.symbolic.ring.SR.new_var()` and `sage.symbolic.ring.is_ComplexVariable()` functions. The first is same as `SR.symbol()` and I don't see a use for the second, since all variables are complex. :)\n* removed pickling changes in sage.symbolic.expression.Expression, since unpickling in this case could create a new variable with the same name as an existing one, but with a different domain. This would lead to rather confusing situations.\n\nThe referee patch reorganizes the new code a little to make it more efficient. Apparently the new variable creation is an important operation and being sloppy here greatly increases doctest timings. It also adds new methods like `_is_positive()`, `_is_real()` to the expression class to allow querying for more properties.\n\nOnly the patches \n* attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch and\n* attachment:trac_6559-referee.patch \nshould be applied.\n\nThis ticket depends on the new pynac package here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n\nwhich in turns depends on the patches at #7822, #7876, #7363, #7955, #7957, #7916 and #6465 (in that order).\n\nThe changes here seem to slow down the maxima interface dramatically, so I'm leaving this as needs work for now.",
    "created_at": "2010-01-19T14:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53387",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6559-referee.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-referee.patch) by @burcin created at 2010-01-19 14:38:15

I uploaded a revised version of Golam's patch at attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch, and a referee patch at attachment:trac_6559-referee.patch.

The changes in the revised patch over Golam's version are
* rebased to 4.3.rc0
* removed `sage.symbolic.ring.SR.new_var()` and `sage.symbolic.ring.is_ComplexVariable()` functions. The first is same as `SR.symbol()` and I don't see a use for the second, since all variables are complex. :)
* removed pickling changes in sage.symbolic.expression.Expression, since unpickling in this case could create a new variable with the same name as an existing one, but with a different domain. This would lead to rather confusing situations.

The referee patch reorganizes the new code a little to make it more efficient. Apparently the new variable creation is an important operation and being sloppy here greatly increases doctest timings. It also adds new methods like `_is_positive()`, `_is_real()` to the expression class to allow querying for more properties.

Only the patches 
* attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch and
* attachment:trac_6559-referee.patch 
should be applied.

This ticket depends on the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

which in turns depends on the patches at #7822, #7876, #7363, #7955, #7957, #7916 and #6465 (in that order).

The changes here seem to slow down the maxima interface dramatically, so I'm leaving this as needs work for now.



---

archive/issue_comments_053388.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T04:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53388",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053389.json:
```json
{
    "body": "Attachment [trac_6559-referee.take2.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-referee.take2.patch) by @burcin created at 2010-01-20 04:11:21\n\nNew patches up, ready for review.\n\nApply only:\n* attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch\n* attachment:trac_6559-referee.take2.patch\n\nDepends on the pynac package here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n\nand the tickets #7822, #7876, #7363, #7955, #7957, #7916 and #6465 (in that order).",
    "created_at": "2010-01-20T04:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53389",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6559-referee.take2.patch](tarball://root/attachments/some-uuid/ticket6559/trac_6559-referee.take2.patch) by @burcin created at 2010-01-20 04:11:21

New patches up, ready for review.

Apply only:
* attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch
* attachment:trac_6559-referee.take2.patch

Depends on the pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

and the tickets #7822, #7876, #7363, #7955, #7957, #7916 and #6465 (in that order).



---

archive/issue_comments_053390.json:
```json
{
    "body": "I applied the patches in this order:\n\n\n```\n$ hg qseries\ntrac_7999-encoding.patch\ntrac_6961-psi.patch\ntrac_7822-py_log.take2.patch\ntrac_7876-pynac_print.take2.patch\ntrac_7363-mul_coeff.patch\ntrac_7955-integrate_latex.patch\ntrac_7957-pynac_exceptions.patch\ntrac_7916-same_name_method.take2.patch\ntrac_6465-chain_rule.take2.patch\ntrac_6465-moves-integration-into-sfunction-subclass.take2.patch\ntrac_6465-integral.patch\ntrac_6559-domain-and-latex_name-for-variable.take2.3.patch\ntrac_6559-referee.take2.patch\n```\n\n\nThere's only one failure (sage -tp, not long) in arith.py, which is a documentation thing and unrelated to this ticket.",
    "created_at": "2010-01-21T01:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53390",
    "user": "https://github.com/jasongrout"
}
```

I applied the patches in this order:


```
$ hg qseries
trac_7999-encoding.patch
trac_6961-psi.patch
trac_7822-py_log.take2.patch
trac_7876-pynac_print.take2.patch
trac_7363-mul_coeff.patch
trac_7955-integrate_latex.patch
trac_7957-pynac_exceptions.patch
trac_7916-same_name_method.take2.patch
trac_6465-chain_rule.take2.patch
trac_6465-moves-integration-into-sfunction-subclass.take2.patch
trac_6465-integral.patch
trac_6559-domain-and-latex_name-for-variable.take2.3.patch
trac_6559-referee.take2.patch
```


There's only one failure (sage -tp, not long) in arith.py, which is a documentation thing and unrelated to this ticket.



---

archive/issue_comments_053391.json:
```json
{
    "body": "Is it likely that the rebase referred to in #6961 might affect other patches than just that one?  Read that before refereeing, in any case.",
    "created_at": "2010-01-27T19:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53391",
    "user": "https://github.com/kcrisman"
}
```

Is it likely that the rebase referred to in #6961 might affect other patches than just that one?  Read that before refereeing, in any case.



---

archive/issue_comments_053392.json:
```json
{
    "body": "I can't even begin to say where these are from... but \n\n```\nsage/misc/citation.pyx\", line 60:\n    sage: get_systems('integrate(x^2, x)')\nExpected:\n    ['ginac', 'Maxima']\nGot:\n    ['MPFI', 'ginac', 'Maxima']\n```\n\n\n```\nsage/symbolic/random_tests.py\", line 206:\n    sage: random_expr(5, verbose=True)\nExpected:\n    About to apply <built-in function add> to [v1, v1]\n    About to apply <built-in function div> to [-1/3, 2*v1]\n    -1/6/v1\nGot:\n    About to apply <built-in function add> to [v1, v1]\n    About to apply <built-in function div> to [94, 2*v1]\n    47/v1\n```\n\nseem to be related to just random changes in 4.3.1, while \n\n```\nsage/functions/generalized.py\", line 239:\n    sage: t.subs(x=1)\nExpected:\n    2\nGot:\n    heaviside(x) + 1\n```\n\nand a few friends seem to be related to something in pickling changing (I get no other errors with things like that).\n\nIn addition, I am getting quite a few segfaults when testing against 4.3.1. \n\n```\n Desktop/sage-4.3.1/sage -t devel/sage/sage/calculus/calculus.py devel/sage/sage/functions/piecewise.py devel/sage/sage/plot/plot.py devel/sage/sage/symbolic/expression.pyx devel/sage/sage/misc/functional.py devel/sage/sage/symbolic/relation.py devel/sage/sage/symbolic/assumptions.py devel/sage/sage/calculus/wester.py devel/sage/sage/calculus/functional.py \n```\n \nall do. Probably I should not have applied all patches at once, but I was impatient :)",
    "created_at": "2010-01-27T20:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53392",
    "user": "https://github.com/kcrisman"
}
```

I can't even begin to say where these are from... but 

```
sage/misc/citation.pyx", line 60:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['ginac', 'Maxima']
Got:
    ['MPFI', 'ginac', 'Maxima']
```


```
sage/symbolic/random_tests.py", line 206:
    sage: random_expr(5, verbose=True)
Expected:
    About to apply <built-in function add> to [v1, v1]
    About to apply <built-in function div> to [-1/3, 2*v1]
    -1/6/v1
Got:
    About to apply <built-in function add> to [v1, v1]
    About to apply <built-in function div> to [94, 2*v1]
    47/v1
```

seem to be related to just random changes in 4.3.1, while 

```
sage/functions/generalized.py", line 239:
    sage: t.subs(x=1)
Expected:
    2
Got:
    heaviside(x) + 1
```

and a few friends seem to be related to something in pickling changing (I get no other errors with things like that).

In addition, I am getting quite a few segfaults when testing against 4.3.1. 

```
 Desktop/sage-4.3.1/sage -t devel/sage/sage/calculus/calculus.py devel/sage/sage/functions/piecewise.py devel/sage/sage/plot/plot.py devel/sage/sage/symbolic/expression.pyx devel/sage/sage/misc/functional.py devel/sage/sage/symbolic/relation.py devel/sage/sage/symbolic/assumptions.py devel/sage/sage/calculus/wester.py devel/sage/sage/calculus/functional.py 
```
 
all do. Probably I should not have applied all patches at once, but I was impatient :)



---

archive/issue_comments_053393.json:
```json
{
    "body": "Update: None of the previous errors happen in this symbolics queue until I hit this ticket, so they are definitely due to this one.\n\nMore comments:  \n\n1. The original patch only causes the sage/functions/generalized.py doctest errors, not the other two.  It did not appear with all patches up through ticket #6465.\n\n2. The original patch does NOT cause massive slowdown or segfaults in doctesting sage/calculus/calculus.py.\n\nSo perhaps the referee patch has changed something weird?",
    "created_at": "2010-01-28T21:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53393",
    "user": "https://github.com/kcrisman"
}
```

Update: None of the previous errors happen in this symbolics queue until I hit this ticket, so they are definitely due to this one.

More comments:  

1. The original patch only causes the sage/functions/generalized.py doctest errors, not the other two.  It did not appear with all patches up through ticket #6465.

2. The original patch does NOT cause massive slowdown or segfaults in doctesting sage/calculus/calculus.py.

So perhaps the referee patch has changed something weird?



---

archive/issue_comments_053394.json:
```json
{
    "body": "Followup:\n\nAdding the referee patch causes a number of segfaults in things relating to assumptions.  For example, the calculus/calculus.py doctest where it is assumed that abs(q)<1, and the one in calculus/wester.py where it is assumed that x>=y, y>=z, z>=x.    It is not consistent whether the assumption itself or the thing using the assumption causes the hang.  Is it possible that the _is_* methods or the info flags in ginac/decl.pxi are responsible?  This is a question out of ignorance; I don't see how they would interfere with Maxima or the use of it by (e.g.) symbolic_sum, but it's all I can think of.\n\nAlso, the citation.pyx and random_tests.py are repeatable.",
    "created_at": "2010-01-29T03:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53394",
    "user": "https://github.com/kcrisman"
}
```

Followup:

Adding the referee patch causes a number of segfaults in things relating to assumptions.  For example, the calculus/calculus.py doctest where it is assumed that abs(q)<1, and the one in calculus/wester.py where it is assumed that x>=y, y>=z, z>=x.    It is not consistent whether the assumption itself or the thing using the assumption causes the hang.  Is it possible that the _is_* methods or the info flags in ginac/decl.pxi are responsible?  This is a question out of ignorance; I don't see how they would interfere with Maxima or the use of it by (e.g.) symbolic_sum, but it's all I can think of.

Also, the citation.pyx and random_tests.py are repeatable.



---

archive/issue_comments_053395.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-29T03:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53395",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053396.json:
```json
{
    "body": "I can't reproduce these problems on my 64-bit laptop with Sage 4.3.2.alpha0, gcc 4.3.4. I'll try on a 32-bit machine tomorrow.\n\nNote that the rebased patch on #6961 applies without problems to a clean 4.3.2.alpha0 here. Though my patch queue contains `trac_7822-py_log.take2.patch` before `trac_6961-psi.rebased.patch`. I tested the rest of the queue when I rebased the patch for #6961, there weren't any problems.\n\nIs it possible that the problems you report might be caused by the fact that your tree got messed up by the git style patches attached to #6465?",
    "created_at": "2010-01-31T21:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53396",
    "user": "https://github.com/burcin"
}
```

I can't reproduce these problems on my 64-bit laptop with Sage 4.3.2.alpha0, gcc 4.3.4. I'll try on a 32-bit machine tomorrow.

Note that the rebased patch on #6961 applies without problems to a clean 4.3.2.alpha0 here. Though my patch queue contains `trac_7822-py_log.take2.patch` before `trac_6961-psi.rebased.patch`. I tested the rest of the queue when I rebased the patch for #6961, there weren't any problems.

Is it possible that the problems you report might be caused by the fact that your tree got messed up by the git style patches attached to #6465?



---

archive/issue_comments_053397.json:
```json
{
    "body": "I cannot reproduce these problems on a 32-bit Debian Lenny box after applying all the symbolics patches and updating pynac to version 0.11.",
    "created_at": "2010-02-03T11:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53397",
    "user": "https://github.com/burcin"
}
```

I cannot reproduce these problems on a 32-bit Debian Lenny box after applying all the symbolics patches and updating pynac to version 0.11.



---

archive/issue_comments_053398.json:
```json
{
    "body": "> Is it possible that the problems you report might be caused by the fact that your tree got messed up by the git style patches attached to #6465?\n\nPossibly, but wouldn't that have made everything not work, as opposed to just a few weird segfaults related to assumptions and a couple other things? \n\nAlso, when I say I applied them all at once, what I mean is I applied them one after the other using hg_sage.import_patch, which I believe is equivalent to hg import.",
    "created_at": "2010-02-04T03:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53398",
    "user": "https://github.com/kcrisman"
}
```

> Is it possible that the problems you report might be caused by the fact that your tree got messed up by the git style patches attached to #6465?

Possibly, but wouldn't that have made everything not work, as opposed to just a few weird segfaults related to assumptions and a couple other things? 

Also, when I say I applied them all at once, what I mean is I applied them one after the other using hg_sage.import_patch, which I believe is equivalent to hg import.



---

archive/issue_comments_053399.json:
```json
{
    "body": "I tried once more with the patches downloaded from trac. I cannot reproduce any problems.\n\nHere is an easier way to test all the patches:\n\n* Make a fresh clone, called \"pynac\"\n* go to the source tree for the clone\n\n\n```\ncd $SAGE_ROOT/devel/sage-pynac\n```\n\n* download this tar file\n\n\n```\nwget http://boxen.math.washington.edu/home/burcin/pynac/pynac_patches.tar.bz2\n```\n\n* extract it to the queue repository\n\n\n```\ncd .hg\ntar jxvf ../pynac_patches.tar.bz2\ncd ..\n```\n\n* apply all the patches\n\n\n```\nhg qpush -a\n```\n\n\n* if the new pynac package is not already installed download and install it\n\n\n```\nhttp://boxen.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n```\n\n\n* rebuild Sage\n\n\n```\n./sage -br\n```\n\n\n* run tests\n\n\n```\n./sage -tp 3 devel/sage-pynac/sage/{symbolic,calculus,functions}\n```\n",
    "created_at": "2010-02-04T09:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53399",
    "user": "https://github.com/burcin"
}
```

I tried once more with the patches downloaded from trac. I cannot reproduce any problems.

Here is an easier way to test all the patches:

* Make a fresh clone, called "pynac"
* go to the source tree for the clone


```
cd $SAGE_ROOT/devel/sage-pynac
```

* download this tar file


```
wget http://boxen.math.washington.edu/home/burcin/pynac/pynac_patches.tar.bz2
```

* extract it to the queue repository


```
cd .hg
tar jxvf ../pynac_patches.tar.bz2
cd ..
```

* apply all the patches


```
hg qpush -a
```


* if the new pynac package is not already installed download and install it


```
http://boxen.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg
```


* rebuild Sage


```
./sage -br
```


* run tests


```
./sage -tp 3 devel/sage-pynac/sage/{symbolic,calculus,functions}
```




---

archive/issue_comments_053400.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T09:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53400",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053401.json:
```json
{
    "body": "\n```\napplying trac_7822-py_log.take2.patch\napplying trac_6961-psi.rebased.patch\napplying trac_7876-pynac_print.take2.patch\napplying trac_7363-mul_coeff.patch\napplying trac_7955-integrate_latex.patch\napplying trac_7957-pynac_exceptions.patch\napplying trac_7916-same_name_method.take2.patch\napplying trac_6465-chain_rule.take2.patch\napplying trac_6465-moves-integration-into-sfunction-subclass.take2.patch\npatching file sage/misc/functional.py\nHunk #1 FAILED at 662\n1 out of 2 hunks FAILED -- saving rejects to file sage/misc/functional.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_6465-moves-integration-into-sfunction-subclass.take2.patch\n```\n",
    "created_at": "2010-02-13T05:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53401",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```


```
applying trac_7822-py_log.take2.patch
applying trac_6961-psi.rebased.patch
applying trac_7876-pynac_print.take2.patch
applying trac_7363-mul_coeff.patch
applying trac_7955-integrate_latex.patch
applying trac_7957-pynac_exceptions.patch
applying trac_7916-same_name_method.take2.patch
applying trac_6465-chain_rule.take2.patch
applying trac_6465-moves-integration-into-sfunction-subclass.take2.patch
patching file sage/misc/functional.py
Hunk #1 FAILED at 662
1 out of 2 hunks FAILED -- saving rejects to file sage/misc/functional.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6465-moves-integration-into-sfunction-subclass.take2.patch
```




---

archive/issue_comments_053402.json:
```json
{
    "body": "See comment:19:ticket:6465. Two patches on that ticket needed to be rebased to 4.3.2. Unfortunately, I didn't have time to update the patch tarball.\n\nYou can use `hg qdelete <patch_name>` to remove the offending patches from the queue, and `hg qimport` new ones. The specific list of command to be executed is:\n\n\n```\ncd $SAGE_ROOT/devel/sage-pynac\nhg qpop -a\nhg qdelete trac_6465-moves-integration-into-sfunction-subclass.take2.patch\nhg qdelete trac_6465-integral.take3.patch\nhg qgoto trac_6465-chain_rule.take2.patch\nhg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6465/trac_6465-integral.take4.patch\nhg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch\nhg qpush -a\n```\n\n\nThen rebuild sage, and proceed with the tests...\n\nMany thanks for looking at this.",
    "created_at": "2010-02-13T10:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53402",
    "user": "https://github.com/burcin"
}
```

See comment:19:ticket:6465. Two patches on that ticket needed to be rebased to 4.3.2. Unfortunately, I didn't have time to update the patch tarball.

You can use `hg qdelete <patch_name>` to remove the offending patches from the queue, and `hg qimport` new ones. The specific list of command to be executed is:


```
cd $SAGE_ROOT/devel/sage-pynac
hg qpop -a
hg qdelete trac_6465-moves-integration-into-sfunction-subclass.take2.patch
hg qdelete trac_6465-integral.take3.patch
hg qgoto trac_6465-chain_rule.take2.patch
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6465/trac_6465-integral.take4.patch
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch
hg qpush -a
```


Then rebuild sage, and proceed with the tests...

Many thanks for looking at this.



---

archive/issue_comments_053403.json:
```json
{
    "body": "The hg qgoto didnt work. (And if its easier at any stage to blow away the pynac clone and start again, feel free to suggest that). \n\n```\nrossk@sage:/scratch/rossk/sage-4.3.3.alpha0-sage.math.washington.edu-x86_64-Linux/devel/sage-pynac$ hg qgoto trac_6465-chain_rule.take2.patch\napplying trac_7822-py_log.take2.patch\napplying trac_6961-psi.rebased.patch\napplying trac_7876-pynac_print.take2.patch\napplying trac_7363-mul_coeff.patch\napplying trac_7955-integrate_latex.patch\npatching file sage/calculus/calculus.py\nHunk #1 FAILED at 1710\nHunk #2 FAILED at 1719\nHunk #3 FAILED at 1742\nHunk #4 FAILED at 1771\nHunk #5 FAILED at 1781\nHunk #6 FAILED at 1790\n6 out of 6 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_7955-integrate_latex.patch\n```\n",
    "created_at": "2010-02-13T12:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53403",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

The hg qgoto didnt work. (And if its easier at any stage to blow away the pynac clone and start again, feel free to suggest that). 

```
rossk@sage:/scratch/rossk/sage-4.3.3.alpha0-sage.math.washington.edu-x86_64-Linux/devel/sage-pynac$ hg qgoto trac_6465-chain_rule.take2.patch
applying trac_7822-py_log.take2.patch
applying trac_6961-psi.rebased.patch
applying trac_7876-pynac_print.take2.patch
applying trac_7363-mul_coeff.patch
applying trac_7955-integrate_latex.patch
patching file sage/calculus/calculus.py
Hunk #1 FAILED at 1710
Hunk #2 FAILED at 1719
Hunk #3 FAILED at 1742
Hunk #4 FAILED at 1771
Hunk #5 FAILED at 1781
Hunk #6 FAILED at 1790
6 out of 6 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7955-integrate_latex.patch
```




---

archive/issue_comments_053404.json:
```json
{
    "body": "Hi Ross,\n\nThe last output you posted doesn't make sense to me. Did you update to 4.3.3.alpha0 since comment:18? In comment:18, the output shows that `trac_7955-integrate_latex.patch` applies cleanly. I don't see any other reason why it would fail now.\n\nI don't have a working copy of 4.3.3.alpha0 yet. Unfortunately, it will take me a couple of days update to that.",
    "created_at": "2010-02-13T13:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53404",
    "user": "https://github.com/burcin"
}
```

Hi Ross,

The last output you posted doesn't make sense to me. Did you update to 4.3.3.alpha0 since comment:18? In comment:18, the output shows that `trac_7955-integrate_latex.patch` applies cleanly. I don't see any other reason why it would fail now.

I don't have a working copy of 4.3.3.alpha0 yet. Unfortunately, it will take me a couple of days update to that.



---

archive/issue_comments_053405.json:
```json
{
    "body": "Youre right - made a minor mistake so I had to start again and I could only find a version of 4.3.3.alpha0 easily and I used that (apologies). To get some testing done sooner than later Ill go back to 4.3.3 for now. Thanks.",
    "created_at": "2010-02-13T13:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53405",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Youre right - made a minor mistake so I had to start again and I could only find a version of 4.3.3.alpha0 easily and I used that (apologies). To get some testing done sooner than later Ill go back to 4.3.3 for now. Thanks.



---

archive/issue_comments_053406.json:
```json
{
    "body": ":) Ticket #7955 was merged in 4.3.3.alpha0, so it's natural that the patch fails. If you just do\n\n\n```\nhg qdelete trac_7955-integrate_latex.patch\n```\n\n\nthe rest of the patches should apply without problems.\n\nThanks again for your time.",
    "created_at": "2010-02-15T00:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53406",
    "user": "https://github.com/burcin"
}
```

:) Ticket #7955 was merged in 4.3.3.alpha0, so it's natural that the patch fails. If you just do


```
hg qdelete trac_7955-integrate_latex.patch
```


the rest of the patches should apply without problems.

Thanks again for your time.



---

archive/issue_comments_053407.json:
```json
{
    "body": "Looks good to me. See #6961 for the order in which to merge patches.",
    "created_at": "2010-02-18T21:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good to me. See #6961 for the order in which to merge patches.



---

archive/issue_comments_053408.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-18T21:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053409.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006796.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-18T21:53:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6559#event-6796"
}
```



---

archive/issue_comments_053410.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch)\n2. [trac_6559-referee.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-referee.take2.patch)",
    "created_at": "2010-02-18T21:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6559#issuecomment-53410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch)
2. [trac_6559-referee.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-referee.take2.patch)
