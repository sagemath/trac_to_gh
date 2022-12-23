# Issue 6741: pil interface

Issue created by migration from https://trac.sagemath.org/ticket/6741

Original creator: wdj

Original creation time: 2009-08-13 23:15:11

Assignee: was

The attached patch implements several functions providing a simpler interface to the Python Imaging Library. For example, you can sharpen the image of an image on the internet you have the url of and save it to Sage's tmp subdirectory.


---

Attachment

requires pil-1.1.6, applies to 4.1.1.rc2


---

Comment by mvngu created at 2009-08-18 17:45:03

Changing component from interfaces to packages.


---

Comment by mvngu created at 2009-08-18 17:45:03

Changing assignee from was to mabshoff.


---

Comment by mvngu created at 2009-08-18 17:47:56

This [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/caac9691d6fb0160) thread has a discussion about making PIL a standard spkg. The vote for doing so was carried out in that thread.


---

Comment by jason created at 2009-09-17 09:55:31

This looks very nice.  However, the doctests write to SAGE_ROOT/tmp, which means that a normal user cannot run doctests on this file.  Isn't there somewhere else that we should write temporary data during a doctest?  Maybe using SAGE_TMP or something like that?


---

Comment by jason created at 2009-09-17 09:56:42

I guess there isn't a SAGE_TMP.  How about a temporary directory under .sage?


---

Comment by mvngu created at 2009-09-17 10:05:17

Replying to [comment:6 jason]:
> I guess there isn't a SAGE_TMP.  How about a temporary directory under .sage?
Yes.


---

Comment by jason created at 2009-09-22 15:21:52

Nice work; thanks for doing this!

Marking as "needs work" for the following reasons:

 * Doctests which rely on internet should be marked "optional - requires internet"
 * image_convert should probably let me specify an output file name, or by default write in the current directory so that we can use it easily in the notebook (e.g., we convert something and it magically appears in the cell output).
 * someone should test this on a mac and then remove the note about it not being tested on a mac
 * stylistically, it looks like there is lots of duplicated code that opens files from the internet; maybe this could be refactored into a single function (and then used for image_convert as well)?


---

Comment by wdj created at 2010-01-04 03:52:26

Replying to [comment:8 jason]:
> Nice work; thanks for doing this!
> 
> Marking as "needs work" for the following reasons:
> 

Arrgghh ...
Just saw this now, going through old emails.

I will try to work on these referee comments/suggestions now. It probably needs rebasing anyway.
Sorry for the late reply.


---

Comment by wdj created at 2010-01-08 12:15:54

Good news: it applies fine and does not need rebasing.

Bad news: Now I can't even get the code to work. I've tried on an imac (which requires some extra work to get libjpeg to install) and on an ubuntu machine. Probably I'm missing something obvious, but I don't know what it is.


---

Attachment

ok, here is a cleanup patch.

There is an issue with fontmanager that I do not understand


---

Comment by chapoton created at 2013-08-31 14:46:10

Can one mark in some way the tests that depends on the presence of libpeg ?

Something like # optional libjpeg ?


---

Comment by chapoton created at 2014-01-08 09:00:33

New commits:


---

Comment by git created at 2016-05-19 12:22:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-29 18:31:32

Branch pushed to git repo; I updated commit sha1. New commits:
