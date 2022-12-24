# Issue 6882: bug in conversion of "i" from Maxima to Sage

archive/issues_006882.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robert-marik\n\n\n```\n-----------\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string\nsage: symbolic_expression_from_maxima_string('%i')\nI\nsage: symbolic_expression_from_maxima_string('i')\nI\n-----------\n\nSo as you see, we are converting both '%i' and 'i' to  imaginary 'I' !!!!\n```\n\n\nSee the sage-devel thread about this on Sept 3 for some discussion and motivation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6882\n\n",
    "created_at": "2009-09-03T22:58:43Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "bug in conversion of \"i\" from Maxima to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6882",
    "user": "@williamstein"
}
```
Assignee: @burcin

CC:  @robert-marik


```
-----------
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('%i')
I
sage: symbolic_expression_from_maxima_string('i')
I
-----------

So as you see, we are converting both '%i' and 'i' to  imaginary 'I' !!!!
```


See the sage-devel thread about this on Sept 3 for some discussion and motivation.

Issue created by migration from https://trac.sagemath.org/ticket/6882





---

archive/issue_comments_056834.json:
```json
{
    "body": "Here is the relevant [discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/93713a7c32100625/31b2cd361def53b0?show_docid=31b2cd361def53b0#).",
    "created_at": "2009-10-23T23:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56834",
    "user": "@kcrisman"
}
```

Here is the relevant [discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/93713a7c32100625/31b2cd361def53b0?show_docid=31b2cd361def53b0#).



---

archive/issue_comments_056835.json:
```json
{
    "body": "This will also happen with %e and e, and any other similar pairs, so a fix should take care of all of them.",
    "created_at": "2009-10-24T00:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56835",
    "user": "@kcrisman"
}
```

This will also happen with %e and e, and any other similar pairs, so a fix should take care of all of them.



---

archive/issue_comments_056836.json:
```json
{
    "body": "As another consequence, solving of ode y'=c*x is not correct, the free variable is messed up with a parameter, see [sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/e04cbc547095f2ac) - thanks for  \t \t\nYuri Karadzhov\n\n```\n[marik@um-bc107 /opt/sage-4.3.4]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string\nsage: symbolic_expression_from_maxima_string('%c')\nc\nsage: c=var('c'); y=function('y',x); eq=diff(y,x)==c*x; eq\nD[0](y)(x) == c*x\nsage: desolve(eq,y,ivar=x)\n1/2*c*x^2 + c\n```\n\nthe answer should be something like 1/2*c*x^2 + c1",
    "created_at": "2010-03-23T21:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56836",
    "user": "@robert-marik"
}
```

As another consequence, solving of ode y'=c*x is not correct, the free variable is messed up with a parameter, see [sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/e04cbc547095f2ac) - thanks for  	 	
Yuri Karadzhov

```
[marik@um-bc107 /opt/sage-4.3.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('%c')
c
sage: c=var('c'); y=function('y',x); eq=diff(y,x)==c*x; eq
D[0](y)(x) == c*x
sage: desolve(eq,y,ivar=x)
1/2*c*x^2 + c
```

the answer should be something like 1/2*c*x^2 + c1



---

archive/issue_comments_056837.json:
```json
{
    "body": "See #8734 for what I think is a \"needs work\" solution.",
    "created_at": "2010-05-03T17:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56837",
    "user": "@jasongrout"
}
```

See #8734 for what I think is a "needs work" solution.



---

archive/issue_comments_056838.json:
```json
{
    "body": "Actually, I guess the patch at #8734 will *help* with the solution, but may not totally solve the problem.",
    "created_at": "2010-05-03T17:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56838",
    "user": "@jasongrout"
}
```

Actually, I guess the patch at #8734 will *help* with the solution, but may not totally solve the problem.



---

archive/issue_comments_056839.json:
```json
{
    "body": "This should fix also #9421.",
    "created_at": "2010-07-04T15:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56839",
    "user": "@robert-marik"
}
```

This should fix also #9421.



---

archive/issue_comments_056840.json:
```json
{
    "body": "Also, in a situation where we *don't* have the duplication of constants, we get\n\n```\nsage: c\nTraceback (click to the left of this block for traceback)\n...\nNameError: name 'c' is not defined\n```\n\nwhich isn't good either, though apparently that part of the expression still has type SymbolicExpression.",
    "created_at": "2012-07-26T15:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56840",
    "user": "@kcrisman"
}
```

Also, in a situation where we *don't* have the duplication of constants, we get

```
sage: c
Traceback (click to the left of this block for traceback)
...
NameError: name 'c' is not defined
```

which isn't good either, though apparently that part of the expression still has type SymbolicExpression.



---

archive/issue_comments_056841.json:
```json
{
    "body": "Set to critical due to dependent tickets.",
    "created_at": "2014-02-18T07:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56841",
    "user": "@rwst"
}
```

Set to critical due to dependent tickets.



---

archive/issue_comments_056842.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2014-02-18T07:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56842",
    "user": "@rwst"
}
```

Changing priority from major to critical.



---

archive/issue_comments_056843.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Actually, I guess the patch at #8734 will *help* with the solution, but may not totally solve the problem.\n\nIndeed, because the patch at #8734 (needing review) only is about vars, and it will only help with the problem in comment:3 if the then marked sage vars are renamed to some other specific string before output in desolve...().",
    "created_at": "2014-03-24T17:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56843",
    "user": "@rwst"
}
```

Replying to [comment:5 jason]:
> Actually, I guess the patch at #8734 will *help* with the solution, but may not totally solve the problem.

Indeed, because the patch at #8734 (needing review) only is about vars, and it will only help with the problem in comment:3 if the then marked sage vars are renamed to some other specific string before output in desolve...().



---

archive/issue_comments_056844.json:
```json
{
    "body": "Replying to [comment:3 robert.marik]:\n> As another consequence, solving of ode y'=c*x is not correct\n> ...\n> the answer should be something like 1/2*c*x^2 + c1\n\nThis one is resolved in #16007. So it seems only variables are left (#8734).",
    "created_at": "2014-03-26T16:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56844",
    "user": "@rwst"
}
```

Replying to [comment:3 robert.marik]:
> As another consequence, solving of ode y'=c*x is not correct
> ...
> the answer should be something like 1/2*c*x^2 + c1

This one is resolved in #16007. So it seems only variables are left (#8734).



---

archive/issue_comments_056845.json:
```json
{
    "body": "Yes, variables are all that's left, but the other way around!   (Don't forget the initial examples of this ticket.) We need to disambiguate Maxima variables like `i` and `e` from the things that become those in Sage - `%i` and `%e`.   I suppose one could take the Maxima variables `i` and `I` and turn them into `_i` and `_I`, and likewise for e, as at #16007, but I'm not sure if that's ideal or not.  Thoughts?",
    "created_at": "2014-03-27T16:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56845",
    "user": "@kcrisman"
}
```

Yes, variables are all that's left, but the other way around!   (Don't forget the initial examples of this ticket.) We need to disambiguate Maxima variables like `i` and `e` from the things that become those in Sage - `%i` and `%e`.   I suppose one could take the Maxima variables `i` and `I` and turn them into `_i` and `_I`, and likewise for e, as at #16007, but I'm not sure if that's ideal or not.  Thoughts?



---

archive/issue_comments_056846.json:
```json
{
    "body": "Priority changed as the more important fixes were outsourced to other tickets.",
    "created_at": "2014-06-06T13:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56846",
    "user": "@rwst"
}
```

Priority changed as the more important fixes were outsourced to other tickets.



---

archive/issue_comments_056847.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2014-06-06T13:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56847",
    "user": "@rwst"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_056848.json:
```json
{
    "body": "> Priority changed as the more important fixes were outsourced to other tickets.\nHmm, though the BDFL originally reported this with the comment\n\n```\nI think my email must have not been clear.  I think it's an instance   \nof a *HUGE BUG* in Sage.  No more, no less.    \n```\n",
    "created_at": "2014-06-10T00:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56848",
    "user": "@kcrisman"
}
```

> Priority changed as the more important fixes were outsourced to other tickets.
Hmm, though the BDFL originally reported this with the comment

```
I think my email must have not been clear.  I think it's an instance   
of a *HUGE BUG* in Sage.  No more, no less.    
```




---

archive/issue_comments_056849.json:
```json
{
    "body": "Maybe we can change the Maxima `i` and `e` to Sage `_i` and `_e`, leaving `%i` and `%e` to become `i` and `e` as currently, and then taking advantage of the last changes at #16007 for typesetting more-or-less properly.",
    "created_at": "2014-06-24T15:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56849",
    "user": "@kcrisman"
}
```

Maybe we can change the Maxima `i` and `e` to Sage `_i` and `_e`, leaving `%i` and `%e` to become `i` and `e` as currently, and then taking advantage of the last changes at #16007 for typesetting more-or-less properly.



---

archive/issue_comments_056850.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2014-06-24T15:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56850",
    "user": "@kcrisman"
}
```

