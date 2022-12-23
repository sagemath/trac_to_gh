# Issue 8512: database_stein_watkins_mini uses 'cp -v' which fails on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/8512

Original creator: drkirkby

Original creation time: 2010-03-12 23:48:03

Assignee: tbd

CC:  was

The optional package  "database_stein_watkins_mini" fails to install on Solaris 10, as 'cp' uses an illegal option -v, which is not defined by POSIX. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/cp.html

Since the GNU version of 'cp' only uses the -v option to show what is being done - from the 'cp' man page on Linux:


```
       -v, --verbose
              explain what is being done
```


The -v option can simply be removed.


---

Comment by drkirkby created at 2010-03-13 00:25:09

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-03-13 00:25:09

The solution to this GNUism was very easy - just remove the -v option.

I also added a *very incomplete* SPKG.txt file - previously there was no file called SPKG.txt. I leave it up to William or others with more knowledge to fill this in. It does at least document the change I made. 

The database can be found at http://boxen.math.washington.edu/home/kirkby/optional/database_stein_watkins_mini.p0/database_stein_watkins_mini.p0.spkg

Attached are a diff of the spkg-install and the new SPKG.txt

 == Note to the release manager. == 

There is no Mercurial repository - I this will have to be integrated manually.


---

Comment by drkirkby created at 2010-03-13 00:25:56

Brand new (but mostly incomplete) SPKG.txt


---

Attachment

Modified spkg-install, removing the '-v' option to 'cp'


---

Attachment


---

Comment by drkirkby created at 2010-03-13 23:45:03

Changing assignee from tbd to drkirkby.


---

Comment by was created at 2010-06-02 22:03:01

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-07 05:06:57

Resolution: fixed
