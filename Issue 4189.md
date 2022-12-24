# Issue 4189: hmm documentation buglet

archive/issues_004189.json:
```json
{
    "body": "Assignee: @williamstein\n\nmapb reported in http://groups.google.com/group/sage-devel/t/8109b386f0e94251\n\n```\nThe fourth argument in the following routine is called \n\"emission_symbols\", while the INPUTS section reports \"emission_state\". \nhmm.DiscreteHiddenMarkovModel(A, B, pi=None, emission_symbols=None, \nname=None, normalize=True) \nn \n    INPUTS: \n        A  -- square matrix of doubles; the state change probabilities \n        B  -- matrix of doubles; emission probabilities \n        pi -- list of floats; probabilities for each initial state \n        emission_state -- list of B.ncols() symbols (just used for \nprinting) \n        name -- (optional) name of the model \n        normalize -- (optional; default=True) whether or not to \nnormalize \n                     the model so the probabilities add to 1 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4189\n\n",
    "created_at": "2008-09-24T10:56:05Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "hmm documentation buglet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4189",
    "user": "mabshoff"
}
```
Assignee: @williamstein

mapb reported in http://groups.google.com/group/sage-devel/t/8109b386f0e94251

```
The fourth argument in the following routine is called 
"emission_symbols", while the INPUTS section reports "emission_state". 
hmm.DiscreteHiddenMarkovModel(A, B, pi=None, emission_symbols=None, 
name=None, normalize=True) 
n 
    INPUTS: 
        A  -- square matrix of doubles; the state change probabilities 
        B  -- matrix of doubles; emission probabilities 
        pi -- list of floats; probabilities for each initial state 
        emission_state -- list of B.ncols() symbols (just used for 
printing) 
        name -- (optional) name of the model 
        normalize -- (optional; default=True) whether or not to 
normalize 
                     the model so the probabilities add to 1 
```


Issue created by migration from https://trac.sagemath.org/ticket/4189





---

archive/issue_comments_030394.json:
```json
{
    "body": "Attachment [trac-4189.patch](tarball://root/attachments/some-uuid/ticket4189/trac-4189.patch) by @williamstein created at 2008-09-24 23:29:19",
    "created_at": "2008-09-24T23:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4189#issuecomment-30394",
    "user": "@williamstein"
}
```

Attachment [trac-4189.patch](tarball://root/attachments/some-uuid/ticket4189/trac-4189.patch) by @williamstein created at 2008-09-24 23:29:19



---

archive/issue_comments_030395.json:
```json
{
    "body": "Looks good to me, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T23:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4189#issuecomment-30395",
    "user": "mabshoff"
}
```

Looks good to me, positive review.

Cheers,

Michael



---

archive/issue_comments_030396.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-25T00:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4189#issuecomment-30396",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-25T00:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4189#issuecomment-30397",
    "user": "mabshoff"
}
```

Resolution: fixed
