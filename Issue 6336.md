# Issue 6336: optional doctest failure -- constructions calculus tests hang forever

archive/issues_006336.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\n\t [32.9 s]\nsage -t -long --optional devel/sage/doc/en/constructions/calculus.rst\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\nxprop:  unable to open display ''\nError: no \"view\" rule for type \"application/x-dvi\" passed its test case\n       (for more information, add \"--debug=1\" on the command line)\nxprop:  unable to open display ''\nError: no \"view\" rule for type \"application/x-dvi\" passed its test case\n       (for more information, add \"--debug=1\" on the command line)\n*** *** Error: TIMED OUT! *** ***\n\t [1800.1 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6336\n\n",
    "created_at": "2009-06-16T15:20:05Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "optional doctest failure -- constructions calculus tests hang forever",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6336",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
	 [32.9 s]
sage -t -long --optional devel/sage/doc/en/constructions/calculus.rst
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
xprop:  unable to open display ''
Error: no "view" rule for type "application/x-dvi" passed its test case
       (for more information, add "--debug=1" on the command line)
xprop:  unable to open display ''
Error: no "view" rule for type "application/x-dvi" passed its test case
       (for more information, add "--debug=1" on the command line)
*** *** Error: TIMED OUT! *** ***
	 [1800.1 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6336





---

archive/issue_comments_050474.json:
```json
{
    "body": "Attachment [trac_6336.patch](tarball://root/attachments/some-uuid/ticket6336/trac_6336.patch) by @jhpalmieri created at 2009-06-16 18:47:10",
    "created_at": "2009-06-16T18:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6336#issuecomment-50474",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6336.patch](tarball://root/attachments/some-uuid/ticket6336/trac_6336.patch) by @jhpalmieri created at 2009-06-16 18:47:10



---

archive/issue_comments_050475.json:
```json
{
    "body": "Here's a patch.  This seems to fix this bug, but exposes another optional doctest failure (related to octave, I think): on sage.math, before the patch, I see the error message printed above.  After the patch, I don't, although I see this:\n\n```\nsage -t -optional \"devel/sage/doc/en/constructions/calculus.rst\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n\t [360.1 s]\n```\n\nSo this patch is a partial fix.  Any takers for the octave timeout?",
    "created_at": "2009-06-16T19:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6336#issuecomment-50475",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.  This seems to fix this bug, but exposes another optional doctest failure (related to octave, I think): on sage.math, before the patch, I see the error message printed above.  After the patch, I don't, although I see this:

```
sage -t -optional "devel/sage/doc/en/constructions/calculus.rst"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
	 [360.1 s]
```

So this patch is a partial fix.  Any takers for the octave timeout?



---

archive/issue_comments_050476.json:
```json
{
    "body": "Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild constructions html (resp., pdf) went fine.",
    "created_at": "2009-06-16T22:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6336#issuecomment-50476",
    "user": "https://github.com/wdjoyner"
}
```

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild constructions html (resp., pdf) went fine.



---

archive/issue_comments_050477.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6336#issuecomment-50477",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
