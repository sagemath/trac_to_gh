# Issue 5315: Fix MPIR.spkg build on more OSX MacIntel boxen

Issue created by migration from https://trac.sagemath.org/ticket/5315

Original creator: mabshoff

Original creation time: 2009-02-20 05:33:37

Assignee: mabshoff

There is a known problem with PIC enabled MPIR code on 32 bit OSX when the CPU is capable of 64 bits. To work around that we delete some files, but there are some left that are used on older Macs:

```
p6/mode1o.asm
p6/dive_1.asm
pentium/hamdist.asm
pentium/mod_1.asm
pentium/popcount.asm
pentium/mode1o.asm
pentium/dive_1.asm
```

Deleting them on demand will fix the build. See also the thread at

 http://groups.google.com/group/sage-devel/browse_thread/thread/88c084b8cd828ac6

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 13:35:30

The spkg at 

 http://sage.math.washington.edu/home/mabshoff/SPKG/gmp-mpir-0.9.spkg

ought to fix the problem. I have asked the reported of the original issue to test and report back.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 16:28:49

Positive review by proxy from Mark:

```
> I had a class this morning and have only just started the build.
> It is running now and I can tell you that it has definitely made it
> past this specific problem.

Ok, this is a positive review from you in my eyes for this problem and
we can merge the spkg. I will ask someone else to take another look,
but I can assure you I did a very clean checkin :)

>  It should still take a couple of hours
> to complete.  I'll report back when I've got the finished product.

Cool, let me know if anything else blows up for you. I would assume
3.3.rc3 is out before your build finishes.
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 16:30:48

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 16:30:48

Resolution: fixed
