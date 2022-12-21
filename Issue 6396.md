# Issue 6396: primes_of_degree_one is broken for relative extensions

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-06-24 17:07:16

Assignee: was

CC:  ncalexan

This is kind of irritating:


```
sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: N.primes_of_degree_one_list(10)
[Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1)]
```



---

Comment by davidloeffler created at 2009-06-24 18:05:33

Here's a patch. Turns out that the bug was due to using the wrong generator. I've set it to use `absolute_generator` rather than `gen`, and patched absolute number fields so `absolute_generator` is an alias for `gen` in that case. The patch also ReSTifies small_primes_of_degree_one.py and adds it to the reference manual.

(Nick, since he wrote the original code.)

David


---

Comment by ncalexan created at 2009-06-24 18:10:57

This looks good to me, and I am cautiously optimistic that the method will select the same generator on all architectures.  Apply.


---

Comment by boothby created at 2009-06-26 17:27:29

Doctest failures when applied to 4.1.alpha1


```
sage -t -long devel/sage/sage/rings/number_field/small_primes_of_degree_one.py
**********************************************************************
File "/space/boothby/sage-4.1.alpha1/devel/sage-main/sage/rings/number_field/small_primes_of_degree_one.py", line 204:
    sage: N.primes_of_degree_one_list(10)
Expected:
    [Fractional ideal ((-1/2*b + 1/2)*a + 2),
     Fractional ideal (-b*a + 1/2*b + 1/2),
     Fractional ideal ((1/2*b + 3/2)*a - b),
     Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
     Fractional ideal (-b*a - b + 1),
     Fractional ideal (3*a + 1/2*b - 1/2),
     Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),
     Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
     Fractional ideal (2*a - 3/2*b - 1/2),
     Fractional ideal (3*a + 1/2*b + 5/2)]
Got:
    [Fractional ideal (2*a + 1/2*b - 1/2), Fractional ideal ((-1/2*b - 1/2)*a - b), Fractional ideal (b*a + 1/2*b + 3/2), Fractional ideal ((-1/2*b - 3/2)*a + b - 1), Fractional ideal ((-b + 1)*a + b), Fractional ideal (3*a + 1/2*b - 1/2), Fractional ideal ((1/2*b - 1/2)*a + 3/2*b - 1/2), Fractional ideal ((-1/2*b - 5/2)*a - b + 1), Fractional ideal (2*a - 3/2*b - 1/2), Fractional ideal (3*a + 1/2*b + 5/2)]
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /space/boothby/sage-4.1.alpha1/tmp/.doctest_small_primes_of_degree_one.py
         [3.2 s]
```



---

Comment by davidloeffler created at 2009-06-26 17:42:56

Aargh! Every damn thing we do with ideals seems to return different answers on different platforms -- I've never understood why this is and it's fantastically annoying. The ideals are the same ones, of course, but their string representations are different because Pari picks generators in a totally unpredictable way.

I'll fix this when I get around to it (probably after SD16 is over)

David


---

Attachment


---

Comment by davidloeffler created at 2009-06-26 18:06:03

Can you try this new patch and see if it works better for you? It works on my machine, but then so did the last one, and there is no sage.math binary of 4.0.2 available AFAIK.


---

Comment by davidloeffler created at 2009-06-27 07:48:33

BTW: having built myself a 4.1.alpha1 on sage.math overnight, I've checked that it passes doctests there too. Can I just reinstate the positive review now, or does it need to be re-reviewed?


---

Comment by davidloeffler created at 2009-07-14 16:43:04

Hello? I'm marking this as "positive review" so it comes to the attention of the release managers for 4.1.1, who can decide as they see fit what to do given the slightly ambiguous status. All that's needed is for someone to check that the doctests pass on both 64-bit and 32-bit.

(I really would prefer it if this patch didn't hang around bitrotting forever -- this is necessary for a major project I'm working on, which seems to have exposed a remarkable number of bugs; see also #6457, #6458, #6462 and #6463.)


---

Attachment

reviewer patch; fix minor docstring formatting


---

Comment by mvngu created at 2009-07-16 18:10:47

The patch `trac_6396-reviewer.patch` makes some adjustment to the docstring introduced by `trac_6396-deg1primes.patch`, and fixes some typos therein. All tests passed on sage.math (a 64-bit machine) and on my 32-bit Debian Lenny machine. Just to let people know, both patches have been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:14:18

Resolution: fixed


---

Comment by mvngu created at 2009-08-22 20:26:52

See #6806 for a follow up to this ticket.
