# Issue 1781: preparser bug involving backslash-to-continue line

archive/issues_001781.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n\nOn Jan 14, 2008 10:33 PM, Dan Drake <> wrote:\n> On Mon, 14 Jan 2008 at 05:05PM -0800, William Stein wrote:\n> > On Jan 14, 2008 5:00 PM, Dan Drake <> wrote:\n> > > In a .sage script file, I have:\n> > >\n> > >   maple.eval('plotsetup(ps, plotoutput=`logplot.eps`, \\\n> > >     plotoptions=`portrait,noborder,color`)')\n> > >   maple.eval('plot(log(2*x), x=1..2,filled=true,color=yellow, \\\n> > >     view=[.75..2.25,0..1.5])')\n> > >\n> > > but the corresponding .py file has, for the second command,\n> > >\n> > >   maple.eval('plot(log(2*x), x=1..2,filled=true,color=yellow, \\\n> > >     view=(ellipsis_range(.75,Ellipsis,2.25,0,Ellipsis,1.5)))')\n> > >\n> > > Maple obviously doesn't understand this. It seems the preparser is a\n> > > bit too eager; it needs to ignore stuff that will get passed to\n> > > Maple or whatever. Can this be fixed?\n> >\n> > The problem is the multiple lines.  Try the same thing but without the\n> > \\ at the end of the line and see what happens.\n> \n> It works fine in that case...which I discovered (naturally) a minute or\n> two after sending the message.\n> \n> Looks like the preparser is not aware of the\n> backslash-continues-the-line convention.\n\nThe parts of the preparser I wrote are:\n\nsage: v = '1 + \\\n....: 3'\nsage: v\n'1 + 3'\n\nBut Robert B. wrote the really cool [n..m] parser code,\nand unfortunately he appears to have written it in a way that\ndoes not work correctly with \\'s.  He'll undoubtedly see\nthis and fix it. \n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1781\n\n",
    "created_at": "2008-01-15T06:41:55Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "preparser bug involving backslash-to-continue line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1781",
    "user": "was"
}
```
Assignee: was


```


On Jan 14, 2008 10:33 PM, Dan Drake <> wrote:
> On Mon, 14 Jan 2008 at 05:05PM -0800, William Stein wrote:
> > On Jan 14, 2008 5:00 PM, Dan Drake <> wrote:
> > > In a .sage script file, I have:
> > >
> > >   maple.eval('plotsetup(ps, plotoutput=`logplot.eps`, \
> > >     plotoptions=`portrait,noborder,color`)')
> > >   maple.eval('plot(log(2*x), x=1..2,filled=true,color=yellow, \
> > >     view=[.75..2.25,0..1.5])')
> > >
> > > but the corresponding .py file has, for the second command,
> > >
> > >   maple.eval('plot(log(2*x), x=1..2,filled=true,color=yellow, \
> > >     view=(ellipsis_range(.75,Ellipsis,2.25,0,Ellipsis,1.5)))')
> > >
> > > Maple obviously doesn't understand this. It seems the preparser is a
> > > bit too eager; it needs to ignore stuff that will get passed to
> > > Maple or whatever. Can this be fixed?
> >
> > The problem is the multiple lines.  Try the same thing but without the
> > \ at the end of the line and see what happens.
> 
> It works fine in that case...which I discovered (naturally) a minute or
> two after sending the message.
> 
> Looks like the preparser is not aware of the
> backslash-continues-the-line convention.

The parts of the preparser I wrote are:

sage: v = '1 + \
....: 3'
sage: v
'1 + 3'

But Robert B. wrote the really cool [n..m] parser code,
and unfortunately he appears to have written it in a way that
does not work correctly with \'s.  He'll undoubtedly see
this and fix it. 