Changing priority from minor to major.



---

archive/issue_comments_056851.json:
```json
{
    "body": "The original bug report on sage-devel had:\n\n```\nsage: var('i')\ni\nsage: i\ni\nsage: a = i^2\nsage: a.simplify_full()\n-1\n```\n\nHowever, with develop I get `i^2`. Is this ticket still valid?",
    "created_at": "2014-06-26T09:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56851",
    "user": "@rwst"
}
```

The original bug report on sage-devel had:

```
sage: var('i')
i
sage: i
i
sage: a = i^2
sage: a.simplify_full()
-1
```

However, with develop I get `i^2`. Is this ticket still valid?



---

archive/issue_comments_056852.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2014-06-26T09:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56852",
    "user": "@rwst"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_056853.json:
```json
{
    "body": "And indeed,\n\n```\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string\nsage: symbolic_expression_from_maxima_string('i')\ni\nsage: symbolic_expression_from_maxima_string('%i')\nI\n```\n\nAnd the original solving case William reported is also fixed.  \n\nHuh.  Is this before or after #8734? (I would imagine that one would have an impact.)  Anyway, I would say we add some doctests (for both the `sefms` and `i^2` cases) and call it a day, regardless of which ticket it depends on.  Good work, since ideally one wouldn't be creating a Maxima `i` and then trying to bring it to Sage.",
    "created_at": "2014-06-26T12:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56853",
    "user": "@kcrisman"
}
```

