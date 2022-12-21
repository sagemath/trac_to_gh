# Issue 7706: palp (lattice polytopes): replace the pickle-based database of lattice polytopes by a non-pickle database format

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 08:53:07

Assignee: mhampton

The Sage source distribution must ship with a bare minimum of opaque potentially dangerous binary files.   Pickles (i.e. sobjs) are opaque binary files that can invoke arbitrary code when being unpickled.  Also, sobj's have the drawback that they can someday break, and can be very hard to update and extend later.  They are also hard to scan for virus.     There are currently three places in the Sage source code that includes pickles:  
   * the pickle jar,
   * the database of lattice polytopes
   * the world map graph

For this ticket, please find a way to replace the lattice polytopes database spkg with something that contains no pickles.  One solution would be to put plain text files in polytopes_db-*.spkg that described the 2d and 3d lattice polytopes. Then make the sobj's only when the spkg is installed.   This would require making the spkg depend on the sage library (which is very reasonable). 

Another possibility would be to change your code so that the first time the lattice polytope table is needed, a plain text file is parsed (so there is never an sobj).  


---

Comment by was created at 2009-12-16 08:53:54

See also #7705.


---

Comment by novoselt created at 2009-12-16 15:52:59

Changing assignee from mhampton to novoselt.


---

Attachment

Based on 4.3.rc0


---

Comment by novoselt created at 2009-12-17 06:41:59

Must be placed in DB_HOME/reflexive_polytopes


---

Attachment

Must be placed in DB_HOME/reflexive_polytopes


---

Comment by novoselt created at 2009-12-17 07:00:10

4 sobj files should be removed and replaced with two attached text files.

After some thinking and adjusting internal functions it turned out to be possible to reduce computing time for databases from 15 minutes to about 5 seconds (by avoiding extra checks and using initial polytopes in normal form), which is about 10 times longer than it was taking to load pickled files, but still seems quite reasonable to me as a once-per-session computation. It also now has the advantage of cached points (which are dropped during pickling for faster unpickling).

Timing (on sage.math):

Before (with sobj's):


```
sage: time len(ReflexivePolytopes(3))
CPU times: user 0.51 s, sys: 0.02 s, total: 0.53 s
Wall time: 0.54 s
4319
sage: time len(ReflexivePolytopes(3))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4319

```


After (with text data files):


```
sage: time len(ReflexivePolytopes(3))
CPU times: user 5.04 s, sys: 0.25 s, total: 5.29 s
Wall time: 5.90 s
4319
sage: time len(ReflexivePolytopes(3))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4319
```



---

Comment by novoselt created at 2009-12-17 07:00:10

Changing status from new to needs_review.


---

Comment by was created at 2010-02-07 00:43:54

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 17:09:30

Is there a new `polytopes_db-*.spkg`?


---

Comment by mpatel created at 2010-02-10 17:09:30

Changing status from positive_review to needs_work.


---

Comment by novoselt created at 2010-02-11 04:17:25

Should be used instead of two data files attached earlier


---

Comment by novoselt created at 2010-02-11 04:19:45

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-02-11 13:12:06

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 13:12:06


```
 Please remember to update the relevant ticket fields --- the release
 managers use an automated script to generate lists of merged tickets.

```



---

Comment by mpatel created at 2010-02-11 15:04:42

Resolution: fixed
