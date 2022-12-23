# Issue 7814: [with spkg; needs review] eclib ignores SAGE64 if OS is not Darwin

Issue created by migration from https://trac.sagemath.org/ticket/7814

Original creator: drkirkby

Original creation time: 2010-01-02 04:53:07

Assignee: drkirkby

eclib-20080310.p7 suffered the usual problem of many packages - SAGE64 was ignored unless the operating system was OS X. This trivial patch simply ensure SAGE64 is not ignored on any platform. 

I've checked in the changes with 'hg' 

See: 
http://boxen.math.washington.edu/home/kirkby/portability/eclib-20080310.p8/




---

Comment by jsp created at 2010-01-02 20:53:44

Changing status from new to needs_work.


---

Comment by jsp created at 2010-01-02 20:53:44

I think the wrong spkg is in this link.

Jaap


---

Comment by jsp created at 2010-01-02 20:57:56

I see:



```
if [ "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel build"
    DYN_FLAGS="-m64"; export DYN_FLAGS
    PICFLAG="-m64 -fPIC"
fi
export PICFLAG

```



in spkg-install

Jaap


---

Comment by drkirkby created at 2010-01-02 21:11:38

yes, I should have removed that comment about the MacIntel. I think you will find it does build, but I will remove that command and make a new package.


---

Comment by jsp created at 2010-01-03 19:18:08

If there is a new spkg (see above) I can give it a positive review. Tested on Fedora 12 and Open Solaris 32 bit


```
real	4m15.073s
user	3m35.053s
sys	0m24.029s
Successfully installed eclib-20080310.p8
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3/spkg/build/eclib-20080310.p8
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing eclib-20080310.p8.spkg
jaap@opensolaris:~/Downloads/sage-4.3$ 

```


After a successful install of ntl and pari.

Jaap


---

Comment by drkirkby created at 2010-01-03 20:39:24

I've updated the package. It is now missing the comment that its a MacIntel. 

Please double check the package again though please - just in case I've messed up. 

dave


---

Comment by jsp created at 2010-01-03 20:41:20

Replying to [comment:5 drkirkby]:
> I've updated the package. It is now missing the comment that its a MacIntel. 
> 
> Please double check the package again though please - just in case I've messed up. 
> 
> dave 

Sure,

Jaap


---

Comment by jsp created at 2010-01-03 21:11:42

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-01-03 21:11:42

On Open Solaris:

```
real	4m8.443s
user	3m36.556s
sys	0m24.188s
Successfully installed eclib-20080310.p8

```


Looks good, build tested on Fedora 12 and Fedora 11.

Positive review.

Jaap


---

Comment by jsp created at 2010-01-03 21:12:36

Couldn't change to positive review. Will do now.

Jaap


---

Comment by jsp created at 2010-01-03 21:12:36

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-03 21:29:26

Cheers. 

I'm just going to remove the 'needs review from the title. I'm not sure if we are still supposed to do that or not. I find it easier to find me own sometime if its in the title. But anyway, I'm removing it now.


---

Comment by jsp created at 2010-01-03 21:35:32

Hi,

It already had a positive review, so ...?

Cheers,

Jaap


---

Comment by rlm created at 2010-01-13 06:28:55

Resolution: fixed


---

Comment by cremona created at 2010-01-24 14:45:13

Dave, I only just noticed this ticket (from the Release Notes).  I think you should have incereased the patch level from p8 to p9 - there now exist two different version s of the eclib spkg both called eclib-20080310.p8 which is rather confusing.

John


---

Comment by drkirkby created at 2010-01-24 18:42:55

Looking at the diff file I made of the SPKG.txt

http://boxen.math.washington.edu/home/kirkby/portability/eclib-20080310.p8/SPKG.txt.diff

the last revision made was in 

 === eclib-20080310.p7 (Michael Abshoff, October 12th, 2008) ===
  * Work around paralle make issue (#4228)

then I added 

### eclib-20080310.p8 (David Kirkby, 2nd January 2010)
 * Allow SAGE64 to work on all platforms, not just OS X. 

Are you sure the previous one was patch level 8 and not 7? If it was, then SPKG.txt was not updated when it moved to 8. Sorry about that, if I did overlook this. I agree it is confusing, if this is so. 

For it to also be merged, and the release manager not notice, seems a bit strange. 

Dave


---

Comment by cremona created at 2010-01-24 19:59:51

What I found was this.  On my own computer I have a p8 with the following changelog entry:

```
### eclib-20080310.p8 (John Cremona, January 6th, 2009)
 * Change to debugging output in procs/p2points.cc (not relevant for Sage)
 * Change to pdivs() in procs/marith.cc (not relevant for Sage)
```

Now, whatever that was about, it was not relevant for Sage (either referred to functions not used by anything wrapped in Sage, or under compiler options which Sage does not use), and presumably for that reason I did not make a ticket for it to replace the (then) standard p7 in Sage.

I guess the thing for me to do now is to make a p9 which has both the changes I made in my p8 and the ones you made, and get it into Sage.  I have to keep the version of the source files which are used by Sage in sync with the versions I have, otherwise I'll go mad.
