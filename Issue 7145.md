# Issue 7145: [with patch, needs review] Interval exchange transformations

Issue created by migration from https://trac.sagemath.org/ticket/7145

Original creator: vdelecroix

Original creation time: 2009-10-07 11:48:19

Assignee: somebody

CC:  slabbe

This module implement Interval exchange transformations (iet) (and linear involutions (li)) from a combinatorial point of vue. It also makes the link with strata of Abelian differentials on Riemann surfaces. The three main objects defined in this module are:

  - Special kinds of permutations
  - Rauzy diagrams (oriented graph)
  - Strata of differentials

There are different class of permuttations associated to iet, but all are constructed within a class factory:


```
sage: p = PermutationIET('a b c d','d c b a')
sage: p
a b c d
d c b a
sage: p.stratum()
H(2)
```


The object which links those permutations to the dynamic of strata of differentials is the Rauzy diagram:


```
sage: p = PermutationIET('a b c','c b a')
sage: d = p.rauzy_diagram()
Rauzy diagram with 3 permutations
```



---

Attachment


---

Comment by vdelecroix created at 2009-10-07 12:15:27

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2009-10-11 20:45:01

Changing assignee from somebody to vdelecroix.


---

Comment by slabbe created at 2009-12-08 16:30:33

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2009-12-08 16:30:33

First I must say that I am not expert at all in that field. I just know some of Interval exchange transformations. So, Vincent, I read through your patch today and I will post some small corrections in a patch soon. I have also some comments (sometimes suggestions open to you) below :

I would gather those related functionalities under a same bag where the user could found them (and all of them) more easily. For example.


```
sage: IET.[TAB]
```


or maybe


```
sage: from sage.combinat.iet.all import IET
sage: IET.[TAB]
```


For `constructor.py`, I suggest to 

- Create a class `constructor` containing the functions `PermutationsIET`, `PermutationIET`, `PermutationLI`, `GeneralizedPermutation`, `RauzyDiagram`, `IntervalExchangeTransformation`.
- Create the object `IET = constructor()`
- Rename `PermutationsIET` to `PermutationsIET_iterator`
- Add a function named `IntervalExchangeTransformation` to the class `constructor` that wrapped the constructor of `IET` in `iet.py`.
- Do we want `AbelianStratum`, `QuadraticStratum` and `AbelianStrata` to be wrapped in `constructor` as well? I don't know, but if it is realated to everything in iet folder, then it would clearly help the user to know about it.

For `iet.py`

