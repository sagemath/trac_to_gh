# Issue 2607: find_minimum_on_interval() uses the wrong scipy function

Issue created by migration from https://trac.sagemath.org/ticket/2607

Original creator: AlexGhitza

Original creation time: 2008-03-19 22:17:25

Assignee: was

CC:  robert.marik kcrisman

This was reported by Dean Moore on sage-support.  Consider:


```
sage: f(x) = -x*sin(x^2)
sage: f.find_minimum_on_interval(-2.5, 2)
(-1.3076194129914434, 1.35521114057)
sage: f.find_minimum_on_interval(-2.5, -1)
(-2.1827697846777219, -2.19450274985)
```


So find_minimum_on_interval() returns a local minimum as opposed to the global one.  (The same issue applies to find_maximum_on_interval.)  This is due to the fact that the function wraps scipy.optimize.fminbound, which is only a local optimizer (Carl Witty pointed this out).  We should instead use one of the global optimizers, i.e. scipy.optimize.anneal or scipy.optimize.brute.


---

Comment by jwmerrill created at 2008-08-31 14:30:42

Changing component from calculus to numerical.


---

Comment by jwmerrill created at 2008-08-31 15:08:55

Changing component from numerical to calculus.


---

Comment by robert.marik created at 2010-08-25 21:24:54

It seems that there are two global optimizers in scipy: scipy.optimize.anneal and scipy.optimize.brute. Does anybody more experienced in numerics know, which one is better for including into Sage?


---

Comment by jason created at 2010-08-25 22:28:29

Robert, that sounds like a great question for either sage-devel or the scipy list.


---

Comment by kcrisman created at 2011-06-15 21:56:12

This [Scipy tutorial page](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html) should be relevant.  I will try to resolve this soon.


---

Comment by kcrisman created at 2011-06-15 21:56:12

Changing keywords from "" to "sd31".


---

Comment by kcrisman created at 2011-06-16 00:07:53

#5960 was a dup.   Here are the examples from there.

```
sage: h(x) =  -sin(x) - 2*sin(2*x)
sage: h.find_minimum_on_interval(0, 2*pi)
(-1.3271810224585345, 3.8298351449342838)
But there is another local minimum at h(0.8666760871050464) = -2.73581510406


sage: find_minimum_on_interval(x*(x-1)*(x+1), -2, 2)
(-0.38490017945975047, 0.57735026913115706)
The minimum on this interval is the endpoint h(-2) = 6.


sage: find_minimum_on_interval((x-2)*(x-1)*x*(x+1) - x, -2, 2)
(-0.43749999999999994, -0.49999999973911674)

but
sage: find_minimum_on_interval((x-2)*(x-1)*x*(x+1) - x, 0, 2)
(-2.6642135623730949, 1.7071067879138031)
```



---

Comment by kcrisman created at 2011-06-16 00:12:33

The `brent` algorithm will also not work.

```
Triple (a,b,c) where (a<b<c) and func(b) < func(a),func(c). If bracket consists of two numbers (a,c) then they are assumed to be a starting interval for a downhill bracket search (see bracket); it doesn’t always mean that the obtained solution will satisfy a<=x<=c.
```

Which is not the same as constrained minimization, for us.


---

Comment by jwmerrill created at 2011-06-16 00:18:01

It seems like finding a local minimum might be the best you can hope for with a general function. Wouldn't finding an absolute minimum (on an interval) be intractable unless you can exploit some special structure of the function?


---

Comment by kcrisman created at 2011-06-16 00:26:49

Answering the question first...

Sure, but it would be nice if we at least got the 'right' answer for 'easy' functions.  That's all I'm looking for here, not things like finding a minimum on a set of measure zero...

----


I think we can fix Brent to use this.  Compare:

```
sage: optimize.fminbound(h._fast_float_(x),0,6,full_output=True)
(3.8298366870225147, -1.327181022449951, 0, 10)
sage: optimize.fminbound(h._fast_float_(x),0,3,full_output=True)
(0.86667541098916612, -2.7358151040622416, 0, 9)
sage: optimize.brent(h._fast_float_(x),brack=(0,6),full_output=True)
(0.86667608708813437, -2.73581510406422, 11, 12)
```

