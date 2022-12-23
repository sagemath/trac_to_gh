# Issue 7495: notebook: get rid of all possible "internal server errors" when doing "Data --> Upload or attach file"

Issue created by migration from https://trac.sagemath.org/ticket/7495

Original creator: was

Original creation time: 2009-11-20 00:34:35

Assignee: boothby

Uploading or attaching an empty file or a file that doesn't exist, etc. can cause internal server errors instead of a proper error message.

Moreover, notice these lines in twist.py:

```
class Worksheet_do_upload_data
...
        dest = os.path.join(self.worksheet.data_directory(), name)
        if os.path.exists(dest):
            os.unlink(dest)
```


With a properly crafted URL I bet name could contain .. and hence one could make the notebook *server* delete any file it has access to!  This is a critical security vulnerability. 

See also #3849 for similar issues when uploading a worksheet. 


---

Comment by was created at 2009-11-20 01:44:32

Yes, this is fully exploitable and allows one to delete any file on the server:
E.g., on my laptop I created a file tmp/xyz, then pasted in this url, and that file was deleted. 


```
http://localhost:8000/home/admin/13/do_upload_data?urlField=%27%27&nameField=../../../../../../../../tmp/xyz
```


With a little more work, one could not only delete any file, but I think *replace* it by a file of ones choice.  That's a pretty massive exploit.  

So I'm upping this to a blocker and fixing it now.


---

Comment by was created at 2009-11-20 01:44:32

Changing priority from critical to blocker.


---

Comment by jason created at 2009-11-20 01:49:09

Can you do a quick grep through the source to see if any os.* functions are used in a like manner in the notebook?


---

Comment by was created at 2009-11-20 02:18:12

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2009-11-20 03:50:21

Creating a new file with name `&` raises an OSError.


---

Comment by mpatel created at 2009-11-20 03:52:32

Replying to [comment:4 mpatel]:
> Creating a new file with name `&` raises an OSError.
Actually, clicking to delete this file raises the error:

```
        exceptions.OSError: [Errno 21] Is a directory: '/home/apps/.sage/sage_notebook.sagenb/home/admin/88/data/'

```



---

Attachment

Version 2.  Minor simplifications.  Apply only this patch to sagenb repo.


---

Comment by mpatel created at 2009-11-20 06:41:57

I think the `OSError` above is a separate URI encoding problem.


---

Comment by mpatel created at 2009-11-20 06:43:00

Anyway, my digression aside, my review is positive, as far as it goes.


---

Comment by mpatel created at 2009-11-20 07:09:31

Replying to [comment:6 mpatel]:
> I think the `OSError` above is a separate URI encoding problem.
This is now #7500.


---

Comment by was created at 2009-11-24 15:55:32

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-24 15:55:32

"Anyway, my digression aside, my review is positive, as far as it goes. "  so positive review.


---

Comment by was created at 2009-12-07 16:47:07

Resolution: fixed


---

Comment by was created at 2009-12-07 16:47:07

merged into sage-4.3
