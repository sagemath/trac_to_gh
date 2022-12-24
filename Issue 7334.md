# Issue 7334: Sage cannot simplify sums of logarithms

archive/issues_007334.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  fmaltey@nerim.fr\n\nKeywords: logarithm\n\nCurrently there is no direct way in Sage to apply the transformation:\n\n```\nlog(x) + log(y) -> log(x*y)\n```\n\n\nThe attached patch fixes this by inserting a call to logcontract()\nin the definition of simplify_radical.\n\nNow the following works:\n\n```\nsage: f = log(sqrt(2) - 1) + log(sqrt(2) + 1)\nsage: f.simplify_full()\n0\n```\n\n\nBut I'm not sure if this is the right place for this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7334\n\n",
    "created_at": "2009-10-28T17:32:35Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Sage cannot simplify sums of logarithms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7334",
    "user": "whuss"
}
```
Assignee: @burcin

CC:  fmaltey@nerim.fr

Keywords: logarithm

Currently there is no direct way in Sage to apply the transformation:

```
log(x) + log(y) -> log(x*y)
```


The attached patch fixes this by inserting a call to logcontract()
in the definition of simplify_radical.

Now the following works:

```
sage: f = log(sqrt(2) - 1) + log(sqrt(2) + 1)
sage: f.simplify_full()
0
```


But I'm not sure if this is the right place for this.

Issue created by migration from https://trac.sagemath.org/ticket/7334





---

archive/issue_comments_061337.json:
```json
{
    "body": "Attachment [trac-7334-logcontract.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract.patch) by whuss created at 2009-10-28 17:33:27",
    "created_at": "2009-10-28T17:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61337",
    "user": "whuss"
}
```

Attachment [trac-7334-logcontract.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract.patch) by whuss created at 2009-10-28 17:33:27



---

archive/issue_comments_061338.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T17:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61338",
    "user": "whuss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061339.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-29T18:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61339",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061340.json:
```json
{
    "body": "Hey, I love this idea!  And the code seems fine on the face of it.  \n\nBut probably it makes the most sense to make it separately available as a simplification, i.e. make a new method .simplify_log() or something.  Exposing as many of these as possible is good for the (many) users who keep one wanting some, but not all simplifications, which I think is something people really like about Maxima (from reading their lists).  \n\nAnyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  And one would want a (perhaps slightly complicated) example added to simplify_full() which shows that it's used correctly there as well.",
    "created_at": "2009-10-29T18:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61340",
    "user": "@kcrisman"
}
```

Hey, I love this idea!  And the code seems fine on the face of it.  

But probably it makes the most sense to make it separately available as a simplification, i.e. make a new method .simplify_log() or something.  Exposing as many of these as possible is good for the (many) users who keep one wanting some, but not all simplifications, which I think is something people really like about Maxima (from reading their lists).  

Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  And one would want a (perhaps slightly complicated) example added to simplify_full() which shows that it's used correctly there as well.



---

archive/issue_comments_061341.json:
```json
{
    "body": "I also think that it is better to keep the function logcontract separately from simplify_full() since sometimes the contraction of logarithms is not what user wants. Consider please also option which allows to set logconfcoef as described in [Maxima](http://maxima.sourceforge.net/docs/manual/en/maxima_14.html#Item_003a-logconcoeffp). This allows to contract expressions like log(x)+1/2*log(8) into log(x*sqrt(8)).",
    "created_at": "2009-11-07T21:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61341",
    "user": "@robert-marik"
}
```

I also think that it is better to keep the function logcontract separately from simplify_full() since sometimes the contraction of logarithms is not what user wants. Consider please also option which allows to set logconfcoef as described in [Maxima](http://maxima.sourceforge.net/docs/manual/en/maxima_14.html#Item_003a-logconcoeffp). This allows to contract expressions like log(x)+1/2*log(8) into log(x*sqrt(8)).



---

archive/issue_comments_061342.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  \n\nDo not do it please. The user knows if he/she wants to contract logarithms or not and then he/she can run the coresponding method. If you include this as an automatical simplification in simplify_full, consider the following\n\n* domain of log(1-x)+log(1+x) is different from domain of log(1-x^2)\n\n* you should add a function which expands logarithms\n\nThanks \nRobert",
    "created_at": "2009-11-07T21:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61342",
    "user": "@robert-marik"
}
```

Replying to [comment:2 kcrisman]:
> Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  

Do not do it please. The user knows if he/she wants to contract logarithms or not and then he/she can run the coresponding method. If you include this as an automatical simplification in simplify_full, consider the following

