# Issue 7138: freetype always builds 32-bit libraries on Solaris, even when SAGE64="yes"

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-06 01:09:25

Assignee: tbd

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/lib, we can see the _freetype_' libraries are 32-bit, even though SAGE64 was set to "yes"


---

Comment by drkirkby created at 2010-01-02 07:10:06

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-02 07:10:06

I decided to make only the minimum changes necessary to get this to build 64-bit with gcc. As such, the only change is to spkg-install, so instead of -m64 being added only on Darwin, it is now added whenever SAGE64 is set to yes. 

I'll leave a better fix until a later date. See

http://boxen.math.washington.edu/home/kirkby/portability/freetype-2.3.5.p2/


---

Comment by jsp created at 2010-01-02 18:32:33

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-02 18:32:33

Looks ok for me. Tested on Open Solaris 0906 64 bit and Fedora 12.

I think SPKG.txt needs work, that can be done later by the official maintainer :)

Positive review.

Jaap


---

Comment by drkirkby created at 2010-01-02 18:52:51

I think you mean spkg-install needs further work, not SPKG.txt 

But this will at least allow it to build with gcc on Open Solaris.


---

Comment by jsp created at 2010-01-02 21:23:24

Replying to [comment:6 drkirkby]:
> I think you mean spkg-install needs further work, not SPKG.txt 
> 
> But this will at least allow it to build with gcc on Open Solaris.
> 

I really mean SPKG.txt as it is not conform the rules!

William is the maintainer so he will make the changes sometime.

spkg-install is ok withe me.

Jaap


---

Comment by mhansen created at 2010-01-04 02:01:26

Resolution: fixed
