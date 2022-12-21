# Issue 3470: [with spkg; needs review] add pyprocessing (=multiproccessing) to sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-19 16:32:23

Assignee: yi

This has been officially excepted for Python 2.7, but we need it now.  It is Python/c and takes literally 1 second to install, and supports OSX, Linux, Windows, etc.


---

Attachment

spkg contains spkg-check, SPKG.txt, hg repo.  Works on debian/xeon.  Needs testing on other platforms.


---

Comment by gfurnish created at 2008-06-19 18:08:53

Having looked at the source, I'm very worried about the lack of comments, but the design is solid.  The socket io code is poor - its not very robust or fast compared to twisted.  However, it "just works" as of now, and as long as it is hidden entirely behind the parallel api (so that we don't have any pyprocessing specific functions), I approve of this spkg from a code review perspective.


---

Comment by yi created at 2008-06-19 20:56:37

Looks good to me, pretty straightforward spkg. Also I'm not worried too much about the code since it will be included upstream in python 2.7 and it will have to adhere to Python's coding standards.


---

Comment by was created at 2008-06-24 17:10:55


```
Anyway, since every single person voted +1 and nobody voted -1 or
had issues, I declare this package officially accepted.

 -- William
```



---

Comment by was created at 2008-06-24 17:29:40

Nick wants the vote reopened for two more days, so I reopened it until Thursday.


---

Comment by mabshoff created at 2008-06-26 04:02:07

In the end the vote was positive and no one voted against it. It is nearly Thursday, so I am merging this. I did end up adding a `.hgignore` and check some more files into the repo. I also renamed the spkg `pyprocessing-0.52.spkg`. Additional positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 04:12:01

Resolution: fixed


---

Comment by mabshoff created at 2008-06-26 04:12:01

Merged in Sage 3.0.4.alpha1
