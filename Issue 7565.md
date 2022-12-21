# Issue 7565: README.txt: enhance instructions on installing binary distribution

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-11-30 23:04:10

Assignee: mvngu

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/4a36a68dcd5a9190):

```
> My two-cent, but you probably know already: Say as root, you build
> Sage and then move the resulting binary to a different directory.
> After moving the whole Sage (binary) directory, you need to start up
> Sage as root at least once before you use Sage as another user.

I guess David's point was that this information should be stated more
clearly in the Readme text.
```



---

Comment by mvngu created at 2009-11-30 23:19:07

new README.txt file, based on Sage 4.3.alpha0


---

Attachment

differences between old and new README.txt files; do not apply


---

Comment by mvngu created at 2009-11-30 23:23:45

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-11-30 23:23:45

I have attached a new `README.txt` file. The patch `readme.patch` shows the differences between the old and new README.txt files. You should not apply that patch because the `SAGE_ROOT` directory is not under revision control. Instead, you should only replace the old `README.txt` with the newer, attached `README.txt`. A related ticket is #7553.


---

Comment by mhansen created at 2009-12-01 08:28:50

Resolution: fixed


---

Comment by mhansen created at 2009-12-01 08:28:50

Looks good.