And indeed,

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('i')
i
sage: symbolic_expression_from_maxima_string('%i')
I
```

And the original solving case William reported is also fixed.  

Huh.  Is this before or after #8734? (I would imagine that one would have an impact.)  Anyway, I would say we add some doctests (for both the `sefms` and `i^2` cases) and call it a day, regardless of which ticket it depends on.  Good work, since ideally one wouldn't be creating a Maxima `i` and then trying to bring it to Sage.



---

archive/issue_comments_056854.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2014-06-26T16:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56854",
    "user": "@rwst"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_056855.json:
```json
{
    "body": "With develop:\n\n```\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string\nsage: symbolic_expression_from_maxima_string('t')\nt\nsage: symbolic_expression_from_maxima_string('i')\nI\nsage: var('i')\ni\nsage: symbolic_expression_from_maxima_string('i')\ni\n```\n\nSo that example is a different animal than the ticket case.",
    "created_at": "2014-06-26T16:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56855",
    "user": "@rwst"
}
```

With develop:

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('t')
t
sage: symbolic_expression_from_maxima_string('i')
I
sage: var('i')
i
sage: symbolic_expression_from_maxima_string('i')
i
```

So that example is a different animal than the ticket case.



---

archive/issue_comments_056856.json:
```json
{
    "body": "Okay, I see.  But the thing is that, in principle, we should never get `i` inside Maxima without asking for it via Sage having a variable `i`; we should only get `%i` the imaginary in Maxima, which translates differently (and correctly) now.  Does that make sense, or do you think this is still worth fixing?  (We should check what happens with `e` as well, maybe via `ln(e)`.)",
    "created_at": "2014-06-26T19:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56856",
    "user": "@kcrisman"
}
```

Okay, I see.  But the thing is that, in principle, we should never get `i` inside Maxima without asking for it via Sage having a variable `i`; we should only get `%i` the imaginary in Maxima, which translates differently (and correctly) now.  Does that make sense, or do you think this is still worth fixing?  (We should check what happens with `e` as well, maybe via `ln(e)`.)



---

