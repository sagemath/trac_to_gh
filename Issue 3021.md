# Issue 3021: add curl and divergence functions to symbolic vectors

archive/issues_003021.json:
```json
{
    "body": "Assignee: was\n\nCC:  eviatarbach\n\nMake curl work if the vector has 2 or 3 components.  Is there a higher-dimensional analogue for curl?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3021\n\n",
    "created_at": "2008-04-25T12:17:10Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "add curl and divergence functions to symbolic vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3021",
    "user": "jason"
}
```
Assignee: was

CC:  eviatarbach

Make curl work if the vector has 2 or 3 components.  Is there a higher-dimensional analogue for curl?

Issue created by migration from https://trac.sagemath.org/ticket/3021





---

archive/issue_comments_020765.json:
```json
{
    "body": "(After some discussion on IRC) It seems that Sage is really lacking in the differential geometry area.  If some good work is done there, this request will likely automatically be satisfied.\n\nA short term solution would be to write a vector field class.",
    "created_at": "2008-04-25T15:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20765",
    "user": "jason"
}
```

(After some discussion on IRC) It seems that Sage is really lacking in the differential geometry area.  If some good work is done there, this request will likely automatically be satisfied.

A short term solution would be to write a vector field class.



---

archive/issue_comments_020766.json:
```json
{
    "body": "\n```\n# a possible implementation of div, for irc user hedgehog\n\nvar('x, y, z')\n(x, y, z)\nf1 = x^2 + 2*y; f2 = x^3 + sin(z); f3 = y*z + 2\nF = vector([f1, f2, f3])\n\nprint F(x=0, y=2, z=3)\n\ndef _variables(F):\n    # this is a little funky -- we're finding all the variables that occur\n    # in the components of F, and somehow choosing an ordering.  There are\n    # other (better ways) but I'm not sure what the correct interface is.\n    # For now, the user can specify the variables if they choose, just\n    # like the gradient method.\n    variables = list(set(flatten([ list(f.variables()) for f in F ])))\n    variables.sort()\n    return variables\n\ndef div(F, variables=None):\n    assert len(F) == 3\n    if variables is None:\n        variables = _variables(F)\n\n    s = 0\n    for i in range(len(F)):\n        s += F[i].derivative(variables[i])\n    return s\n\nprint F\nprint div(F)\nprint div(F, variables=(y, x, z))\n\ndef curl(F, variables=None):\n    assert len(F) == 3\n    if variables is None:\n        variables = _variables(F)\n    assert len(variables) == 3\n    x, y, z = variables\n    Fx, Fy, Fz = F\n    i = Fz.derivative(y) - Fy.derivative(z)\n    j = Fz.derivative(z) - Fx.derivative(x)\n    k = Fy.derivative(x) - Fz.derivative(y)\n    return vector([i, j, k])\n    \nprint curl(F)\nprint curl(F, variables=(y, x, z))\n\n# let's assert that div(curl) == 0\n# we need the variables because the ordering is suspect otherwise: for me,\n# sage: _variables(F)\n# [x, y, z]\n# sage: _variables(curl(F))\n# [z, x, y]\nassert div(curl(F, variables=(x, y, z)), variables=(x, y, z)) == 0\n```\n",
    "created_at": "2009-06-14T21:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20766",
    "user": "ncalexan"
}
```


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

archive/issue_comments_020767.json:
```json
{
    "body": "See #5506 for a collection of things to add to a symbolic vectors class",
    "created_at": "2010-05-11T18:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20767",
    "user": "jason"
}
```

See #5506 for a collection of things to add to a symbolic vectors class



---

archive/issue_comments_020768.json:
```json
{
    "body": "There is a 7-dim curl. Why doesn't the generic vector one work?",
    "created_at": "2010-05-11T18:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20768",
    "user": "robertwb"
}
```

There is a 7-dim curl. Why doesn't the generic vector one work?



---

archive/issue_comments_020769.json:
```json
{
    "body": "What generic curl (I don't think it's in Sage right now)?  Or are you saying we should just add curl to generic vectors?  I agree; no reason to add this to just the callable symbolic vectors class (what was I thinking?).",
    "created_at": "2010-05-11T18:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20769",
    "user": "jason"
}
```

What generic curl (I don't think it's in Sage right now)?  Or are you saying we should just add curl to generic vectors?  I agree; no reason to add this to just the callable symbolic vectors class (what was I thinking?).



---

archive/issue_comments_020770.json:
```json
{
    "body": "Note that in the code above, it should be:\n\n```\nk = Fy.derivative(x) - Fx.derivative(y)\n```\n\n\nThe \"`Fz`\" should be \"`Fx`\".",
    "created_at": "2011-07-28T20:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20770",
    "user": "ddrake"
}
```

Note that in the code above, it should be:

```
k = Fy.derivative(x) - Fx.derivative(y)
```


The "`Fz`" should be "`Fx`".



---

archive/issue_comments_020771.json:
```json
{
    "body": "Also\n\n```\n j = Fx.derivative(z) - Fz.derivative(x)\n```\n",
    "created_at": "2012-02-19T14:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20771",
    "user": "robert.marik"
}
```

Also

```
 j = Fx.derivative(z) - Fz.derivative(x)
