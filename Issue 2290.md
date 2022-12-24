# Issue 2290: [with easy patch] typo in calculus.py

archive/issues_002290.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2290\n\n",
    "created_at": "2008-02-24T09:48:13Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "[with easy patch] typo in calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2290",
    "user": "zimmerma"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/2290





---

archive/issue_comments_015188.json:
```json
{
    "body": "Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2290/8681.patch) by zimmerma created at 2008-02-24 09:48:36",
    "created_at": "2008-02-24T09:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2290#issuecomment-15188",
    "user": "zimmerma"
}
```

Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2290/8681.patch) by zimmerma created at 2008-02-24 09:48:36



---

archive/issue_comments_015189.json:
```json
{
    "body": "Hmm, I am not convinced that the result is correct:\n\n```\n88\t88\t    We can also make \\class{CallableSymbolicExpressions}, which is a \\class{SymbolicExpression} \n89\t \t    that are functions of variables in a fixed order. Each \n \t89\t    that is function of variables in a fixed order. Each \n90\t90\t    \\class{SymbolicExpression} has a function() method used to create a \n91\t91\t    \\class{CallableSymbolicExpression}.\n```\n\nWhile I agree that it should be singular, I think an article is missing. I guess in British English the above without the article would be correct, but with my American English I would like to see an article there.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T17:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2290#issuecomment-15189",
    "user": "mabshoff"
}
```

Hmm, I am not convinced that the result is correct:

```
88	88	    We can also make \class{CallableSymbolicExpressions}, which is a \class{SymbolicExpression} 
89	 	    that are functions of variables in a fixed order. Each 
 	89	    that is function of variables in a fixed order. Each 
90	90	    \class{SymbolicExpression} has a function() method used to create a 
91	91	    \class{CallableSymbolicExpression}.
```

While I agree that it should be singular, I think an article is missing. I guess in British English the above without the article would be correct, but with my American English I would like to see an article there.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_015190.json:
```json
{
    "body": "Attachment [sage-2290-english.patch](tarball://root/attachments/some-uuid/ticket2290/sage-2290-english.patch) by was created at 2008-02-24 20:47:18\n\nmy attempt, as a native english speaker",
    "created_at": "2008-02-24T20:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2290#issuecomment-15190",
    "user": "was"
}
```

Attachment [sage-2290-english.patch](tarball://root/attachments/some-uuid/ticket2290/sage-2290-english.patch) by was created at 2008-02-24 20:47:18

my attempt, as a native english speaker



---

archive/issue_comments_015191.json:
```json
{
    "body": "I am neither an american nor a british english speaker, but the new patch seems definitively better\nto me (it also fixes the extra 's' in CallableSymbolicExpressions which I did not spot).",
    "created_at": "2008-02-25T14:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2290#issuecomment-15191",
    "user": "zimmerma"
}
```

I am neither an american nor a british english speaker, but the new patch seems definitively better
to me (it also fixes the extra 's' in CallableSymbolicExpressions which I did not spot).



---

archive/issue_comments_015192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T15:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2290#issuecomment-15192",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015193.json:
```json
{
    "body": "Merged sage-2290-english.patch in Sage 2.10.3.alpha0",
    "created_at": "2008-02-25T15:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2290#issuecomment-15193",
    "user": "mabshoff"
}
```

Merged sage-2290-english.patch in Sage 2.10.3.alpha0
