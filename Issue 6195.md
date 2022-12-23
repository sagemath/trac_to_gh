# Issue 6195: [with patch, needs review] in symbolic Expression.math() return a dictionary with matched values of wildcards

archive/issues_006195.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mhansen\n\nWhile matching patterns containing wildcards in symbolic expressions, GiNaC supports returning the sub expressions that match the given wildcards.\n\nAttached patch wraps this interface.\n\nThe current interface for .match() on sage.symbolic.expression.Expression is to return False if there was a match, and True otherwise. The patch changes this to return a dictionary with the wildcards in the pattern as keys. This might result in an empty dictionary being returned. See the doctests in the patch for examples.\n\nI am open to suggestions for improvements on this interface. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6195\n\n",
    "created_at": "2009-06-03T15:24:16Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] in symbolic Expression.math() return a dictionary with matched values of wildcards",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6195",
    "user": "burcin"
}
```
Assignee: burcin

CC:  mhansen

While matching patterns containing wildcards in symbolic expressions, GiNaC supports returning the sub expressions that match the given wildcards.

Attached patch wraps this interface.

The current interface for .match() on sage.symbolic.expression.Expression is to return False if there was a match, and True otherwise. The patch changes this to return a dictionary with the wildcards in the pattern as keys. This might result in an empty dictionary being returned. See the doctests in the patch for examples.

I am open to suggestions for improvements on this interface. 


Issue created by migration from https://trac.sagemath.org/ticket/6195





---

archive/issue_comments_049472.json:
```json
{
    "body": "Attachment\n\nI don't understand this.\n\nWhy does the first match but the second not?  \n\n```\nsage: ((x+y)).match(w0+w1)\n{$1: x, $0: y}\nsage: ((x+x)).match(w0+w1)\n```\n\n\n\nCan you explain the difference in these behaviours?\n\n```\nsage: ((x+y)^a).match((x+y)^a)\n{}\nsage: print ((x+y)^a).match((x+y)^b)\nNone\n```\n",
    "created_at": "2009-06-15T21:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49472",
    "user": "ncalexan"
}
```

Attachment

I don't understand this.

Why does the first match but the second not?  

```
sage: ((x+y)).match(w0+w1)
{$1: x, $0: y}
sage: ((x+x)).match(w0+w1)
```



Can you explain the difference in these behaviours?

```
sage: ((x+y)^a).match((x+y)^a)
{}
sage: print ((x+y)^a).match((x+y)^b)
None
```




---

archive/issue_comments_049473.json:
```json
{
    "body": "Replying to [comment:1 ncalexan]:\n> Why does the first match but the second not?  \n {{{\n sage: ((x+y)).match(w0+w1)\n {$1: x, $0: y}\n sage: ((x+x)).match(w0+w1)\n }}}\n\n\n```\nsage: t = (x+x); t\n2*x\nsage: t.operator()\n<built-in function mul>\n```\n\n\nYou're looking for an add object, matching doesn't work algebraically in this case. We could start a \"pitfalls of pattern matching in symbolics\" wiki page to document these.\n\n> Can you explain the difference in these behaviours?\n {{{\n sage: ((x+y)<sup>a).match((x+y)</sup>a)\n {}\n sage: print ((x+y)<sup>a).match((x+y)</sup>b)\n None\n }}}\n\nThe first example doesn't have any wildcards. It is a match, so it returns a dictionary, but without any keys. There is no match in the second example, so we return None. As I say in the description, I'm open to suggestions to improve the interface.",
    "created_at": "2009-06-23T21:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49473",
    "user": "burcin"
}
```

Replying to [comment:1 ncalexan]:
> Why does the first match but the second not?  
 {{{
 sage: ((x+y)).match(w0+w1)
 {$1: x, $0: y}
 sage: ((x+x)).match(w0+w1)
 }}}


```
sage: t = (x+x); t
2*x
sage: t.operator()
<built-in function mul>
```


You're looking for an add object, matching doesn't work algebraically in this case. We could start a "pitfalls of pattern matching in symbolics" wiki page to document these.

> Can you explain the difference in these behaviours?
 {{{
 sage: ((x+y)<sup>a).match((x+y)</sup>a)
 {}
 sage: print ((x+y)<sup>a).match((x+y)</sup>b)
 None
 }}}

The first example doesn't have any wildcards. It is a match, so it returns a dictionary, but without any keys. There is no match in the second example, so we return None. As I say in the description, I'm open to suggestions to improve the interface.



---

archive/issue_comments_049474.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-23T21:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49474",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049475.json:
```json
{
    "body": "Attachment\n\napply after the first patch",
    "created_at": "2009-07-17T09:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49475",
    "user": "AlexGhitza"
}
```

Attachment

apply after the first patch



---

archive/issue_comments_049476.json:
```json
{
    "body": "Changing keywords from \"\" to \"symbolic expression match\".",
    "created_at": "2009-07-17T09:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49476",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "symbolic expression match".



---

archive/issue_comments_049477.json:
```json
{
    "body": "The patch looks good to me.  Nick's questions above were very good, and it's good to have the answers in a visible place so I've added these two to the docstring of `match()`.",
    "created_at": "2009-07-17T09:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49477",
    "user": "AlexGhitza"
}
```

The patch looks good to me.  Nick's questions above were very good, and it's good to have the answers in a visible place so I've added these two to the docstring of `match()`.



---

archive/issue_comments_049478.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T13:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6195#issuecomment-49478",
    "user": "mvngu"
}
```

Resolution: fixed
