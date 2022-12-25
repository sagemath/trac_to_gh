# Issue 3401: extend li to work with complex input

archive/issues_003401.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  myurko @benjaminfjones\n\nHere is some example code from M. Yurko that explains how to do this.\nI think something based on this should be put into the Li function itself.\n\n\n```\nO.K. I defined li(x) as follows:\n\ndef li(z): #def log integral for real and complex variables\n   if z in RR and z >= 2: #check if real number greater than 2\n       return Li(z) +\n1.045163780117492784844588889194613136522615578151 #adjust for offset\nin SAGE def\n   elif z == 1:\n       return -infinity\n   else: #mode for complex and below 2 from incomplete gamma\n       z = CDF(z)\n       return -gamma_inc(0,-log(z)) + (log(log(z))-log(1/log(z)))/2-\nlog(-log(z))\n\nThe first part uses SAGE's built in Li(x) but adjusts for the offset.\nThe second part should be self explanatory. The third part uses a\nformula involving the incomplete gamma function which I found on the\nWolfram Functions website. On testing different values with an\nexternal calculator,  the third statement appears to only be valid for\nnegative reals and complex numbers. This leaves the interval [0,2)\nundefined. Please note that I have no background in complex analysis\nand that my above statements about domain are only based upon\nexperimentation.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3401\n\n",
    "created_at": "2008-06-11T17:46:09Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.3",
    "title": "extend li to work with complex input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3401",
    "user": "https://github.com/williamstein"
}
```
Assignee: @garyfurnish

CC:  myurko @benjaminfjones

Here is some example code from M. Yurko that explains how to do this.
I think something based on this should be put into the Li function itself.


```
O.K. I defined li(x) as follows:

def li(z): #def log integral for real and complex variables
   if z in RR and z >= 2: #check if real number greater than 2
       return Li(z) +
1.045163780117492784844588889194613136522615578151 #adjust for offset
in SAGE def
   elif z == 1:
       return -infinity
   else: #mode for complex and below 2 from incomplete gamma
       z = CDF(z)
       return -gamma_inc(0,-log(z)) + (log(log(z))-log(1/log(z)))/2-
log(-log(z))

The first part uses SAGE's built in Li(x) but adjusts for the offset.
The second part should be self explanatory. The third part uses a
formula involving the incomplete gamma function which I found on the
Wolfram Functions website. On testing different values with an
external calculator,  the third statement appears to only be valid for
negative reals and complex numbers. This leaves the interval [0,2)
undefined. Please note that I have no background in complex analysis
and that my above statements about domain are only based upon
experimentation.
```


Issue created by migration from https://trac.sagemath.org/ticket/3401





---

archive/issue_comments_023769.json:
```json
{
    "body": "No version\n\n```\ndef li(z): #def log integral for real and complex variables\n   if z in RR and z >= 2: #check if real number greater than 2\n       return Li(z) +\n1.045163780117492784844588889194613136522615578151 #adjust for offset\nin SAGE def\n   elif z == 0:\n       return 0\n   elif z > 1 and z < 2:\n       return Ei(log(z))\n   elif z == 1:\n       return -infinity\n   elif z > 0 and z < 1:\n       return\n   else: #mode for complex and below 2 from incomplete gamma\n       z = CDF(z)\n       return -gamma_inc(0,-log(z)) + (log(log(z))-log(1/log(z)))/2-\nlog(-log(z))\n\n```\n",
    "created_at": "2008-06-11T18:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23769",
    "user": "https://github.com/williamstein"
}
```

No version

```
def li(z): #def log integral for real and complex variables
   if z in RR and z >= 2: #check if real number greater than 2
       return Li(z) +
1.045163780117492784844588889194613136522615578151 #adjust for offset
in SAGE def
   elif z == 0:
       return 0
   elif z > 1 and z < 2:
       return Ei(log(z))
   elif z == 1:
       return -infinity
   elif z > 0 and z < 1:
       return
   else: #mode for complex and below 2 from incomplete gamma
       z = CDF(z)
       return -gamma_inc(0,-log(z)) + (log(log(z))-log(1/log(z)))/2-
log(-log(z))

