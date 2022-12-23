# Issue 7464: [with spkg; needs review] Remove '-v' option from 'cp' command (GNUism) in database_cremona_ellcurve

Issue created by migration from https://trac.sagemath.org/ticket/7464

Original creator: drkirkby

Original creation time: 2009-11-14 20:33:48

Assignee: drkirkby

CC:  was drkirkby

Keywords: optional GNUism

The use of a non-POSIX option '-v' to the 'cp' command prevents this package installing on Solaris. The option, which can also be written as --verbose, is only to show what is actually being copied, so removing it should have no impact. 
Therefore

```
cp -rv cremona $SAGE_DATA/
```

was changed to 

```
cp -r cremona $SAGE_DATA/
```

in spkg-install. 

I also renamed 'SAGE.txt' to SPKG.txt, and added a slightly better description, and upstream contact information, to make it more consistent with other packages. 

This is an optional Sage package. 

It is unusual in that the .spkg file, was a tar file, and not a compressed tar file as they usually are. 

The updated files can be found at: 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/database_cremona_ellcurve/




---

Comment by drkirkby created at 2009-11-14 20:37:47

Changing status from new to needs_review.


---

Comment by was created at 2009-11-17 06:59:29

> It is unusual in that the .spkg file, was a tar file, and 
> not a compressed tar file as they usually are. 

This is the case for all databases of compressed files.  One makes a non-compressed spkg by doing

```
   sage -pkg_nc directory_name
```



---

Comment by drkirkby created at 2009-11-17 23:03:30

Thank you for the information. I used 'tar' to create it, rather than Sage with any option. It seems to work for me. Perhaps you can test it and review it.


---

Comment by cremona created at 2009-11-22 12:17:25

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2009-11-22 12:17:25

This looks fine to me. I read the changed files and also successfully installed it onto 4.2.1.  I am happy to be the upstream contact (and would expect to be contacted if anyone found an error in the database).  I should probably volunteer to be the spkg maintainer, but (embarrassingly) I do not even know the format of the main data file "cremona" in there!  So in practice William is the maintainer.  I will ask him to give me instructions....


---

Comment by was created at 2009-11-22 21:57:30

>  I do not even know the format of the main data file "cremona" in there! 
> So in practice William is the maintainer. I will ask him to give me instructions.... 

It's just a Python pickle.

William


---

Comment by mhansen created at 2009-11-29 05:39:06

Resolution: fixed


---

Comment by mhansen created at 2009-11-29 05:39:06

Copied into optional packages.
