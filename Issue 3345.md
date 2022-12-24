# Issue 3345: trace no longer works in 3.0.2

archive/issues_003345.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: trace\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: trace('2 + 2')\n> <string>(1)<module>()\n(Pdb) s\n--Return--\n> <string>(1)<module>()->4\n(Pdb) s\n4\n```\n\nBut now\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.1, Release Date: 2008-05-05                       |\n| Type notebook() for the GUI, and license() for information.        |\n| SAGE Version 3.0.2, Release Date: 2008-05-24                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: trace('2 + 2')\n> <string>(1)<module>()\n(Pdb) s\nNameError: \"name 'Integer' is not defined\"\n> <string>(1)<module>()\n(Pdb) s\n--Return--\n> <string>(1)<module>()->None\n(Pdb) s\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/Users/mafwc/<ipython console> in <module>()\n\n/Users/mafwc/sage-3.0.2/local/lib/python2.5/site-packages/sage/misc/trace.py in trace(code, preparse)\n     41     \"\"\"\n     42     code = preparser.preparse(code)\n---> 43     return pdb.runeval(code)\n     44 \n     45     # this could also be useful; it drops\n\n/Users/mafwc/sage-3.0.2/local/lib/python2.5/pdb.py in runeval(expression, globals, locals)\n   1144 \n   1145 def runeval(expression, globals=None, locals=None):\n-> 1146     return Pdb().runeval(expression, globals, locals)\n   1147 \n   1148 def runctx(statement, globals, locals):\n\n/Users/mafwc/sage-3.0.2/local/lib/python2.5/bdb.py in runeval(self, expr, globals, locals)\n    383         try:\n    384             try:\n--> 385                 return eval(expr, globals, locals)\n    386             except BdbQuit:\n    387                 pass\n\n/Users/mafwc/<string> in <module>()\n\nNameError: name 'Integer' is not defined\n```\n \n\nIt seems that in 3.0.2 nothing is defined inside trace.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3345\n\n",
    "created_at": "2008-05-31T22:01:56Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "trace no longer works in 3.0.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3345",
    "user": "fwclarke"
}
```
Assignee: cwitty

Keywords: trace


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: trace('2 + 2')
> <string>(1)<module>()
(Pdb) s
--Return--
> <string>(1)<module>()->4
(Pdb) s
4
```

But now

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.1, Release Date: 2008-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
| SAGE Version 3.0.2, Release Date: 2008-05-24                       |
| Type notebook() for the GUI, and license() for information.        |
sage: trace('2 + 2')
> <string>(1)<module>()
(Pdb) s
NameError: "name 'Integer' is not defined"
> <string>(1)<module>()
(Pdb) s
--Return--
> <string>(1)<module>()->None
(Pdb) s
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/mafwc/<ipython console> in <module>()

