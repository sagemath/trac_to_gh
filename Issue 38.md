# Issue 38: bug in notebook (too much text clipped)

archive/issues_000038.json:
```json
{
    "body": "Assignee: somebody\n\n bug in notebook: \n\n```\n  sage: sys.stdout.write('hi there')\n  sage: sys.stdout.flush()\n  hi ther\n      ^^^^ ----- where's the e!!\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/38\n\n",
    "created_at": "2006-09-12T23:30:56Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in notebook (too much text clipped)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/38",
    "user": "@williamstein"
}
```
Assignee: somebody

 bug in notebook: 

```
  sage: sys.stdout.write('hi there')
  sage: sys.stdout.flush()
  hi ther
      ^^^^ ----- where's the e!!
```


Issue created by migration from https://trac.sagemath.org/ticket/38





---

archive/issue_comments_000245.json:
```json
{
    "body": "Try the following:\n\n```\nsys.stdout.write('hi there')\nsleep(2)\n```\n\nWhile sage is sleep()ing, you'll see the full text.  When it finishes, the e disappears.  ?????\n\n\nMessing with stdout from the notebook seems like a categorically bad idea.  I've found that any of the following commands cause the notebook to hang.\n\n\n```\nsys.stdout.close()\nsys.stdout.next()\nsys.stdout.read()\n```\n\n\nI have found a trivial workaround.  If we tack an extra print statement onto the end, it works fine.  But why do we have to do this?  Mysterious. \n\n```\n  sage: sys.stdout.write('hi there')\n  sage: print\n  hi there\n         ^ ----- w00t\n```\n",
    "created_at": "2006-09-14T18:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/38",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/38#issuecomment-245",
    "user": "boothby"
}
```

Try the following:

```
sys.stdout.write('hi there')
sleep(2)
```

While sage is sleep()ing, you'll see the full text.  When it finishes, the e disappears.  ?????


Messing with stdout from the notebook seems like a categorically bad idea.  I've found that any of the following commands cause the notebook to hang.


```
sys.stdout.close()
sys.stdout.next()
sys.stdout.read()
```


I have found a trivial workaround.  If we tack an extra print statement onto the end, it works fine.  But why do we have to do this?  Mysterious. 

```
  sage: sys.stdout.write('hi there')
  sage: print
  hi there
         ^ ----- w00t
```




---

archive/issue_comments_000246.json:
```json
{
    "body": "Fixed.\n\nThere was some interaction between the code that asks for an updated list of variables that have been defined and this problem.  \n\nI changed a few lines in sage/server/notebook/worksheet.py to the following:\n\n\n```\n        if not C.introspect():\n            input += 'print \"\\\\n\\\\n%s'%SAGE_VARS + '=%s\"%_support_.variables(True)'\n```\n",
    "created_at": "2006-10-15T17:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/38",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/38#issuecomment-246",
    "user": "@williamstein"
}
```

Fixed.

There was some interaction between the code that asks for an updated list of variables that have been defined and this problem.  

I changed a few lines in sage/server/notebook/worksheet.py to the following:


```
        if not C.introspect():
            input += 'print "\\n\\n%s'%SAGE_VARS + '=%s"%_support_.variables(True)'
```




---

archive/issue_comments_000247.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T17:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/38",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/38#issuecomment-247",
    "user": "@williamstein"
}
```

Resolution: fixed
