# Issue 9868: finite field bug

archive/issues_009868.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\n# Demonstrate a finite field bug in which\n# a product of nonzero elements is equal to 0 \n# (which should not happen in a field)\n#\n# This is the smallest example I could find. It seems salient that\n# the square of p is bigger than a 32-bit C integer. Larger values\n# for p also exhibit the bug, smaller ones do not.\n\np = 2^16 + 1\n\n# Create a quadratic field extension\nK.<alpha> = GF(p^2)\n\n# Choose some non-zero element of K, use the random_element\n# method.\nx = K(0)\nwhile x == K(0):\n  x = K.random_element()\n\nK.<alpha> = GF(p^2)  # this line is necessary for bug\nx_coerce = K(x)\nprint 2*x_coerce  # prints zero\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9869\n\n",
    "created_at": "2010-09-07T18:27:37Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "finite field bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9868",
    "user": "mariah"
}
```
Assignee: AlexGhitza


```
# Demonstrate a finite field bug in which
# a product of nonzero elements is equal to 0 
# (which should not happen in a field)
#
# This is the smallest example I could find. It seems salient that
# the square of p is bigger than a 32-bit C integer. Larger values
# for p also exhibit the bug, smaller ones do not.

p = 2^16 + 1

# Create a quadratic field extension
K.<alpha> = GF(p^2)

# Choose some non-zero element of K, use the random_element
# method.
x = K(0)
while x == K(0):
  x = K.random_element()

K.<alpha> = GF(p^2)  # this line is necessary for bug
x_coerce = K(x)
print 2*x_coerce  # prints zero
```



Issue created by migration from https://trac.sagemath.org/ticket/9869





---

archive/issue_comments_097490.json:
```json
{
    "body": "Duplicate of #10045 .",
    "created_at": "2010-10-19T15:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9868#issuecomment-97490",
    "user": "robertwb"
}
```

Duplicate of #10045 .



---

archive/issue_comments_097491.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-19T15:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9868#issuecomment-97491",
    "user": "robertwb"
}
```

Resolution: duplicate