/Users/mafwc/sage-3.0.2/local/lib/python2.5/site-packages/sage/misc/trace.py in trace(code, preparse)
     41     """
     42     code = preparser.preparse(code)
---> 43     return pdb.runeval(code)
     44 
     45     # this could also be useful; it drops

/Users/mafwc/sage-3.0.2/local/lib/python2.5/pdb.py in runeval(expression, globals, locals)
   1144 
   1145 def runeval(expression, globals=None, locals=None):
-> 1146     return Pdb().runeval(expression, globals, locals)
   1147 
   1148 def runctx(statement, globals, locals):

/Users/mafwc/sage-3.0.2/local/lib/python2.5/bdb.py in runeval(self, expr, globals, locals)
    383         try:
    384             try:
--> 385                 return eval(expr, globals, locals)
    386             except BdbQuit:
    387                 pass

/Users/mafwc/<string> in <module>()

NameError: name 'Integer' is not defined
```
 

It seems that in 3.0.2 nothing is defined inside trace.



Issue created by migration from https://trac.sagemath.org/ticket/3345





---

archive/issue_comments_023228.json:
```json
{
    "body": "Attachment [3345.patch](tarball://root/attachments/some-uuid/ticket3345/3345.patch) by @mwhansen created at 2008-06-10 04:06:56",
    "created_at": "2008-06-10T04:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23228",
    "user": "@mwhansen"
}
```

Attachment [3345.patch](tarball://root/attachments/some-uuid/ticket3345/3345.patch) by @mwhansen created at 2008-06-10 04:06:56



---

archive/issue_comments_023229.json:
```json
{
    "body": "I've attached a patch which grabs the interpreters namespace from IPython and passes it in as the globals to pdb.runeval.  I'm not sure why trace worked before / why it's not working now though.",
    "created_at": "2008-06-10T04:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23229",
    "user": "@mwhansen"
}
```

I've attached a patch which grabs the interpreters namespace from IPython and passes it in as the globals to pdb.runeval.  I'm not sure why trace worked before / why it's not working now though.



---

archive/issue_comments_023230.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-10T04:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23230",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023231.json:
```json
{
    "body": "Changing assignee from cwitty to @mwhansen.",
    "created_at": "2008-06-10T04:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23231",
    "user": "@mwhansen"
}
```

Changing assignee from cwitty to @mwhansen.



---

archive/issue_comments_023232.json:
```json
{
    "body": "With the patch `trace('2 + 2')` works now, but strangely each instance of trace seems to start by recalling the last : \n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: fwc\nsage: trace('2 + 2')\n> <string>(1)<module>()\n(Pdb) s\n--Return--\n> <string>(1)<module>()->4\n(Pdb) s\n4\nsage: trace('2 + 2')\n> <string>(1)<module>()->4\n(Pdb) s\n--Return--\n> <string>(1)<module>()->4\n(Pdb) s\n4\nsage: trace('3 + 3')\n> <string>(1)<module>()->4\n(Pdb) s\n--Return--\n> <string>(1)<module>()->6\n(Pdb) s\n6\nsage: trace('3 + 3')\n> <string>(1)<module>()->6\n(Pdb) s\n--Return--\n> <string>(1)<module>()->6\n(Pdb) s\n6\n```\n\n| SAGE Version 3.0.2, Release Date: 2008-05-24                       |\n| Type notebook() for the GUI, and license() for information.        |\nAnd there are still some things `trace` can't do:\n\n\n```\nsage: trace(\"P.<y> = QQ[]\")\n------------------------------------------------------------\n   File \"<string>\", line 1\n     P = QQ['y']; (y,) = P._first_ngens(Integer(1))\n       ^\nSyntaxError: invalid syntax\n```\n\nBut there's no problem with\n\n```\nsage: P = QQ['y']; (y,) = P._first_ngens(Integer(1))\nsage: P\nUnivariate Polynomial Ring in y over Rational Field\nsage: P == parent(y)\nTrue\n```\n",
    "created_at": "2008-06-10T07:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23232",
    "user": "fwclarke"
}
```

With the patch `trace('2 + 2')` works now, but strangely each instance of trace seems to start by recalling the last : 

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: fwc
sage: trace('2 + 2')
> <string>(1)<module>()
(Pdb) s
--Return--
> <string>(1)<module>()->4
(Pdb) s
4
sage: trace('2 + 2')
> <string>(1)<module>()->4
(Pdb) s
--Return--
> <string>(1)<module>()->4
(Pdb) s
4
sage: trace('3 + 3')
> <string>(1)<module>()->4
(Pdb) s
--Return--
> <string>(1)<module>()->6
(Pdb) s
6
sage: trace('3 + 3')
> <string>(1)<module>()->6
(Pdb) s
--Return--
> <string>(1)<module>()->6
(Pdb) s
6
```

| SAGE Version 3.0.2, Release Date: 2008-05-24                       |
| Type notebook() for the GUI, and license() for information.        |
And there are still some things `trace` can't do:


```
sage: trace("P.<y> = QQ[]")
------------------------------------------------------------
   File "<string>", line 1
     P = QQ['y']; (y,) = P._first_ngens(Integer(1))
       ^
SyntaxError: invalid syntax
```

But there's no problem with

```
sage: P = QQ['y']; (y,) = P._first_ngens(Integer(1))
sage: P
Univariate Polynomial Ring in y over Rational Field
sage: P == parent(y)
True
```




---

archive/issue_comments_023233.json:
```json
{
    "body": "Why did this get positive review? It looks broken.",
    "created_at": "2008-06-15T21:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23233",
    "user": "@mwhansen"
}
```

Why did this get positive review? It looks broken.



---

archive/issue_comments_023234.json:
```json
{
    "body": "Changing keywords from \"trace\" to \"trace, editor_mhansen\".",
    "created_at": "2008-06-20T04:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23234",
    "user": "@craigcitro"
}
```

Changing keywords from "trace" to "trace, editor_mhansen".



---

archive/issue_comments_023235.json:
```json
{
    "body": "Attachment [trac_3345.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345.patch) by @mwhansen created at 2008-07-15 21:26:10",
    "created_at": "2008-07-15T21:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23235",
    "user": "@mwhansen"
}
```

Attachment [trac_3345.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345.patch) by @mwhansen created at 2008-07-15 21:26:10



---

archive/issue_comments_023236.json:
```json
{
    "body": "I don't know what's going on recalling the last value produced by trace, but that seems to be something within pdb.  Trace has never worked on (and probably shouldn't) work on statements (like assignment ones) -- only on expressions.",
    "created_at": "2008-07-15T21:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23236",
    "user": "@mwhansen"
}
```

I don't know what's going on recalling the last value produced by trace, but that seems to be something within pdb.  Trace has never worked on (and probably shouldn't) work on statements (like assignment ones) -- only on expressions.



---

archive/issue_comments_023237.json:
```json
{
    "body": "Attachment [trac_3345-part2.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345-part2.patch) by @williamstein created at 2008-07-21 18:19:39\n\ndone while refereeing.",
    "created_at": "2008-07-21T18:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23237",
    "user": "@williamstein"
}
```

Attachment [trac_3345-part2.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345-part2.patch) by @williamstein created at 2008-07-21 18:19:39

done while refereeing.



---

archive/issue_comments_023238.json:
```json
{
    "body": "While refereeing trac_3345.patch I:\n1. fix the issue with running assignments, and \n2. added some mean serious doctests\n3. Added a proper error message when one uses trace in the notebook",
    "created_at": "2008-07-21T18:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23238",
    "user": "@williamstein"
}
```

While refereeing trac_3345.patch I:
1. fix the issue with running assignments, and 
2. added some mean serious doctests
3. Added a proper error message when one uses trace in the notebook



---

archive/issue_comments_023239.json:
```json
{
    "body": "To apply this patch you should apply trac_3345.patch and trac_3345-part2.patch",
    "created_at": "2008-07-21T18:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23239",
    "user": "@williamstein"
}
```

To apply this patch you should apply trac_3345.patch and trac_3345-part2.patch



---

archive/issue_comments_023240.json:
```json
{
    "body": "When applying the two patches William recommended I am seeing the following failure on sage.math:\n\n```\nsage -t -long devel/sage/sage/misc/trace.py    \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/tmp/trace.py\", line 49:\n    sage: print s.before\nExpected:\n    /rings/arith.py(...)factor()\n    ...\n    ipdb> c\n    2 * 5\n    <BLANKLINE>\nGot:\n    -3.0.6.alpha1/local/lib/python2.5/site-packages/\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_1\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/tmp/.doctest_trace.py\n         [3.8 s]\nexit code: 1024\n```\n\n\nAm I doing something wrong?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-21T19:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23240",
    "user": "mabshoff"
}
```

When applying the two patches William recommended I am seeing the following failure on sage.math:

```
sage -t -long devel/sage/sage/misc/trace.py    
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/tmp/trace.py", line 49:
    sage: print s.before
Expected:
    /rings/arith.py(...)factor()
    ...
    ipdb> c
    2 * 5
    <BLANKLINE>
Got:
    -3.0.6.alpha1/local/lib/python2.5/site-packages/
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/tmp/.doctest_trace.py
         [3.8 s]
exit code: 1024
```


Am I doing something wrong?

Cheers,

Michael



---

archive/issue_comments_023241.json:
```json
{
    "body": "Attachment [trac_3345-part3.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345-part3.patch) by @williamstein created at 2008-07-21 21:00:13",
    "created_at": "2008-07-21T21:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23241",
    "user": "@williamstein"
}
```

Attachment [trac_3345-part3.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345-part3.patch) by @williamstein created at 2008-07-21 21:00:13



---

archive/issue_comments_023242.json:
```json
{
    "body": "Attachment [trac_3345-part4.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345-part4.patch) by @mwhansen created at 2008-07-21 22:52:30",
    "created_at": "2008-07-21T22:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23242",
    "user": "@mwhansen"
}
```

Attachment [trac_3345-part4.patch](tarball://root/attachments/some-uuid/ticket3345/trac_3345-part4.patch) by @mwhansen created at 2008-07-21 22:52:30



---

archive/issue_comments_023243.json:
```json
{
    "body": "Positive review for all four trac_3345* patches.",
    "created_at": "2008-07-21T22:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23243",
    "user": "@mwhansen"
}
```

Positive review for all four trac_3345* patches.



---

archive/issue_comments_023244.json:
```json
{
    "body": "Merged trac_3345.patch, trac_3345-part2.patch, trac_3345-part3.patch and\ntrac_3345-part4.patch in Sage 3.0.6.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-21T22:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23244",
    "user": "mabshoff"
}
```

Merged trac_3345.patch, trac_3345-part2.patch, trac_3345-part3.patch and
trac_3345-part4.patch in Sage 3.0.6.rc0.

Cheers,

Michael



---

archive/issue_comments_023245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-21T22:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3345#issuecomment-23245",
    "user": "mabshoff"
}
```

Resolution: fixed
