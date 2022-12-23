# Issue 7231: cryptanalysis of the Vigenere cipher

archive/issues_007231.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  rbeezer rws\n\nKeywords: Vigenere cipher, cryptanalysis\n\nAs the subject says. This depends on #7124.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7231\n\n",
    "created_at": "2009-10-16T00:52:35Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "cryptanalysis of the Vigenere cipher",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7231",
    "user": "mvngu"
}
```
Assignee: somebody

CC:  rbeezer rws

Keywords: Vigenere cipher, cryptanalysis

As the subject says. This depends on #7124.

Issue created by migration from https://trac.sagemath.org/ticket/7231





---

archive/issue_comments_059980.json:
```json
{
    "body": "A method could be added to the `VigenereCryptosystem` class in `src/sage/crypto/classical.py`. I would suggest calling the method something like `cryptanalyze`. If more than one method of cryptanalysis is implemented, then I would suggest providing an `algorithm` keyword argument, so the user can choose between them.\n\nFollow-up ticket: The `AffineCryptosystem` and `ShiftCryptosystem` classes have methods `rank_by_chi_square`, `rank_by_squared_differences`, and `brute_force`. I would suggest making them all available from a single `cryptanalyze` method (with `algorithm` keyword argument) so they are easier to find.",
    "created_at": "2022-04-03T20:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7231#issuecomment-59980",
    "user": "@DaveWitteMorris"
}
```

A method could be added to the `VigenereCryptosystem` class in `src/sage/crypto/classical.py`. I would suggest calling the method something like `cryptanalyze`. If more than one method of cryptanalysis is implemented, then I would suggest providing an `algorithm` keyword argument, so the user can choose between them.

Follow-up ticket: The `AffineCryptosystem` and `ShiftCryptosystem` classes have methods `rank_by_chi_square`, `rank_by_squared_differences`, and `brute_force`. I would suggest making them all available from a single `cryptanalyze` method (with `algorithm` keyword argument) so they are easier to find.
