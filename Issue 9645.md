# Issue 9645: Bugs in the computation of Groebner bases over the integers

Issue created by migration from https://trac.sagemath.org/ticket/9645

Original creator: SimonKing

Original creation time: 2010-07-30 13:56:53

Assignee: malb

CC:  jakobkroeker jpflori

Keywords: Groebner basis integer

A bug report on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/46124695d2f7469a) made me play around with the following example:


```
sage: R.<x,y>=PolynomialRing(ZZ,2)
sage: I = R*(4*x^2*y^2+2*x*y^3+3*x*y,2*x^2+x*y,2*y^2)
sage: I.groebner_basis(algorithm='libsingular:std')
[x^2*y, x*y^2, 2*x^2 + x*y, 3*x*y, 2*y^2]
sage: (I.groebner_basis(algorithm='libsingular:std')*R).interreduced_basis()
[x^2*y, x*y^2, 2*x^2 + x*y, 3*x*y, 2*y^2]
sage: I.groebner_basis(algorithm='libsingular:slimgb')
[2*x^2 + x*y, 3*x*y, 2*y^2]
sage: (I.groebner_basis(algorithm='libsingular:slimgb')*R).interreduced_basis()
[2*x^2 + x*y, 3*x*y, 2*y^2]
sage: (I.groebner_basis(algorithm='toy:buchberger')*R).interreduced_basis()
[2*x^2 + x*y, 3*x*y, 2*y^2]
sage: I.groebner_basis(algorithm='toy:buchberger2')
[4*x^2*y^2 + 2*x*y^3 + 3*x*y, 2*x^2 + x*y, 2*y^2]
sage: (I.groebner_basis(algorithm='toy:buchberger2')*R).interreduced_basis()
[2*x^2 + x*y, 3*x*y, 2*y^2]
sage: I.groebner_basis(algorithm='magma')
[x^2*y, x*y^2, 2*x^2 + x*y, 3*x*y, 2*y^2]
```


*__First bug__*

The documentation suggests that `toy:buchberger2` is supposed to return a reduced Groebner basis, but it doesn't. So, to the very least, the documentation is a little unclear.

*__Second bug__*

The five algorithms return two _different_ reduced Groebner bases. So, at least one of them must be wrong.

`libsingular:std` and `magma` agree on this result:

```
sage: G1 = I.groebner_basis(algorithm='libsingular:std'); G1
[x^2*y, x*y^2, 2*x^2 + x*y, 3*x*y, 2*y^2]
```

while `libsingular:slimgb`, `toy:buchberger` and `toy:buchberger2` agree on this result:

```
sage: G2 = I.groebner_basis(algorithm='libsingular:slimgb'); G2
[2*x^2 + x*y, 3*x*y, 2*y^2]
```


The following suggests that at least answer `G2` is wrong:

```
sage: [g.reduce(G2) for g in G1]
[x^2*y, x*y^2, 0, 0, 0]
sage: [g.reduce(G1) for g in G2]
[0, 0, 0]
```


Let us check that indeed the element `x*y^2` belongs to the original ideal:

```
sage: y*I.0 -2*y^3*I.1 -x*I.2
x*y^2
```


Conclusion: *Under the assumption that there is no bug in reduce and the basic arithmetic, it is proven that slimgb and toy:buchberger(2) give a wrong answer.*

*__Third bug__*

Of course, if `G1` is a Groebner basis then all of its elements must belong to the ideal. Singular provides a command to express the Groebner basis elements as combinations of the given ideal generators: `liftstd`.

But `liftstd` apparently gives a wrong answer:

```
sage: r = singular(R)
sage: i = singular(I)
sage: singular.eval('matrix m')
'matrix m;'
sage: print singular.eval('liftstd(%s,m)'%i.name())
_[1]=2*y^2
_[2]=-3*x*y
_[3]=2*x^2+x*y
_[4]=x*y^2
_[5]=x^2*y
sage: singular('m')
0,-1,   0,y,     -3*x-y,
0,2*y^2,1,-2*y^3,2*y^3+5*y,
1,0,    0,-x,    -x-2*y
```


So, up to order and sign, the answer given by `liftstd` coincides with `G1`. Now, the matrix `m` should transform the list of ideal generators into the Groebner basis. But it does not for the element `x^2*y`:

```
sage: print singular.eval('matrix(%s)*m'%i.name())
_[1,1]=2*y^2
_[1,2]=-3*x*y
_[1,3]=2*x^2+x*y
_[1,4]=x*y^2
_[1,5]=-12*x^3*y^2-6*x^2*y^3+x^2*y-4*y^3
```


So, there is a bug in `liftstd` as well. At least, it is possible to verify that `x^2*y` (and therefore all of `G1`) belongs to the ideal:

```
sage: 2*y*I.1 - x*I.0 + (2*x^3 + x^2*y - x)*I.2
x^2*y
```



---

Comment by SimonKing created at 2010-07-30 14:54:03

There is a new singular spkg at #8059. However, this does not solve the problem. The only difference is that now one has

