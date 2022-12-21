# Issue 3785: upgrade atlas in sage to version 3.8.2

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-06 23:58:10

Assignee: was

This is a non-negotiable blocker for Sage-3.1.


---

Comment by mabshoff created at 2008-08-07 02:42:27

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-08-07 02:42:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-17 14:15:43

We need this for a quick build on the new sage.math hardware :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-02 05:56:50

The spkg at

http://sage.math.washington.edu/home/mabshoff/spkgs/atlas-3.8.2.spkg

fixes the following problems:

 * update to 3.8.2
 * better detection of Pentium D and E
 * detect more Core2Duos cores
 * properly detect Dunnington cores

In addition the spkg has been cleaned up. Build time:

 * on the new sage.math down from 180 minutes to 

```
real	11m36.903s
user	9m58.840s
sys	1m17.870s
```

 * On cleo/iras, i.e. Itanium2 machines on SkyNet:

```
real	37m34.354s
user	34m18.232s
sys	1m20.748s
```


This also fixes #3787

Cheers,

Michael


---

Comment by cremona created at 2009-01-02 09:20:54

Michael, do I have to wait until there's a 3.2.3.alpha before testing this?  I have been using 3.2.2 for a while now.  John


---

Comment by mabshoff created at 2009-01-02 15:45:11

Replying to [comment:5 cremona]:
> Michael, do I have to wait until there's a 3.2.3.alpha before testing this?  I have been using 3.2.2 for a while now.  John

This can be tested with any recent Sage release. William did some complete build of Sage with this ATLAS.spkg, so hopefully it will get a review soon :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-02 21:52:06

Resolution: fixed


---

Comment by mabshoff created at 2009-01-02 21:52:06

Merged in Sage 3.2.3.final

Cheers,

Michael