This shows that brent does give the 'right' answer in this case.   So when does it give a 'wrong' answer?

```
sage: j(x) = sin(x)
sage: optimize.brent(j._fast_float_(x),brack=(0,6),full_output=True)
(10.995574367047061, -0.99999999999999689, 10, 11)
sage: 3.5*pi.n()
10.9955742875643
```

Well, of course - there IS no calculus-style minimum of sin between 0 and pi!  Only a minimum relative to the interval itself.  Interesting that it goes all the way to 7/2*pi, rather than 3/2*pi, but oh well!

So the fix is to switch to Brent, and then if it gives an answer outside the interval, pick the 'lower' endpoint.  This would need lots of testing with well-behaved functions to make sure they actually work correctly.


---

Comment by jwmerrill created at 2011-06-16 00:58:09

Changing assignee from was to jwmerrill.


---

Comment by jwmerrill created at 2011-06-16 00:58:09

But how will you explain to users which functions are 'easy', and when they should expect to get the 'right' answer? I think it's better design to just change the contract of this function to admit that it is only looking for local minima.


---

Comment by kcrisman created at 2011-06-16 01:06:05

It doesn't matter.  Or, at worst, we add some documentation to clarify that.  

The reason it doesn't matter is that this is still _better_ than the other.  Unless you can produce some (natural) examples where optimize.brent does the same.  

The Scipy documentation is not 100% clear on what is done, and it's conceivable they are the same.  It's certainly possible that in fact using optimize.brent in the way I'm suggesting would be just as 'bad' as the previous one, or even essentially equivalent.  But it would be nice to have an explicit example of this before we resort to that.


---

Comment by kcrisman created at 2011-06-16 01:10:59

Here's another example where `brent` does better.

```
sage: j(x) = sin(x^8)-.1*x
sage: optimize.brent(j._fast_float_(x),brack=(0,2),full_output=True)
(2.0000389609484905, -1.2000038913452364, 22, 23)
sage: optimize.fminbound(j._fast_float_(x),0,2,full_output=True)
(1.5288339777087034, -1.152883200877608, 0, 16)
```

Of course, this does cause problems for my supposed algorithm to then go back to an endpoint, since it's _just_ outside of it...


---

Comment by ddrake created at 2012-04-23 01:57:51

I just ran into this bug with the following input:

```
   find_maximum_on_interval(fast_float(8*e^(-x)*sin(x) - 1, x), 0, 8)
    (1.5791755355586754, 0.78539817769603915)

    find_maximum_on_interval(fast_float(8*e^(-x)*sin(x) - 1, x), 0, 9)
    (-0.9951835373923219, 7.0685835435476418)
```

...and was truly surprised that `find_maximum_on_interval` is not monotonic (in the sense that a bigger interval should always give a (weakly) bigger maximum)!

At the VERY LEAST, we should fix the documentation to specify that this finds _local_ extrema, and perhaps change the name of the function, too, since it does _not_ always find the actual maximum value on the interval!

Note that one strange workaround is to simply plot the function; something like:

```
def find_maximum_on_interval(f, a, b):
    return plot(f, a, b).ymax()
```

seems like it would be pretty effective, despite being inelegant and crude!


---

Comment by ddrake created at 2012-05-25 00:47:10

Changing keywords from "sd31" to "sd31, sd40.5".


---

Comment by ddrake created at 2012-05-25 00:47:10

Patch up, please review. I have just changed the documentation and added some suggestions for a workaround using `plot(...).ymin()`. I think we should at least merge something like this right away and worry about fixing the algorithm later.


---

Comment by ddrake created at 2012-05-25 00:47:10

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-05-25 00:55:01

Suggestions in person about how to further enhance the messages in documentation.  Thank you so much for doing this - don't forget to open a followup ticket.


---

Comment by kcrisman created at 2012-05-25 00:55:01

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2012-05-25 02:42:39

