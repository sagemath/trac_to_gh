# Issue 8983: solve(erf(x)==0,x) should return x==0 as a solution

Issue created by migration from Trac.

Original creator: rossk

Original creation time: 2010-05-17 13:15:56

Assignee: RossK

CC:  burcin kcrisman

Keywords: erf zero

Currently it doesnt...


```
sage: solve(erf(x)==0,x)
[erf(x) == 0]
```



---

Comment by rossk created at 2010-05-17 13:16:30

Changing type from defect to enhancement.


---

Comment by rossk created at 2010-05-17 13:16:30

Changing priority from major to minor.


---

Comment by burcin created at 2010-05-17 13:27:17

Here is the relevant thread on sage-devel:

http://groups.google.com/group/sage-devel/t/d236e80bf7826bff

The main problem is this:


```
sage: erf(0)
erf(0)
```


We should just return 0.


---

Comment by burcin created at 2010-08-28 16:16:51

Changing keywords from "erf zero" to "erf, beginner".


---

Comment by dsm created at 2011-02-20 05:58:07

Beginner reporting for duty!  So I have a patch which sets erf(0) to 0 -- or, rather, to parent(x)(0) if x==0, so that it's the "right" zero; I think this is the right idiom -- and adds complex arguments from mpmath.

But I have a few questions that came up along the way:

(1) In 4.6.1, solve(erf(x)==0,x) seems to work for me already, before the patch.  Did I get my binaries confused somehow, or did something change elsewhere?

(2) It'd be nice if #8720 (fixing str(CC(0))) were finished, it surprised me when writing tests for the zero type preservation. Maybe I should have a look, I think it's mostly fixing some doctests left.

(3) My patch broke a doctest in functions/special.py, which expected erf(0.5) to be evaluated to 0.520499877813047, but the existing doctests for erf demand that erf(2) = erf(2). I can get that behaviour, namely to evaluate for reals and to hold for integers except for zero, but I don't quite follow it.

(4) Since I'm doing a bit more, should I open an enhancement ticket instead?


---

Comment by kcrisman created at 2011-02-21 16:54:13

You should always feel free to add patches - it's MUCH easier to tell what people are talking about, even if the patch is really, really preliminary.
> (1) In 4.6.1, solve(erf(x)==0,x) seems to work for me already, before the patch.  Did I get my binaries confused somehow, or did something change elsewhere?
This must be from an improvement in Maxima during the several recent upgrades.  I've updated the description.
> (3) My patch broke a doctest in functions/special.py, which expected erf(0.5) to be evaluated to 0.520499877813047, but the existing doctests for erf demand that erf(2) = erf(2). I can get that behaviour, namely to evaluate for reals and to hold for integers except for zero, but I don't quite follow it.
No, the usual practice is to not evaluate (give symbolic back) for "exact" rings and evaluate (give numeric back) for "inexact" rings.  There is some disagreement among developers about exactly what these words mean, but basically `erf(x),erf(1/2),erf(2),erf(e)` should all return something symbolic and `erf(.1),erf(RDF(1))`, etc. should return something numeric.  I.e. `erf2)!=erf(2.)`.
> 
> (4) Since I'm doing a bit more, should I open an enhancement ticket instead?
I believe there already is a ticket for the complex pieces at #1173, similarly at #9044.  If you have a good solution to the whole thing, you could do it at one of those and then say this ticket can be closed when they are (if you have also documented that it's fixed.


---

Comment by dsm created at 2011-02-24 01:38:10

`@`kcrisman: okay, understood.  Will propose under #1173.


---

Comment by kcrisman created at 2011-12-19 17:59:02

If #1173 isn't going to happen anytime soon because of #11513, a very simple patch here would be nice.  It would document

```
sage: solve(erf(x)==0,x)
[x == 0]
```

as mentioned above already works, and take care of the issue in the summary, of course.


---

Comment by benjaminfjones created at 2012-01-09 17:19:34

I think the right thing to do here is to depend on #11513. There are several ways one could address the issue in the summary about erf(0) not returning 0, but when a good patch for 11513 appears, the code being touched here would need to be changed again.


---

Attachment

make erf(0) return 0


---

Comment by benjaminfjones created at 2012-02-12 06:36:41

Changing status from new to needs_review.


---

Comment by benjaminfjones created at 2012-02-12 06:36:41

I uploaded a simple patch now that #11513 is merged.


---

Comment by dsm created at 2012-02-13 02:26:44

Looks good, but I think we should return a Sage zero (or at least match the type):


```

sage: erf(0)
0
sage: parent(erf(0))
<type 'int'>

```



---

Comment by benjaminfjones created at 2012-02-13 04:32:08

That's a good point, this patch addresses the issue by returning the input `x` instead of 0 when a python 0 would have been returned in the previous patch.


```
sage: erf(0)
0
sage: type(erf(0))
<type 'sage.rings.integer.Integer'>
sage: parent(erf(0))
Integer Ring
```



---

Attachment

make erf(0) return 0


---

Comment by dsm created at 2012-02-13 05:12:52

Okay, looks good to me (or at least none of my obvious tricks could break it).


---

Comment by burcin created at 2012-02-13 09:44:00

Thanks for the patch Benjamin. It looks great and gets the job done. However, I'd be much happier if there were a couple more doctests. There are quite a few branches in the new `_eval_()` function, but the patch adds only one doctest.

One more suggestion: It might be better to leave the last `return None` statement outside the `if`s. IMHO, the following is more compact and readable.


```
if not isinstance(x, Expression): 
    if is_inexact(x): 
        return self._evalf_(x, parent=parent(x)) 
    elif x == 0: 
        return x 
elif x.is_trivial_zero(): 
        return x 
return None 
```



---

Comment by kcrisman created at 2012-02-13 18:22:28

Replying to [comment:11 dsm]:
> Looks good, but I think we should return a Sage zero (or at least match the type):
Is this what you were referring to at comment:2:ticket:10133, dsm?

More generally, does anyone think the present way of ensuring `erf(0)` returns an Integer (or even Symbolic Expression) is a good one for #10133?  Or is it better to address this at the Pynac level?


---

Comment by benjaminfjones created at 2012-02-14 05:22:03

Replying to [comment:15 burcin]:
That's a good suggestion. I modified the `_eval_` method accordingly and added several doctests verifying that all branches are reached. Maybe that's overkill, but it took me a while to find an input that actually reached the `x.is_trivial_zero()` branch.


---

Comment by burcin created at 2012-02-14 10:45:00

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2012-02-14 10:45:00

Replying to [comment:17 benjaminfjones]:
> Maybe that's overkill, but it took me a while to find an input that actually reached the `x.is_trivial_zero()` branch.

It's not overkill at all, after adding _a_ doctest to every function, perhaps we will measure the coverage in terms of percentage of lines executed with those tests. Thanks for spending the time and giving this function 100% coverage. :)

BTW, `erf(SR(0))` should be a simple way of hitting the `is_trivially_zero()` branch.


---

Attachment

make erf(0) return 0, with added doctests and simplified branching in _eval_


---

Comment by benjaminfjones created at 2012-02-14 16:53:54

Ok, I simplified that last doctest in `_eval_`.


---

Comment by jdemeyer created at 2012-02-22 10:44:00

Resolution: fixed
