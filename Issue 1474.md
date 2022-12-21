# Issue 1474: gap -- port to Itanium Linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 13:13:43

Assignee: was

Problem: GAP totally fails to build with -O2 (the default).  With
-O0 it builds and works, but is very very very slow, for the reasons
discussed below.  I'm trying to find somebody who can
help with this.  The bottom email below from Steve Linton explains
what needs to be done.  If anybody wants to work on this, let me know
(wstein`@`gmail.com). 


```
> > >   (1) What's the latest status of this question?
> >
> > No change.
> >
> > >   (2) Is there any hope?
> >
> > Yes. It needs a C programmer who can manage a few lines of in-line assembler
> > with GCC, an Itanium to test it on and about 30 lines of code.
> > If it acquired a high enough priority I would do it, but I can't hope to do it
> > this month or next. I can explain what is needed about GAP in an email if you
> > have a C programmer.

(see below for what is needed)

>
> > >   (3) Who should I talk to?
> > >
> > Me.
>
> Excellent.
>
> > > Would giving a certain GAP developer a temporary account on an Itanium
> > > machine help?  It's possible that this could be arranged.
> > >
> >
> > There aren't many of that are happy doing fiddly C work of this kind. I can
> > see if anyone wants to try.
>
> Thanks.  There are actually a lot of Itaniums at supercomputing centers
> in the US, for some reason.
>

```




```
Steve Linton to me
	
	
OK. The issue is with garbage collection. The GAP garbage collector looks for
any C local variable which appears to contain a reference to a GAP object. If
it finds one it assumes that it is a reference and keeps the object in
question alive. This is done in GenStackFuncBags in gasman.c. There is
relevant documentation about line 1474 and the code is at line 1667. A
collection of horrible, but surprisingly portable hacks are used to find and
scan all the C local variables on the stack and in the registers.

The problems on Itanium are that an Itanium has two stacks. One is used
for local variables, return addresses, etc. in the usual way. The other is used
when the register file overflows.

So what is needed is a few lines of assembler to

1) force the whole register file to be flushed onto this stack
(SparcStackFuncBags does this on Sparc)

2) find the top and botom of this stack so that it can be scanned.

It all works with -O0 because nothing is then kept in registers that is not
also on the main stack, but this is cripplingly slow.

If someone can come up with the assembler and the necessary wrapper to include
it in gasman.c I can trivially adjust the C code to call it and then scan both
stacks.

       Steve
```



---

Comment by jsp created at 2008-02-14 17:30:30

See fwd message on sage-devel:



```
Dear GAP Forum,

As some of you will recall, there is a very long standing
problem running GAP on processors from Intel's Itanium processor family, found
mainly in large multi-processor servers and supercomputers.

We believe that we have now fixed this problem, and the fix will be included
in the next release of GAP, but, if you wish to try it out in the meantime,
you can download it as a patch to apply to GAP 4r4p10. See
http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html
for a link to the patch.

Please let us know how you get on.

	Steve Linton
```



---

Comment by mabshoff created at 2008-02-14 17:32:26

William did try the updated sources yesterday and they segfaulted on his Itanium test box :(

Cheers,

Michael


---

Comment by was created at 2008-02-19 15:29:08

Steve Linton did this :-)

http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html

Now putting it into sage: #2209


---

Comment by was created at 2008-02-19 15:29:08

Resolution: fixed
