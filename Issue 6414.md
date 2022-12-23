# Issue 6414: OS X binaries should issue a better warning on incompatible CPUs

Issue created by migration from https://trac.sagemath.org/ticket/6414

Original creator: GeorgSWeber

Original creation time: 2009-06-25 20:41:50

Assignee: tbd

CC:  dimpase

Currently, every now and then a user reports on sage-support, that he got an error message like

```
/Applications/sage-4.0.1-OSX10.5-PowerPC-PowerMacintosh-Darwin/sage/
local/bin/sage-sage: line 198:   407 Illegal instruction     sage-
ipython "$@" -i
```

This is e.g. the case if a Sage binary built on a MacPPC with a G5 processor (typically the one the OS X 10.5 bdist is created on) is used on a MacPPC with only a G4 processor.

For the *nix world on Intel/AMD processors, the sage-flags.txt file was created for just the purpose to check whether the CPU is sufficient, to let a certain Sage binary run.

We seem to need something in that direction for OS X, too (though momentarily only for the PPC processors, not the Intel ones).



---

Comment by kcrisman created at 2010-05-26 20:30:24

Is this still an issue with the new checks for moving OSX etc?


---

Comment by kcrisman created at 2015-01-05 16:08:41

This is essentially the same as #5950, except newer and with a little more info, so I'm keeping it.  Both of these should be addressed, I guess.  From #5950:

> -bdist should add something analog to the SSE flags on Linux so that if someone tried to run a ppc build on an x86 it aborts with a sane error message instead of just blowing up.


---

Comment by jdemeyer created at 2016-04-11 09:55:13

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-04-11 09:55:13

There should be no warning needed, the binaries should be produced to run on any CPU.


---

Comment by jdemeyer created at 2016-04-11 09:55:18

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2016-04-11 14:25:37

> There should be no warning needed, the binaries should be produced to run on any CPU.
? That doesn't really work on OS X all the time, we have seen many error messages on ask.sagemath for this for different instruction sets.


---

Comment by kcrisman created at 2016-04-11 14:25:47

Changing status from positive_review to needs_info.


---

Comment by kcrisman created at 2016-04-11 14:26:05

(By which I mean to say this isn't just a PPC/Intel issue.)


---

Comment by dimpase created at 2016-04-11 15:10:16

it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know. 

SAGE_FAT_BINARY cooked with wrong FAT... :-)


---

Comment by jdemeyer created at 2016-04-11 17:53:04

Replying to [comment:8 dimpase]:
> it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know.

I haven't heard of any such bug recently. In any case, such things should be fixed on a case-by-case basis, I don't think that there is a general fix possible. So I still think that this ticket should be closed.


---

Comment by dimpase created at 2016-04-11 23:08:18

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 dimpase]:
> > it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know.
> 
> I haven't heard of any such bug recently.
certainly with 6.9 binaries it is the case (e.g. reported  [today on sage-support](https://groups.google.com/d/msg/sage-support/C1eENI3yrtw/b5ChRoJkAQAJ)). There were also very entertaining bugs like this reported by someone with a Mac box having a non-standard (upgraded?) CPU... 
Don't recall about 7.1/2 right now. 

By the way: [faq-usage](http://doc.sagemath.org/html/en/faq/faq-usage.html#i-downloaded-a-sage-binary-and-it-crashes-on-startup-with-illegal-instruction-what-can-i-do) says: **Nobody has yet figured out how to build Sage in such a way that MPIR and ATLAS work on all hardware.**


> In any case, such things should be fixed on a case-by-case basis, I don't think that there is a general fix possible. So I still think that this ticket should be closed.


---

Comment by jdemeyer created at 2016-04-12 07:32:05

OK, then let's close this ticket not as "worksforme" but as "invalid" because it's too general.


---

Comment by jdemeyer created at 2016-04-12 07:32:05

Changing status from needs_info to positive_review.


---

Comment by kcrisman created at 2016-04-12 12:54:21

That seems like a good compromise.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
