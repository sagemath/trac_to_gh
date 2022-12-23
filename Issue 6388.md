# Issue 6388: Logarithm function log(x) is partially broken for x <= 0

Issue created by migration from https://trac.sagemath.org/ticket/6388

Original creator: gmhossain

Original creation time: 2009-06-23 12:36:04

Keywords: negative argument, log

Although log(x) function in new symbolics is appeared to be defined for entire complex plane, it throws out error sometime 

(1) Negative argument


```
sage: log(-1 + 0*I)
I*pi
sage: log(-1)
...
ValueError: self must be positive
```

It behaves differently for mathematically equivalent arguments.


(2) Value of log(x) at x=0


```
sage: log(0)
...
ValueError: self must be positive
```


log(0) should throw out an unevaluated symbolic expression "log(0)" instead of raising error. Depending on the way it appears in an expression, one could use it for simplifications.



---

Attachment

Based on 4.1.1


---

Attachment

Based on 4.1.1


---

Comment by kcrisman created at 2009-09-02 13:15:16

Attach either patch, they are the same - things timed out on me and I wasn't sure if it uploaded the first time.  I can't figure out how to remove the redundant one.

Please note that there should now be NO log(-1) that return an error (including log(RIF(-1)), log(float(-1)), and log(complex(-1))) and there should be NO log(0) that return a symbol or NaN (including the same types).  This is a change, but presumably will not break anything.  It does change the error message for 

```
sage: plot(log,-1,1)
```

to something about complexes rather than math domain error, but that is not a big deal since it still plots.  It passed all tests for me.


---

Comment by gmhossain created at 2009-09-02 21:58:49

I am going through this patch. It applied cleanly and also passed some of the doctests that
I tried. Few initial comments:

While log(SR(0)) typesets nicely but log(CC(0)) or log(RDF(0)) doesn't. Although, I don't think
that this patch should fix these typesetting issue but in case there is an one-liner fix.


---

Comment by kcrisman created at 2009-09-03 01:58:36

The supplemental patch requires the previous patch, and adds a few cases I missed.  I was able to get typesetting properly for one case, but cannot figure out how to use the same trick for real_mpfr or real_double (it works when you do it in the commmand line, but when running the whole _latex_ method it mysteriously fails).


---

Attachment

Requires regular patch, based on 4.1.1


---

Comment by gmhossain created at 2009-09-05 15:51:41

Hi,

Thanks, you have added more features than I had wanted. Here are my last comments before
I give positive review:


```
sage: log(SR(-1), e)
I*pi
sage: log(CDF(-1), e)
3.14159265359*I
```


works but it doesn't work or CC, RR, CIF...

I think, it would be better if you could change this two lines in log() 

```
except AttributeError:
    return ln(x) / ln(base)
```


to


```
except (AttributeError, TypeError):
    return log(x) / log(base)
```


We should call log() recursively so that it can take advantage of
the features that you have added. Another supplementary patch should be fine too.


---

Comment by gmhossain created at 2009-09-05 16:13:49

Just to clarify: changing above two lines should also fix the issue I mentioned.


---

Attachment

Apply after others


---

Comment by kcrisman created at 2009-09-05 17:39:02

Okay, probably several solutions to this, but that is a good one.  Apply all three (distinct) patches.


---

Comment by gmhossain created at 2009-09-05 17:45:01

Overall its a great improvement of log() and here goes positive review from me. Thanks.

Cheers,
Golam


---

Comment by mvngu created at 2009-09-07 16:44:24

Merged patches in this order:

 1. `trac_6388-log-behavior.2.patch`
 1. `trac_6388-log-behavior-supplement.patch`
 1. `trac_6388-log-behavior-supp2.patch`


---

Comment by mvngu created at 2009-09-07 16:44:24

Resolution: fixed
