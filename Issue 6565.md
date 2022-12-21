# Issue 6565: substitution cryptosystems: converting a key from alphabetic to numerical values

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-20 11:49:03

Assignee: somebody

Keywords: substitution cryptosystem

The class `SubstitutionCryptosystem` accepts keys whose values are alphabetic characters. We should implement a method to allow a key
to be converted between alphabetic characters and numerical values. For example, here is what I have in mind:

```
sage: A = AlphabeticStrings()
sage: S = SubstitutionCryptosystem(A)
sage: key = S.random_key()
ABC
sage: S.alphabet_to_numbers(key)
012
sage: S.numbers_to_alphabet([0, 1, 2])
ABC
```



---

Comment by tscholl2 created at 2015-05-26 19:01:50

Changing status from new to needs_review.


---

Comment by tscholl2 created at 2015-05-26 19:01:50

I think it would be better to add some kind of conversion/coercion for string monoids instead of specifically for substitution cryptosystem strings. Also I don't believe there is an ASCII/byte value monoid. In either case, that would be a different ticket (see #9118). If someone still wants that they should open a new ticket.

This is also pretty easy to do by hand if someone wants to. For example, to take and element from an alphabetic monoid to a list of ascii values you can use this:

```
    sage: A = AlphabeticStrings()
    sage: a = A.encoding("THISISATURTLE")
    sage: map(lambda x: ord(str(x)),a)
    [84, 72, 73, 83, 73, 83, 65, 84, 85, 82, 84, 76, 69]
```


I'm going to set this as won't fix and give it positive review.


---

Comment by tscholl2 created at 2015-05-26 19:02:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-06-19 08:38:23

Resolution: wontfix