* domain of log(1-x)+log(1+x) is different from domain of log(1-x^2)

* you should add a function which expands logarithms

Thanks 
Robert



---

archive/issue_comments_061343.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-07T23:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61343",
    "user": "@robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061344.json:
```json
{
    "body": "Attached new patch, apply only this patch.\n\nOptions which controls if simplify expressions like 1/2*log(x) or not has been introduced.\n\nsimplify_log now does not use radcan, it calls only logcontract in Maxima session. However, there are many aliases for radcan:\nradical_simplify, simplify_radical, exp_simplify, simplify_exp",
    "created_at": "2009-11-07T23:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61344",
    "user": "@robert-marik"
}
```

Attached new patch, apply only this patch.

Options which controls if simplify expressions like 1/2*log(x) or not has been introduced.

simplify_log now does not use radcan, it calls only logcontract in Maxima session. However, there are many aliases for radcan:
radical_simplify, simplify_radical, exp_simplify, simplify_exp



---

archive/issue_comments_061345.json:
```json
{
    "body": "Attachment [trac-7344-logcontract-2.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7344-logcontract-2.patch) by @kcrisman created at 2009-11-08 01:58:15\n\nReplying to [comment:4 robert.marik]:\n> Replying to [comment:2 kcrisman]:\n> > Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  \n> \n> Do not do it please. The user knows if he/she wants to contract logarithms or not and then he/she can run the coresponding method. If you include this as an automatical simplification in simplify_full, consider the following\n> \n\nI disagree.  simplify_full is the sort of thing used by people who do NOT know if they want to contract - they want the simplest-looking form possible.  In fact, these people usually use just simplify() first and then email sage-support complaining it doesn't do things like this :)  \n\nAnyone who is looking for something specific can use the specific wrappers for the Maxima simplifiers; the general user who is not actually interested in symbolics or niceties like domains (which presumably the other simplifiers also disrespect, e.g. x**2/x is not x but presumably one of them does this and is part of simplify_full) needs a function which applies as much machinery as possible, and simplify_full is it.\n\nThat said, wrapping more of the expanding functions is a very good idea!  One could even have an \"expand_full\" function to complement the \"simplify_full\".  \n\n(Unfortunately, many users (including me) get tripped on on simplify versus expand linguistically, because in colloquial high school English they are often used interchangeably... sigh, but I'm just as guilty as anyone.)",
    "created_at": "2009-11-08T01:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61345",
    "user": "@kcrisman"
}
```

Attachment [trac-7344-logcontract-2.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7344-logcontract-2.patch) by @kcrisman created at 2009-11-08 01:58:15

Replying to [comment:4 robert.marik]:
> Replying to [comment:2 kcrisman]:
> > Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  
> 
> Do not do it please. The user knows if he/she wants to contract logarithms or not and then he/she can run the coresponding method. If you include this as an automatical simplification in simplify_full, consider the following
> 

I disagree.  simplify_full is the sort of thing used by people who do NOT know if they want to contract - they want the simplest-looking form possible.  In fact, these people usually use just simplify() first and then email sage-support complaining it doesn't do things like this :)  

Anyone who is looking for something specific can use the specific wrappers for the Maxima simplifiers; the general user who is not actually interested in symbolics or niceties like domains (which presumably the other simplifiers also disrespect, e.g. x**2/x is not x but presumably one of them does this and is part of simplify_full) needs a function which applies as much machinery as possible, and simplify_full is it.

That said, wrapping more of the expanding functions is a very good idea!  One could even have an "expand_full" function to complement the "simplify_full".  

