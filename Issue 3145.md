# Issue 3145: documentation and defaults for the 'view' function

Issue created by migration from https://trac.sagemath.org/ticket/3145

Original creator: jhpalmieri

Original creation time: 2008-05-09 19:16:33

Assignee: cwitty

Keywords: latex, view

I'm attaching a patch with, I suppose, three changes (two of which are minor) to the 'view' function:
 1. longer (and I think clearer) documentation
 2. no 'center' option anymore. I don't think centering things in displayed equations has any effect in LaTeX.
 3. changed default value of 'sep' from '$$ $$' to _.  I have two reasons for this: I think the output looks better this way, and I think that the default value of '$$ $$' is misleading: someone might infer that it's playing the role of the variables 'math_left' and 'math_right' in _latex_file, when in fact it's just adding some vertical space between the output lines.  If you don't like having a default of _, then I would suggest changing it to something like '\\vspace{5mm}' which gives a better idea of what 'sep' actually does and even implies how one might change it (by changing the length).


---

Comment by jhpalmieri created at 2008-05-09 19:17:15

patch to sage/misc/latex.py


---

Attachment

Sorry, I didn't look at the preview carefully enough.  In item 3, the default for 'sep' is changed from '$$ $$' to the empty string (two single quotes with no space between them), which I haven't yet figured out how to type here...


---

Comment by jhpalmieri created at 2008-05-25 16:18:47

mercurial patch (instead of diff), to replace previous patch


---

Attachment


---

Comment by craigcitro created at 2008-06-15 21:59:00

Changing keywords from "latex, view" to "latex, view, editor_wstein".


---

Comment by was created at 2008-06-16 00:44:27

REFEREE REPORT:

1. The new docs say "If in notebook mode, this embeds a png image in the output.".  That is not true.  view uses jsmath to typeset output -- this does not in any way involve png's.

2. There absolutely have to be some doctests added, e.g., examples illustrating what this function does.  E.g., you can in the doctest set the system to be in EMBEDDED_MODE, then get html  output, or something. 

3. I agree with removing center and the sep, i.e., with the core changes.

4.. I can't actually apply this patch to either sage-3.0.2 or sage-3.0.2.alpha2:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3145/3145.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3145/3145.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg status
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg status
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg import   "/home/was/.sage/temp/sage/32714/tmp_1.patch"
applying /home/was/.sage/temp/sage/32714/tmp_1.patch
patching file sage/misc/latex.py
Hunk #1 FAILED at 423
Hunk #2 FAILED at 452
2 out of 2 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej
abort: patch failed to apply
sage: 
```


So please do what you can from above and let me know.


---

Attachment

I've tried to address these issues.  I've also changed the documentation a little more, to reflect the fact that 'xdvi' is not required: dvi files are not necessarily displayed by xdvi -- see 

[http://trac.sagemath.org/sage_trac/ticket/3137](http://trac.sagemath.org/sage_trac/ticket/3137)

So I've tried to change the references to xdvi to be more accurate.


---

Comment by jhpalmieri created at 2008-06-16 05:13:01

(This latest patch was built using Sage 3.0.2.)


---

Attachment

part 2 of 2


---

Comment by was created at 2008-06-19 23:34:38

I did some slight changes in the followup patch.  This is now good to go.

Apply sage-3145-new.patch and sage-3145-new-part2of2.patch.


---

Comment by jhpalmieri created at 2008-06-20 02:23:30

Great, I was thinking about similar changes too.  I like it.


---

Comment by mabshoff created at 2008-06-23 11:09:49

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 11:09:49

Merged sage-3145-new.patch and sage-3145-new-part2of2.patch in Sage 3.0.4.alpha0
