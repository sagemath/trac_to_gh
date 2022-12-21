# Issue 2786: [with spkg] update zn_poly to 0.8

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-04-03 02:29:11

Assignee: mabshoff

I have made an spkg for `zn_poly` 0.8, please see attached.

Currently spkg-install runs a test suite (about 10 minutes). This should be disabled in the deployed version. I wasn't quite sure of the right way to do that.

It may or may not be necessary to touch files in the sage library that depend on `zn_poly` and rebuild:


```
touch devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx
touch devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob/*.cpp
```


So far I have positive build/tune/test reports from mhansen (Ubuntu Gutsy, 64-bit), wstein (osx 10.5.2), ddrake (Ubuntu Hardy, 32 bit), and myself (intel 64 mac OSX 10.4.11, ppc 64 mac OSX 10.4.11, AMD64 linux).



---

Attachment


---

Comment by mabshoff created at 2008-04-03 15:55:19

David,

the spkg looks food and builds fine. Numerous other people in IRC have confirmed that it builds for them, too. But: While the tuning phase is quick it seems that the spkg linked above runs integrity tests which took an extra eleven minutes of cputime on sage.math. While I think this is a good idea for 3.0.alphaX I would recommend that you turn that off before the final release of 3.0. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-03 15:55:38

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-03 15:55:38

Resolution: fixed


---

Comment by dmharvey created at 2008-04-03 16:02:17

Replying to [comment:1 mabshoff]:
> But: While the tuning phase is quick it seems that the spkg linked above runs integrity tests which took an extra eleven minutes of cputime on sage.math. While I think this is a good idea for 3.0.alphaX I would recommend that you turn that off before the final release of 3.0. Positive review.

Of course... I believe I already mentioned this above :-)

Question: is there any standardised way to put in test suites like that which run only in alpha releases?


---

Comment by mabshoff created at 2008-04-03 16:16:32

Replying to [comment:3 dmharvey]:

> Of course... I believe I already mentioned this above :-)

Oops, I didn't read the ticket in detail, I just remembered you asking in IRC about a one minute tuning phase.
 
> Question: is there any standardised way to put in test suites like that which run only in alpha releases?

Nope. Maybe we should add spkg-check-alpha, but that would increase build times across the board. Another possibility would be to run spkg-check depending on version number. We should take that over to sage-devel.

Cheers,

Michael