(Unfortunately, many users (including me) get tripped on on simplify versus expand linguistically, because in colloquial high school English they are often used interchangeably... sigh, but I'm just as guilty as anyone.)



---

archive/issue_comments_061346.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-11-08T14:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61346",
    "user": "@robert-marik"
}
```

apply only this patch



---

archive/issue_comments_061347.json:
```json
{
    "body": "Attachment [trac-7344-logcontract-3.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7344-logcontract-3.patch) by @robert-marik created at 2009-11-08 14:14:43\n\nAdded contraction of logarithms to simplify_full() and some more options.",
    "created_at": "2009-11-08T14:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61347",
    "user": "@robert-marik"
}
```

Attachment [trac-7344-logcontract-3.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7344-logcontract-3.patch) by @robert-marik created at 2009-11-08 14:14:43

Added contraction of logarithms to simplify_full() and some more options.



---

archive/issue_comments_061348.json:
```json
{
    "body": "note that something does not work as expected due to recently fixed Maxima [bug](http://sourceforge.net/tracker/index.php?func=detail&aid=2835634&group_id=4933&atid=104933).\n\nAs a particular example (log(5)-log(2)).logcontract() does not work now, (log(x)-log(y)).logcontract() works as expected.",
    "created_at": "2009-11-08T14:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61348",
    "user": "@robert-marik"
}
```

note that something does not work as expected due to recently fixed Maxima [bug](http://sourceforge.net/tracker/index.php?func=detail&aid=2835634&group_id=4933&atid=104933).

As a particular example (log(5)-log(2)).logcontract() does not work now, (log(x)-log(y)).logcontract() works as expected.



---

archive/issue_comments_061349.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T14:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61349",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061350.json:
```json
{
    "body": "Here are a few comments, which you can incorporate if you agree with them.  Overall, though, a VERY well documented patch, which tells the user exactly what they can and cannot do with it, options, etc.  Good work!\n\n1. typo of \"gowerns\" instead of \"governs\" in line 5268\n\n2. Maybe the if coeff is not None:\u00a0 should be set off in a block? For better readability and logical flow.\n\n3. Perhaps \n\n```\nsage: (log(5)-log(2)).simplify_log()\n-log(2) + log(5)\n```\n\nshould be included as a doctest, with a comment that this is not simplified (though it's not mathematically wrong, so I am okay with this being as is).  This will also encourage us to upgrade Maxima :)\n\n4. There are some duplicated doctests.  Is this intentional (i.e., to show it won't simplify any more)?  Since \n\n```\nsage: x,y,t=var('x y t') \nsage: f = log(x)+2*log(y)+1/2*log(t) \nsage: f.simplify_log()\nlog(x*y^2) + 1/2*log(t)\nsage: f\n1/2*log(t) + log(x) + 2*log(y)\n```\n\nit must have some other rationale.  Anyway, that should be clarified, or the duplicates should be removed, as this is confusing.",
    "created_at": "2009-11-10T14:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61350",
    "user": "@kcrisman"
}
```

Here are a few comments, which you can incorporate if you agree with them.  Overall, though, a VERY well documented patch, which tells the user exactly what they can and cannot do with it, options, etc.  Good work!

1. typo of "gowerns" instead of "governs" in line 5268

2. Maybe the if coeff is not None:  should be set off in a block? For better readability and logical flow.

3. Perhaps 

```
sage: (log(5)-log(2)).simplify_log()
-log(2) + log(5)
```

should be included as a doctest, with a comment that this is not simplified (though it's not mathematically wrong, so I am okay with this being as is).  This will also encourage us to upgrade Maxima :)

4. There are some duplicated doctests.  Is this intentional (i.e., to show it won't simplify any more)?  Since 

```
sage: x,y,t=var('x y t') 
sage: f = log(x)+2*log(y)+1/2*log(t) 
sage: f.simplify_log()
log(x*y^2) + 1/2*log(t)
sage: f
1/2*log(t) + log(x) + 2*log(y)
```

it must have some other rationale.  Anyway, that should be clarified, or the duplicates should be removed, as this is confusing.



---

archive/issue_comments_061351.json:
```json
{
    "body": "Attachment [trac-7334-logcontract-4.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract-4.patch) by @robert-marik created at 2009-11-12 10:50:19\n\nApply only this patch.",
    "created_at": "2009-11-12T10:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61351",
    "user": "@robert-marik"
}
```

Attachment [trac-7334-logcontract-4.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract-4.patch) by @robert-marik created at 2009-11-12 10:50:19

Apply only this patch.



---

archive/issue_comments_061352.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-12T10:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61352",
    "user": "@robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061353.json:
```json
{
    "body": "Many thanks for reviewing and comments. New patch is there. It accepts your suggestions and adds more:\n\nIf we contract logarithms, we have to build the way back - I added expansion of logarithms.\n\nI also updated simplification of rational functions and added one option to simplify_trig.",
    "created_at": "2009-11-12T10:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61353",
    "user": "@robert-marik"
}
```

Many thanks for reviewing and comments. New patch is there. It accepts your suggestions and adds more:

If we contract logarithms, we have to build the way back - I added expansion of logarithms.

I also updated simplification of rational functions and added one option to simplify_trig.



---

archive/issue_comments_061354.json:
```json
{
    "body": "And there was also no way to go back after expanding trigonometric function. I added interface to Maxima's trigreduce to this patch.",
    "created_at": "2009-11-12T10:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61354",
    "user": "@robert-marik"
}
```

And there was also no way to go back after expanding trigonometric function. I added interface to Maxima's trigreduce to this patch.



---

archive/issue_comments_061355.json:
```json
{
    "body": "I really dislike the idea of adding a new function for each functionality of this kind. This makes it very hard for users to figure out the function name they need for a specific task.\n\nWe should be able to provide an interface to all these \"rewriting\" tasks through a few conceptually defined methods like rewrite(), expand() and combine()( or contract()?).\n\nFrancois Maltey had a proposal for a possible interface to all this. Maybe he can comment here, or we can discuss his proposal on sage-devel.",
    "created_at": "2009-11-12T11:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61355",
    "user": "@burcin"
}
```

I really dislike the idea of adding a new function for each functionality of this kind. This makes it very hard for users to figure out the function name they need for a specific task.

We should be able to provide an interface to all these "rewriting" tasks through a few conceptually defined methods like rewrite(), expand() and combine()( or contract()?).

Francois Maltey had a proposal for a possible interface to all this. Maybe he can comment here, or we can discuss his proposal on sage-devel.



---

archive/issue_comments_061356.json:
```json
{
    "body": "started discussion [on sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/3899a578da747009)",
    "created_at": "2009-11-12T13:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61356",
    "user": "@robert-marik"
}
```

started discussion [on sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/3899a578da747009)



---

archive/issue_comments_061357.json:
```json
{
    "body": "According to the discussion on sage-devel, let's wait (perhaps short time) and look for some cleaner solution.",
    "created_at": "2009-11-13T14:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61357",
    "user": "@robert-marik"
}
```

According to the discussion on sage-devel, let's wait (perhaps short time) and look for some cleaner solution.



---

archive/issue_comments_061358.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-13T14:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61358",
    "user": "@robert-marik"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061359.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-03T15:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61359",
    "user": "@burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061360.json:
```json
{
    "body": "3 months is more than enough time to wait. The patch looks good to me (apart from minor formatting problems like long lines). I want to give a positive review, but it seems I can't switch from needs_work to positive_review directly. I'll run doctests first, then come back here.",
    "created_at": "2010-02-03T15:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61360",
    "user": "@burcin"
}
```

3 months is more than enough time to wait. The patch looks good to me (apart from minor formatting problems like long lines). I want to give a positive review, but it seems I can't switch from needs_work to positive_review directly. I'll run doctests first, then come back here.



---

archive/issue_comments_061361.json:
```json
{
    "body": "On Sage-4.3.2.alpha1, I get these doctest failures:\n\n\n```\nsage -t  devel/sage-s/sage/symbolic/expression.pyx\n**********************************************************************\nFile \"/scratch/berocal/sage/i686/sage-4.3.rc0/devel/sage-s/sage/symbolic/expression.pyx\", line 5837:\n    sage: (x*log(9)).simplify_log('all')\nExpected:\n    log(9^x)\nGot:\n    x*log(9)\n**********************************************************************\nFile \"/scratch/berocal/sage/i686/sage-4.3.rc0/devel/sage-s/sage/symbolic/expression.pyx\", line 5849:\n    sage: (log(5)-log(2)).simplify_log()\nExpected:\n    -log(2) + log(5)\nGot:\n    log(5/2)\n**********************************************************************\n```\n\n\nI don't know about the first one, but the second one seems to be confirming a bug fix in Maxima. :)",
    "created_at": "2010-02-03T15:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61361",
    "user": "@burcin"
}
```

On Sage-4.3.2.alpha1, I get these doctest failures:


```
sage -t  devel/sage-s/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/berocal/sage/i686/sage-4.3.rc0/devel/sage-s/sage/symbolic/expression.pyx", line 5837:
    sage: (x*log(9)).simplify_log('all')
