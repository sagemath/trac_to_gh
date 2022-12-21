# Issue 2148: PolyBoRi inconsistency

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-13 13:06:07

Assignee: malb

CC:  malb

Keywords: polybori


```
sage: P.<x,y> = PolynomialRing(GF(2),2,order='degrevlex')
sage: x > y
True

sage: P.<x,y> = BooleanPolynomialRing(2,order='degrevlex')
sage: x > y
False
```


This should be changed because it leads to funny performance figures.


---

Attachment

fix monomial order keywords in polybori wrapper


---

Comment by burcin created at 2008-02-17 16:53:55

Changing assignee from malb to burcin.


---

Comment by burcin created at 2008-02-17 16:53:55

Changing status from new to assigned.


---

Comment by burcin created at 2008-02-17 16:53:55

attachment:2148-polybori_monomial_order_keywords.patch corrects the monomial order keywords in the `PolyBoRi` wrapper.


---

Comment by malb created at 2008-02-17 17:53:04

I am not convinced the patch fixes the issue:

'dp' and 'Dp' refer to degrevlex and deglex respectively and in neither of those x < y.


```
sage: P.<x,y> = PolynomialRing(GF(2),order='degrevlex')
sage: x > y
True
sage: P.<x,y> = PolynomialRing(GF(2),order='deglex')
sage: x > y
True
```


However, there is a deglex with variables inverted ordering ib PolyBoRi which has no Singular/Sage equivalent AFAIK:


```
sage: B.<x,y> = BooleanPolynomialRing(2,order='deglex')
sage: x > y
True
sage: B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')
sage: x > y
False
```



---

Comment by burcin created at 2008-02-17 18:35:48

You're right, it's not so simple. I'll look at it a bit more.


---

Comment by burcin created at 2008-02-27 09:06:03


```
On Wed, 20 Feb 2008 10:40:09 +0100
Alexander Dreyer <alexander.dreyer`@`itwm.fraunhofer.de> wrote:

> PolyBoRi does not implement degrevlex (dp), but a variant, which we
> called dp_asc. It is adp (not a dlex, as Martin states), but with
> variables reversed. The reason for this was, that this can be
> implemented more efficiently on our ZDD-based data structure. So, for
> correcting the command
> 
> B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')
> 
> you have to reverse the variable vector before it is returned to <x, y>.
> (If there's something like BooleanVariable(idx), it has to be mapped to
> BooleVariable(n-idx).)
```



---

Comment by burcin created at 2008-03-08 13:26:49

reverse variables for degrevlex to dp_asc conversion


---

Attachment

attachment:2148-polybori-fix_degrevlex.patch arranges the variable indexes in the Sage - `PolyBoRi` interface to handle the difference between degrevlex and dp_asc orders.

Note that with this patch, printing is reversed when using dp_asc orders:


```
sage: P.<x,y,z> = BooleanPolynomialRing(3,order='degrevlex')
sage: x*y*z
z*y*x
sage: P.<x,y,z> = BooleanPolynomialRing(3,order='lex')
sage: x*y*z
x*y*z
```



---

Comment by mhansen created at 2008-03-16 18:32:23

Looks good to me.


---

Comment by mabshoff created at 2008-03-18 00:08:24

Resolution: fixed


---

Comment by mabshoff created at 2008-03-18 00:08:24

Merged 2148-polybori-fix_degrevlex.patch in Sage 2.11.alpha0