I fixed the versions of this function in `symbolic.expression` to specify that they call the `numerical.optimize` version. Please check the documentation; I looked at the bare html, but am working remotely and haven't viewed the result.


---

Comment by ddrake created at 2012-05-25 02:42:39

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2012-05-25 03:34:45

The whitespace patch removes trailing whitespace (and tabs! **TABS**!) from the relevant source files.


---

Comment by kcrisman created at 2012-05-25 03:50:03

Needs work for sentence that doesn't end and `:trac:` thing...


---

Comment by ddrake created at 2012-05-25 05:34:24

apply to Sage library


---

Attachment

Add a "..." to fix doctest on OS X.


---

Comment by zimmerma created at 2012-05-25 07:46:31

should `trac2607.2.patch` be removed?

Paul


---

Comment by zimmerma created at 2012-05-25 08:03:46

after applying both patches on Sage 5.0, I still get:

```
sage: f(x) = -x*sin(x^2)                 
sage: f.find_minimum_on_interval(-2.5, 2)
(-1.3076194129914434, 1.3552111405712108)
```

Did I something wrong?

Paul


---

Comment by dsm created at 2012-05-25 13:15:12

The patch doesn't change the behaviour, it only warns the user that it only returns some local minimum.


---

Comment by zimmerma created at 2012-05-25 13:23:53

Replying to [comment:25 dsm]:
> The patch doesn't change the behaviour, it only warns the user that it only returns some local minimum.

then I don't get any warning (see comment [comment:24]).

Paul


---

Comment by kcrisman created at 2012-05-25 13:26:06

`@`dsm: Correct, and we HAVE to open a new ticket to get something better eventually.  But that turns out to be hard with the current tools.

Hmm, maybe Paul is suggesting we should use the new "system warning that you won't get what you think/mathematically correct result" in Sage whose name I forget?  Paul, the warning is just in the documentation, not the function itself.

I also have a tiny change to this so that the documentation looks better coming up.


---

Comment by kcrisman created at 2012-05-25 13:29:03

Actually, if we need to do more along the lines of warnings, I'll just put it here.  The point is the tilde, as opposed to having the big long thing show up in the doc (while still telling people that it's in another place, which I imagine was the point of not having the tilde before).

```
-Uses :func:`sage.numerical.optimize.find_minimum_on_interval`
+Uses the :func:`~sage.numerical.optimize.find_minimum_on_interval`
+function in the numerical optimization module of Sage.
```



---

Comment by zimmerma created at 2012-05-25 14:10:20

Karl-Dieter, you mean the "stopgap" mechanism?

Paul


---

Comment by kcrisman created at 2012-05-25 14:22:46

I think so.  I've not yet used it, so I don't know if it would be appropriate here.


---

Comment by ddrake created at 2012-05-25 15:42:59

Replying to [comment:23 zimmerma]:
> should `trac2607.2.patch` be removed?

Yes. Or simply ignored.

Replying to [comment:26 zimmerma]:
> then I don't get any warning

The warning is in the documentation, which isn't the best...but it's better than right now, where it's impossible to figure out without reading a lot of code. There will, of course, be a followup ticket that actually fixes the functionality.


---

Comment by zimmerma created at 2012-05-25 18:14:23

I'm not in favour of giving a positive review, since the proposed patch does not solve the problem described in the description of that ticket.

Paul


---

Comment by ddrake created at 2012-05-25 22:09:46

Replying to [comment:32 zimmerma]:
> I'm not in favour of giving a positive review, since the proposed patch does not solve the problem described in the description of that ticket.

Fair enough. However, no one is offerring a fix to the code; it looks like we are going to change the documentation, and then later fix the actual function. This will require two tickets. We could use this ticket for the documentation and a new ticket for the code, or vice versa. We can change the description of this ticket if we want.

The exact way we do this doesn't seem very important to me, as long as we fix the documentation and later fix the code. If you would like to make a new ticket and move attachment:trac2607.patch and attachment:trac2607-whitespace.patch over, that's fine.


---

Comment by benjaminfjones created at 2012-05-26 02:56:19

