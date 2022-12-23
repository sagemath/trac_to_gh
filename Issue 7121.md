# Issue 7121: Make it possible to build Sage but not documentation

Issue created by migration from https://trac.sagemath.org/ticket/7121

Original creator: kcrisman

Original creation time: 2009-10-05 13:27:08

Assignee: tbd

On slow machines (or even fast ones), building all the documentation for a build which will not be used for general purposes takes a looooong time.  There should be a switch for make and/or sage -upgrade which disables this.


---

Comment by drkirkby created at 2009-10-05 14:29:02

Another option might be an environment variable 'NO_DOCUMENTATION' or similar. I was about to update sage-env to handle a lot more environment variables. This could be added. The biggest problem is chaning every single packaging that builds the documentation. Adding a switch or compiler variable is the easy part!

Dave


---

Comment by kcrisman created at 2012-07-07 02:36:23

I have a feeling that I was being silly about this.  One can do `make build`, I think.

However, the targets in the Makefile are not particularly well documented in the installation guide.  So I'm changing this ticket's


---

Comment by kcrisman created at 2012-07-07 02:36:23

Changing priority from minor to major.


---

Comment by kcrisman created at 2012-07-07 02:36:23

Changing component from build to documentation.


---

Comment by kcrisman created at 2014-11-20 16:57:00

Okay, the [installation guide](http://www.sagemath.org/doc/installation/source.html?#section-make) is a lot better now.  Updating description for some things I see us being able to do now.


---

Comment by kcrisman created at 2014-11-20 16:57:00

Changing priority from major to minor.
