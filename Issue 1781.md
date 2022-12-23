# Issue 1781: preparser bug involving backslash-to-continue line

Issue created by migration from https://trac.sagemath.org/ticket/1781

Original creator: was

Original creation time: 2008-01-15 06:41:55

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



---

Comment by robertwb created at 2008-01-15 07:19:16

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-15 07:19:16

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-01-15 07:19:16

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

Comment by @DaveWitteMorris created at 2020-05-14 01:13:25

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

Comment by @DaveWitteMorris created at 2020-05-14 01:13:25

Changing status from new to needs_review.


---

Comment by @DaveWitteMorris created at 2020-05-14 01:13:25

Changing priority from major to minor.


---

Comment by dimpase created at 2020-07-31 17:00:54

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-19 16:17:50

Resolution: worksforme