- Rename `IntervalExchangeTransformation.__mul__` to something like multiply_lengths.
- Keep `IntervalExchangeTransformation.__mul__` for multiplication of two IET.
- Change `IntervalExchangeTransformation._repr_` to look more like an IET and less as two tuples. For example it could say Interval exchange transformation from [0, 1[ to [0, 1[ of permutation ?.
- Rename `IntervalExchangeTransformation.copy` as `__copy__` or `__deepcopy__` if it corresponds to what you want. This may applies to many other classes in the files.

I would like the following to work :


```
sage: p = Permutation([3,2,1])
sage: t = IntervalExchangeTransformation(p, [0.6, 0.1, 0.3])
Traceback (most recent call last):
...
TypeError: cannot concatenate 'str' and 'int' objects
```


where labels of the intervals are facultative:


```
sage: t = IntervalExchangeTransformation(p, [0.6, 0.1, 0.3], labels='abc')
```



Why do the following doesn't work:


```
sage: p = Permutation([3,2,1])
sage: PermutationIET(p)
1 2 3
3 2 1
sage: PermutationIET([3,2,1])
Traceback (most recent call last):
...
ValueError: your argument can not be split in two parts
```


- I don't know if the numerous `_P_IET = PermutationIET` really help the readability. I would not rename them and rather keep them as they are. Or, if so, I would use `from this import longname as shortname` instead because if shortname is new to me, than I don't have to go in the file this to understand that shortname simply means longname.

For template.py :

I am getting the following :


```
sage -t  "devel/sage-combinat/sage/combinat/iet/template.py"
**********************************************************************
File "/home/slabbe/sage-4.2/devel/sage-combinat/sage/combinat/iet/template.py", line 1898:
    sage: g == loads(dumps(g))
Exception raised:
    Traceback (most recent call last):
      File "/home/slabbe/sage-4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/slabbe/sage-4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/slabbe/sage-4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_50[5]>", line 1, in <module>
        g == loads(dumps(g))###line 1898:
    sage: g == loads(dumps(g))
      File "sage_object.pyx", line 735, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8008)
      File "sage_object.pyx", line 165, in sage.structure.sage_object.SageObject.dumps (sage/structure/sage_object.c:2158)
    PicklingError: Can't pickle <class 'sage.combinat.iet.labeled.Path'>: attribute lookup sage.combinat.iet.labeled.Path failed
```



---

Comment by slabbe created at 2009-12-08 16:36:32

I submitted before preview. So I repeat below the lists that I messed up above.

For constructor.py, I suggest to

 - Create a class constructor containing the functions `PermutationsIET`, `PermutationIET`, `PermutationLI`, `GeneralizedPermutation`, `RauzyDiagram`, `IntervalExchangeTransformation`. 
 - Create the object `IET` = `constructor()` 
 - Rename `PermutationsIET` to `PermutationsIET_iterator` 
 - Add a function named `IntervalExchangeTransformation` to the class constructor that wrapped the constructor of IET in `iet.py`. 
 - Do we want `AbelianStratum`, `QuadraticStratum` and `AbelianStrata` to be wrapped in constructor as well? I don't know, but if it is realated to everything in iet folder, then it would clearly help the user to know about it.

For iet.py

 - Rename `IntervalExchangeTransformation.__mul__` to something like `multiply_lengths`. 
 - Keep `IntervalExchangeTransformation.__mul__` for multiplication of two IET. 
 - Change `IntervalExchangeTransformation._repr_` to look more like an `IET` and less as two tuples. For example it could say Interval exchange transformation from [0, 1[ to [0, 1[ of permutation ?. 
 - Rename `IntervalExchangeTransformation.copy` as `__copy__` or `__deepcopy__` if it corresponds to what you want. This may applies to many other classes in the files.


---

Comment by slabbe created at 2009-12-08 16:38:18

Applies over the precedent patch.


---

Attachment

Vincent, I tried your code again with Thierry Monteil who knows better this field and he liked all the functions you implemented.

He suggested that you change Permutation* to `LabelledPermutation` or `PermutationwithLabel`... up to you.

Also, I notice the following. I think it should be a method and not an attribute :


```
sage: p = Permutation([4,3,2,1])
sage: pp = PermutationIET(p)
sage: pp.alphabet
Ordered Alphabet [1, 2, 3, 4]
```



---

Comment by vdelecroix created at 2009-12-10 23:57:26

Replying to [comment:5 slabbe]:
> Vincent, I tried your code again with Thierry Monteil who knows better this field and he liked all the functions you implemented.
> 
> He suggested that you change Permutation* to `LabelledPermutation` or `PermutationwithLabel`... up to you.

It won't be possible. I consider two kinds of permutations
  * ReducedPermutation
  * LabelledPermutation

A ReducedPermutation can be identified with a permutation of an ordered alphabet.
A Labeledpermutation is a couple of bijection (p_t,p_b) : alphabet -> [1,n]
 
> Also, I notice the following. I think it should be a method and not an attribute :
> 
> {{{
> sage: p = Permutation([4,3,2,1])
> sage: pp = PermutationIET(p)
> sage: pp.alphabet
> Ordered Alphabet [1, 2, 3, 4]
> }}}

The resason is because it's possible to change the alphabet
sage: p = PermutationIET('a b c','c b a')
sage: p
a b c
c b a
sage: p.alphabet = [1,2,3]
sage: p
1 2 3
3 2 1
sage: p.alphabet = 'cd'
...
ValueError: Your alphabet has not enough letters


---

Comment by vdelecroix created at 2009-12-13 13:47:00

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2009-12-13 13:47:00

>  - Create a class constructor containing the functions `PermutationsIET`, `PermutationIET`, `PermutationLI`, `GeneralizedPermutation`, `RauzyDiagram`, `IntervalExchangeTransformation`. 
>  - Create the object `IET` = `constructor()` 

done. Everything is in constructor.py which is imported as iet. Then the iet.<tab> gives the (approximately) the following list

   * Permutation
   * RauzyDiagram
   * IntervalExchangeTransformation

>  - Rename `PermutationsIET` to `PermutationsIET_iterator` 

done 

>  - Add a function named `IntervalExchangeTransformation` to the class constructor that wrapped the constructor of IET in `iet.py`. 

done

>  - Do we want `AbelianStratum`, `QuadraticStratum` and `AbelianStrata` to be wrapped in constructor as well? I don't know, but if it is realated to everything in iet folder, then it would clearly help the user to know about it.

I don't know... the strata here means strata of Abelian differentials on Riemann surfaces. The fact is we need them to understand precisely the structure of Rauzy diagram. It is hence related to Rauzy diagram but somewhat independent of the theory of interval exchange transformations.

> 
> For iet.py
> 
>  - Rename `IntervalExchangeTransformation.__mul__` to something like `multiply_lengths`. 

done. In fact, it's implemented in .normalize()

>  - Keep `IntervalExchangeTransformation.__mul__` for multiplication of two IET. 

done. But a little todo remains. I choose to create canonic labels from the labels of the two iets and this force a conversion of labels to strings. It's not so beautiful if we do not need the labels.

>  - Change `IntervalExchangeTransformation._repr_` to look more like an `IET` and less as two tuples. For example it could say Interval exchange transformation from [0, 1[ to [0, 1[ of permutation ?. 

done.

>  - Rename `IntervalExchangeTransformation.copy` as `__copy__` or `__deepcopy__` if it corresponds to what you want. This may applies to many other classes in the files. 

done.


---

Attachment


---

Comment by slabbe created at 2009-12-24 12:54:22

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2009-12-24 12:54:22

Dear Vincent,

Thanks for doing all those changes.

I am now looking at your recent patch and I have a few more comments. I am sorry I was not able to tell them before. I will try now to make a complete review with all my (hopefully) final remarks. After those FIVE remarks answered, I think we will be very near of a positive review!

Sébastien

ONE.

> The resason is because it's possible to change the alphabet 
> sage: p = PermutationIET('a b c','c b a') 
> sage: p a b c c b a 
> sage: p.alphabet = [1,2,3] 
> sage: p 1 2 3 3 2 1 
> sage: p.alphabet = 'cd' 
> ... 
> ValueError?: Your alphabet has not enough letters 

I am not sure this is a good reason for using an attribute instead of a method. See the following example :


```
sage: g = Graph()
sage: p = g.plot()
sage: p.xmin()
-1.0
sage: p.xmin(-2)
sage: p.xmin()
-2.0
```


TWO.

The documentation and doctest coverage is very good (96%) but not perfect :


```
slabbe@pol:~/sage-4.2/devel/sage-combinat/sage/combinat/iet$ sage -coverage .
constructors.py: 75% (6 of 8)
iet.py: 100% (23 of 23)
labelled.py: 95% (57 of 60)
reduced.py: 100% (55 of 55)
strata.py: 100% (39 of 39)
template.py: 96% (89 of 92)

Overall weighted coverage score:  96.9%
Total number of functions:  277
We need    5 more function to get to 99% coverage.
```


Moreover, `sage -coverage *` tells many `function name doesn't occur in doctests`. Maybe you could add `#indirect doctest` in doctests that are indirect.

While you are at it, you may consider to add some INPUT and OUTPUT where there are missing. See the discussion [sage-devel: input and output in docstrings](http://groups.google.com/group/sage-devel/browse_thread/thread/7d529c646c685877/3f7678e55f60759f?hl=en&lnk=gst&q=coverage#3f7678e55f60759f)

THREE.

I am getting 2 doctests failures :


```
sage -t  "devel/sage-combinat/sage/combinat/iet/constructors.py"
**********************************************************************
File "/home/slabbe/sage-4.2/devel/sage-combinat/sage/combinat/iet/constructors.py", line 531:
    sage: for p in P: print p, "* *\n"
Expected:
    a b
    b a
    * *
Got:
    a b
    b a * *
    <BLANKLINE>
    b a
    a b * *
    <BLANKLINE>
**********************************************************************
File "/home/slabbe/sage-4.2/devel/sage-combinat/sage/combinat/iet/constructors.py", line 536:
    sage: for p in P: print p, "\* * *\n"
Expected:
    a b c
    c b a
    * * *
Got:
    a b c
    b c a \* * *
    <BLANKLINE>
    a b c
    c a b \* * *
    <BLANKLINE>
    a b c
    c b a \* * *
    <BLANKLINE>
    a c b
    b a c \* * *
    <BLANKLINE>
    a c b
    b c a \* * *
    <BLANKLINE>
    a c b
    c b a \* * *
    <BLANKLINE>
    b a c
    a c b \* * *
    <BLANKLINE>
    b a c
    c a b \* * *
    <BLANKLINE>
    b a c
    c b a \* * *
    <BLANKLINE>
    b c a
    a b c \* * *
    <BLANKLINE>
    b c a
    a c b \* * *
    <BLANKLINE>
    b c a
    c a b \* * *
    <BLANKLINE>
    c a b
    a b c \* * *
    <BLANKLINE>
    c a b
    b a c \* * *
    <BLANKLINE>
    c a b
    b c a \* * *
    <BLANKLINE>
    c b a
    a b c \* * *
    <BLANKLINE>
    c b a
    a c b \* * *
    <BLANKLINE>
    c b a
    b a c \* * *
    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of   6 in __main__.example_4
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/slabbe/.sage//tmp/.doctest_constructors.py
	 [3.0 s]
exit code: 1024
```


FOUR.

I use sage-4.2 and I have problem to docbuild a branch of sage. It docbuilds the sage main branch, so I am not able to test if there are no Sphinx warnings and if everythings looks good on the html doc. I am waiting sage-4.3 to come out to test your patch on it and see the doc.

FIVE.

I changed a little bit the `_repr_` of Interval exchange transformation. See the patch attached. Hope you agree.


---

Attachment

Applies over the precedent 3 patches.


---

Comment by vdelecroix created at 2009-12-29 10:55:30

Replying to [comment:8 slabbe]:
Dear Sebastien,

> 
> Thanks for doing all those changes.
>

Thanks for this nice review ! It will be a *very* good patch.

> ONE.
> 
> > The resason is because it's possible to change the alphabet 
> > sage: p = PermutationIET('a b c','c b a') 
> > sage: p a b c c b a 
> > sage: p.alphabet = [1,2,3] 
> > sage: p 1 2 3 3 2 1 
> > sage: p.alphabet = 'cd' 
> > ... 
> > ValueError?: Your alphabet has not enough letters 
> 
> I am not sure this is a good reason for using an attribute instead of a method. See the following example :
> 
> {{{
> sage: g = Graph()
> sage: p = g.plot()
> sage: p.xmin()
> -1.0
> sage: p.xmin(-2)
> sage: p.xmin()
> -2.0
> }}}

It works now as

```
sage: p = iet.Permutation('a b c','c b a')
sage: print p
a b c
c b a
sage: p.alphabet([1,2,3])
sage: print p
1 2 3
3 2 1
```


 
> TWO.
> 
> The documentation and doctest coverage is very good (96%) but not perfect :
>

up to 100% now
 
> While you are at it, you may consider to add some INPUT and OUTPUT where there are missing. See the discussion [sage-devel: input and output in docstrings](http://groups.google.com/group/sage-devel/browse_thread/thread/7d529c646c685877/3f7678e55f60759f?hl=en&lnk=gst&q=coverage#3f7678e55f60759f)

lot of INPUT/OUTPUT added
 
> THREE.
> 
> I am getting 2 doctests failures :
> 

corrected
 
> 
> FIVE.
> 
> I changed a little bit the `_repr_` of Interval exchange transformation. See the patch attached. Hope you agree.
> 

I realy agree. In France, we use the coma instead of points to distinguish the integer part and the decimal that why we use dot comman for intervals... I keep it for the french translation ;-)


---

Comment by vdelecroix created at 2009-12-29 10:55:30

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2009-12-29 10:56:06

Applies over the 4 precedings


---

Attachment

Great. Point ONE above was addressed. The documentation coverage is now 100% perfect. All tests passed. 

I builded the documentation and there was several sphinx issues. I corrected them in a patch that I will upload shortly.


---

Attachment

Applies over all the precedent patches.


---

Comment by slabbe created at 2010-01-06 15:43:23

Vincent, can you review my last patch and make sure everything is OK with the sphinx output? My patch solved some sphinx syntax, but I feel like more improvements could be done.


---

Comment by vdelecroix created at 2010-01-08 00:00:56

Hi,

> Vincent, can you review my last patch and make sure everything is OK with the sphinx output? My patch solved some sphinx syntax, but I feel like more improvements could be done.

I'm not sure about what you did with the OUTPUT part of the documentation string. It does not correspond to what is written in the "developer's guide"


```
OUTPUT:

    integer -- the ...
```


What do I do for this ?

I will make a complete review of the documentation after the answer.


---

Comment by slabbe created at 2010-01-08 15:06:54

> I'm not sure about what you did with the OUTPUT part of the documentation string. It does not correspond to what is written in the "developer's guide"

My fault. In fact, I should update the way I write the OUTPUT part. I will take a closer look to the developer's guide. Feel free to change those.


---

Comment by vdelecroix created at 2010-01-09 18:56:37

I made a complete review of the doc. There is no warning when building the documentation and there is INPUT and OUTPUT fields where there are needed.

I replace your patch trac_7145-review3-sl.patch with my trac-7145-documentation-review-vd.patch (because I find it more natural to erase the OUTPUT field modification than modify it back).

I also made little modifications on default argument on some method (.flips() and .list() of FlippedPermutation) and a change of name (.rauzy_1n() becomes .cylindric()). The latter is due to a forthcoming paper.


---

Attachment

applies over (trac_7145-iet-vd.patch, trac_7145-review-sl.patch, trac_7145-corrections-vd.patch, trac_7145-review2-sl ,trac_7145-corrections2-vd.patch)


---

Attachment

applies over (trac_7145-iet-vd.patch, trac_7145-review-sl.patch, trac_7145-corrections-vd.patch, trac_7145-review2-sl ,trac_7145-corrections2-vd.patch)


---

Attachment

Apply only this one.


---

Comment by slabbe created at 2010-01-13 17:59:23

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-01-13 17:59:23

I folded the relevant patches together : trac_7145-iet-final.patch .

Positive review.


---

Comment by slabbe created at 2010-01-13 18:01:03

> Positive review.

I just want to add that I tested it on a fresh Sage-4.3.


---

Comment by rlm created at 2010-01-14 07:01:05

Resolution: fixed
