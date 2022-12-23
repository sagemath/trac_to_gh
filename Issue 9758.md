# Issue 9758: Addition of SI prefixes capabilities to the units module

Issue created by migration from https://trac.sagemath.org/ticket/9759

Original creator: cousteau

Original creation time: 2010-08-17 22:51:22

Assignee: burcin

CC:  rbeezer was

Although the units module already has a si_prefixes component, it's not very convenient, since you have to do units.si_prefixes.nano*units.mass.gram, and you get something like "gram*nano" that doesn't look very well.
This ticket is a modification that adds properties named as the components of units.si_prefixes, so that calling something like units.mass.gram.nano will create a units.mass.nanogram element and return it.


---

Attachment

Patch that adds components of units.si_prefixes as properties on the UnitExpression class


---

Comment by cousteau created at 2010-08-17 23:22:42

Changing status from new to needs_review.


---

Comment by burcin created at 2011-05-10 18:54:28

The patch looks good to me. It is a hack and I am not really happy with the use of `sage_eval()`, but this seems to be used everywhere in `sage/symbolic/units.py`. I'm ready to give a positive review, though it would be better if somebody who actually uses this module comments on the improvement.

Why does the new function name start with an underscore? Wouldn't it be easier to find it if was just named `si_prefix()`?


---

Comment by cousteau created at 2011-05-10 19:58:09

The truth is that this patch was created as a suggestion done in #sage-devel; it was done pretty fast and probably not elegantly. I later submitted another patch with a better implementation (see ticket #9778), which also added the basics for `LaTeX` representation of the units.

(I also made the alternate "metrology" module on #9763, which also has LaTeX and units support)


---

Comment by kcrisman created at 2012-05-26 07:25:10

I agree with Burcin that this is a bit hackish.  
> The truth is that this patch was created as a suggestion done in #sage-devel; it was done pretty fast and probably not elegantly. I later submitted another patch with a better implementation (see ticket #9778), which also added the basics for `LaTeX` representation of the units.
So should this be closed in favor of #9778?

Also, 

```
def _add_si_property_(prefix): 
 	    setattr(UnitExpression, prefix, property(lambda self: self._si_prefix_(prefix))) 
 
for prefix in unitdict['si_prefixes']: 
     _add_si_property_(prefix) 
```

seems to be missing a doctest in the underscore function.


---

Comment by kcrisman created at 2012-05-26 07:25:10

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-05-26 07:25:10

Changing keywords from "" to "sd40.5".


---

Comment by cousteau created at 2012-05-28 14:21:59

Replying to [comment:6 kcrisman]:
> So should this be closed in favor of #9778?
I think it'd be a good idea.


---

Comment by kcrisman created at 2012-05-28 15:49:43

> > So should this be closed in favor of #9778?
> I think it'd be a good idea.
Okay, I'll make a comment there to that effect.


---

Comment by kcrisman created at 2012-05-28 15:49:43

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:47:05

Resolution: duplicate
