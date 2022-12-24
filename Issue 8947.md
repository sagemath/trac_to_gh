# Issue 8947: pretty printing of vectors over callable symbolic rings

archive/issues_008947.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer @williamstein @robertwb\n\nThis patch makes vectors of callable symbolic rings print nicer, in the form arguments mapsto vector\n\n\n```\nsage: f(x,y)=[3*x,e^x,2*x*y]\nsage: f\n(x, y) |--> (3*x, e^x, 2*x*y)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8947\n\n",
    "created_at": "2010-05-11T06:25:01Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "pretty printing of vectors over callable symbolic rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8947",
    "user": "@jasongrout"
}
```
Assignee: jason, was

CC:  @rbeezer @williamstein @robertwb

This patch makes vectors of callable symbolic rings print nicer, in the form arguments mapsto vector


```
sage: f(x,y)=[3*x,e^x,2*x*y]
sage: f
(x, y) |--> (3*x, e^x, 2*x*y)
```



Issue created by migration from https://trac.sagemath.org/ticket/8947





---

archive/issue_comments_082367.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-11T06:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82367",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_082368.json:
```json
{
    "body": "Doctests need to be fixed up.",
    "created_at": "2010-05-11T06:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82368",
    "user": "@jasongrout"
}
```

Doctests need to be fixed up.



---

archive/issue_comments_082369.json:
```json
{
    "body": "Attachment [trac-8947-callable-SR-vectors-print.patch](tarball://root/attachments/some-uuid/ticket8947/trac-8947-callable-SR-vectors-print.patch) by @jasongrout created at 2010-05-11 18:03:00",
    "created_at": "2010-05-11T18:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82369",
    "user": "@jasongrout"
}
```

Attachment [trac-8947-callable-SR-vectors-print.patch](tarball://root/attachments/some-uuid/ticket8947/trac-8947-callable-SR-vectors-print.patch) by @jasongrout created at 2010-05-11 18:03:00



---

archive/issue_comments_082370.json:
```json
{
    "body": "The doctests depend on a patch in 4.4.2.alpha0.\n\nI think the right way to change printing for a vector over callable symbolic expressions is to subclass as I did in the patch and override the _repr_ and _latex_ methods.  Can was or robertwb comment on this?",
    "created_at": "2010-05-11T18:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82370",
    "user": "@jasongrout"
}
```

The doctests depend on a patch in 4.4.2.alpha0.

I think the right way to change printing for a vector over callable symbolic expressions is to subclass as I did in the patch and override the _repr_ and _latex_ methods.  Can was or robertwb comment on this?



---

archive/issue_comments_082371.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-11T18:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82371",
    "user": "@jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082372.json:
```json
{
    "body": "#5506 adds some further ideas about what to do about this class.",
    "created_at": "2010-05-11T18:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82372",
    "user": "@jasongrout"
}
```

#5506 adds some further ideas about what to do about this class.



---

archive/issue_comments_082373.json:
```json
{
    "body": "Yep, that's the way to do it. The code looks good, but I only glanced at it quickly haven't tested it.",
    "created_at": "2010-05-11T18:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82373",
    "user": "@robertwb"
}
```

Yep, that's the way to do it. The code looks good, but I only glanced at it quickly haven't tested it.



---

archive/issue_comments_082374.json:
```json
{
    "body": "Hi Jason,\n\nNice patch.\n\n1.  Do you think this should be called \"free_module_element_callable_symbolic_dense\"?  Technically these don't have to be vectors, and they do have entries over a ring?  Yes, that's an unwieldy name.  ;-)  Just asking.\n\n2.  Do you want to add it into the documentation, doesn't seem to be included when I build the docs?\n\n3.  Docstring for _latex_ looks like it has an indentation problem that needs fixing.\n\nRunning tests right now.\n\nRob",
    "created_at": "2010-05-19T04:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82374",
    "user": "@rbeezer"
}
```

Hi Jason,

Nice patch.

1.  Do you think this should be called "free_module_element_callable_symbolic_dense"?  Technically these don't have to be vectors, and they do have entries over a ring?  Yes, that's an unwieldy name.  ;-)  Just asking.

2.  Do you want to add it into the documentation, doesn't seem to be included when I build the docs?

3.  Docstring for _latex_ looks like it has an indentation problem that needs fixing.

Running tests right now.

Rob



---

archive/issue_comments_082375.json:
```json
{
    "body": "Replying to [comment:6 rbeezer]:\n> Hi Jason,\n> \n> Nice patch.\n> \n> 1.  Do you think this should be called \"free_module_element_callable_symbolic_dense\"?  Technically these don't have to be vectors, and they do have entries over a ring?  Yes, that's an unwieldy name.  ;-)  Just asking.\n\nWell, Sage thinks that it is a field:\n\n\n```\n\nsage: f(x,y)=x^2+y                             \nsage: R=f.parent()\nsage: R \nCallable function ring with arguments (x, y)\nsage: R.is_field()\nTrue\n```\n\n\n\n> \n> 2.  Do you want to add it into the documentation, doesn't seem to be included when I build the docs?\n> \n> 3.  Docstring for _latex_ looks like it has an indentation problem that needs fixing.\n\nLooks like (2) and (3) both probably need to be fixed.",
    "created_at": "2010-05-19T04:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82375",
    "user": "@jasongrout"
}
```

