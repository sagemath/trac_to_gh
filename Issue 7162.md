# Issue 7162: maybe remove linking xpm into gd

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-08 20:07:15

Assignee: tbd

CC:  was drkirkby jsp

I'm trying to build sage-4.1.2 on disk.math.washington.edu (opensolaris x86) and had to change the spkg-install of gd-2.0.35.p2:

```
# We explicitly disable X support, since (1) X is not a SAGE dependency,
# and (2) the gd build fails on a lot of OS X PPC machines when X is enabled.
./configure --prefix="$SAGE_LOCAL" --without-jpeg --without-x --without-xpm --with-zlib="$SAGE_LOCAL" --with-freetype="$SAGE_LOCAL"
```


I added `--without-xpm`.

Maybe we should make this standard?



---

Comment by drkirkby created at 2009-11-04 04:42:45

It seems sensible to make it standard to me. 

If you want to post a package, I'll review it.


---

Comment by drkirkby created at 2010-01-02 18:49:34

Changing status from new to needs_review.


---

Attachment

A revised .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg


---

Comment by jsp created at 2010-01-02 21:15:45

Replying to [comment:2 drkirkby]:
> A revised .spkg can be found at 
> 
> http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg

This change make the build depend on setting export CFLAGS=-m64

Is this a good thing to  do?

Jaap


---

Comment by drkirkby created at 2010-01-02 22:36:40

Hi, 
you have a point, but there was some logic to this. 

The purpose of the ticket which William opened was to add 


```
--without-xpm
```


to the line where the configure script it invoked. The ticket had nothing to to with SAGE64.

I think whilst trying to build on Solaris in 64-bit mode, you should set CFLAGS and CXXFLAGS to include -m64, as that will allow *some* packages to build without making changes to their spkg-install files. This is one such package. 

I've written two scripts (#7505) which check what the compiler is (GCC, Sun Studio, HP, IBM etc). That ticket already has positive review. 

I've written an updated version of sage-env, #7818 which is awaiting review. That will uses those two script, determine the right compiler flag, then automatically export the right compiler flag to CFLAGS. 

As such, I believe making only the change William suggested is sufficient in this case. Just export CFLAGS and CXXFLAGS to include -m64, and expect that in the next release or two, that will happen automatically for you. Doing this, will reduce somewhat the number of spkg-install files that need editing. 

Dave


---

Comment by jsp created at 2010-01-02 23:02:51

Ok, nobody is hurt here. People who are porting should know this.

So I give it a positive review.

Jaap


---

Comment by jsp created at 2010-01-02 23:02:51

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 22:07:43

Resolution: fixed
