# Issue 5726: RDF quotes -- docstring bug (possibly cython issue)

archive/issues_005726.json:
```json
{
    "body": "Assignee: tba\n\n\n```\nsage: RDF.random_element?\n...\nDefinition: RDF.random_element(min='-1', max='1')\n```\n\nNotice the stupid quotes around -1 and 1, which are very confusing!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5726\n\n",
    "created_at": "2009-04-09T16:58:20Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "RDF quotes -- docstring bug (possibly cython issue)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5726",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba


```
sage: RDF.random_element?
...
Definition: RDF.random_element(min='-1', max='1')
```

Notice the stupid quotes around -1 and 1, which are very confusing!

Issue created by migration from https://trac.sagemath.org/ticket/5726





---

archive/issue_comments_044659.json:
```json
{
    "body": "In the notebook definition is wrong in at least two ways:\n\n```\nsage: factor?\nDefinition:  factor(n, proof, int_, algorithm, verbose, **kwds)\n```\n\nbut it should be\n\n```\nDefinition:     factor(n, proof=None, int_=False, algorithm='pari', verbose=0, **kwds)\n```\n\nwhich it *is* in the command line. \n\nOn the command line, cython code *never* gets a function \"Definition\".",
    "created_at": "2009-04-09T19:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5726#issuecomment-44659",
    "user": "https://github.com/williamstein"
}
```

In the notebook definition is wrong in at least two ways:

```
sage: factor?
Definition:  factor(n, proof, int_, algorithm, verbose, **kwds)
```

but it should be

```
Definition:     factor(n, proof=None, int_=False, algorithm='pari', verbose=0, **kwds)
```

which it *is* in the command line. 

On the command line, cython code *never* gets a function "Definition".



---

archive/issue_comments_044660.json:
```json
{
    "body": "Attachment [trac_5726-sageinspect.patch](tarball://root/attachments/some-uuid/ticket5726/trac_5726-sageinspect.patch) by @jhpalmieri created at 2009-08-24 16:42:40",
    "created_at": "2009-08-24T16:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5726#issuecomment-44660",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_5726-sageinspect.patch](tarball://root/attachments/some-uuid/ticket5726/trac_5726-sageinspect.patch) by @jhpalmieri created at 2009-08-24 16:42:40



---

archive/issue_comments_044661.json:
```json
{
    "body": "The problems lie in sage.misc.sageinspect.\n\nThe issue with `factor` is a one-line fix -- see the patch.  (\"defaults\" was missing from the return value of the function `sage_getargspec`.)\n\nThe issue with `RDF.random_element` is a cython one.  To get the arguments of a Cython function, as far as I can tell, the source code is scanned and parsed, so *everything* is a string.  The default arguments are therefore returned as strings.  See the function `_sage_getargspec_cython` -- the examples even demonstrate this.  I don't have a good idea for a simple fix yet.  Since this is a separate issue, the first patch can be reviewed, and if we don't find a quick fix for the Cython issue, we can open a new ticket just for that.",
    "created_at": "2009-08-24T16:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5726#issuecomment-44661",
    "user": "https://github.com/jhpalmieri"
}
```

The problems lie in sage.misc.sageinspect.

The issue with `factor` is a one-line fix -- see the patch.  ("defaults" was missing from the return value of the function `sage_getargspec`.)

The issue with `RDF.random_element` is a cython one.  To get the arguments of a Cython function, as far as I can tell, the source code is scanned and parsed, so *everything* is a string.  The default arguments are therefore returned as strings.  See the function `_sage_getargspec_cython` -- the examples even demonstrate this.  I don't have a good idea for a simple fix yet.  Since this is a separate issue, the first patch can be reviewed, and if we don't find a quick fix for the Cython issue, we can open a new ticket just for that.



---

archive/issue_comments_044662.json:
```json
{
    "body": "Applied the patch. Doctests pass, and the default arguments now appear. Nice work.\n\nAs for the Cython issue, perhaps using `repr(eval(argument))` will work. Output as string if the output starts and ends with quotes, and output without quotes for any other result.",
    "created_at": "2009-08-30T19:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5726#issuecomment-44662",
    "user": "https://github.com/TimDumol"
}
```

Applied the patch. Doctests pass, and the default arguments now appear. Nice work.

As for the Cython issue, perhaps using `repr(eval(argument))` will work. Output as string if the output starts and ends with quotes, and output without quotes for any other result.



---

archive/issue_comments_044663.json:
```json
{
    "body": "Replying to [comment:4 timdumol]:\n> As for the Cython issue, perhaps using `repr(eval(argument))` will work. Output as string if the output starts and ends with quotes, and output without quotes for any other result.\n\nGood idea.  See #6848.",
    "created_at": "2009-08-30T21:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5726#issuecomment-44663",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:4 timdumol]:
> As for the Cython issue, perhaps using `repr(eval(argument))` will work. Output as string if the output starts and ends with quotes, and output without quotes for any other result.

Good idea.  See #6848.



---

archive/issue_comments_044664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-31T04:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5726#issuecomment-44664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
