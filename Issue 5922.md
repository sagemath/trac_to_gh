# Issue 5922: doctesting sage tree does not work when SAGE_ROOT is a symbolic link

Issue created by migration from https://trac.sagemath.org/ticket/5922

Original creator: was

Original creation time: 2009-04-28 21:05:38

Assignee: mabshoff

If you make a symbolic link to SAGE_ROOT, then doctesting will not work at all:


```
wstein@bsd:~$ ln -s build/sage-3.4.1 xyz
wstein@bsd:~$ cd xyz
wstein@bsd:~/xyz$ ls
0.png			devel			ipython			sage-python		test.sobj
COPYING.txt		dist			local			sage.png		testlong.log
HISTORY.txt		docs-0.html		makefile		sage0.png		tmp
README.txt		examples		sage			sage1.png		tmp.sws
data			install.log		sage-README-osx.txt	spkg
wstein@bsd:~/xyz$ ./sage -t devel/sage/sage/plot/plot3d/parametric_plot3d.py 
sage -t  "devel/sage/sage/plot/plot3d/parametric_plot3d.py" 
  File "./parametric_plot3d.py", line 18
    from devel/sage/sage/plot/plot3d/parametric_plot3d import *
              ^
SyntaxError: invalid syntax

	 [0.8 s]
exit code: 1024
 
```


The reason for this is related to *my* bugfix for testing files outside the tree.  Basically, that we're in the tree is not detected correctly in the case of symlinks, so the doctest program decides we are not in the tree, hence tries to import the function.  This, of course, fails. 

Ideas for solutions:
  
  1. Use a different command line option for testing outside tree.
 
  2. Improve detection of whether or not in Sage tree. 



---

Comment by mpatel created at 2009-08-11 03:48:40

I think the "scripts_doctest" patch at #6645 fixes this problem by using `os.path.realpath()` to expand symbolic links.

If this is true, please consider closing this ticket if/when #6645 merges.


---

Comment by mpatel created at 2009-10-15 18:09:18

Changing status from new to needs_info.


---

Comment by mpatel created at 2010-01-20 11:28:02

Let's close this?


---

Comment by mvngu created at 2010-02-01 01:46:38

Close as fixed by #6645.


---

Comment by mvngu created at 2010-02-01 01:46:38

Resolution: fixed
