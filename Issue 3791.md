# Issue 3791: ATLAS.spkg: add Altivec errata support for Linux PPC

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-08 16:15:19

Assignee: mabshoff

CC:  fbissey jpflori


```
I was told that this line means that altivec was not detected.
For atlas on linux ppc with altivec, we should use the options
--cflags='-mregnames' -D c -DATL_AVgcc
for configure ( http://math-atlas.sourceforge.net/errata.html#G4gcc ).

With these options, I had "Vector ISA Extension configured as  AltiVec (1,2)".

Best regards,
Bin 
```



---

Comment by mabshoff created at 2008-08-08 16:15:23

Changing status from new to assigned.


---

Comment by kcrisman created at 2015-01-05 16:06:15

What do you guys think - is this still valid?


---

Comment by jpflori created at 2015-01-05 16:11:53

Frankly, I'd say we don't care about such systems...
And from the ticket description it just seems that ATLAS won't be optimized on such systems but would still build.


---

Comment by fbissey created at 2015-01-05 18:53:55

My own experience is that you need to let ATLAS set its own flags on power7 and probably other ppc(64) arch. It detects and adds altivec/vsx flags appropriately. If you touch CFLAGS you have to make sure to include flags that activate altivec (appropriate -mcpu and -mtune does the trick the CPPFLAGS should be included automatically and failure to include the right flags will result in a compilation failure at some point).

Is this for your project of building a last tiger ppc binary?


---

Comment by kcrisman created at 2015-01-05 20:37:25

>Is this for your project of building a last tiger ppc binary?

No, although that is going fine.  This is just me seeing random tickets that possibly could be closed as wontfix/invalid... I can't say whether it would but if you both agree then I say you should do so :)


---

Comment by fbissey created at 2015-01-05 21:33:01

Changing status from new to needs_review.


---

Comment by fbissey created at 2015-01-05 21:33:52

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2015-01-05 21:33:52

I am putting it as "invalid".


---

Comment by vbraun created at 2015-01-13 01:13:57

Resolution: invalid


---

Comment by vbraun created at 2015-01-13 01:13:57

You are supposed to change the milestone to "duplicate/invalid/wontfix" then...
