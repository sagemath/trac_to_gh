# Issue 783: dilog is lame

archive/issues_000783.json:
```json
{
    "body": "Assignee: somebody\n\ndilog on almost all input gives NotImplementedError:\n\n\n```\nsage: dilog(-1)\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/home/was/Desktop/<ipython console> in <module>()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/functions/special.py in dilog(t)\n    743         return t.dilog()\n    744     except AttributeError:\n--> 745         raise NotImplementedError\n    746\n    747 def lngamma(t):\n\n<type 'exceptions.NotImplementedError'>:\nsage:                                     \n```\n\n\nShould add dilog to RDF, RR, CDF, CC elements, when it makes sense.\n\nThis does work:\n\n```\nsage: dilog(pari(2))\n2.4674011002723396547086227499690377838 - 2.1775860903036021305006888982376139473*I\n```\n\n\nSee also this from pari-dev (which I don't agree with):\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/783\n\n",
    "created_at": "2007-10-02T13:26:29Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "dilog is lame",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/783",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

dilog on almost all input gives NotImplementedError:


```
sage: dilog(-1)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/was/Desktop/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/functions/special.py in dilog(t)
    743         return t.dilog()
    744     except AttributeError:
--> 745         raise NotImplementedError
    746
    747 def lngamma(t):

<type 'exceptions.NotImplementedError'>:
sage:                                     
```


Should add dilog to RDF, RR, CDF, CC elements, when it makes sense.

This does work:

```
sage: dilog(pari(2))
2.4674011002723396547086227499690377838 - 2.1775860903036021305006888982376139473*I
```


See also this from pari-dev (which I don't agree with):


Issue created by migration from https://trac.sagemath.org/ticket/783





---

archive/issue_comments_004666.json:
```json
{
    "body": "\n```\nVincent Lefevre <vincent@vinc17.org> \t\nto pari-dev\n\t\nshow details\n\t 1:08 am (5 hours ago) \nHi,\n\nWith Pari 2.3.2:\n\n? dilog(-1)\n%1 = -0.8224670334241132182362075834 + 9.136285398175292265776793780 E-29*I\n\nbut the value should be a real number. I suppose that the imaginary\nterm is due to a rounding error, in which case it should be zeroed\nif one knows that the mathematical result is a real number.\n\nNote that due to this problem, the plot function fails with:\n *** plot: impossible assignment t_COMPLEX --> t_REAL.\n```\n",
    "created_at": "2007-10-02T13:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4666",
    "user": "https://github.com/williamstein"
}
```


```
Vincent Lefevre <vincent@vinc17.org> 	
to pari-dev
	
show details
	 1:08 am (5 hours ago) 
Hi,

With Pari 2.3.2:

? dilog(-1)
%1 = -0.8224670334241132182362075834 + 9.136285398175292265776793780 E-29*I

but the value should be a real number. I suppose that the imaginary
term is due to a rounding error, in which case it should be zeroed
if one knows that the mathematical result is a real number.

Note that due to this problem, the plot function fails with:
 *** plot: impossible assignment t_COMPLEX --> t_REAL.