It seems reasonable to me to fix the docs now, add `stopgap`, and open a new ticket to address the global / local optimization issue; especially given how old this ticket is. In this case the added documentation that refers to "See :trac:`2607`" should be updated to point to the new ticket.


---

Comment by ddrake created at 2012-05-26 17:37:00

Here's a relevant sage-support thread, showing some other problems with these functions: https://groups.google.com/forum/#!topic/sage-support/KCjW5QlB_sA


---

Comment by kini created at 2012-05-26 19:54:13

patchbot: apply trac2607.patch trac2607-whitespace.patch


---

Comment by novoselt created at 2012-05-27 05:07:57

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2012-05-27 05:07:57

I talked to Dan and plan to write the following patch:
 * rename this functions to clearly mark that they compute local extrema;
 * keep old names with deprecation warning and explanation of their behaviour.

Will do it on top of the current patches, so no changes please!


---

Comment by novoselt created at 2012-05-27 05:40:20

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2012-05-27 05:40:20

Apply trac2607.patch trac2607-whitespace.patch trac_2607_renaming.patch


---

Comment by mhansen created at 2012-05-28 19:41:57

According to the patchbot, these patches introduce some trailing whitespace :-)  Otherwise, it looks good to me.


---

Comment by novoselt created at 2012-05-28 19:44:39

Given how many whitespaces were removed, I think these are fine to go...


---

Comment by mhansen created at 2012-05-28 21:10:15

Okay, sounds good to me.  Everything looks good.


---

Comment by mhansen created at 2012-05-28 21:10:15

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-01 09:38:59

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-06-01 09:38:59

Why [attachment:trac2607-whitespace.patch]?  These kind of patches are very annoying for rebasing.  Removing whitespace _from code which you change_ is fine (and even encouraged!), simply removing whitespace all over the place is bad.


---

Comment by novoselt created at 2012-06-01 21:24:24

Hi Jeroen, this patch removes some surprising TABs and I already rebased another patch on top of this whitespace removal, so maybe we can leave it... (Although in general I agree that meddling with whitespaces only complicates life and perhaps patchbot plugin was not such a great idea.)


---

Comment by kini created at 2012-06-01 22:22:18

What's wrong with the patchbot plugin? It only checks whether you added new trailing whitespace. I'm pretty sure everyone agrees you should at least try to avoid doing that.


---

Comment by novoselt created at 2012-06-01 22:37:18

Replying to [comment:44 kini]:
> What's wrong with the patchbot plugin? It only checks whether you added new trailing whitespace. I'm pretty sure everyone agrees you should at least try to avoid doing that.

The problem is that some people get too eager to remove whitespace or insist on patchbot not showing any whitespace mistakes while others don't want to work on new patches if whitespaces are the only issue, and I cannot blame them. I am pretty sure that nobody adds whitespaces on purpose, but having some is not such a problem. Perhaps limiting the overall line length would be better. By the way - will the switch to git help somehow with whitespaces and patches that have conflicts because of them only?


---

Comment by jdemeyer created at 2012-06-01 22:51:14

In any case, this should be rebased to #12950.


---

Comment by ddrake created at 2012-06-07 04:55:17

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2012-06-07 04:55:17

The new whitespace patch now only affects the relevant functions and removes a couple tabs from `expression.pyx`. It's far less invasive. All three relevant patches apply to 5.1.beta2.


---

Comment by novoselt created at 2012-06-07 20:38:02

Changing status from needs_review to positive_review.


---

Comment by aginiewicz created at 2012-06-09 09:05:49

If in this ticket find_maximum_on_interval is renamed to find_local_maximum_on_interval, why not use the change to name it just find_local_maximum and keep it consistent with find_root? After all they both work same:


```
find_root(f, a, b)
find_local_maximum(f, a, b)
```


find_local_maximum_on_interval is 31 characters long, I think that such long names become hard to type. I know, it works on interval, but find_root also looks for root on [a,b] and isn't called find_root_on_interval.


---

Comment by novoselt created at 2012-06-09 18:43:06

Makes sense to me, new patch is attached. Please review!


---

Comment by novoselt created at 2012-06-09 18:43:31

