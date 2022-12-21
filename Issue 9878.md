# Issue 9878: allow preventing automatic evaluation of symbolic expressions (hold)

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-09-09 08:46:26

Assignee: burcin

Keywords: pynac

Symbolic expressions automatically evaluate themselves to simplify the data structures, representation, etc. For example,


```
sage: x+x
2*x
sage: x*x
x^2
```


The ability to disable this evaluation is a feature requested very often.


---

Attachment

With attachment:trac_9879-hold.patch and the new pynac package at #9201, one can do:


```
sage: x.add(x,(x+1), hold=True)
x + x + (x + 1)
sage: sin(pi, hold=True)
sin(pi)
```


The pynac package includes patches for #9394, #9834, #9878, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.


---

Comment by burcin created at 2010-09-12 12:17:49

Changing status from new to needs_review.


---

Comment by burcin created at 2010-09-12 12:27:11

Replying to [comment:1 burcin]:
> With attachment:trac_9879-hold.patch and the new pynac package at #9201

at #9901. Sorry for the noise.


---

Comment by kcrisman created at 2010-09-29 18:59:59

A question arises in reviewing:

```
>> Do all the holds in the Pynac code (such as ``return
>> conjugate_function(asin(x)).hold();``) prevent someone from ever
>> evaluating these?  I just don't know how it works.
>
> The hold() function sets the evaluated flag of a basic object in
> GiNaC. The automatic evaluation is skipped if this flag is set. Perhaps
> the duplicate() method ignores this, I'm not sure.
>
> In any case, we should provide a method to force this evaluation, but
> this should be on a separate ticket. Also see my comments below about
> this.

```

This is now #10034.


---

Comment by kcrisman created at 2010-09-29 19:08:40

Making a context for holding is now #10035.


---

Attachment

Apply after initial patch


---

Comment by kcrisman created at 2010-10-04 15:10:07

This still needs review, just because the review patch itself is so long. I've added myself as author, but obviously I didn't do much Pynac - just trying to document thoroughly - so if someone disagrees they can change that.  

Burcin, can you review this?  With this I pass all doctests.

Also, here are some issues which I believe should NOT be addressed here, but need to be on followup tickets.  My philosophy here is that mathematically correct brand-new functionality can be merged even if there are enhancements to it needed.   This ticket shouldn't be closed until new tickets are opened for these issues.

 * Typesetting issues. There is nothing mathematically wrong with these (you can try it), but they are obviously confusing to users.  

```

sage: i.mul(2)
2*I
sage: i.mul(2,hold=True)
2*I*
sage: i.mul(2,hold=True).simplify()
2*I
sage: i.mul(i)
-1
sage: i.mul(i,hold=True)
-
sage: i.mul(i,hold=True).simplify()
-1
```


 * `heaviside(0) != SR(0).step()` This is already true in Sage, so we don't need to address in this ticket, but it becomes obvious when trying to simplify a 'held' expression with `step()`.

 * There is no way to get `Order(hold=True)` to evaluate!  Same problem with `csgn` and `step` (the latter could be fixed via the above).  This is annoying but probably they are still useful.

 * Big problem, which is why I didn't make log_gamma symbolic:

```
sage: log_gamma(i).n()
-0.0219785471672303 - 0.168184318273662*I
sage: log_gamma(pari(i))
-0.650923199301856 - 1.87243664726243*I
(%i3) ev(log_gamma(%i),numer);
(%o3)             - 1.872436647262428 %i - .6509231993018556
```

So no new error has been introduced with this patch, but it exposed this Pynac difference/bug.

 * Enhancement - coth, sech, csch and their arc-guys basically already are purely symbolic and hold doesn't do much for them.  For instance:

```
sage: cosh(0)
1
sage: sech(0)
sech(0)
```

So we should do something about that.  But Maxima knows:

```
sage: sech(0).simplify()
1
```


 * Here is something where I was able to make it work in the doctests, but honestly don't know what is going on.

```
sage: I.log(hold=True).simplify()
1/2*I*pi
sage: var('I')
I
sage: I.log(hold=True).simplify()
log(I)
sage: restore('I')
sage: I.log(hold=True).simplify()
log(I)
```

This turns out to cause trouble in doctests.  I don't know why this happens.


---

Comment by jpflori created at 2010-10-05 11:02:52

Changing status from needs_review to positive_review.


---

Comment by jpflori created at 2010-10-05 11:02:52

