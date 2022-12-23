# Issue 2693: Sage should have generic resultant implementation for multivariate polynomials

archive/issues_002693.json:
```json
{
    "body": "Assignee: was\n\nCC:  tscrim vdelecroix vklein\n\nConsider this example, which fails:\n\n```\nR.<x,y> = RR[]\np = x + y\nq = x*y\np.resultant(q)\n```\n\n(as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/1d6289cead33d063#)\n\nThis is because multivariate resultants are implemented using the Singular pexpect interface, which does not support RR.\n\nA workaround for this particular problem (and a possible basis for an improved version) is:\n\n```\np.polynomial(x).resultant(q.polynomial(x)) \n```\n\nThat is, fall back to univariate resultants, which are implemented using Pari and are somewhat more generic.  (This is still not truly generic, though, since there are Sage rings which have no Pari equivalent.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2693\n\n",
    "created_at": "2008-03-28T02:21:37Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "Sage should have generic resultant implementation for multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2693",
    "user": "cwitty"
}
```
Assignee: was

CC:  tscrim vdelecroix vklein

Consider this example, which fails:

```
R.<x,y> = RR[]
p = x + y
q = x*y
p.resultant(q)
```

(as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/1d6289cead33d063#)

This is because multivariate resultants are implemented using the Singular pexpect interface, which does not support RR.

A workaround for this particular problem (and a possible basis for an improved version) is:

```
p.polynomial(x).resultant(q.polynomial(x)) 
```

That is, fall back to univariate resultants, which are implemented using Pari and are somewhat more generic.  (This is still not truly generic, though, since there are Sage rings which have no Pari equivalent.)

Issue created by migration from https://trac.sagemath.org/ticket/2693





---

archive/issue_comments_018528.json:
```json
{
    "body": "In fact, singular resultants are slow compared to other methods, so it would really be a good idea to write specific sage code for resultants.\n\nSee #16749 and #12174 for ideas about it.\n\nJust something like:\n\n\n```\ndef resultant(self, other, variable):\n    m = self.sylvester_matrix(other, variable)\n    return m.determinant()\n```\n\n\nWould be both general for any polynomial ring, and faster than the current implementation. And of course, there could be a lot of cases where things can be done much faster, using specific backends where they are better.",
    "created_at": "2014-08-25T08:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18528",
    "user": "mmarco"
}
```

In fact, singular resultants are slow compared to other methods, so it would really be a good idea to write specific sage code for resultants.

See #16749 and #12174 for ideas about it.

Just something like:


```
def resultant(self, other, variable):
    m = self.sylvester_matrix(other, variable)
    return m.determinant()
```


Would be both general for any polynomial ring, and faster than the current implementation. And of course, there could be a lot of cases where things can be done much faster, using specific backends where they are better.



---

archive/issue_comments_018529.json:
```json
{
    "body": "Changing keywords from \"\" to \"resultant\".",
    "created_at": "2019-05-01T14:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18529",
    "user": "chapoton"
}
```

Changing keywords from "" to "resultant".



---

archive/issue_comments_018530.json:
```json
{
    "body": "New commits:",
    "created_at": "2019-05-01T15:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18530",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_018531.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-05-01T15:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18531",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018532.json:
```json
{
    "body": "green bot, please review",
    "created_at": "2019-05-01T18:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18532",
    "user": "chapoton"
}
```

green bot, please review



---

archive/issue_comments_018533.json:
```json
{
    "body": "hmm, the second doctest is more about univariate polynomials. Maybe it should go there ?",
    "created_at": "2019-05-02T06:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18533",
    "user": "chapoton"
}
```

hmm, the second doctest is more about univariate polynomials. Maybe it should go there ?



---

archive/issue_comments_018534.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2019-05-06T15:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18534",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_018535.json:
```json
{
    "body": "ok, test is now at the right place.",
    "created_at": "2019-05-06T15:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18535",
    "user": "chapoton"
}
```

ok, test is now at the right place.



---

archive/issue_comments_018536.json:
```json
{
    "body": "and the bot is green.",
    "created_at": "2019-05-06T17:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18536",
    "user": "chapoton"
}
```

and the bot is green.



---

archive/issue_comments_018537.json:
```json
{
    "body": "LGTM.",
    "created_at": "2019-05-07T00:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18537",
    "user": "tscrim"
}
```

LGTM.



---

archive/issue_comments_018538.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-05-07T00:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18538",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2019-05-12T21:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18539",
    "user": "vbraun"
}
```

Resolution: fixed
