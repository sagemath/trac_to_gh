# Issue 9223: improve doctest coverage of databases/cremona.py

Issue created by migration from https://trac.sagemath.org/ticket/9223

Original creator: AlexGhitza

Original creation time: 2010-06-12 09:26:59

Assignee: mvngu

Keywords: cremona elliptic curve database

As of sage-4.4.3, we have:


```
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE cremona.py: 42% (17 of 40)

Missing documentation:
	 * _init(self, ftpdata):
	 * __repr__(self):
	 * CremonaDatabase():


Missing doctests:
	 * rebuild(data_tgz, largest_conductor, decompress=True):
	 * __init__(self, read_only=True):
	 * __iter__(self):
	 * __getitem__(self, N):
	 * __repr__(self):
	 * allbsd(self, N):
	 * allcurves(self, N):
	 * allgens(self, N):
	 * degphi(self, N):
	 * elliptic_curve_from_ainvs(self, N, ainvs):
	 * elliptic_curve(self, label):
	 * iter(self, conductors):
	 * isogeny_classes(self, conductor):
	 * isogeny_class(self, label):
	 * list(self, conductors):
	 * _init_allcurves(self, ftpdata, largest_conductor=0):
	 * _init_degphi(self, ftpdata, largest_conductor=0):
	 * _init_allbsd(self, ftpdata, largest_conductor=0):
	 * _init_allgens(self, ftpdata, largest_conductor=0):
	 * __init__(self, read_only=True):
```



---

Comment by AlexGhitza created at 2010-06-12 11:47:41

After the patch:


```
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE cremona.py: 85% (34 of 40)

Missing documentation:
	 * _init(self, ftpdata):


Missing doctests:
	 * rebuild(data_tgz, largest_conductor, decompress=True):
	 * _init_allcurves(self, ftpdata, largest_conductor=0):
	 * _init_degphi(self, ftpdata, largest_conductor=0):
	 * _init_allbsd(self, ftpdata, largest_conductor=0):
	 * _init_allgens(self, ftpdata, largest_conductor=0):
```


I'm not sure how to test the remaining ones...


---

Attachment


---

Comment by AlexGhitza created at 2010-06-12 11:49:15

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-12 16:55:31

I applied the patch successfully to a 4.4.4.alpha0 build, which did not at first have the optional database installed.  I tested that the command to install it worked as advertised, and that all tests in sage/databases/cremona.py passed, with and without -optional.  I noticed a real bug and some cosmetic stuff, and made a new patch (reviewer patch, to be applied after the main one).  Then to test that I went to a different machine which did not have the optional database installed, applied both patches and tested the non-optional tests, then installed the optional database and tested both non-optional and non-optional tests.  Phew!

Here's the thing I found of actual substance:  in the iterator, the parameter should be a complete list of conductors, or a generator object, and *not* the first and last conductor wanted.  So in the function and test as it was, the iterator delivers the three curves of conductor 11 and nothing else!

Finally, I agree that it is not reasonable to test the (re)-installation of the database in the normal way, since for a start it takes a long time.  I think we need some input from William on this.  Around 2006 I was updating the database regularly, and giving him access to the new tgz file, but since then it has happened only rarely.  But it is very important that it still works!


---

Comment by cremona created at 2010-06-12 17:08:38

Apply after previous patch


---

Attachment

PS Apart from that range issue, I give a positive review to everything else Alex did, so all we need is someone to review my additional patch, and a decision on what to do about the remaining missing tests.  Can we tag them as "not tested" with some extra explanatory code?  Of course, somce one other than William ought to test the rebuilding of the database, and it should probably be me as I am the only one who has the raw data.


---

Comment by AlexGhitza created at 2010-06-13 00:34:09

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-06-13 00:34:09

John's reviewer patch looks good to me.  Sorry about the iterator business: when I tested that method, I realised that it was broken but for some reason I put [11, blah] instead of the [11..blah] that I intended.  Your revised tests for that also make more sense.

I agree that we want the database installation code to keep working, but I really don't know how/whether we can doctest this.  It's an issue that concerns all the databases so it would be good to have a general solution.  I'd like to ask about this on sage-devel, and if we can get a good method going it can be implemented on a new ticket.

In the meantime, it's better to get the things on this ticket going.


---

Comment by ddrake created at 2010-07-22 07:48:24

Resolution: fixed
