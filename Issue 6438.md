# Issue 6438: Upgrade to Cython 0.11.2

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-06-28 09:03:55

Assignee: mabshoff

At the very least, native complex support will be valuable. 

The spkg at http://sage.math.washington.edu/home/robertwb/cython/ built and passed all doctests a couple of versions back. 


---

Comment by mhansen created at 2009-07-17 19:35:27

Here is a direct link: http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.spkg


---

Comment by robertwb created at 2009-07-17 21:55:28

We should update to the latest tip to fix the numpy issue.


---

Comment by jason created at 2009-07-19 03:59:47

Does your comment mean that we need a new spkg?  Is this a "needs work" ticket now?


---

Comment by jason created at 2009-07-19 04:13:26

On the other hand, the spkg seems fine, except that the SPKG.txt file does not include a changelog of any sort.  Shouldn't this be added?


---

Comment by robertwb created at 2009-07-21 19:45:13

http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.1.spkg

I don't see anything in SPKG.txt that needs changing--the changelog would be pretty boring if it was there ("Upgraded to version x.y.z" * 100).


---

Attachment

All tests pass with the above spkg and patch.


---

Comment by mvngu created at 2009-07-24 12:00:39

The SPKG at

http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.1.spkg

doesn't contain a file called `.hgignore` like the current version in Sage 4.1. So when one executes the command

```
hg status
```

one sees a lot of source files. I've added a `.hgignore` file to the repository of that SPKG. The updated SPKG is up at

http://sage.math.washington.edu/home/mvngu/patch/cython-0.11.2.1.spkg

All doctests passed with the latter SPKG and `6438-cython.patch`.


---

Comment by mvngu created at 2009-07-24 13:41:08

Resolution: fixed
