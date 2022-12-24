# Issue 6403: Custom definitions for latex style

archive/issues_006403.json:
```json
{
    "body": "CC:  mvngu\n\nKeywords: latex\n\n#6290 introduced a way to custom-define the latex style of functions, but it would be great if something similar was made possible for any variable. I used to do it in the following way, but now I get an error message:\n\nsage: var('hi kunsati delyui')\n\nsage: hi._latex_ = lambda: 'h_i'\n     \nsage: kunsati._latex_ = lambda: 'K_{unsat,i}' \n   \nsage: delyui._latex_ = lambda: '\\delta_{yu,i}'\n\n  \nTraceback (most recent call last):\n\n\n...\n\nAttributeError: 'sage.symbolic.expression.Expression' object attribute '_latex_' is read-only\n\n\nComment by Burcin Erocal on sage-devel (25/06/2006):\n\n>Since Expression is a cython class, you cannot overwrite the _latex_() method. \n>\n>Pynac supports setting latex names for variables at creation, but this functionality is not exposed in the wrapper. Another solution by hacking latex_variable_name() might be possible, but I would like to avoid that if possible.\n>\n>Feel free to open a new issue in trac about it.\n>\n>Cheers,\n>Burcin\n\nHow could the Pynac funtionality of setting latex names for variables at creation be exposed?\n\nIssue created by migration from https://trac.sagemath.org/ticket/6403\n\n",
    "created_at": "2009-06-25T12:30:37Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Custom definitions for latex style",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6403",
    "user": "schymans"
}
```
CC:  mvngu

Keywords: latex

#6290 introduced a way to custom-define the latex style of functions, but it would be great if something similar was made possible for any variable. I used to do it in the following way, but now I get an error message:

sage: var('hi kunsati delyui')

sage: hi._latex_ = lambda: 'h_i'
     
sage: kunsati._latex_ = lambda: 'K_{unsat,i}' 
   
sage: delyui._latex_ = lambda: '\delta_{yu,i}'

  
Traceback (most recent call last):


...

AttributeError: 'sage.symbolic.expression.Expression' object attribute '_latex_' is read-only


Comment by Burcin Erocal on sage-devel (25/06/2006):

>Since Expression is a cython class, you cannot overwrite the _latex_() method. 
>
>Pynac supports setting latex names for variables at creation, but this functionality is not exposed in the wrapper. Another solution by hacking latex_variable_name() might be possible, but I would like to avoid that if possible.
>
>Feel free to open a new issue in trac about it.
>
>Cheers,
>Burcin

How could the Pynac funtionality of setting latex names for variables at creation be exposed?

Issue created by migration from https://trac.sagemath.org/ticket/6403





---

archive/issue_comments_051427.json:
```json
{
    "body": "There is no patch above, though the title said there was a patch.",
    "created_at": "2009-11-10T15:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6403#issuecomment-51427",
    "user": "@jasongrout"
}
```

There is no patch above, though the title said there was a patch.



---

archive/issue_comments_051428.json:
```json
{
    "body": "Supposedly, the patch for #6559 fixes this (see comment added to description). Could you review #6559 instead? Thanks!\n\nStan",
    "created_at": "2009-11-10T16:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6403#issuecomment-51428",
    "user": "schymans"
}
```

Supposedly, the patch for #6559 fixes this (see comment added to description). Could you review #6559 instead? Thanks!

Stan



---

archive/issue_comments_051429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-19T11:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6403#issuecomment-51429",
    "user": "@burcin"
}
```

Resolution: fixed



---

archive/issue_comments_051430.json:
```json
{
    "body": "I'm closing this, since #6559 just got merged. It adds a `latex_name` keyword argument to `var()`, which is the functionality requested here.",
    "created_at": "2010-02-19T11:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6403#issuecomment-51430",
    "user": "@burcin"
}
```

I'm closing this, since #6559 just got merged. It adds a `latex_name` keyword argument to `var()`, which is the functionality requested here.
