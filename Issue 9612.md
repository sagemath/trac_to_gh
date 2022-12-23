# Issue 9612: revise functional_programming.rst

Issue created by migration from https://trac.sagemath.org/ticket/9612

Original creator: jhpalmieri

Original creation time: 2010-07-27 20:55:42

Assignee: mvngu

At #8465, the following suggestions were made about the document "Functional Programming for Mathematicians" (sage/doc/en/thematic_tutorials/functional_programming.rst):

1. reduce will be part of the functools module in python 3. might be helpful to import it from there to make it forward compatible  http://docs.python.org/library/functools.html <- or at least you might wanna add a link to that module in the bottom section.

2.  http://docs.python.org/library/itertools.html#itertools.starmap is quite cool if you have "izip"ed values for the function arguments. i.e. starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000. it's like f(a,b) vs. f(*c)

3. Besides that, have you explained the generator concept with the "yield" keyword? I'm not sure if that counts as functional programming but it is a nice topic in that context.

4. In the styles of programming section, the object-oriented example seemed a little contrived, and I would say was bad style to make an object for adding two things. I believe a better example would to use comparison instead of adding. Something procedural

```
def compare(a, b)
    return a - b;
```

versus like this for object-oriented

```
def class Comparable
    def compare(b)
        return self - b;
```


