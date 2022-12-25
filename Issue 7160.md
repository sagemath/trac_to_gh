# Issue 7160: comparison with quadratic number field elements needs work

archive/issues_007160.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @videlec\n\n\n```\nsage: I^2\n-1\nsage: bool(I^2 < 0)\nTrue\nsage: bool(I^2 > 0)\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7160\n\n",
    "created_at": "2009-10-08T18:38:28Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "comparison with quadratic number field elements needs work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7160",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @loefflerd

CC:  @videlec


```
sage: I^2
-1
sage: bool(I^2 < 0)
True
sage: bool(I^2 > 0)
True
```


Issue created by migration from https://trac.sagemath.org/ticket/7160





---

archive/issue_comments_059226.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-08T18:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59226",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059227.json:
```json
{
    "body": "This is basically the same as #6132.",
    "created_at": "2009-10-08T19:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59227",
    "user": "https://github.com/mwhansen"
}
```

This is basically the same as #6132.



---

archive/issue_comments_059228.json:
```json
{
    "body": "I think this is confusing:  you have an ordering of elements of a real or imaginary quadratic field which is based on some kind of lexicographic ordering on the representation of the elements rather than anything mathematical.  Presumably this is so lists, etc, can be sorted in a pythonic way.  But I find this bizarre:\n\n```\nsage: K.<i> = QuadraticField(-1)\nsage: i>0\nTrue\n```\n\nand this raises a strange error:\n\n```\nsage: K.<a> = NumberField(x^2+x-10)\nsage: a < -a\n---------------------------------------------------------------------------\nSystemError                               Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/790/_home_john__sage_init_sage_0.py in <module>()\n\nSystemError: error return without exception set\nsage: Type(K)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/790/_home_john__sage_init_sage_0.py in <module>()\n\nNameError: name 'Type' is not defined\nsage: type(K)\n<class 'sage.rings.number_field.number_field.NumberField_quadratic'>\n```\n",
    "created_at": "2009-10-29T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59228",
    "user": "https://github.com/JohnCremona"
}
```

I think this is confusing:  you have an ordering of elements of a real or imaginary quadratic field which is based on some kind of lexicographic ordering on the representation of the elements rather than anything mathematical.  Presumably this is so lists, etc, can be sorted in a pythonic way.  But I find this bizarre:

```
sage: K.<i> = QuadraticField(-1)
sage: i>0
True
```

and this raises a strange error:

```
sage: K.<a> = NumberField(x^2+x-10)
sage: a < -a
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/790/_home_john__sage_init_sage_0.py in <module>()

SystemError: error return without exception set
sage: Type(K)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/790/_home_john__sage_init_sage_0.py in <module>()

