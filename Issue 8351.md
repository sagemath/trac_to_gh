# Issue 8351: ratpoints-2.1.3.p0 fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-02-24 19:52:47

Assignee: drkirkby

ratpoints builds in 32 bit mode on Solaris x64.

A patch is coming up.

Jaap




---

Comment by jsp created at 2010-02-24 20:09:30

Changing status from new to needs_review.


---

Attachment

A new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg)



```
find_points.o:	ELF 64-bit LSB relocatable AMD64 Version 1
init.o:		ELF 64-bit LSB relocatable AMD64 Version 1
sift.o:		ELF 64-bit LSB relocatable AMD64 Version 1
sturm.o:	ELF 64-bit LSB relocatable AMD64 Version 1

```


Jaap


---

Comment by drkirkby created at 2010-02-24 20:24:35

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-24 20:24:35

There is a problem with this patch, in that tests for CCFLAG64, not CFLAG64 as others do. So it needs work. 

However, there are other problems with ratpoints that I am aware of. It is using the compiler option 


```
-DUSE_SSE 
```


on SPARC, even though the SPARC processor has no SSE instructions. That does not appear to be a serious issue, but ratpoints has been implicated as the reason the Sage library does not build - see #7867, which is *very* serious.

It might be better if you leave this one to me to try to sort out, as the SPARC issues are more serious. 

Dave


---

Comment by jsp created at 2010-02-24 21:25:32

Replying to [comment:2 drkirkby]:
> There is a problem with this patch, in that tests for CCFLAG64, not CFLAG64 as others do. So it needs work. 
> 

Ok, I can do that though CFLAG64 is not used in this spkg.


> However, there are other problems with ratpoints that I am aware of. It is using the compiler option 
> 
> {{{
> -DUSE_SSE 
> }}}
> 
> on SPARC, even though the SPARC processor has no SSE instructions. That does not appear to be a serious issue, but ratpoints has been implicated as the reason the Sage library does not build - see #7867, which is *very* serious.
> 
> It might be better if you leave this one to me to try to sort out, as the SPARC issues are more serious. 
> 

Yes, please solve the problems on SPARC, but that is certainly an other ticket.
Let this spkg work on Open Solaris x64 is the only issue solved with this ticket.

Cheers,

Jaap


> Dave


---

Attachment


---

Comment by jsp created at 2010-02-24 21:34:32

New spkg with the same name:

[http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg)

Jaap


---

Comment by jsp created at 2010-02-24 21:34:32

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-03-03 21:11:25

Sorry, I should have noted this earlier, but the package says 

"Building with extra 64-bit flags for OS X and Open Solaris"

Whereas a more accurate description would be 

"Building with the compiler flag(s) $CFLAG64 for a 64-bit build"

Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.

I would avoid mentioning Solaris specifically unless it is necessary. In this case it is not. 

Dave


---

Comment by drkirkby created at 2010-03-03 21:11:25

Changing status from needs_review to needs_work.


---

Comment by jsp created at 2010-03-03 21:21:04

Replying to [comment:5 drkirkby]:
> Sorry, I should have noted this earlier, but the package says 
> 
> "Building with extra 64-bit flags for OS X and Open Solaris"
> 
> Whereas a more accurate description would be 
> 
> "Building with the compiler flag(s) $CFLAG64 for a 64-bit build"
> 

How important is this nit picking?

> Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.
> 

Solaris 10 64 bit? Since when is this an option?

> I would avoid mentioning Solaris specifically unless it is necessary. In this case it is not. 
> 

Please go ahead and make a reviewers patch.

Jaap


> Dave


---

Comment by drkirkby created at 2010-03-03 22:39:56

Replying to [comment:6 jsp]:
> Replying to [comment:5 drkirkby]:
> > Sorry, I should have noted this earlier, but the package says 
> > 
> > "Building with extra 64-bit flags for OS X and Open Solaris"
> > 
> > Whereas a more accurate description would be 
> > 
> > "Building with the compiler flag(s) $CFLAG64 for a 64-bit build"
> > 
> 
> How important is this nit picking?

I do not consider it nit-picking, for reasons you see below. 
 
> > Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.
> > 
> 
> Solaris 10 64 bit? Since when is this an option?

It is very much a Sage goal. There is every reason to believe a Solaris 10 port will be 64-bit. The only reason the port was first 32-bit is that gcc tends to be less reliable on 64-bit SPARC. 

It could even beat the Open Solaris port, though my interest is more in Open Solaris now. 

Dave


---

Comment by jsp created at 2010-03-03 22:59:49

Replying to [comment:7 drkirkby]:
> Replying to [comment:6 jsp]:
> > Replying to [comment:5 drkirkby]:
> > > Sorry, I should have noted this earlier, but the package says 
> > > 
> > > "Building with extra 64-bit flags for OS X and Open Solaris"
> > > 
> > > Whereas a more accurate description would be 
> > > 
> > > "Building with the compiler flag(s) $CFLAG64 for a 64-bit build"
> > > 
> > 
> > How important is this nit picking?
> 
> I do not consider it nit-picking, for reasons you see below. 
> 

I don't see that.

> > > Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.
> > > 
> > 
> > Solaris 10 64 bit? Since when is this an option?
> 
> It is very much a Sage goal. There is every reason to believe a Solaris 10 port will be 64-bit. The only reason the port was first 32-bit is that gcc tends to be less reliable on 64-bit SPARC. 
> 
> It could even beat the Open Solaris port, though my interest is more in Open Solaris now. 
> 

Please make it possible. My interest is in Open Solaris too. Let's make this
possible asap. If you insist on making this ticket the first in a target to make Solaris 10 64 bit work, please go ahead and count me off.

Jaap


> Dave 
>


---

Comment by drkirkby created at 2010-06-04 10:09:45

Lets just get this done. It works. 

Dave


---

Comment by drkirkby created at 2010-06-04 10:09:45

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-06-04 10:09:59

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 07:31:10

Resolution: fixed
