# Issue 9169: cygwin: a cachefunc.py doctest hangs seemingly forever

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:32:34

Assignee: tbd

CC:  jpflori dimpase kcrisman

On Cygwin, the following test hangs:

```

            sage: `@`cached_function
            ... def oddprime_factors(n):
            ...     l = [p for p,e in factor(n) if p != 2]
            ...     return len(l)
            sage: oddprime_factors.precompute(range(1,100), 4)
```


The above is very fast on any other platform. 

This results in a doctest file failure:

```
sage -t  "devel/sage/sage/misc/cachefunc.py"                
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
	 [361.6 s]
```



---

Comment by kcrisman created at 2013-01-15 15:20:56

FWIW, this file is now `cachefunc.pyx`.


---

Comment by kcrisman created at 2013-01-15 15:46:33

This same test still fails, though for me it is because of forking errors and an inability to start Singular at times (presumably for that reason).


---

Comment by jpflori created at 2013-01-15 18:00:28

On my install (64bits Windows 7 + sage 5.6.rc0) the test passes.


---

Comment by kcrisman created at 2013-01-15 18:09:54

That's good to hear.  I am frustrated by this forking business.  A complete rebase just shifts the error to a different random file that won't be remapped.  So I can never tell whether things are really a problem or not.


---

Comment by dimpase created at 2013-01-27 10:07:51

Replying to [comment:5 kcrisman]:
> That's good to hear.  I am frustrated by this forking business.  A complete rebase just shifts the error to a different random file that won't be remapped.  So I can never tell whether things are really a problem or not.

Are you working on a 32-bit Windows? I've given up on attempting to use Cygwin on 32-bit systems.

Anyhow, this test works for me too. Let's close this one.


---

Comment by dimpase created at 2013-01-27 10:07:51

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-01-28 02:11:23

I'd feel best if we were able to try on 32-bit XP... though I recognize this may be impossible unless my box stops acting up.


---

Comment by jpflori created at 2013-01-30 10:43:00

When the status on my 64 bits Windows 7 looks good enough (which looks close), I'll dig up an old 32 bits install and give it a try.


---

Comment by jpflori created at 2013-02-08 12:41:16

This is ok on 32 bits Windows 7, so I'll close it.


---

Comment by jpflori created at 2013-02-08 12:41:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-08 13:21:28

Resolution: worksforme
