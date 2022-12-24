# Issue 9249: Wrong answer in is_hamiltonian if no LP solver available

archive/issues_009249.json:
```json
{
    "body": "Assignee: jason, mvngu, ncohen, rlm\n\nCC:  mvngu\n\nis_hamiltonian always returned False when no LP solver was installed.\n\nFixed !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9249\n\n",
    "created_at": "2010-06-16T13:15:47Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Wrong answer in is_hamiltonian if no LP solver available",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9249",
    "user": "ncohen"
}
```
Assignee: jason, mvngu, ncohen, rlm

CC:  mvngu

is_hamiltonian always returned False when no LP solver was installed.

Fixed !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9249





---

archive/issue_comments_087043.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-16T13:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87043",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087044.json:
```json
{
    "body": "Here it is ! We should also take care of updating the Developper's guide concerning the use of this new exceptions in another ticket.\n\nNathann",
    "created_at": "2010-06-17T10:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87044",
    "user": "ncohen"
}
```

Here it is ! We should also take care of updating the Developper's guide concerning the use of this new exceptions in another ticket.

Nathann



---

archive/issue_comments_087045.json:
```json
{
    "body": "This seems to be installing and passing tests okay but I'm not seeing any new docstring tests that correspond to the new code. Am I missing something? If not, I think more tests should be added (eg, Minh's OP on sage-devel in the thread cited above).",
    "created_at": "2010-06-17T15:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87045",
    "user": "wdj"
}
```

This seems to be installing and passing tests okay but I'm not seeing any new docstring tests that correspond to the new code. Am I missing something? If not, I think more tests should be added (eg, Minh's OP on sage-devel in the thread cited above).



---

archive/issue_comments_087046.json:
```json
{
    "body": "Hmmm.... It is a bit hard to test, though. Minh's commands fails when no LP solver is installed. If we make a docstring for it, the docstring will pass when there is no solver installed, but as soon as a solver is, the doctest will fails. The problem is that we have a flag \"optional CBC\", but nothing like \"optional NOT CBC\" ^^;\n\nNathann",
    "created_at": "2010-06-17T15:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87046",
    "user": "ncohen"
}
```

Hmmm.... It is a bit hard to test, though. Minh's commands fails when no LP solver is installed. If we make a docstring for it, the docstring will pass when there is no solver installed, but as soon as a solver is, the doctest will fails. The problem is that we have a flag "optional CBC", but nothing like "optional NOT CBC" ^^;

Nathann



---

archive/issue_comments_087047.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n> Hmmm.... It is a bit hard to test, though. Minh's commands fails when no LP solver is installed. If we make a docstring for it, the docstring will pass when there is no solver installed, but as soon as a solver is, the doctest will fails. The problem is that we have a flag \"optional CBC\", but nothing like \"optional NOT CBC\" ^^;\n> \n> Nathann\n\nGood point!\n\nI wonder what you think about this idea:\n\nAdd a not tested docstring  (I've forgotten how you do that though) which has one\ntest in the case when the package is loaded and another test in the case when the package is not. There there could be a remark that only one of these will trigger an error exception?",
    "created_at": "2010-06-17T15:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87047",
    "user": "wdj"
}
```

Replying to [comment:4 ncohen]:
> Hmmm.... It is a bit hard to test, though. Minh's commands fails when no LP solver is installed. If we make a docstring for it, the docstring will pass when there is no solver installed, but as soon as a solver is, the doctest will fails. The problem is that we have a flag "optional CBC", but nothing like "optional NOT CBC" ^^;
> 
> Nathann

Good point!

I wonder what you think about this idea:

Add a not tested docstring  (I've forgotten how you do that though) which has one
test in the case when the package is loaded and another test in the case when the package is not. There there could be a remark that only one of these will trigger an error exception?



---

archive/issue_comments_087048.json:
```json
{
    "body": "What do you think of this ? :-)\n\nNathann",
    "created_at": "2010-06-17T15:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87048",
    "user": "ncohen"
}
```

What do you think of this ? :-)

Nathann



---

archive/issue_comments_087049.json:
```json
{
    "body": "Attachment [trac_9249.patch](tarball://root/attachments/some-uuid/ticket9249/trac_9249.patch) by ncohen created at 2010-06-17 15:57:21",
    "created_at": "2010-06-17T15:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87049",
    "user": "ncohen"
}
```

Attachment [trac_9249.patch](tarball://root/attachments/some-uuid/ticket9249/trac_9249.patch) by ncohen created at 2010-06-17 15:57:21



---

archive/issue_comments_087050.json:
```json
{
    "body": "This looks good for now... Applies and passes tests. However, we should use dancing links (exact cover) for is_hamiltonian in general. It may actually turn out to be faster than MILP, I'm not sure. But then it would be a standard feature.",
    "created_at": "2010-06-17T20:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87050",
    "user": "rlm"
}
```

This looks good for now... Applies and passes tests. However, we should use dancing links (exact cover) for is_hamiltonian in general. It may actually turn out to be faster than MILP, I'm not sure. But then it would be a standard feature.



---

archive/issue_comments_087051.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-17T20:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87051",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087052.json:
```json
{
    "body": "You think it can be reduced to dancing links ?? O_o\n\nHow so ? O_o\n\nI'm *very* interested !!\n\nNathann",
    "created_at": "2010-06-17T20:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87052",
    "user": "ncohen"
}
```

You think it can be reduced to dancing links ?? O_o

How so ? O_o

I'm *very* interested !!

Nathann



---

archive/issue_comments_087053.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> You think it can be reduced to dancing links ?? O_o\n> \n> How so ? O_o\n> \n> I'm *very* interested !!\n> \n> Nathann\n\nIt might be a bit of a challenge. As Tom Boothby points out, bipartite matching can easily be reduced to dancing links. We should use that where we can, instead of using optional packages.",
    "created_at": "2010-06-17T20:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87053",
    "user": "rlm"
}
```

Replying to [comment:8 ncohen]:
> You think it can be reduced to dancing links ?? O_o
> 
> How so ? O_o
> 
> I'm *very* interested !!
> 
> Nathann

It might be a bit of a challenge. As Tom Boothby points out, bipartite matching can easily be reduced to dancing links. We should use that where we can, instead of using optional packages.



---

archive/issue_comments_087054.json:
```json
{
    "body": "Well, I clearly agree for bipartite perfect matching, but for is_hamiltonian ? How the hell could we translate the \"connexity\" constraint ?\n\nAnd... Well... :p\n\nI know LP is optional in Sage, but... Well, there are now **many** important functions that use LP, so even if it is optional because of license problems, it is more and more part of Sage's graph library :p\n\nNathan",
    "created_at": "2010-06-17T20:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87054",
    "user": "ncohen"
}
```

Well, I clearly agree for bipartite perfect matching, but for is_hamiltonian ? How the hell could we translate the "connexity" constraint ?

And... Well... :p

I know LP is optional in Sage, but... Well, there are now **many** important functions that use LP, so even if it is optional because of license problems, it is more and more part of Sage's graph library :p

Nathan



---

archive/issue_comments_087055.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87055",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_087056.json:
```json
{
    "body": "The patch here leads to a docbuild warning:\n\n```\nWarning: Missing title for sage.misc.exceptions\n```\n\nPlease see #9571, a blocker for Sage 4.5.2.",
    "created_at": "2010-07-22T02:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9249#issuecomment-87056",
    "user": "mpatel"
}
```

The patch here leads to a docbuild warning:

```
Warning: Missing title for sage.misc.exceptions
```

Please see #9571, a blocker for Sage 4.5.2.