Changing status from positive_review to needs_work.


---

Comment by novoselt created at 2012-06-09 18:43:42

Changing status from needs_work to needs_review.


---

Comment by aginiewicz created at 2012-06-11 10:29:27

Changing status from needs_review to positive_review.


---

Comment by aginiewicz created at 2012-06-11 10:29:27

I'd say it looks good now, applies cleanly, all tests passed, and new name is way easier to remember.


---

Comment by jdemeyer created at 2012-06-18 07:50:20

[attachment:trac2607-whitespace.patch] needs a proper commit message.


---

Comment by jdemeyer created at 2012-06-18 07:51:13

More importantly, this fails on OS X 10.4 ppc with numerical noise:

```
sage -t  --long -force_lib devel/sage/sage/numerical/optimize.py
**********************************************************************
File "/Users/buildbot/build/sage/moufang-1/moufang_full/build/sage-5.1.beta5/devel/sage-main/sage/numerical/optimize.py", line 135:
    sage: find_local_maximum(fast_float(8*e^(-x)*sin(x) - 1, x), 0, 8)
Expected:
    (1.5791755355586754, 0.78539817769603...)
Got:
    (1.5791755355586754, 0.7853981777050254)
GLPK Simplex Optimizer, v4.44
6 rows, 3 columns, 8 non-zeros
Preprocessing...
2 rows, 2 columns, 4 non-zeros
Scaling...
 A: min|aij| =  2.400e+01  max|aij| =  5.000e+01  ratio =  2.083e+00
GM: min|aij| =  8.128e-01  max|aij| =  1.230e+00  ratio =  1.514e+00
EQ: min|aij| =  6.606e-01  max|aij| =  1.000e+00  ratio =  1.514e+00
Constructing initial basis...
Size of triangular part = 2
*     0: obj =  -5.100000000e+01  infeas =  0.000e+00 (0)
*     1: obj =  -5.225000000e+01  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
**********************************************************************
```



---

Comment by jdemeyer created at 2012-06-18 07:58:57

Changing status from positive_review to needs_work.


---

Comment by aginiewicz created at 2012-06-24 10:07:41

patch trac2607-whitespace.patch with commit message


---

Attachment

patch trac_2607_renaming.2.patch rebased on top of trac2607-whitespace.2.patch


---

Attachment

doctest and spacing cleanup


---

Comment by aginiewicz created at 2012-06-24 10:13:11

Changing status from needs_work to needs_review.


---

Attachment

I added the commit message to whitespace patch and rebased renaming patch based on it (keeping original authors/dates, I did not wanted to claim their work and it was minor rebase only to accommodate the commit message taken from comment by Dan).

I also uploaded trac2607-doctest-and-spacing.patch, which adjusts doctest for numerical noise, fixes spacing to be more consistent (3 places, spaces between arguments - i.e. "0,5" looks very close to "0.5" instead of "0, 5") and changed "f.find_local_minimum(" to "find_local_minimum(f" - because after all this test occurs in definition of find_local_minimum function, not method.


---

Comment by novoselt created at 2012-06-25 12:41:00

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2012-06-25 12:41:00

Looks good and all tests pass.


---

Comment by vbraun created at 2012-06-30 18:26:33

Added patch to switch the deprecation to the new syntax.


---

Comment by vbraun created at 2012-06-30 18:28:31

Updated patch


---

Attachment


---

Comment by vbraun created at 2012-06-30 18:31:26

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2012-06-30 18:31:33

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-06-30 19:21:58

Deprecation changes look good to me.


---

Comment by jhpalmieri created at 2012-06-30 19:21:58

Changing status from needs_review to positive_review.


---

Comment by aginiewicz created at 2012-06-30 19:43:43

(and all tests still pass)


---

Comment by aginiewicz created at 2012-07-08 12:19:30

As I understand that ticket moved to sage-pending together with #13109 because it depends on it. But #13109 is back in 5.2 with positive review, so let's move this one back too.


---

Comment by jdemeyer created at 2012-08-01 12:08:41

Resolution: fixed