```




---

archive/issue_comments_004667.json:
```json
{
    "body": "Attachment [783-dilog_lame.patch](tarball://root/attachments/some-uuid/ticket783/783-dilog_lame.patch) by @aghitza created at 2008-04-19 14:41:38\n\nBut polylog is implemented to a more serious extent, in calculus.py.  I think we should just have dilog(z) be an alias for polylog(2, z).\n\nI've put up a patch making this change.",
    "created_at": "2008-04-19T14:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4667",
    "user": "https://github.com/aghitza"
}
```

Attachment [783-dilog_lame.patch](tarball://root/attachments/some-uuid/ticket783/783-dilog_lame.patch) by @aghitza created at 2008-04-19 14:41:38

But polylog is implemented to a more serious extent, in calculus.py.  I think we should just have dilog(z) be an alias for polylog(2, z).

I've put up a patch making this change.



---

archive/issue_comments_004668.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-26T01:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4668",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_004669.json:
```json
{
    "body": "The hunk\n\n```\ndiff -r 631bb7b11fe9 -r 2829ba5e615e sage/functions/all.py\n--- a/sage/functions/all.py     Tue Apr 15 04:19:13 2008 -0700\n+++ b/sage/functions/all.py     Sat Apr 19 10:33:01 2008 -0400\n@@ -16,7 +16,7 @@ from special    import (bessel_I, bessel\n                         spherical_bessel_J, spherical_bessel_Y,\n                         spherical_hankel1, spherical_hankel2,\n                         spherical_harmonic, jacobi,\n-                        inverse_jacobi, dilog,\n+                        inverse_jacobi,\n                         lngamma, exp_int, error_fcn)\n\n from orthogonal_polys import (chebyshev_T,\n```\n\nconflicts with one of the other patches in 3.0.1.alpha0, so I am merging that one manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T02:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The hunk

```
diff -r 631bb7b11fe9 -r 2829ba5e615e sage/functions/all.py
--- a/sage/functions/all.py     Tue Apr 15 04:19:13 2008 -0700
+++ b/sage/functions/all.py     Sat Apr 19 10:33:01 2008 -0400
@@ -16,7 +16,7 @@ from special    import (bessel_I, bessel
                         spherical_bessel_J, spherical_bessel_Y,
                         spherical_hankel1, spherical_hankel2,
                         spherical_harmonic, jacobi,
-                        inverse_jacobi, dilog,
+                        inverse_jacobi,
                         lngamma, exp_int, error_fcn)

 from orthogonal_polys import (chebyshev_T,
```

conflicts with one of the other patches in 3.0.1.alpha0, so I am merging that one manually.

Cheers,

Michael



---

archive/issue_comments_004670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T03:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004671.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T03:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha0



---

archive/issue_events_000888.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-26T03:35:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/783#event-888"
}
```



---

archive/issue_comments_004672.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-02-07T10:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4672",
    "user": "https://github.com/zimmermann6"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_004673.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-02-07T10:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4673",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from closed to new.



---

archive/issue_events_000889.json:
```json
{
    "actor": "https://github.com/zimmermann6",
    "created_at": "2010-02-07T10:44:24Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/783#event-889"
}
```



---

archive/issue_comments_004674.json:
```json
{
    "body": "I'd like to reopen this ticket, since the fix only corrected integer input (here with Sage 4.3.1):\n\n```\nsage: dilog(-1.1)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2251, 0))\n\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last\n```\n\nPari knows how to compute this:\n\n```\nsage: gp.dilog(-1.1)\n-0.89083809026228267332015894927022713036\n```\n",
    "created_at": "2010-02-07T10:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4674",
    "user": "https://github.com/zimmermann6"
}
```

I'd like to reopen this ticket, since the fix only corrected integer input (here with Sage 4.3.1):

```
sage: dilog(-1.1)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2251, 0))

