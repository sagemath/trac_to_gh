# Issue 7205: fix the list of old sage releases website

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-14 02:40:54

Assignee: tbd

CC:  schilly

1. If I go to http://sagemath.org/src/ there is only the last release.

 2. If I click on "up one directory level", I'm just dumped to
http://sagemath.org, which makes no sense.

 3. Clicking on changelogs gives
http://sagemath.org/src/changelogs/index.html which does indeed list
changelogs.  But it also lists  a file "OLD_VERSIONS_HERE.txt",
randomly right in the middle.  Looking at that file I find the
completely wrong statement: "These are archived old versions.  For the
new versions see the main SAGE website. http://modular.ucsd.edu/sage".

 4. There is a random "README.txt" for no reason also in the middle
of http://sagemath.org/src/changelogs/

 5. Finally, logging into the server I find that
http://sagemath.org/src-old/ has the old versions.  But how could I
find that otherwise?   Also, the description at the top of src-old
doesn't explain what it is accurately.  It would be better to say
"Here you can download the source code for any past version of Sage so
you can build it from source."

 6. This listing at http://sagemath.org/src-old/ also has various
random files like README.txt.in and install.html mixed in.

It would also be worth mentioning that we have many old sage install on sage.math. 

I wonder if it would also be good to archive bdists for one specific Linux release, e.g., 32-bit x86 Ubuntu 8.04 LTS?  Since then one can easily get a virtual machine and drop our binary in it.


---

Comment by was created at 2009-10-14 16:55:52

Harald has fixed the problems involving finding the old source.  Some of the directory listing and header problems remain.


---

Comment by timdumol created at 2009-10-25 19:44:26

Seems to me that almost every problem except the 6th problem is solved. There are still some random files at http://www.sagemath.org/src-old/


---

Comment by jdemeyer created at 2012-05-17 22:05:06

Harald, it seems to me that none of this is still relevant.  Do you agree?


---

Comment by jdemeyer created at 2012-05-17 22:05:06

Changing component from distribution to website/wiki.


---

Comment by jdemeyer created at 2012-05-17 22:05:06

Changing status from new to needs_review.


---

Comment by schilly created at 2012-05-17 22:16:09

`@`jdemeyer: honestly, i have no memory of that. a short introduction note for the src-old files is the only thing that is still open. we can close it, i'll add a note.


---

Comment by jdemeyer created at 2012-05-18 09:58:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-21 08:06:18

Resolution: fixed
