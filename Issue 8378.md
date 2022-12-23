# Issue 8378: [trivial to fix] typo in documentation of crt

Issue created by migration from https://trac.sagemath.org/ticket/8378

Original creator: zimmerma

Original creation time: 2010-02-26 10:14:22

Assignee: AlexGhitza

CC:  cremona jason


```
sage: crt(15,1,30,4)
...
ValueError: arguments a and b must be coprime
```

However in the documentation of `crt` a, b are the residues,
and the moduli are called m, n. Thus the message should be:

```
ValueError: arguments m and n must be coprime
```



---

Attachment


---

Comment by zimmerma created at 2010-04-23 10:31:47

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-23 11:22:39

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-04-23 11:22:39

Of course this patch is fine (it applies OK to 4.4.alpha1).

Looking at this function and its docstring, though, these thoughts occur to me:

    1. If the condition gcd(m,n) is required, it should be documented in the INPUT block (which is missing);  and there should be a test to show what happens when the condition fails.
    2. As we all know, there exists a solution iff gcd(m,n) divides a-b.  So why not generalise the function to allow for this case too?  It would only take a small change to the code, and of course the documentation would also need chenging.  (The solution is unique modulo lcm(m,n), not m*n, in general).

I happen to have just been teaching this!

Paul, if you fancy upgrading your patch, go ahead.  Or you could ask me to do it since I'm the one who has made difficulties!


---

Comment by zimmerma created at 2010-04-23 11:52:10

John,

> Or you could ask me to do it since I'm the one who has made difficulties!

please go ahead! By the way, I noticed this while writing a textbook in french about Sage.
The textbook currently proposes a function `mycrt` which implements the general case:

```
def mycrt(a,b,m,n):
   g = gcd(m,n)
   x0 = a % g                                                                   
   y0 = b % g                                                                   
   if x0 <> y0:
      raise ValueError, "no solution"
   return (x0 + g * crt((a-x0)//g,(b-x0)//g,m//g,n//g)) % (n*m//g)              
sage: mycrt(15,1,30,4)
45
sage: mycrt(15,2,30,4)
Traceback (most recent call last):
...
ValueError: no solution
```

If you implement the general case, I will need to revise the textbook, but this is not a
problem... I will be happy to review your patch, but maybe a separate ticket is needed,
otherwise we would both appear as author+reviewer, and I'm not sure the release manager
will be happy with that.


---

Attachment

replaces previous;  applies to 4.4.rc0


---

Comment by cremona created at 2010-04-25 10:45:13

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-04-25 10:45:13

My patch trac_8378-crt.patch replaces Paul's (though note that it still has Paul's user id in it).  It extends the crt function to handle non-coprime moduli sensibly, with additional doctests.

This also means that the typo in the error message which Paul's patch fixed has now changed even more, so that in effect the effect of original patch is obsolete.

One might now argue for a greater change in the title of the ticket, and  a change from the tag "defect" to "enhancement".  I am not bothered -- I hope Paul does not mind my having totally taking over this ticket!  We probably need an independent review anyway.


---

Comment by zimmerma created at 2010-04-27 12:43:26

By the way, I notice that the way `crt([a1,a2,a3],[m1,m2,m3])` is not documented in
`crt?`.


---

Attachment


---

Comment by mvngu created at 2010-04-28 11:34:12

Reviewer patch has the following changes:

 * Explicitly mention the default values.
 * Properly typeset `lcm(m,n)`.
 * Clean up code following the conventions of [PEP 008](http://www.python.org/dev/peps/pep-0008/).
 * The improved documentation of `crt` says that this function also takes a list of residues and a list of moduli. Provide an example to demonstrate this usage.
 * Cross-reference the two functions `crt` and `CRT_list`.
 * The patch [trac_8378-crt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8378/trac_8378-crt.patch) results in two doctest failures in the English and French version of the Sage tutorial. Fix those doctest failures.

If the reviewer patch gets a positive review, then the whole ticket gets a positive review. I'm happy with [trac_8378-crt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8378/trac_8378-crt.patch). Any one but myself could review my reviewer patch.


---

Comment by cremona created at 2010-04-28 11:52:08

Reviewer patch looks good;   testing now.  Thank a lot, Minh, for tidying upwhat I wrote (e.g. when I found that \lcm was not defined I just did the lazy thing, while you did the proper thing!)


---

Comment by cremona created at 2010-04-28 11:52:08

Changing assignee from AlexGhitza to cremona.


---

Comment by cremona created at 2010-04-28 11:53:03

Tests pass, so I'm giving this (the review patch) a positive review, hence an overall positive review.


---

Comment by cremona created at 2010-04-28 11:53:03

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:20:35

Resolution: fixed
