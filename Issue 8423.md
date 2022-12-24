# Issue 8423: fractals: add code to plot julia sets

archive/issues_008423.json:
```json
{
    "body": "Assignee: sdietzel\n\nCC:  ncohen brunellus bhutz atowsley\n\nAdd code to sage for plotting Julia sets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8423\n\n",
    "created_at": "2010-03-02T18:37:36Z",
    "labels": [
        "fractals",
        "minor",
        "enhancement"
    ],
    "title": "fractals: add code to plot julia sets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8423",
    "user": "was"
}
```
Assignee: sdietzel

CC:  ncohen brunellus bhutz atowsley

Add code to sage for plotting Julia sets.

Issue created by migration from https://trac.sagemath.org/ticket/8423





---

archive/issue_comments_075494.json:
```json
{
    "body": "adds a \"fractals\" module to sage...",
    "created_at": "2010-03-02T19:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75494",
    "user": "was"
}
```

adds a "fractals" module to sage...



---

archive/issue_comments_075495.json:
```json
{
    "body": "Attachment [trac-8423_part1.patch](tarball://root/attachments/some-uuid/ticket8423/trac-8423_part1.patch) by mhampton created at 2010-03-02 19:54:46\n\nCarl Witty and I wrote a function for integral curvature Apollonian gaskets:\nhttp://neutraldrifts.blogspot.com/2009/01/integral-apollonian-packings-with-sage.html\nI have a Koch curve generator I can dig out as well.",
    "created_at": "2010-03-02T19:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75495",
    "user": "mhampton"
}
```

Attachment [trac-8423_part1.patch](tarball://root/attachments/some-uuid/ticket8423/trac-8423_part1.patch) by mhampton created at 2010-03-02 19:54:46

Carl Witty and I wrote a function for integral curvature Apollonian gaskets:
http://neutraldrifts.blogspot.com/2009/01/integral-apollonian-packings-with-sage.html
I have a Koch curve generator I can dig out as well.



---

archive/issue_comments_075496.json:
```json
{
    "body": "Also, as a big \"todo\" list, this wikipedia page is pretty comprehensive:\nhttp://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension",
    "created_at": "2010-03-02T19:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75496",
    "user": "mhampton"
}
```

Also, as a big "todo" list, this wikipedia page is pretty comprehensive:
http://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension



---

archive/issue_comments_075497.json:
```json
{
    "body": "(cc: me)",
    "created_at": "2010-03-02T20:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75497",
    "user": "ncohen"
}
```

(cc: me)



---

archive/issue_comments_075498.json:
```json
{
    "body": "Here's an iterated function system example (the fern):\n\n```\ndef fern(x,y):\n    \"\"\"\n    An iterated function system whose orbit traces out\n    a fern shape.\n    \n    INPUT:\n        x,y - numerical scalars\n    \n    OUTPUT:\n        a 2-component list of new x and y values.\n    \"\"\"\n    r = random()\n    if r<.01:\n        return [0,.16*y]\n    elif r < .08:\n        return [.2*x-.26*y, .23*x+.22*y+1.6]\n    elif r < .15:\n        return [-.15*x+.28*y, .26*x+.24*y+.44]\n    else: \n        return [.85*x+.04*y,-.04*x+.85*y+1.6]\ndef fern_orbit(n):\n    \"\"\"\n    Returns a trajectory of length n of the fern\n    iterated function system.\n    \n    INPUT:\n        n - an integer, the length of the trajectory\n        \n    OUTPUT:\n        a list of 2-component lists\n        \n    EXAMPLE:\n       sage: show(points(fern_orbit(10000),pointsize=1),axes=False)\n    \"\"\"\n    traj = [[0,0]]\n    for i in range(n):\n        nt = fern(traj[-1][0],traj[-1][1])\n        traj.append(nt)\n    return traj\n```\n",
    "created_at": "2010-03-02T21:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75498",
    "user": "mhampton"
}
```

Here's an iterated function system example (the fern):

```
def fern(x,y):
    """
    An iterated function system whose orbit traces out
    a fern shape.
    
    INPUT:
        x,y - numerical scalars
    
    OUTPUT:
        a 2-component list of new x and y values.
    """
    r = random()
    if r<.01:
        return [0,.16*y]
    elif r < .08:
        return [.2*x-.26*y, .23*x+.22*y+1.6]
    elif r < .15:
        return [-.15*x+.28*y, .26*x+.24*y+.44]
    else: 
        return [.85*x+.04*y,-.04*x+.85*y+1.6]