```




---

archive/issue_comments_020772.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-05-01T05:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20772",
    "user": "robertwb"
}
```

New commits:



---

archive/issue_comments_020773.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-01T05:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20773",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020774.json:
```json
{
    "body": "I was just going to work on this today!\n\nI haven't tested the code, but looks good. Just a few things:\n\n1. Is there any reason why you're converting the variables to their string representations in `._variables()`?\n2. The parameter in `Expression.gradient` is called `variables`; I think it would be good to switch `vars` to `variables` for consistency.\n3. I think there should be test(s) for `.curl()` with the variables parameter.\n4. I believe the `raise TypeError, \"curl only defined for 3 dimensions\"` syntax is deprecated, and that the string should be passed as an argument.",
    "created_at": "2014-05-01T09:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20774",
    "user": "eviatarbach"
}
```

I was just going to work on this today!

I haven't tested the code, but looks good. Just a few things:

1. Is there any reason why you're converting the variables to their string representations in `._variables()`?
2. The parameter in `Expression.gradient` is called `variables`; I think it would be good to switch `vars` to `variables` for consistency.
3. I think there should be test(s) for `.curl()` with the variables parameter.
4. I believe the `raise TypeError, "curl only defined for 3 dimensions"` syntax is deprecated, and that the string should be passed as an argument.



---

archive/issue_comments_020775.json:
```json
{
    "body": "Nitpicking on the error message in `div`: I would change it from `\"variable list must be equal to the dimension of self\"` to `\"number of variables must equal dimension of self\"`.\n\nAbout point 4 in eviatarbach's comment:\n- A reference for the change in exception raising syntax is [PEP-3109](http://legacy.python.org/dev/peps/pep-3109/).\n-  the `ValueError` in `div` on follows the new syntax. By contrast, both the `TypeError` and `ValueError` in `curl` follow the old syntax.",
    "created_at": "2014-05-01T12:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20775",
    "user": "slelievre"
}
```

Nitpicking on the error message in `div`: I would change it from `"variable list must be equal to the dimension of self"` to `"number of variables must equal dimension of self"`.

About point 4 in eviatarbach's comment:
- A reference for the change in exception raising syntax is [PEP-3109](http://legacy.python.org/dev/peps/pep-3109/).
-  the `ValueError` in `div` on follows the new syntax. By contrast, both the `TypeError` and `ValueError` in `curl` follow the old syntax.



---

archive/issue_comments_020776.json:
```json
{
    "body": "More nitpicking:\n- Use \"Return\" instead of \"Returns\" in docstrings, see [PEP 0257](http://legacy.python.org/dev/peps/pep-0257/):\n\n    The docstring is a phrase ending in a period. It prescribes the\n    function or method's effect as a command (\"Do this\", \"Return that\"),\n    not as a description; e.g. don't write \"Returns the pathname ...\".\n\n- Should there be a docstring and tests for the `_variables` function?\n- In examples for `div`, remove extra space before `w` in `R.<x,y,z, w> = QQ[]`",
    "created_at": "2014-05-01T14:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20776",
    "user": "slelievre"
}
```

More nitpicking:
- Use "Return" instead of "Returns" in docstrings, see [PEP 0257](http://legacy.python.org/dev/peps/pep-0257/):

    The docstring is a phrase ending in a period. It prescribes the
    function or method's effect as a command ("Do this", "Return that"),
    not as a description; e.g. don't write "Returns the pathname ...".

- Should there be a docstring and tests for the `_variables` function?
- In examples for `div`, remove extra space before `w` in `R.<x,y,z, w> = QQ[]`



---

archive/issue_comments_020777.json:
```json
{
    "body": "Another thought:\n\nThe extracting of variables from each element and then sorting by name looks scary, and can give unexpected results (if your vector is `(x1, x10, x2)`, I believe you would get 3 for the divergence instead of 1 as you might expect, since `'10'` comes before `'2'` in the alphanumeric sort). Unless there's a better solution, I think we should have it so that the variables list has to always be given explicitly.",
    "created_at": "2014-05-01T19:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20777",
    "user": "eviatarbach"
}
```

Another thought:

The extracting of variables from each element and then sorting by name looks scary, and can give unexpected results (if your vector is `(x1, x10, x2)`, I believe you would get 3 for the divergence instead of 1 as you might expect, since `'10'` comes before `'2'` in the alphanumeric sort). Unless there's a better solution, I think we should have it so that the variables list has to always be given explicitly.



---

archive/issue_comments_020778.json:
```json
{
    "body": "If your vectors are callable symbolic vectors, you should be able to get the list of arguments from the base ring (since you've already explicitly given an order to the variables):\n\n\n```\nsage: f(x,y,z)=(x*y,y*z,z^2)\nsage: f\n(x, y, z) |--> (x*y, y*z, z^2)\nsage: type(f)\n<class 'sage.modules.vector_callable_symbolic_dense.Vector_callable_symbolic_dense'>\nsage: f.base_ring().arguments()\n(x, y, z)\n```\n",
    "created_at": "2014-05-02T02:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20778",
    "user": "jason"
}
```

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

archive/issue_comments_020779.json:
```json
{
    "body": "That's a great idea. I think we should have that for callable vectors.\n\nFor the record, Mathematica and Maple both have default coordinate systems, which is how they deal with this issue.",
    "created_at": "2014-05-03T05:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20779",
    "user": "eviatarbach"
}
```

That's a great idea. I think we should have that for callable vectors.

For the record, Mathematica and Maple both have default coordinate systems, which is how they deal with this issue.



---

archive/issue_comments_020780.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-18T03:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20780",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_020781.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-20T07:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20781",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_020782.json:
```json
{
    "body": "I've addressed all the comments.",
    "created_at": "2014-06-20T07:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20782",
    "user": "robertwb"
}
```

I've addressed all the comments.



---

archive/issue_comments_020783.json:
```json
{
    "body": "I was going to look at this, but looks like Eviatar and Samuel are on top, so just think of this as a ping :)",
    "created_at": "2014-08-27T15:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20783",
    "user": "kcrisman"
}
```

I was going to look at this, but looks like Eviatar and Samuel are on top, so just think of this as a ping :)



---

archive/issue_comments_020784.json:
```json
{
    "body": "Replying to [comment:24 kcrisman]:\n> I was going to look at this, but looks like Eviatar and Samuel are on top, so just think of this as a ping :)\n\nFeel free to look at this yourself :)",
    "created_at": "2014-10-22T06:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20784",
    "user": "robertwb"
}
```

Replying to [comment:24 kcrisman]:
> I was going to look at this, but looks like Eviatar and Samuel are on top, so just think of this as a ping :)

Feel free to look at this yourself :)



---

archive/issue_comments_020785.json:
```json
{
    "body": "My 2 cents, I'd have curl also take 2-dim inputs and return a vector. It might also be a good idea for a way (likely another method) which takes a 2-dim input and return a scalar as a shorthand (a la Green's theorem).\n\n+1 to getting these (fundamental) methods into Sage.",
    "created_at": "2014-10-22T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20785",
    "user": "tscrim"
}
```

My 2 cents, I'd have curl also take 2-dim inputs and return a vector. It might also be a good idea for a way (likely another method) which takes a 2-dim input and return a scalar as a shorthand (a la Green's theorem).

+1 to getting these (fundamental) methods into Sage.



---

archive/issue_comments_020786.json:
```json
{
    "body": "Are there any enhancements to this with-patch, 7-year-old ticket that simply can't be deferred 'till later so we can finally get this in?",
    "created_at": "2015-02-11T05:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20786",
    "user": "robertwb"
}
```

Are there any enhancements to this with-patch, 7-year-old ticket that simply can't be deferred 'till later so we can finally get this in?



---

archive/issue_comments_020787.json:
```json
{
    "body": "I added the 2-dim input. If you're happy with my changes, then I think we can set this to a positive review.\n----\nNew commits:",
    "created_at": "2015-02-11T15:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20787",
    "user": "tscrim"
}
```

I added the 2-dim input. If you're happy with my changes, then I think we can set this to a positive review.
----
New commits:



---

archive/issue_comments_020788.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-12T04:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20788",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020789.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-02-17T19:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3021#issuecomment-20789",
    "user": "vbraun"
}
```

Resolution: fixed
