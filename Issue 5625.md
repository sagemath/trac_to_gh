# Issue 5625: group cohomology -- bad error messages; should indicate an optional package is needed

archive/issues_005625.json:
```json
{
    "body": "Assignee: joyner\n\nThe following fails because I don't have the optional  gap_packages-* package installed:\n\n\n```\nsage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])\nsage: G.cohomology(1,3)\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/wstein/.sage/sage_notebook/worksheets/admin/59/code/369.py\", line 8, in <module>\n    G.cohomology(_sage_const_1 ,_sage_const_3 )\n  File \"/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\", line 1132, in cohomology\n    L = eval(gap.eval(\"GroupCohomology(%s,%s,%s)\"%(GG,n,p)))\n  File \"/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 479, in eval\n    result = Expect.eval(self, input_line, **kwds)\n  File \"/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 974, in eval\n    return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n  File \"/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 723, in _eval_line\n    raise RuntimeError, message\nRuntimeError: Gap produced error output\nVariable: 'GroupCohomology' must have a value\n\n\n   executing GroupCohomology(Group([(3,4), (1,2,3)(4,5)]),1,3);\n```\n\n\nThe error message should say that I have to install that package.\n\nIncidentally, installing the package doesn't work right now since Sage ships gap-4.12 (though I guess we're downgrading to 4.10 soon):\n\n\n```\n$ sage -i gap_packages-4.4.10_6\n...\nboom\nmkdir: /Users/wstein/build/sage-3.4/local/lib/gap-4.4.10: No such file or directory\ncp: directory /Users/wstein/build/sage-3.4/local/lib/gap-4.4.10/pkg does not exist\nError copying SPKG.txt\n\nreal\t0m0.078s\nuser\t0m0.007s\nsys\t0m0.019s\n```\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/5625\n\n",
    "created_at": "2009-03-29T00:36:43Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "group cohomology -- bad error messages; should indicate an optional package is needed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5625",
    "user": "was"
}
```
Assignee: joyner

The following fails because I don't have the optional  gap_packages-* package installed:


```
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.cohomology(1,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wstein/.sage/sage_notebook/worksheets/admin/59/code/369.py", line 8, in <module>
    G.cohomology(_sage_const_1 ,_sage_const_3 )
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 1132, in cohomology
    L = eval(gap.eval("GroupCohomology(%s,%s,%s)"%(GG,n,p)))
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 479, in eval
    result = Expect.eval(self, input_line, **kwds)
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 974, in eval
    return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 723, in _eval_line
    raise RuntimeError, message
RuntimeError: Gap produced error output
Variable: 'GroupCohomology' must have a value


   executing GroupCohomology(Group([(3,4), (1,2,3)(4,5)]),1,3);
```


The error message should say that I have to install that package.

Incidentally, installing the package doesn't work right now since Sage ships gap-4.12 (though I guess we're downgrading to 4.10 soon):


```
$ sage -i gap_packages-4.4.10_6
...
boom
mkdir: /Users/wstein/build/sage-3.4/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wstein/build/sage-3.4/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real	0m0.078s
user	0m0.007s
sys	0m0.019s
```
 

Issue created by migration from https://trac.sagemath.org/ticket/5625





---

archive/issue_comments_043922.json:
```json
{
    "body": "Here's a patch.  Skimming through the Sage source code, it seems that in other cases we usually raise a RuntimeError when an optional package is needed but not installed, so that's what I've done here.",
    "created_at": "2009-07-22T03:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43922",
    "user": "jhpalmieri"
}
```

Here's a patch.  Skimming through the Sage source code, it seems that in other cases we usually raise a RuntimeError when an optional package is needed but not installed, so that's what I've done here.



---

archive/issue_comments_043923.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-07-22T03:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43923",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_043924.json:
```json
{
    "body": "Applies fine and passes sage -testall. A simple patch which does what it claims.",
    "created_at": "2009-07-25T19:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43924",
    "user": "wdj"
}
```

Applies fine and passes sage -testall. A simple patch which does what it claims.



---

archive/issue_comments_043925.json:
```json
{
    "body": "reviewer patch; fix typos",
    "created_at": "2009-07-25T20:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43925",
    "user": "mvngu"
}
```

reviewer patch; fix typos



---

archive/issue_comments_043926.json:
```json
{
    "body": "Attachment\n\nThe patch `trac_5625-typo-fixes.patch` fixes a number of typos found in John's patch.",
    "created_at": "2009-07-25T20:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43926",
    "user": "mvngu"
}
```

Attachment

The patch `trac_5625-typo-fixes.patch` fixes a number of typos found in John's patch.



---

archive/issue_comments_043927.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-25T20:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43927",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_043928.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-07-25T20:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5625#issuecomment-43928",
    "user": "mvngu"
}
```

Merged both patches.
