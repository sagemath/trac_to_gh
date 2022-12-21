# Issue 1104: Ideal() should check arguments better

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-11-05 04:21:16

Assignee: somebody

Keywords: ideal arguments


```
sage: Ideal(3, 5)
Principal ideal (3) of Integer Ring
```


Misleading!


---

Comment by mabshoff created at 2007-12-26 03:05:32

It actually does exactly what it is supposed to do in the documentation [from Ideal?]:

```
        Alternatively, one can also call this function with the syntax
             Ideal(gens)
        where gens is a nonempty list of generators or a single generator.
```

From Sage 2.9.1.1:

```
sage: R.<x,y> = QQ[]
sage: R
Multivariate Polynomial Ring in x, y over Rational Field
sage: R.ideal(x^2,x-y)
Ideal (x^2, x - y) of Multivariate Polynomial Ring in x, y over Rational Field
sage: Ideal([x^2,x-y])
Ideal (x^2, x - y) of Multivariate Polynomial Ring in x, y over Rational Field
sage: Ideal(x^2,x-y)
Principal ideal (x^2) of Multivariate Polynomial Ring in x, y over Rational Field
```



---

Comment by AlexGhitza created at 2008-02-16 23:47:52

The patch fixes the problem pointed out by Nick, and makes Ideal() complain loudly rather than return the wrong thing in other cases.

Before:


```
sage: Ideal(3,5)
Principal ideal (3) of Integer Ring
sage: Ideal(ZZ,3,5)
Principal ideal (3) of Integer Ring
```


After:


```
sage: Ideal(3,5)
Principal ideal (1) of Integer Ring
sage: Ideal(ZZ,3,5)
...

<type 'exceptions.TypeError'>: coerce must be either True or False
```



---

Comment by dmharvey created at 2008-02-23 02:58:14

Sorry this patch doesn't work right. With the patch I get for example:

```
sage: Ideal(2, 4, 6)
[...]
<type 'exceptions.TypeError'>: coerce must be either True or False
```

which is still very confusing.

The recursive function call is not the right way to do this. Should use the `def func(*x, **kwds)` idiom instead; to see an example, look at

```
sage: R.<x> = PolynomialRing(ZZ)
sage: R.ideal??
```



---

Comment by craigcitro created at 2008-06-20 04:25:57

Changing keywords from "ideal arguments" to "ideal arguments, editor_malb".


---

Comment by malb created at 2008-06-25 11:15:25

*state of affairs for editorial meeting 26/06/08*
No movement on my end, sorry.


---

Comment by mabshoff created at 2008-09-27 22:32:40

Change the subject line. 

malb: any hope for this ticket?

Cheers,

Michael


---

Attachment


---

Comment by AlexGhitza created at 2008-09-29 23:19:56

I have completely rewritten the patch in a way that I think addresses the objections given above.


---

Comment by malb created at 2008-09-30 10:25:26

Patch applies cleanly against 3.1.2 and reads good.


---

Comment by mabshoff created at 2008-09-30 11:44:47

Resolution: fixed


---

Comment by mabshoff created at 2008-09-30 11:44:47

Merged in Sage 3.1.3.alpha2
