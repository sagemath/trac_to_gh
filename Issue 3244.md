# Issue 3244: [with patch, needs review] add support for inner plethysms of symmetric functions

archive/issues_003244.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jbandlow sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3244\n\n",
    "created_at": "2008-05-17T20:45:56Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] add support for inner plethysms of symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3244",
    "user": "@mwhansen"
}
```
Assignee: @mwhansen

CC:  @jbandlow sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/3244





---

archive/issue_comments_022458.json:
```json
{
    "body": "For the most part this looks really good!  However, before I can give this a positive review, I have two requests for improvement.\n\n1.  Currently\n\nsage: S = SFASchur(QQ); S([]).inner_plethysm(S([2,1]))\n\nblows up. However, in general, S([]).inner_plethysm(S[p]), for p a partition of n, should return S([n]).\n\n2. The doc string currently contains examples, but no explanation.  I propose the following doc for inner_plethysm:\n\nInner plethysm is a bilinear product on the ring of symmetric functions.  The result of f.inner_plethysm(g) on the Schur functions f = S(la), g = S(mu) can be interpreted as follows.  Setting n = mu.size(), the function g can be thought of as the character of an irreducible representation, $\\rho$, of the symmetric group $S_n$.  Let N be the dimension of this representation.  If the number of parts of la is greater then N, then f.inner_plethysm(g) = 0 by definition.  Otherwise, we can interpret f as the character of an irreducible $GL_N$ representation, call it $\\sigma$.  Now $\\sigma \\circ \\rho$ is an $S_n$ representation and, by definition, the character of this representation is f.inner_plethysm(g).\n\nREFERENCES:\n    King, R. \"Branching rules for $GL_m \\supset \\Sigma_n $ and the evaluation of inner plethysms.\" J. Math. Phys. 15, 258 (1974)",
    "created_at": "2008-05-22T18:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22458",
    "user": "@jbandlow"
}
```

For the most part this looks really good!  However, before I can give this a positive review, I have two requests for improvement.

1.  Currently

sage: S = SFASchur(QQ); S([]).inner_plethysm(S([2,1]))

blows up. However, in general, S([]).inner_plethysm(S[p]), for p a partition of n, should return S([n]).

2. The doc string currently contains examples, but no explanation.  I propose the following doc for inner_plethysm:

Inner plethysm is a bilinear product on the ring of symmetric functions.  The result of f.inner_plethysm(g) on the Schur functions f = S(la), g = S(mu) can be interpreted as follows.  Setting n = mu.size(), the function g can be thought of as the character of an irreducible representation, $\rho$, of the symmetric group $S_n$.  Let N be the dimension of this representation.  If the number of parts of la is greater then N, then f.inner_plethysm(g) = 0 by definition.  Otherwise, we can interpret f as the character of an irreducible $GL_N$ representation, call it $\sigma$.  Now $\sigma \circ \rho$ is an $S_n$ representation and, by definition, the character of this representation is f.inner_plethysm(g).

REFERENCES:
    King, R. "Branching rules for $GL_m \supset \Sigma_n $ and the evaluation of inner plethysms." J. Math. Phys. 15, 258 (1974)



---

archive/issue_comments_022459.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-22T20:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22459",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022460.json:
```json
{
    "body": "Attachment [3244.patch](tarball://root/attachments/some-uuid/ticket3244/3244.patch) by @mwhansen created at 2008-05-22 20:15:35\n\nI updated the patch to address your concerns.  Note that inner plethysm isn't bilinear, but only linear in the first argument.\n\n(I also updated 2144 to have this patch.)",
    "created_at": "2008-05-22T20:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22460",
    "user": "@mwhansen"
}
```

Attachment [3244.patch](tarball://root/attachments/some-uuid/ticket3244/3244.patch) by @mwhansen created at 2008-05-22 20:15:35

I updated the patch to address your concerns.  Note that inner plethysm isn't bilinear, but only linear in the first argument.

(I also updated 2144 to have this patch.)



---

archive/issue_comments_022461.json:
```json
{
    "body": "Yes, of course you are right, bilinear is not correct, I have updated doc below.  More troubling to me is that I am now getting:\n\nsage: S = SFASchur(QQ); f = S([2,1])\nsage: S([]).inner_plethysm(f)\n2*s[3]\n\nAccording to my reference the answer should be s[3].  Am I wrong about this?\n\nNew suggested doc:\n            Retuns the inner plethysm of self with x.\n            \n            The result of f.inner_plethysm(g) is linear in f and linear in\n            \"homogeneous pieces\" of g.  So, to describe this function, we assume\n            without loss that f is some Schur function S(la) and g is a\n            homogeneous symmetric function of degree n. The function g can be\n            thought of as the character of an irreducible representation, rho,\n            of the symmetric group S_n. Let N be the dimension of this\nrepresentation. If the number of parts of la is greater then N, then\n            f.inner_plethysm(g) = 0 by definition.  Otherwise, we can interpret f\n            as the character of an irreducible GL_N representation, call it\nsigma. Now sigma circ rho is an S_n representation and, by\n            definition, the character of this representation is\n            f.inner_plethysm(g).",
    "created_at": "2008-05-22T21:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22461",
    "user": "@jbandlow"
}
```

Yes, of course you are right, bilinear is not correct, I have updated doc below.  More troubling to me is that I am now getting:

sage: S = SFASchur(QQ); f = S([2,1])
sage: S([]).inner_plethysm(f)
2*s[3]

According to my reference the answer should be s[3].  Am I wrong about this?

New suggested doc:
            Retuns the inner plethysm of self with x.
            
            The result of f.inner_plethysm(g) is linear in f and linear in
            "homogeneous pieces" of g.  So, to describe this function, we assume
            without loss that f is some Schur function S(la) and g is a
            homogeneous symmetric function of degree n. The function g can be
            thought of as the character of an irreducible representation, rho,
            of the symmetric group S_n. Let N be the dimension of this
representation. If the number of parts of la is greater then N, then
            f.inner_plethysm(g) = 0 by definition.  Otherwise, we can interpret f
            as the character of an irreducible GL_N representation, call it
sigma. Now sigma circ rho is an S_n representation and, by
            definition, the character of this representation is
            f.inner_plethysm(g).



---

archive/issue_comments_022462.json:
```json
{
    "body": "Attachment [3244.2.patch](tarball://root/attachments/some-uuid/ticket3244/3244.2.patch) by @jbandlow created at 2008-05-25 07:03:50\n\nThis looks good to me now.  Nice work, Mike.",
    "created_at": "2008-05-25T07:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22462",
    "user": "@jbandlow"
}
```

Attachment [3244.2.patch](tarball://root/attachments/some-uuid/ticket3244/3244.2.patch) by @jbandlow created at 2008-05-25 07:03:50

This looks good to me now.  Nice work, Mike.



---

archive/issue_comments_022463.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-25T14:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22463",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_022464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-25T14:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3244#issuecomment-22464",
    "user": "mabshoff"
}
```

Resolution: fixed