NameError: name 'Type' is not defined
sage: type(K)
<class 'sage.rings.number_field.number_field.NumberField_quadratic'>
```




---

archive/issue_comments_059229.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-29T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59229",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059230.json:
```json
{
    "body": "Apparently related to #6132 and #10064, see [this sage-devel discussion](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/01168722573ff736).",
    "created_at": "2011-02-07T15:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59230",
    "user": "https://github.com/kcrisman"
}
```

Apparently related to #6132 and #10064, see [this sage-devel discussion](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/01168722573ff736).



---

archive/issue_comments_059231.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-19T10:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59231",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059232.json:
```json
{
    "body": "I've put up a new patch which is minimally invasive and fixes the issue.",
    "created_at": "2011-12-19T10:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59232",
    "user": "https://github.com/mwhansen"
}
```

I've put up a new patch which is minimally invasive and fixes the issue.



---

archive/issue_comments_059233.json:
```json
{
    "body": "Does this result in any interesting speed regressions when doing things with I?",
    "created_at": "2011-12-19T15:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59233",
    "user": "https://github.com/kcrisman"
}
```

Does this result in any interesting speed regressions when doing things with I?



---

archive/issue_comments_059234.json:
```json
{
    "body": "1. Typo: \" comparision\" in sage/rings/number_field/number_field_element_quadratic.pyx. \n\n2. This code raises a big red flag for me:\n\n```\n        1704\t                from sage.rings.all import RR \n \t1705\t                r = RR(right) \n \t1706\t                l = RR(embedding(left)) \n \t1707\t                return cmp(l, r) \n```\n\nMy concern is that you're comparing to double (=53 bits) precision, which is totally arbitrary.  What if there is an embedding and cmp(left, right) requires 54 bits of precision to sort out?  I could probably with some work construct a nasty example of this, where the above code just gives totally the wrong answer.   I guess we need to (1) compute to precision of the embedding, and (2) if cmp(l,r)==0, then check something more?\n\n3. Where is \"self._element_class\" actually used?  I guess by the coercion model, but it's hard to see how from this patch, exactly. \n\n4. I feel like this is too much code that gets around a fundamental problem or bug in number field elements in the case of the reported problem, but leaves the underlying bug unfixed.  Note that *before* applying your patch:\n\n```\nsage: bool(I^2 < 0)\nTrue\nsage: (I^2).pyobject() < 0\nFalse\n```\n\n\nIt seems to me that the output of both lines above should be the same, right, but I bet pynac is evaluating the first comparison and not even going to the pyobject level. Similarly:\n\n\n```\nsage: bool(I^2 < SR(0))\nTrue\nsage: (I^2).pyobject() < SR(0).pyobject()\nFalse\n```\n\n\nThis is because in Sage we currently have:\n\n```\nsage: K.<I> = QuadraticField(-1)\nsage: I^2 < 0\nFalse\nsage: I^2\n-1\n```\n\nThis is, as Cremona pointed out, due to the arbitrary lexicographic ordering rather than using the one we get on the intersection of K and R inside embedding(K). \n\nSo... it seems to me that the real problem is that the arbitrary ordering is lame.   What you've done is implemented a natural fix in one very, very special case.  Maybe that's the intention, and maybe you had something more general before?  I don't know, since you changed the patch. \n\nI'm guessing your more general patch changed comparison for all elements to:\n  (1) check if there is an embedding of the parent(s), and (2) if so, use that to induce an embedding on *the* real subfield of the field(s).   That would be natural. \n\nSo all of the above, is just me understanding why you are doing what you're doing.  It might make sense to add something like this to the documentation.",
    "created_at": "2011-12-20T06:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59234",
    "user": "https://github.com/williamstein"
}
```

1. Typo: " comparision" in sage/rings/number_field/number_field_element_quadratic.pyx. 

2. This code raises a big red flag for me:

```
        1704	                from sage.rings.all import RR 
 	1705	                r = RR(right) 
 	1706	                l = RR(embedding(left)) 
 	1707	                return cmp(l, r) 
