# Issue 6551: fix ugliness in printing of multivariate polynomials

archive/issues_006551.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb\n\nKeywords: print latex multivariate polynomial\n\nThe printing (and latex-ing) of multivariate polynomials is sometimes quite ugly, and inconsistent with the much prettier printing of univariate polynomials.  One gets things like the following (taken from doctests in the Sage library):\n\n\n```\n(-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y\n```\n\n\nor even\n\n\n```\nsage: xgcd((b+g)*y^2, (a+g)*y+b)\n((b^3 + (g)*b^2)/(a^2 + (2*g)*a + 3), 1, ((-b + (-g))/(a + (g)))*y + (b^2 + (g)*b)/(a^2 + (2*g)*a + 3))\n```\n\n\nThe attached patch fixes this, factors out common code for printing and latex-ing, and makes printing consistent across various representations of multivariate polynomials.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6551\n\n",
    "created_at": "2009-07-18T00:25:01Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix ugliness in printing of multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6551",
    "user": "https://github.com/aghitza"
}
```
Assignee: tbd

CC:  @malb

Keywords: print latex multivariate polynomial

The printing (and latex-ing) of multivariate polynomials is sometimes quite ugly, and inconsistent with the much prettier printing of univariate polynomials.  One gets things like the following (taken from doctests in the Sage library):


```
(-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y
```


or even


```
sage: xgcd((b+g)*y^2, (a+g)*y+b)
((b^3 + (g)*b^2)/(a^2 + (2*g)*a + 3), 1, ((-b + (-g))/(a + (g)))*y + (b^2 + (g)*b)/(a^2 + (2*g)*a + 3))
```


The attached patch fixes this, factors out common code for printing and latex-ing, and makes printing consistent across various representations of multivariate polynomials.


Issue created by migration from https://trac.sagemath.org/ticket/6551





---

archive/issue_comments_053315.json:
```json
{
    "body": "Attachment [trac_6551.patch](tarball://root/attachments/some-uuid/ticket6551/trac_6551.patch) by @aghitza created at 2009-07-18 00:26:09",
    "created_at": "2009-07-18T00:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53315",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6551.patch](tarball://root/attachments/some-uuid/ticket6551/trac_6551.patch) by @aghitza created at 2009-07-18 00:26:09



---

archive/issue_comments_053316.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2009-07-18T00:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53316",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_053317.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-18T00:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53317",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053318.json:
```json
{
    "body": "Bad news: this conflicts quite severely with my patches at #6500. I feel a bit guilty about this, because it was my referee comments on #6183 that pushed you into working on this, so I will handle preparing a rebased version.",
    "created_at": "2009-07-20T08:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53318",
    "user": "https://github.com/loefflerd"
}
```

Bad news: this conflicts quite severely with my patches at #6500. I feel a bit guilty about this, because it was my referee comments on #6183 that pushed you into working on this, so I will handle preparing a rebased version.



---

archive/issue_comments_053319.json:
```json
{
    "body": "Attachment [trac_6551-rebased_for_6500.patch](tarball://root/attachments/some-uuid/ticket6551/trac_6551-rebased_for_6500.patch) by @loefflerd created at 2009-07-20 09:05:14\n\napply after the three patches at #6500",
    "created_at": "2009-07-20T09:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53319",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6551-rebased_for_6500.patch](tarball://root/attachments/some-uuid/ticket6551/trac_6551-rebased_for_6500.patch) by @loefflerd created at 2009-07-20 09:05:14

apply after the three patches at #6500



---

archive/issue_comments_053320.json:
```json
{
    "body": "Here's a patch that applies cleanly on top of the #6500 patches. For what it's worth, the patch looks fine to me, but I'm not an expert on multivariate commutative algebra so probably it'd be better to get someone else to review it.",
    "created_at": "2009-07-20T09:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53320",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch that applies cleanly on top of the #6500 patches. For what it's worth, the patch looks fine to me, but I'm not an expert on multivariate commutative algebra so probably it'd be better to get someone else to review it.



---

archive/issue_comments_053321.json:
```json
{
    "body": "Hi Alex,\n\nI decided to run all doctests just to check that I had rebased the patch correctly, but there seems to be some funny business in quaternion algebras. This is with the #6500 patches and the rebased patch here, applied to 4.1:\n\n\n```\nsage -t  \"devel/sage/sage/algebras/quaternion_algebra_element.py\"                                      \n**********************************************************************                                 \nFile \"/home/david/sage-4.1/devel/sage/sage/algebras/quaternion_algebra_element.py\", line 17:           \n    sage: sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0(*t)    \nExpected:                                                                                              \n    2/3 + X*i - X^2*j + X^3*k                                                                          \nGot:                                                                                                   \n    2/3 + X*i + (-X^2)*j + X^3*k                                                                       \n**********************************************************************                                 \n```\n\nand\n\n```\n**********************************************************************                                 \nFile \"/home/david/sage-4.1/devel/sage/sage/algebras/quatalg/quaternion_algebra.py\", line 455:          \n    sage: QuaternionAlgebra(GF(17)(2),3).random_element()                                              \nExpected:                                                                                              \n    11 + 16*i + 4*j + 13*k                                                                             \nGot:                                                                                                   \n    11 - i + 4*j + 13*k                                                                                \n**********************************************************************                                 \n```\n\n\nThis has nothing to do with the rebasing, because I ran these two tests again using your original patch and without the #6500 patches and they failed in exactly the same way. Any idea what is going on here?\n\nDavid",
    "created_at": "2009-07-20T10:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53321",
    "user": "https://github.com/loefflerd"
}
```

Hi Alex,

I decided to run all doctests just to check that I had rebased the patch correctly, but there seems to be some funny business in quaternion algebras. This is with the #6500 patches and the rebased patch here, applied to 4.1:


```
sage -t  "devel/sage/sage/algebras/quaternion_algebra_element.py"                                      
**********************************************************************                                 
File "/home/david/sage-4.1/devel/sage/sage/algebras/quaternion_algebra_element.py", line 17:           
    sage: sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0(*t)    
Expected:                                                                                              
    2/3 + X*i - X^2*j + X^3*k                                                                          
Got:                                                                                                   
    2/3 + X*i + (-X^2)*j + X^3*k                                                                       
**********************************************************************                                 
```

and

```
**********************************************************************                                 
File "/home/david/sage-4.1/devel/sage/sage/algebras/quatalg/quaternion_algebra.py", line 455:          
    sage: QuaternionAlgebra(GF(17)(2),3).random_element()                                              
Expected:                                                                                              
    11 + 16*i + 4*j + 13*k                                                                             
Got:                                                                                                   
    11 - i + 4*j + 13*k                                                                                
**********************************************************************                                 
```


This has nothing to do with the rebasing, because I ran these two tests again using your original patch and without the #6500 patches and they failed in exactly the same way. Any idea what is going on here?

David



---

archive/issue_comments_053322.json:
```json
{
    "body": "Hi David,\n\nI just checked and I'm getting the same failures as you both on my laptop and sage.math (which is weird because I could swear I tested this about a million times).\n\nI have an inkling of what might be going on but it's going to have to wait until tomorrow because I'm falling asleep in my chair.\n\nThanks for reviewing, and for the work you put in rebasing the patch.",
    "created_at": "2009-07-20T14:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53322",
    "user": "https://github.com/aghitza"
}
```

Hi David,

I just checked and I'm getting the same failures as you both on my laptop and sage.math (which is weird because I could swear I tested this about a million times).

I have an inkling of what might be going on but it's going to have to wait until tomorrow because I'm falling asleep in my chair.

Thanks for reviewing, and for the work you put in rebasing the patch.



---

archive/issue_comments_053323.json:
```json
{
    "body": "Attachment [trac_6551_fix.patch](tarball://root/attachments/some-uuid/ticket6551/trac_6551_fix.patch) by @aghitza created at 2009-07-21 00:54:03",
    "created_at": "2009-07-21T00:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53323",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6551_fix.patch](tarball://root/attachments/some-uuid/ticket6551/trac_6551_fix.patch) by @aghitza created at 2009-07-21 00:54:03



---

archive/issue_comments_053324.json:
```json
{
    "body": "Yes, the problem was indeed that I was mixing up some stuff with #6183.\n\nI've added a small patch that takes care of this, and all tests (should) now pass.",
    "created_at": "2009-07-21T00:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53324",
    "user": "https://github.com/aghitza"
}
```

Yes, the problem was indeed that I was mixing up some stuff with #6183.

I've added a small patch that takes care of this, and all tests (should) now pass.



---

archive/issue_comments_053325.json:
```json
{
    "body": "Unfortunately, the patch has bit-rotted:\n\n\n```\napplying trac_6551-rebased_for_6500.patch\npatching file sage/matrix/matrix_mpolynomial_dense.pyx\nHunk #1 FAILED at 0\n1 out of 6 hunks FAILED -- saving rejects to file sage/matrix/matrix_mpolynomial_dense.pyx.rej\npatching file sage/rings/polynomial/polydict.pyx\nHunk #5 succeeded at 887 with fuzz 1 (offset 0 lines).\npatching file sage/rings/polynomial/toy_buchberger.py\nHunk #1 FAILED at 53\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/toy_buchberger.py.rej\npatching file sage/schemes/elliptic_curves/ell_curve_isogeny.py\nHunk #7 FAILED at 1864\n1 out of 21 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_curve_isogeny.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_6551-rebased_for_6500.patch\n```\n\n\nI read the patch and it looks fine so far. It is mainly a question of taste anyway IMHO. However, it might be worth checking for performance loses due to this patch (conversion to strings is used to communicate with Singular for instance)",
    "created_at": "2009-08-18T09:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53325",
    "user": "https://github.com/malb"
}
```

Unfortunately, the patch has bit-rotted:


```
applying trac_6551-rebased_for_6500.patch
patching file sage/matrix/matrix_mpolynomial_dense.pyx
Hunk #1 FAILED at 0
1 out of 6 hunks FAILED -- saving rejects to file sage/matrix/matrix_mpolynomial_dense.pyx.rej
patching file sage/rings/polynomial/polydict.pyx
Hunk #5 succeeded at 887 with fuzz 1 (offset 0 lines).
patching file sage/rings/polynomial/toy_buchberger.py
Hunk #1 FAILED at 53
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/toy_buchberger.py.rej
patching file sage/schemes/elliptic_curves/ell_curve_isogeny.py
Hunk #7 FAILED at 1864
1 out of 21 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_curve_isogeny.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6551-rebased_for_6500.patch
```


I read the patch and it looks fine so far. It is mainly a question of taste anyway IMHO. However, it might be worth checking for performance loses due to this patch (conversion to strings is used to communicate with Singular for instance)



---

archive/issue_comments_053326.json:
```json
{
    "body": "After thinking about this some more time: I think the proposed implementation for libSingular polynomials is way too slow. I suggest someone (e.g. me) re-implements the PolyDict printing for those to make it reasonably efficient.",
    "created_at": "2009-08-26T17:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53326",
    "user": "https://github.com/malb"
}
```

After thinking about this some more time: I think the proposed implementation for libSingular polynomials is way too slow. I suggest someone (e.g. me) re-implements the PolyDict printing for those to make it reasonably efficient.



---

archive/issue_comments_053327.json:
```json
{
    "body": "Martin,\n\nThanks for looking at this carefully, and sorry for having left things somewhat half-baked.  In my defense, I had already spent a long time getting the formatting to be consistent, and I'm not sure I'd be very good at speed issues.  But I completely agree with you that this is ubiquitous code that should be fast.  Count on me to referee your implementation when you're done with it.",
    "created_at": "2009-08-26T23:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53327",
    "user": "https://github.com/aghitza"
}
```

Martin,

Thanks for looking at this carefully, and sorry for having left things somewhat half-baked.  In my defense, I had already spent a long time getting the formatting to be consistent, and I'm not sure I'd be very good at speed issues.  But I completely agree with you that this is ubiquitous code that should be fast.  Count on me to referee your implementation when you're done with it.



---

archive/issue_events_015450.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15450"
}
```



---

archive/issue_events_015451.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15451"
}
```



---

archive/issue_events_015452.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15452"
}
```



---

archive/issue_events_015453.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15453"
}
```



---

archive/issue_events_015454.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15454"
}
```



