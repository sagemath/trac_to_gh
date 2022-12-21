# Issue 8251: traceback when computing E.torsion_subgroup() for an elliptic curve E

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-12 15:29:39

Assignee: cremona

CC:  robertwb was

It's possible to get a traceback for some dumb reason in some cases when computing the torsion subgroup of an elliptic curve:

```
...
Traceback (most recent call last):           for K in J.unramified_outside([i],3):
  File "", line 1, in <module>
    
  File "/tmp/tmpSAW9n5/___code___.py", line 6, in <module>
    T=E.torsion_subgroup()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3515, in torsion_subgroup
    self.__torsion_subgroup = ell_torsion.EllipticCurveTorsionSubgroup(self, algorithm)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_torsion.py", line 159, in __init__
    if self.__K is RationalField() and algorithm in pari_torsion_algorithms:
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/rational_field.py", line 208, in __init__
    self._assign_names(('x',),normalize=False) # ???
  File "parent_gens.pyx", line 327, in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2854)
  File "category_object.pyx", line 336, in sage.structure.category_object.CategoryObject._assign_names (sage/structure/category_object.c:3286)
ValueError: variable names cannot be changed after object creation.
```


The above is caused by running this script:

```
J=JonesDatabase()
P=Primes()
for E in cremona_optimal_curves([0..50]):
    T=E.torsion_subgroup()
    i=E.conductor()
    if i.is_prime():
       for K in J.unramified_outside([i],3):
                F=E.base_extend(K)
                T_1=F.torsion_subgroup() 

                if T != T_1:
                    E.label();
                    K.is_galois();
                    T;
                    T_1;
    else:
        j=2 
        while j < i :
            if j.is_prime():
                n=i/j
                if n.is_integral():
                    for K in J.unramified_outside([j],3):
                        F=E.base_extend(K)

                        T_1=F.torsion_subgroup() 
                        if T != T_1:
                            E.label();

                            K.is_galois();
                            T;
                            T_1;
            j=P.next(j)
```



---

Comment by cremona created at 2010-02-13 18:07:32

This may be related to #7930.  In both cases, a sequence of elliptic curves and number fields and reduction mod primes is carried out, and something is getting confused about all the finite fields which getting created.

It would be a great help if we could simplify the script which causes this.  There's an outer look through curves and an inner loop through certain fields, depending on the curve, and then the torsion of the curve over that field is computed.  I'll try to do that.


---

Comment by cremona created at 2010-06-25 07:38:42

This error has (a) nothing to do with elliptic curve code and (b) nothing to do with number fields at all!

It is arising because in several places in Sage source code the field of rational numbers is referred to as `RationalField()` instead of as QQ.  This should not matter, since the `RationalField()` call is supposed to return the unique object of its class, which is pre-assigned to QQ, but apparently sometimes it does go through the process of running the code in `RationalField.__init__()`.  That code contains the mysterious line

```
        self._assign_names(('x',),normalize=False) # ???
```

-- note that some one (not me) has added those ??? -- I cannot see any reason for assigning any "names" to QQ.  It is this call to the _assign_names() function which sometimes raises the error.  I do not know why it only happens sometimes.

It might therefore be a good idea to change the title of this ticket.  I will ask other people for their opinion.  Robert?  (You added the ???)  William?  (You added the assign_names line!)

I would like to try commenting out that line and testing the entire Sage library.


---

Comment by robertwb created at 2010-06-25 20:49:54

Easier to reproduce.


```
sage: RationalField()
Rational Field
sage: list(JonesDatabase().unramified_outside([3], 3))
[Number Field in a with defining polynomial x^3 - 3*x + 1, Number Field in a with defining polynomial x^3 - 3]
sage: RationalField()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (436, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/sekhon/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/rational_field.pyc in __init__(self)
    212         print id(self)
    213         ParentWithGens.__init__(self, self, category = Fields())
--> 214         self._assign_names(('x',),normalize=False) # ???
    215         self._populate_coercion_lists_(element_constructor=rational.Rational, init_no_parent=True)
    216 

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2869)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/category_object.so in sage.structure.category_object.CategoryObject._assign_names (sage/structure/category_object.c:3287)()

ValueError: variable names cannot be changed after object creation.

```



---

Comment by robertwb created at 2010-06-25 21:01:59

Changing assignee from cremona to nthiery.


---

Comment by robertwb created at 2010-06-25 21:01:59

