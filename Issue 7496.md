# Issue 7496: symbolic variable names should be valid identifiers, or ridiculousness follows

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-20 02:16:09

Assignee: burcin

WTF?


```
sage: var('1')
1
sage: var('1')+1
1 + 1
sage: expand((var('2')+var('2'))^2)
4*2^2
```



---

Comment by burcin created at 2010-01-17 08:29:27

This would be really easy to implement once we have python 3. Apparently, valid identifiers got extended:

http://www.python.org/dev/peps/pep-3131/

String literals also got an `isidentifier()` method.

I don't know how to do this efficiently, while still allowing people to just use α (alpha) as a variable name.


---

Comment by SimonKing created at 2011-03-03 10:31:43

As long as we don't have Python 3, I would try to find a regular expression that does what we need. It is of course easy to write a regular expression that works for ascii strings. But as soon as 'ä' or other language-specific letters are supposed to be considered a variable name, things will become difficult.

I tried

```
sage: import re
sage: _identifiers = re.compile("(?!\d)\w*\Z", re.LOCALE|re.UNICODE)
```


It works for simple cases:

```
sage: _identifiers.match('k_1')
<_sre.SRE_Match object at 0x50d1030>
sage: _identifiers.match('1k')
sage: _identifiers.match('_1k')
<_sre.SRE_Match object at 0x50d1238>
```


But it ignores other letters:

```
sage: print _identifiers.match('ä')
None
```


Perhaps I have misunderstood the effect of `re.LOCALE`? What value should `re.LOCALE` have in order to work with accented letters?


---

Comment by robertwb created at 2011-03-03 21:44:54

Whatever we do, let's be sure to avoid locality dependance on what a valid symbol is. Let's look into back-porting whatever Python3 does, and then falling back to that once we make the transition.


---

Comment by vbraun created at 2011-06-18 04:45:27

Changing status from new to needs_review.


---

Comment by vbraun created at 2011-06-18 04:45:27

Changing keywords from "" to "sd31".


---

Comment by kcrisman created at 2011-06-24 01:29:50

This code should be correct - nice to learn something about the parser and bytecode.  Is this how it's implemented in Python 3 (presumably that's written in C, though)?  I couldn't find it, anyway.