---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last
```

Pari knows how to compute this:

```
sage: gp.dilog(-1.1)
-0.89083809026228267332015894927022713036
```




---

archive/issue_comments_004675.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T21:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4675",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_004676.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-08-30T12:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4676",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_004677.json:
```json
{
    "body": "There is something strange in the examples added:\n\n```\nsage: from sage.symbolic.pynac import py_li2_for_doctests as py_li2 \nsage: py_li2(-1.1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/users/caramel/zimmerma/Adm/Stages/10/Prest/<ipython console> in <module>()\n\n/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_li2_for_doctests (sage/symbolic/pynac.cpp:15450)()\n\nTypeError: py_li2_for_doctests() takes exactly 2 positional arguments (1 given)\n```\n\nShouldn't `py_li2` take two arguments?\n\nAlso I've noticed the following, which maybe should be in a different ticket:\n\n```\nsage: dilog(+Infinity)\ndilog(+Infinity)\nsage: dilog(-Infinity)\ndilog(-Infinity)\nsage: limit(dilog(x),x=+Infinity)\nInfinity\nsage: limit(dilog(x),x=-Infinity)\n-Infinity\n```\n\nMaybe `dilog(+Infinity)` and `dilog(-Infinity)` should return the corresponding limits?",
    "created_at": "2010-08-30T12:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4677",
    "user": "https://github.com/zimmermann6"
}
```

There is something strange in the examples added:

```
sage: from sage.symbolic.pynac import py_li2_for_doctests as py_li2 
sage: py_li2(-1.1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/Adm/Stages/10/Prest/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_li2_for_doctests (sage/symbolic/pynac.cpp:15450)()

TypeError: py_li2_for_doctests() takes exactly 2 positional arguments (1 given)
```

Shouldn't `py_li2` take two arguments?

Also I've noticed the following, which maybe should be in a different ticket:

```
sage: dilog(+Infinity)
dilog(+Infinity)
sage: dilog(-Infinity)
dilog(-Infinity)
sage: limit(dilog(x),x=+Infinity)
Infinity
sage: limit(dilog(x),x=-Infinity)
-Infinity
```

Maybe `dilog(+Infinity)` and `dilog(-Infinity)` should return the corresponding limits?



---

archive/issue_comments_004678.json:
```json
{
    "body": "The patch had some typos so I uploaded a correct version.  The +Infinity/-Infinity thing should probably be a new ticket as it's something that should be done in a manner consistent for all functions.",
    "created_at": "2010-08-30T18:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4678",
    "user": "https://github.com/mwhansen"
}
```

The patch had some typos so I uploaded a correct version.  The +Infinity/-Infinity thing should probably be a new ticket as it's something that should be done in a manner consistent for all functions.



---

archive/issue_comments_004679.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-30T18:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4679",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_004680.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-01T14:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4680",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004681.json:
```json
{
    "body": "good work, Mike!",
    "created_at": "2010-09-01T14:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4681",
    "user": "https://github.com/zimmermann6"
}
```

good work, Mike!



---

archive/issue_comments_004682.json:
```json
{
    "body": "The function `syntactically_equal()` in attachment:trac_783.patch doesn't contain doctests. I don't see how the changes to `sage/symbolic/expression.pyx` in that patch are relevant to this ticket. Perhaps these should be on a different ticket.",
    "created_at": "2010-09-12T12:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4682",
    "user": "https://github.com/burcin"
}
```

The function `syntactically_equal()` in attachment:trac_783.patch doesn't contain doctests. I don't see how the changes to `sage/symbolic/expression.pyx` in that patch are relevant to this ticket. Perhaps these should be on a different ticket.



---

archive/issue_comments_004683.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-12T12:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4683",
    "user": "https://github.com/burcin"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_004684.json:
```json
{
    "body": "Replying to [comment:12 burcin]:\n> The function `syntactically_equal()` in attachment:trac_783.patch doesn't contain doctests. I don't see how the changes to `sage/symbolic/expression.pyx` in that patch are relevant to this ticket. Perhaps these should be on a different ticket.\n\nyou are perfectly right, Burcin. Mike, please could you remove that unused code from the patch?\nPaul",
    "created_at": "2010-09-12T12:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4684",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:12 burcin]:
> The function `syntactically_equal()` in attachment:trac_783.patch doesn't contain doctests. I don't see how the changes to `sage/symbolic/expression.pyx` in that patch are relevant to this ticket. Perhaps these should be on a different ticket.

you are perfectly right, Burcin. Mike, please could you remove that unused code from the patch?
Paul



---

archive/issue_comments_004685.json:
```json
{
    "body": "Attachment [trac_783.patch](tarball://root/attachments/some-uuid/ticket783/trac_783.patch) by @mwhansen created at 2010-09-12 17:00:00",
    "created_at": "2010-09-12T17:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4685",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_783.patch](tarball://root/attachments/some-uuid/ticket783/trac_783.patch) by @mwhansen created at 2010-09-12 17:00:00



---

archive/issue_comments_004686.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-12T17:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4686",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_004687.json:
```json
{
    "body": "Sorry about that -- I'm not sure how those changes snuck into that patch.",
    "created_at": "2010-09-12T17:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4687",
    "user": "https://github.com/mwhansen"
}
```

Sorry about that -- I'm not sure how those changes snuck into that patch.



---

archive/issue_comments_004688.json:
```json
{
    "body": "> Sorry about that -- I'm not sure how those changes snuck into that patch. \n\nI'm sorry I didn't see that during my review. Anyway I confirm all doctests still pass\n(tested with Sage 4.5.2).\n\nPaul",
    "created_at": "2010-09-13T10:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4688",
    "user": "https://github.com/zimmermann6"
}
```

> Sorry about that -- I'm not sure how those changes snuck into that patch. 

I'm sorry I didn't see that during my review. Anyway I confirm all doctests still pass
(tested with Sage 4.5.2).

Paul



---

archive/issue_comments_004689.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/783#issuecomment-4689",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_000890.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:13:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/783#event-890"
}
```