Replying to [comment:6 rbeezer]:
> Hi Jason,
> 
> Nice patch.
> 
> 1.  Do you think this should be called "free_module_element_callable_symbolic_dense"?  Technically these don't have to be vectors, and they do have entries over a ring?  Yes, that's an unwieldy name.  ;-)  Just asking.

Well, Sage thinks that it is a field:


```

sage: f(x,y)=x^2+y                             
sage: R=f.parent()
sage: R 
Callable function ring with arguments (x, y)
sage: R.is_field()
True
```



> 
> 2.  Do you want to add it into the documentation, doesn't seem to be included when I build the docs?
> 
> 3.  Docstring for _latex_ looks like it has an indentation problem that needs fixing.

Looks like (2) and (3) both probably need to be fixed.



---

archive/issue_comments_082376.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-19T04:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82376",
    "user": "@jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082377.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n\n> Callable function ring with arguments (x, y)\n> sage: R.is_field()\n> True\n\nAnd I trusted the _repr_ output?\n\nFailing a few tests, in the obvious way, in \n\n```\n/sage/dev/devel/sage-main/sage/symbolic/expression.pyx\n/sage/dev/devel/sage-main/sage/calculus/calculus.py\n```\n\n\n(and not done testing).",
    "created_at": "2010-05-19T04:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82377",
    "user": "@rbeezer"
}
```

Replying to [comment:7 jason]:

> Callable function ring with arguments (x, y)
> sage: R.is_field()
> True

And I trusted the _repr_ output?

Failing a few tests, in the obvious way, in 

```
/sage/dev/devel/sage-main/sage/symbolic/expression.pyx
/sage/dev/devel/sage-main/sage/calculus/calculus.py
```


(and not done testing).



---

archive/issue_comments_082378.json:
```json
{
    "body": "On 4.4.2.rc0 I get the following failures.  The one for R is totally unrelated I believe, the others I saw are just the obvious differences in format for functions involved in this patch.\n\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage-main/sage/symbolic/expression.pyx # 4 doctests failed\n        sage -t  devel/sage-main/sage/calculus/calculus.py # 2 doctests failed   \n        sage -t  devel/sage-main/sage/interfaces/r.py # 1 doctests failed        \n        sage -t  devel/sage-main/sage/modules/free_module_element.pyx # 3 doctests failed\n\n```\n",
    "created_at": "2010-05-19T05:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82378",
    "user": "@rbeezer"
}
```

On 4.4.2.rc0 I get the following failures.  The one for R is totally unrelated I believe, the others I saw are just the obvious differences in format for functions involved in this patch.


```
The following tests failed:

        sage -t  devel/sage-main/sage/symbolic/expression.pyx # 4 doctests failed
        sage -t  devel/sage-main/sage/calculus/calculus.py # 2 doctests failed   
        sage -t  devel/sage-main/sage/interfaces/r.py # 1 doctests failed        
        sage -t  devel/sage-main/sage/modules/free_module_element.pyx # 3 doctests failed

```




---

archive/issue_comments_082379.json:
```json
{
    "body": "Attachment [trac-8947-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket8947/trac-8947-doctest-fix.patch) by @jasongrout created at 2010-06-01 22:08:08\n\napply on top of previous patches",
    "created_at": "2010-06-01T22:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82379",
    "user": "@jasongrout"
}
```

Attachment [trac-8947-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket8947/trac-8947-doctest-fix.patch) by @jasongrout created at 2010-06-01 22:08:08

apply on top of previous patches



---

archive/issue_comments_082380.json:
```json
{
    "body": "Okay, the doctest issues you mentioned should all be fixed now.",
    "created_at": "2010-06-01T22:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82380",
    "user": "@jasongrout"
}
```

Okay, the doctest issues you mentioned should all be fixed now.



---

archive/issue_comments_082381.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-01T22:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82381",
    "user": "@jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082382.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-02T04:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82382",
    "user": "@rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082383.json:
```json
{
    "body": "sage/calculus, sage/modules, sage/symbolic directories pass all tests, and documentation for `vector_callable_symbolic_dense` looks good.\n\nPositive review.",
    "created_at": "2010-06-02T04:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82383",
    "user": "@rbeezer"
}
```

sage/calculus, sage/modules, sage/symbolic directories pass all tests, and documentation for `vector_callable_symbolic_dense` looks good.

Positive review.



---

archive/issue_comments_082384.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8947#issuecomment-82384",
    "user": "@qed777"
}
```

Resolution: fixed
