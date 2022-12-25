# Issue 6290: Allow latex_name=LaTeX keyword while defining symbolic function

archive/issues_006290.json:
```json
{
    "body": "CC:  @williamstein\n\nKeywords: latex_name, symbolic function\n\nIn new symbolics, underlying \"sage.symbolic.SFunction\" class allows\none to pass the keyword \"latex_name=LaTeX\". It would be really good if we expose this feature at the user interface level. Currently,\nSage (4.0.1) raises error if one tries to do so.\n\n\nExample uses:\n\n\n```\nriemann(x) = function('riemann', x, latex_name=\"\\\\mathcal{R}\")\nlatex( riemann(x) )\n\\mathcal{R}\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6290\n\n",
    "created_at": "2009-06-14T23:29:44Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Allow latex_name=LaTeX keyword while defining symbolic function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6290",
    "user": "https://github.com/golam-m-hossain"
}
```
CC:  @williamstein

Keywords: latex_name, symbolic function

In new symbolics, underlying "sage.symbolic.SFunction" class allows
one to pass the keyword "latex_name=LaTeX". It would be really good if we expose this feature at the user interface level. Currently,
Sage (4.0.1) raises error if one tries to do so.


Example uses:


```
riemann(x) = function('riemann', x, latex_name="\\mathcal{R}")
latex( riemann(x) )
\mathcal{R}
```


Issue created by migration from https://trac.sagemath.org/ticket/6290





---

archive/issue_comments_050123.json:
```json
{
    "body": "Nice.  Could you add more to the docstring for function (at least the one that I get by default when I do function? from the sage prompt) that explains what happens to all kwds arguments?  You do give a nice example (with riemann), but a sentence or two explaining what is going on would be very nice.",
    "created_at": "2009-06-15T17:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50123",
    "user": "https://github.com/williamstein"
}
```

Nice.  Could you add more to the docstring for function (at least the one that I get by default when I do function? from the sage prompt) that explains what happens to all kwds arguments?  You do give a nice example (with riemann), but a sentence or two explaining what is going on would be very nice.



---

archive/issue_comments_050124.json:
```json
{
    "body": "Attachment [allow-keyword-arguments-such-as-latex_name-in-symbolic-functions.patch](tarball://root/attachments/some-uuid/ticket6290/allow-keyword-arguments-such-as-latex_name-in-symbolic-functions.patch) by @golam-m-hossain created at 2009-06-15 20:07:59",
    "created_at": "2009-06-15T20:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50124",
    "user": "https://github.com/golam-m-hossain"
}
```

Attachment [allow-keyword-arguments-such-as-latex_name-in-symbolic-functions.patch](tarball://root/attachments/some-uuid/ticket6290/allow-keyword-arguments-such-as-latex_name-in-symbolic-functions.patch) by @golam-m-hossain created at 2009-06-15 20:07:59



---

archive/issue_comments_050125.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> Nice.  Could you add more to the docstring for function (at least the one that I get by default when I do function? from the sage prompt) that explains what happens to all kwds arguments?  \n\nThanks for your comments! As you suggested, I have updated the patch with expanded docstrings.",
    "created_at": "2009-06-15T20:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50125",
    "user": "https://github.com/golam-m-hossain"
}
```

Replying to [comment:3 was]:
> Nice.  Could you add more to the docstring for function (at least the one that I get by default when I do function? from the sage prompt) that explains what happens to all kwds arguments?  

Thanks for your comments! As you suggested, I have updated the patch with expanded docstrings.



---

archive/issue_comments_050126.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-15T20:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50126",
    "user": "https://github.com/ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_050127.json:
```json
{
    "body": "Merged in sage-4.1.alpha0.",
    "created_at": "2009-06-24T09:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50127",
    "user": "https://github.com/rlmill"
}
```

Merged in sage-4.1.alpha0.



---

archive/issue_comments_050128.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50128",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_050129.json:
```json
{
    "body": "Would something similar be possible whenever a variable is defined?\nE.g. if I want to use multiple subscripts, I would like to define\nvar('A_gs', latex_name=\"A_{gs}\"). \n\nThat would make it really flexible.",
    "created_at": "2009-06-25T10:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50129",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

Would something similar be possible whenever a variable is defined?
E.g. if I want to use multiple subscripts, I would like to define
var('A_gs', latex_name="A_{gs}"). 

That would make it really flexible.



---

archive/issue_comments_050130.json:
```json
{
    "body": "Replying to [comment:8 schymans]:\n> Would something similar be possible whenever a variable is defined?\n> E.g. if I want to use multiple subscripts, I would like to define\n> var('A_gs', latex_name=\"A_{gs}\"). \n\nHmmm, thats a great suggestion. Could you please post this to sage-devel?",
    "created_at": "2009-06-25T10:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6290#issuecomment-50130",
    "user": "https://github.com/golam-m-hossain"
}
```

Replying to [comment:8 schymans]:
> Would something similar be possible whenever a variable is defined?
> E.g. if I want to use multiple subscripts, I would like to define
> var('A_gs', latex_name="A_{gs}"). 

Hmmm, thats a great suggestion. Could you please post this to sage-devel?
