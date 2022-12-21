# Issue 3342: bizarre source code introspection output

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-31 17:44:28

Assignee: tba

CC:  ddrake

I observed the following in sage-3.0.2 on both Linux and OS X.
Note the very bizarre output of x.is_zero??


```
sage: R.<x,y> = QQ[]; S.<x,y> = Frac(R)
sage: x.is_zero??
Type:		builtin_function_or_method
Base Class:	<type 'builtin_function_or_method'>
String Form:	<built-in method is_zero of FractionFieldElement object at 0x2afd954b16e0>
Namespace:	Interactive
Source:
    def is_zero(self):
        """
        Return True if self equals self.parent()(0). The default
        implementation is to fall back to 'not self.__nonzero__'.

        NOTE: Do not re-implement this method in your subclass but
        implement __nonzero__ instead.
        """
        return not selfClass Docstring:
    <attribute '__doc__' of 'builtin_function_or_method' objects>

```



---

Comment by jhpalmieri created at 2009-06-10 21:19:54

I'm not sure which part is bizarre -- maybe the lack of any white space or line break between "return not self" and "Class Docstring"?  As far as I can tell, this is an IPython issue.  If you change line 520 of OInspect.py (in SAGEROOT/local/lib/python/site-packages/IPython/) from 

```
                    out.writeln(header('Class Docstring:\n') +
```

to

```
                    out.writeln(header('\n\nClass Docstring:\n') +
```

it fixes this problem.

Should we patch the IPython to incorporate this change?  I've put a new spkg [here](http://sage.math.washington.edu/home/palmieri/SPKG/ipython-0.9.1.spkg), but I don't know if this is the right solution.


---

Comment by jhpalmieri created at 2009-06-12 05:47:17

By the way, there are similar problems with other docstrings and source code retrieval: type `GroupAlgebra??` or `SteenrodAlgebra??`.  The former yields lines looking like this:

```
        return GroupAlgebras(self.base_ring())
Constructor information:
```

(not too bad, but there should be an extra blank line before "Constructor information:") while the latter gives

```
            return SteenrodAlgebra_generic(p=p, basis=basis_name)Call docstring:
```

There should be two blank lines before "Call docstring".  

The new version of the spkg has a slight disadvantage: if you ask for docstrings, not source, in situations like these (`x.is_zero?`, `GroupAlgebra?`, `SteenrodAlgebra?`), then there are maybe two new blank lines between the main part of the docstring and "Class docstring", "Constructor information", or "Call docstring".  We could get rid of these with yet more tinkering, but I'm not sure it's worth it.

When refereeing, the only new thing in the ipython spkg is the patch to OInspect.py.


---

Comment by wjp created at 2009-07-16 09:10:12

It looks like the new spkg is in fact at http://sage.math.washington.edu/home/palmieri/SPKG/ipython-0.9.1.p0.spkg rather than at the link given.

Also, independent from this ticket there is another 0.9.1.p0 spkg in sage-4.1, so these versions will have to be merged. I'll merge and review later today.


---

Comment by wjp created at 2009-07-16 13:59:54

I think this patch is not the right way to approach this. Maybe replacing the `write` in `out.write(header('Source:\n')+source.rstrip())` by `writeln` is a cleaner approach. I'd feel a lot more confident about changing that if I would understand why some of the writes in the `pinfo` function use `write` while others use `writeln`, though...

Another thing is that this particular class docstring "<attribute '__doc__' of 'builtin_function_or_method' objects>" looks like a good candidate for inclusion in the "Skip Python's auto-generated docstring" list in that function, because it doesn't seem to add much (if any) useful information.
(That seems to be caused by it being in a Cython class, which is probably why IPython doesn't already list it.)


---

Comment by wjp created at 2010-07-09 20:11:17

I did some more research:

In 'vanilla' IPython, the `<attribute '__doc__' of 'builtin_function_or_method' objects>` output is suppressed because `inspect.getdoc(object)` checks if `object.__doc__` is an instance of `types.StringTypes`.

Our replacement `sage.misc.sageinspect.sage_getdoc` doesn't have this check. We can probably add it, but I'll (or someone else) will have to test that doesn't break introspection in other places such as the notebook.


I also reported the missing whitespace between `Source` and `Class Docstring` upstream to the ipython developers.


---

Comment by wjp created at 2010-07-09 20:20:58

Changing status from needs_work to needs_review.


---

Comment by wjp created at 2010-07-09 20:26:00

I added a patch that adds the extra check I mentioned to `sage_getdoc`. It seems to work both on the command line and in the notebook.


---

Attachment


---

Comment by wjp created at 2010-07-09 20:31:49

Small addendum: I failed to notice that the sagenb package has its own sage_getdoc, so it's not surprising this didn't break the notebook.


---

Comment by wjp created at 2010-07-09 20:51:24

the same change to duplicated code in sagenb


---

Comment by jhpalmieri created at 2010-07-10 02:53:34

Changing status from needs_review to positive_review.


---

Attachment

It looks okay and seems to behave well.  For some reason, I only see the original problem from the command line, not the notebook, so the sagenb patch may not strictly be needed; however, I think the two sageinspect files are supposed to synchronized as much as possible.

I didn't know about `types.StringTypes` before; that looks useful.


---

Comment by mpatel created at 2010-07-23 07:17:50

I've merged the sagenb repository patch into SageNB 0.8.2 at #9572.


---

Comment by ddrake created at 2010-07-27 02:30:23

Resolution: fixed


---

Comment by wjp created at 2011-03-22 16:03:47

The remaining whitespace issue has just been fixed upstream in ipython by https://github.com/ipython/ipython/commit/ab3257a1428fa7e61a3f0b25d8410653ec42aa35
