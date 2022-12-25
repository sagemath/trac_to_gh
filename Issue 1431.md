# Issue 1431: basic plotting: add support for setting the location and labels of all tick marks on the x and y axes

archive/issues_001431.json:
```json
{
    "body": "Assignee: @williamstein\n\nAmazingly some very basic functionality for plotting hasn't yet been implemented!  In particular, there is nothing yet for setting the location and labels of all tick marks on the x and y axes.  This need to be implemented.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1431\n\n",
    "created_at": "2007-12-09T02:49:00Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "basic plotting: add support for setting the location and labels of all tick marks on the x and y axes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1431",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Amazingly some very basic functionality for plotting hasn't yet been implemented!  In particular, there is nothing yet for setting the location and labels of all tick marks on the x and y axes.  This need to be implemented.

Issue created by migration from https://trac.sagemath.org/ticket/1431





---

archive/issue_comments_009193.json:
```json
{
    "body": "Changing component from algebraic geometry to graphics.",
    "created_at": "2007-12-09T02:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9193",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to graphics.



---

archive/issue_comments_009194.json:
```json
{
    "body": "This should be available now with #5448, but this ticket would now be to expose that functionality from matplotlib.",
    "created_at": "2009-09-15T17:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9194",
    "user": "https://github.com/kcrisman"
}
```

This should be available now with #5448, but this ticket would now be to expose that functionality from matplotlib.



---

archive/issue_comments_009195.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-11-12T00:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9195",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_009196.json:
```json
{
    "body": "Attachment [formatter.patch](tarball://root/attachments/some-uuid/ticket1431/formatter.patch) by @jasongrout created at 2009-11-12 00:17:34\n\nStill needs doctest examples.\n\nExample:\n\n\n```\n\ndef multiple_of_pi(n,pos):\n    m = n*1.0/float(pi)\n    c=[i for i in convergents(m) if i.denominator()<12]\n    q=c[-1]\n    if q.denominator()==1:\n        if q.numerator()==1:\n            return r'$\\pi$'\n        elif q.numerator()==-1:\n            return r'$-\\pi$'            \n        else:\n            return r'$%s\\pi$'%q\n    else:\n        if q.numerator()==1:\n            return r'$\\frac{\\pi}{%s}$'%q.denominator()\n        elif q.numerator()==-1:\n            return r'$\\frac{-\\pi}{%s}$'%q.denominator()\n        else:\n            return r'$\\frac{%s\\pi}{%s}$'%(q.numerator(),q.denominator())\n\nfrom matplotlib.ticker import MultipleLocator, FuncFormatter\nplot(sin(x), (x, -4, 4), tick_locator=MultipleLocator(float(pi/3)), tick_formatter=FuncFormatter(multiple_of_pi))\n\n```\n",
    "created_at": "2009-11-12T00:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9196",
    "user": "https://github.com/jasongrout"
}
```

Attachment [formatter.patch](tarball://root/attachments/some-uuid/ticket1431/formatter.patch) by @jasongrout created at 2009-11-12 00:17:34

Still needs doctest examples.

Example:


```

def multiple_of_pi(n,pos):
    m = n*1.0/float(pi)
    c=[i for i in convergents(m) if i.denominator()<12]
    q=c[-1]
    if q.denominator()==1:
        if q.numerator()==1:
            return r'$\pi$'
        elif q.numerator()==-1:
            return r'$-\pi$'            
        else:
            return r'$%s\pi$'%q
    else:
        if q.numerator()==1:
            return r'$\frac{\pi}{%s}$'%q.denominator()
        elif q.numerator()==-1:
            return r'$\frac{-\pi}{%s}$'%q.denominator()
        else:
            return r'$\frac{%s\pi}{%s}$'%(q.numerator(),q.denominator())

from matplotlib.ticker import MultipleLocator, FuncFormatter
plot(sin(x), (x, -4, 4), tick_locator=MultipleLocator(float(pi/3)), tick_formatter=FuncFormatter(multiple_of_pi))

```




---

archive/issue_comments_009197.json:
```json
{
    "body": "This looks like a great start.  Now we need a wrapper to make creating the formatters and locators easy for the average user.  I will try to help with that, and documentation, as I get a chance.  Thanks!",
    "created_at": "2009-11-12T03:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9197",
    "user": "https://github.com/kcrisman"
}
```

This looks like a great start.  Now we need a wrapper to make creating the formatters and locators easy for the average user.  I will try to help with that, and documentation, as I get a chance.  Thanks!



---

archive/issue_comments_009198.json:
```json
{
    "body": "Personally, I think creating formatters and locators *is* easy.  Notice what I did to create the locator: `MultipleLocator(float(pi/3))`.  The formatter is slightly harder because it's a harder problem I was trying to solve---given a floating point number, find a nice multiple of pi expression for a label.  In general, though, it's easy to just give a list of tick values and strings.\n\nWhat did you have in mind for an easier wrapper?",
    "created_at": "2009-11-12T03:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9198",
    "user": "https://github.com/jasongrout"
}
```

Personally, I think creating formatters and locators *is* easy.  Notice what I did to create the locator: `MultipleLocator(float(pi/3))`.  The formatter is slightly harder because it's a harder problem I was trying to solve---given a floating point number, find a nice multiple of pi expression for a label.  In general, though, it's easy to just give a list of tick values and strings.

What did you have in mind for an easier wrapper?



---

archive/issue_comments_009199.json:
```json
{
    "body": "A simpler example:\n\n\n```\ndef multiple_of_pi(n,pos):\n    m = n*1.0/float(pi)\n    c=[i for i in convergents(m) if i.denominator()<12]\n    q=c[-1]\n    return '$%s$'%latex(q*pi)\n\nfrom matplotlib.ticker import MultipleLocator, FuncFormatter\nplot(sin(x), (x, -4, 4), tick_locator=MultipleLocator(float(pi/4)), tick_formatter=FuncFormatter(multiple_of_pi))\n\n```\n",
    "created_at": "2009-11-12T03:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9199",
    "user": "https://github.com/jasongrout"
}
```

A simpler example:


```
def multiple_of_pi(n,pos):
    m = n*1.0/float(pi)
    c=[i for i in convergents(m) if i.denominator()<12]
    q=c[-1]
    return '$%s$'%latex(q*pi)

from matplotlib.ticker import MultipleLocator, FuncFormatter
plot(sin(x), (x, -4, 4), tick_locator=MultipleLocator(float(pi/4)), tick_formatter=FuncFormatter(multiple_of_pi))

```




---

archive/issue_comments_009200.json:
```json
{
    "body": "See #4529 for a related ticket---logarithmic scales.",
    "created_at": "2009-11-12T04:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9200",
    "user": "https://github.com/jasongrout"
}
```

See #4529 for a related ticket---logarithmic scales.



---

archive/issue_comments_009201.json:
```json
{
    "body": "One last one that is even simpler:\n\n\n```\ndef multiple_of_pi(n,pos):\n    c=[i for i in convergents(n/pi) if i.denominator()<=12]\n    return '$%s$'%latex(c[-1]*pi)\n\nfrom matplotlib.ticker import MultipleLocator, FuncFormatter\nplot(sin(x), (x, -10, 10), tick_locator=MultipleLocator(float(pi/2)), tick_formatter=FuncFormatter(multiple_of_pi),figsize=[10,4])\n```\n",
    "created_at": "2009-11-12T04:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9201",
    "user": "https://github.com/jasongrout"
}
```

One last one that is even simpler:


```
def multiple_of_pi(n,pos):
    c=[i for i in convergents(n/pi) if i.denominator()<=12]
    return '$%s$'%latex(c[-1]*pi)

from matplotlib.ticker import MultipleLocator, FuncFormatter
plot(sin(x), (x, -10, 10), tick_locator=MultipleLocator(float(pi/2)), tick_formatter=FuncFormatter(multiple_of_pi),figsize=[10,4])
```




---

archive/issue_comments_009202.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-12T15:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9202",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_009203.json:
```json
{
    "body": "This is what I meant:\n\n\n```\nsage: plot(sin(x), (x,0,2*pi), tick_locator=pi/3, tick_formatter='pi')\nsage: plot(1.5/(1+e^(-x)), (x,-10,10), tick_locator=[None, 1.5/4]) # shows the inflection point height!\n```\n\n\nSee soon-to-be-attached patch.  Thanks SO much for making this possible - my additions just make it easier for people like me who don't know matplotlib :)\n\nAlso, positive review to the parts I didn't do.",
    "created_at": "2009-11-12T15:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9203",
    "user": "https://github.com/kcrisman"
}
```

This is what I meant:


```
sage: plot(sin(x), (x,0,2*pi), tick_locator=pi/3, tick_formatter='pi')
sage: plot(1.5/(1+e^(-x)), (x,-10,10), tick_locator=[None, 1.5/4]) # shows the inflection point height!
```


See soon-to-be-attached patch.  Thanks SO much for making this possible - my additions just make it easier for people like me who don't know matplotlib :)

Also, positive review to the parts I didn't do.



---

archive/issue_comments_009204.json:
```json
{
    "body": "Perhaps a followup is what sort of object is a Locator?  Just a list?  I couldn't find this in the built-in documentation for ticker (and wasn't online when I created it).  If so, then the documentation should be updated to reflect that; I still think this having the option of just a number is a good one, though I was cludgy in dealing with some of the Errors that might arise.",
    "created_at": "2009-11-12T15:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9204",
    "user": "https://github.com/kcrisman"
}
```

Perhaps a followup is what sort of object is a Locator?  Just a list?  I couldn't find this in the built-in documentation for ticker (and wasn't online when I created it).  If so, then the documentation should be updated to reflect that; I still think this having the option of just a number is a good one, though I was cludgy in dealing with some of the Errors that might arise.



---

archive/issue_comments_009205.json:
```json
{
    "body": "Based on 4.2",
    "created_at": "2009-11-12T15:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9205",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.2



---

archive/issue_comments_009206.json:
```json
{
    "body": "Attachment [trac_1431.patch](tarball://root/attachments/some-uuid/ticket1431/trac_1431.patch) by @jasongrout created at 2009-11-12 17:46:09\n\nTwo comments:\n\n* tick_formatter should accept rational multiples of *any* symbolic constant.  I think the code ought to be generalized before going into Sage.  For example, I should have ticks that are rational multiples of e as well.\n\n* I like the idea of having tick_locator be a number.  I think it should be expanded to being a list (if symbolic expressions, then latexing them can give the formatters), or a function.\n\nSee http://reference.wolfram.com/mathematica/ref/Ticks.html for the equivalent mathematica feature.",
    "created_at": "2009-11-12T17:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9206",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_1431.patch](tarball://root/attachments/some-uuid/ticket1431/trac_1431.patch) by @jasongrout created at 2009-11-12 17:46:09

Two comments:

* tick_formatter should accept rational multiples of *any* symbolic constant.  I think the code ought to be generalized before going into Sage.  For example, I should have ticks that are rational multiples of e as well.

* I like the idea of having tick_locator be a number.  I think it should be expanded to being a list (if symbolic expressions, then latexing them can give the formatters), or a function.

See http://reference.wolfram.com/mathematica/ref/Ticks.html for the equivalent mathematica feature.



---

archive/issue_comments_009207.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-12T17:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9207",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_009208.json:
```json
{
    "body": "I'm putting this as needs_work while we flush out a nice design.",
    "created_at": "2009-11-12T17:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9208",
    "user": "https://github.com/jasongrout"
}
```

I'm putting this as needs_work while we flush out a nice design.



---

archive/issue_comments_009209.json:
```json
{
    "body": "Replying to [comment:12 jason]:\n> Two comments:\n> \n> * tick_formatter should accept rational multiples of *any* symbolic constant.  I think the code ought to be generalized before going into Sage.  For example, I should have ticks that are rational multiples of e as well.\n> \n> * I like the idea of having tick_locator be a number.  I think it should be expanded to being a list (if symbolic expressions, then latexing them can give the formatters), or a function.\n\nThese make lots of sense.  It should be easy to check if the string is in symbolic.constants or something (or even accept those as input), and then of course one would have to check if there was a symbolic expression in the list, and (possibly override) use tick_formatter appropriately.  After all, multiple_of_pi could be made generic to multiple_of_symbolic_constant, and then we could make a dummy function to input into FuncFormatter or something.",
    "created_at": "2009-11-12T18:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9209",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:12 jason]:
> Two comments:
> 
> * tick_formatter should accept rational multiples of *any* symbolic constant.  I think the code ought to be generalized before going into Sage.  For example, I should have ticks that are rational multiples of e as well.
> 
> * I like the idea of having tick_locator be a number.  I think it should be expanded to being a list (if symbolic expressions, then latexing them can give the formatters), or a function.

These make lots of sense.  It should be easy to check if the string is in symbolic.constants or something (or even accept those as input), and then of course one would have to check if there was a symbolic expression in the list, and (possibly override) use tick_formatter appropriately.  After all, multiple_of_pi could be made generic to multiple_of_symbolic_constant, and then we could make a dummy function to input into FuncFormatter or something.



---

archive/issue_comments_009210.json:
```json
{
    "body": "Okay, I've finally had time to return to this, and I'm almost done dealing with this.  It is actually really cool!\n\nFormatting by multiples of constants (or numbers) will be implemented, as well as locating by arbitrary lists.  Note that \n\n```\n    ``LogLocator``\n       logarithmically ticks from min to max\n```\n\ncould solve our log problems, though I think that would not belong on this ticket (and I think there is one for this).",
    "created_at": "2010-04-20T17:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9210",
    "user": "https://github.com/kcrisman"
}
```

Okay, I've finally had time to return to this, and I'm almost done dealing with this.  It is actually really cool!

Formatting by multiples of constants (or numbers) will be implemented, as well as locating by arbitrary lists.  Note that 

```
    ``LogLocator``
       logarithmically ticks from min to max
```

could solve our log problems, though I think that would not belong on this ticket (and I think there is one for this).



---

archive/issue_comments_009211.json:
```json
{
    "body": "Attachment [trac_1431-ticks-and-formatting.patch](tarball://root/attachments/some-uuid/ticket1431/trac_1431-ticks-and-formatting.patch) by @kcrisman created at 2010-04-20 19:42:16\n\nBased on 4.3.5, apply only this patch to Sage library",
    "created_at": "2010-04-20T19:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9211",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_1431-ticks-and-formatting.patch](tarball://root/attachments/some-uuid/ticket1431/trac_1431-ticks-and-formatting.patch) by @kcrisman created at 2010-04-20 19:42:16

Based on 4.3.5, apply only this patch to Sage library



---

archive/issue_comments_009212.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-20T19:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9212",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_009213.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2010-04-20T20:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9213",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_009214.json:
```json
{
    "body": "1. \"Private\" functions (like the first one) should begin with an underscore\n   1. plot(2*x+1,(x,0,5),tick_locator=[[0,1,e,pi,sqrt(20)],2],tick_formatter=\"latex\") looks really bad since the minor ticks do not pay attention to the major ticks\n   2. in general, it looks really weird to have very small latex numbers on one axis while having large non-latex numbers on the other axis.\u00a0 I'm not sure what we can do about this.",
    "created_at": "2010-04-20T20:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9214",
    "user": "https://github.com/jasongrout"
}
```

1. "Private" functions (like the first one) should begin with an underscore
   1. plot(2*x+1,(x,0,5),tick_locator=[[0,1,e,pi,sqrt(20)],2],tick_formatter="latex") looks really bad since the minor ticks do not pay attention to the major ticks
   2. in general, it looks really weird to have very small latex numbers on one axis while having large non-latex numbers on the other axis.  I'm not sure what we can do about this.



---

archive/issue_comments_009215.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-20T20:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9215",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_009216.json:
```json
{
    "body": "Changing assignee from @jasongrout to @kcrisman.",
    "created_at": "2010-04-20T20:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9216",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @jasongrout to @kcrisman.



---

archive/issue_comments_009217.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n>  1. \"Private\" functions (like the first one) should begin with an underscore\nYou mean the multiple one?  Ok.\n>  1. plot(2*x+1,(x,0,5),tick_locator=[[0,1,e,pi,sqrt(20)],2],tick_formatter=\"latex\") looks really bad since the minor ticks do not pay attention to the major ticks\nI totally agree, but I figured it was best to respond to your suggestion first, and then take ideas for how to fix this issue.  Any ideas?\n>  1. in general, it looks really weird to have very small latex numbers on one axis while having large non-latex numbers on the other axis.\u00a0 I'm not sure what we can do about this.\nI see.  I don't think this is a problem - we can just make it so that \"latex\" is applied to both axes, if used.  What do you think?",
    "created_at": "2010-04-20T20:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9217",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:18 jason]:
>  1. "Private" functions (like the first one) should begin with an underscore
You mean the multiple one?  Ok.
>  1. plot(2*x+1,(x,0,5),tick_locator=[[0,1,e,pi,sqrt(20)],2],tick_formatter="latex") looks really bad since the minor ticks do not pay attention to the major ticks
I totally agree, but I figured it was best to respond to your suggestion first, and then take ideas for how to fix this issue.  Any ideas?
>  1. in general, it looks really weird to have very small latex numbers on one axis while having large non-latex numbers on the other axis.  I'm not sure what we can do about this.
I see.  I don't think this is a problem - we can just make it so that "latex" is applied to both axes, if used.  What do you think?



---

archive/issue_comments_009218.json:
```json
{
    "body": "Okay, I've fixed all of these things.  Note that Mma only includes major ticks for lists of ticks, so I just went with that (much easier!).  The latex thing was annoying - there was a bug in sage.misc.latex.str_function:\n\n```\nsage: sage.misc.latex.str_function('4')\n'4'\nsage: sage.misc.latex.str_function('4.0')\n'\\\\texttt{4.0}'\n```\n\nAt least I view this as a bug, and in any case it prevents the latexing from working properly even if the tick_locator had [0,1.0,e] rather than [0,1,e].  Unified patch coming up.",
    "created_at": "2010-04-21T03:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9218",
    "user": "https://github.com/kcrisman"
}
```

Okay, I've fixed all of these things.  Note that Mma only includes major ticks for lists of ticks, so I just went with that (much easier!).  The latex thing was annoying - there was a bug in sage.misc.latex.str_function:

```
sage: sage.misc.latex.str_function('4')
'4'
sage: sage.misc.latex.str_function('4.0')
'\\texttt{4.0}'
```

At least I view this as a bug, and in any case it prevents the latexing from working properly even if the tick_locator had [0,1.0,e] rather than [0,1,e].  Unified patch coming up.



---

archive/issue_comments_009219.json:
```json
{
    "body": "Apply only ticks, formatting, and latex patch.",
    "created_at": "2010-04-21T03:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9219",
    "user": "https://github.com/kcrisman"
}
```

Apply only ticks, formatting, and latex patch.



---

archive/issue_comments_009220.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-21T03:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9220",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_009221.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-21T03:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9221",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_009222.json:
```json
{
    "body": "Very nice now!\u00a0 One last thing that I saw: the examples for _multiple_... still have the problem of halfof the ticks being in latex and the other half not.\u00a0 For example, plot(x!^2, (x, -2, 2), tick_formatter=pi) has the vertical labels in the standard font and the horizontal labels in tex.",
    "created_at": "2010-04-21T03:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9222",
    "user": "https://github.com/jasongrout"
}
```

Very nice now!  One last thing that I saw: the examples for _multiple_... still have the problem of halfof the ticks being in latex and the other half not.  For example, plot(x!^2, (x, -2, 2), tick_formatter=pi) has the vertical labels in the standard font and the horizontal labels in tex.



---

archive/issue_comments_009223.json:
```json
{
    "body": "Replying to [comment:24 jason]:\n> Very nice now!\u00a0 One last thing that I saw: the examples for _multiple_... still have the problem of halfof the ticks being in latex and the other half not.\u00a0 For example, plot(x!^2, (x, -2, 2), tick_formatter=pi) has the vertical labels in the standard font and the horizontal labels in tex.\n\nHmm, that's true.  I don't know - this is more of a design decision than anything.  In theory, we could latex ALL our tick labels, but that seems overkill.  On the other hand, the solution to this would be kind of cludgy.\n\nAlso, I was thinking about it this morning and wondered whether it would make sense to have the \"tick_locator\" keyword be just \"ticks\" or \"tick\" instead.  Mma using \"ticks\", and \"tick_locator\" is a little longish (\"tick_formatter\" makes sense, though).\n\nLet me know if you have any ideas.",
    "created_at": "2010-04-21T12:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9223",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:24 jason]:
> Very nice now!  One last thing that I saw: the examples for _multiple_... still have the problem of halfof the ticks being in latex and the other half not.  For example, plot(x!^2, (x, -2, 2), tick_formatter=pi) has the vertical labels in the standard font and the horizontal labels in tex.

Hmm, that's true.  I don't know - this is more of a design decision than anything.  In theory, we could latex ALL our tick labels, but that seems overkill.  On the other hand, the solution to this would be kind of cludgy.

Also, I was thinking about it this morning and wondered whether it would make sense to have the "tick_locator" keyword be just "ticks" or "tick" instead.  Mma using "ticks", and "tick_locator" is a little longish ("tick_formatter" makes sense, though).

Let me know if you have any ideas.



---

archive/issue_comments_009224.json:
```json
{
    "body": "Thanks for all the work on this ticket.  I'm helping my wife with a final project for an environmental science class (involving measuring \"smog\"), and not having tick control is devastating.   Finally, for the first time, I personally really need this capability :-)\n\nAnother killer is not have a legend.  Is that also easy to add via something similar?  (Probably.)",
    "created_at": "2010-05-18T05:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9224",
    "user": "https://github.com/williamstein"
}
```

Thanks for all the work on this ticket.  I'm helping my wife with a final project for an environmental science class (involving measuring "smog"), and not having tick control is devastating.   Finally, for the first time, I personally really need this capability :-)

Another killer is not have a legend.  Is that also easy to add via something similar?  (Probably.)



---

archive/issue_comments_009225.json:
```json
{
    "body": "Replying to [comment:26 was]:\n\n> Another killer is not have a legend.  Is that also easy to add via something similar?  (Probably.)\n\nSee #4342",
    "created_at": "2010-05-18T05:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9225",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:26 was]:

> Another killer is not have a legend.  Is that also easy to add via something similar?  (Probably.)

See #4342



---

archive/issue_comments_009226.json:
```json
{
    "body": "Of course, you can also always use straight matplotlib to do these things right now.",
    "created_at": "2010-05-18T05:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9226",
    "user": "https://github.com/jasongrout"
}
```

Of course, you can also always use straight matplotlib to do these things right now.



---

archive/issue_comments_009227.json:
```json
{
    "body": "And it turned out that this patch 100% totally worked to solve my problem.  Yes!  \n\n  http://tutorial.sagenb.org/home/pub/19/\n\nOf course, it will be nice when the capabilities are doctested. \n\nRegarding using \"straight matplotlib\", that would be a bit annoying, since all my plot commands are in Sage, so I have to get at the secret underlying matplotlib fig/canvas, right?  Or rewrite all my code to use pylab directly.   I don't want to do that \"on principle\".",
    "created_at": "2010-05-18T05:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9227",
    "user": "https://github.com/williamstein"
}
```

And it turned out that this patch 100% totally worked to solve my problem.  Yes!  

  http://tutorial.sagenb.org/home/pub/19/

Of course, it will be nice when the capabilities are doctested. 

Regarding using "straight matplotlib", that would be a bit annoying, since all my plot commands are in Sage, so I have to get at the secret underlying matplotlib fig/canvas, right?  Or rewrite all my code to use pylab directly.   I don't want to do that "on principle".



---

archive/issue_comments_009228.json:
```json
{
    "body": "Replying to [comment:29 was]:\n\n> Regarding using \"straight matplotlib\", that would be a bit annoying, since all my plot commands are in Sage, so I have to get at the secret underlying matplotlib fig/canvas, right?  \n\nWell, it's not so secret, though, as it is exposed in a public function:\n\np=plot(x^2,(x,-3,4))\nfigure=p.matplotlib()\nfrom matplotlib.backends.backend_agg import FigureCanvasAgg\nfigure.set_canvas(FigureCanvasAgg(figure))\nfigure.savefig('test.png')\n\n(the last three lines are a bit esoteric, but they are fairly straightforward matplotlib...)",
    "created_at": "2010-05-18T06:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9228",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:29 was]:

> Regarding using "straight matplotlib", that would be a bit annoying, since all my plot commands are in Sage, so I have to get at the secret underlying matplotlib fig/canvas, right?  

Well, it's not so secret, though, as it is exposed in a public function:

p=plot(x^2,(x,-3,4))
figure=p.matplotlib()
from matplotlib.backends.backend_agg import FigureCanvasAgg
figure.set_canvas(FigureCanvasAgg(figure))
figure.savefig('test.png')

(the last three lines are a bit esoteric, but they are fairly straightforward matplotlib...)



---

archive/issue_comments_009229.json:
```json
{
    "body": "Replying to [comment:29 was]:\n> And it turned out that this patch 100% totally worked to solve my problem.  Yes!  \n> \n>   http://tutorial.sagenb.org/home/pub/19/\n\nSweet!  Looks great.\n\n> \n> Of course, it will be nice when the capabilities are doctested. \n\nOkay, that and figuring out what to do with the Latex situation are all this ticket needs, then.  I can't work on this until after the first PREP workshop, but after that it's very high on my list.",
    "created_at": "2010-05-18T16:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9229",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:29 was]:
> And it turned out that this patch 100% totally worked to solve my problem.  Yes!  
> 
>   http://tutorial.sagenb.org/home/pub/19/

Sweet!  Looks great.

> 
> Of course, it will be nice when the capabilities are doctested. 

Okay, that and figuring out what to do with the Latex situation are all this ticket needs, then.  I can't work on this until after the first PREP workshop, but after that it's very high on my list.



---

archive/issue_comments_009230.json:
```json
{
    "body": "From private email, in response to kcrisman's comment above:\n\n>\n>\n> Hmm, that's true. I don't know - this is more of a design decision\n> than anything. In theory, we could latex ALL our tick labels, but that\n> seems overkill. On the other hand, the solution to this would be kind\n> of cludgy.\n>\n> Also, I was thinking about it this morning and wondered whether it\n> would make sense to have the \"tick_locator\" keyword be just \"ticks\" or\n> \"tick\" instead. Mma using \"ticks\", and \"tick_locator\" is a little\n> longish (\"tick_formatter\" makes sense, though).\n>\n> Let me know if you have any ideas.\n\n+1 to \"ticks\"\n\nI'm not sure what to do about the latex issue.  I suppose the real problem here is that matplotlib does not use compatible fonts for $1$ and just straight 1.  That's a bummer.  Still, in the common case (i.e., people didn't specify formatters), I think we should make it all latex or all not latex.  plot(sin(x), (x,0,pi), tick_formatter=pi) is likely to be a very common case, and we shouldn't have \"ugly\" output for it.  It looks like it might be as easy as changing the line:\n\n\n```\n 1818            if y_formatter is None:  \n1819                y_formatter = OldScalarFormatter()\n```\n\nto\n\n```\nif y_formatter is None:\n    y_formatter = copy(x_formatter)  # maybe copy isn't needed\n```\n\nWe could then also delete the if statement above dealing with setting both formatters to \"latex\" if tick_formatter=\"latex\".\n\nThe one problem with this is that plot(..., ticks=pi) would change both the x and the y axis.  Maybe we could special-case that situation.",
    "created_at": "2010-05-25T15:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9230",
    "user": "https://github.com/jasongrout"
}
```

From private email, in response to kcrisman's comment above:

>
>
> Hmm, that's true. I don't know - this is more of a design decision
> than anything. In theory, we could latex ALL our tick labels, but that
> seems overkill. On the other hand, the solution to this would be kind
> of cludgy.
>
> Also, I was thinking about it this morning and wondered whether it
> would make sense to have the "tick_locator" keyword be just "ticks" or
> "tick" instead. Mma using "ticks", and "tick_locator" is a little
> longish ("tick_formatter" makes sense, though).
>
> Let me know if you have any ideas.

+1 to "ticks"

I'm not sure what to do about the latex issue.  I suppose the real problem here is that matplotlib does not use compatible fonts for $1$ and just straight 1.  That's a bummer.  Still, in the common case (i.e., people didn't specify formatters), I think we should make it all latex or all not latex.  plot(sin(x), (x,0,pi), tick_formatter=pi) is likely to be a very common case, and we shouldn't have "ugly" output for it.  It looks like it might be as easy as changing the line:


```
 1818            if y_formatter is None:  
1819                y_formatter = OldScalarFormatter()
```

to

```
if y_formatter is None:
    y_formatter = copy(x_formatter)  # maybe copy isn't needed
```

We could then also delete the if statement above dealing with setting both formatters to "latex" if tick_formatter="latex".

The one problem with this is that plot(..., ticks=pi) would change both the x and the y axis.  Maybe we could special-case that situation.



---

archive/issue_comments_009231.json:
```json
{
    "body": "> > Also, I was thinking about it this morning and wondered whether it\n> > would make sense to have the \"tick_locator\" keyword be just \"ticks\" or\n> > \"tick\" instead. Mma using \"ticks\", and \"tick_locator\" is a little\n> > longish (\"tick_formatter\" makes sense, though).\n> >\n> +1 to \"ticks\"\n\nOk, done.\n\n> I'm not sure what to do about the latex issue.  I suppose the real problem here is that matplotlib does not use compatible fonts for $1$ and just straight 1.  That's a bummer.  Still, in the common case (i.e., people didn't specify formatters), I think we should make it all latex or all not latex.  plot(sin(x), (x,0,pi), tick_formatter=pi) is likely to be a very common case, and we shouldn't have \"ugly\" output for it.  It looks like it might be as easy as changing the line:\n> \n> {{{\n>  1818            if y_formatter is None:  \n> 1819                y_formatter = OldScalarFormatter()\n> }}}\n> to\n> {{{\n> if y_formatter is None:\n>     y_formatter = copy(x_formatter)  # maybe copy isn't needed\n> }}}\n> We could then also delete the if statement above dealing with setting both formatters to \"latex\" if tick_formatter=\"latex\".\n> \n> The one problem with this is that plot(..., ticks=pi) would change both the x and the y axis.  Maybe we could special-case that situation.\n\nIf you note, the documentation is already quite explicit that you should not do that example in 'real life' :-)  though I'll make it even more explicit.  Luckily that example is also in an underscore function.\n\nI think a better solution is that if y_formatter is None and x_formatter was in SR, then we should do y_formatter='latex'.  I propose to do this via \n\n```\n        from sage.symbolic.ring import SR\n        if not isinstance(tick_formatter, (list, tuple)):\n            if tick_formatter == \"latex\" or tick_formatter in SR:\n                tick_formatter = (tick_formatter, \"latex\")\n            else:\n                tick_formatter = (tick_formatter, None)        \n```\n\nI also will check for the much rarer case of plotting arcsin, so to speak.  Patch coming up.",
    "created_at": "2010-05-25T18:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9231",
    "user": "https://github.com/kcrisman"
}
```

> > Also, I was thinking about it this morning and wondered whether it
> > would make sense to have the "tick_locator" keyword be just "ticks" or
> > "tick" instead. Mma using "ticks", and "tick_locator" is a little
> > longish ("tick_formatter" makes sense, though).
> >
> +1 to "ticks"

Ok, done.

> I'm not sure what to do about the latex issue.  I suppose the real problem here is that matplotlib does not use compatible fonts for $1$ and just straight 1.  That's a bummer.  Still, in the common case (i.e., people didn't specify formatters), I think we should make it all latex or all not latex.  plot(sin(x), (x,0,pi), tick_formatter=pi) is likely to be a very common case, and we shouldn't have "ugly" output for it.  It looks like it might be as easy as changing the line:
> 
> {{{
>  1818            if y_formatter is None:  
> 1819                y_formatter = OldScalarFormatter()
> }}}
> to
> {{{
> if y_formatter is None:
>     y_formatter = copy(x_formatter)  # maybe copy isn't needed
> }}}
> We could then also delete the if statement above dealing with setting both formatters to "latex" if tick_formatter="latex".
> 
> The one problem with this is that plot(..., ticks=pi) would change both the x and the y axis.  Maybe we could special-case that situation.

If you note, the documentation is already quite explicit that you should not do that example in 'real life' :-)  though I'll make it even more explicit.  Luckily that example is also in an underscore function.

I think a better solution is that if y_formatter is None and x_formatter was in SR, then we should do y_formatter='latex'.  I propose to do this via 

```
        from sage.symbolic.ring import SR
        if not isinstance(tick_formatter, (list, tuple)):
            if tick_formatter == "latex" or tick_formatter in SR:
                tick_formatter = (tick_formatter, "latex")
            else:
                tick_formatter = (tick_formatter, None)        
```

I also will check for the much rarer case of plotting arcsin, so to speak.  Patch coming up.



---

archive/issue_comments_009232.json:
```json
{
    "body": "Based on 4.3.5, apply only this patch to Sage library",
    "created_at": "2010-05-25T18:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9232",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.3.5, apply only this patch to Sage library



---

archive/issue_comments_009233.json:
```json
{
    "body": "Attachment [trac_1431-ticks-and-formatting-and-latex.patch](tarball://root/attachments/some-uuid/ticket1431/trac_1431-ticks-and-formatting-and-latex.patch) by @kcrisman created at 2010-05-25 18:46:48\n\nNeeds review.  Notice that for some reason it kept the old message - but this latest one is based on 4.4.2, no worries :-)",
    "created_at": "2010-05-25T18:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9233",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_1431-ticks-and-formatting-and-latex.patch](tarball://root/attachments/some-uuid/ticket1431/trac_1431-ticks-and-formatting-and-latex.patch) by @kcrisman created at 2010-05-25 18:46:48

Needs review.  Notice that for some reason it kept the old message - but this latest one is based on 4.4.2, no worries :-)



---

archive/issue_comments_009234.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T18:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9234",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_009235.json:
```json
{
    "body": "Looks great, applies to 4.5.2, and doctests pass in changed files.  Great job!",
    "created_at": "2010-09-03T22:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9235",
    "user": "https://github.com/jasongrout"
}
```

Looks great, applies to 4.5.2, and doctests pass in changed files.  Great job!



---

archive/issue_comments_009236.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-03T22:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9236",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_009237.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1431#issuecomment-9237",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_001578.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T10:40:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1431",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1431#event-1578"
}
```
