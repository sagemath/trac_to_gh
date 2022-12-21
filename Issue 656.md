# Issue 656: incorporate mabshoff's bugfixes into iml and make a new spkg

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-14 15:26:33

Assignee: was

CC:  michael.abshoff@googlemail.com

From Mabshoff:


```
I have found 3 small issues in the IML 1.0.1 release. One of them is
somewhat serious (a use after free situation in certsolve.c) and two
small memory leaks. For patches see:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/IML-1.0.1-fix-use-after-free.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/IML-1.0.1-fix-trivial-mem-leak-in-largeentry.c.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/IML-1.0.1-fix-trivial-mem-leak-in-smallentry.c.patch

I am CCing William and Clement because I hope that Clement might be able
to get in touch with the right people in case there is no answer and
because William told me that in the past he never got an answer from
Zhuliang and Arne. So that way we might be able to establish contact
between the IML developers and the Sage people. Since IML is supposed
to/ will get integrated into LinBox I am also curious how that will work
out.

There is one more problem I didn't fix yet (due to lack of time):

==23789== Conditional jump or move depends on uninitialised value(s)
==23789==    at 0x411BC5: RowEchelonTransform_rec (mtrans.c:212)
==23789==    by 0x411822: RowEchelonTransform_rec (mtrans.c:256)
==23789==    by 0x411822: RowEchelonTransform_rec (mtrans.c:256)
==23789==    by 0x41250E: RowEchelonTransform (mtrans.c:148)
==23789==    by 0x406F6E: specialminSolveRNS (certsolve.c:2637)
==23789==    by 0x40DDAF: certSolveMP (certsolve.c:1143)
==23789==    by 0x4021BF: tstcertsolveMP (test-largeentry.c:128)
==23789==    by 0x402BFC: main (test-largeentry.c:82)


If anybody has a solution let me know.

```



---

Comment by was created at 2007-09-14 18:53:42

From one of the IML authors:


```
Arne Storjohann <> 	
to Arne, Michael.Abshoff, Zhuliang, Clement, me
	
show details
	 11:47 am (1 minute ago) 
Hi Michael,

Thanks very much for the patches.  We will incorporate
the fixes and try to correct the additional problem
you found.

If you find other problems please let us know.
I will keep you informed of changes.
```



---

Comment by mabshoff created at 2007-09-14 21:30:51

There is movement on the IML front and there will be a 1.0.2 release shortly. Currently there is some discussion what patches need to go in.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-21 01:11:50

There is a new spkg with the 1.0.1->1.0.2 diff at

http://sage.math.washington.edu/home/mabshoff/iml-1.0.1.p7.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-21 01:39:28

Resolution: fixed
