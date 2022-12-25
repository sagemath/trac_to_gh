# Issue 7472: Taylor polynomial in two variables does not work

archive/issues_007472.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: taylor polynomial, derivative\n\nmake taylor(x*y^3,[x,y],[1,-1],4) work\n\nIssue created by migration from https://trac.sagemath.org/ticket/7472\n\n",
    "created_at": "2009-11-16T09:26:26Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Taylor polynomial in two variables does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7472",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

Keywords: taylor polynomial, derivative

make taylor(x*y^3,[x,y],[1,-1],4) work

Issue created by migration from https://trac.sagemath.org/ticket/7472





---

archive/issue_comments_062821.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-16T09:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62821",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062822.json:
```json
{
    "body": "I hope it has been fixed by the attached patch.",
    "created_at": "2009-11-16T09:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62822",
    "user": "https://github.com/robert-marik"
}
```

I hope it has been fixed by the attached patch.



---

archive/issue_comments_062823.json:
```json
{
    "body": "Attachment [trac-7472-taylor.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-taylor.patch) by @robert-marik created at 2009-11-16 09:32:27",
    "created_at": "2009-11-16T09:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62823",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7472-taylor.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-taylor.patch) by @robert-marik created at 2009-11-16 09:32:27



---

archive/issue_comments_062824.json:
```json
{
    "body": "this patch should be installed on the top of previous patch and improves documentation",
    "created_at": "2009-11-16T09:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62824",
    "user": "https://github.com/robert-marik"
}
```

this patch should be installed on the top of previous patch and improves documentation



---

archive/issue_comments_062825.json:
```json
{
    "body": "Attachment [trac-7472-taylor-fixed_doc.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-taylor-fixed_doc.patch) by @robert-marik created at 2009-11-16 10:32:02",
    "created_at": "2009-11-16T10:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62825",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7472-taylor-fixed_doc.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-taylor-fixed_doc.patch) by @robert-marik created at 2009-11-16 10:32:02



---

archive/issue_comments_062826.json:
```json
{
    "body": "I'm waiting for a build of 4.2.1... but in the meantime, is the new syntax (list for variables, list for numbers) more or less equivalent to other Sage functionality, or Mathematica/Maple syntax?  I honestly don't know, just asking.  It would be good to have compatibility, though.  For instance, plotting has the variable and range together (x,-5,5), so maybe [x,4] and [y,1] would be more appropriate? Looks like Mma allows for different \"distance\" for different variables, see [here](http://reference.wolfram.com/mathematica/ref/SeriesCoefficient.html)...  Just thinking out loud here.",
    "created_at": "2009-11-16T15:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62826",
    "user": "https://github.com/kcrisman"
}
```

I'm waiting for a build of 4.2.1... but in the meantime, is the new syntax (list for variables, list for numbers) more or less equivalent to other Sage functionality, or Mathematica/Maple syntax?  I honestly don't know, just asking.  It would be good to have compatibility, though.  For instance, plotting has the variable and range together (x,-5,5), so maybe [x,4] and [y,1] would be more appropriate? Looks like Mma allows for different "distance" for different variables, see [here](http://reference.wolfram.com/mathematica/ref/SeriesCoefficient.html)...  Just thinking out loud here.



---

archive/issue_comments_062827.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> I'm waiting for a build of 4.2.1... but in the meantime, is the new syntax (list for variables, list for numbers) more or less equivalent to other Sage functionality, or Mathematica/Maple syntax?  I honestly don't know, just asking.  It would be good to have compatibility, though.  For instance, plotting has the variable and range together (x,-5,5), so maybe [x,4] and [y,1] would be more appropriate? Looks like Mma allows for different \"distance\" for different variables, see [here](http://reference.wolfram.com/mathematica/ref/SeriesCoefficient.html)...  Just thinking out loud here.\n\nCan be done easily, the expression is passed to Maxima and Maxima allows many possibilities how to use [taylor command](http://maxima.sourceforge.net/docs/manual/en/maxima_30.html#Item_003a-taylor). I wanted to do as minotr change as possible. I was thinking for example also on the possibility to use different order for different variable, but I do not know if there is a demand for this.\n\nI do not know to much about habits in Sage notation, but I think that we evaluate expansion about point in n-dimensional space, so the coordinates should be together.",
    "created_at": "2009-11-16T19:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62827",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:3 kcrisman]:
> I'm waiting for a build of 4.2.1... but in the meantime, is the new syntax (list for variables, list for numbers) more or less equivalent to other Sage functionality, or Mathematica/Maple syntax?  I honestly don't know, just asking.  It would be good to have compatibility, though.  For instance, plotting has the variable and range together (x,-5,5), so maybe [x,4] and [y,1] would be more appropriate? Looks like Mma allows for different "distance" for different variables, see [here](http://reference.wolfram.com/mathematica/ref/SeriesCoefficient.html)...  Just thinking out loud here.

Can be done easily, the expression is passed to Maxima and Maxima allows many possibilities how to use [taylor command](http://maxima.sourceforge.net/docs/manual/en/maxima_30.html#Item_003a-taylor). I wanted to do as minotr change as possible. I was thinking for example also on the possibility to use different order for different variable, but I do not know if there is a demand for this.

I do not know to much about habits in Sage notation, but I think that we evaluate expansion about point in n-dimensional space, so the coordinates should be together.



---

archive/issue_comments_062828.json:
```json
{
    "body": "FWIW, I also like the MMA notation better. It is more consistent with the interface to `integrate`, `plot`, etc. as kcrisman mentioned.",
    "created_at": "2009-11-23T14:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62828",
    "user": "https://github.com/burcin"
}
```

FWIW, I also like the MMA notation better. It is more consistent with the interface to `integrate`, `plot`, etc. as kcrisman mentioned.



---

archive/issue_comments_062829.json:
```json
{
    "body": "OK. what about this, is it acceptable? \n\n```\nsage: y=var('y');taylor(sin(x)*exp(y),(x,y),(0,1),4)\n1/6*(y - 1)^3*x*e - 1/6*(y - 1)*x^3*e + 1/2*(y - 1)^2*x*e - 1/6*x^3*e + (y - 1)*x*e + x*e\nsage: y=var('y');taylor(sin(x)*exp(y),(x,0,4),(y,1,4))\n-1/144*((y - 1)^4*e + 4*(y - 1)^3*e + 12*(y - 1)^2*e + 24*(y - 1)*e + 24*e)*x^3 + 1/24*((y - 1)^4*e + 4*(y - 1)^3*e + 12*(y - 1)^2*e + 24*(y - 1)*e + 24*e)*x\nsage: y=var('y');taylor(sin(x)*exp(y),x,0,4)\n-1/6*x^3*e^y + x*e^y\nsage: y=var('y');taylor(sin(x)*exp(y),(x,0,4))\n-1/6*x^3*e^y + x*e^y\n```\n\nNote that in the first example the degree of  polynomial is 4 and in the second example the degree of polynomial is 7.\n(Not yet documented in the experimental patch)",
    "created_at": "2009-11-23T19:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62829",
    "user": "https://github.com/robert-marik"
}
```

OK. what about this, is it acceptable? 

```
sage: y=var('y');taylor(sin(x)*exp(y),(x,y),(0,1),4)
1/6*(y - 1)^3*x*e - 1/6*(y - 1)*x^3*e + 1/2*(y - 1)^2*x*e - 1/6*x^3*e + (y - 1)*x*e + x*e
sage: y=var('y');taylor(sin(x)*exp(y),(x,0,4),(y,1,4))
-1/144*((y - 1)^4*e + 4*(y - 1)^3*e + 12*(y - 1)^2*e + 24*(y - 1)*e + 24*e)*x^3 + 1/24*((y - 1)^4*e + 4*(y - 1)^3*e + 12*(y - 1)^2*e + 24*(y - 1)*e + 24*e)*x
sage: y=var('y');taylor(sin(x)*exp(y),x,0,4)
-1/6*x^3*e^y + x*e^y
sage: y=var('y');taylor(sin(x)*exp(y),(x,0,4))
-1/6*x^3*e^y + x*e^y
```

Note that in the first example the degree of  polynomial is 4 and in the second example the degree of polynomial is 7.
(Not yet documented in the experimental patch)



---

archive/issue_comments_062830.json:
```json
{
    "body": "apply on the top of the two other patches",
    "created_at": "2009-11-23T19:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62830",
    "user": "https://github.com/robert-marik"
}
```

apply on the top of the two other patches



---

archive/issue_comments_062831.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-11-23T19:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62831",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_062832.json:
```json
{
    "body": "Attachment [trac-7472-taylor-experimental.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-taylor-experimental.patch) by @robert-marik created at 2009-11-23 19:31:08",
    "created_at": "2009-11-23T19:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62832",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7472-taylor-experimental.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-taylor-experimental.patch) by @robert-marik created at 2009-11-23 19:31:08



---

archive/issue_comments_062833.json:
```json
{
    "body": "btw: it seems that taylor command in Maxima may return not only Taylor polynomial as in calculus books, but also truncated power expansion truncated at given power. I think that this could be something different from Taylor polynomial, so the name of the command is misleading. How is it in Mathematica and Maple? What should be in Sage?",
    "created_at": "2009-11-23T19:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62833",
    "user": "https://github.com/robert-marik"
}
```

btw: it seems that taylor command in Maxima may return not only Taylor polynomial as in calculus books, but also truncated power expansion truncated at given power. I think that this could be something different from Taylor polynomial, so the name of the command is misleading. How is it in Mathematica and Maple? What should be in Sage?



---

archive/issue_comments_062834.json:
```json
{
    "body": "New patch, replaces all previous patches. Notation is more Sage like.",
    "created_at": "2010-01-05T20:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62834",
    "user": "https://github.com/robert-marik"
}
```

New patch, replaces all previous patches. Notation is more Sage like.



---

archive/issue_comments_062835.json:
```json
{
    "body": "Attachment [trac-7472.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472.patch) by @robert-marik created at 2010-01-05 20:19:53",
    "created_at": "2010-01-05T20:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62835",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7472.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472.patch) by @robert-marik created at 2010-01-05 20:19:53



---

archive/issue_comments_062836.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-01-05T20:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62836",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_062837.json:
```json
{
    "body": "I assume the idea of different degrees for different variables was lost?  That really doesn't matter to me, though.\n\nWhat about this one, from the documentation?\n\n```\nsage: x,y=var('x y'); taylor(x*y^3,(x,1),(y,-1),4)  \n(y + 1)^3*(x - 1) + (y + 1)^3 - 3*(y + 1)^2*(x - 1) - 3*(y + 1)^2 + 3*(y + 1)*(x - 1) - x + 3*y + 3 \n```\n\nWhy doesn't it end this way?\n\n```\n-(x-1)+3*(y+1) -1\n```\n\nMaybe this is documented in Maxima?  It does seem odd, though, if I'm understanding what a multivariable Taylor polynomial is supposed to look like.\n\nBut overall this looks fine, assuming the Maxima computations are correct.  I am waiting for 4.3.alpha2 to build to see if there needs to be a rebase, but surely it would be trivial if so.",
    "created_at": "2010-01-13T21:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62837",
    "user": "https://github.com/kcrisman"
}
```

I assume the idea of different degrees for different variables was lost?  That really doesn't matter to me, though.

What about this one, from the documentation?

```
sage: x,y=var('x y'); taylor(x*y^3,(x,1),(y,-1),4)  
(y + 1)^3*(x - 1) + (y + 1)^3 - 3*(y + 1)^2*(x - 1) - 3*(y + 1)^2 + 3*(y + 1)*(x - 1) - x + 3*y + 3 
```

Why doesn't it end this way?

```
-(x-1)+3*(y+1) -1
```

Maybe this is documented in Maxima?  It does seem odd, though, if I'm understanding what a multivariable Taylor polynomial is supposed to look like.

But overall this looks fine, assuming the Maxima computations are correct.  I am waiting for 4.3.alpha2 to build to see if there needs to be a rebase, but surely it would be trivial if so.



---

archive/issue_comments_062838.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> I assume the idea of different degrees for different variables was lost?  That really doesn't matter to me, though.\n\nYes, different degrees for different variables seem odd to me (from the point of view of pure caculcus) and I do not know, if there is a demand to keep this functionality.\n\n> \n> What about this one, from the documentation?\n> {{{\n> sage: x,y=var('x y'); taylor(x*y^3,(x,1),(y,-1),4)  \n> (y + 1)^3*(x - 1) + (y + 1)^3 - 3*(y + 1)^2*(x - 1) - 3*(y + 1)^2 + 3*(y + 1)*(x - 1) - x + 3*y + 3 \n> }}}\n> Why doesn't it end this way?\n> {{{\n> -(x-1)+3*(y+1) -1\n> }}}\n> Maybe this is documented in Maxima?  It does seem odd, though, if I'm understanding what a multivariable Taylor polynomial is supposed to look like.\n\n\nVery good question :). Maxima in fact returns \n\n```\n-(x-1)+3*(y+1) -1\n```\n\nand Sage changes it somehow into \n\n```\n-x+3y+.... \n```\n\nI do not know why, perhaps I should ask on sage-devel. The same problem is also in current Sage. The linear Taylor polynomial hal always slope intercept form f'(a)*x+q, but should be (and Maxima returns) point slope form  f'(a)*(x-a)+f(a)\n\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: maxima(\"taylor(x^3,x,2,1)\")\n8+12*(x-2)\nsage: maxima(\"taylor(x^3,x,2,1)\").sage()\n12*x - 16\nsage: taylor(x^3,x,2,1)\n12*x - 16\nsage:\n```\n\n| Sage Version 4.3, Release Date: 2009-12-24                         |\n| Type notebook() for the GUI, and license() for information.        |\n> \n> But overall this looks fine, assuming the Maxima computations are correct.  I am waiting for 4.3.alpha2 to build to see if there needs to be a rebase, but surely it would be trivial if so.",
    "created_at": "2010-01-13T22:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62838",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:10 kcrisman]:
> I assume the idea of different degrees for different variables was lost?  That really doesn't matter to me, though.

Yes, different degrees for different variables seem odd to me (from the point of view of pure caculcus) and I do not know, if there is a demand to keep this functionality.

> 
> What about this one, from the documentation?
> {{{
> sage: x,y=var('x y'); taylor(x*y^3,(x,1),(y,-1),4)  
> (y + 1)^3*(x - 1) + (y + 1)^3 - 3*(y + 1)^2*(x - 1) - 3*(y + 1)^2 + 3*(y + 1)*(x - 1) - x + 3*y + 3 
> }}}
> Why doesn't it end this way?
> {{{
> -(x-1)+3*(y+1) -1
> }}}
> Maybe this is documented in Maxima?  It does seem odd, though, if I'm understanding what a multivariable Taylor polynomial is supposed to look like.


Very good question :). Maxima in fact returns 