archive/issue_comments_056857.json:
```json
{
    "body": "With #8734 `I` can result from a Sage `I` variable, from Maxima `%i`, or from Maxima `i` which is only creatable from Sage via the Maxima interface. But not from any trick involving the Sage variable `i` due to the protection via `_SAGE_VAR_`. The `i` case is why Jason said #8734 will help, but not totally solve the problem.\n\nI don't know why the `i^2` example failed at all, and when exactly it stopped failing. Maybe it didn't fail; certainly nobody posted a confirmation message. And certainly we all confirmed the sefms snippet because that's what the ticket presented.",
    "created_at": "2014-06-26T20:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56857",
    "user": "@rwst"
}
```

With #8734 `I` can result from a Sage `I` variable, from Maxima `%i`, or from Maxima `i` which is only creatable from Sage via the Maxima interface. But not from any trick involving the Sage variable `i` due to the protection via `_SAGE_VAR_`. The `i` case is why Jason said #8734 will help, but not totally solve the problem.

I don't know why the `i^2` example failed at all, and when exactly it stopped failing. Maybe it didn't fail; certainly nobody posted a confirmation message. And certainly we all confirmed the sefms snippet because that's what the ticket presented.



---

archive/issue_comments_056858.json:
```json
{
    "body": "Yeah, even in Sage 4.4.4 (which I have lying around due to some custom fixes I use for research I'm too lazy to update) \n\n```\nsage: var('i')\ni\nsage: i\ni\nsage: a = i^2\nsage: a\ni^2\nsage: a.simplify_full()\ni^2\n```\n\nYour thoughts on a resolution?  The thing that was a bug is not there any more, and the only potential bug is from 'user error', in some sense.",
    "created_at": "2014-06-26T21:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56858",
    "user": "@kcrisman"
}
```

