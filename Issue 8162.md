# Issue 8162: p-adic ring constructor documentation incorrect

Issue created by migration from https://trac.sagemath.org/ticket/8162

Original creator: dmharvey

Original creation time: 2010-02-03 02:43:38

Assignee: roed

CC:  roed

According to the documentation for Zq, the following code should construct the degree 3 unramified extension of the 5-adic integers, but fails.


```
sage: R = Zq([(5,3)], names="alpha")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/padics/factory.pyc in Zq(q, prec, type, modulus, names, print_mode, halt, ram_name, res_name, print_pos, print_sep, print_max_ram_terms, print_max_unram_terms, print_max_terse_terms, check)
   1915     if check:
   1916         if not isinstance(q, Integer):
-> 1917             q = Integer(q)
   1918         if not isinstance(prec, Integer):
   1919             prec = Integer(prec)

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6820)()

TypeError: unable to coerce <type 'list'> to an integer
```




---

Attachment


---

Comment by roed created at 2011-11-09 03:43:10

Changing status from new to needs_review.


---

Comment by johanbosman created at 2011-11-14 14:44:11

Wouldn't it be better to have a pair as input, rather than a list whose only element is a pair?


---

Comment by roed created at 2011-11-14 15:15:13

The reason to use a list with a pair in it is so that the you can also pass in a factorization object.


---

Comment by johanbosman created at 2011-11-30 21:16:11

Ah, I see.  Yet, there is still a lot of room for improvement here.  The code doesn't check that the list has only 1 element.  And it would also be a lot better if it accepted a bare 2-tuple as well.


---

Comment by johanbosman created at 2011-11-30 21:16:11

Changing status from needs_review to needs_work.


---

Attachment

I changed the requirement that check=False.

Apply only 8162.patch.


---

Comment by roed created at 2011-12-12 15:28:05

Changing status from needs_work to needs_review.


---

Comment by saraedum created at 2011-12-19 00:15:26

Changing status from needs_review to needs_work.


---

Comment by saraedum created at 2011-12-19 00:15:26

I guess one should apply 8162.2.patch.

Even though I read the comment above I don't understand under which circumstances one would get a list of the form [(p,n)]. If you factor some q you get a factorization object. If you select one of its coefficients you get a tuple. The only way I could think of is casting a factorization to a list but would this really be useful?

I also find the use of 'check' confusing. One would expect 'check' to actually check whether q is a prime power (which probably the ExtensionFactory does, I haven't checked). Here it is also used to disable some of the input formats:


```
sage: k.<alpha> = Qq((2,1)) #works
sage: k.<alpha> = Qq((2,1),check=False)
TypeError: 'sage.rings.integer.Integer' object does not support indexing
```


So, something that works with check does not work without check anymore.

I can go ahead and fix these issues if you don't mind.


---

Comment by roed created at 2011-12-19 00:34:58

Yeah, that was a typo: apply only 8162.2.patch.

I can't think of a good reason to allow a list, but also no particular reason not to allow it, since lists are a common container for objects in Python.  :-)

As for the check parameter, my interpretation of check=False is that it only accepts input of a particular format in order to minimize the time spent in handling different input formats.  So I think it's completely reasonable for your example to fail when you don't pass in something of the form [(p, k)].

So I guess my conclusion is that I don't think the issues you're pointing out are problems.


---

Comment by saraedum created at 2011-12-21 15:24:55

Changing keywords from "" to "sd35".


---

Comment by roed created at 2012-01-04 11:22:34

Any further thoughts?  I don't think we currently have agreement on what to do with this ticket, so I don't think "needs work" is the right classification.


---

Comment by roed created at 2012-01-04 11:22:34

Changing status from needs_work to needs_info.


---

Comment by roed created at 2012-03-03 00:07:42

Changing status from needs_info to needs_review.


---

Attachment

Replying to [comment:7 roed]:
> I can't think of a good reason to allow a list, but also no particular reason not to allow it, since lists are a common container for objects in Python.  :-)
Sure, this makes sense.

> As for the check parameter, my interpretation of check=False is that it only accepts input of a particular format in order to minimize the time spent in handling different input formats.  So I think it's completely reasonable for your example to fail when you don't pass in something of the form [(p, k)].
I mostly agree with you. I think that with `check=False` nothing should be done that could be expensive (things like checking whether a minimal polynomial is actually irreducible). However, I believe that `check` should not have an influence on the interface.

I adapted your patch to only make the check trigger whether we check that `p` is actually a prime. All the other checks are just `isinstance` and `len` checks which come essentially for free.

I looked at some timings and the two versions don't really seem to differ with `q=(p,k)` and `check=False`.

Would this patch be acceptable for you?

[I haven't run full doctests yet, so let me see if the patchbot at least likes it.]


---

Comment by saraedum created at 2012-11-19 21:02:14

Apply only trac_8162.patch


---

Comment by saraedum created at 2013-01-22 00:02:02

The startup plugin says that the startup time might have increased. However, the functions this patch touches are not executed on startup, so this should only be noise.


---

Comment by rws created at 2014-03-31 14:16:59

Patch applies fine with 6.2.beta5. One doctest fail (an aged patchbot run was fine):

```
File "src/sage/rings/padics/factory.py", line 1953, in sage.rings.padics.factory.?
Failed example:
    R = Zq([(5,3)], names="alpha"); R
Expected:
    Unramified Extension of 5-adic Ring with capped absolute precision 20 in alpha defined by (1 + O(5^20))*x^3 + (3 + O(5^20))*x + (3 + O(5^20))
Got:
    Unramified Extension of 5-adic Ring with capped absolute precision 20 in alpha defined by (1 + O(5^20))*x^3 + (O(5^20))*x^2 + (3 + O(5^20))*x + (3 + O(5^20))
```



---

Comment by rws created at 2014-03-31 14:16:59

Changing status from needs_review to needs_work.


---

Comment by saraedum created at 2014-04-02 11:23:01

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-04-02 14:12:19

All tests pass now.
----
New commits:


---

Comment by rws created at 2014-04-02 14:12:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-04 18:52:22

Resolution: fixed
