# Issue 9693: Maxima is printing asinh(1.0) without a leading zero (.8813735870195429) on Solaris 10 x86

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-05 23:44:01

Assignee: jason, jkantor

CC:  jhpalmieri cremona mhansen

An almost complete 32-bit port of Sage 4.5.2 to Solaris 10 on x86 processors had been done on the following hardware:

 * Dell OptiPlex 755
 * 2.40 GHz Intel Quad-Core Core2 Q6600 CPU
 * 8 GB RAM, 8 GB swap. 
 * Solaris 10 update 5 (5/08) on x86 
 * gcc 4.5.0 configured to use the Sun linker and GNU assembler
 * sage-4.5.2.rc1 with several changes. 

the result printed during a doctest lacks a leading zero. 


```
**********************************************************************
File "/home/palmieri/fulvia/sage-4.5.2.rc0/devel/sage-main/sage/symbolic/expression.pyx", line 508\
8:
    sage: maxima('asinh(1.0)')
Expected:
    0.881373587019543
Got:
    .8813735870195429
**********************************************************************
```


Following a suggestion of Carl Witty 

http://groups.google.com/group/sage-devel/msg/aa318e11e84afe8d?hl=en

I run 


```
2 drkirkby`@`fulvia:[/home/palmieri/fulvia/32bit/sage-4.5.2.rc1] $ ./sage -maxima
;;; Loading #P"/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/local/lib/ecl/defsystem.fas"
;;; Loading #P"/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/local/lib/ecl/cmp.fas"
;;; Loading #P"/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) asinh(1.0); 
(%o1)                          .8813735870195429
(%i2) 
```


clearly showing the missing leading zero on this Solaris 10 x86 machine. 

Trying this on the same version of Sage, but this time on a SPARC processor with Solaris 10, the result is different:


```
32 drkirkby`@`redstart:[~/redstart/32/sage-4.5.2.rc1] $ ./sage -maxima
;;; Loading #P"/export/home/drkirkby/redstart/32/sage-4.5.2.rc1/local/lib/ecl/defsystem.fas"
;;; Loading #P"/export/home/drkirkby/redstart/32/sage-4.5.2.rc1/local/lib/ecl/cmp.fas"
;;; Loading #P"/export/home/drkirkby/redstart/32/sage-4.5.2.rc1/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1)  asinh(1.0); 
(%o1)                          0.881373587019543
(%i2) 
```


Clearly this demonstrates a difference in the behaviour of the Maxima and ECL combination on Solaris 10 systems, where one has a SPARC processor and the other has an Intel Xeon processor. 

The version of ECL in this version of Sage is 10.2.1


Dave 


---

Comment by drkirkby created at 2010-08-06 00:00:56

Changing assignee from jason, jkantor to drkirkby.


---

Comment by drkirkby created at 2010-08-06 00:00:56

I've reported this under the title

"Maxima/ECL combination not printing a leading zero" to both

maxima`@`math.utexas.edu and ecls-list`@`lists.sourceforge.net

Dave


---

Comment by drkirkby created at 2010-08-09 03:13:24

Here's a couple of links to where this is discussed. 

 * [Maxima mailing list](http://www.math.utexas.edu/pipermail/maxima/2010/022230.html)
 * [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/43159b440ae83200)

It's not clear if the maxima developers consider this a bug or not - if they do, its certainly not considered a high priority for them to fix, so it looks like a fix in Sage is necessary. 

Note, other Maxima developers can redproduce this on some Linux systems, so it is not a specific to Solaris x86.


---

Comment by drkirkby created at 2010-08-19 04:09:56

As discussed here

http://groups.google.com/group/sage-devel/browse_thread/thread/351c46eb4cb91598/995e04912042c4be?lnk=gst&q=asinh#995e04912042c4be

I've changed the doctest to compute asinh(2.0) rather than asinh(1.0). Since asinh(2.0) is greater than one:


```
sage: maxima('asinh(2.0)')
1.44363547517881
```


there needs to be no leading zero, so the printing problem does not show. 

Whilst I can't guarantee every system will show 1.44363547517881, everyone who has tested this on their systems get *exactly* the same answer, so numerical rounding problems do not appear to exist here. Tests have been run on 

 * Sun SPARC processors 
 * Intel processors
 * AMD processors

using the following systems. 

 * sage.math (Linux)
 * bsd.math (OS X)
 * t2.math (Solaris 10 on SPARC)
 * fulvia `@` skynet (Solaris 10 on x86)
 * My Sun Blade 1000 (Solaris 10). 
 * My Sun Ultra 27 (OpenSolaris on x86) 
 * 32-bit Linux system of John Cremona using an Intel processor
 * 64-bit Linux system of John Cremona using an AMD Opteron processor. 

A more accurate result, computed using arbitrary precision arithmetic in Mathematica is:


```
In[4]:= N[ArcSinh[2],30]

Out[4]= 1.44363547517881034249327674027 
```


So every digit printed by Sage is correct. 

Dave


---

Attachment

Mercurial patch which changes computing asinh(1.0) to asinh(2.0)


---

Comment by drkirkby created at 2010-08-19 04:14:40

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-19 19:15:51

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-19 19:15:51

Works fine for me on both 32- and 64-bit linux machines.


---

Comment by mpatel created at 2010-08-23 22:14:19

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-08-24 02:51:07

Resolution: fixed
