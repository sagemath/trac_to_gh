# Issue 5722: fast callable pow

archive/issues_005722.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  cwitty\n\npow(double, double) inconsistent for bad input. See extensive documentation in floatobject.c\n\nIssue created by migration from https://trac.sagemath.org/ticket/5722\n\n",
    "created_at": "2009-04-09T02:15:41Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "title": "fast callable pow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5722",
    "user": "robertwb"
}
```
Assignee: somebody

CC:  cwitty

pow(double, double) inconsistent for bad input. See extensive documentation in floatobject.c

Issue created by migration from https://trac.sagemath.org/ticket/5722





---

archive/issue_comments_044711.json:
```json
{
    "body": "Oops, I spoke too soon in person. There are two doctest failures that need fixing:\n\n```\nsage -t -long \"devel/sage/sage/ext/fast_callable.pyx\"       \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/ext/fast_callable.pyx\", line 2213:\n    sage: fast_callable(sin(x)/x, vars=[x], domain=RDF).get_orig_args()\nExpected:\n    {'domain': Real Double Field, 'code': [0, 0, 16, 0, 0, 7, 2], 'py_constants': [], 'args': 1, 'stack': 2, 'constants': []}\nGot:\n    {'domain': Real Double Field, 'code': [0, 0, 16, 0, 0, 8, 2], 'py_constants': [], 'args': 1, 'stack': 2, 'constants': []}\n**********************************************************************\n1 items had failures:\n```\n\nAnd\n\n```\nsage -t -long \"devel/sage/sage/ext/gen_interpreters.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/ext/gen_interpreters.py\", line 2772:\n    sage: print buff.getvalue()\nExpected:\n        case 7: /* div */\n          {\n            double i1 = *--stack;\n            double i0 = *--stack;\n            double o0;\n            o0 = i0 / i1;\n            *stack++ = o0;\n          }\n          break;\n    <BLANKLINE>\nGot:\n        case 8: /* div */\n          {\n            double i1 = *--stack;\n            double i0 = *--stack;\n            double o0;\n            o0 = i0 / i1;\n            *stack++ = o0;\n          }\n          break;\n    <BLANKLINE>\n<SNIP>\n```\n\n\nI think that just the doctests need to be updated, but I will leave this to you :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T02:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44711",
    "user": "mabshoff"
}
```

Oops, I spoke too soon in person. There are two doctest failures that need fixing:

```
sage -t -long "devel/sage/sage/ext/fast_callable.pyx"       
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/ext/fast_callable.pyx", line 2213:
    sage: fast_callable(sin(x)/x, vars=[x], domain=RDF).get_orig_args()
Expected:
    {'domain': Real Double Field, 'code': [0, 0, 16, 0, 0, 7, 2], 'py_constants': [], 'args': 1, 'stack': 2, 'constants': []}
Got:
    {'domain': Real Double Field, 'code': [0, 0, 16, 0, 0, 8, 2], 'py_constants': [], 'args': 1, 'stack': 2, 'constants': []}
**********************************************************************
1 items had failures:
```

And

```
sage -t -long "devel/sage/sage/ext/gen_interpreters.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/ext/gen_interpreters.py", line 2772:
    sage: print buff.getvalue()
Expected:
        case 7: /* div */
          {
            double i1 = *--stack;
            double i0 = *--stack;
            double o0;
            o0 = i0 / i1;
            *stack++ = o0;
          }
          break;
    <BLANKLINE>
Got:
        case 8: /* div */
          {
            double i1 = *--stack;
            double i0 = *--stack;
            double o0;
            o0 = i0 / i1;
            *stack++ = o0;
          }
          break;
    <BLANKLINE>
<SNIP>
```


I think that just the doctests need to be updated, but I will leave this to you :)

Cheers,

Michael



---

archive/issue_comments_044712.json:
```json
{
    "body": "Yes, those are both inconsequential ordering issues.",
    "created_at": "2009-04-09T06:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44712",
    "user": "robertwb"
}
```

Yes, those are both inconsequential ordering issues.



---

archive/issue_comments_044713.json:
```json
{
    "body": "Hi Robert,\n\nthere are actually two more doctest failure that I cut off since the failure message is quite long:\n\n```\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/ext/gen_interpreters.py\", line 3592:\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/ext/gen_interpreters.py\", line 3608:\n```\n\nSorry for causing confusion ;)\n\nBut the other doctest failures are fixed.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T06:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44713",
    "user": "mabshoff"
}
```

Hi Robert,

there are actually two more doctest failure that I cut off since the failure message is quite long:

```
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/ext/gen_interpreters.py", line 3592:
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/ext/gen_interpreters.py", line 3608:
```

Sorry for causing confusion ;)

But the other doctest failures are fixed.

Cheers,

Michael



---

archive/issue_comments_044714.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-09T07:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44714",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_044715.json:
```json
{
    "body": "OK, all doctests in that file pass now.",
    "created_at": "2009-04-09T07:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44715",
    "user": "robertwb"
}
```

OK, all doctests in that file pass now.



---

archive/issue_comments_044716.json:
```json
{
    "body": "Positive review. Doctests do pass :). \n\nI also read the patch and I am happy with it.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44716",
    "user": "mabshoff"
}
```

Positive review. Doctests do pass :). 

I also read the patch and I am happy with it.

Cheers,

Michael



---

archive/issue_comments_044717.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T18:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44717",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044718.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCCing cwitty so he is aware of this patch. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5722#issuecomment-44718",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

CCing cwitty so he is aware of this patch. 

Cheers,

Michael