```

My concern is that you're comparing to double (=53 bits) precision, which is totally arbitrary.  What if there is an embedding and cmp(left, right) requires 54 bits of precision to sort out?  I could probably with some work construct a nasty example of this, where the above code just gives totally the wrong answer.   I guess we need to (1) compute to precision of the embedding, and (2) if cmp(l,r)==0, then check something more?

3. Where is "self._element_class" actually used?  I guess by the coercion model, but it's hard to see how from this patch, exactly. 

4. I feel like this is too much code that gets around a fundamental problem or bug in number field elements in the case of the reported problem, but leaves the underlying bug unfixed.  Note that *before* applying your patch:

```
sage: bool(I^2 < 0)
True
sage: (I^2).pyobject() < 0
False
```


It seems to me that the output of both lines above should be the same, right, but I bet pynac is evaluating the first comparison and not even going to the pyobject level. Similarly:


```
sage: bool(I^2 < SR(0))
True
sage: (I^2).pyobject() < SR(0).pyobject()
False
```


This is because in Sage we currently have:

```
sage: K.<I> = QuadraticField(-1)
sage: I^2 < 0
False
sage: I^2
-1
```

This is, as Cremona pointed out, due to the arbitrary lexicographic ordering rather than using the one we get on the intersection of K and R inside embedding(K). 

So... it seems to me that the real problem is that the arbitrary ordering is lame.   What you've done is implemented a natural fix in one very, very special case.  Maybe that's the intention, and maybe you had something more general before?  I don't know, since you changed the patch. 

I'm guessing your more general patch changed comparison for all elements to:
  (1) check if there is an embedding of the parent(s), and (2) if so, use that to induce an embedding on *the* real subfield of the field(s).   That would be natural. 

So all of the above, is just me understanding why you are doing what you're doing.  It might make sense to add something like this to the documentation.



---

archive/issue_comments_059235.json:
```json
{
    "body": "Note: With sage-4.8.alpha5 and this patch, all tests in devel/sage/sage pass.",
    "created_at": "2011-12-20T07:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59235",
    "user": "https://github.com/williamstein"
}
```

Note: With sage-4.8.alpha5 and this patch, all tests in devel/sage/sage pass.



---

archive/issue_comments_059236.json:
```json
{
    "body": "Replying to [comment:7 was]:\n> 2. This code raises a big red flag for me:\n\n```\n\t1704\t                from sage.rings.all import RR \n\t1705\t                r = RR(right) \n\t1706\t                l = RR(embedding(left)) \n\t1707\t                return cmp(l, r) \n```\n\n> My concern is that you're comparing to double (=53 bits) precision, which is totally arbitrary. What if there is an embedding and cmp(left, right) requires 54 bits of precision to sort out?  I could probably with some work construct a nasty example of this, where the above code just gives totally the wrong answer.   I guess we need to (1) compute to precision of the embedding, and (2) if cmp(l,r)==0, then check something more?\n\nIsn't this what we have the QQbar class for?",
    "created_at": "2011-12-20T09:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59236",
    "user": "https://github.com/loefflerd"
}
```

Replying to [comment:7 was]:
> 2. This code raises a big red flag for me:

```
	1704	                from sage.rings.all import RR 
	1705	                r = RR(right) 
	1706	                l = RR(embedding(left)) 
	1707	                return cmp(l, r) 
```

> My concern is that you're comparing to double (=53 bits) precision, which is totally arbitrary. What if there is an embedding and cmp(left, right) requires 54 bits of precision to sort out?  I could probably with some work construct a nasty example of this, where the above code just gives totally the wrong answer.   I guess we need to (1) compute to precision of the embedding, and (2) if cmp(l,r)==0, then check something more?

Isn't this what we have the QQbar class for?



---

archive/issue_comments_059237.json:
```json
{
    "body": "Attachment [trac_7160.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160.patch) by @mwhansen created at 2011-12-20 10:09:51",
    "created_at": "2011-12-20T10:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59237",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7160.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160.patch) by @mwhansen created at 2011-12-20 10:09:51



---

archive/issue_comments_059238.json:
```json
{
    "body": "I've added a new patch which should be better.  It turns out just using the embedding directly should be fine.",
    "created_at": "2011-12-20T10:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59238",
    "user": "https://github.com/mwhansen"
}
```

I've added a new patch which should be better.  It turns out just using the embedding directly should be fine.



---

archive/issue_comments_059239.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd35\".",
    "created_at": "2011-12-20T12:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59239",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "" to "sd35".



---

