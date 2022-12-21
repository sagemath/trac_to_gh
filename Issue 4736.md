# Issue 4736: The doctesting doesn't always report segfaults properly

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-07 05:46:15

Assignee: gfurnish

When reintroducing the bug from #4540 on purposed the doctesting framework after applying #717 and #4719 has trouble detecting segfualts and summarizing them at the end. For example consider this failure:

```
sage -t  "devel/sage/sage/combinat/sf/kschur.py"           
Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in
'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult(1)
       [3.1 s]
```

When running "-tp 8 -long" the failure is reported as:

```
 sage -t -long devel/sage/sage/combinat/sf/kschur.py # 0 doctests failed
```


Cheers,

Michael


---

Attachment


---

Comment by gfurnish created at 2008-12-07 05:48:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-07 06:44:31

Patch looks nice, but there are two small problems:

For -t the new line is missing before the time is being printed. I consider this cosmetic, but other people might be annoyed:

```
sage -t  "devel/sage/sage/combinat/sf/homogeneous.py"       	 [3.1 s]
```

CTRL-C isn't caught properly - at least it shouldn't print "Error!!!" with "-t":

```
sage -t  "devel/sage/sage/combinat/sf/jack.py"              Error!!!
	 [8.5 s]
```

For -tp CTRL-C now seems to kill all doctests:

```
sage -t  devel/doc/const/const.tex
Error!!!

	 [1.8 s]
sage -t  devel/doc/tut/tut.tex
Error!!!

	 [1.7 s]
sage -t  devel/doc/prog/prog.tex
Error!!!

	 [1.8 s]

The following tests failed:

	sage -t  devel/doc/const/const.tex # KeyboardInterrupt
	sage -t  devel/doc/tut/tut.tex # KeyboardInterrupt
	sage -t  devel/doc/prog/prog.tex # KeyboardInterrupt
-------------------------------------------------------------------
```

I think this is the desired behavior since now the timeout kills run away jobs properly.

Cheers,

Michael


---

Attachment

Apply on top of existing patch.


---

Comment by mabshoff created at 2008-12-10 08:55:54

Very nice, the second patch fixes all the issues I reported. Great work Gary!

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 08:56:38

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-10 08:56:38

Resolution: fixed