```
-(x-1)+3*(y+1) -1
```

and Sage changes it somehow into 

```
-x+3y+.... 
```

I do not know why, perhaps I should ask on sage-devel. The same problem is also in current Sage. The linear Taylor polynomial hal always slope intercept form f'(a)*x+q, but should be (and Maxima returns) point slope form  f'(a)*(x-a)+f(a)



```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: maxima("taylor(x^3,x,2,1)")
8+12*(x-2)
sage: maxima("taylor(x^3,x,2,1)").sage()
12*x - 16
sage: taylor(x^3,x,2,1)
12*x - 16
sage:
```

| Sage Version 4.3, Release Date: 2009-12-24                         |
| Type notebook() for the GUI, and license() for information.        |
> 
> But overall this looks fine, assuming the Maxima computations are correct.  I am waiting for 4.3.alpha2 to build to see if there needs to be a rebase, but surely it would be trivial if so.



---

archive/issue_comments_062839.json:
```json
{
    "body": "Replying to [comment:11 robert.marik]:\n> I do not know why, perhaps I should ask on sage-devel. \n\nThe [question](http://groups.google.cz/group/sage-devel/browse_thread/thread/81a2e114559cac8a) at sage-devel.",
    "created_at": "2010-01-13T22:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62839",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:11 robert.marik]:
> I do not know why, perhaps I should ask on sage-devel. 

The [question](http://groups.google.cz/group/sage-devel/browse_thread/thread/81a2e114559cac8a) at sage-devel.



---

archive/issue_comments_062840.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-15T05:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62840",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062841.json:
```json
{
    "body": "I have made some trivial changes.  The new thing is a bug in some ways, but shouldn't keep us from merging this valuable functionality.",
    "created_at": "2010-01-15T05:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62841",
    "user": "https://github.com/kcrisman"
}
```

I have made some trivial changes.  The new thing is a bug in some ways, but shouldn't keep us from merging this valuable functionality.



---

archive/issue_comments_062842.json:
```json
{
    "body": "Apply only this.",
    "created_at": "2010-01-15T05:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62842",
    "user": "https://github.com/kcrisman"
}
```

Apply only this.



---

archive/issue_comments_062843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T22:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62843",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_062844.json:
```json
{
    "body": "Attachment [trac-7472-review.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-review.patch) by @rlmill created at 2010-01-18 22:57:36",
    "created_at": "2010-01-18T22:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7472#issuecomment-62844",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-7472-review.patch](tarball://root/attachments/some-uuid/ticket7472/trac-7472-review.patch) by @rlmill created at 2010-01-18 22:57:36



---

archive/issue_events_007698.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-18T22:57:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7472#event-7698"
}
```
