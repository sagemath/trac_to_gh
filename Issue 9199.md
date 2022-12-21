# Issue 9199: plot(..., fill=False) still turns on filling

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-10 01:14:40

Assignee: jason, was

CC:  kcrisman

Try `plot(x^2,(x,-1,1), fill=False)`.


---

Comment by kcrisman created at 2010-07-27 17:49:05

Right, because `fill=None` is the current default.  This should be very easy to fix.


---

Comment by kcrisman created at 2010-07-27 17:49:05

Changing keywords from "" to "beginner".


---

Comment by ryan created at 2010-08-03 06:27:05

make "fill=False" work.


---

Comment by ryan created at 2010-08-03 06:34:10

Changing status from new to needs_work.


---

Attachment

here is the patch that fixes the fill=False issue.  It breaks fill=None (however, fill=None isn't really that natural).

Interesting issue...when running the doctests for this patch, the doctest timed out and then crashed.
---------------------------------------
Trying:
plot(x**Integer(3),(x,Integer(1),Integer(2))) # this one does not###line
2276:_sage_ >>> plot(x^3,(x,1,2)) # this one does not
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
[361.7 s]
--------------------------------------- 
when plotting this in sagenb, it works fine.


---

Comment by ryan created at 2010-08-03 06:35:55

Oops, here it is with better formatting.


```
---------------------------------------
Trying:
plot(x**Integer(3),(x,Integer(1),Integer(2))) # this one does not###line
2276:_sage_ >>> plot(x^3,(x,1,2)) # this one does not
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
[361.7 s]
--------------------------------------- 
```



---

Comment by kcrisman created at 2010-08-03 15:07:31

This could come from the change somehow.  

More important is whether anyone relies somewhere else in the code on fill=None as working.  There should be a way to handle both of these - catch fill=False and then rename fill to None, for instance.  What do you think?


---

Comment by ryan created at 2010-08-03 15:16:57

well...about sage -t.  Every doctest I run crashes (they all time out and then crash at about 360 seconds).  It even crashes with my sage-main branch (which is my clean sage 4.5.1).  It's strange because with my last patch, the doctests work fine.  I'll try undoing the changes and see it changes anything.

As far as handling fill both False and None, not anything big.
just need to change 

```
if fill is not False:

to

if fill is not False and fill is not None:
```


I originally had it the second way, but I removed in the hopes that it would fix the doctest crashes (it didn't).

I'll add it back as soon as I get back to my sage computer.


---

Attachment

update: fill=None works too!


---

Comment by ryan created at 2010-08-28 18:22:51

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-08-29 02:45:55

How did you get that second patch (i.e., how did you generated whatever you posted as the patch)?  It seems to be two patches concatenated together.  When I apply it, I don't get the "fill=None works again" behavior or piece of code.


---

Attachment

Rebased to 4.5.2; apply only this patch


---

Comment by jason created at 2010-08-29 02:54:42

I rebased your patch (your patch had the default color to be rgbcolor=(0,0,0) for some reason), and combined your two patches into one patch.  However, when I do:


```
plot(x^2,(x,-1,1), fill=None)

```


I get filling (where I didn't before the patch).


---

Comment by jason created at 2010-08-29 02:54:42

Changing status from needs_review to needs_work.


---

Comment by ryan created at 2010-09-11 05:20:39

Updated patch (with Sage 4.5.3)


---

Attachment

Replying to [comment:8 jason]:
> I rebased your patch (your patch had the default color to be rgbcolor=(0,0,0) for some reason), and combined your two patches into one patch.  However, when I do:
> 
> {{{
> plot(x^2,(x,-1,1), fill=None)
> 
> }}}
> 
> I get filling (where I didn't before the patch).

Updated patch should fix this.


---

Comment by ryan created at 2010-09-11 05:26:14

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-11 16:21:02

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-11 16:21:02

Looks good!  Thanks!

Apply only trac_9199_plot_fill.3.patch

Karl-Dieter: if you reviewed this patch too, add your name to the list.


---

Comment by jason created at 2010-09-11 16:22:49

Note that this is Ryan's first contribution (along with #8838 and #7154)


---

Comment by mpatel created at 2010-09-15 10:40:35

Resolution: fixed
