# Issue 137: notebook %form widget maker

archive/issues_000137.json:
```json
{
    "body": "Assignee: boothby\n\nExample:\n\n\n```\n%form\n\nEnter an integer n=300\nEnter a prime p=2\nShow prime factors only primes=False\nOperate on primes op=\n  * sum\n  * product\n\n{{{\n  v = factor(n%p)\n  if primes:\n    for i in v:\n      print i[0]\n  else:\n    for i in v:\n      print \"%d**%d\"%i\n  if op == \"sum\"\n    print \"Sum of prime factors\"\n    s = 0\n    for i in v:\n      s += i[0]*i[1]\n    print s\n  if op == \"product\"\n    print \"Product of distinct prime factors\"\n    s = 1\n    for i in v:\n      s *= i[0]\n    print s\n}}}\n\n```\n\n\nThe above would make an interactive widget which would make an input form for the variables used in the code block.  A submit button would read the input fields and display output from the code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/137\n\n",
    "created_at": "2006-10-18T23:59:58Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "notebook %form widget maker",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/137",
    "user": "boothby"
}
```
Assignee: boothby

Example:


```
%form

Enter an integer n=300
Enter a prime p=2
Show prime factors only primes=False
Operate on primes op=
  * sum
  * product

{{{
  v = factor(n%p)
  if primes:
    for i in v:
      print i[0]
  else:
    for i in v:
      print "%d**%d"%i
  if op == "sum"
    print "Sum of prime factors"
    s = 0
    for i in v:
      s += i[0]*i[1]
    print s
  if op == "product"
    print "Product of distinct prime factors"
    s = 1
    for i in v:
      s *= i[0]
    print s
}}}

```


The above would make an interactive widget which would make an input form for the variables used in the code block.  A submit button would read the input fields and display output from the code.

Issue created by migration from https://trac.sagemath.org/ticket/137





---

archive/issue_comments_000644.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-08T20:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/137#issuecomment-644",
    "user": "jason"
}
```

Resolution: duplicate



---

archive/issue_comments_000645.json:
```json
{
    "body": "This will be easily possible with William's \"manipulate\" or \"interact\" patch on #1322.",
    "created_at": "2008-03-08T20:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/137#issuecomment-645",
    "user": "jason"
}
```

This will be easily possible with William's "manipulate" or "interact" patch on #1322.
