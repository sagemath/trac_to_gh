# Issue 7973: Documentation for submitting a patch is overly confusing

Issue created by migration from Trac.

Original creator: gaer

Original creation time: 2010-01-18 07:06:59

Assignee: mvngu

"Producing patches with Mercurial" is overly informative and thus hides the basic info.


---

Comment by mvngu created at 2010-01-18 07:10:36

Is this a duplicate of #6987?


---

Attachment

Mercurial documentation simplifications/patches


---

Comment by gaer created at 2010-01-18 07:53:23

Changing status from new to needs_review.


---

Comment by gaer created at 2010-01-18 07:53:23

This is not the same as 6987 which suggests moving the entire section to a different location in the manual.  That might be a good idea, but this is a revision of the actual content, not a change in the location.  

And one probably shouldn't perform the location changes requested in 6987 without first applying the above patch to the actual text.


---

Attachment

for reference only; don't apply


---

Comment by mvngu created at 2010-01-18 08:11:55

for reference only; don't apply


---

Attachment

for reference only; don't apply


---

Comment by mvngu created at 2010-01-18 08:17:05

Changing status from needs_review to needs_work.


---

Attachment

You're concatenating three different patches into one file. That would result in failures when applying the resulting one file (with the three patches):

```
[mvngu`@`mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7973/13639.patch && hg qpush
adding 13639.patch to series file
applying 13639.patch
patching file doc/en/developer/producing_patches.rst
Hunk #1 FAILED at 21
Hunk #2 FAILED at 58
2 out of 2 hunks FAILED -- saving rejects to file doc/en/developer/producing_patches.rst.rej
patching file doc/en/developer/producing_patches.rst
Hunk #1 FAILED at 21
Hunk #2 FAILED at 58
2 out of 2 hunks FAILED -- saving rejects to file doc/en/developer/producing_patches.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 13639.patch
```

Looking at the attachment [13639.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.patch) more closely, I see that the three patches only touch the file

```
doc/en/developer/producing_patches.rst
```

I have split the three different patches into three different files and attached them to this ticket for reference. Applying any one of them individually is OK. But if I then first apply one and then any of the other two, I'd get hunk failures. So of all the changes in your original attachment, which set of changes did you intend to submit for review? Also, one minor nit-pick: please reference the ticket number in your commit message. The general format of a commit message should be:

```
trac xxxx: <your-commit-message-here>
```

where "xxxx" is the ticket number.


---

Attachment

Revised patching doc patch


---

Comment by gaer created at 2010-01-18 09:08:37

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-01-18 09:56:19

reviewer patch


---

Attachment

I'm OK with the proposed changes in [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch). I have attached a reviewer patch [trac_7973-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/trac_7973-reviewer.patch), which fixes some typos. The attachment [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch) contains some tab characters, which don't look good when you view the HTML version of the Developer's Guide, i.e. only the corresponding section in the Developer's Guide. Try to avoid tabs as much as possible in patches. If you're OK with the reviewer patch, then the whole ticket gets a positive review.


---

Comment by jhpalmieri created at 2010-01-18 15:44:29

Now wait, what's wrong with "Cardinal Fang"?  According to [the Python documentation](http://docs.python.org/tutorial/appetite.html), 

```
Making references to Monty Python skits in documentation is not only allowed, it is encouraged!
```

Since Sage is written in Python, "Cardinal Fang" seems completely appropriate. :)


---

Comment by gaer created at 2010-01-18 20:12:11

Replying to [comment:6 jhpalmieri]:
> Now wait, what's wrong with "Cardinal Fang"?  According to [the Python documentation](http://docs.python.org/tutorial/appetite.html), 
> {{{
> Making references to Monty Python skits in documentation is not only allowed, it is encouraged!
> }}}
> Since Sage is written in Python, "Cardinal Fang" seems completely appropriate. :)
> 

That change was a direct request from wstein, who is, apparently, the anti-Python(Monty). :-)


---

Comment by gaer created at 2010-01-18 20:15:07

Replying to [comment:5 mvngu]:
> I'm OK with the proposed changes in [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch). I have attached a reviewer patch [trac_7973-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/trac_7973-reviewer.patch), which fixes some typos. The attachment [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch) contains some tab characters, which don't look good when you view the HTML version of the Developer's Guide, i.e. only the corresponding section in the Developer's Guide. Try to avoid tabs as much as possible in patches. If you're OK with the reviewer patch, then the whole ticket gets a positive review.

All those reviewer changes are spot on.  Thanks!  It's good to go for me.


---

Comment by gaer created at 2010-01-18 20:15:07

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-18 22:26:08

Sage isn't Python, and I think it's funner in math software to have references to math-related items.  The vast majority of potential Sage users and developers will have no clue about these Python in jokes, and I don't want to confuse them.


---

Comment by rlm created at 2010-01-19 00:40:09

Resolution: fixed
