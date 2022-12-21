# Issue 6245: make a custom infix operator decorator

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-06-08 11:46:12

Assignee: cwitty

CC:  cwitty hivert mhansen kcrisman

It would be nice to incorporate the code developed in http://groups.google.com/group/sage-devel/browse_thread/thread/100de89e7d402134/fe89570b403344ae (and in the same spirit as the backslash operator).  An example of the final developed code is at http://sagenb.org/home/pub/565.


---

Comment by jason created at 2009-06-08 11:48:34

For reference, the code is:


```
class infix_operator:
    def __init__(self, function, left=None, right=None):
        self.function = function
        self.left = left
        self.right = right

    def __rmul__(self, left):
        if self.right is None:
            if self.left is None:
                return infix_operator(self.function, left=left)
            else:
                raise SyntaxError, "Infix operator already has its left argument"
        else:
            return self.function(left, self.right)

    def __mul__(self, right):
        if self.left is None:
            if self.right is None:
                return infix_operator(self.function, right=right)
            else:
                raise SyntaxError, "Infix operator already has its right argument"
        else:
            return self.function(self.left, right) 
        	
```


And several examples (doctests?) are:


```
# This emul operator returns the element-wise product of two lists...
`@`infix_operator
def emul(a,b):
    return [i*j for i,j in zip(a,b)] 
        	
a=[1,2,3]
b=[3,4,5]

# Returns [3,8,15]
a *emul* b 
        	
`@`infix_operator
def hadamard_product(a, b):
   if a.nrows()!=b.nrows() or a.ncols()!=b.ncols():
       raise ValueError, "Matrices must have the same dimensions in a Hadamard product"
   return matrix(a.nrows(), a.ncols(), [x*y for x, y in zip(a.list(), b.list())]) 
        	
A=random_matrix(ZZ,3)
B=random_matrix(ZZ,3)
A *hadamard_product* B 
```



---

Comment by jason created at 2009-09-16 06:01:45

The patch is an initial go at this.  The documentation for the function needs to change (it still is just the same docs as the code I followed in plot/misc.py).

Here are some examples:


```
sage: from sage.misc.misc import infix_operator
sage: # A post-fix operator
sage: `@`infix_operator('or')
sage: def pipe(a,b):
...       return b(a)
...
sage: print (x |pipe| cos)
sage: print pi |pipe| n
sage: print pi |pipe| n |pipe| cos
cos(x)
3.14159265358979
-1.00000000000000
sage: # an infix dot product
sage: `@`infix_operator('multiply')
sage: def dot(a,b):
...       return a.dot_product(b)
...       
...
sage: vector([1,2]) *dot* vector([2,4])
10
sage: # an infix sum
sage: `@`infix_operator('add')
sage: def esum(a,b):
...       return [i+j for i,j in zip(a,b)]
...
sage: [1,2,4] +esum+ [3,-1,2]
[4, 1, 6]
```



---

Comment by jason created at 2009-09-16 06:02:45

CCing mhansen, since he probably has very enlightening things to say about how I dealt with the decorators :).


---

Comment by jason created at 2009-09-17 05:53:31

I cleaned up the code a bit and made much better documentation.


---

Comment by kcrisman created at 2009-09-17 13:46:46

I have no comment on the technical side, but wonder - are you limiting "object" to be or, add, or multiply?  What if someone wanted to create an infix for, say, factorial - would they have to change this code?


---

Comment by jason created at 2009-09-17 16:38:03

Replying to [comment:7 kcrisman]:
> I have no comment on the technical side, but wonder - are you limiting "object" to be or, add, or multiply?  What if someone wanted to create an infix for, say, factorial - would they have to change this code?