```
sage: I.groebner_basis(algorithm='toy:buchberger2')
[2*x^2 + x*y, 3*x*y, 2*y^2]
```

Hence, the result is reduced (the first bug is gone), but still wrong.


---

Comment by SimonKing created at 2010-07-30 15:23:26

At least the problem with `liftstd` has disappeared in Singular-3-1-1.

But since the bug in `slimgb` persists, I reported [upstream](http://www.singular.uni-kl.de:8002/trac/ticket/245).


---

Comment by duleorlovic created at 2010-08-03 12:18:01

Changing assignee from malb to duleorlovic.


---

Comment by duleorlovic created at 2010-08-03 12:18:01

Replying to [comment:1 SimonKing]:

> There is a new singular spkg at #8059. However, this does not solve the problem. The only difference is that now one has ` sage: I.groebner_basis(algorithm='toy:buchberger2') [2*x^2 + x*y, 3*x*y, 2*y^2] ` Hence, the result is reduced (the first bug is gone), but still wrong.

Result is *right *because reduce is different in field and in ring (please read [this book chapter 4](http://books.google.com/books?id=Caoxi78WaIAC&pg=PA201&dq=adams+loustaunau+introduction+to+grobner+bases+chapter+4&hl=sr&ei=CwdYTJzPHcGe4AaZsKmhBw&sa=X&oi=book_result&ct=result&resnum=1&ved=0CCkQ6AEwAA#v=onepage&q=adams%20loustaunau%20introduction%20to%20grobner%20bases%20chapter%204&f=false)).

x*y!^2  is reduced to zero on [2*x!^2 + x*y, 3*x*y, 2*y!^2] because x*y!^2 - (y*3*x*y-x*2*y!^2)=0.

So libsingular:slimgb and toy:buchberger2 are right, and singular:std and libsingular:std has bug.


---

Comment by SimonKing created at 2010-08-03 14:18:07

Replying to [comment:4 duleorlovic]:
> Replying to [comment:1 SimonKing]:
> 
> > There is a new singular spkg at #8059. However, this does not solve the problem. The only difference is that now one has ` sage: I.groebner_basis(algorithm='toy:buchberger2') [2*x^2 + x*y, 3*x*y, 2*y^2] ` Hence, the result is reduced (the first bug is gone), but still wrong.
> 
> Result is *right *because reduce is different in field and in ring (please read [this book chapter 4](http://books.google.com/books?id=Caoxi78WaIAC&pg=PA201&dq=adams+loustaunau+introduction+to+grobner+bases+chapter+4&hl=sr&ei=CwdYTJzPHcGe4AaZsKmhBw&sa=X&oi=book_result&ct=result&resnum=1&ved=0CCkQ6AEwAA#v=onepage&q=adams%20loustaunau%20introduction%20to%20grobner%20bases%20chapter%204&f=false)).
> 
> x*y!^2  is reduced to zero on [2*x!^2 + x*y, 3*x*y, 2*y!^2] because x*y!^2 - (y*3*x*y-x*2*y!^2)=0.

I don't buy this and repeat that this is not a reduction. Martin, do you agree?


---

Comment by SimonKing created at 2010-08-03 16:12:07

Many thanks to Michael Brickenstein who explained [here](http://groups.google.com/group/sage-devel/browse_thread/thread/46124695d2f7469a) that our misunderstanding comes from the fact that Dusan expects to work with _weak_ Gröbner bases - a notion that I was not aware of.

Singular computes a strong Gröbner basis. So, not a bug.

By the way, the remaining problem with slimgb is solved upstream: By now (i.e., with the current developer version and in the next official release), slimgb will raise an error when being called for an ideal over the integers.


---

Comment by jakobkroeker created at 2015-01-27 01:13:12

In sage Singular was recently upgraded to 3.1.7.
1. What I do not understand, a slimgb call in standalone Singular 3.1.7  raises now an error

```
ring rng = integer,(x,y),dp;
option("redSB");
ideal I = 4*x^2*y^2 + 2*x*y^3 + 3*x*y, 2*x^2 + x*y, 2*y^2;
slimgb(I);
//? not implemented for rings with rings as coeffients}}}
```

but the slimgb call in sage

```
sage: R.<x,y>=PolynomialRing(ZZ,2)
sage: I = R*(4*x^2*y^2+2*x*y^3+3*x*y,2*x^2+x*y,2*y^2)
sage: I.groebner_basis(algorithm='libsingular:slimgb')
}}} 
succeeds. Why is that ??
2. if there is really a difference between strong and weak groebner basis, 
then at least the 'toy:buchberger','toy:buchberger2' and 'groebner_basis' documentation   should be updated ,
hoping that nobody intermixes weak and strong groebner bases  by accident. (new ticket?)

3. Remark: the liftstd bug seems fixed


---

Comment by kcrisman created at 2020-10-08 12:48:39

See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA


---

Comment by kcrisman created at 2020-10-08 12:48:39

Changing priority from critical to major.
