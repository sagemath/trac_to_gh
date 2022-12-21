# Issue 8423: fractals: add code to plot julia sets

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-02 18:37:36

Assignee: sdietzel

CC:  ncohen brunellus bhutz atowsley

Add code to sage for plotting Julia sets.


---

Comment by was created at 2010-03-02 19:08:49

adds a "fractals" module to sage...


---

Attachment

Carl Witty and I wrote a function for integral curvature Apollonian gaskets:
http://neutraldrifts.blogspot.com/2009/01/integral-apollonian-packings-with-sage.html
I have a Koch curve generator I can dig out as well.


---

Comment by mhampton created at 2010-03-02 19:55:59

Also, as a big "todo" list, this wikipedia page is pretty comprehensive:
http://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension


---

Comment by ncohen created at 2010-03-02 20:30:58

(cc: me)


---

Comment by mhampton created at 2010-03-02 21:13:43

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
    traj = [This is the Trac macro *0,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0,0-macro)
    for i in range(n):
        nt = fern(traj[-1][0],traj[-1][1])
        traj.append(nt)
    return traj
```



---

Comment by mhampton created at 2010-03-02 21:16:44

The `@`interact example on the logistic bifurcation diagram might qualify as a fractal too:

http://wiki.sagemath.org/interact/dynsys#CythonizedLogisticOrbitMap


---

Comment by sdietzel created at 2010-04-09 06:28:51

Actually, trac_8423_julia.patch is not correct. Don't use it.


---

Comment by kcrisman created at 2017-06-26 16:45:07

Probably related: #23257


---

Comment by bbarros created at 2017-08-02 12:51:06

Changing status from new to needs_review.


---

Comment by bbarros created at 2017-08-02 12:51:06

Changing keywords from "" to "complexdynamics, gcoc2017".


---

Comment by bbarros created at 2017-08-02 12:51:06

Changing component from fractals to dynamics.


---

Comment by bhutz created at 2017-08-02 18:14:12

Changing status from needs_review to needs_work.


---

Comment by bhutz created at 2017-08-02 18:14:12

I have only minor issues with this

- I see that when you pass in a period you are giving a random root of the dynatomic. I'm not opposed to this, but it should definitely be documented. Especially since some of the roots are actually lower period points when the tail is not 0, for example `julia_plot(period=[1,1])` returns a c value of a fixed point sometimes.

- return_points - This seems to return the c value associated to a particular period. If I've understood this correctly, it is not needed.

- In several places you say you are iterating `c` for the Julia set. You are not, you are iterating the complex point corresponding to that pixel for the fixed c value defining the map.
----
Last 10 new commits:


---

Comment by bbarros created at 2017-08-02 22:08:59

The idea behind `return_points` was to provide a way for the user to find all of the Julia sets of a certain cycle structure instead of just getting a random one. For example, if I wanted to find all of Julia sets with cycle structure (2,3) I can run the following code:


```python
c_values = julia_plot(period=[2,3], return_points=True)
for c in c_values:
    julia_plot(c)
```


I wasn't sure if this would be useful or not so if it isn't practical, I can remove it.


---

Comment by bhutz created at 2017-08-03 00:34:40

Yes, it would be nice to be able to generate those c values, but I don't think that belongs in the julia_plot function.

Having an example that loops through the roots of the dynatomic and plots each Julia set is probably a good example to add to the documentation so the user doesn't have to come up with their own way to do it.


---

Comment by git created at 2017-08-03 21:34:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by bbarros created at 2017-08-03 21:40:09

I separated the functionality of finding c values based on cycle structure into a separate function. Should this be something that users need to import before using? Also, to make sure that my documentation is correct, is the cycle structure being inputted for the point c under the map Q_c(z) = z * * 2 + c  ?


---

Comment by bhutz created at 2017-08-04 02:26:27

Except that now you have the problem that this function will not always return correct answers (some the c values will have a different minimal period structure).

The right functionality here is something that takes a post-critical portrait and returns the maps with the specified family has that portrait (such as quadratic polynomials...). This is not a trivial construction in general and implementing this particular specialized function that sort of does it seems like not a good long term plan.

I'm still inclined to remove that function entirely and have an example that demonstrates how to do it as part of the julia_plot() documentation.


---

Comment by bbarros created at 2017-08-04 17:23:17

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

Comment by git created at 2017-08-04 19:26:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by bbarros created at 2017-08-04 19:27:22

Changing status from needs_work to needs_review.


---

Comment by bhutz created at 2017-08-05 14:06:30

Note that there is a merge conflict now.

Also, there are a few more minor things in the docs

- misspelling - 'diplay'

- You don't have all the instances of `c` and `p` right. It should be `Q_c(p)` and you are coloring `p`.

- you need to wrap some of the kwds descriptions as those lines are too long

- I'd also suggest saying that the period: `with (formal) cycle structure` to indicted that you are using the dynatomic polynomial

- `if period is not None` I guess is ok, but I'm used to seeing `if not period is None`.


---

Comment by git created at 2017-08-07 17:59:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by bhutz created at 2017-08-08 16:16:26

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-08-11 18:17:22

Resolution: fixed