Changing component from elliptic curves to categories.


---

Comment by wjp created at 2011-01-08 21:51:23

Even easier to reproduce:


```
RationalField()
x = load(SAGE_ROOT + "/data/jones/jones.sobj")
RationalField()
```



---

Comment by wjp created at 2011-01-08 21:58:21

As far as I can tell, `jones.sobj` contains a `RationalField` with `_names` equal to `'x'`, while in current versions of sage, `QQ._names` equals `('x',)`.


---

Comment by wjp created at 2011-01-09 06:34:47

As suggested by William, I've converted the pickle `data/jones/jones.sobj` to be less dependent on the version of Sage by storing the polynomials as lists of python ints rather than as actual polynomials. This solves the problem encountered in this ticket, and also prevents similar things in the future.

I'll try to create a new jones spkg soon, but for now I'm attaching the sage patch and the updated `data/jones/jones.sobj`.

There was also a new polynomial on John Jones' webpage, so the contents of this new sobj are slightly different than the previous version of the database.


---

Attachment


---

Attachment

It would also be possible to fix unpickling the old sobj (and any other potentially broken old pickles) by creating an empty `RationalField.__setstate__(state)`.


---

Comment by kcrisman created at 2020-10-08 12:47:47

See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA  Is this still even relevant?  I assume the database exists somewhere still.


---

Comment by cremona created at 2020-10-08 12:50:08

Replying to [comment:13 kcrisman]:
> See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA  Is this still even relevant?  I assume the database exists somewhere still.

https://hobbes.la.asu.edu/NFDB/


---

Comment by kcrisman created at 2020-10-08 15:06:25

John, does that mean the bug in question still is a problem?  I only updated this since _you_ mentioned it in the sage-devel thread :-) hope the downgrade is okay.

I just risked destroying my Sage build (computer OS upgrade) to try this out, but I think it might not be a problem any longer.


```
sage: RationalField()
Rational Field
sage: from sage.env import SAGE_SHARE
sage: x = load(os.path.join(SAGE_SHARE, 'jones', 'jones.sobj'))
sage: RationalField()
Rational Field
```


Do you think that is the 'modern' equivalent of comment:5?  For what it's worth, apparently I `sage -i' and loaded the database correctly:

```
sage: list(JonesDatabase().unramified_outside([3], 3))
[Number Field in a with defining polynomial x^3 - 3*x + 1,
 Number Field in a with defining polynomial x^3 - 3]
```



---

Comment by cremona created at 2020-10-08 16:28:34

I know nothing about the bug, and have never installed the optional Jones-Roberts database.  I only posted here to answer the question about whether that database still exists.  It does, and is being maintained, as it can do some things not yet available in the LMFDB though John Jones also maintains the number field collection there.

It seems that you haves tested that the package database_jones_numfield does work, and I am also now installing it....done, and I see no problem.

Let's close this issue.


---

Comment by kcrisman created at 2020-10-08 16:35:57

Did you try the `RationalField()` before and after using it like in comment:15?  I agree that we can close it if that succeeds.  I only assumed you knew something about it since you were already on this ticket.


---

Comment by cremona created at 2020-10-08 17:03:28

Replying to [comment:17 kcrisman]:
> Did you try the `RationalField()` before and after using it like in comment:15?  
yes
> I agree that we can close it if that succeeds.  I only assumed you knew something about it since you were already on this ticket.
I was on the ticket since (I think) William first caused the failure while doing somthing with elliptic curves, so he fingered me.  I then pointed out that the failure had nothing to do with elliptic curves!

```
sage: RationalField()
Rational Field
sage: from sage.env import SAGE_SHARE
sage: x = load(os.path.join(SAGE_SHARE, 'jones', 'jones.sobj'))
sage: RationalField()
Rational Field
sage: list(JonesDatabase().unramified_outside([3], 3))
[Number Field in a with defining polynomial x^3 - 3*x + 1,
 Number Field in a with defining polynomial x^3 - 3]
sage: RationalField()
Rational Field
```



---

Comment by kcrisman created at 2020-10-08 17:13:35

Changing status from new to needs_review.


---

Comment by kcrisman created at 2020-10-08 17:13:43

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2020-10-08 17:14:02

If there is still a bug, at any rate we didn't find it :-)


---

Comment by chapoton created at 2020-10-08 18:23:28

Resolution: invalid
