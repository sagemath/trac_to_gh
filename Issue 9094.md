# Issue 9094: is_square and sqrt for fraction fields

Issue created by migration from https://trac.sagemath.org/ticket/9094

Original creator: robertwb

Original creation time: 2010-05-30 08:45:39

Assignee: AlexGhitza

CC:  mderickx pbruin mstreng minz

Depends on #9093 for correctness.


---

Comment by robertwb created at 2010-05-30 09:27:55

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-06-06 19:57:08

Looks good (and useful).  Patch applies fine to 4.4.3.  I tested all sage/rings and had one failure (in a new doctest, on 64-bit ubuntu):

```
File "/storage/jec/sage-4.4.3/devel/sage-tests/sage/rings/polynomial/polynomial_element.pyx", line 1262:
    sage: (9 * f^10 * g^4).sqrt() == 3 * f^5 * g^2
Expected:
    True
Got:
    False
```

I have never been happy about doctests using random elements, however deterministic they are supposed to be.

I would have tested for self==0 at the start of the sqrt function, but that case will be caught quickly anyway, so no problem.

I have been working on a patch to add both all= and extend= parameters to the sqrt function for AA and QQbar, having found how awkward it is when the parameters are not uniform across types.  Would it be worth adding an extend= parameter here, even if a NotImplementedError is raised when it is needed (i.e. for sqrt of a non-square when extend=True)?

So: needs work because of the doctest failure;  up to you whether to do the extend= thing.


---

Comment by cremona created at 2010-06-06 19:57:08

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2010-07-07 09:48:23

is_square and sqrt can be done generally for fraction fields, given the corresponding functions for the base ring:


```
is_square (a / b) = is_square (a * b)
sqrt (a / b) = sqrt (a * b) / b
```



---

Comment by mderickx created at 2010-07-07 14:34:33

On sage days 23 we discussed how to make this faster by avoiding factoring in polynomial rings. We are currently implementing this together with the remark of pbruin. When finnished the patch will be added to 9054 because it also fixes some other bugs on that ticket.


---

Comment by mderickx created at 2010-07-08 18:12:41

This patch also leaks memory, probably because of bug #9129


```
t=get_memory_usage()
Pr.<x>=ZZ[]
for i in range(500):
    C=((x^2+1)*x+1)
    B=C^2
    print "memusage", get_memory_usage(t)
    time x=B.sqrt()
```

executing the above gives:

```
memusage 0.0
Time: CPU 0.00 s, Wall: 0.00 s
memusage 0.0
Time: CPU 0.00 s, Wall: 0.00 s
memusage 0.0
Time: CPU 0.00 s, Wall: 0.00 s
memusage 0.0
Time: CPU 0.00 s, Wall: 0.00 s
memusage 0.0
Time: CPU 0.02 s, Wall: 0.02 s
memusage 1.20703125
Time: CPU 0.18 s, Wall: 0.19 s
memusage 23.79296875
Time: CPU 2.33 s, Wall: 2.36 s
memusage 148.12890625
Time: CPU 31.70 s, Wall: 32.24 s
memusage 1534.01171875
^C
^C
```


Ps. if you want to check this, please don't let the loop run as long as I did ;). It might make your computer on the edge of crashing


---

Comment by mderickx created at 2010-07-17 10:03:28

I just added a patch which should fix this also. It does it in a slightly different way. The sqrt() functions just are using the is_square(root=True) functionality (one should not have two square root finding algorithms in parralel). Also the sqrt() function has now the optional parameter extend. The is_square() function now also uses the trick mentioned by Peter the Bruin which is very general as it should be in this general base class.

The patch should be installed aplied to 4.4.4 instead of the other patch.


---

Comment by mderickx created at 2010-07-17 10:03:28

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2010-07-17 11:34:21

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-07-17 11:34:21

Changing type from defect to enhancement.


---

Comment by mstreng created at 2010-07-17 11:34:21

