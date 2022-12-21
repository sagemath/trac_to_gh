# Issue 1945: [with patch] improve reference manual formatting

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-01-27 01:04:41

Assignee: tba

I've gone through and made some changes to improve the formatting of the reference manual.  Here are my commit comments:

```
Many changes to improve the refman.
1) Change SAGE->\sage many places
2) LaTeXify lots of math, literal strings, filenames, URLs, etc.
3) fix typos, adjust content in other minor ways
```

and

```
Miscellaneous changes to make the reference manual prettier.
1) Override python.sty so that list environments (itemize, etc.) inside
funcdesc environments work better.
2) Change SAGE->Sage several places.
3) Fix problem where sage.crypto.mq files were added to refman
"the old way".
4) Fix typos, adjust content in minor ways.
5) Improve reference manual autogeneration:
  a) only recognize "sage:" as doctest at the beginning of a line
  b) only remove "EXAMPLES:" if it's the only thing on the line
  c) start parsing "INPUT:" and "OUTPUT:" sections (so now you can
     include LaTeX markup)
  d) make parsing more flexible (authors can be separated by "*" as well
     as "--", for example)
  e) skip Cython file-location in module and class docstrings
  f) if __init__ method has a docstring, put it in the refman
  g) if a class includes a non-method, don't put it in the refman
  h) if a module docstring includes "nodoctest", replace it with
     useful text
  i) work even when -f ("force") argument is not given
```



---

Attachment

The hg_doc part of the patch


---

Attachment

The hg_sage part of the patch


---

Comment by cwitty created at 2008-01-27 01:08:21

I have verified that testall passes with this patch.


---

Comment by cwitty created at 2008-01-27 01:51:14

Jason reviewed the changes to calculus.py; he says:

```
 Okay, I've got to go, but I agree with all of your changes to calculus.py.
 (with the above exceptions :)
```

where "the above exceptions" are:

```
One change: 
 sage/calculus/calculus.py: line 1510
 with respect to $x$.
 (instead of "with respect to $n$."
```

and

```
<jason> cwitty: in calculus.py, you changed .arguments() to .args().  Both seem to work.  Why the change?
<jason> line 4440
<cwitty> Because it's the doctest for .args(); if I don't make the change, then the doctest isn't testing the right thing.
<jason> Especially since the docs to the function talk about .arguments()
<cwitty> Oops; looks like more things should be changed then.
<jason> oh, I didn't see that from the patch.
<cwitty> (Or the whole .args() method should be replaced with "args = arguments".)
<jason> That's my vote.  No code duplication then.
```



---

Comment by ncalexan created at 2008-01-27 04:22:01

I didn't go over this with a fine tooth comb, but all changes are minor and seem reasonable.  I say apply.


---

Comment by mabshoff created at 2008-01-27 05:21:28

I needed to apply hunk 1 from the safe library patch manually.


---

Comment by mabshoff created at 2008-01-27 05:21:44

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 05:21:44

Merged in Sage 2.10.1.rc1
