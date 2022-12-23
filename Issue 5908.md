# Issue 5908: [with patch; needs review] fix issues/bugs with load/attach

Issue created by migration from https://trac.sagemath.org/ticket/5908

Original creator: was

Original creation time: 2009-04-27 03:38:23

Assignee: cwitty

CC:  mvngu

From Rado

```
Alright, here is my first open-source project patch:

http://www.math.uiuc.edu/~rkirov2/sage/11803.patch

The description in the patch file is short because vi is driving me
insane. I was going to add a better description in the .patch file
with gedit but wasn't sure if it is checksumed. Here is more detailed
description of what the patch does:

- for sage prompt, I added attached_files to the imported functions in
sage.misc.all
- for sage prompt, I added detach magic word (to mirror the build-in
behaviour in the notebook).
- for notebook attach and load, I used shlex.split (shlex is a
standard python library for shell commands), instead of regular split.
This makes sure that if your file has spacebars you can still call it
as long as it is enclosed by double-quotation marks i.e. "file1".
- for notebook detach, there was a simple bug (I must be the first one
to use it), where variable "filename" was referenced before being
defined.
- for notebook I exposed the build in function "attached_files()", by
adding it the preparser. This is a bit hacky, since it makes it look
like a function but it is not. Things like "detach attached_files()
[0]" won't work in notebook.

One thing worth mentioning is that in sage prompt, load and attach
cannot work with multiple files like in notebook. I figured that
ideally the prompt preparser should be unified with the notebook one
(the notebook code for loading and attaching is quite different),
which is a bigger project and should be well-thought out first.

Rado
```



---

Attachment

This has an eval in there that seems really bad to me.  And no doctests.  (I once added the machinery to doctest such things, did it ever get merged?)


---

Comment by rkirov created at 2009-06-18 00:19:12

I put eval, because I mimicked the code for "attach" that was already there. I can put some doctests, but is there a guide to doing proper doctests, especially doctests which create temp files and erase them after?


---

Comment by mpatel created at 2010-01-16 19:37:43

With the merge of #7514, should we close this ticket?


---

Comment by mvngu created at 2010-02-01 08:12:55

Resolution: invalid


---

Comment by mvngu created at 2010-02-01 08:12:55

Close as invalid. If you want to address any specific issue mentioned in the description of this ticket, please open a concise ticket addressing that one issue. I find the goal of the ticket too broad and the ticket's subject too vague.


---

Comment by rkirov created at 2010-02-02 07:11:08

yeah, i tested and most of it was fixed. There is still an issue with spacebar in names and also "attach" and "load" work like "print" (in python <3.0) along with their functions. I will make a ticket for those when i have time. At least the notebook and prompt behavior is consistent.