Yeah, even in Sage 4.4.4 (which I have lying around due to some custom fixes I use for research I'm too lazy to update) 

```
sage: var('i')
i
sage: i
i
sage: a = i^2
sage: a
i^2
sage: a.simplify_full()
i^2
```

Your thoughts on a resolution?  The thing that was a bug is not there any more, and the only potential bug is from 'user error', in some sense.



---

archive/issue_comments_056859.json:
```json
{
    "body": "At the moment we also get behaviour like\n\n```\nsage: symbolic_expression_from_maxima_string('%inf')\nInf\n```\n\nso I think the ticket should implement `multi_word_replace()` in `sage.misc.multireplace` and use that on a symtable with additional entries `'e':'_e', 'i':'_i', 'I':'_I'`.",
    "created_at": "2014-06-27T09:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56859",
    "user": "@rwst"
}
```

At the moment we also get behaviour like

```
sage: symbolic_expression_from_maxima_string('%inf')
Inf
```

so I think the ticket should implement `multi_word_replace()` in `sage.misc.multireplace` and use that on a symtable with additional entries `'e':'_e', 'i':'_i', 'I':'_I'`.



---

archive/issue_comments_056860.json:
```json
{
    "body": "Changing assignee from @burcin to @rwst.",
    "created_at": "2014-06-27T09:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56860",
    "user": "@rwst"
}
```

Changing assignee from @burcin to @rwst.



---

archive/issue_comments_056861.json:
```json
{
    "body": "> At the moment we also get behaviour like\n> {{{\n> sage: symbolic_expression_from_maxima_string('%inf')\n> Inf\n> }}}\nIs `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.\n> so I think the ticket should implement `multi_word_replace()` in `sage.misc.multireplace` and use that on a symtable with additional entries `'e':'_e', 'i':'_i', 'I':'_I'`.\nI guess one could do so... I'm just trying to imagine cases in which this would be necessary due only to Sage usage.  If someone uses Maxima to create variables it's quite different.",
    "created_at": "2014-06-27T12:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56861",
    "user": "@kcrisman"
}
```

> At the moment we also get behaviour like
> {{{
> sage: symbolic_expression_from_maxima_string('%inf')
> Inf
> }}}
Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.
> so I think the ticket should implement `multi_word_replace()` in `sage.misc.multireplace` and use that on a symtable with additional entries `'e':'_e', 'i':'_i', 'I':'_I'`.
I guess one could do so... I'm just trying to imagine cases in which this would be necessary due only to Sage usage.  If someone uses Maxima to create variables it's quite different.



---

archive/issue_comments_056862.json:
```json
{
    "body": "Replying to [comment:27 kcrisman]:\n> Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.\nNo but we do not want to be surprised when some new Maxima variable starting `%i` is introduced. At the moment it's really just a string replace from `%i` to `I`, without sense of word boundaries.",
    "created_at": "2014-06-27T14:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56862",
    "user": "@rwst"
}
```

Replying to [comment:27 kcrisman]:
> Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.
No but we do not want to be surprised when some new Maxima variable starting `%i` is introduced. At the moment it's really just a string replace from `%i` to `I`, without sense of word boundaries.



---

archive/issue_comments_056863.json:
```json
{
    "body": "> > Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.\n> No but we do not want to be surprised when some new Maxima variable starting `%i` is introduced. At the moment it's really just a string replace from `%i` to `I`, without sense of word boundaries.\nAha!  I didn't catch that was the reason.  I don't think Maxima introduces many new constants with `%` but I see your point.",
    "created_at": "2014-06-27T14:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56863",
    "user": "@kcrisman"
}
```

> > Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.
> No but we do not want to be surprised when some new Maxima variable starting `%i` is introduced. At the moment it's really just a string replace from `%i` to `I`, without sense of word boundaries.
Aha!  I didn't catch that was the reason.  I don't think Maxima introduces many new constants with `%` but I see your point.



---

archive/issue_comments_056864.json:
```json
{
    "body": "I also found an error in the definition for maxima variable, because it didn't allow variable names without '%' or the '%' not at the beginning. Now the mentioned rules can be expressed as simple entries in symtable.\n----\nNew commits:",
    "created_at": "2014-06-28T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56864",
    "user": "@rwst"
}
```

I also found an error in the definition for maxima variable, because it didn't allow variable names without '%' or the '%' not at the beginning. Now the mentioned rules can be expressed as simple entries in symtable.
----
New commits:



---

archive/issue_comments_056865.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-28T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56865",
    "user": "@rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056866.json:
```json
{
    "body": "> I also found an error in the definition for maxima variable, because it didn't allow variable names without '%' or the '%' not at the beginning. Now the mentioned rules can be expressed as simple entries in symtable.\nYou'll note that `maxima_var` was never currently used in the codebase, so it wasn't a problem, more of just old code - [here](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/calculus/calculus.py#n1792) is where the `%` were all replaced.  If you wanted I guess you could just replace that with `_` and it would be much more efficient than doing this whole loop every time, or so it seems to me.  How does this do with `timeit` for long expressions one gets in 'real life'?  (See sage/symbolic/random_tests.py.)  Also note that usually we end up having to special-case things with `%` anyway - e.g., `%ilt` (inverse Laplace transform) gets handled somewhere else, I'd have to look up where.",
    "created_at": "2014-06-30T14:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56866",
    "user": "@kcrisman"
}
```

> I also found an error in the definition for maxima variable, because it didn't allow variable names without '%' or the '%' not at the beginning. Now the mentioned rules can be expressed as simple entries in symtable.
You'll note that `maxima_var` was never currently used in the codebase, so it wasn't a problem, more of just old code - [here](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/calculus/calculus.py#n1792) is where the `%` were all replaced.  If you wanted I guess you could just replace that with `_` and it would be much more efficient than doing this whole loop every time, or so it seems to me.  How does this do with `timeit` for long expressions one gets in 'real life'?  (See sage/symbolic/random_tests.py.)  Also note that usually we end up having to special-case things with `%` anyway - e.g., `%ilt` (inverse Laplace transform) gets handled somewhere else, I'd have to look up where.



---

archive/issue_comments_056867.json:
```json
{
    "body": "Replying to [comment:34 kcrisman]:\n> How does this do with `timeit` for long expressions one gets in 'real life'?  (See sage/symbolic/random_tests.py.)\nIt's within the measurement error:\n\n```\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms\nsage: var('v1,v2,v3')\n(v1, v2, v3)\nsage: ex=-1/3*(pi + 1)*(3*(euler_gamma - e)*(pi - 3*v1 - v1/arcsech(1) + e^(-1)/pi) - 6*v3^2*arcsinh(-v1 + e)/v2 - v2 - 3*log_gamma(v1*v3)/v2 - 3*e^(-254) + 3)*(-catalan/v3)^(twinprime*pi - 1/2*v1 - 1/2*v2)*inverse_jacobi_cs(1, v3)/jacobi_sc(1/arccos(-1/(v1*csc(v3))), v3/v1 + e) - 1/4*(2*v3^2*(e + 1) + ((e*log_integral(arcsech(exp_integral_e1(v2^mertens - 1) - 4)) + 15*v1 + jacobi_dn(v2, pi))*v1*e^(-1) + golden_ratio*pi^v1*(1/v3^12 + jacobi_ds(-10, csc(v3^2)))^(v2 - 1/2/v2)*sinh(v2*e)/((v1 + v2 + v3 + 1)*v2))/(v1^2*inverse_jacobi_nc(v1, -e)) - 2*bessel_Y(v3, v2))/v2 + v3/inverse_jacobi_sc(1, v2) - (v1 + 1)/((v2 + v3)*(2*(v1 + e)*(v3 - 1)/(pi + v1) + (-v3*sech(v1*v3)/v2)^(-e/v1))) + inverse_jacobi_cn(pi + v1*v3, pi - v3) + jacobi_sn(e, arctanh(-(-log_integral(2) + log_integral(jacobi_ds(-1, v3)))^v2*e)^(1/7*(18*v2 - v3)*(14*v2 + e)/(v3*arctan(1/v2)*kronecker_delta(v1, v3))))\nsage: timeit('sefms(str(ex))')\n5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)\n5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)\n```\n\nObviously the whole routine takes so long that the loop doesn't signify. That may be worth an optimization ticket alone.\n> Also note that usually we end up having to special-case things with `%` anyway - e.g., `%ilt` (inverse Laplace transform) gets handled somewhere else, I'd have to look up where.\nJust put it in `symtable`, give it a special value, and ask for that value within the new loop. Having it all in the loop is more efficient than find every time.",
    "created_at": "2014-06-30T15:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56867",
    "user": "@rwst"
}
```

Replying to [comment:34 kcrisman]:
> How does this do with `timeit` for long expressions one gets in 'real life'?  (See sage/symbolic/random_tests.py.)
It's within the measurement error:

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
sage: var('v1,v2,v3')
(v1, v2, v3)
sage: ex=-1/3*(pi + 1)*(3*(euler_gamma - e)*(pi - 3*v1 - v1/arcsech(1) + e^(-1)/pi) - 6*v3^2*arcsinh(-v1 + e)/v2 - v2 - 3*log_gamma(v1*v3)/v2 - 3*e^(-254) + 3)*(-catalan/v3)^(twinprime*pi - 1/2*v1 - 1/2*v2)*inverse_jacobi_cs(1, v3)/jacobi_sc(1/arccos(-1/(v1*csc(v3))), v3/v1 + e) - 1/4*(2*v3^2*(e + 1) + ((e*log_integral(arcsech(exp_integral_e1(v2^mertens - 1) - 4)) + 15*v1 + jacobi_dn(v2, pi))*v1*e^(-1) + golden_ratio*pi^v1*(1/v3^12 + jacobi_ds(-10, csc(v3^2)))^(v2 - 1/2/v2)*sinh(v2*e)/((v1 + v2 + v3 + 1)*v2))/(v1^2*inverse_jacobi_nc(v1, -e)) - 2*bessel_Y(v3, v2))/v2 + v3/inverse_jacobi_sc(1, v2) - (v1 + 1)/((v2 + v3)*(2*(v1 + e)*(v3 - 1)/(pi + v1) + (-v3*sech(v1*v3)/v2)^(-e/v1))) + inverse_jacobi_cn(pi + v1*v3, pi - v3) + jacobi_sn(e, arctanh(-(-log_integral(2) + log_integral(jacobi_ds(-1, v3)))^v2*e)^(1/7*(18*v2 - v3)*(14*v2 + e)/(v3*arctan(1/v2)*kronecker_delta(v1, v3))))
sage: timeit('sefms(str(ex))')
5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
```