archive/issue_comments_059240.json:
```json
{
    "body": "Attachment [trac_7160-Q_to_quadratic_field_element.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-Q_to_quadratic_field_element.patch) by @burcin created at 2012-01-10 05:41:36\n\nReplying to [comment:7 was]:\n> 4. I feel like this is too much code that gets around a fundamental problem or bug in number field elements in the case of the reported problem, but leaves the underlying bug unfixed.  Note that *before* applying your patch:\n {{{\n sage: bool(I^2 < 0)\n True\n sage: (I^2).pyobject() < 0\n False\n }}}\n> \n> It seems to me that the output of both lines above should be the same, right, but I bet pynac is evaluating the first comparison and not even going to the pyobject level.\n\nThe first comparison is done in the `test_relation()` method of `sage.symbolic.expression.Expression`. This converts both sides of the relation to `CIF` and performs the comparison there.\n\n> Similarly:\n> \n> {{{\n> sage: bool(I^2 < SR(0))\n> True\n> sage: (I^2).pyobject() < SR(0).pyobject()\n> False\n> }}}\n> \n> This is because in Sage we currently have:\n> {{{\n> sage: K.<I> = QuadraticField(-1)\n> sage: I^2 < 0\n> False\n> sage: I^2\n> -1\n> }}}\n> This is, as Cremona pointed out, due to the arbitrary lexicographic ordering rather than using the one we get on the intersection of K and R inside embedding(K). \n> \n> So... it seems to me that the real problem is that the arbitrary ordering is lame.   What you've done is implemented a natural fix in one very, very special case.  Maybe that's the intention, and maybe you had something more general before?  I don't know, since you changed the patch. \n\nNote that this lame ordering is causing problems all over symbolics since `is_positive()` checks fail. See #10849, #10062, #10064 for examples.\n\n> I'm guessing your more general patch changed comparison for all elements to:\n>   (1) check if there is an embedding of the parent(s), and (2) if so, use that to induce an embedding on *the* real subfield of the field(s).   That would be natural. \n\nI attached a new patch at attachment:trac_7160-quadratic_number_field_element_comparison.patch, based on Mike's last patch attachment:trac_7160.patch. This changes the comparison function of quadratic number field elements to always use the embedding into `CC`.\n\nTimings with the patch:\n\n\n```\nsage: K.<sqrt2> = QuadraticField(2)\nsage: t = K.random_element(); t\n-2*sqrt2 - 35\nsage: u = K.random_element(); u\n-1\nsage: %timeit res = cmp(t,u)\n625 loops, best of 3: 659 \u00b5s per loop\nsage: u = K.random_element(); u\n-2*sqrt2 - 1\nsage: %timeit res = cmp(t,u)\n625 loops, best of 3: 807 \u00b5s per loop\n```\n\n\nWithout the patch:\n\n\n```\nsage: K.<sqrt2> = QuadraticField(2)\nsage: t = -2*sqrt2 - 35\nsage: u = K(-1)\nsage: %timeit res = cmp(t,u)\n625 loops, best of 3: 419 ns per loop\nsage: u = -2*sqrt2 - 1\nsage: %timeit res = cmp(t,u)\n625 loops, best of 3: 419 ns per loop\n```\n\n\nSo there is a significant slow down.\n\nThere are two failing doctests I need help with:\n\n\n```\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py\n**********************************************************************\nFile \"/home/burcin/sage/sage-5.0.prealpha0/devel/sage-main/sage/schemes/elliptic_curves/ell_curve_isogeny.py\", line 4361:\n    sage: _[0].rational_maps()\nExpected:\n    (((-4/25*i - 3/25)*x^5 + (-4/5*i + 2/5)*x^3 + x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)),\n    ((2/125*i - 11/125)*x^6*y + (64/125*i + 23/125)*x^4*y + (162/125*i - 141/125)*x^2*y + (-4/25*i - 3/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))\nGot:\n    (((4/25*i + 3/25)*x^5 + (4/5*i - 2/5)*x^3 - x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)), ((11/125*i + 2/125)*x^6*y + (-23/125*i + 64/125)*x^4*y + (141/125*i + 162/125)*x^2*y + (3/25*i - 4/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))\n**********************************************************************\nFile \"/home/burcin/sage/sage-5.0.prealpha0/devel/sage-main/sage/schemes/elliptic_curves/ell_curve_isogeny.py\", line 4622:\n    sage: isogenies_13_0(E)[0].rational_maps()\nExpected:\n    (((-4/169*r - 11/169)*x^13 + (-128/13*r - 456/13)*x^10 + (-1224/13*r - 2664/13)*x^7 + (-2208/13*r + 5472/13)*x^4 + (1152/13*r - 8064/13)*x)/(x^12 + (4*r - 36)*x^9 + (-1080/13*r + 3816/13)*x^6 + (2112/13*r + 5184/13)*x^3 + (17280/169*r - 1152/169)), ((18/2197*r - 35/2197)*x^18*y + (-23142/2197*r + 35478/2197)*x^15*y + (-1127520/2197*r + 1559664/2197)*x^12*y + (87744/2197*r + 5992704/2197)*x^9*y + (-6625152/2197*r + 9085824/2197)*x^6*y + (28919808/2197*r - 2239488/2197)*x^3*y + (-1990656/2197*r + 3870720/2197)*y)/(x^18 + (6*r - 54)*x^15 + (-3024/13*r + 11808/13)*x^12 + (31296/13*r - 51840/13)*x^9 + (-487296/169*r - 2070144/169)*x^6 + (-940032/169*r - 248832/169)*x^3 + (-1990656/2197*r + 3870720/2197)))\nGot:\n    (((7/338*r + 23/338)*x^13 + (-164/13*r - 420/13)*x^10 + (720/13*r + 3168/13)*x^7 + (3840/13*r - 576/13)*x^4 + (4608/13*r + 2304/13)*x)/(x^12 + (4*r + 36)*x^9 + (1080/13*r + 3816/13)*x^6 + (2112/13*r - 5184/13)*x^3 + (-17280/169*r - 1152/169)), ((18/2197*r + 35/2197)*x^18*y + (23142/2197*r + 35478/2197)*x^15*y + (-1127520/2197*r - 1559664/2197)*x^12*y + (-87744/2197*r + 5992704/2197)*x^9*y + (-6625152/2197*r - 9085824/2197)*x^6*y + (-28919808/2197*r - 2239488/2197)*x^3*y + (-1990656/2197*r - 3870720/2197)*y)/(x^18 + (6*r + 54)*x^15 + (3024/13*r + 11808/13)*x^12 + (31296/13*r + 51840/13)*x^9 + (487296/169*r - 2070144/169)*x^6 + (-940032/169*r + 248832/169)*x^3 + (1990656/2197*r + 3870720/2197)))\n```\n",
    "created_at": "2012-01-10T05:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59240",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7160-Q_to_quadratic_field_element.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-Q_to_quadratic_field_element.patch) by @burcin created at 2012-01-10 05:41:36

