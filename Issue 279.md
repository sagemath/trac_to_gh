# Issue 279: Add test a range of revisions

Issue created by migration from https://trac.sagemath.org/ticket/279

Original creator: ncalexan

Original creation time: 2007-02-22 23:57:12

Assignee: was

Keywords: test hg mercurial

I often want to test only files touched by a range of revisions.  It would be nice if there was a 'test revisions' command, so sage -tr branch:tip, sage -tr 1023, etc queried hg for changes and only tested those files.


---

Comment by ncalexan created at 2007-02-25 08:57:46

Changeset 0e2d1b3b9389 changes sage -tnew rev to support this.


```
# By default, we compare to tip.  However, it is handy to compare against
# a certain revision, perhaps tagged 2.2 or similar:
#
# EXAMPLES:
#
# Find things modified but not committed:
# % sage -tnew tip
#
# Find things modified since 2.2:
# % sage -tnew 2.2
#
# Find things modified between 2.1 and 2.2:
# % sage -tnew 2.1:2.2
```



---

Comment by ncalexan created at 2007-02-25 08:57:46

Resolution: fixed


---

Attachment
