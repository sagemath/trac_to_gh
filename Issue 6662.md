# Issue 6662: [with patch, needs review] sampling from a general discrete probability distribution

archive/issues_006662.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  kohel\n\nThis patch exposes the general discrete distribution code in the Gnu Scientific Library (GSL). It provides a fast way to sample from a user-defined discrete probability distribution, and it also extends the DiscreteProbabilitySpace class by allowing sampling from the defined distribution.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6662\n\n",
    "created_at": "2009-07-31T14:32:08Z",
    "labels": [
        "statistics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] sampling from a general discrete probability distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6662",
    "user": "carlohamalainen"
}
```
Assignee: mhampton

CC:  kohel

This patch exposes the general discrete distribution code in the Gnu Scientific Library (GSL). It provides a fast way to sample from a user-defined discrete probability distribution, and it also extends the DiscreteProbabilitySpace class by allowing sampling from the defined distribution.

Issue created by migration from https://trac.sagemath.org/ticket/6662





---

archive/issue_comments_054678.json:
```json
{
    "body": "Why is the reference manual formatting broken? After doing \"sage -docbuild reference html\" the examples in the entry \"Interface to gsl discrete random variable generator\" in Probability have examples that are not formatted. Why? What's going wrong with the docstring formatting in my pyx file?",
    "created_at": "2009-07-31T14:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54678",
    "user": "carlohamalainen"
}
```

Why is the reference manual formatting broken? After doing "sage -docbuild reference html" the examples in the entry "Interface to gsl discrete random variable generator" in Probability have examples that are not formatted. Why? What's going wrong with the docstring formatting in my pyx file?



---

archive/issue_comments_054679.json:
```json
{
    "body": "Attachment [general_discrete_distribution.patch](tarball://root/attachments/some-uuid/ticket6662/general_discrete_distribution.patch) by carlohamalainen created at 2009-07-31 17:32:14",
    "created_at": "2009-07-31T17:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54679",
    "user": "carlohamalainen"
}
```

Attachment [general_discrete_distribution.patch](tarball://root/attachments/some-uuid/ticket6662/general_discrete_distribution.patch) by carlohamalainen created at 2009-07-31 17:32:14



---

archive/issue_comments_054680.json:
```json
{
    "body": "Fixed the docstring formatting.",
    "created_at": "2009-07-31T17:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54680",
    "user": "carlohamalainen"
}
```

Fixed the docstring formatting.



---

archive/issue_comments_054681.json:
```json
{
    "body": "I can try to test this, but I'm wondering how (for example) do I generate a list of 10 numbers in (0.1,2.3) randomly having the normal distribution with mean 1 and standard deviation 2? (Similar question for other common distributions.)",
    "created_at": "2009-08-02T02:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54681",
    "user": "@wdjoyner"
}
```

I can try to test this, but I'm wondering how (for example) do I generate a list of 10 numbers in (0.1,2.3) randomly having the normal distribution with mean 1 and standard deviation 2? (Similar question for other common distributions.)



---

archive/issue_comments_054682.json:
```json
{
    "body": "This patch installs fine with 4.1.1.a1 on an amd64 machine running ubuntu 9.04. It passes sage -testall, except for the known failures.\n\nI'm a little concerned about the docstrings. If I were more of a probability expert maybe this would not be an issue but not being an expert (which maybe is a good thing?) I don't see how to use it to do some basic sampling which might be useful for teaching a first course in probability.",
    "created_at": "2009-08-02T10:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54682",
    "user": "@wdjoyner"
}
```

This patch installs fine with 4.1.1.a1 on an amd64 machine running ubuntu 9.04. It passes sage -testall, except for the known failures.

I'm a little concerned about the docstrings. If I were more of a probability expert maybe this would not be an issue but not being an expert (which maybe is a good thing?) I don't see how to use it to do some basic sampling which might be useful for teaching a first course in probability.



---

archive/issue_comments_054683.json:
```json
{
    "body": "I only wrote an interface to one particular discrete distribution in gsl. I'll add stuff for normal distribution, binomial, etc later this month (travelling and no time to do Sage).",
    "created_at": "2009-08-06T17:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54683",
    "user": "carlohamalainen"
}
```

I only wrote an interface to one particular discrete distribution in gsl. I'll add stuff for normal distribution, binomial, etc later this month (travelling and no time to do Sage).



---

archive/issue_comments_054684.json:
```json
{
    "body": "Closing this as a duplicate of #6662.",
    "created_at": "2009-09-09T10:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54684",
    "user": "mvngu"
}
```

Closing this as a duplicate of #6662.



---

archive/issue_comments_054685.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-09T10:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54685",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_054686.json:
```json
{
    "body": "You mean #6827!  That wasted 20 minutes for me, Minh.\n\n :)",
    "created_at": "2011-06-15T18:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6662#issuecomment-54686",
    "user": "@kcrisman"
}
```

You mean #6827!  That wasted 20 minutes for me, Minh.

 :)
