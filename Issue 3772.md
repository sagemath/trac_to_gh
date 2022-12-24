# Issue 3772: Gnuplot.py uses IPython/Python 2.6 keyword with

archive/issues_003772.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage: help\nType help() for interactive help, or help(object) for help about object.\nsage: help('keywords')\n\nHere is a list of the Python keywords.  Enter any keyword to get more help.\n\nand                 elif                if                  print\nas                  else                import              raise\nassert              except              in                  return\nbreak               exec                is                  try\nclass               finally             lambda              while\ncontinue            for                 not                 with\ndef                 from                or                  yield\n\nShould be simple to fix, by renaming the with argument to something creative like witharg or w\n\nIssue created by migration from https://trac.sagemath.org/ticket/3772\n\n",
    "created_at": "2008-08-04T01:35:51Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Gnuplot.py uses IPython/Python 2.6 keyword with",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3772",
    "user": "Jondice"
}
```
Assignee: @williamstein

sage: help
Type help() for interactive help, or help(object) for help about object.
sage: help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield

Should be simple to fix, by renaming the with argument to something creative like witharg or w

Issue created by migration from https://trac.sagemath.org/ticket/3772





---

archive/issue_comments_026831.json:
```json
{
    "body": "This was fixed by the new spkg at #7187",
    "created_at": "2009-11-17T11:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3772#issuecomment-26831",
    "user": "@mwhansen"
}
```

This was fixed by the new spkg at #7187



---

archive/issue_comments_026832.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T11:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3772#issuecomment-26832",
    "user": "@mwhansen"
}
```

Resolution: fixed
