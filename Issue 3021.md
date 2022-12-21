# Issue 3021: add curl and divergence functions to symbolic vectors

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-25 12:17:10

Assignee: was

CC:  eviatarbach

Make curl work if the vector has 2 or 3 components.  Is there a higher-dimensional analogue for curl?


---

Comment by jason created at 2008-04-25 15:42:43

(After some discussion on IRC) It seems that Sage is really lacking in the differential geometry area.  If some good work is done there, this request will likely automatically be satisfied.

A short term solution would be to write a vector field class.


---

Comment by ncalexan created at 2009-06-14 21:03:52


```
# a possible implementation of div, for irc user hedgehog

var('x, y, z')
(x, y, z)
f1 = x^2 + 2*y; f2 = x^3 + sin(z); f3 = y*z + 2
F = vector([f1, f2, f3])

print F(x=0, y=2, z=3)

def _variables(F):
    # this is a little funky -- we're finding all the variables that occur
    # in the components of F, and somehow choosing an ordering.  There are
    # other (better ways) but I'm not sure what the correct interface is.
    # For now, the user can specify the variables if they choose, just
    # like the gradient method.
    variables = list(set(flatten([ list(f.variables()) for f in F ])))
    variables.sort()
    return variables

def div(F, variables=None):
    assert len(F) == 3
    if variables is None:
        variables = _variables(F)

    s = 0
    for i in range(len(F)):
        s += F[i].derivative(variables[i])
    return s

print F
print div(F)
print div(F, variables=(y, x, z))

def curl(F, variables=None):
    assert len(F) == 3
    if variables is None:
        variables = _variables(F)
    assert len(variables) == 3
    x, y, z = variables
    Fx, Fy, Fz = F
    i = Fz.derivative(y) - Fy.derivative(z)
    j = Fz.derivative(z) - Fx.derivative(x)
    k = Fy.derivative(x) - Fz.derivative(y)
    return vector([i, j, k])
    
print curl(F)
print curl(F, variables=(y, x, z))

# let's assert that div(curl) == 0
# we need the variables because the ordering is suspect otherwise: for me,
# sage: _variables(F)
# [x, y, z]
# sage: _variables(curl(F))
# [z, x, y]
assert div(curl(F, variables=(x, y, z)), variables=(x, y, z)) == 0
```



---

Comment by jason created at 2010-05-11 18:15:51

See #5506 for a collection of things to add to a symbolic vectors class


---

Comment by robertwb created at 2010-05-11 18:20:10

There is a 7-dim curl. Why doesn't the generic vector one work?


---

Comment by jason created at 2010-05-11 18:33:06

What generic curl (I don't think it's in Sage right now)?  Or are you saying we should just add curl to generic vectors?  I agree; no reason to add this to just the callable symbolic vectors class (what was I thinking?).


---

Comment by ddrake created at 2011-07-28 20:12:07

Note that in the code above, it should be:

```
k = Fy.derivative(x) - Fx.derivative(y)
```


The "`Fz`" should be "`Fx`".


---

Comment by robert.marik created at 2012-02-19 14:06:17

Also

```
 j = Fx.derivative(z) - Fz.derivative(x)
```



---

Comment by robertwb created at 2014-05-01 05:12:57

New commits:


---

Comment by robertwb created at 2014-05-01 05:12:57

Changing status from new to needs_review.


---

Comment by eviatarbach created at 2014-05-01 09:12:46

I was just going to work on this today!

I haven't tested the code, but looks good. Just a few things:

1. Is there any reason why you're converting the variables to their string representations in `._variables()`?
2. The parameter in `Expression.gradient` is called `variables`; I think it would be good to switch `vars` to `variables` for consistency.
3. I think there should be test(s) for `.curl()` with the variables parameter.
4. I believe the `raise TypeError, "curl only defined for 3 dimensions"` syntax is deprecated, and that the string should be passed as an argument.


---

Comment by slelievre created at 2014-05-01 12:34:13

Nitpicking on the error message in `div`: I would change it from `"variable list must be equal to the dimension of self"` to `"number of variables must equal dimension of self"`.

About point 4 in eviatarbach's comment:
- A reference for the change in exception raising syntax is [PEP-3109](http://legacy.python.org/dev/peps/pep-3109/).
-  the `ValueError` in `div` on follows the new syntax. By contrast, both the `TypeError` and `ValueError` in `curl` follow the old syntax.


---

Comment by slelievre created at 2014-05-01 14:08:49

More nitpicking:
- Use "Return" instead of "Returns" in docstrings, see [PEP 0257](http://legacy.python.org/dev/peps/pep-0257/):

    The docstring is a phrase ending in a period. It prescribes the
    function or method's effect as a command ("Do this", "Return that"),
    not as a description; e.g. don't write "Returns the pathname ...".

- Should there be a docstring and tests for the `_variables` function?
- In examples for `div`, remove extra space before `w` in `R.<x,y,z, w> = QQ[]`


---

Comment by eviatarbach created at 2014-05-01 19:08:26

Another thought:

The extracting of variables from each element and then sorting by name looks scary, and can give unexpected results (if your vector is `(x1, x10, x2)`, I believe you would get 3 for the divergence instead of 1 as you might expect, since `'10'` comes before `'2'` in the alphanumeric sort). Unless there's a better solution, I think we should have it so that the variables list has to always be given explicitly.


---

Comment by jason created at 2014-05-02 02:10:30

If your vectors are callable symbolic vectors, you should be able to get the list of arguments from the base ring (since you've already explicitly given an order to the variables):


```
sage: f(x,y,z)=(x*y,y*z,z^2)
sage: f
(x, y, z) |--> (x*y, y*z, z^2)
sage: type(f)
<class 'sage.modules.vector_callable_symbolic_dense.Vector_callable_symbolic_dense'>
sage: f.base_ring().arguments()
(x, y, z)
```



---

Comment by eviatarbach created at 2014-05-03 05:09:39

That's a great idea. I think we should have that for callable vectors.

For the record, Mathematica and Maple both have default coordinate systems, which is how they deal with this issue.


---

Comment by git created at 2014-06-18 03:56:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-06-20 07:05:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by robertwb created at 2014-06-20 07:07:48

I've addressed all the comments.


---

Comment by kcrisman created at 2014-08-27 15:41:26

I was going to look at this, but looks like Eviatar and Samuel are on top, so just think of this as a ping :)


---

Comment by robertwb created at 2014-10-22 06:43:55

Replying to [comment:24 kcrisman]:
> I was going to look at this, but looks like Eviatar and Samuel are on top, so just think of this as a ping :)

Feel free to look at this yourself :)


---

Comment by tscrim created at 2014-10-22 07:24:03

My 2 cents, I'd have curl also take 2-dim inputs and return a vector. It might also be a good idea for a way (likely another method) which takes a 2-dim input and return a scalar as a shorthand (a la Green's theorem).

+1 to getting these (fundamental) methods into Sage.


---

Comment by robertwb created at 2015-02-11 05:22:17

Are there any enhancements to this with-patch, 7-year-old ticket that simply can't be deferred 'till later so we can finally get this in?


---

Comment by tscrim created at 2015-02-11 15:09:42

I added the 2-dim input. If you're happy with my changes, then I think we can set this to a positive review.
----
New commits:


---

Comment by robertwb created at 2015-02-12 04:55:54

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-17 19:28:29

Resolution: fixed
