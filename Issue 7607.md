# Issue 7607: add uncommitted files to the script repository

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-12-05 13:33:46

Assignee: mvngu

CC:  mhansen

With Sage 4.3.alpha0 and 4.3.alpha1, this shows up under the script repository:

```
~/Desktop/sage-4.3.alpha1/sage -hg st
? hmac256
? jmol
? pilconvert.py
? pildriver.py
? pilfile.py
? pilfont.py
? pilprint.py
? sphinx-autogen
```

Those files should be added using "hg add" and then checked in with "hg ci".


---

Comment by mhansen created at 2009-12-05 13:49:41

I don't think that those should be checked in since they are installed by spkgs.


---

Comment by mvngu created at 2009-12-05 13:56:34

based on Sage 4.3.alpha1


---

Comment by mvngu created at 2009-12-05 13:59:52

Changing component from documentation to misc.


---

Attachment

Replying to [comment:1 mhansen]:
> I don't think that those should be checked in since they are installed by spkgs.

Yes, good point! Would you consider configuring Mercurial to ignore those files? If so, I have attached the patch `trac_7607-hgignore.patch` to take care of the Mercurial configuration. That patch should be applied to the script repository.


---

Comment by mvngu created at 2009-12-05 13:59:52

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-06 08:28:24

Looks good to me.


---

Comment by mhansen created at 2009-12-06 08:28:24

Resolution: fixed
