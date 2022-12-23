# Issue 2577: improving diagonal_matrix and vector (iterable) input

Issue created by migration from https://trac.sagemath.org/ticket/2577

Original creator: ncalexan

Original creation time: 2008-03-17 23:16:47

Assignee: was

CC:  ncalexan

Keywords: diagonal_matrix vector iterable

I don't like either of these behaviours -- why can't any old iterable thing go into diagonal_matrix?


```
sage: x = ZZ['x'].gen()
sage: temp = NumberField(x^4 + x^3 + x^2 + x + 1, 'a')
sage: diagonal_matrix(vector(1, 2))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/Documents/School/MATH235/genus2cm/free_module_element.pyx in sage.modules.free_module_element.vector()

/Users/ncalexan/Documents/School/MATH235/genus2cm/free_module_element.pyx in sage.modules.free_module_element.prepare()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/structure/sequence.py in __init__(self, x, universe, check, immutable, cr, cr_str)
    201                  immutable=False, cr=False, cr_str=None):
    202         if not isinstance(x, (list, tuple)):
--> 203             x = list(x)
    204             #raise TypeError, "x must be a list or tuple"
    205         self.__hash = None

<type 'exceptions.TypeError'>: 'sage.rings.integer.Integer' object is not iterable
sage: diagonal_matrix(vector(temp(1), temp(2)))
---------------------------------------------------------------------------
<type 'exceptions.UnboundLocalError'>     Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/matrix/constructor.py in diagonal_matrix(arg0, arg1, arg2, sparse)
    565             v = arg2
    566             
--> 567     if isinstance(v, list):
    568         w = {}
    569         for i in range(len(v)):

<type 'exceptions.UnboundLocalError'>: local variable 'v' referenced before assignment
```



---

Comment by dfdeshom created at 2008-03-18 15:48:29

Just to be clear: we are talking about 2 bugs here.
 * Vectors don't accept simple integers. Ie, `vector(1,2,3,4)` is not currently allowed. This annoys me too. I'll try to tackle it later.
 * For `diagonal_matrix`, only list and tuples are currently accepted. Vectors and matrices aren't (I checked). I'm currently working on this.


---

Comment by dfdeshom created at 2008-03-18 16:14:42

Replying to [comment:1 dfdeshom]:
>  * For `diagonal_matrix`, only list and tuples are currently accepted. Vectors and matrices aren't (I checked). I'm currently working on this.
> 

I'm not sure we should accept matrices, since you can get teh job done with `bloc_diagonal_matrix` or `block_matrix`.


---

Comment by dfdeshom created at 2008-03-19 00:39:32

I've added a patch that makes diagonal_matrix accept most iterable objects.


---

Comment by dfdeshom created at 2008-03-20 17:32:26

I've added another patch (2577-2.patch) that makes this possible for vectors:

```
sage: vector(1,2,2.0)
(1.00000000000000, 2.00000000000000, 2.00000000000000)
sage: v=vector(1,2,2.0,RDF(32),23/3); v
(1.00000000000000, 2.00000000000000, 2.00000000000000, 32.0000000000000, 7.66666666\
666667)

sage: v = vector([1,2,3/5]); v
(1, 2, 3/5)
sage: w = vector(1,2,3/5) ; w == v
True
```


I'm treating 1) and 2) as 2 separate issues, so apply each patch one at a time. Feel free to open another ticket for either patch.


---

Comment by dfdeshom created at 2008-03-20 17:32:26

Changing assignee from was to dfdeshom.


---

Comment by jason created at 2008-04-09 03:13:23

Comments on 2577-1.patch (line numbers are the new line numbers): how come in line 579, you call `len(list(v)) `, but in lines 589 and 597, you left it at `len(v)`.  Do the latter two calls (and whatever other calls there are) need to be changed to len(list(v))?


2577-2.patch: The "python" way to get a keyword value if set, but a default if not set, is the following:


```
sparse=kwds.get('sparse', None)
```


See http://docs.python.org/lib/typesmapping.html


---

Comment by jason created at 2008-04-09 03:14:48

BTW, +1 to the functionality enhancement proposed.  I keep getting annoyed that I can't do vector(1,2,3) too!


---

Attachment


---

Comment by dfdeshom created at 2008-04-10 15:33:34