I only chose a few precedence levels (that's really the issue here).  There's no reason we couldn't put all of the special functions in (like subtract, for example).


---

Comment by rossk created at 2010-02-12 11:45:41

Applied patch to 4.3.2


(Cool functionality - Can review quickly once this is addressed) 

```
applying trac-6245-infix-decorator.patch
patching file sage/misc/misc.py
Hunk #1 FAILED at 2219
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/misc.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-6245-infix-decorator.patch
```



---

Comment by jason created at 2010-04-15 03:50:10

rebased


---

Attachment

I rebased the patch to Sage 4.3.4.  Can you look at it again?


---

Comment by rossk created at 2010-04-15 23:07:49

Replying to [comment:10 jason]:
> I rebased the patch to Sage 4.3.4.  Can you look at it again?

Will aim to look at this later today


---

Comment by rossk created at 2010-04-18 08:47:45

Can confirm all examples work as indicated and all tests passed for me

```
sage: def dot(a,b):
sage:     return a.dot_product(b)
sage: dot=infix_operator('multiply')(dot)
sage: u=vector([1,2,3])
sage: v=vector([5,4,3])
sage: u *dot* v

22

# Also these examples here show precedence works as 
#   expected (i.e. * before +)
#
sage: def eadd(a,b): 
sage:     return a.parent([i+j for i,j in zip(a,b)])
sage: 
sage: eadd=infix_operator('add')(eadd)
sage: u=vector([1,2,3])
sage: v=vector([5,4,3])
sage: print u +eadd+ v
sage: print 2*u +eadd+ v
sage: print v +eadd+ 2*u 
sage: print v +eadd+ u*2 
sage: print (v +eadd+ u)*2  	

(6, 6, 6)
(7, 8, 9)
(7, 8, 9)
(7, 8, 9)
(12, 12, 12)

# Last example: function composition not commutative as expected
sage: def thendo(a,b): return b(a)
sage: thendo=infix_operator('or')(thendo)
sage: print x |thendo| cos |thendo| (lambda x: x^2)
sage: print x |thendo| (lambda x: x^2) |thendo| cos 

cos(x)^2
cos(x^2)
```



---

Comment by rossk created at 2010-04-18 11:27:22

Noticed references to `__rmul__` in the code so I thought I might try setting up a situation


where `__mul__` fails so `__rmul__` would be exercised. In setting up the test code, I got an


error but cant see whats wrong (any thoughts?)

```
class Fraction:
  def __init__(self, numerator, denominator=1):
    self.numerator = numerator
    self.denominator = denominator
  def __str__(self):
    return "%d/%d" % (self.numerator, self.denominator)
  def zmul(self, other):
    return Fraction(self.numerator*other.numerator,
                  self.denominator*other.denominator)
  def zrmul(self, other):
    return Fraction(other*self.numerator,
                  self.denominator)
  def __mul__(self, other):
    return Fraction(self.numerator*other.numerator,
                  self.denominator*other.denominator)
  def __rmul__(self, other):
    return Fraction(other*self.numerator,self.denominator)

# multiplication operator using methods
print Fraction(2,3).zmul(Fraction(5,4))
```

10/12

```
# multiplication infix operator
def dot(a,b):
  return a.zmul(b)
dot = infix_operator('multiply')(dot)
print Fraction(2,3) *dot* Fraction(5,4)
```

crashes with 

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_59.py", line 9, in <module>
    open("___code___.py","w").write("# -*- coding: utf-8 -*-\n" + _support_.preparse_worksheet_cell(base64.b64decode("Z...<abbreviated>...Y="),globals())+"\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpIR_EGe/___code___.py", line 8, in <module>
    u *dot* v
  File "", line 1, in <module>
    
  File "", line 13, in __mul__
    
AttributeError: dot instance has no attribute 'numerator'
```



---

Comment by jason created at 2010-04-20 04:02:00

Replying to [comment:14 rossk]:
> Noticed references to `__rmul__` in the code so I thought I might try setting up a situation

> 
> where `__mul__` fails so `__rmul__` would be exercised. In setting up the test code, I got an

> 
> error but cant see whats wrong (any thoughts?)


The problem is that your __mul__ function does not check its arguments.  Note that:


```
sage: Fraction(2,3)*matrix(2,1,[1,2])
Traceback (click to the left of this block for traceback)
...
AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'
object has no attribute 'numerator'
```


Instead, you should check your arguments in the __mul__ function before blindly calling the .numerator method, or at least you should catch the error, like this:


```
class Fraction:
  def __init__(self, numerator, denominator=1):
    self.numerator = numerator
    self.denominator = denominator
  def __str__(self):
    return "Fraction(%d,%d)" % (self.numerator, self.denominator)
  __repr__=__str__
  def zmul(self, other):
    return Fraction(self.numerator*other.numerator,
                  self.denominator*other.denominator)
  def __mul__(self, other):
    try:
        return Fraction(self.numerator*other.numerator,
                  self.denominator*other.denominator)
    except:
        return NotImplemented

```



---

Comment by rossk created at 2010-04-20 13:44:13

Thanks Jason - I appreciate what your code is doing a bit more now and see where I erred - thanks for the explanation. I would think these are enough tests to update this to a positive review. 
 

```
class Fraction:
  def __init__(self, numerator, denominator=1):
    self.numerator = numerator
    self.denominator = denominator
  def __str__(self):
    return "Fraction(%d,%d)" % (self.numerator, self.denominator)
  __repr__=__str__
  def zmul(self, other):
    return Fraction(self.numerator*other.numerator,
                  self.denominator*other.denominator)
  def __mul__(self, other):
    try:
        return Fraction(self.numerator*other.numerator,
                  self.denominator*other.denominator)
    except:
        return NotImplemented
  def __rmul__(self, other):
    try:
      return Fraction(other*self.numerator,self.denominator)
    except:
        return NotImplemented
    
def dot(a,b): 
    return a*b
dot = infix_operator('multiply')(dot)

u = Fraction(2,3)
v = Fraction(5,4)
print u *dot* v
print 3 *dot* v
```



---

Comment by rossk created at 2010-04-20 13:44:13

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-23 17:11:37

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:11:37

Merged into 4.4.alpha2.
