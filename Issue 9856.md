# Issue 9856: Upgrade biopython to version 1.55 (released Augest 31, 2010)

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2010-09-04 20:31:05

Assignee: tbd

CC:  mhansen mvngu schilly

Keywords: biopython

Biopython is actively maintained and this latest release comes closer to supporting python 3.0.  It also improves some command-line utilities and other miscellaneous improvements.

An spkg is available at:
http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg


---

Comment by awebb created at 2010-09-16 14:32:06

Hi,

The patch is no longer needed and should be removed. The test in the src/Bio/Wise/__init__.py has been improved to test if the test is being run from a tty. The tests now passes when run using export SAGE_CHECK="yes". 

Adam


---

Comment by mhampton created at 2010-09-16 18:41:08

Thanks for looking at this.  I removed the patch directory, removed the change from the spkg-install, and updated SPKG.txt to note this.  I also added you as a spkg maintainer.  

I just over-wrote the same file at [http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg) with these changes.


---

Comment by mhampton created at 2010-09-16 20:10:42

I just ran the tests and got the old failures from the Wise module, so this doesn't seem to be fixed after all unless I'm missing something.


---

Comment by awebb created at 2010-09-17 12:08:12

Unfortunately, I haven't been able to duplicate that. I get:

```
test_Wise ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.
test_psw ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.
```

but I think this is expected as I don't have Wise2 installed. I also get:

```
Bio.Wise docstring test ... ok
Bio.Wise.psw docstring test ... ok
```

What I did was to run the commands:

```
export SAGE_CHECK="yes"
sage -f biopython-1.55.p0.spkg
```

I noticed that that previous installed version was not overwritten. I then removed the directory and did the install again. This time the new file was present. The tests again passed. 

How did you run the tests?

Adam


---

Comment by mhampton created at 2010-09-17 12:54:24

I tried this from scratch and it worked as expected (as you reported above).  So it must have been a problem with not over-writing something.  I will double-check on a different machine today but I think things are OK as is.


---

Comment by mhampton created at 2010-09-17 12:54:24

Changing status from new to needs_review.


---

Comment by awebb created at 2010-09-17 13:03:35

I have had this sort of problem with python distutils before. Old versions are not written over even though the files have changed. My guess is that the root of the problem is that the old version is not removed first. It is very easy to end up with an install that is a mixture of versions this way.


---

Comment by awebb created at 2010-09-18 12:24:03

The package looks fine to me. I guess I should I have an email; maxthemouse at googlemail dot com.


---

Comment by awebb created at 2010-09-21 10:40:10

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 09:20:38

Mike, Minh, or Harald, could one of you please merge 

 http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg

into the optional packages repository?


---

Comment by schilly created at 2010-09-28 09:37:55

Replying to [comment:10 mpatel]:
> Mike, Minh, or Harald, could one of you please merge 
> http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg
> into the optional packages repository?

Done.


---

Comment by mpatel created at 2010-09-28 09:50:58

Thanks!


---

Comment by mpatel created at 2010-09-28 09:50:58

Resolution: fixed