Replying to [comment:7 was]:
> 4. I feel like this is too much code that gets around a fundamental problem or bug in number field elements in the case of the reported problem, but leaves the underlying bug unfixed.  Note that *before* applying your patch:
 {{{
 sage: bool(I^2 < 0)
 True
 sage: (I^2).pyobject() < 0
 False
 }}}
> 
> It seems to me that the output of both lines above should be the same, right, but I bet pynac is evaluating the first comparison and not even going to the pyobject level.

The first comparison is done in the `test_relation()` method of `sage.symbolic.expression.Expression`. This converts both sides of the relation to `CIF` and performs the comparison there.

> Similarly:
> 
> {{{
> sage: bool(I^2 < SR(0))
> True
> sage: (I^2).pyobject() < SR(0).pyobject()
> False
> }}}
> 
> This is because in Sage we currently have:
> {{{
> sage: K.<I> = QuadraticField(-1)
> sage: I^2 < 0
> False
> sage: I^2
> -1
> }}}
> This is, as Cremona pointed out, due to the arbitrary lexicographic ordering rather than using the one we get on the intersection of K and R inside embedding(K). 
> 
> So... it seems to me that the real problem is that the arbitrary ordering is lame.   What you've done is implemented a natural fix in one very, very special case.  Maybe that's the intention, and maybe you had something more general before?  I don't know, since you changed the patch. 

Note that this lame ordering is causing problems all over symbolics since `is_positive()` checks fail. See #10849, #10062, #10064 for examples.

> I'm guessing your more general patch changed comparison for all elements to:
>   (1) check if there is an embedding of the parent(s), and (2) if so, use that to induce an embedding on *the* real subfield of the field(s).   That would be natural. 

I attached a new patch at attachment:trac_7160-quadratic_number_field_element_comparison.patch, based on Mike's last patch attachment:trac_7160.patch. This changes the comparison function of quadratic number field elements to always use the embedding into `CC`.

Timings with the patch:


```
sage: K.<sqrt2> = QuadraticField(2)
sage: t = K.random_element(); t
-2*sqrt2 - 35
sage: u = K.random_element(); u
-1
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 659 µs per loop
sage: u = K.random_element(); u
-2*sqrt2 - 1
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 807 µs per loop
```


Without the patch:


```
sage: K.<sqrt2> = QuadraticField(2)
sage: t = -2*sqrt2 - 35
sage: u = K(-1)
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 419 ns per loop
sage: u = -2*sqrt2 - 1
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 419 ns per loop
```


