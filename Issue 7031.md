# Issue 7031: singular believes the Sun C++ compiler is broken.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 14:14:02

Assignee: tbd

CC:  dimpase

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used  (#7021)

CC was set to the Sun C compler, and CXX to the Sun C++ compiler. The singular configure script does not believe the Sun C++ compiler can create executables. This is the same sort of error as seen in quaddouble-2.2.p9 #7030. 

This time the problem is easy to diagnose. The test is used adds the option -fPIC when trying to test the C++ compiler. But -fPIC is a GNU-specific option - it is not acceptable to the Sun C++ compiler. Instead  -xcode=pic32, -KPIC or -PIC would work, but not -fPIC. 

It's clearly dumb to send a GNU specific option to test a C++ compiler unless you are 100% sure the C++ compiler is the GNU C++ compiler. 


```
checking for c++... /opt/xxxsunstudio12.1/bin/CC
checking whether the C++ compiler (/opt/xxxsunstudio12.1/bin/CC  -O3 -g -fPIC ) works... no
```





---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mjo created at 2020-07-12 20:01:13

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by mjo created at 2020-07-12 20:01:13

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
