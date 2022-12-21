# Issue 9988: easier access to operands of a symbolic expression

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-09-23 22:07:51

Assignee: burcin

CC:  jpflori

Attached patch adds an `op` attribute to symbolic expressions which gives easy access to its operands. We now have:


```
sage: x,y,z = var('x,y,z')
sage: e = x + x*y + z^y + 3*y*z; e
x*y + 3*y*z + z^y + x
sage: e.op[1]
3*y*z
sage: e.op[1,1]
z
sage: e.op[-1]
x
sage: e.op[1:]
[3*y*z, z^y, x]
```


Using `__getitem__()` directly was not an option since it breaks conversion to numpy.


---

Comment by burcin created at 2010-09-23 22:09:59

Changing status from new to needs_review.


---

Attachment


---

Comment by kcrisman created at 2010-09-24 14:44:47

This looks like a good addition, after many sage-support queries - great!    I hope to be able to review this eventually, though it will take some time because I am not a Cython expert and would want to be very careful.

What is the `property` thing in Python/Cython?  I haven't heard of that before (as opposed to `def` or `cdef` or `class`).

Does this depend at all on any of the Pynac 0.2.1 tickets' patches?


---

Comment by burcin created at 2010-09-24 15:19:33

Replying to [comment:2 kcrisman]:
> What is the `property` thing in Python/Cython?  I haven't heard of that before (as opposed to `def` or `cdef` or `class`).

I also found out about it while looking through the Sage library code for a way to make `numpy` work when I define `__getitem__()`:

http://docs.cython.org/src/userguide/extension_types.html#properties

The function defined by `__get__()` is run when you access that property. This makes the syntax look much cleaner. You don't need to put `()` at the end any more, compared to the syntax needed for `.operands()`.
 
> Does this depend at all on any of the Pynac 0.2.1 tickets' patches?

No, it should be independent. Though I admit that there are a bunch of symbolics patches before this on my queue.


---

Comment by robertwb created at 2010-12-16 16:23:13

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-12-16 16:23:13

The error "TypeError: cannot index numeric, constant or symbol" is rather obscure, better to make it something like "... has no operands."

Any reason why expr.op isn't just a plain list?


---

Comment by burcin created at 2011-03-23 11:18:44

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2011-03-23 11:18:44

Replying to [comment:5 robertwb]:
> The error "TypeError: cannot index numeric, constant or symbol" is rather obscure, better to make it something like "... has no operands."

Done. The new message is: "expressions containing only a numeric coefficient, constant or symbol have no operands"

> Any reason why expr.op isn't just a plain list?

I wanted to avoid traversing the vector storing the operands and creating a python object for each. A list wouldn't allow nested indexing either:


```
sage: x,y,z = var('x,y,z')
sage: e = x + x*y + z^y + 3*y*z; e
x*y + 3*y*z + z^y + x
sage: e.op[1]
3*y*z
sage: e.op[1,1]
z
```


This syntax was proposed in a discussion at Sage days 24 last summer.


Apply trac_9989-operands.take2.patch


---

Comment by kcrisman created at 2011-03-23 11:51:39

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2011-03-23 11:51:39

Replying to [comment:6 burcin]:
> Replying to [comment:5 robertwb]:
> > The error "TypeError: cannot index numeric, constant or symbol" is rather obscure, better to make it something like "... has no operands."
> 
> Done. The new message is: "expressions containing only a numeric coefficient, constant or symbol have no operands"
> 
I think that the part in expression.pyx still has this syntax, and I agree that it is confusing.  Putting 'needs info' just in case that is intentional.


---

Attachment


---

Comment by burcin created at 2011-03-23 12:06:39

Changing status from needs_info to needs_review.


---

Comment by burcin created at 2011-03-23 12:06:39

