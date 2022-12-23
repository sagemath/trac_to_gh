# Issue 8758: Add a top-level /data with static.File(DATA) that serves files from the data directory

Issue created by migration from https://trac.sagemath.org/ticket/8758

Original creator: acleone

Original creation time: 2010-04-24 22:58:06

Assignee: acleone

CC:  acleone was timdumol

Instead of having /js, /css, etc, we should serve all static data files out of /data.  For now this patch just adds /data using `child_data = static.File(DATA)`, where `static.File(path)` is defined in twisted.  It will serve files with the correct MIME type based on extension.

Eventually we should find all the /js and /css paths and change them to /data

At some point in the future we could even implement caching of all the static files easily by subclassing static.File(path), and making everything in /data cached.


---

Comment by acleone created at 2010-04-24 23:01:42

Adds the two static.File(DATA) calls to twist.py


---

Attachment


---

Comment by acleone created at 2010-04-24 23:02:01

Changing status from new to needs_review.


---

Comment by was created at 2010-04-25 00:28:08

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-25 00:28:08

Not a patch bomb.


---

Comment by acleone created at 2010-05-29 22:38:07

Changes the url to /static/.  Replaces previous.


---

Attachment

The latest patch changes the url to /static/.

I think we should also rename the "data" directory in the sagenb source to "static", and rename the global DATA to STATIC.

DATA is slightly confusing because uploading files to a worksheet also uses a DATA global, eg DATA+'mydatafile.txt'.


---

Comment by acleone created at 2010-06-02 23:14:25

Ok - ignore the new patch.  Let's leave the url as /data.


---

Comment by timdumol created at 2010-07-11 05:58:13

Resolution: fixed
