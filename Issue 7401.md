# Issue 7401: Derivative at a point is not translated into Maxima

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2009-11-06 10:53:17

Assignee: was

CC:  eviatarbach

Keywords: derivative, at, maxima

Alex reported [http://groups.google.cz/group/sage-support/browse_thread/thread/81b96a7731600ec2](http://groups.google.cz/group/sage-support/browse_thread/thread/81b96a7731600ec2) this bug (see the link for short discussion related to the problem)

```
Hi all:

I found some strange behavior in solve that's related to function
composition.  Check out this short example.

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('x,t')
(x, t)
sage: f= function('f',x)
sage: e= {x:exp(t)}
sage: ft= f.subs(e); ft
f(e^t)
sage: Ft = t^2 + ft^2; Ft
t^2 + f(e^t)^2
sage: a= diff(Ft,t); a
2*e^t*f(e^t)*D[0](f)(e^t) + 2*t
sage: solve(a==0,diff(f,x).subs(e))
[D[0](f)(t) == -t*e^(-t)/f(e^t)]
| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
Did you spot the strangeness?  Somehow diff(f,x).subs(e) became diff
(f,x).subs({x:t}) after solving.  Does anybody know how to fix this?

Alex 

```



---

Attachment

apply together with the patch for #385 (if necessary)


---

Comment by robert.marik created at 2009-11-06 10:58:39

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-11-06 10:58:39

Submitted patch solves the problem described above

limitation and disadvantage of this patch are:

* it works for univariable functions only

* introduces new dummy variable into Maxima session

All comments are welcomed and any help appretiated


---

Comment by kcrisman created at 2009-11-10 15:20:41

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-11-10 15:20:41

Replying to [comment:1 robert.marik]:
> Submitted patch solves the problem described above
> 

Yes, this should do so.  It would probably be best to add one more doctest, just to show that the original one works (i.e. without showing the Maxima internals). 

> limitation and disadvantage of this patch are:
> 
> * it works for univariable functions only

That's fine - that's still improving the previous situation, correct?  Looking at the code, it would be helpful to know what happens if params has more than one element - particularly in 

```
return "at(diff('%s(dummy_var_der), %s),dummy_var_der=%s)"%(f.name(), ", ".join(params), opnds[0]) 
```

it seems like one could have more items in the substitution tuple than there are %s to fill up, even if for some reason len(args)==1.  What is the relation between args and params - could there be more params than args?

Also, make sure to add a doctest showing that the NotImplementedError comes into play.  Search for 'Traceback' in the file to see how the doctests for errors look.

> 
> * introduces new dummy variable into Maxima session

This is unfortunate, but probably unavoidable currently.  You should test whether this breaks anything in Maxima, but I don't see why it would.


---

Comment by jason created at 2009-11-10 16:24:42

Also, there needs to be a blank line after "TESTS::" for documentation formatting.


---

Comment by robert.marik created at 2009-11-12 14:48:24

Replying to [comment:2 kcrisman]:
> This is unfortunate, but probably unavoidable currently.  You should test whether this breaks anything in Maxima, but I don't see why it would.


Perhaps we can use variable from f.variables() instead of introducing dummy variable.


---

Comment by kcrisman created at 2009-11-12 15:48:30

Why not see if that works, then update the patch?  One might have to be careful in testing for how many variables/args there are.  I am never clear on the difference between those two things, anyway, in Sage.


---

Comment by robert.marik created at 2009-11-13 12:29:16

Replying to [comment:5 kcrisman]:
> Why not see if that works, then update the patch?  One might have to be careful in testing for how many variables/args there are.  I am never clear on the difference between those two things, anyway, in Sage.

My suggestion related to f.variables() does not work, since I cannot acces the variables inside the function derivative. 

The original patch does not work for something like diff(f(x,y),x).subs(x=3) so I updated it and tested for various combination how many variables are in the function, how many variables appear at the resulting expression, how many variables are substituted etc.

Perhaps could be improved for multivariable functions, but Maxima expression "at (expr, [eqn_1, ..., eqn_n])" cannot be translated to current Sage and both issues should be fixed together. Perhaps in this ticket? (leaving as needs_work, despite the fact that the original problem has been fixed and doctested)


---

Attachment

Apply only this patch.


---

Comment by kcrisman created at 2009-11-13 13:51:02

> Perhaps could be improved for multivariable functions, but Maxima expression "at (expr, [eqn_1, ..., eqn_n])" cannot be translated to current Sage and both issues should be fixed together. Perhaps in this ticket? (leaving as needs_work, despite the fact that the original problem has been fixed and doctested)

Can you give an example of Sage command -> Maxima command -> Maxima output that would give rise to such a situation?  That should make it fairly straightforward to change the at function appropriately.


---

Comment by robert.marik created at 2009-11-16 10:30:42

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2009-11-16 10:30:42

Replying to [comment:7 kcrisman]:
> 
> Can you give an example of Sage command -> Maxima command -> Maxima output that would give rise to such a situation?  That should make it fairly straightforward to change the at function appropriately.

I thought that this happens for taylor polynomial in more variables. However, it is not the case (btw. taylor polynomial in more variables seem to be not supported in Sage and I submited patch for #7472).

Hence I think that the problem is patched and if someone finds situation where she/he needs to enhace the functionallity, this can be solved in another ticket.


---

Comment by robert.marik created at 2009-11-17 14:43:15

The patch fixes also #6376.


---

Comment by kcrisman created at 2009-11-17 16:04:53

Okay, positive review, and all relevant tests pass.  It is not optimal because of the dummy variable, one variable, etc., but it fixes things and there are open tickets (some with patches!) for making it even better.  Great.  I will also put a comment on #6376.


---

Comment by kcrisman created at 2009-11-17 16:04:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-19 17:44:22

Resolution: fixed


---

Comment by mhansen created at 2009-11-22 05:30:20

This causes a failure in sage/interfaces/maxima.py with this example


```
maxima(derivative(ceil(x*y*d), d,x,x,y))
```


since multivariate derivatives are not supported.


---

Comment by mhansen created at 2009-11-22 07:27:24

I've backed this out for now.


---

Comment by mhansen created at 2009-11-22 07:27:24

Changing status from closed to needs_work.


---

Comment by nbruin created at 2014-12-05 04:53:11

Changing status from needs_work to needs_review.


---

Comment by nbruin created at 2014-12-05 04:53:11

On sage 6.5beta1 I get

```
sage: solve(a==0,diff(f,x).subs(e))
[D[0](f)(e^t) == -t*e^(-t)/f(e^t)]
```

so I think this problem has been resolved. Do we close it as (now) invalid?


---

Comment by pbruin created at 2014-12-05 08:06:57

All doctests in the patch now work without the patch, even the ones that were expected to fail.


---

Comment by pbruin created at 2014-12-05 08:06:57

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2014-12-05 14:02:03

Awesome!  I tested this last night but it must have been too late, because I didn't notice it worked. :P

In which case we should _document_ that it is fixed so we don't get bitten if (say) we switch symbolics or something again.


---

Comment by kcrisman created at 2014-12-05 14:02:03

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2014-12-05 14:05:01

As you say, e.g.

```
sage: x,y,=var('x y') 
sage: a = function('f', x, y).diff(x).subs(x=4).subs(y=8) 
sage: b=maxima(a); b         
?%at('diff('f(t0,t1),t0,1),[t0=4,t1=8])
sage: b.sage()
D[0](f)(4, 8)
```

Huh.  Maybe this is a side effect of making symbolic variables unique in Maxima?  Or the library interface?  I bet no one has looked at this for a _long_ time.


---

Comment by pbruin created at 2014-12-05 15:28:07

Changing type from defect to task.


---

Comment by pbruin created at 2014-12-05 15:28:07

Replying to [comment:21 kcrisman]:
> Awesome!  I tested this last night but it must have been too late, because I didn't notice it worked. :P
> 
> In which case we should _document_ that it is fixed so we don't get bitten if (say) we switch symbolics or something again.
Good point, I guess we can just add the doctests from the patch.


---

Comment by pbruin created at 2014-12-05 15:28:07

Changing priority from major to minor.


---

Comment by kcrisman created at 2014-12-05 18:48:38

New commits:


---

Comment by kcrisman created at 2014-12-05 18:48:38

Changing status from needs_work to needs_review.


---

Comment by nbruin created at 2014-12-05 19:09:20

Replying to [comment:24 kcrisman]:
> New commits:
> ||[476d8c4](http://git.sagemath.org/sage.git/commit/?id=476d8c43f23185ea22c46a9b30fd37c9ead46668)||`Add doctests for #7401 about derivatives at a point`||
Two comments:
 * use `a = function('f')(x,y).diff(x)` to avoid the confusing (and hopefully to deprecated) function('f',x,y).
 * perhaps include an example that also tests the behaviour when the auxiliary variables aren't necessary:

```
sage: a = function('f')(x,y).diff(x)
sage: a
D[0](f)(x, y)
sage: maxima(a)
'diff('f(_SAGE_VAR_x,_SAGE_VAR_y),_SAGE_VAR_x,1)
```

since that also illustrates a template how to arrive at more user-friendly printing.


---

Comment by git created at 2014-12-09 01:59:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-12-09 02:00:55

Since you basically wrote all the other tests, adding to authors.


---

Comment by pbruin created at 2014-12-15 14:37:14

The reviewer patch (typesetting, logical ordering of doctests, checking a few more intermediate results) adds/changes nothing essential.


---

Comment by pbruin created at 2014-12-15 14:37:14

Changing status from needs_review to positive_review.
