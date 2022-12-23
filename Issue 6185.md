# Issue 6185: [with patch, needs review] Add SBox -> CNF Conversion

archive/issues_006185.json:
```json
{
    "body": "Assignee: malb\n\nCC:  mvngu rpw burcin\n\nKeywords: crypto, cnf\n\nWhile not really complicated it is nice to have a direct conversion from S-Boxes to CNF since SAT-solves enjoy some attention right now in crypto.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6185\n\n",
    "created_at": "2009-06-02T13:56:38Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Add SBox -> CNF Conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6185",
    "user": "malb"
}
```
Assignee: malb

CC:  mvngu rpw burcin

Keywords: crypto, cnf

While not really complicated it is nice to have a direct conversion from S-Boxes to CNF since SAT-solves enjoy some attention right now in crypto.

Issue created by migration from https://trac.sagemath.org/ticket/6185





---

archive/issue_comments_049378.json:
```json
{
    "body": "Minh, can I ask you to review this ticket?",
    "created_at": "2009-06-02T13:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49378",
    "user": "malb"
}
```

Minh, can I ask you to review this ticket?



---

archive/issue_comments_049379.json:
```json
{
    "body": "Replying to [comment:1 malb]:\n> Minh, can I ask you to review this ticket?\nHi Martin. Sorry for my simple question: Is there a reference or paper that describes the algorithm you use for converting an S-box to CNF? I only know about the application of SAT to cryptanalysis by reading this ticket. I usually find it much easier to understand code if I can access a reference somewhere that describes the algorithm.",
    "created_at": "2009-06-03T19:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49379",
    "user": "mvngu"
}
```

Replying to [comment:1 malb]:
> Minh, can I ask you to review this ticket?
Hi Martin. Sorry for my simple question: Is there a reference or paper that describes the algorithm you use for converting an S-box to CNF? I only know about the application of SAT to cryptanalysis by reading this ticket. I usually find it much easier to understand code if I can access a reference somewhere that describes the algorithm.



---

archive/issue_comments_049380.json:
```json
{
    "body": "Hi Minh,\n\nthe standard reference for SAT-solvers in block cipher cryptanalysis is:\n\n   http://eprint.iacr.org/2007/024\n\nI've implemented a converter along those lines at\n\n   http://bitbucket.org/malb/algebraic_attacks/src/tip/anf2cnf.py\n\nwhich isn't ready for inclusion yet. This ticket follows a different approach and converts the S-Box directly. The algorithm used is the standard algorithm for computing CNF from a truth table, \n\ncf. `sage.sage.logic.boolformula`",
    "created_at": "2009-06-03T22:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49380",
    "user": "malb"
}
```

Hi Minh,

the standard reference for SAT-solvers in block cipher cryptanalysis is:

   http://eprint.iacr.org/2007/024

I've implemented a converter along those lines at

   http://bitbucket.org/malb/algebraic_attacks/src/tip/anf2cnf.py

which isn't ready for inclusion yet. This ticket follows a different approach and converts the S-Box directly. The algorithm used is the standard algorithm for computing CNF from a truth table, 

cf. `sage.sage.logic.boolformula`



---

archive/issue_comments_049381.json:
```json
{
    "body": "Hi Burcin, Ralf,\n\ncan I ask for this (hopefully) easy review?",
    "created_at": "2009-06-08T10:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49381",
    "user": "malb"
}
```

Hi Burcin, Ralf,

can I ask for this (hopefully) easy review?



---

archive/issue_comments_049382.json:
```json
{
    "body": "My 2 cents:\n\n* the complexity is 'n * 2**m' (instead of 'm * 2**n'):\n\n```\n  for x in X:                        <-- 2^m\n      for output_bit in output_bits: <-- n\n```\n\n* typos:\n   * line 866: evaluate instead of evaulate\n   * line 840: endianness instead of endianess\n\n* maybe add an exception if xi or yi has wrong size\n\n* maybe (but as you like) construct x's on the fly:\n\n```\n  for e in xrange(2**m):\n      x = self.to_bits(e)\n```\n\notherwise seems good to me.",
    "created_at": "2009-06-11T07:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49382",
    "user": "ylchapuy"
}
```

My 2 cents:

* the complexity is 'n * 2**m' (instead of 'm * 2**n'):

```
  for x in X:                        <-- 2^m
      for output_bit in output_bits: <-- n
```

* typos:
   * line 866: evaluate instead of evaulate
   * line 840: endianness instead of endianess

* maybe add an exception if xi or yi has wrong size

* maybe (but as you like) construct x's on the fly:

```
  for e in xrange(2**m):
      x = self.to_bits(e)
```

otherwise seems good to me.



---

archive/issue_comments_049383.json:
```json
{
    "body": "Attachment\n\nThe attached updated patch addresses the reviewer's comments. Is that a positive review then?",
    "created_at": "2009-06-11T11:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49383",
    "user": "malb"
}
```

Attachment

The attached updated patch addresses the reviewer's comments. Is that a positive review then?



---

archive/issue_comments_049384.json:
```json
{
    "body": "Yes it is. Positive review.",
    "created_at": "2009-06-11T13:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49384",
    "user": "ylchapuy"
}
```

Yes it is. Positive review.



---

archive/issue_comments_049385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T20:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6185#issuecomment-49385",
    "user": "ncalexan"
}
```

Resolution: fixed