Looks good. No time for a complete review right now, but here are some remarks:

 * Check spelling of your documentation, you probably don't mean "wether" (=castrated sheep), but "whether" (spell checker doesn't help that much here). "Requiered" has one "e" too much.

 * Illustrate is_square(root = True) for the user by providing a square example and a non-square example.

 * The internal variable name ``is_sqrt`` is confusing, remove the "t".

 * You write "This code is quite general, it could even be implemented for all integral domains as soon as they have the is_square(root=True) option", don't you mean "This code is quite general, it works for all integral domains that have the is_square(root = True) option"?

 * I think sqrt(self, extend = True, all = False, name=None ) should have tests of all combinations of options and squareness, i.e: sq/non-sq, extend True/False, all True/False = 2*2*2 = at least 8 examples. The extend=True for a non-square should also have examples with name=None and name=something.

 * Perhaps include examples for more base fields?

 * consider adding a few more spaces for readability thougout, e.g. around "="

 * "if root==True:", why not write "if root:"?


---

Comment by mderickx created at 2010-07-17 14:33:48

I changed all you asked for except for "Perhaps include examples for more base fields?". Time for another review :)


---

Comment by mderickx created at 2010-07-17 14:33:48

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2010-07-18 09:48:44

fraction_field_element.pyx, line 326 "_parent" --> "parent()" (don't use a hidden variable, use the function that returns its value)

polynomial_ring_element.pyx, line 1306, "#This code is quite general, it works for all integral domains that have the is_square(root = True) option"
- This comment is confusing: does "all integral domains that..." refer to self.parent() or to self.parent().base_ring()? Why not just remove this comment?
- Are you proposing to move the code to are more general class of ring elements? Then why not just do that? Right now, you have the same code for fraction fields and polynomial rings, but you could just put it in a more general class and add a test if self.parent() is a domain and "self.is_square()" exists and has a parameter "root". (You don't have to do this to get a positive review, but you can think about it and/or try it)

(for both files:) It is helpful for others if the documentation of sqrt says how square roots are computed, i.e. says "Calls is_square(root = True) to find the square root". This can be done in an "ALGORITHM:" block. 

Build the documentation using "sage -docbuild reference html" to test the following yourself:
- the input, output, and examples blocks of lines 1260, 1265, and 1269 of sqrt for Polynomial don't indent and don't format nicely. All this needs is an extra empty line after the mentioned lines. See for example the is_square documentation.
- same for the input and output blocks of sqrt for fraction field elements on lines 336 and 341.


---

Comment by mstreng created at 2010-07-18 09:48:44

Changing status from needs_review to needs_work.


---

Comment by mderickx created at 2010-07-18 11:00:01

The "This code is quite general" comment did what it had to do. I put it there in the hope that someone would come with a suggestion like you did. I had the feeling that the dubble code could be removed in a nice and general way, but I didn't know how. So by what you say I should just move the code to a more general class and then it will also work for fraction fields and polynomial rings (and possibly even more rings). What would be this more general class and where to find it?

sage/rings/ring_element.py has only one line of code:


```

from sage.structure.element import !RingElement, is_RingElement

```


So should I add it to the RingElement class thats imported from sage.structure.element?


---

Comment by mstreng created at 2010-07-18 13:20:36

In the sage reference manual [http://www.sagemath.org/doc/reference/](http://www.sagemath.org/doc/reference/), you can search for a class and then click on its base classes. It appears that the least general common base class is sage.structure.element.CommutativeRingElement, which in turn extends sage.structure.element.RingElement. As your implementation is for domains only, you should put it in CommutativeRingElement.

You can start your code by checking hasattr(self, 'is_square'). I don't know how to check if the function self.is_square has a keyword argument 'root' other than using try. You should try to catch "TypeError: is_square() got an unexpected keyword argument 'root'" and raise NotImplementedError, "Please implement is_square with option 'root = True' for objects of type %s" % type(self)

Most importantly, check if there is no subclass of CommutativeRingElement that implements is_square by calling sqrt ;p


---

Comment by mstreng created at 2010-07-18 13:51:52

actually, instead of CommutativeRingElement, I guess RingElement is fine as well, as long as all = True raises a NotImplementedError


---

Comment by mderickx created at 2010-07-18 19:11:13

Catching a specific TypeError isn't possible apparently.


```

try:

    raise !TypeError("sqrt() got an unexpected keyword argument 'root'")

except !TypeError("sqrt() got an unexpected keyword argument 'root'"):

    print "lol"

```


gives as output


```

Traceback (click to the left of this block for traceback)
...
TypeError: sqrt() got an unexpected keyword argument 'root'
` ||
|| `

```


but a new version is on it's way wich just catches all typeerrors


---

Comment by mderickx created at 2010-07-18 20:03:17

Your e.blablablah remark worked so I do the catching in that way now. 

I decided to go for the commutative ring element class and I already implemented it there. If you think general ring elements is nicer you can put it there if you want (shouldn't be to much work, just some extra checking needed I guess). Upload comming in a few minutes.


---

Comment by mderickx created at 2010-07-18 20:19:48

Hej Marco,

I was already finnished when I read your last comment. Your suggestion last suggestion makes it slightly faster I guess. But I think the code is ok like it is now. I'm leaving for a holliday tomorrow and still got stuff to do, so I hope the patch is ok as it is now and else it will have to wait.


---

Comment by mderickx created at 2010-07-18 20:59:47

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2010-07-20 23:02:42

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-07-20 23:02:42

On line 1903 you check if the message is "is_square() got an unexpected keyword argument 'root'", but you should also check for "is_square() takes no keyword arguments", which happens for 5.sqrt(root = True). This behaviour should have a good doctest.

After catching a ValueError, line 1904 says:

raise NotImplementedError("Please implement is_square with option 'root = True' for %s" % type(self))

The ValueError may have been raised by another object than self. For example, if self has an is_square(root = True), but calls b.is_square(root = root) of another object b. In that case, this message is misleading: it says that self.is_square(root = True) should be implemented, while it is already well implemented and it is in fact b.is_square(root = True) that should be implemented. You can replace the message by the following:

raise NotImplementedError("Please implement sqrt() for objects of type %s" % type(self))

Can you get examples where these errors are raised and add them to the doctests?

Alternatively, you can either

 * make sure "is_square" exists for CommutativeRingElement and "is_square" has a keyword argument "root" for every subclass of CommutativeRingElement (you'll be writing NotImplementedError a lot :) and should check for tickets that implement the root = True behaviour). This seems to be a lot more stable than the current approach.

 * or bring back the double-code version with the same sqrt() function in two distinct classes.


---

Comment by mstreng created at 2010-07-22 12:27:32

Are you sure you did a complete doctest of sage before submitting the patch?

```
sage: QuadraticField(2, 'a')
NotImplementedError: Please implement is_square with option 'root = True' for <type 'sage.rings.real_lazy.LazyWrapper'>
```

The problem is in RLF(2).sqrt()

```
sage: RLF(2).sqrt()
NotImplementedError: Please implement is_square with option 'root = True' for <type 'sage.rings.real_lazy.LazyWrapper'>
```


RLF(2) is a LazyWrapper, which doesn't have a sqrt attribute, but simulates one via __getattr__ (line 631 of sage/rings/real_lazy.pyx). But LazyWrapper extends (via some other classes) CommutativeRingElement, so that now it does have an attribute sqrt (your sqrt function), which means the __getattr__ of LazyWrapper doesn't get a chance. Your sqrt function then complains about the non-existence of is_square with root = 'True'.

You can probably fix this by making a sqrt function for LazyWrapper that calls LazyNamedUnop(self._parent, self, 'sqrt'). Or you can follow your own advice: "implement is_square with option 'root = True' for ....". Maybe there is a better way, you can also ask one of the mailing lists. Alternatively, you can always go back to your double code.

Anyway, every time before submitting a patch, do everything that a reviewer would do, including a full doctest of all of Sage:
[http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch](http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch)
On a multi-core machine, you can speed up the doctest by using
`./sage -tp 4 -long devel/sage-main/`
where 4 is replaced by the number of cores you are willing to use.


---

Attachment


---

Comment by mderickx created at 2011-03-22 01:11:46

Only apply: trac_9094-sqrt-mderickx.2.patch


---

Comment by mderickx created at 2011-03-22 01:11:46

Changing status from needs_work to needs_review.


---

Comment by minz created at 2011-03-22 05:15:26

Since you told me you're going to rewrite the patch, I'm holding off on doctesting. Three short comments:

in structure/element.pyx


1) Line 1920 (): true --> True


2) Line 2002 (): all=False = all=True

3) The memory leak (from comment [#9](http://trac.sagemath.org/sage_trac/ticket/9094#comment:9)) is no leak after all. Note that you replace x in each iteration by C. If one doesn't do that, memory usage in each iteration is 0.0. :)


---

Comment by minz created at 2011-03-22 05:15:26

Changing assignee from AlexGhitza to minz.


---

Comment by minz created at 2011-03-22 05:22:06

Changing assignee from minz to AlexGhitza.


---

Comment by robertwb created at 2011-03-22 05:56:44

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2011-03-22 05:56:44

* is_square for fraction field elements now always computes a root, even if it's not needed. This can be quite expensive. 

 * Why are you writing boilerplate wrappers for all of LazyNamedUnop? Just do is_square and sqrt if need be. 

 * Using _parent is just fine, especially for subclasses. No need to incur the extra expense of a method call.


---

Comment by mstreng created at 2011-03-22 12:27:21

Replying to [comment:27 robertwb]:
>  * is_square for fraction field elements now always computes a root, even if it's not needed. This can be quite expensive. 

Indeed, it should use `root=root` instead of `root=True`

> 
>  * Why are you writing boilerplate wrappers for all of LazyNamedUnop? Just do is_square and sqrt if need be. 

Hi Robert,

I can answer this question. This was [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/441948aa73d1c49f). 4 options were discussed for dealing with these unitary operators for lazy numbers.

A) leaving them as they were

B) hard-coding them (as Maarten just did)

C) "fixing LazyNamedUnop to preserve documentation"

D) "populating these methods at class creation time
(rather than attribute lookup time, perhaps dynamically creating a
docstring for them)"