William
```


Issue created by migration from https://trac.sagemath.org/ticket/1781





---

archive/issue_comments_011274.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-15T07:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11274",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011275.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-01-15T07:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11275",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_011276.json:
```json
{
    "body": "The problem is not specific to the [..] notation, but that the preparser processes things one line at a time. For example \n\n\n```\nsage: K.<a> = NumberField('\\\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     K = NumberField('\\; (a,) = K._first_ngens(1)\n                                                ^\n<type 'exceptions.SyntaxError'>: EOL while scanning single-quoted string\n```\n\n\nWe abuse the \\ notation to have the same matrix solving property as Matlab too, but within strings it should be fine. I've been meaning to refactors the preparsing to make it more efficient, and will fix bugs like this at the same time.",
    "created_at": "2008-01-15T07:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11276",
    "user": "robertwb"
}
```

The problem is not specific to the [..] notation, but that the preparser processes things one line at a time. For example 


```
sage: K.<a> = NumberField('\
------------------------------------------------------------
   File "<ipython console>", line 1
     K = NumberField('\; (a,) = K._first_ngens(1)
                                                ^
<type 'exceptions.SyntaxError'>: EOL while scanning single-quoted string
```


We abuse the \ notation to have the same matrix solving property as Matlab too, but within strings it should be fine. I've been meaning to refactors the preparsing to make it more efficient, and will fix bugs like this at the same time.



---

archive/issue_comments_011277.json:
```json
{
    "body": "The error was fixed at some point (probably long ago).  I put the given lines into a .sage file, and the corresponding .py file has a valid translation:\n\n```\nmaple.eval('plotsetup(ps, plotoutput=`logplot.eps`, \\\n  plotoptions=`portrait,noborder,color`)')\nmaple.eval('plot(log(2*x), x=1..2,filled=true,color=yellow, \\\n  view=[.75..2.25,0..1.5])')\n```\n\nAlso, the example in comment:1 now gives the same error as equivalent code without a line break.\n\n```\nsage: K.<a> = NumberField('\\\n....: x^2 + 1')\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n/Users/dmorris/Documents/misc/Programs/sage3/local/lib/python3.7/site-packages/sage/rings/number_field/number_field.py in create_key_and_extra_args(self, polynomial, name, check, embedding, latex_name, assume_disc_small, maximize_at_primes, structure)\n    625             try:\n--> 626                 polynomial = polynomial.polynomial(QQ)\n    627             except (AttributeError, TypeError):\n\nAttributeError: 'str' object has no attribute 'polynomial'\n\nDuring handling of the above exception, another exception occurred:\n\nTypeError                                 Traceback (most recent call last)\n<ipython-input-148-c544dd60baaa> in <module>()\n----> 1 K = NumberField('x^2 + 1', names=('a',)); (a,) = K._first_ngens(1)\n...\n    626                 polynomial = polynomial.polynomial(QQ)\n    627             except (AttributeError, TypeError):\n--> 628                 raise TypeError(\"polynomial (=%s) must be a polynomial.\" % polynomial)\n    629 \n    630         # convert polynomial to a polynomial over a field\n\nTypeError: polynomial (=x^2 + 1) must be a polynomial.\n\nsage: K.<a> = NumberField('x^2 + 1')\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n/Users/dmorris/Documents/misc/Programs/sage3/local/lib/python3.7/site-packages/sage/rings/number_field/number_field.py in create_key_and_extra_args(self, polynomial, name, check, embedding, latex_name, assume_disc_small, maximize_at_primes, structure)\n    625             try:\n--> 626                 polynomial = polynomial.polynomial(QQ)\n    627             except (AttributeError, TypeError):\n\nAttributeError: 'str' object has no attribute 'polynomial'\n\nDuring handling of the above exception, another exception occurred:\n\nTypeError                                 Traceback (most recent call last)\n<ipython-input-149-c544dd60baaa> in <module>()\n----> 1 K = NumberField('x^2 + 1', names=('a',)); (a,) = K._first_ngens(1)\n...\n    626                 polynomial = polynomial.polynomial(QQ)\n    627             except (AttributeError, TypeError):\n--> 628                 raise TypeError(\"polynomial (=%s) must be a polynomial.\" % polynomial)\n    629 \n    630         # convert polynomial to a polynomial over a field\n\nTypeError: polynomial (=x^2 + 1) must be a polynomial.",
    "created_at": "2020-05-14T01:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11277",
    "user": "@DaveWitteMorris"
}
```

The error was fixed at some point (probably long ago).  I put the given lines into a .sage file, and the corresponding .py file has a valid translation:

```
maple.eval('plotsetup(ps, plotoutput=`logplot.eps`, \
  plotoptions=`portrait,noborder,color`)')
maple.eval('plot(log(2*x), x=1..2,filled=true,color=yellow, \
  view=[.75..2.25,0..1.5])')
```

Also, the example in comment:1 now gives the same error as equivalent code without a line break.

```
sage: K.<a> = NumberField('\
....: x^2 + 1')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/Users/dmorris/Documents/misc/Programs/sage3/local/lib/python3.7/site-packages/sage/rings/number_field/number_field.py in create_key_and_extra_args(self, polynomial, name, check, embedding, latex_name, assume_disc_small, maximize_at_primes, structure)
    625             try:
--> 626                 polynomial = polynomial.polynomial(QQ)
    627             except (AttributeError, TypeError):

AttributeError: 'str' object has no attribute 'polynomial'

During handling of the above exception, another exception occurred:

TypeError                                 Traceback (most recent call last)
<ipython-input-148-c544dd60baaa> in <module>()
----> 1 K = NumberField('x^2 + 1', names=('a',)); (a,) = K._first_ngens(1)
...
    626                 polynomial = polynomial.polynomial(QQ)
    627             except (AttributeError, TypeError):
--> 628                 raise TypeError("polynomial (=%s) must be a polynomial." % polynomial)
    629 
    630         # convert polynomial to a polynomial over a field

TypeError: polynomial (=x^2 + 1) must be a polynomial.

sage: K.<a> = NumberField('x^2 + 1')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/Users/dmorris/Documents/misc/Programs/sage3/local/lib/python3.7/site-packages/sage/rings/number_field/number_field.py in create_key_and_extra_args(self, polynomial, name, check, embedding, latex_name, assume_disc_small, maximize_at_primes, structure)
    625             try:
--> 626                 polynomial = polynomial.polynomial(QQ)
    627             except (AttributeError, TypeError):

AttributeError: 'str' object has no attribute 'polynomial'

During handling of the above exception, another exception occurred:

TypeError                                 Traceback (most recent call last)
<ipython-input-149-c544dd60baaa> in <module>()
----> 1 K = NumberField('x^2 + 1', names=('a',)); (a,) = K._first_ngens(1)
...
    626                 polynomial = polynomial.polynomial(QQ)
    627             except (AttributeError, TypeError):
--> 628                 raise TypeError("polynomial (=%s) must be a polynomial." % polynomial)
    629 
    630         # convert polynomial to a polynomial over a field

TypeError: polynomial (=x^2 + 1) must be a polynomial.



---

archive/issue_comments_011278.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-14T01:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11278",
    "user": "@DaveWitteMorris"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011279.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2020-05-14T01:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11279",
    "user": "@DaveWitteMorris"
}
```

Changing priority from major to minor.



---

archive/issue_comments_011280.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-31T17:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11280",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011281.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2020-08-19T16:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1781#issuecomment-11281",
    "user": "chapoton"
}
```

Resolution: worksforme