So there is a significant slow down.

There are two failing doctests I need help with:


```
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py
**********************************************************************
File "/home/burcin/sage/sage-5.0.prealpha0/devel/sage-main/sage/schemes/elliptic_curves/ell_curve_isogeny.py", line 4361:
    sage: _[0].rational_maps()
Expected:
    (((-4/25*i - 3/25)*x^5 + (-4/5*i + 2/5)*x^3 + x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)),
    ((2/125*i - 11/125)*x^6*y + (64/125*i + 23/125)*x^4*y + (162/125*i - 141/125)*x^2*y + (-4/25*i - 3/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))
Got:
    (((4/25*i + 3/25)*x^5 + (4/5*i - 2/5)*x^3 - x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)), ((11/125*i + 2/125)*x^6*y + (-23/125*i + 64/125)*x^4*y + (141/125*i + 162/125)*x^2*y + (3/25*i - 4/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))
**********************************************************************
File "/home/burcin/sage/sage-5.0.prealpha0/devel/sage-main/sage/schemes/elliptic_curves/ell_curve_isogeny.py", line 4622:
    sage: isogenies_13_0(E)[0].rational_maps()
Expected:
    (((-4/169*r - 11/169)*x^13 + (-128/13*r - 456/13)*x^10 + (-1224/13*r - 2664/13)*x^7 + (-2208/13*r + 5472/13)*x^4 + (1152/13*r - 8064/13)*x)/(x^12 + (4*r - 36)*x^9 + (-1080/13*r + 3816/13)*x^6 + (2112/13*r + 5184/13)*x^3 + (17280/169*r - 1152/169)), ((18/2197*r - 35/2197)*x^18*y + (-23142/2197*r + 35478/2197)*x^15*y + (-1127520/2197*r + 1559664/2197)*x^12*y + (87744/2197*r + 5992704/2197)*x^9*y + (-6625152/2197*r + 9085824/2197)*x^6*y + (28919808/2197*r - 2239488/2197)*x^3*y + (-1990656/2197*r + 3870720/2197)*y)/(x^18 + (6*r - 54)*x^15 + (-3024/13*r + 11808/13)*x^12 + (31296/13*r - 51840/13)*x^9 + (-487296/169*r - 2070144/169)*x^6 + (-940032/169*r - 248832/169)*x^3 + (-1990656/2197*r + 3870720/2197)))
Got:
    (((7/338*r + 23/338)*x^13 + (-164/13*r - 420/13)*x^10 + (720/13*r + 3168/13)*x^7 + (3840/13*r - 576/13)*x^4 + (4608/13*r + 2304/13)*x)/(x^12 + (4*r + 36)*x^9 + (1080/13*r + 3816/13)*x^6 + (2112/13*r - 5184/13)*x^3 + (-17280/169*r - 1152/169)), ((18/2197*r + 35/2197)*x^18*y + (23142/2197*r + 35478/2197)*x^15*y + (-1127520/2197*r - 1559664/2197)*x^12*y + (-87744/2197*r + 5992704/2197)*x^9*y + (-6625152/2197*r - 9085824/2197)*x^6*y + (-28919808/2197*r - 2239488/2197)*x^3*y + (-1990656/2197*r - 3870720/2197)*y)/(x^18 + (6*r + 54)*x^15 + (3024/13*r + 11808/13)*x^12 + (31296/13*r + 51840/13)*x^9 + (487296/169*r - 2070144/169)*x^6 + (-940032/169*r + 248832/169)*x^3 + (1990656/2197*r + 3870720/2197)))
```




---

archive/issue_comments_059241.json:
```json
{
    "body": "This patch doesn't apply to 5.0.beta11 -- see patchbot logs.",
    "created_at": "2012-03-29T17:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59241",
    "user": "https://github.com/loefflerd"
}
```

This patch doesn't apply to 5.0.beta11 -- see patchbot logs.



---