I ran the doctests and looked at the patch.
Everything looks fine.
Maybe at line 392 of sage/functions/hyperbolic.py you changed "WARNING:" to ".. warning::" but Sage doc (http://www.sagemath.org/doc/developer/conventions.html) encourages to use uppercase, so ".. WARNING::" could be used.
Nothing important however.

Other unrelated problems, I'll try to report :

-By the way there is a problem within http://www.sagemath.org/doc/developer/conventions.html.
It says to use ".. NOTE:" and there is "NOTES:" in the example.
There is also nothing about "TESTS:" section which is often used.
The reccurent use of ".. blah ::", "::" and "sage: " could also be documented or point to the corresponding pages of Sphynx doc (even if looking at the examples is of course the best way to go and looking through Sphynx doc explains many things).

- In sage/symbolic/relation.py inside a warning block a "{ does }" should be replaced by "*does*"


---

Comment by kcrisman created at 2010-10-05 13:11:14

Replying to [comment:6 jpflori]:
> I ran the doctests and looked at the patch.
> Everything looks fine.

Great, thanks!  

Do you mind putting your "real" name in the "reviewer" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.

> Maybe at line 392 of sage/functions/hyperbolic.py you changed "WARNING:" to ".. warning::" but Sage doc (http://www.sagemath.org/doc/developer/conventions.html) encourages to use uppercase, so ".. WARNING::" could be used.
> Nothing important however.

Huh - I just did `search_src('warning')` and LOTS of things came up in exactly this way.  That should probably be a global ticket, I agree. 

> Other unrelated problems, I'll try to report :
> 
> -By the way there is a problem within http://www.sagemath.org/doc/developer/conventions.html.
> It says to use ".. NOTE:" and there is "NOTES:" in the example.
> There is also nothing about "TESTS:" section which is often used.
> The reccurent use of ".. blah ::", "::" and "sage: " could also be documented or point to the corresponding pages of Sphynx doc (even if looking at the examples is of course the best way to go and looking through Sphynx doc explains many things).
Yes, open a ticket and cc: mvgnu and jhpalmieri on it, who both seem to understand Sphinx and would at least have comments on it.
> - In sage/symbolic/relation.py inside a warning block a "{ does }" should be replaced by "*does*"
This would have priority "trivial", I think ;)


---

Comment by kcrisman created at 2010-10-05 13:59:56

>  * Typesetting issues. There is nothing mathematically wrong with these (you can try it), but they are obviously confusing to users.  
This is now #10069.
> 
>  * `heaviside(0) != SR(0).step()` This is already true in Sage, so we don't need to address in this ticket, but it becomes obvious when trying to simplify a 'held' expression with `step()`.
This is now #10070.
>  * There is no way to get `Order(hold=True)` to evaluate!  Same problem with `csgn` and `step` (the latter could be fixed via the above).  This is annoying but probably they are still useful.
This is now #10071.
>  * Big problem, which is why I didn't make log_gamma symbolic:
This is now #10072, and making `log_gamma` symbolic is #10075.
>  * Enhancement - coth, sech, csch and their arc-guys basically already are purely symbolic and hold doesn't do much for them.  For instance:
This is now #10074.
> 
>  * Here is something where I was able to make it work in the doctests, but honestly don't know what is going on.
This is now #10073.


---

Comment by kcrisman created at 2010-10-05 15:52:22

> Do you mind putting your "real" name in the "reviewer" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.

Okay, I found your name on an email from Burcin on sage-devel - hope you don't mind :)  But you should still add yourself to the list on the main page.  Thanks!


---

Comment by jpflori created at 2010-10-05 20:47:50

Replying to [comment:7 kcrisman]:

> Do you mind putting your "real" name in the "reviewer" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.

Done, I thought I already put it somewhere at some point...

> Huh - I just did `search_src('warning')` and LOTS of things came up in exactly this way.  That should probably be a global ticket, I agree.

This is now ticket #10078.

> Yes, open a ticket and cc: mvgnu and jhpalmieri on it, who both seem to understand Sphinx and would at least have comments on it.

This is now ticket #10077.

> This would have priority "trivial", I think ;)

This is now #10079 (with a "patch" provided).


---

Comment by kcrisman created at 2010-10-06 01:47:38

Speaking of these doc issues, when reading through the doc in symbolic/expression.pyx I realized that there were some pre-existing problems in the html documentation.  This is now #10080.

11 out of 12 consecutive tickets all as followups from one ticket... this must be a good ticket ;)  Or at least well-proofread, since nearly all of these things have nothing to do with the ticket per se, but were discovered while reviewing it.


---

Comment by mpatel created at 2010-10-06 03:20:12

Resolution: fixed