Replying to [comment:7 kcrisman]:
> Replying to [comment:6 burcin]:
> > Replying to [comment:5 robertwb]:
> > > The error "TypeError: cannot index numeric, constant or symbol" is rather obscure, better to make it something like "... has no operands."
> > 
> > Done. The new message is: "expressions containing only a numeric coefficient, constant or symbol have no operands"
> > 
> I think that the part in expression.pyx still has this syntax, and I agree that it is confusing.  Putting 'needs info' just in case that is intentional.

Good catch! I forgot to change that message. Updated patch attached, with same name.


---

Comment by kcrisman created at 2011-03-23 12:47:52

Is the `normalize_index()` business needed because cdef'd things don't accept appropriate negative indices or something?  I get what it does, I don't get why it's necessary.  Maybe because of the potential for multiple indices to get suboperands?

Slowly working my way through it... Cython not being my forte... but looks good so far.


---

Comment by kcrisman created at 2011-03-23 12:52:02

There is no doctest for

```
ind_err_msg = "index should either be a slice object, an integer or a list of integers"
```

And you might as well just use `ind_err_msg` in line 139 instead of typing it again.


---

Comment by kcrisman created at 2011-03-23 15:14:24

So far looks good - thanks to [a little help](http://stackoverflow.com/questions/2936863/python-implementing-slicing-in-getitem) and [the Ginac refs](http://www.ginac.de/tutorial/Information-about-expressions.html).  

Questions, though.
 * Regarding the error message:

```
sage: f = 3*x^2+2*sin(x)-32*sin(ln(x))
sage: f.op[3]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
IndexError: operand index out of range, got 3, expect between -3 and 3
```

   Is this really the error message we want?  Here it's the 'exclusive' between, but that could be confusing.  Maybe it should say between -3 and 2 (length ops -1)?  

 * Next, I wonder whether the following can be supported:

```
sage: f.op[2:3,3]
TypeError: an integer is required
```

   since matrices can do this

```
sage: M = matrix(4,range(16))
sage: M[2:3]
[ 8  9 10 11]
sage: M[2:3,3]
[11]
```

   The current code ends everything if it's a slice; you just get the operands at that level.  But it would be interesting to get the 2nd element of each operand, though perhaps not very useful since you might not know what it is ahead of time.  But perhaps for very regular expressions (Christoffel symbol-type surfeit of indices?) it could be useful.  We might also want something like `sage: M[2:3,3:4]` to be supported, such as `sage: f.op[2,0:1]` instead of having to do 

```
sage: f.op[2].op[0:1]
[sin(log(x))]
```

   But maybe going back and forth between Ginac and Sage in the way you'd have to for that is tricky.
 * Here is something needed for sure:

```
sage: f = 3*x^2+2*sin(x)-32*sin(ln(x))
sage: f[1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
TypeError: 'sage.symbolic.expression.Expression' object does not support indexing
sage: search_src('does not support indexing')
<no response>
```

   We should have at least one doctest _somewhere_ that tests this.

But overall the code is correct for the promised functionality and passes its tests, documented pretty well _if_ you know enough about !GEx etc.  So I would say good work, needs work for the last item above and probably the first, and needs info for the second item (matrix-style slices).


---

Comment by kcrisman created at 2011-03-23 15:14:24

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2011-05-31 13:28:14

Thank you for the thorough reviews. I appreciate the feedback and it's certainly good for someone to look over my changes, since there are often rough edges I fail to see after staring at the code for a while.

Replying to [comment:11 kcrisman]:

> Questions, though.
>  * Regarding the error message:
> {{{
> sage: f = 3*x^2+2*sin(x)-32*sin(ln(x))
> sage: f.op[3]
> ---------------------------------------------------------------------------
> IndexError                                Traceback (most recent call last)
> IndexError: operand index out of range, got 3, expect between -3 and 3
> }}}
>    Is this really the error message we want?  Here it's the 'exclusive' between, but that could be confusing.  Maybe it should say between -3 and 2 (length ops -1)?  

Fixed.

>  * Next, I wonder whether the following can be supported:
> {{{
> sage: f.op[2:3,3]
> TypeError: an integer is required
> }}}
>    since matrices can do this
> {{{
> sage: M = matrix(4,range(16))
> sage: M[2:3]
> [ 8  9 10 11]
> sage: M[2:3,3]
> [11]
> }}}
>    The current code ends everything if it's a slice; you just get the operands at that level.  But it would be interesting to get the 2nd element of each operand, though perhaps not very useful since you might not know what it is ahead of time.  But perhaps for very regular expressions (Christoffel symbol-type surfeit of indices?) it could be useful.  We might also want something like `sage: M[2:3,3:4]` to be supported, such as `sage: f.op[2,0:1]` instead of having to do 
> {{{
> sage: f.op[2].op[0:1]
> [sin(log(x))]
> }}}
>    But maybe going back and forth between Ginac and Sage in the way you'd have to for that is tricky.

The output is a list if the index is a slice. We could pass further indices to the list's `__getitem__()` of course, though I'm not convinced this convenience is really a good feature.

>  * Here is something needed for sure:
> {{{
> sage: f = 3*x^2+2*sin(x)-32*sin(ln(x))
> sage: f[1]
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> TypeError: 'sage.symbolic.expression.Expression' object does not support indexing
> sage: search_src('does not support indexing')
> <no response>
> }}}
>    We should have at least one doctest _somewhere_ that tests this.

I added a test in the docstring for `__get__` in `expression.pyx`.


For patchbot:

Apply trac_9989-operands.take3.patch


---

Comment by burcin created at 2011-05-31 13:28:14

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-06-08 20:28:19

Changing status from needs_review to positive_review.


---

Attachment


```
Hunk #2 succeeded at 2476 with fuzz 1 (offset -32 lines).
```


I certainly don't have time to reread this whole patch again, so _assuming_ that the only changes are the ones mentioned, then tests pass, changes are good, explanation of second point is sufficient, good to go.


---

Comment by fbissey created at 2011-06-12 23:17:26

*cringe* I am ready to write some documentation if that gets people to use SAGE_LOCAL and SAGE_INC and all the other variables defined in module_list.py

```
numpy_depends = [SAGE_LOCAL + '/lib/python/site-packages/numpy/core/include/numpy/_numpyconfig.h']

flint_depends = [SAGE_LOCAL + '/include/FLINT/flint.h']
singular_depends = [SAGE_LOCAL + '/include/libsingular.h']
ginac_depends = [SAGE_LOCAL + '/include/pynac/ginac.h']
```

 rather than 

```
SAGE_ROOT + "/local/include/pynac/ginac.h"
```

and other combinations of SAGE_ROOT + "/local..."


---

Comment by burcin created at 2011-06-13 17:15:45

Good catch. Thanks, Francois.

I uploaded a new patch that just changes `module_list.py` to use `SAGE_LOCAL` instead of `SAGE_ROOT`.

Francois, why don't you open a ticket to rename `SAGE_ROOT` in `module_list.py` to something like `SAGE_ROOT_DO_NOT_USE` with a comment above it to point out why `SAGE_LOCAL` is better.


---

Comment by fbissey created at 2011-06-13 19:04:06

Actually you could have used the ginac_depends variable. But your suggestion is good I can make it a part of #11377. I think I may try to write a little bit about these variables in the manual.


---

Attachment

Apply trac_9989-operands.take4.patch


---

Comment by vbraun created at 2011-06-14 00:42:45

Changing keywords from "" to "sd31".


---

Comment by vbraun created at 2011-06-14 00:42:45

By private communication, I asked Burcin to change the `_repr_()` of the operand wrapper to just `Operands of x^2`. I think its looks great now.


---

Comment by jdemeyer created at 2011-06-14 17:29:33

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-06-14 17:30:47

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-06-14 17:30:47

Somebody should review the new patch... (I am not sure whether Volker's comment "I think its looks great now." means a formal positive_review)


---

Comment by vbraun created at 2011-06-14 17:40:01

Yes, positive review!


---

Comment by vbraun created at 2011-06-14 17:40:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-15 15:23:46

Resolution: fixed
