# Issue 8740: Upgrade sqlalchemy to 0.6.0

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-04-21 19:28:18

Assignee: tbd

CC:  tdumol fbissey

The latest version of SQLAlchemy is now [0.6.0](http://www.sqlalchemy.org/trac/wiki/06Migration). This brings a bunch of changes, notably a native unicode mode, which would be a lot faster for unicode rich applications, such as the Sage Notebook.


---

Comment by timdumol created at 2010-04-21 19:43:21

Changing status from new to needs_review.


---

Comment by fbissey created at 2011-05-31 22:08:51

Now at 0.6.7 anyone wants to make a new spkg?


---

Comment by timdumol created at 2011-06-01 04:01:03

Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?


---

Comment by fbissey created at 2011-06-01 04:07:06

Replying to [comment:5 timdumol]:
> Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?

No objections, I seem to be in a reviewing mood. If you post it, I'll test it on a couple of systems.


---

Comment by timdumol created at 2011-06-01 04:30:38

Alright. Package made, but it's taking a bit of time to upload to server.


---

Comment by timdumol created at 2011-06-01 04:30:38

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2011-06-01 04:31:07

Here: http://sage.math.washington.edu/home/timdumol/sqlalchemy-0.7.0.spkg


---

Comment by timdumol created at 2011-06-01 04:31:07

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2011-06-01 13:00:46

everything is ok on x86 and amd64. I am testing this on OSX and then I'll give it a positive review.


---

Comment by fbissey created at 2011-06-01 23:40:49

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2011-06-01 23:40:49

Fine on OS X. No doctests to run or break and there is currently no SPKG check but that should be another ticket provided that sqlalchemy has some self-tests. Positive review from me.


---

Comment by jdemeyer created at 2011-06-08 07:40:03

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-06-08 07:40:03

SPKG.txt should mention version number 0.7*.0* instead of 0.7.  It would also be good to mention the ticket number in SPKG.txt


---

Comment by jdemeyer created at 2011-06-08 07:42:04

Note that in the mean time, SQLAlchemy 0.7.1 was released (http://www.sqlalchemy.org/download.html), maybe you might as well use that version?


---

Comment by jdemeyer created at 2011-06-18 08:59:39

*ping*


---

Comment by fbissey created at 2011-06-18 20:06:44

Sorry Jeroen, I have been busy with a couple of earthquakes and I was hoping Tim would make the new spkg.


---

Comment by mhansen created at 2012-03-28 21:22:32

I've updated the spkg to 0.7.6.


---

Comment by mhansen created at 2012-03-28 21:22:32

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2014-06-13 22:20:54

Ok, last version of sqlalchemy is now 0.9.4. Does not make much sense to run behind versions of pire Python modules. The following works perfectly on my computer

```
sage -sh
easy_install pip
pip install sqlalchemy==0.9.4
```

We should rather include `pip` in Sage as proposed in [this thread in sage-devel](https://groups.google.com/forum/#!topic/sage-devel/e48IruDu7Kg) and make 'sage -i sqlalchemy` points to the last version.


---

Comment by vdelecroix created at 2014-06-13 22:20:54

Changing status from needs_review to needs_info.


---

Comment by vbraun created at 2014-08-20 20:33:56

Resolution: wontfix