def fern_orbit(n):
    """
    Returns a trajectory of length n of the fern
    iterated function system.
    
    INPUT:
        n - an integer, the length of the trajectory
        
    OUTPUT:
        a list of 2-component lists
        
    EXAMPLE:
       sage: show(points(fern_orbit(10000),pointsize=1),axes=False)
    """
    traj = [[0,0]]
    for i in range(n):
        nt = fern(traj[-1][0],traj[-1][1])
        traj.append(nt)
    return traj
```




---

archive/issue_comments_075499.json:
```json
{
    "body": "The `@`interact example on the logistic bifurcation diagram might qualify as a fractal too:\n\nhttp://wiki.sagemath.org/interact/dynsys#CythonizedLogisticOrbitMap",
    "created_at": "2010-03-02T21:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75499",
    "user": "mhampton"
}
```

The `@`interact example on the logistic bifurcation diagram might qualify as a fractal too:

http://wiki.sagemath.org/interact/dynsys#CythonizedLogisticOrbitMap



---

archive/issue_comments_075500.json:
```json
{
    "body": "Actually, trac_8423_julia.patch is not correct. Don't use it.",
    "created_at": "2010-04-09T06:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75500",
    "user": "sdietzel"
}
```

Actually, trac_8423_julia.patch is not correct. Don't use it.



---

archive/issue_comments_075501.json:
```json
{
    "body": "Probably related: #23257",
    "created_at": "2017-06-26T16:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75501",
    "user": "kcrisman"
}
```

Probably related: #23257



---

archive/issue_comments_075502.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-08-02T12:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75502",
    "user": "bbarros"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075503.json:
```json
{
    "body": "Changing keywords from \"\" to \"complexdynamics, gcoc2017\".",
    "created_at": "2017-08-02T12:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75503",
    "user": "bbarros"
}
```

Changing keywords from "" to "complexdynamics, gcoc2017".



---

archive/issue_comments_075504.json:
```json
{
    "body": "Changing component from fractals to dynamics.",
    "created_at": "2017-08-02T12:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75504",
    "user": "bbarros"
}
```

Changing component from fractals to dynamics.



---

archive/issue_comments_075505.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-08-02T18:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75505",
    "user": "bhutz"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075506.json:
```json
{
    "body": "I have only minor issues with this\n\n- I see that when you pass in a period you are giving a random root of the dynatomic. I'm not opposed to this, but it should definitely be documented. Especially since some of the roots are actually lower period points when the tail is not 0, for example `julia_plot(period=[1,1])` returns a c value of a fixed point sometimes.\n\n- return_points - This seems to return the c value associated to a particular period. If I've understood this correctly, it is not needed.\n\n- In several places you say you are iterating `c` for the Julia set. You are not, you are iterating the complex point corresponding to that pixel for the fixed c value defining the map.\n----\nLast 10 new commits:",
    "created_at": "2017-08-02T18:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75506",
    "user": "bhutz"
}
```

I have only minor issues with this

- I see that when you pass in a period you are giving a random root of the dynatomic. I'm not opposed to this, but it should definitely be documented. Especially since some of the roots are actually lower period points when the tail is not 0, for example `julia_plot(period=[1,1])` returns a c value of a fixed point sometimes.

- return_points - This seems to return the c value associated to a particular period. If I've understood this correctly, it is not needed.

- In several places you say you are iterating `c` for the Julia set. You are not, you are iterating the complex point corresponding to that pixel for the fixed c value defining the map.
----
Last 10 new commits:



---

archive/issue_comments_075507.json:
```json
{
    "body": "The idea behind `return_points` was to provide a way for the user to find all of the Julia sets of a certain cycle structure instead of just getting a random one. For example, if I wanted to find all of Julia sets with cycle structure (2,3) I can run the following code:\n\n\n```python\nc_values = julia_plot(period=[2,3], return_points=True)\nfor c in c_values:\n    julia_plot(c)\n```\n\n\nI wasn't sure if this would be useful or not so if it isn't practical, I can remove it.",
    "created_at": "2017-08-02T22:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75507",
    "user": "bbarros"
}
```

The idea behind `return_points` was to provide a way for the user to find all of the Julia sets of a certain cycle structure instead of just getting a random one. For example, if I wanted to find all of Julia sets with cycle structure (2,3) I can run the following code:


```python
c_values = julia_plot(period=[2,3], return_points=True)
for c in c_values:
    julia_plot(c)