archive/issue_comments_059242.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-29T17:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59242",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059243.json:
```json
{
    "body": "Attachment [trac_7160-quadratic_number_field_element_comparison.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-quadratic_number_field_element_comparison.patch) by @mwhansen created at 2012-03-29 20:23:37\n\napply only this patch",
    "created_at": "2012-03-29T20:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59243",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7160-quadratic_number_field_element_comparison.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-quadratic_number_field_element_comparison.patch) by @mwhansen created at 2012-03-29 20:23:37

apply only this patch



---

archive/issue_comments_059244.json:
```json
{
    "body": "I rebased the patch to beta11.",
    "created_at": "2012-03-29T20:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59244",
    "user": "https://github.com/mwhansen"
}
```

I rebased the patch to beta11.



---

archive/issue_comments_059245.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-15T02:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59245",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059246.json:
```json
{
    "body": "This applies cleanly on beta13, I believe it needs review again?",
    "created_at": "2012-04-15T02:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59246",
    "user": "https://github.com/orlitzky"
}
```

This applies cleanly on beta13, I believe it needs review again?



---

archive/issue_comments_059247.json:
```json
{
    "body": "This ticket applies against cleanly against 5.1.beta0 but still has the two doctest failures.  This patch would get rid of several other problems -- #10064 and #10849 -- so it'd be nice to get in.",
    "created_at": "2012-05-25T04:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59247",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

This ticket applies against cleanly against 5.1.beta0 but still has the two doctest failures.  This patch would get rid of several other problems -- #10064 and #10849 -- so it'd be nice to get in.



---

archive/issue_comments_059248.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-29T19:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59248",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059249.json:
```json
{
    "body": "Hi,\n\nI made a sort of duplicate with #13213. My aim was to use the natural order of RR in the case of real embedding. For quadratic field it is quite easy and fast. In the same patch, I aim to implement other functions related to the real embedding (is_positive, floor, ceil, abs, ...).\n\nOn the other hand, the difference of timings with my patch have an order of magnitude of x10 and not of x1000.\n\nShould I close my ticket ? What to do with my patch ?",
    "created_at": "2012-07-09T07:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59249",
    "user": "https://github.com/videlec"
}
```

Hi,

I made a sort of duplicate with #13213. My aim was to use the natural order of RR in the case of real embedding. For quadratic field it is quite easy and fast. In the same patch, I aim to implement other functions related to the real embedding (is_positive, floor, ceil, abs, ...).

On the other hand, the difference of timings with my patch have an order of magnitude of x10 and not of x1000.

Should I close my ticket ? What to do with my patch ?



---

archive/issue_comments_059250.json:
```json
{
    "body": "Hi Vincent,\n\nthanks a lot for taking a look at this long standing problem.\n\nReplying to [comment:18 vdelecroix]:\n> I made a sort of duplicate with #13213. My aim was to use the natural order of RR in the case of real embedding. For quadratic field it is quite easy and fast. In the same patch, I aim to implement other functions related to the real embedding (is_positive, floor, ceil, abs, ...).\n\nFixing the comparison of quadratic number fields elements and implementing `floor`, `ceil`, etc. should be in separate patches.\n\n> On the other hand, the difference of timings with my patch have an order of magnitude of x10 and not of x1000.\n> \n> Should I close my ticket ? What to do with my patch ?\n\nSince your patch performs much better, we can move ahead using that. I will try to review your patch on #13213.\n\nOnce the patches in this ticket are rebased on your patch, we can close this as a duplicate.",
    "created_at": "2012-07-10T15:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59250",
    "user": "https://github.com/burcin"
}
```

Hi Vincent,

thanks a lot for taking a look at this long standing problem.

Replying to [comment:18 vdelecroix]:
> I made a sort of duplicate with #13213. My aim was to use the natural order of RR in the case of real embedding. For quadratic field it is quite easy and fast. In the same patch, I aim to implement other functions related to the real embedding (is_positive, floor, ceil, abs, ...).

Fixing the comparison of quadratic number fields elements and implementing `floor`, `ceil`, etc. should be in separate patches.

> On the other hand, the difference of timings with my patch have an order of magnitude of x10 and not of x1000.
> 
> Should I close my ticket ? What to do with my patch ?

Since your patch performs much better, we can move ahead using that. I will try to review your patch on #13213.

Once the patches in this ticket are rebased on your patch, we can close this as a duplicate.



---

archive/issue_comments_059251.json:
```json
{
    "body": "Now #13213 is in positive review (and performances much better than what I expected at the begining)! Should we add a doctest related to the example in the description of the ticket or do we simply close it as a duplicate ?",
    "created_at": "2013-05-15T17:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59251",
    "user": "https://github.com/videlec"
}
```

Now #13213 is in positive review (and performances much better than what I expected at the begining)! Should we add a doctest related to the example in the description of the ticket or do we simply close it as a duplicate ?



---

archive/issue_comments_059252.json:
```json
{
    "body": "> Now #13213 is in positive review (and performances much better than what I expected at the begining)! Should we add a doctest related to the example in the description of the ticket or do we simply close it as a duplicate ?\nIf there are nearly identical examples to these in #13213, then I think that's okay; if there is nothing like this there, we should add a trivial patch. to check it's improved.   I'm not going to look through that whole patch to find ones like this but presumably you know whether there is one like that, as the author :)",
    "created_at": "2013-05-15T18:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59252",
    "user": "https://github.com/kcrisman"
}
```

> Now #13213 is in positive review (and performances much better than what I expected at the begining)! Should we add a doctest related to the example in the description of the ticket or do we simply close it as a duplicate ?
If there are nearly identical examples to these in #13213, then I think that's okay; if there is nothing like this there, we should add a trivial patch. to check it's improved.   I'm not going to look through that whole patch to find ones like this but presumably you know whether there is one like that, as the author :)



---

archive/issue_comments_059253.json:
```json
{
    "body": "Attachment [trac_7160-doctest.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-doctest.patch) by @videlec created at 2013-05-15 20:25:48",
    "created_at": "2013-05-15T20:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59253",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_7160-doctest.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-doctest.patch) by @videlec created at 2013-05-15 20:25:48



---

archive/issue_comments_059254.json:
```json
{
    "body": "There are no example which deals with the symbolic ring... that's why I suggested to add some doctest here. See the proposition in the patch. Nevertheless, I found stupid the following behavior (or at least confusing)\n\n```\nsage: I**2 == -1\n-1 == -1\nsage: (I+4)**4 > 0\n-4 > 0\n```\n\n\napply trac_7160-doctest.patch",
    "created_at": "2013-05-15T20:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59254",
    "user": "https://github.com/videlec"
}
```

There are no example which deals with the symbolic ring... that's why I suggested to add some doctest here. See the proposition in the patch. Nevertheless, I found stupid the following behavior (or at least confusing)

```
sage: I**2 == -1
-1 == -1
sage: (I+4)**4 > 0
-4 > 0
```


apply trac_7160-doctest.patch



---

archive/issue_comments_059255.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-05-15T20:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59255",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059256.json:
```json
{
    "body": "Now #13213 is positive review. I guess we may close that ticket ?",
    "created_at": "2013-05-31T22:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59256",
    "user": "https://github.com/videlec"
}
```

Now #13213 is positive review. I guess we may close that ticket ?



---

archive/issue_comments_059257.json:
```json
{
    "body": "Attachment [trac_7160-doctest.take2.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-doctest.take2.patch) by @burcin created at 2013-06-03 13:52:04\n\nfix commit message, and sphinx trac link",
    "created_at": "2013-06-03T13:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59257",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7160-doctest.take2.patch](tarball://root/attachments/some-uuid/ticket7160/trac_7160-doctest.take2.patch) by @burcin created at 2013-06-03 13:52:04

fix commit message, and sphinx trac link



---

archive/issue_comments_059258.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-03T13:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59258",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059259.json:
```json
{
    "body": "I attached a new patch which fixes the commit message and missing `:` before the trac link in the documentation. This is good to go.\n\nThanks!",
    "created_at": "2013-06-03T13:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59259",
    "user": "https://github.com/burcin"
}
```

I attached a new patch which fixes the commit message and missing `:` before the trac link in the documentation. This is good to go.

Thanks!



---

archive/issue_comments_059260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-06T12:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7160#issuecomment-59260",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_007380.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-06-06T12:31:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7160",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7160#event-7380"
}
```
