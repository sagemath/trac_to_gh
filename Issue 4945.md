# Issue 4945: LaTeX for gp elements shouldn't use verbatim environment

archive/issues_004945.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: jsmath\n\nGary wrote: \n \nWhen using the SAGE notebook with typeset on, the command \n\n``` \n  gp(2+2) \n```\n \ngives the error `'Unknown environment \"verbatim\"'`. \n \nTyping \n\n``` \n  gp(2+2) \n```\n \nin the SAGE command line works fine. I think it is a latex output \nerror. \n \nI can confirm this bug. It is caused by the generic latex method for Expect elements: \n \n\n``` \nsage: latex(gp(2+2)) \n\\begin{verbatim}4\\end{verbatim} \n```\n \n \nwhich apparently doesn't play well with jsMath. \n \n`search_src(\"begin{verbatim}\")` returns 43 hits.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4945\n\n",
    "created_at": "2009-01-06T16:56:57Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "LaTeX for gp elements shouldn't use verbatim environment",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4945",
    "user": "malb"
}
```
Assignee: cwitty

Keywords: jsmath

Gary wrote: 
 
When using the SAGE notebook with typeset on, the command 

``` 
  gp(2+2) 
```
 
gives the error `'Unknown environment "verbatim"'`. 
 
Typing 

``` 
  gp(2+2) 
```
 
in the SAGE command line works fine. I think it is a latex output 
error. 
 
I can confirm this bug. It is caused by the generic latex method for Expect elements: 
 

``` 
sage: latex(gp(2+2)) 
\begin{verbatim}4\end{verbatim} 
```
 
 
which apparently doesn't play well with jsMath. 
 
`search_src("begin{verbatim}")` returns 43 hits.

Issue created by migration from https://trac.sagemath.org/ticket/4945





---

archive/issue_comments_037535.json:
```json
{
    "body": "| search_src(\"begin{verbatim}\") returns 43 hits\nMost of those are in docstrings, so we don't need to worry about them.  I think the only relevant instances are interfaces/expect.py, misc/latex.py, misc/log.py.  I don't understand how verbatim is used in the last two.  The attached patch seems to fix the problem in the first one: `latex(gp(2+2))` works in the notebook now.\n\n(The solution here is to change verbatim to verb -- search misc/all.py for 'verbatim' to see very similar code) and then to use the jsMath 'verb' extension.)",
    "created_at": "2009-01-06T18:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37535",
    "user": "jhpalmieri"
}
```

| search_src("begin{verbatim}") returns 43 hits
Most of those are in docstrings, so we don't need to worry about them.  I think the only relevant instances are interfaces/expect.py, misc/latex.py, misc/log.py.  I don't understand how verbatim is used in the last two.  The attached patch seems to fix the problem in the first one: `latex(gp(2+2))` works in the notebook now.

(The solution here is to change verbatim to verb -- search misc/all.py for 'verbatim' to see very similar code) and then to use the jsMath 'verb' extension.)



---

archive/issue_comments_037536.json:
```json
{
    "body": "The extra \\require{verb} worries me, since it is included each time an element is LaTeXified. Shouldn't it be in some header?\n\nCheers,\nMartin",
    "created_at": "2009-01-06T20:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37536",
    "user": "malb"
}
```

The extra \require{verb} worries me, since it is included each time an element is LaTeXified. Shouldn't it be in some header?

Cheers,
Martin



---

archive/issue_comments_037537.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> The extra \\require{verb} worries me, since it is included each time an element is LaTeXified. Shouldn't it be in some header?\n\nYes, maybe it should.  I couldn't figure out where, though.\n\n(For more on the jsMath verb extension, including different ways of loading it, see [this web page](http://www.math.union.edu/~dpvc/jsMath/authors/verb.html).)",
    "created_at": "2009-01-06T20:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37537",
    "user": "jhpalmieri"
}
```

Replying to [comment:2 malb]:
> The extra \require{verb} worries me, since it is included each time an element is LaTeXified. Shouldn't it be in some header?

Yes, maybe it should.  I couldn't figure out where, though.

(For more on the jsMath verb extension, including different ways of loading it, see [this web page](http://www.math.union.edu/~dpvc/jsMath/authors/verb.html).)



---

archive/issue_comments_037538.json:
```json
{
    "body": "I just posted a slightly different version of the patch.  It doesn't address malb's issue, but it is a little cleaner: it only includes '\\require{verb}' if in notebook mode.",
    "created_at": "2009-01-06T20:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37538",
    "user": "jhpalmieri"
}
```

I just posted a slightly different version of the patch.  It doesn't address malb's issue, but it is a little cleaner: it only includes '\require{verb}' if in notebook mode.



---

archive/issue_comments_037539.json:
```json
{
    "body": "Okay, here's a patch which (I think) addresses malb's issue.",
    "created_at": "2009-01-07T00:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37539",
    "user": "jhpalmieri"
}
```

Okay, here's a patch which (I think) addresses malb's issue.



---

archive/issue_comments_037540.json:
```json
{
    "body": "Attachment [4945.patch](tarball://root/attachments/some-uuid/ticket4945/4945.patch) by malb created at 2009-01-07 12:13:37\n\nPatch looks good.",
    "created_at": "2009-01-07T12:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37540",
    "user": "malb"
}
```

Attachment [4945.patch](tarball://root/attachments/some-uuid/ticket4945/4945.patch) by malb created at 2009-01-07 12:13:37

Patch looks good.



---

archive/issue_comments_037541.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T02:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37541",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_037542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T02:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4945#issuecomment-37542",
    "user": "mabshoff"
}
```

Resolution: fixed