Replying to [comment:5 jason]:
> Comments on 2577-1.patch (line numbers are the new line numbers): how come in line 579, you call `len(list(v)) `, but in lines 589 and 597, you left it at `len(v)`.  Do the latter two calls (and whatever other calls there are) need to be changed to len(list(v))?
> 
> 
> 2577-2.patch: The "python" way to get a keyword value if set, but a default if not set, is the following:
> 
> {{{
> sparse=kwds.get('sparse', None)
> }}}
> 
> See http://docs.python.org/lib/typesmapping.html
> 

Thanks for the reviews. I've made the necessary changes to both patches. I've also added a way to construct a diagonal matrix from a matrix in 2577-1.patch


---

Comment by craigcitro created at 2008-06-15 21:57:06

Changing keywords from "diagonal_matrix vector iterable" to "diagonal_matrix vector iterable, editor_mhansen".


---

Comment by cremona created at 2008-08-10 13:20:57

What is the relation between this patch and the one for #2577?


---

Comment by dfdeshom created at 2008-08-10 14:02:19

Replying to [comment:9 cremona]:
> What is the relation between this patch and the one for #2577? 

Could you clariry your question? This *is* #2577.


---

Comment by cremona created at 2008-08-10 14:53:05

Replying to [comment:10 dfdeshom]:
> Replying to [comment:9 cremona]:
> > What is the relation between this patch and the one for #2577? 
> 
> Could you clariry your question? This *is* #2577.

Sorry, I meant #3704 which I reviewed recently, and seems to do the same kind of thing.  If that patch does what this one does, then this one can be marked "duplicate", perhaps.  But it would be best of you could look at both to make sure we get the best of both.


---

Comment by jason created at 2008-08-15 23:18:58

I'm comparing 2577-1.patch and the patch up at #3704.  I like the patch at #3704 better.  Here are the reasons:

1. Much simpler function (it's not broken into cases, but instead passes off all the hard work to the matrix() constructor, which also makes it more consistent with the matrix() constructor).

2. With the patch here, it looks like you still have the problem noted in the comments of #3704 of iterable objects giving weird answers, like a factored polynomial putting a factor in each element.  In #3704, I finally decided on just making it do this iterable thing (putting the elements down the diagonal) if the passed object was a list (or Sequence), tuple, or vector.  For all other cases, I think it is clearer to just say `diagonal_matrix(list(myobject))` or `diagonal_matrix(myobject.list())`.

3. I honestly can't think of a reason why diagonal_matrix(matrix) would want to take the entries and put them down the diagonal.

4. When I apply the patch here and do `diagonal_matrix(x^3+3, x+1)`, I get an error:

```
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/home/jason/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.5/site-packages/sage/matrix/constructor.py in diagonal_matrix(*args, **kwds)
    769             v = arg2
    770 
--> 771     if  hasattr(v, '_matrix_'):
    772         # Format 5
    773         v = v.list()

UnboundLocalError: local variable 'v' referenced before assignment
```


So I vote to take the patch 2577-2.patch here and the patch at #3704 and leave the 2577-1.patch.  I'd feel more comfortable if someone (preferably dfdeshom) expressed an opinion, though, since I wrote the patch over at #3704.


---

Comment by jason created at 2008-08-15 23:20:57

I should also say that I forgot that dfdeshom had already done the work here on diagonal_matrix when I wrote the patch at #3704; if I had not forgotten, I would have not duplicated the work.


---

Comment by jason created at 2008-08-15 23:57:02

After playing around with 2577-2.patch, I have some concerns:

1. I don't like arbitrarily getting the items of any iterable object.  There are many, many objects that are iterable in ways that don't make sense for vector().  For example:


```
sage: x=polygen(QQ)
sage: vector(x^2-1)
(-1, 0, 1)
sage: vector(x^2-1, x)
(-1, 0, 1)
sage: vector(x^2-1, x,x)
(x^2 - 1, x, x)
```


I would much rather that vector() *only* try to get the items in an iterable object if the object was a list, tuple, or another vector.  Otherwise you have funny things like the above happening.


---

Comment by mabshoff created at 2008-09-02 13:13:31

Sorry Didier,

this is "wontfix" since we will be merging #3704.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-02 13:13:31

Resolution: fixed
