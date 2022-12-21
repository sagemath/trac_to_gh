# Issue 9082: Some unnecessary files being modified

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-29 07:28:36

Assignee: GeorgSWeber

CC:  dimpase jdemeyer

Keywords: beginner

When one build sage, the modification times of the following 3 files are changed. 


```
./README.txt
./COPYING.txt
./sage-README-osx.txt
```


Whilst not a major problem in itself, it does mean that 'make distclean' does not return the source tree to its original state. 

If one runs

```
$ 'make distclean'
$ find . -mtime -2
```

it will list all files modified in the last two days. Those files should not modified but they are. Some files created in the build process are not being removed, but they should be. That will be the subject of another ticket.





---

Comment by drkirkby created at 2010-05-29 07:38:52

The other relevant ticket is #9083. These are two different but related problems, since

 * The modification of unnecessary files. 
 * Failing to remove files or directories with 'make distclean'

both result in 'make distclean' not doing what it should do.


---

Comment by rws created at 2014-02-11 17:23:09

Changing keywords from "beginner" to "makefile".


---

Comment by mkoeppe created at 2016-10-28 04:09:19

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2016-10-28 04:09:19

This ticket seems outdated. I propose to close it


---

Comment by dimpase created at 2016-10-28 12:25:36

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2016-10-28 12:25:36

Agreed. This is no longer the case; besides, the 1st file is renamed and became README.md, and the 3rd file is gone.


---

Comment by vbraun created at 2017-01-21 18:03:11

Resolution: invalid
