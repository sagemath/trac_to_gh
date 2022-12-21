# Issue 5326: support weighted term orderings

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-02-21 02:07:21

Assignee: malb

CC:  john_perry

Jacob wrote on [sage-devel]:

> From reading the documentation of the TermOrder command, it looks 
> like if I want to use a term order not defined in SAGE, I should 
> be able to make my term order a string that can be passed to 
> Singular.  This works for some term orderings, but not for those 
> that have commas in their definitions.  Judging from the code, I 
> think that SAGE sees the comma and assumes that I want a block 
> ordering (which I don't).

> For example, if I want weighted reverse lex ordering with some
> weights, I can do that in Singular:
 {{{
ring rr=0,(x,y),wp(2,3);
poly f=x2+y3;
deg(f);
9
poly g = x<sup>3*y+y</sup>3;
ideal I = f,g;
std(I);
_[1]=y3+x2
_[2]=x3y-x2
_[3]=x5+x2y2
 }}}

> But not in SAGE:

```
sage: T = TermOrder("wp(2,3)")
Traceback (most recent call last):
...
TypeError: wp(2,3) is not a valid term ordering
```


```
sage: R.<x,y> = PolynomialRing(QQ,2,T)
sage: R._singular_()
//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
```



---

Comment by john_perry created at 2012-01-26 18:48:28

Changing status from new to needs_info.


---

Comment by john_perry created at 2012-01-26 18:48:28

I believe this is a duplicate of #11316, in which case it has been fixed!


---

Comment by chapoton created at 2017-04-06 10:05:56

Changing status from needs_info to positive_review.


---

Comment by chapoton created at 2017-04-06 10:05:56

weighted term orders are implemented since long..


---

Comment by chapoton created at 2017-04-06 10:07:56

Changing status from positive_review to needs_info.


---

Comment by chapoton created at 2017-04-06 10:07:56

maybe not so clear..


---

Comment by chapoton created at 2017-06-02 13:28:48

Changing status from needs_info to positive_review.


---

Comment by chapoton created at 2017-06-02 13:28:48

The correct syntax is 

```
T =  TermOrder("wp",(2,3))
```



---

Comment by embray created at 2017-07-13 07:54:31

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).


---

Comment by embray created at 2017-07-13 07:54:31

Resolution: wontfix