Obviously the whole routine takes so long that the loop doesn't signify. That may be worth an optimization ticket alone.
> Also note that usually we end up having to special-case things with `%` anyway - e.g., `%ilt` (inverse Laplace transform) gets handled somewhere else, I'd have to look up where.
Just put it in `symtable`, give it a special value, and ask for that value within the new loop. Having it all in the loop is more efficient than find every time.



---

archive/issue_comments_056868.json:
```json
{
    "body": "Replying to [comment:35 rws]:\n> {{{\n> sage: timeit('sefms(str(ex))')\n> 5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)\n> 5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)\n> }}}\nIt calls 120 times the function `MaximaLib._eval_line()` which takes 17ms in average = 2 seconds. 17 ms is an eternity.",
    "created_at": "2014-06-30T16:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56868",
    "user": "@rwst"
}
```

Replying to [comment:35 rws]:
> {{{
> sage: timeit('sefms(str(ex))')
> 5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
> 5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
> }}}
It calls 120 times the function `MaximaLib._eval_line()` which takes 17ms in average = 2 seconds. 17 ms is an eternity.



---

archive/issue_comments_056869.json:
```json
{
    "body": "> > {{{\n> > sage: timeit('sefms(str(ex))')\n> > 5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)\n> > 5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)\n> > }}}\nWow, those timings are indeed an eternity, though presumably not for shorter expressions.  I'll put this ticket in my \"finally finish reviewing\" queue, then, for sure.",
    "created_at": "2014-06-30T16:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56869",
    "user": "@kcrisman"
}
```

