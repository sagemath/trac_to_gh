# Issue 6843: Permission problem when uploading worksheet

Issue created by migration from https://trac.sagemath.org/ticket/6843

Original creator: wjp

Original creation time: 2009-08-29 17:21:25

Assignee: boothby

When trying to upload a .sws that contains directories with permission 700, the unpacked directories are still 700 and owned by the user running the notebook.

When running the notebook with `server_pool=['other_user`@`localhost']`, evaluating the cells then fails with


```
IOError: [Errno 13] Permission denied:
'/home/other_user/sage_notebook/worksheets/user/7/code/1.py'
```


because `.../7/code/` is 700.

When creating a new worksheet manually this directory is 755 and evaluating cells in that worksheet works properly.


---

Attachment

sws that shows this problem


---

Attachment

I attached a patch that does a `chmod -R go-rwx,+rwX *` on the untarred sws file, to make the unpacked files match the current umask. (Both in the restrictive and permissive directions.)


---

Comment by iandrus created at 2009-10-31 12:02:38

Changing status from needs_review to needs_work.


---

Comment by iandrus created at 2009-10-31 12:02:38

I think we should use && instead of ; to ensure sure that we don't change the permissions of other files if we can't cd to the directory.


---

Comment by wjp created at 2009-10-31 12:50:30

If tmp_dir() failed to create a directory we can cd to, tmp_dir would/should already have thrown an exception. If it doesn't, that's a different issue than the one this patch addresses, and should be solved by fixing tmp_dir, in my opinion.


---

Comment by wjp created at 2009-10-31 12:51:02

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-12-08 20:08:35

Resolution: fixed


---

Comment by was created at 2009-12-08 20:08:35

This was fixed in my rewrite of how notebook evaluates code.  In particular "When creating a new worksheet manually this directory is 755 and evaluating cells in that worksheet works properly." isn't an issue since all code gets evaluated in a special /tmp directory that is created by the server and has permissions carefully set.  Moreover, the code in the worksheet storage directory now has all permissions very carefully set using platform independent Python functions.
