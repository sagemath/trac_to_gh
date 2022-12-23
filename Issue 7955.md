# Issue 7955: printing unevaluated integrals, limits, etc. broken

archive/issues_007955.json:
```json
{
    "body": "Assignee: burcin\n\nFrom the sage-devel thread here:\n\nhttp://groups.google.com/group/sage-devel/t/592ce36b210c2fbe\n\n\n```\nOn Mon, 11 Jan 2010 23:58:54 -0800 (PST)\n\"marik@mendelu.cz\" <marik@mendelu.cz> wrote:\n\n> Dear sage-devel\n> \n> the following (definite) integral is not evaluated by maxima and show\n> () command should return the same unevaluated integral in TeX\n> notation. I think this was the case in previous versions. On Sage 4.3.\n> I get th following\n> \n> input: integrate(1/(1+sqrt(x)),x,0,1).show()\n> \n> output: \\int integrate\\,{d \\frac{1}{\\sqrt{x} + 1}}\n> \n> expected output: \\int_0^1 \\frac{..}{...} dx\n> \n> What has changed?\n```\n\n\nAfter #7490, we give the function object as the first argument to\ncustom methods of symbolic functions. The function that prints integrals\nis _integrate_latex_() on line 1556 of sage/calculus/calculus.py. It\ngets the function integrate as a first argument, and prints the\nnonsense reported above.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7955\n\n",
    "created_at": "2010-01-16T18:26:41Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "printing unevaluated integrals, limits, etc. broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7955",
    "user": "burcin"
}
```
Assignee: burcin

From the sage-devel thread here:

http://groups.google.com/group/sage-devel/t/592ce36b210c2fbe


```
On Mon, 11 Jan 2010 23:58:54 -0800 (PST)
"marik@mendelu.cz" <marik@mendelu.cz> wrote:

> Dear sage-devel
> 
> the following (definite) integral is not evaluated by maxima and show
> () command should return the same unevaluated integral in TeX
> notation. I think this was the case in previous versions. On Sage 4.3.
> I get th following
> 
> input: integrate(1/(1+sqrt(x)),x,0,1).show()
> 
> output: \int integrate\,{d \frac{1}{\sqrt{x} + 1}}
> 
> expected output: \int_0^1 \frac{..}{...} dx
> 
> What has changed?
```


After #7490, we give the function object as the first argument to
custom methods of symbolic functions. The function that prints integrals
is _integrate_latex_() on line 1556 of sage/calculus/calculus.py. It
gets the function integrate as a first argument, and prints the
nonsense reported above.


Issue created by migration from https://trac.sagemath.org/ticket/7955





---

archive/issue_comments_069415.json:
```json
{
    "body": "Attachment\n\nfix typesetting of unevaluated integrals",
    "created_at": "2010-01-17T09:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7955#issuecomment-69415",
    "user": "burcin"
}
```

Attachment

fix typesetting of unevaluated integrals



---

archive/issue_comments_069416.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T09:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7955#issuecomment-69416",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069417.json:
```json
{
    "body": "attachment:trac_7955-integrate_latex.patch should fix this.",
    "created_at": "2010-01-17T09:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7955#issuecomment-69417",
    "user": "burcin"
}
```

attachment:trac_7955-integrate_latex.patch should fix this.



---

archive/issue_comments_069418.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> attachment:trac_7955-integrate_latex.patch should fix this.\n\n...and it does, on 4.3.1. The code looks good, all doctests pass, and the problem is fixed.",
    "created_at": "2010-01-27T06:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7955#issuecomment-69418",
    "user": "ddrake"
}
```

Replying to [comment:1 burcin]:
> attachment:trac_7955-integrate_latex.patch should fix this.

...and it does, on 4.3.1. The code looks good, all doctests pass, and the problem is fixed.



---

archive/issue_comments_069419.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T06:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7955#issuecomment-69419",
    "user": "ddrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7955#issuecomment-69420",
    "user": "mpatel"
}
```

Resolution: fixed
