# Issue 4766: parallel? is lame and incomplete

archive/issues_004766.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mvngu\n\n\n```\n20:11 < wstein> I just noticed that the doctesting for parallel? is very confusing.\n20:11 < wstein> It has no examples, and doesn't even seem right.\n20:12 < wstein> The examples are in the __init__ method.\n20:12 < wstein> Moreover, the docstring doesn't document that one can give an integer\n20:12 < wstein> as input, which defaults to pyprocessing with that many cores.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4766\n\n",
    "created_at": "2008-12-12T04:16:06Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "parallel? is lame and incomplete",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4766",
    "user": "was"
}
```
Assignee: cwitty

CC:  mvngu


```
20:11 < wstein> I just noticed that the doctesting for parallel? is very confusing.
20:11 < wstein> It has no examples, and doesn't even seem right.
20:12 < wstein> The examples are in the __init__ method.
20:12 < wstein> Moreover, the docstring doesn't document that one can give an integer
20:12 < wstein> as input, which defaults to pyprocessing with that many cores.
```


Issue created by migration from https://trac.sagemath.org/ticket/4766





---

archive/issue_comments_036115.json:
```json
{
    "body": "Further comment.  On the command line, IPython outputs the docstring for the class *and* the __init__ method, but in the notebook the output is *only* the class docstring.  Thus maybe the problem is partly in how the notebook shows docstrings.\n\n```\nIn IPython.\n        Create paralleled functions.\n    \n        INPUT:\n            p_iter -- parallel iterator function or string:\n                      'multiprocessing' -- use multiprocessing (aka pyprocessing)\n                      'reference'       -- use a fake serial reference\n                                           implementation\n                      DSage instance    -- use dsage\n        \n\nConstructor information:\nDefinition:     parallel(self, p_iter='multiprocessing')\nDocstring:\n    \n            Create a parallel iterator decorator object.\n    \n            EXAMPLES:\n                sage: @parallel()\n                ... def f(N): return N^2\n                sage: v = list(f([1,2,4])); v.sort(); v\n                [(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]\n                sage: @parallel('reference')\n                ... def f(N): return N^2\n```\n",
    "created_at": "2008-12-12T04:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4766#issuecomment-36115",
    "user": "was"
}
```

Further comment.  On the command line, IPython outputs the docstring for the class *and* the __init__ method, but in the notebook the output is *only* the class docstring.  Thus maybe the problem is partly in how the notebook shows docstrings.

```
In IPython.
        Create paralleled functions.
    
        INPUT:
            p_iter -- parallel iterator function or string:
                      'multiprocessing' -- use multiprocessing (aka pyprocessing)
                      'reference'       -- use a fake serial reference
                                           implementation
                      DSage instance    -- use dsage
        

Constructor information:
Definition:     parallel(self, p_iter='multiprocessing')
Docstring:
    
            Create a parallel iterator decorator object.
    
            EXAMPLES:
                sage: @parallel()
                ... def f(N): return N^2
                sage: v = list(f([1,2,4])); v.sort(); v
                [(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
                sage: @parallel('reference')
                ... def f(N): return N^2
```




---

archive/issue_comments_036116.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4766#issuecomment-36116",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036117.json:
```json
{
    "body": "I get the same, complete information from `parallel?` in the notebook and at the command-line.\u00a0 I suggest closing this ticket as fixed.",
    "created_at": "2010-02-01T08:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4766#issuecomment-36117",
    "user": "mpatel"
}
```

I get the same, complete information from `parallel?` in the notebook and at the command-line.  I suggest closing this ticket as fixed.



---

archive/issue_comments_036118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-01T09:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4766#issuecomment-36118",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_036119.json:
```json
{
    "body": "Using the command line interface or notebook of Sage 4.3.2.alpha1, \"parallel?\" returns the same docstring.",
    "created_at": "2010-02-01T09:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4766#issuecomment-36119",
    "user": "mvngu"
}
```

Using the command line interface or notebook of Sage 4.3.2.alpha1, "parallel?" returns the same docstring.