Option A was discarded: it lacks tab completion, and (as we saw in this ticket) leads to a big mess and a lot of confusion when a base class such as RingElement gets a default implementation for one of these unitary operators.

Options C and D were suggested by you, but you seemed to be the only one in the discussion who knew how to do them. Maarten said he was interested in them, and then nothing happened for months.

So I guess that in the end Maarten implemented the only remaining option, which leads to stable, transparent, understandable code that is unfortunately a bit long.

I think the extra time that Sage developers will need when extending or changing Maarten's long list of similar methods is not too bad if you compare it to the time that Sage developers will need when trying to understand more complicated code and having to debug it if something unforeseen happens. But that's just my opinion.

+1 from me for the way Maarten implemented it.

> 
>  * Using _parent is just fine, especially for subclasses. No need to incur the extra expense of a method call. 

Are there general guidelines for this? I can imagine `_parent` to be faster, but `parent()` to be more stable in case creative implementations are in base classes.


---

Comment by mderickx created at 2011-03-22 16:29:23

New file added Only apply: trac_9094-sqrt-mderickx.patch

It's RLF is now boiler plate code free, works with tab completion and works with inheritance thanks to Thomas Kluiver here at sage days since he told me how to do it :).

Also added the other suggestions. Hopefully finally a final version??


---

Comment by mderickx created at 2011-03-22 16:29:23

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2011-03-22 17:05:17

Hi Maarten, could you add a doctest to `__dir__` so that doctest coverage goes up instead of down? Just something simple like

```
sage: "log" in RLF(sqrt(8)).__dir__()
True
```



---

Comment by mderickx created at 2011-03-22 17:24:03

A patch instead of the other one, which I ofcourse think is better ;)


---

Attachment

Done :)


---

Comment by robertwb created at 2011-03-22 19:05:23

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2011-03-22 19:05:23

Looks good.


---

Comment by jdemeyer created at 2011-04-13 07:42:45

Resolution: fixed