---

archive/issue_events_015455.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15455"
}
```



---

archive/issue_events_015456.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15456"
}
```



---

archive/issue_comments_053328.json:
```json
{
    "body": "This ticket seems invalid. For the first example:\n\n\n```python\nsage: R.<x,y> = QQ[]\nsage: p = (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y\nsage: p\n-6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y\n```\n\n\nI cannot make the second example work (and this does not appear in the doctests).",
    "created_at": "2016-04-13T14:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53328",
    "user": "https://github.com/bgrenet"
}
```

This ticket seems invalid. For the first example:


```python
sage: R.<x,y> = QQ[]
sage: p = (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y
sage: p
-6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y
```


I cannot make the second example work (and this does not appear in the doctests).



---

archive/issue_events_015457.json:
```json
{
    "actor": "https://github.com/bgrenet",
    "created_at": "2016-04-13T14:28:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15457"
}
```



---

archive/issue_events_015458.json:
```json
{
    "actor": "https://github.com/bgrenet",
    "created_at": "2016-04-13T14:28:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15458"
}
```



---

archive/issue_comments_053329.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2016-04-18T08:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53329",
    "user": "https://github.com/bgrenet"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_053330.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6551#issuecomment-53330",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_015459.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-06-12T12:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6551",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6551#event-15459"
}
```
