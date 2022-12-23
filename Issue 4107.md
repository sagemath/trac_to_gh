# Issue 4107: [with patch, needs review] trivial typos in tut.tex

Issue created by migration from https://trac.sagemath.org/ticket/4107

Original creator: GeorgSWeber

Original creation time: 2008-09-12 20:17:24

Assignee: somebody

(see the thread of the same name in sage-devel)


---

Comment by mabshoff created at 2008-09-12 23:06:48

Where is the patch? :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-13 00:06:26

I have attached a diff (not a patch) against 3.1.2.rc2 since not all fixes do apply any more due to the rewrite of the manual by John Palmieri. I left out the fix 

```
 There is one subtlety in defining complex numbers: as mentioned above, 
-the symbol \code{i} represents a square root of \minusone, but it is a 
+the symbol \code{i} represents the square root of \minusone, but it is a 
 \emph{formal} square root of \minusone; it is not in the complex numbers. 
 Calling \code{CC(i)} returns the complex square root of \minusone.
```

since there are multiple roots.

Cheers,

Michael


---

Comment by mhansen created at 2008-09-13 00:34:13

Looks good to me.


---

Attachment

Updated patch with changes commited in Minh Nguyen's name


---

Comment by mabshoff created at 2008-09-13 00:43:06

Resolution: fixed


---

Comment by mabshoff created at 2008-09-13 00:43:06

Merged in Sage 3.1.2.rc2
