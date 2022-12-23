# Issue 9690: explain differences between standard, optional, and experimental packages

Issue created by migration from https://trac.sagemath.org/ticket/9690

Original creator: mvngu

Original creation time: 2010-08-05 09:18:16

Assignee: mvngu

CC:  schilly

The Developer's Guide should distinguish between the following Sage packages: standard, optional, and experimental. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/85f94526238f6e6a/) thread for a start.


---

Comment by schilly created at 2010-08-05 13:46:53

Since I wrote the definition in the thread, here a revised summary:

 * standard
   * included in sage by default
   * runs on all supported platforms and systems
   * well tested, this means all needed functionality is doctested via the sage library
   * sage project as a whole is responsible
   * updates go through trac + extensive review

 * optional
   * not included by default
   * should run on all platforms, unless explicitly noted (i.e. this could be a reason why it cannot be a standard package, e.g. "valgrind")
   * sage project as a whole is responsible
   * updates go through trac + review

 * contributed (formerly known as "experimental")
   * not included by default
   * sage project is not responsible, it's the responsibility of the contributor(s) (maintainer(s)) that it works. he or she is also the dedicated contact person. 
   * doesn't need to run on all platforms, maybe it doesn't run at all (i.e. broken optional package)
   * updates to through trac, with comments, date and maybe a discussion, but there is no review. 

All three types follow the common layout of an SPKG, i.e. the install and (optional) check scripts, the mercurial repository excluding the untouched "src" dir and the SPKG.txt from where it should be possible to extract the description text. (sage -pkg checks that anyways, doesn't it?)


---

Comment by drkirkby created at 2010-11-10 15:27:06

A few comments

## Supported platforms

This bit of the developers guide should have a link to http://wiki.sagemath.org/SupportedPlatforms where the supported platforms are listed. (There needs to be other links in other parts of the developers and user's guide too, but this is one place where a link needs to be). Otherwise people wont know what platforms their optional packages are supposed to be tested on. 

## Optional packages

There should be a comment that optional packages must work on all supported platforms unless there is a *very* good reason why it can't be run on all platforms. (Valgrid is the obvious example of where there's a very good reason). What I am keen to avoid is an optional package, saying "It's only supported on Linux", and not making sufficient effort to actually get it working on any other platforms. 

I think if optional packages are .spkg files, then there should be an spkg-check file to run any self-tests that package may have. 

## Experimental packages

Although it should not be a requirement, I think we should say people are *encouraged* to add doc tests and if appropriate an `SPKG.txt` and `spkg-check` file. 



Is anyone intending to write this? I would like to see this in the developers guide, but don't know how to write the documentation myself, and have so many tickets I'm involved in now, this is not something I have a lot of time for myself. Someone who knows what they are doing can probably do it in a tenth of the time I could. 

Dave


---

Comment by drkirkby created at 2010-11-10 15:30:21

I personally think the word "Experimental" does imply the packages are less well tested than "Optional" whereas the same can not be said of "Contributed". But I guess this is a matter of taste - it's not something I have a big issue with. 

Dave


---

Comment by drkirkby created at 2010-11-18 09:28:06

Also, if renamed, then the top level Makefile, and possible other files would need editing. Is it really worth renaming them?

Dave


---

Comment by drkirkby created at 2010-11-18 09:28:57

Since nobody appears to be doing this, I'll write this page, though it would be good to get some agreement on a few issues before I write it. 

Dave


---

Comment by drkirkby created at 2010-11-18 09:29:15

Changing assignee from mvngu to drkirkby.


---

Comment by jdemeyer created at 2015-09-22 12:01:56

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-22 12:01:56

Please see #19267 which has a section about this.


---

Comment by jdemeyer created at 2015-09-22 12:02:00

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-25 08:07:50

Resolution: fixed