Expected:
    log(9^x)
Got:
    x*log(9)
**********************************************************************
File "/scratch/berocal/sage/i686/sage-4.3.rc0/devel/sage-s/sage/symbolic/expression.pyx", line 5849:
    sage: (log(5)-log(2)).simplify_log()
Expected:
    -log(2) + log(5)
Got:
    log(5/2)
**********************************************************************
```


I don't know about the first one, but the second one seems to be confirming a bug fix in Maxima. :)



---

archive/issue_comments_061362.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-03T15:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61362",
    "user": "@burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061363.json:
```json
{
    "body": "The first problem is outside  maxima, since I have\n\n```\nsage: maxima(\"logconcoeffp:'logconfun\")\nlogconfun\nsage: maxima(\"logconfun(m):= true\")\nlogconfun(m):=true\nsage: maxima(\"logcontract(x*log(9))\")\nlog(9^x)\n```\n\nI have to investigate the problem in details (perhaps tomorrow).\n\nYes, the second \"problem\" is a fixed bug from Maxima :)",
    "created_at": "2010-02-03T15:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61363",
    "user": "@robert-marik"
}
```

The first problem is outside  maxima, since I have

```
sage: maxima("logconcoeffp:'logconfun")
logconfun
sage: maxima("logconfun(m):= true")
logconfun(m):=true
sage: maxima("logcontract(x*log(9))")
log(9^x)
```

I have to investigate the problem in details (perhaps tomorrow).

Yes, the second "problem" is a fixed bug from Maxima :)



---

archive/issue_comments_061364.json:
```json
{
    "body": "Attachment [trac-7334-logcontract-5.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract-5.patch) by @robert-marik created at 2010-02-03 21:24:00\n\nNew patch (switch temporary logexpand to false when doing logcontract) is attched. Apply only this patch.\n\n\n```\n./sage -t devel/sage/sage/symbolic\n```\n\npassed. Running all tests now. If they pass, I'll mark it as 'needs review' (tomorrow morning).",
    "created_at": "2010-02-03T21:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61364",
    "user": "@robert-marik"
}
```

Attachment [trac-7334-logcontract-5.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract-5.patch) by @robert-marik created at 2010-02-03 21:24:00

New patch (switch temporary logexpand to false when doing logcontract) is attched. Apply only this patch.


```
./sage -t devel/sage/sage/symbolic
```

passed. Running all tests now. If they pass, I'll mark it as 'needs review' (tomorrow morning).



---

archive/issue_comments_061365.json:
```json
{
    "body": "Attachment [trac-7334-logcontract-5-bugfix.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract-5-bugfix.patch) by @robert-marik created at 2010-02-04 07:37:26\n\napply after trac-7334-logcontract-5.patch",
    "created_at": "2010-02-04T07:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61365",
    "user": "@robert-marik"
}
```

Attachment [trac-7334-logcontract-5-bugfix.patch](tarball://root/attachments/some-uuid/ticket7334/trac-7334-logcontract-5-bugfix.patch) by @robert-marik created at 2010-02-04 07:37:26

apply after trac-7334-logcontract-5.patch



---

archive/issue_comments_061366.json:
```json
{
    "body": "tests passed. apply patches trac-7334-logcontract-5.patch  and trac-7334-logcontract-5-bugfix.patch",
    "created_at": "2010-02-04T11:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61366",
    "user": "@robert-marik"
}
```

tests passed. apply patches trac-7334-logcontract-5.patch  and trac-7334-logcontract-5-bugfix.patch



---

archive/issue_comments_061367.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T12:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61367",
    "user": "@robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061368.json:
```json
{
    "body": "Apply after others",
    "created_at": "2010-02-04T16:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61368",
    "user": "@kcrisman"
}
```

Apply after others



---

archive/issue_comments_061369.json:
```json
{
    "body": "Attachment [trac_7334-logcontract-5-reviewer.patch](tarball://root/attachments/some-uuid/ticket7334/trac_7334-logcontract-5-reviewer.patch) by @kcrisman created at 2010-02-04 16:08:44\n\nReviewer patch adds some additional doctests, fixes typos, clarifies a few other things.  It also fixes a bug which may not have appeared on the author's platform, essentially the same one as in the 5-bugfix patch but for the log_expand function.  \n\nI don't really understand why the original code didn't work, because it should!  But for some reason the logexpand variable was sticking around, also messing up other doctests in expression.pyx, for me, so I made this change.  Only this change needs review now; all else is enthusiastic positive review!",
    "created_at": "2010-02-04T16:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61369",
    "user": "@kcrisman"
}
```

Attachment [trac_7334-logcontract-5-reviewer.patch](tarball://root/attachments/some-uuid/ticket7334/trac_7334-logcontract-5-reviewer.patch) by @kcrisman created at 2010-02-04 16:08:44

Reviewer patch adds some additional doctests, fixes typos, clarifies a few other things.  It also fixes a bug which may not have appeared on the author's platform, essentially the same one as in the 5-bugfix patch but for the log_expand function.  

I don't really understand why the original code didn't work, because it should!  But for some reason the logexpand variable was sticking around, also messing up other doctests in expression.pyx, for me, so I made this change.  Only this change needs review now; all else is enthusiastic positive review!



---

archive/issue_comments_061370.json:
```json
{
    "body": "An additional thought on this:\n\nAnd to be honest, we should reset logexpand anyway, because after using log_expand one might want to do something else with Maxima where one might want the default logexpand setting, and be surprised that logexpand had been changed by log_expand.",
    "created_at": "2010-02-04T16:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61370",
    "user": "@kcrisman"
}
```

An additional thought on this:

And to be honest, we should reset logexpand anyway, because after using log_expand one might want to do something else with Maxima where one might want the default logexpand setting, and be surprised that logexpand had been changed by log_expand.



---

archive/issue_comments_061371.json:
```json
{
    "body": "The reviwer patch seems to be O.K. for me. Thanks for fixing typos and adding docs. Running tests now.\n\nrestoring default value of logexpand was not necessary, since 'ev' environment has been used in my original patch and this has no influence to the value of logexpand\n\n```\nsage: maxima('logexpand')\ntrue\nsage: maxima('ev(log(x*y),logexpand:false)')\nlog(x*y)\nsage: maxima('logexpand')\ntrue\nsage: maxima('ev(log(x*y),logexpand:super)')\nlog(y)+log(x)\nsage: maxima('logexpand')\ntrue\n```\n\n\nbut the current method without 'ev' enviroment is also O.K. and perhaps better, since ev may lead sometimes to some other problems and should be avoided if possible (as I understand discussions related (for example)to substitution from maxima group).",
    "created_at": "2010-02-04T19:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61371",
    "user": "@robert-marik"
}
```

The reviwer patch seems to be O.K. for me. Thanks for fixing typos and adding docs. Running tests now.

restoring default value of logexpand was not necessary, since 'ev' environment has been used in my original patch and this has no influence to the value of logexpand

```
sage: maxima('logexpand')
true
sage: maxima('ev(log(x*y),logexpand:false)')
log(x*y)
sage: maxima('logexpand')
true
sage: maxima('ev(log(x*y),logexpand:super)')
log(y)+log(x)
sage: maxima('logexpand')
true
```


but the current method without 'ev' enviroment is also O.K. and perhaps better, since ev may lead sometimes to some other problems and should be avoided if possible (as I understand discussions related (for example)to substitution from maxima group).



---

archive/issue_comments_061372.json:
```json
{
    "body": "> restoring default value of logexpand was not necessary, since 'ev' environment has been used in my original patch and this has no influence to the value of logexpand\n\nIt shouldn't have, but for some reason it did in my installation - specifically in some tests in solve and friends which had logs in their answers that mysteriously began simplifying!  Anyway, glad you think this solution is okay.",
    "created_at": "2010-02-04T20:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61372",
    "user": "@kcrisman"
}
```

> restoring default value of logexpand was not necessary, since 'ev' environment has been used in my original patch and this has no influence to the value of logexpand

It shouldn't have, but for some reason it did in my installation - specifically in some tests in solve and friends which had logs in their answers that mysteriously began simplifying!  Anyway, glad you think this solution is okay.



---

archive/issue_comments_061373.json:
```json
{
    "body": "all tests passed for me after  trac-7334-logcontract-5.patch , trac-7334-logcontract-5-bugfix.patch, trac_7334-logcontract-5-reviewer.patch",
    "created_at": "2010-02-04T21:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61373",
    "user": "@robert-marik"
}
```

all tests passed for me after  trac-7334-logcontract-5.patch , trac-7334-logcontract-5-bugfix.patch, trac_7334-logcontract-5-reviewer.patch



---

archive/issue_comments_061374.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T20:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61374",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061375.json:
```json
{
    "body": "Replying to [comment:25 robert.marik]:\n> all tests passed for me after  trac-7334-logcontract-5.patch , trac-7334-logcontract-5-bugfix.patch, trac_7334-logcontract-5-reviewer.patch \n\nIt sounds like this means positive review for the last reviewer change.  Great!",
    "created_at": "2010-02-05T20:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61375",
    "user": "@kcrisman"
}
```

Replying to [comment:25 robert.marik]:
> all tests passed for me after  trac-7334-logcontract-5.patch , trac-7334-logcontract-5-bugfix.patch, trac_7334-logcontract-5-reviewer.patch 

It sounds like this means positive review for the last reviewer change.  Great!



---

archive/issue_comments_061376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7334#issuecomment-61376",
    "user": "@qed777"
}
```

Resolution: fixed
