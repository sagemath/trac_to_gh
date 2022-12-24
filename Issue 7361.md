# Issue 7361: implement is_regular() for a graph

archive/issues_007361.json:
```json
{
    "body": "Assignee: rlm\n\nKeywords: graph regular\n\nThe attached patch implements a method that checks whether a graph is regular.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7361\n\n",
    "created_at": "2009-10-31T14:11:02Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "implement is_regular() for a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7361",
    "user": "AlexGhitza"
}
```
Assignee: rlm

Keywords: graph regular

The attached patch implements a method that checks whether a graph is regular.


Issue created by migration from https://trac.sagemath.org/ticket/7361





---

archive/issue_comments_061681.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-31T14:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61681",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061682.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-31T20:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61682",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061683.json:
```json
{
    "body": "There is not necessarily a vertex named 0 in the graph, in which case the first line of your patch does not do what you want...\n\nWhat you could try is something like that :\n\n```\nit=self.degree_iterator()\nk=it.next()\nfor i in it:\n   if i!=k:\n       return False\nreturn True\n```\n\n\nBesides, if you want your docstring to be \"formally\" correct, here are a few remarks :\nThe first line of the docstring should describe in a few words what the function does. In your case : \"Tests whether the graph is regular\" or simething similar should do.\n\nTwo lines later, you explain a bit more in details what it does if necessary.\n\nYou can create an INPUT: section to describe the parameters of your method.\n\nBesides : when you want something to be written through LaTeX, like u_1 or \\sum_{x=0}^\\infty , you have to write it like that :\n\n```\n`u_1`\nor\n`\\sum_{x=0}^\\infty`\n```\n\nWhen you want a word to be understood a a python keyword, like the name of a variable, or the values True/False, you add two times this sign :\n\n```\n``True``\n``False``\n```\n\n\nAnd this is all I can think of for the moment :-)\n\nNathann",
    "created_at": "2009-10-31T20:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61683",
    "user": "ncohen"
}
```

There is not necessarily a vertex named 0 in the graph, in which case the first line of your patch does not do what you want...

What you could try is something like that :

```
it=self.degree_iterator()
k=it.next()
for i in it:
   if i!=k:
       return False
return True
```


Besides, if you want your docstring to be "formally" correct, here are a few remarks :
The first line of the docstring should describe in a few words what the function does. In your case : "Tests whether the graph is regular" or simething similar should do.

Two lines later, you explain a bit more in details what it does if necessary.

You can create an INPUT: section to describe the parameters of your method.

Besides : when you want something to be written through LaTeX, like u_1 or \sum_{x=0}^\infty , you have to write it like that :

```
`u_1`
or
`\sum_{x=0}^\infty`
```

When you want a word to be understood a a python keyword, like the name of a variable, or the values True/False, you add two times this sign :

```
``True``
``False``
```


And this is all I can think of for the moment :-)

Nathann



---

archive/issue_comments_061684.json:
```json
{
    "body": "Attachment [trac_7361.patch](tarball://root/attachments/some-uuid/ticket7361/trac_7361.patch) by AlexGhitza created at 2009-11-01 02:43:37\n\nThanks for looking at this.  I have replaced the patch with a new one incorporating your comments.",
    "created_at": "2009-11-01T02:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61684",
    "user": "AlexGhitza"
}
```

Attachment [trac_7361.patch](tarball://root/attachments/some-uuid/ticket7361/trac_7361.patch) by AlexGhitza created at 2009-11-01 02:43:37

Thanks for looking at this.  I have replaced the patch with a new one incorporating your comments.



---

archive/issue_comments_061685.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-01T02:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61685",
    "user": "AlexGhitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061686.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-01T08:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61686",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061687.json:
```json
{
    "body": "Now it looks perfect to me :-)\n\nPositive review, and thank you for your work !!!\n\nNathann",
    "created_at": "2009-11-01T08:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61687",
    "user": "ncohen"
}
```

Now it looks perfect to me :-)

Positive review, and thank you for your work !!!

Nathann



---

archive/issue_comments_061688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T04:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7361#issuecomment-61688",
    "user": "mhansen"
}
```

Resolution: fixed
