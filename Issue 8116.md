# Issue 8116: cython fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set to -m64 globally

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-29 12:53:27

Assignee: drkirkby

CC:  robertwb

If $SAGE64 = "yes" we need CFLAGS=-m64 on Open Solaris.

Patch coming up.

Jaap


---

Attachment

[http://boxen.math.washington.edu/home/jsp/ports/cython-0.12.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/cython-0.12.p0.spkg)

This spkg needs testing on OSX with $SAGE64 = "yes"

Jaap


---

Comment by jsp created at 2010-01-29 13:23:27

Changing assignee from drkirkby to jsp.


---

Comment by jsp created at 2010-01-29 16:41:53

Changing assignee from jsp to drkirkby.


---

Comment by jsp created at 2010-01-29 16:42:06

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-29 18:32:04

I would not do this. It was setting of CFLAGS in sage-env which caused cython to mis-compile code. This is probably why it was not done in OS X. I do not know how to get cython to build 64-bit, but I do not believe you should set CFLAGS to do so.


---

Comment by drkirkby created at 2010-01-29 18:32:04

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-01-29 19:43:13

Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library?


---

Comment by jsp created at 2010-01-29 20:51:52

Replying to [comment:6 robertwb]:
> Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? 

So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.

Why not unset CFLAGS in the Cython spkg-install?

Without CFLAGS set building cython failes on Open Solaris x64!

*.pyx files? I don't get sage-4.3.1.alpha build :)!

So let's get Python build correctly on Open Solaris x64!

Jaap


---

Comment by robertwb created at 2010-01-29 21:05:49

Replying to [comment:7 jsp]:
> Replying to [comment:6 robertwb]:
> > Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? 
> 
> So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.

Yes. Worrying about Cython working before Python is set up correctly is probably going to be an exercise in futility. 

> Why not unset CFLAGS in the Cython spkg-install?

For fear of breaking things. I am not an expert on distutils or building stuff, so for me the safest path is to not change stuff. 

> Without CFLAGS set building cython failes on Open Solaris x64!

Do you get a working Cython with CFLAGS set? (If so, it might just be lucky...) What errors do you get otherwise? (I think Cython's supposed to fall back to a pure Python setup if the compile fails, but I could be remembering wrong.)

> *.pyx files? I don't get sage-4.3.1.alpha build :)!

Yet :)

I'm just pointing out that whatever issues we're running into here, we'll be running into later with the sage library. 

> So let's get Python build correctly on Open Solaris x64!

Sounds like the best course of action.


---

Comment by jsp created at 2010-01-29 22:09:09

Replying to [comment:8 robertwb]:
> Replying to [comment:7 jsp]:
> > Replying to [comment:6 robertwb]:
> > > Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? 
> > 
> > So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.
> 
> Yes. Worrying about Cython working before Python is set up correctly is probably going to be an exercise in futility. 
>

I do have a working Python! But I don't know it is setup properly :(


```
Python 2.6.4 (r264:75706, Jan 27 2010, 22:37:41) 
[GCC 4.4.2] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```


 
> > Why not unset CFLAGS in the Cython spkg-install?
> 
> For fear of breaking things. I am not an expert on distutils or building stuff, so for me the safest path is to not change stuff. 
> 

If you don't accept CFLAGS set globally, why not?

> > Without CFLAGS set building cython failes on Open Solaris x64!
> 
> Do you get a working Cython with CFLAGS set? (If so, it might just be lucky...) What errors do you get otherwise? (I think Cython's supposed to fall back to a pure Python setup if the compile fails, but I could be remembering wrong.)
> 

I don't know. It just says it installed successfully :)



> I'm just pointing out that whatever issues we're running into here, we'll be running into later with the sage library. 
> 
> > So let's get Python build correctly on Open Solaris x64!
> 
> Sounds like the best course of action. 


Let's go for it!

Jaap


---

Comment by robertwb created at 2010-01-29 22:20:52

Replying to [comment:9 jsp]:
> If you don't accept CFLAGS set globally, why not?

This is a distutils question, nothing specific to Cython. Hopefully we can get to the root of the issue, as many packages are "python setup.py install"


---

Comment by jsp created at 2010-01-30 12:46:10

I rebuilt python with in the spkg-install Darwin changed to SunOS.

Python buidls ok now with the right CFLAGS set.

Rebuilding cython was ok.

So in principle problem solved!

I close the ticket as invalid.

Jaap


---

Comment by jsp created at 2010-01-30 12:46:10

Resolution: invalid
