# Issue 137: notebook %form widget maker

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2006-10-18 23:59:58

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


---

Comment by jason created at 2008-03-08 20:50:07

Resolution: duplicate


---

Comment by jason created at 2008-03-08 20:50:07

This will be easily possible with William's "manipulate" or "interact" patch on #1322.