```


I wasn't sure if this would be useful or not so if it isn't practical, I can remove it.



---

archive/issue_comments_075508.json:
```json
{
    "body": "Yes, it would be nice to be able to generate those c values, but I don't think that belongs in the julia_plot function.\n\nHaving an example that loops through the roots of the dynatomic and plots each Julia set is probably a good example to add to the documentation so the user doesn't have to come up with their own way to do it.",
    "created_at": "2017-08-03T00:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75508",
    "user": "bhutz"
}
```

Yes, it would be nice to be able to generate those c values, but I don't think that belongs in the julia_plot function.

Having an example that loops through the roots of the dynatomic and plots each Julia set is probably a good example to add to the documentation so the user doesn't have to come up with their own way to do it.



---

archive/issue_comments_075509.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-03T21:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75509",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075510.json:
```json
{
    "body": "I separated the functionality of finding c values based on cycle structure into a separate function. Should this be something that users need to import before using? Also, to make sure that my documentation is correct, is the cycle structure being inputted for the point c under the map Q_c(z) = z * * 2 + c  ?",
    "created_at": "2017-08-03T21:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75510",
    "user": "bbarros"
}
```

I separated the functionality of finding c values based on cycle structure into a separate function. Should this be something that users need to import before using? Also, to make sure that my documentation is correct, is the cycle structure being inputted for the point c under the map Q_c(z) = z * * 2 + c  ?



---

archive/issue_comments_075511.json:
```json
{
    "body": "Except that now you have the problem that this function will not always return correct answers (some the c values will have a different minimal period structure).\n\nThe right functionality here is something that takes a post-critical portrait and returns the maps with the specified family has that portrait (such as quadratic polynomials...). This is not a trivial construction in general and implementing this particular specialized function that sort of does it seems like not a good long term plan.\n\nI'm still inclined to remove that function entirely and have an example that demonstrates how to do it as part of the julia_plot() documentation.",
    "created_at": "2017-08-04T02:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75511",
    "user": "bhutz"
}
```

Except that now you have the problem that this function will not always return correct answers (some the c values will have a different minimal period structure).

The right functionality here is something that takes a post-critical portrait and returns the maps with the specified family has that portrait (such as quadratic polynomials...). This is not a trivial construction in general and implementing this particular specialized function that sort of does it seems like not a good long term plan.

I'm still inclined to remove that function entirely and have an example that demonstrates how to do it as part of the julia_plot() documentation.



---

archive/issue_comments_075512.json:
```json
{
    "body": "That sounds like a good idea. I'll remove the extra function and add the following example to the `julia_plot` documentation:\n\n\n```python\nsage: period = [2,3] # not tested\n....: R.<c> = QQ[]\n....: P.<x,y> = ProjectiveSpace(R,1)\n....: R = P.coordinate_ring()\n....: H = End(P)\n....: f = H([x^2+c*y^2,y^2])\n....: L = f.dynatomic_polynomial(period).subs({x:0,y:1}).roots(ring=CC)\n....: c_values = [k[0] for k in L]\n....: for c in c_values:\n....:     julia_plot(c)\n```\n\n\nIs that what you had in mind?",
    "created_at": "2017-08-04T17:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75512",
    "user": "bbarros"
}
```

That sounds like a good idea. I'll remove the extra function and add the following example to the `julia_plot` documentation:


```python
sage: period = [2,3] # not tested
....: R.<c> = QQ[]
....: P.<x,y> = ProjectiveSpace(R,1)
....: R = P.coordinate_ring()
....: H = End(P)
....: f = H([x^2+c*y^2,y^2])
....: L = f.dynatomic_polynomial(period).subs({x:0,y:1}).roots(ring=CC)
....: c_values = [k[0] for k in L]
....: for c in c_values:
....:     julia_plot(c)
```


Is that what you had in mind?



---

archive/issue_comments_075513.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-04T19:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75513",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075514.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-08-04T19:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75514",
    "user": "bbarros"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075515.json:
```json
{
    "body": "Note that there is a merge conflict now.\n\nAlso, there are a few more minor things in the docs\n\n- misspelling - 'diplay'\n\n- You don't have all the instances of `c` and `p` right. It should be `Q_c(p)` and you are coloring `p`.\n\n- you need to wrap some of the kwds descriptions as those lines are too long\n\n- I'd also suggest saying that the period: `with (formal) cycle structure` to indicted that you are using the dynatomic polynomial\n\n- `if period is not None` I guess is ok, but I'm used to seeing `if not period is None`.",
    "created_at": "2017-08-05T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75515",
    "user": "bhutz"
}
```

Note that there is a merge conflict now.

Also, there are a few more minor things in the docs

- misspelling - 'diplay'

- You don't have all the instances of `c` and `p` right. It should be `Q_c(p)` and you are coloring `p`.

- you need to wrap some of the kwds descriptions as those lines are too long

- I'd also suggest saying that the period: `with (formal) cycle structure` to indicted that you are using the dynatomic polynomial

- `if period is not None` I guess is ok, but I'm used to seeing `if not period is None`.



---

archive/issue_comments_075516.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-07T17:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75516",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075517.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-08-08T16:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75517",
    "user": "bhutz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-08-11T18:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8423#issuecomment-75518",
    "user": "vbraun"
}
```

Resolution: fixed
