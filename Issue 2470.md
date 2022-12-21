# Issue 2470: dsage docs in tutorial -- can't tex them

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-11 07:59:09

Assignee: yi

I can't tex tut.tex unless the dsage section is commented out.  Also there is some "to be written..." section in there -- this is not appropriate for the tutorial, which is meant to be a very very polished documented. 


---

Comment by yi created at 2008-03-11 20:07:28

Thanks for catching that. I will attempt to fix it and post a patch. Is David Joyner the right person to ask about TeX related questions pertaining to the tutorial? I remember that I had problems putting in indexes.


---

Comment by yi created at 2008-03-11 20:07:37

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-03-24 16:53:43

Patch looks good to me. Constructs like ``foo'` will likely cause trouble while TeXing, but we can deal with that once we get closer to release. Yi, feel free to post a followup patch to resolve those issues and I will merge it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-24 16:54:58

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 16:54:58

Merged in Sage 2.11.alpha2