This needs doctests just to document that `var('3')` and `var(' ')` (see #9724) fail, though of course the tests already here document this indirectly.  I'll post a reviewer patch momentarily, assuming I didn't miss something and the patch doesn't actually work.


---

Comment by kcrisman created at 2011-06-24 03:08:02

Ok, I think this is still ok, though I am a little concerned about both of the following being bad:

```
sage: var(' x')
(, x)
```

not good because an empty string is a variable

```
sage: var(' x')
---------------------------------------------------------------------------
ValueError: The name "" is not a valid Python identifier.
```

not good because the intent is clear to make precisely x the variable.  

So is this breaking incorrect but usable behavior? 

```
sage: var("x y  z")
(x, y, , z)
sage: 
```

is similar.

Anyway, I withhold judgment on this.  Reviewer patch attached, but 'needs info' on this.  At the least it seems reasonable to open a new ticket to allow the above behavior - one could easily remove empty strings from the list `names_list` and then complain if there are none left, for instance.


---

Comment by kcrisman created at 2011-06-24 03:08:02

Changing status from needs_review to needs_info.


---

Attachment

Apply after initial patch


---

Comment by kcrisman created at 2011-06-24 03:09:33

Apply [attachment:trac_7496_check_symbolic_variable_names.patch] and [attachment:trac_7496-reviewer.patch].


---

Comment by vbraun created at 2011-06-24 05:10:22

Changing status from needs_info to needs_review.


---

Comment by vbraun created at 2011-06-24 05:10:22

Updated patch splits with any white space and not only on single space:

```
    sage: var(' x y  z    ')
    (x, y, z)
    sage: var(' x  ,  y ,  z    ') 
    (x, y, z)
```

I'm giving the reviewer patch a positive review.


---

Comment by kcrisman created at 2011-06-24 11:24:31

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-06-24 11:24:31

Thanks.  So far it looks good.

But with the original version of the patch (and almost certainly the new one) we get the following doctest error (was letting them run overnight, my apologies):

```
sage -t -long "devel/sage/sage/calculus/desolvers.py"       
**********************************************************************
File "/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py", line 1430:
    sage: sol=desolve_odeint(f,[0.5,2],srange(0,10,0.1),[x,y])
Exception raised:
        sol=desolve_odeint(f,[RealNumber('0.5'),Integer(2)],srange(Integer(0),Integer(10),RealNumber('0.1')),[x,y])###line 1430:
    sage: sol=desolve_odeint(f,[0.5,2],srange(0,10,0.1),[x,y])
      File "/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py", line 1501, in desolve_odeint
        ivar = var(safe_name)
      File "ring.pyx", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)
      File "ring.pyx", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)
      File "ring.pyx", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)
    ValueError: The name "t_[x" is not a valid Python identifier.
**********************************************************************
<snip two failures that result from sol not being defined>
**********************************************************************
File "/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py", line 1446:
    sage: sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=1e-13,atol=1e-14)
Exception raised:
      File "<doctest __main__.example_12[15]>", line 1, in <module>
        sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=RealNumber('1e-13'),atol=RealNumber('1e-14'))###line 1446:
    sage: sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=1e-13,atol=1e-14)
      File "/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py", line 1501, in desolve_odeint
        ivar = var(safe_name)
      File "ring.pyx", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)
      File "ring.pyx", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)
      File "ring.pyx", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)
    ValueError: The name "t_[x" is not a valid Python identifier.
**********************************************************************
File "/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py", line 1470:
    sage: sol=desolve_odeint(f,ci,t,v,rtol=1e-3,atol=1e-4,h0=0.1,hmax=1,hmin=1e-4,mxstep=1000,mxords=17)
Exception raised:
      File "<doctest __main__.example_12[32]>", line 1, in <module>
        sol=desolve_odeint(f,ci,t,v,rtol=RealNumber('1e-3'),atol=RealNumber('1e-4'),h0=RealNumber('0.1'),hmax=Integer(1),hmin=RealNumber('1e-4'),mxstep=Integer(1000),mxords=Integer(17))###line 1470:
    sage: sol=desolve_odeint(f,ci,t,v,rtol=1e-3,atol=1e-4,h0=0.1,hmax=1,hmin=1e-4,mxstep=1000,mxords=17)
      File "/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py", line 1501, in desolve_odeint
        ivar = var(safe_name)
      File "ring.pyx", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)
      File "ring.pyx", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)
      File "ring.pyx", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)
    ValueError: The name "t_[y1" is not a valid Python identifier.
**********************************************************************
```



---

Comment by vbraun created at 2011-06-24 12:14:37

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2011-06-24 12:14:37

Somehow I'm not surprised that somebody used invalid identifiers as variable names ;-)

Updated patch follows.


---

Comment by kcrisman created at 2011-06-24 13:43:08

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-06-24 13:43:08

Replying to [comment:11 vbraun]:
> Somehow I'm not surprised that somebody used invalid identifiers as variable names ;-)

So this actually found a bug of sorts - nice.  Though I have to say that trying to go between the Maxima way of all variables automatic and the Sage way of (nearly) none gave the folks who put that file together quite a challenge, so I don't blame them too much.  But the code is not so elegant, in retrospect.

What's particularly bizarre about this is that in the old and the new cases, `fast_float` is being passed something with three arguments, so it still behaves properly - even though the third thing is an iterable in both cases!  Probably the "right" fix is to just do `'t_'+str(dvar)` for the first dvar only; fast_float just needs something different from the dependent variables.  But I think that would be another ticket, as this doesn't break anything (and the plots still look the same).

Anyway, it fixes the test, doesn't seem to introduce any new bugs.

However, the update to allowing whitespace probably still needs work. Maybe we need to special-case the situation where there is only whitespace in the string passed to `var`:

```
sage: var(' ')
 
sage: a = var(' ')
sage: a
 
sage: type(a)
<type 'sage.symbolic.expression.Expression'>
```


Sorry :(


---

Comment by vbraun created at 2011-06-24 14:34:30

Oh yes good catch, the elements of the empty set (no variable after stripping whitespace) satisfy every property!

Fixed in the updated patch.


---

Comment by vbraun created at 2011-06-24 14:34:30

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2011-06-24 14:34:46

Updated patch


---

Attachment

Updated patch


---

Comment by vbraun created at 2011-06-24 15:35:14

The error message for the "empty variable" case changed in my patch, I just updated the reviewer patch to take that into account.


---

Comment by kcrisman created at 2011-06-24 19:08:35

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-06-24 19:08:35

Okay, I think that this is finally in shape.  Thanks for the back and forth on this.


---

Comment by jdemeyer created at 2011-07-22 12:48:27

Resolution: fixed