> > {{{
> > sage: timeit('sefms(str(ex))')
> > 5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
> > 5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
> > }}}
Wow, those timings are indeed an eternity, though presumably not for shorter expressions.  I'll put this ticket in my "finally finish reviewing" queue, then, for sure.



---

archive/issue_comments_056870.json:
```json
{
    "body": "Well, it's an improvement, though still not perfect:\n\n```\n# Before\nsage: sefms('%inf')\nInf\nsage: sefms('%minf')\n-Infinity\n# After\nsage: sefms('%inf')\n+Infinity\nsage: sefms('%minf')\n-Infinity\n```\n\nNeither of these are infinity in Maxima, of course.  And indeed here is what the [Maxima manual](http://maxima.sourceforge.net/docs/manual/en/maxima_6.html#SEC32) says about identifiers:\n\n```\n(%i1) %an_ordinary_identifier42;\n(%o1)               %an_ordinary_identifier42\n```\n\n\"A numeral may be the first character of an identifier if it is preceded by a backslash. \"  But I don't know that we need to translate all identifiers in Maxima to Sage here... I guess I'm torn about that.  \n\n```\nsage: timeit('sefms(str(ex))')\n5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)\n5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)\n```\n\nOf course, thinking about it, that string is a Sage string, not a Maxima string, so `%time R = random_expr(50,nvars=2); sefms(repr(R._maxima_()))` is probably more accurate, but that is also wildly variant on the expression.\n\nOkay, as far as I can tell this will not break anything (let's really hope!) and fixes the actual problem without slowing down what is already a very slow process (even for `random_expr(5,nvars=2)` it's 2-3 milliseconds either way).  Step in right direction, and again most people should not be affected in the slightest.  If passes tests, let's get it in.",
    "created_at": "2014-07-02T02:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56870",
    "user": "@kcrisman"
}
```

Well, it's an improvement, though still not perfect:

```
# Before
sage: sefms('%inf')
Inf
sage: sefms('%minf')
-Infinity
# After
sage: sefms('%inf')
+Infinity
sage: sefms('%minf')
-Infinity
```

Neither of these are infinity in Maxima, of course.  And indeed here is what the [Maxima manual](http://maxima.sourceforge.net/docs/manual/en/maxima_6.html#SEC32) says about identifiers:

```
(%i1) %an_ordinary_identifier42;
(%o1)               %an_ordinary_identifier42
```

"A numeral may be the first character of an identifier if it is preceded by a backslash. "  But I don't know that we need to translate all identifiers in Maxima to Sage here... I guess I'm torn about that.  

```
sage: timeit('sefms(str(ex))')
5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
```

Of course, thinking about it, that string is a Sage string, not a Maxima string, so `%time R = random_expr(50,nvars=2); sefms(repr(R._maxima_()))` is probably more accurate, but that is also wildly variant on the expression.

Okay, as far as I can tell this will not break anything (let's really hope!) and fixes the actual problem without slowing down what is already a very slow process (even for `random_expr(5,nvars=2)` it's 2-3 milliseconds either way).  Step in right direction, and again most people should not be affected in the slightest.  If passes tests, let's get it in.



---

archive/issue_comments_056871.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-02T03:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56871",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056872.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-07-03T12:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6882#issuecomment-56872",
    "user": "@vbraun"
}
```

Resolution: fixed
