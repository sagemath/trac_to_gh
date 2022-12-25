# Issue 1422: add bibtex function to get the bibtex code for citing the sage components

archive/issues_001422.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @burcin ranosch\n\n6.3 how do i reference sage?\nIf you write a paper using SAGE, please reference computations done with\nSAGE by including\n[SAGE], SAGE Mathematical Software, Version 2.6, http://www.sagemath.org\n<sup>^</sup>\nHow about a function bibtex() similar to latex() which gives a bibtex\nentry? Coudl default to bibtex(sage) but could also provide\nbibtex(pari), bibtex(gp), bibtex(Singular), etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1422\n\n",
    "created_at": "2007-12-07T21:42:23Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "add bibtex function to get the bibtex code for citing the sage components",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1422",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tba

CC:  @burcin ranosch

6.3 how do i reference sage?
If you write a paper using SAGE, please reference computations done with
SAGE by including
[SAGE], SAGE Mathematical Software, Version 2.6, http://www.sagemath.org
<sup>^</sup>
How about a function bibtex() similar to latex() which gives a bibtex
entry? Coudl default to bibtex(sage) but could also provide
bibtex(pari), bibtex(gp), bibtex(Singular), etc.

Issue created by migration from https://trac.sagemath.org/ticket/1422





---

archive/issue_comments_009148.json:
```json
{
    "body": "This is an excellent idea.    The output should probably be both the bibtex\ndatabase entry *and* the result of running it through bibtex, so it can be directly included in a paper (without having to use bibtex).\n\n -- William",
    "created_at": "2008-01-14T05:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1422#issuecomment-9148",
    "user": "https://github.com/williamstein"
}
```

This is an excellent idea.    The output should probably be both the bibtex
database entry *and* the result of running it through bibtex, so it can be directly included in a paper (without having to use bibtex).

 -- William