```




---

archive/issue_comments_023770.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23770",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_023771.json:
```json
{
    "body": "Attachment [Li(x).patch](tarball://root/attachments/some-uuid/ticket3401/Li(x).patch) by myurko created at 2009-10-29 23:21:47",
    "created_at": "2009-10-29T23:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23771",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

Attachment [Li(x).patch](tarball://root/attachments/some-uuid/ticket3401/Li(x).patch) by myurko created at 2009-10-29 23:21:47



---

archive/issue_comments_023772.json:
```json
{
    "body": "Attachment [Lix_2.patch](tarball://root/attachments/some-uuid/ticket3401/Lix_2.patch) by myurko created at 2009-10-29 23:21:56",
    "created_at": "2009-10-29T23:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23772",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

Attachment [Lix_2.patch](tarball://root/attachments/some-uuid/ticket3401/Lix_2.patch) by myurko created at 2009-10-29 23:21:56



---

archive/issue_comments_023773.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T23:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23773",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023774.json:
```json
{
    "body": "Attachment [Lix_3.patch](tarball://root/attachments/some-uuid/ticket3401/Lix_3.patch) by myurko created at 2009-10-29 23:23:52\n\nSorry in advance to the reviewer and release manager, but I couldn't figure out how to flatten the patches without applying them.",
    "created_at": "2009-10-29T23:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23774",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

Attachment [Lix_3.patch](tarball://root/attachments/some-uuid/ticket3401/Lix_3.patch) by myurko created at 2009-10-29 23:23:52

Sorry in advance to the reviewer and release manager, but I couldn't figure out how to flatten the patches without applying them.



---

archive/issue_comments_023775.json:
```json
{
    "body": "I've added a patch which folds the above patches together and deprecates the eps_rel and err_bound parameters so that code that uses them won't \"break\", but will get a deprecation warning.\n\nI'm okay with myurko's changes so if someone could sign off on the deprecation warning, that'd be great.",
    "created_at": "2009-11-04T09:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23775",
    "user": "https://github.com/mwhansen"
}
```

I've added a patch which folds the above patches together and deprecates the eps_rel and err_bound parameters so that code that uses them won't "break", but will get a deprecation warning.

I'm okay with myurko's changes so if someone could sign off on the deprecation warning, that'd be great.



---

archive/issue_comments_023776.json:
```json
{
    "body": "Overall looks good, but there should be at least one doctest for the new DeprecationWarnings (I think this was agreed upon somewhere on sage-devel), and there should also be documentation that this actually fulfills the ticket - namely, to extend Li to complex input!  It certainly does, but I have no idea if the output is correct (I assume it is):\n\n```\nsage: Li(1+i)\n-0.431252110896297 + 2.05958421419258*I\nsage: Li(2+i)\n0.366095261900308 + 1.22470693841030*I\nsage: Li(2+2*i)\n0.875423840014232 + 1.96947430597102*I\nsage: Li(-2-2*i)\n-0.333825651054542 - 3.94714365810975*I\nsage: Li(-8)\n-1.74509249432858 + 5.26897573517771*I\nsage: Li(-10)\n-2.04384864349662 + 5.69678038115052*I\nsage: Li(-100)\n-15.9214591889007 + 17.3366538615045*I\n```\n\nSomething like that should be added.",
    "created_at": "2009-11-10T13:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23776",
    "user": "https://github.com/kcrisman"
}
```

Overall looks good, but there should be at least one doctest for the new DeprecationWarnings (I think this was agreed upon somewhere on sage-devel), and there should also be documentation that this actually fulfills the ticket - namely, to extend Li to complex input!  It certainly does, but I have no idea if the output is correct (I assume it is):

```
sage: Li(1+i)
-0.431252110896297 + 2.05958421419258*I
sage: Li(2+i)
0.366095261900308 + 1.22470693841030*I
sage: Li(2+2*i)
0.875423840014232 + 1.96947430597102*I
sage: Li(-2-2*i)
-0.333825651054542 - 3.94714365810975*I
sage: Li(-8)
-1.74509249432858 + 5.26897573517771*I
sage: Li(-10)
-2.04384864349662 + 5.69678038115052*I
sage: Li(-100)
-15.9214591889007 + 17.3366538615045*I
```

Something like that should be added.



---

archive/issue_comments_023777.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T13:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23777",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023778.json:
```json
{
    "body": "Attachment [trac_3401.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401.patch) by @mwhansen created at 2010-01-16 17:57:25",
    "created_at": "2010-01-16T17:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23778",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3401.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401.patch) by @mwhansen created at 2010-01-16 17:57:25



---

archive/issue_comments_023779.json:
```json
{
    "body": "I've put up a new patch which address the above concerns.",
    "created_at": "2010-01-16T17:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23779",
    "user": "https://github.com/mwhansen"
}
```

I've put up a new patch which address the above concerns.



---

archive/issue_comments_023780.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-16T17:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23780",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023781.json:
```json
{
    "body": "Attachment [trac_3401-reviewed.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401-reviewed.patch) by @kcrisman created at 2010-01-18 16:48:18\n\nLooks good - sometimes slower, sometimes faster, but it's much better to have the complex functionality than worry about the rest.  I removed an auxiliary function which only existed to allow the previous implementation.  Positive review!",
    "created_at": "2010-01-18T16:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23781",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_3401-reviewed.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401-reviewed.patch) by @kcrisman created at 2010-01-18 16:48:18

Looks good - sometimes slower, sometimes faster, but it's much better to have the complex functionality than worry about the rest.  I removed an auxiliary function which only existed to allow the previous implementation.  Positive review!



---

archive/issue_comments_023782.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T16:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23782",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023783.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T18:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23783",
    "user": "https://github.com/burcin"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_023784.json:
```json
{
    "body": "Sorry to come in this late to the discussion, but this needs more work.\n\nThe `prec` argument to symbolic functions is deprecated, adding it to `Li` now doesn't make sense.\n\n\n```\nsage: gamma(10,prec=100)\n.../_home_burcin__sage_init_sage_0.py:1: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example gamma(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., gamma(1).n(300), instead.\n  # -*- coding: utf-8 -*-\n362880.00000000000000000000000\n```\n\n\nYou can get the precision from the argument provided by the user. If the user needs a higher precision, they should explicitly convert the argument to a higher precision, for example by using `RealFiel(300)(val)`.\n\nWe should also start converting these to proper symbolic functions that remain symbolic on exact input, but that can be left to another ticket.",
    "created_at": "2010-01-18T18:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23784",
    "user": "https://github.com/burcin"
}
```

Sorry to come in this late to the discussion, but this needs more work.

The `prec` argument to symbolic functions is deprecated, adding it to `Li` now doesn't make sense.


```
sage: gamma(10,prec=100)
.../_home_burcin__sage_init_sage_0.py:1: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example gamma(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., gamma(1).n(300), instead.
  # -*- coding: utf-8 -*-
362880.00000000000000000000000
```


You can get the precision from the argument provided by the user. If the user needs a higher precision, they should explicitly convert the argument to a higher precision, for example by using `RealFiel(300)(val)`.

We should also start converting these to proper symbolic functions that remain symbolic on exact input, but that can be left to another ticket.



---

archive/issue_comments_023785.json:
```json
{
    "body": "What is wrong with the prec argument? By default it is left as None and will get the precision from the argument as you said.",
    "created_at": "2010-02-10T15:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23785",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

What is wrong with the prec argument? By default it is left as None and will get the precision from the argument as you said.



---

archive/issue_comments_023786.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-28T16:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23786",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_023787.json:
```json
{
    "body": "Possibly related to #11143.",
    "created_at": "2011-10-09T01:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23787",
    "user": "https://github.com/kcrisman"
}
```

Possibly related to #11143.



---

archive/issue_comments_023788.json:
```json
{
    "body": "In #11143 a fully symbolic function is defined for `li(x)` called `exp_integral_li`, the non-offset logarithmic integral. It would be very easy to add `Li` by simply returning `exp_integral_li(x) - exp_integral_li(2)`. On the other hand, adding a symbolic version of `Li`  would be equally easy by copying the definition of `exp_integral_li` and making one simple change. \n\nIf so, what would a good name for the offset `Li` be? Maybe `exp_integral_li_offset`? \n\nAnother thought is that in #11143, we could add an optional parameter `offset` to the init method for `exp_integral_li` which would return `Li` instead of `li`. The eval and evalf methods could be bound in the init call to return the right values and the derivative is obviously the same for both.\n\nEither of these solutions could be put into #11143 without much effort and that would take care of the issue in this ticket because evaluation at complex inputs is handled by mpmath for all the functions defined there.",
    "created_at": "2011-10-09T01:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23788",
    "user": "https://github.com/benjaminfjones"
}
```

In #11143 a fully symbolic function is defined for `li(x)` called `exp_integral_li`, the non-offset logarithmic integral. It would be very easy to add `Li` by simply returning `exp_integral_li(x) - exp_integral_li(2)`. On the other hand, adding a symbolic version of `Li`  would be equally easy by copying the definition of `exp_integral_li` and making one simple change. 

If so, what would a good name for the offset `Li` be? Maybe `exp_integral_li_offset`? 

Another thought is that in #11143, we could add an optional parameter `offset` to the init method for `exp_integral_li` which would return `Li` instead of `li`. The eval and evalf methods could be bound in the init call to return the right values and the derivative is obviously the same for both.

Either of these solutions could be put into #11143 without much effort and that would take care of the issue in this ticket because evaluation at complex inputs is handled by mpmath for all the functions defined there.



---

archive/issue_comments_023789.json:
```json
{
    "body": "My understanding is that the offset `Li` is the same as `li`.  But maybe I've missed something while looking into this - I'm not a special functions expert.  \n\nI think that as long as we have both of these, and not named super-crazily - such as just being named `Li` and `li` - this would be fine.  I think the parameter is not needed.",
    "created_at": "2011-10-10T02:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23789",
    "user": "https://github.com/kcrisman"
}
```

My understanding is that the offset `Li` is the same as `li`.  But maybe I've missed something while looking into this - I'm not a special functions expert.  

I think that as long as we have both of these, and not named super-crazily - such as just being named `Li` and `li` - this would be fine.  I think the parameter is not needed.



---

archive/issue_comments_023790.json:
```json
{
    "body": "Just for the record:\n\n\n```python\nsage: import mpmath\nsage: mpmath.li(1+i)\nmpc(real='0.61391166922119556', imag='2.0595842141925775')\nsage: mpmath.li(1+i, offset=True)\nmpc(real='-0.43125211089629728', imag='2.0595842141925775')\n```\n\n\nBut maybe I've missed something (tl;dr).",
    "created_at": "2011-10-12T06:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23790",
    "user": "https://github.com/nexttime"
}
```

Just for the record:


```python
sage: import mpmath
sage: mpmath.li(1+i)
mpc(real='0.61391166922119556', imag='2.0595842141925775')
sage: mpmath.li(1+i, offset=True)
mpc(real='-0.43125211089629728', imag='2.0595842141925775')
```


But maybe I've missed something (tl;dr).



---

archive/issue_comments_023791.json:
```json
{
    "body": "I don't think you're missing anything.   In #11143 I think Benjamin is using mpmath as much as possible (though we should be checking timings...).  In principle, the hope is that #11143 will render this ticket obsolete, but I like to keep things complete for trollers :)",
    "created_at": "2011-10-12T12:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23791",
    "user": "https://github.com/kcrisman"
}
```

I don't think you're missing anything.   In #11143 I think Benjamin is using mpmath as much as possible (though we should be checking timings...).  In principle, the hope is that #11143 will render this ticket obsolete, but I like to keep things complete for trollers :)



---

archive/issue_comments_023792.json:
```json
{
    "body": "I'm changing this to make the (offset) Li symbolic and to work with complex input.  Simply using the ideas of #11143 should be sufficient.",
    "created_at": "2012-05-26T17:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23792",
    "user": "https://github.com/kcrisman"
}
```

I'm changing this to make the (offset) Li symbolic and to work with complex input.  Simply using the ideas of #11143 should be sufficient.



---

archive/issue_comments_023793.json:
```json
{
    "body": "Attachment [trac_3401_Li.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401_Li.patch) by martinx created at 2012-07-28 21:29:32\n\nSymbolic Li",
    "created_at": "2012-07-28T21:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23793",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

Attachment [trac_3401_Li.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401_Li.patch) by martinx created at 2012-07-28 21:29:32

Symbolic Li



---

archive/issue_comments_023794.json:
```json
{
    "body": "I have created a symbolic Li patch on top of #11143 on sage-5.2.rc1 .  This is my first go at a patch so no doubt will need a good scrubbing...\n\nPlease note doing this is a hobby for me and I have little or no time weekdays to do anything so my responses are likely to be slow.",
    "created_at": "2012-07-28T21:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23794",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

I have created a symbolic Li patch on top of #11143 on sage-5.2.rc1 .  This is my first go at a patch so no doubt will need a good scrubbing...

Please note doing this is a hobby for me and I have little or no time weekdays to do anything so my responses are likely to be slow.



---

archive/issue_comments_023795.json:
```json
{
    "body": "> I have created a symbolic Li patch on top of #11143 on sage-5.2.rc1 .  This is my first go at a patch so no doubt will need a good scrubbing...\nThat's okay, we all have to start somewhere!\n> Please note doing this is a hobby for me and I have little or no time weekdays to do anything so my responses are likely to be slow.  \nThat's also *very* true for many of us.  So we may also be slow to respond.",
    "created_at": "2012-07-29T01:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23795",
    "user": "https://github.com/kcrisman"
}
```

> I have created a symbolic Li patch on top of #11143 on sage-5.2.rc1 .  This is my first go at a patch so no doubt will need a good scrubbing...
That's okay, we all have to start somewhere!
> Please note doing this is a hobby for me and I have little or no time weekdays to do anything so my responses are likely to be slow.  
That's also *very* true for many of us.  So we may also be slow to respond.



---

archive/issue_comments_023796.json:
```json
{
    "body": "Hi `@`martinx, your patch looks very good. I spotted a few whitespace issues to clean up (I'll post a reviewer patch to do that). I'm running full tests now, but I expect a positive review. \n\n----\n\nI wonder if we really need three aliases at the top level for this function. Having `log_integral_eulerian` in addition to `Li` and `log_integral_offset` seems excessive to me, but if that's a common name for the function I'm OK with it.",
    "created_at": "2012-08-03T20:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23796",
    "user": "https://github.com/benjaminfjones"
}
```

Hi `@`martinx, your patch looks very good. I spotted a few whitespace issues to clean up (I'll post a reviewer patch to do that). I'm running full tests now, but I expect a positive review. 

----

I wonder if we really need three aliases at the top level for this function. Having `log_integral_eulerian` in addition to `Li` and `log_integral_offset` seems excessive to me, but if that's a common name for the function I'm OK with it.



---

archive/issue_comments_023797.json:
```json
{
    "body": "Attachment [trac_3401_review.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401_review.patch) by @benjaminfjones created at 2012-08-03 20:43:33\n\nreviewer patch",
    "created_at": "2012-08-03T20:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23797",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_3401_review.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401_review.patch) by @benjaminfjones created at 2012-08-03 20:43:33

reviewer patch



---

archive/issue_comments_023798.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-03T20:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23798",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023799.json:
```json
{
    "body": "Replying to [comment:22 benjaminfjones]:\n> I wonder if we really need three aliases at the top level for this function. Having `log_integral_eulerian` in addition to `Li` and `log_integral_offset` seems excessive to me, but if that's a common name for the function I'm OK with it.\n\nThere's also \"European Li\" (for the offset one) IIRC... ;-)",
    "created_at": "2012-08-04T11:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23799",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:22 benjaminfjones]:
> I wonder if we really need three aliases at the top level for this function. Having `log_integral_eulerian` in addition to `Li` and `log_integral_offset` seems excessive to me, but if that's a common name for the function I'm OK with it.

There's also "European Li" (for the offset one) IIRC... ;-)



---

archive/issue_comments_023800.json:
```json
{
    "body": "I will go with whatever the sagemath intelligentsia thinks appropriate for the number and name of any aliases. \n\nAnd I had better read up on coding conventions before my next efforts :)",
    "created_at": "2012-08-04T14:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23800",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

I will go with whatever the sagemath intelligentsia thinks appropriate for the number and name of any aliases. 

And I had better read up on coding conventions before my next efforts :)



---

archive/issue_comments_023801.json:
```json
{
    "body": "Don't worry about the coding conventions, some of them are unwritten and some of them are subtle. I found a few doctest errors after running `make ptestlong` with the patches applied. These should be simple to fix:\n\nChange 9 to 10:\n\n```\nFile \"/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/misc/sagedoc.py\", line 971:\n    sage: len(search_src('log', 'derivative', interact=False).splitlines()) < 9\nExpected:\n    True\nGot:\n    False\n```\n\n\nsimple change, `Li` is now fully symbolic:\n\n```\nFile \"/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/functions/transcendental.py\", lin\ne 195:\n    sage: Li(100)\nExpected:\n    29.080977804\nGot:\n    -log_integral(2) + log_integral(100)\n```\n\n\nThis one is more mysterious:\n\n```\nFile \"/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/symbolic/random_tests.py\", line 2\n36:\n    sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_eleme\nnt) # random\nException raised:\n    Traceback (most recent call last):      File \"/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jonesbe/sage/sage-5.2/local/bin/sagedoctest.py\", line 38, in run_one_ex\nample\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py\", line 1172, in run_one_e\nxample\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n        print \"ignore this\";  random_expr(Integer(50), nvars=Integer(3), coeff_generator=CDF.random_element) # random###line 236:\n    sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random\n\n    sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random\n      File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py\", line 258, in random_expr\n        return random_expr_helper(size, internal, leaves, verbose)\n      File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py\", line 206, in random_expr_helper\n        children = [random_expr_helper(n+1, internal, leaves, verbose) for n in nodes_per_child]\n      File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py\", line 209, in random_expr_helper\n        return r[1](*children)\n      File \"function.pyx\", line 432, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4941)\n        res = g_function_evalv(self._serial, vec, hold)\n      File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/integral.py\", line 173, in _eval_\n        return integrator(*args)\n      File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/external.py\", line 21, in maxima_integrator\n        result = maxima.sr_integral(expression, v, a, b)\n      File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py\", line 746, in sr_integral\n        raise error\n    RuntimeError: ECL says: Error executing code in Maxima: defint: upper limit of integration must be real; found \n     elliptic_eu(.18648175298340663*I-.7457199773032457,\n                 coth(v3)*(v3*(.12348638361486497*I+.29875723285490263)\n                          +v1*(.12348638361486497*I+.29875723285490263)\n                          -sinh(v3^(.5481180571998028*I-.5534231539946481))))\n```\n",
    "created_at": "2012-08-04T15:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23801",
    "user": "https://github.com/benjaminfjones"
}
```

Don't worry about the coding conventions, some of them are unwritten and some of them are subtle. I found a few doctest errors after running `make ptestlong` with the patches applied. These should be simple to fix:

Change 9 to 10:

```
File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/misc/sagedoc.py", line 971:
    sage: len(search_src('log', 'derivative', interact=False).splitlines()) < 9
Expected:
    True
Got:
    False
```


simple change, `Li` is now fully symbolic:

```
File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/functions/transcendental.py", lin
e 195:
    sage: Li(100)
Expected:
    29.080977804
Got:
    -log_integral(2) + log_integral(100)
```


This one is more mysterious:

```
File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/symbolic/random_tests.py", line 2
36:
    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_eleme
nt) # random
Exception raised:
    Traceback (most recent call last):      File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jonesbe/sage/sage-5.2/local/bin/sagedoctest.py", line 38, in run_one_ex
ample
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1172, in run_one_e
xample
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        print "ignore this";  random_expr(Integer(50), nvars=Integer(3), coeff_generator=CDF.random_element) # random###line 236:
    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random

    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 258, in random_expr
        return random_expr_helper(size, internal, leaves, verbose)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 206, in random_expr_helper
        children = [random_expr_helper(n+1, internal, leaves, verbose) for n in nodes_per_child]
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 209, in random_expr_helper
        return r[1](*children)
      File "function.pyx", line 432, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4941)
        res = g_function_evalv(self._serial, vec, hold)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 173, in _eval_
        return integrator(*args)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
        result = maxima.sr_integral(expression, v, a, b)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py", line 746, in sr_integral
        raise error
    RuntimeError: ECL says: Error executing code in Maxima: defint: upper limit of integration must be real; found 
     elliptic_eu(.18648175298340663*I-.7457199773032457,
                 coth(v3)*(v3*(.12348638361486497*I+.29875723285490263)
                          +v1*(.12348638361486497*I+.29875723285490263)
                          -sinh(v3^(.5481180571998028*I-.5534231539946481))))
```




---

archive/issue_comments_023802.json:
```json
{
    "body": "Replying to [comment:25 martinx]:\n> I will go with whatever the sagemath intelligentsia thinks appropriate for the number and name of any aliases. \n\nWell, with names put into the global namespace, the most important thing is that tab completion is likely to suggest you what you're looking for, i.e., the *prefix* of each name matters.  So in this case I think a single instance of `log_int*` (in addition to `[Ll]i*`, maybe more) would be sufficent.\n\nWith Sage 5.3.beta0, I currently get:\n\n```\nsage: log<TAB>\nlog             log_b           log_gamma       log_text        logstr          \nlog2            log_dvi         log_html        lognormvariate  \nsage: li<TAB>\nlicense                lim                    linear_program         list                   list_plot_semilogx\nlie                    limit                  linear_relation        list_composition       list_plot_semilogy\nlie_console            line                   linear_transformation  list_plot              \nlift                   line2d                 lisp                   list_plot3d            \nlift_to_sl2z           line3d                 lisp_console           list_plot_loglog       \nsage: Li<TAB>  \nLi                         LinearCode                 LinearCodeFromVectorSpace  \nLiE                        LinearCodeFromCheckMatrix  Lisp                       \nsage: euler<TAB>\neuler_gamma             euler_phi               eulers_method_2x2       \neuler_number            eulers_method           eulers_method_2x2_plot  \n```\n\n\n\n(Of course also the docstring for e.g. `li`, perhaps that of `Ei`, too, should refer to `Li` and vice versa.)",
    "created_at": "2012-08-04T15:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23802",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:25 martinx]:
> I will go with whatever the sagemath intelligentsia thinks appropriate for the number and name of any aliases. 

Well, with names put into the global namespace, the most important thing is that tab completion is likely to suggest you what you're looking for, i.e., the *prefix* of each name matters.  So in this case I think a single instance of `log_int*` (in addition to `[Ll]i*`, maybe more) would be sufficent.

With Sage 5.3.beta0, I currently get:

```
sage: log<TAB>
log             log_b           log_gamma       log_text        logstr          
log2            log_dvi         log_html        lognormvariate  
sage: li<TAB>
license                lim                    linear_program         list                   list_plot_semilogx
lie                    limit                  linear_relation        list_composition       list_plot_semilogy
lie_console            line                   linear_transformation  list_plot              
lift                   line2d                 lisp                   list_plot3d            
lift_to_sl2z           line3d                 lisp_console           list_plot_loglog       
sage: Li<TAB>  
Li                         LinearCode                 LinearCodeFromVectorSpace  
LiE                        LinearCodeFromCheckMatrix  Lisp                       
sage: euler<TAB>
euler_gamma             euler_phi               eulers_method_2x2       
euler_number            eulers_method           eulers_method_2x2_plot  
```



(Of course also the docstring for e.g. `li`, perhaps that of `Ei`, too, should refer to `Li` and vice versa.)



---

archive/issue_comments_023803.json:
```json
{
    "body": "(Also on top of the reviewer patch: ;-) )\n\n`s/eulerian/Eulerian/`\n\n`s/for `x > 1`/for `x \\geq 2`/`",
    "created_at": "2012-08-04T15:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23803",
    "user": "https://github.com/nexttime"
}
```

(Also on top of the reviewer patch: ;-) )

`s/eulerian/Eulerian/`

`s/for `x > 1`/for `x \geq 2`/`



---

archive/issue_comments_023804.json:
```json
{
    "body": "Nice theorem:\n\n\\exists x : `\\pi(x) > \\operatorname{Li}(z)`\n\n(`s/z/x/`)\n\n\n\n\n`s/`\n\n```\nHowever it is a theorem that there are very large, (e.g., around `10^{316}`) values of `x`\n```\n\n`/`\n\n```\nHowever, it is a theorem that there are very large values of `x` (e.g., around `10^{316}`)\n```\n\n`/`",
    "created_at": "2012-08-04T16:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23804",
    "user": "https://github.com/nexttime"
}
```

Nice theorem:

\exists x : `\pi(x) > \operatorname{Li}(z)`

(`s/z/x/`)




`s/`

```
However it is a theorem that there are very large, (e.g., around `10^{316}`) values of `x`
```

`/`

```
However, it is a theorem that there are very large values of `x` (e.g., around `10^{316}`)
```

`/`



---

archive/issue_comments_023805.json:
```json
{
    "body": "More nitpicking:  `s/\"polylog()\"/``polylog()``/` and/or make (it) a cross-reference (`:func:`polylog`` -- not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).",
    "created_at": "2012-08-04T16:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23805",
    "user": "https://github.com/nexttime"
}
```

More nitpicking:  `s/"polylog()"/``polylog()``/` and/or make (it) a cross-reference (`:func:`polylog`` -- not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).



---

archive/issue_comments_023806.json:
```json
{
    "body": "Replying to [comment:30 leif]:\n> ... not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).\n\n... or rather `:class:`polylog <sage.functions.log.Function_polylog>`` or something like that.",
    "created_at": "2012-08-04T16:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23806",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:30 leif]:
> ... not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).

... or rather `:class:`polylog <sage.functions.log.Function_polylog>`` or something like that.



---

archive/issue_comments_023807.json:
```json
{
    "body": "Replying to [comment:26 benjaminfjones]:\n> Don't worry about the coding conventions, some of them are unwritten and some of them are subtle.\n\nand I am a slow learner anyway :)\n\n>I found a few doctest errors after running `make ptestlong` with the patches applied. These should be simple to fix:\n> \n> Change 9 to 10:\nAgreed.\n\n> \n> simple change, `Li` is now fully symbolic:\n> {{{\n> File \"/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/functions/transcendental.py\", lin\n> e 195:\n>     sage: Li(100)\n> Expected:\n>     29.080977804\n> Got:\n>     -log_integral(2) + log_integral(100)\n> }}}\n\nThe function can be removed since it was just a convenience one to support the original li and Li.\n> \n> This one is more mysterious:\n> {{{\n> File \"/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/symbolic/random_tests.py\", line 2\n> 36:\n>     sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_eleme\n> nt) # random\n> Exception raised:\n>     Traceback (most recent call last):      File \"/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n>         self.run_one_example(test, example, filename, compileflags)\n>       File \"/home/jonesbe/sage/sage-5.2/local/bin/sagedoctest.py\", line 38, in run_one_ex\n> ample\n>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n>       File \"/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py\", line 1172, in run_one_e\n> xample\n>         compileflags, 1) in test.globs\n>       File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n>         print \"ignore this\";  random_expr(Integer(50), nvars=Integer(3), coeff_generator=CDF.random_element) # random###line 236:\n>     sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random\n> \n>     sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random\n>       File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py\", line 258, in random_expr\n>         return random_expr_helper(size, internal, leaves, verbose)\n>       File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py\", line 206, in random_expr_helper\n>         children = [random_expr_helper(n+1, internal, leaves, verbose) for n in nodes_per_child]\n>       File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py\", line 209, in random_expr_helper\n>         return r[1](*children)\n>       File \"function.pyx\", line 432, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4941)\n>         res = g_function_evalv(self._serial, vec, hold)\n>       File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/integral.py\", line 173, in _eval_\n>         return integrator(*args)\n>       File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/external.py\", line 21, in maxima_integrator\n>         result = maxima.sr_integral(expression, v, a, b)\n>       File \"/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py\", line 746, in sr_integral\n>         raise error\n>     RuntimeError: ECL says: Error executing code in Maxima: defint: upper limit of integration must be real; found \n>      elliptic_eu(.18648175298340663*I-.7457199773032457,\n>                  coth(v3)*(v3*(.12348638361486497*I+.29875723285490263)\n>                           +v1*(.12348638361486497*I+.29875723285490263)\n>                           -sinh(v3^(.5481180571998028*I-.5534231539946481))))\n> }}}\n\nThe function randomly selects from a list of all Pynac functions, to which is now added Li, and so now the functions chosen have changed.  The docs state that it will often raise an error because it tries to create an erroneous expression.  In this case it is trying to pass a complex expression to Maxima. Trial and error and got a return result setting the seed to 1.\n\nWhen I have worked out how to merge patches I'll post a revised patch for review that addresses all comments made so far.",
    "created_at": "2012-08-04T23:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23807",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

Replying to [comment:26 benjaminfjones]:
> Don't worry about the coding conventions, some of them are unwritten and some of them are subtle.

and I am a slow learner anyway :)

>I found a few doctest errors after running `make ptestlong` with the patches applied. These should be simple to fix:
> 
> Change 9 to 10:
Agreed.

> 
> simple change, `Li` is now fully symbolic:
> {{{
> File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/functions/transcendental.py", lin
> e 195:
>     sage: Li(100)
> Expected:
>     29.080977804
> Got:
>     -log_integral(2) + log_integral(100)
> }}}

The function can be removed since it was just a convenience one to support the original li and Li.
> 
> This one is more mysterious:
> {{{
> File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/symbolic/random_tests.py", line 2
> 36:
>     sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_eleme
> nt) # random
> Exception raised:
>     Traceback (most recent call last):      File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
>         self.run_one_example(test, example, filename, compileflags)
>       File "/home/jonesbe/sage/sage-5.2/local/bin/sagedoctest.py", line 38, in run_one_ex
> ample
>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
>       File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1172, in run_one_e
> xample
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_5[4]>", line 1, in <module>
>         print "ignore this";  random_expr(Integer(50), nvars=Integer(3), coeff_generator=CDF.random_element) # random###line 236:
>     sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
> 
>     sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 258, in random_expr
>         return random_expr_helper(size, internal, leaves, verbose)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 206, in random_expr_helper
>         children = [random_expr_helper(n+1, internal, leaves, verbose) for n in nodes_per_child]
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 209, in random_expr_helper
>         return r[1](*children)
>       File "function.pyx", line 432, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4941)
>         res = g_function_evalv(self._serial, vec, hold)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 173, in _eval_
>         return integrator(*args)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
>         result = maxima.sr_integral(expression, v, a, b)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py", line 746, in sr_integral
>         raise error
>     RuntimeError: ECL says: Error executing code in Maxima: defint: upper limit of integration must be real; found 
>      elliptic_eu(.18648175298340663*I-.7457199773032457,
>                  coth(v3)*(v3*(.12348638361486497*I+.29875723285490263)
>                           +v1*(.12348638361486497*I+.29875723285490263)
>                           -sinh(v3^(.5481180571998028*I-.5534231539946481))))
> }}}

The function randomly selects from a list of all Pynac functions, to which is now added Li, and so now the functions chosen have changed.  The docs state that it will often raise an error because it tries to create an erroneous expression.  In this case it is trying to pass a complex expression to Maxima. Trial and error and got a return result setting the seed to 1.

When I have worked out how to merge patches I'll post a revised patch for review that addresses all comments made so far.



---

archive/issue_comments_023808.json:
```json
{
    "body": "Replying to [comment:31 leif]:\n> Replying to [comment:30 leif]:\n> > ... not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).\n> \n> ... or rather `:class:`polylog <sage.functions.log.Function_polylog>`` or something like that.\n\nBoth seem to be allowed:   http://www.sagemath.org/doc/developer/sage_manuals.html#chapter-sage-manuals-links",
    "created_at": "2012-08-04T23:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23808",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

Replying to [comment:31 leif]:
> Replying to [comment:30 leif]:
> > ... not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).
> 
> ... or rather `:class:`polylog <sage.functions.log.Function_polylog>`` or something like that.

Both seem to be allowed:   http://www.sagemath.org/doc/developer/sage_manuals.html#chapter-sage-manuals-links



---

archive/issue_comments_023809.json:
```json
{
    "body": "Revised Li including reviewer patch",
    "created_at": "2012-08-05T00:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23809",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

Revised Li including reviewer patch



---

archive/issue_comments_023810.json:
```json
{
    "body": "Attachment [trac_3401.v2.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401.v2.patch) by martinx created at 2012-08-05 01:02:46\n\nI think v2 addresses all comments made so far and includes reviewer patch.  ptestlong passes I think;  I had some issues with sagedoc.py but that now passes all tests.  Too tired to run ptestlong yet again...........",
    "created_at": "2012-08-05T01:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23810",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

Attachment [trac_3401.v2.patch](tarball://root/attachments/some-uuid/ticket3401/trac_3401.v2.patch) by martinx created at 2012-08-05 01:02:46

I think v2 addresses all comments made so far and includes reviewer patch.  ptestlong passes I think;  I had some issues with sagedoc.py but that now passes all tests.  Too tired to run ptestlong yet again...........



---

archive/issue_comments_023811.json:
```json
{
    "body": "There are lots of lines touched in `sage/functions/transcendental.py` that don't seem to show any difference.  What's going on there? Have invisible non-whitespace characters been deleted?\n\nI looked over the command line and HTML docs for Li and they look good. Running tests now.",
    "created_at": "2012-08-06T23:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23811",
    "user": "https://github.com/benjaminfjones"
}
```

There are lots of lines touched in `sage/functions/transcendental.py` that don't seem to show any difference.  What's going on there? Have invisible non-whitespace characters been deleted?

I looked over the command line and HTML docs for Li and they look good. Running tests now.



---

archive/issue_comments_023812.json:
```json
{
    "body": "I see, it's just whitespace at the beginnings of lines. I guess that doesn't get highlighted by trac when you view the patch. Anyway, I think it's a good thing to clean up trailing whitespace, but you'll have to watch out that touching so many lines of the file doesn't cause conflicts with other patches that modify `sage/functions/transcendental.py`. In this case I think it's probably OK, I don't know of any other currently pending  positively reviewed patches that touch that file.\n\nIf leif is happy with the patch, I'll give it a positive review.",
    "created_at": "2012-08-07T04:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23812",
    "user": "https://github.com/benjaminfjones"
}
```

I see, it's just whitespace at the beginnings of lines. I guess that doesn't get highlighted by trac when you view the patch. Anyway, I think it's a good thing to clean up trailing whitespace, but you'll have to watch out that touching so many lines of the file doesn't cause conflicts with other patches that modify `sage/functions/transcendental.py`. In this case I think it's probably OK, I don't know of any other currently pending  positively reviewed patches that touch that file.

If leif is happy with the patch, I'll give it a positive review.



---

archive/issue_comments_023813.json:
```json
{
    "body": "Replying to [comment:36 benjaminfjones]:\n> I see, it's just whitespace at the beginnings of lines. I guess that doesn't get highlighted by trac when you view the patch. Anyway, I think it's a good thing to clean up trailing whitespace, but you'll have to watch out that touching so many lines of the file doesn't cause conflicts with other patches that modify `sage/functions/transcendental.py`. In this case I think it's probably OK, I don't know of any other currently pending  positively reviewed patches that touch that file.\n\nI got carried away with strip trailing whitespace command in Geany, in response to the previous review comments.  Will try to be more restrained next time ;-)\nMartin",
    "created_at": "2012-08-07T06:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23813",
    "user": "https://trac.sagemath.org/admin/accounts/users/martinx"
}
```

Replying to [comment:36 benjaminfjones]:
> I see, it's just whitespace at the beginnings of lines. I guess that doesn't get highlighted by trac when you view the patch. Anyway, I think it's a good thing to clean up trailing whitespace, but you'll have to watch out that touching so many lines of the file doesn't cause conflicts with other patches that modify `sage/functions/transcendental.py`. In this case I think it's probably OK, I don't know of any other currently pending  positively reviewed patches that touch that file.

I got carried away with strip trailing whitespace command in Geany, in response to the previous review comments.  Will try to be more restrained next time ;-)
Martin



---

archive/issue_comments_023814.json:
```json
{
    "body": "Patches apply cleanly on top of those at #11143 on top of sage-5.3.beta0. All long tests pass. I think this is ready to go.",
    "created_at": "2012-08-07T17:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23814",
    "user": "https://github.com/benjaminfjones"
}
```

Patches apply cleanly on top of those at #11143 on top of sage-5.3.beta0. All long tests pass. I think this is ready to go.



---

archive/issue_comments_023815.json:
```json
{
    "body": "Ok, I'm giving the most recent patch a positive review. If someone can quickly review the small, most recent fix at #11143, perhaps both of these tickets can be closed in sage-5.3.",
    "created_at": "2012-08-11T02:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23815",
    "user": "https://github.com/benjaminfjones"
}
```

Ok, I'm giving the most recent patch a positive review. If someone can quickly review the small, most recent fix at #11143, perhaps both of these tickets can be closed in sage-5.3.



---

archive/issue_comments_023816.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"beginner, Li, log, integral, symbolics, calculus\".",
    "created_at": "2012-08-11T02:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23816",
    "user": "https://github.com/benjaminfjones"
}
```

Changing keywords from "beginner" to "beginner, Li, log, integral, symbolics, calculus".



---

archive/issue_comments_023817.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-11T02:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23817",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023818.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2012-08-11T02:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23818",
    "user": "https://github.com/benjaminfjones"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_023819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-23T12:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3401#issuecomment-23819",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_003617.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-08-23T12:45:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3401",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3401#event-3617"
}
```
