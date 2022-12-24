# Issue 5922: doctesting sage tree does not work when SAGE_ROOT is a symbolic link

archive/issues_005922.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf you make a symbolic link to SAGE_ROOT, then doctesting will not work at all:\n\n\n```\nwstein@bsd:~$ ln -s build/sage-3.4.1 xyz\nwstein@bsd:~$ cd xyz\nwstein@bsd:~/xyz$ ls\n0.png\t\t\tdevel\t\t\tipython\t\t\tsage-python\t\ttest.sobj\nCOPYING.txt\t\tdist\t\t\tlocal\t\t\tsage.png\t\ttestlong.log\nHISTORY.txt\t\tdocs-0.html\t\tmakefile\t\tsage0.png\t\ttmp\nREADME.txt\t\texamples\t\tsage\t\t\tsage1.png\t\ttmp.sws\ndata\t\t\tinstall.log\t\tsage-README-osx.txt\tspkg\nwstein@bsd:~/xyz$ ./sage -t devel/sage/sage/plot/plot3d/parametric_plot3d.py \nsage -t  \"devel/sage/sage/plot/plot3d/parametric_plot3d.py\" \n  File \"./parametric_plot3d.py\", line 18\n    from devel/sage/sage/plot/plot3d/parametric_plot3d import *\n              ^\nSyntaxError: invalid syntax\n\n\t [0.8 s]\nexit code: 1024\n \n```\n\n\nThe reason for this is related to *my* bugfix for testing files outside the tree.  Basically, that we're in the tree is not detected correctly in the case of symlinks, so the doctest program decides we are not in the tree, hence tries to import the function.  This, of course, fails. \n\nIdeas for solutions:\n  \n1. Use a different command line option for testing outside tree.\n \n2. Improve detection of whether or not in Sage tree. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5922\n\n",
    "created_at": "2009-04-28T21:05:38Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "doctesting sage tree does not work when SAGE_ROOT is a symbolic link",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5922",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/5922





---

archive/issue_comments_046821.json:
```json
{
    "body": "I think the \"scripts_doctest\" patch at #6645 fixes this problem by using `os.path.realpath()` to expand symbolic links.\n\nIf this is true, please consider closing this ticket if/when #6645 merges.",
    "created_at": "2009-08-11T03:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5922#issuecomment-46821",
    "user": "mpatel"
}
```

I think the "scripts_doctest" patch at #6645 fixes this problem by using `os.path.realpath()` to expand symbolic links.

If this is true, please consider closing this ticket if/when #6645 merges.



---

archive/issue_comments_046822.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-10-15T18:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5922#issuecomment-46822",
    "user": "mpatel"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_046823.json:
```json
{
    "body": "Let's close this?",
    "created_at": "2010-01-20T11:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5922#issuecomment-46823",
    "user": "mpatel"
}
```

Let's close this?



---

archive/issue_comments_046824.json:
```json
{
    "body": "Close as fixed by #6645.",
    "created_at": "2010-02-01T01:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5922#issuecomment-46824",
    "user": "mvngu"
}
```

Close as fixed by #6645.



---

archive/issue_comments_046825.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-01T01:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5922#issuecomment-46825",
    "user": "mvngu"
}
```

Resolution: fixed
