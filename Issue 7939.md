# Issue 7939: shorten doctests in sage/rings/multi_polynomial_ideal.py

Issue created by migration from https://trac.sagemath.org/ticket/7939

Original creator: rlm

Original creation time: 2010-01-16 02:42:29

Assignee: AlexGhitza

CC:  polybori

Some of these doctests need to be marked `# long time`, at the very least.


---

Comment by rlm created at 2010-01-18 19:19:13

Note that just about every time I run all tests I get the following:


```
sage -t  ./sage/rings/polynomial/multi_polynomial_ideal.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```


Although, I never get this error when just running `sage -t  ./sage/rings/polynomial/multi_polynomial_ideal.py`.


---

Comment by rlm created at 2010-01-18 20:25:51

Changing assignee from AlexGhitza to tbd.


---

Comment by rlm created at 2010-01-18 20:25:51

Changing component from algebra to doctest.


---

Comment by malb created at 2010-01-18 20:56:57

Robert wrote:
> In running parallel doctests, I'm noticing that
> multi_polynomial_ideal.py is taking a very long time. Often, I get
> some sort of weird time out error (with the corresponding mysterious
> error/segfault message) when doing parallel testing, but I never get
> this error when it is testing alone. Also, when running tests, and
> looking at top, I notice that neither the python process or the
> Singular process ever goes above about 10% (or at least spends most of
> its time down around 0%-1%). Any ideas what is going on?

I am afraid I cannot contribute much. One relevant pointer could be that we are shuffling a lot of data between Singular and Sage, potentially via temporary files, this could explain why no process ever gets over 10%?


---

Comment by malb created at 2010-01-20 17:51:52

I decided to take another look. In the attached patch I move most of the functions in `multi_polynomial_ideal.py` to the new libsingular functions interface which does not need pexpect or IPC in general. 

On my Macbook Pro vanilla Sage 4.3 takes roughly *48* seconds to doctest `multi_polynomial_ideal.py`. With the attached patch applied it takes *26* seconds. I'd expect bigger improvements on machines with slow I/O (e.g. disks).

As a side-effect, a lot of the ideal operations are considerably (100x and such) faster now and the libsingular functions interface is more robust and handles more functions now.

Note that I tried to be a bit smart about the creation of the libsingular functions. One can now do:


```
sage: primdecSYZ = sage.libs.singular.ff.primdec.primdecSYZ
```


which will load 'primdec.lib' first and then create a wrapper for `primdecSYZ` in that library. A referee should also register whether he/she likes or dislikes this interface.

The attached patch requires an updated SPKG which is available at:

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20100120.spkg

I didn't mark any doctest `#long`, in fact, I added some doctests!


---

Comment by malb created at 2010-01-20 17:52:31

Changing status from new to needs_review.


---

Comment by malb created at 2010-01-20 17:52:31

Changing component from doctest to interfaces.


---

Comment by malb created at 2010-01-20 18:09:39

*sage.math:* 
 * vanilla:

```
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [360.3 s]
```


 * patch: *105* seconds


---

Comment by malb created at 2010-01-20 18:50:12

The updated patch fixes all doctest issues (on sage.math) for me.


---

Comment by AlexGhitza created at 2010-01-20 21:52:16

Martin,

This is great stuff!  I'll try to look at it as soon as I get the released 4.3.1.


---

Comment by malb created at 2010-01-20 23:10:01

Some details on how much faster single functions got:

*vanilla*

```python
sage: P = PolynomialRing(GF(127),5,'x')
sage: I = sage.rings.ideal.Cyclic(P)
sage: %time _ = I.triangular_decomposition()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 4.83 s

sage: %timeit I.basis_is_groebner(); I.basis_is_groebner.clear_cache()
10 loops, best of 3: 520 ms per loop

sage: I = Ideal([P.random_element() for _ in range(P.ngens())])
sage: %time _ = I.variety()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 4.25 s
```


*patch*

```python
sage: P = PolynomialRing(GF(127),5,'x')
sage: I = sage.rings.ideal.Cyclic(P)
sage: %time _ = I.triangular_decomposition()
CPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s
Wall time: 0.64 s

sage: %timeit I.basis_is_groebner(); I.basis_is_groebner.clear_cache()
1000 loops, best of 3: 1.98 ms per loop

sage: I = Ideal([P.random_element() for _ in range(P.ngens())])
sage: %time _ = I.variety()
CPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.64 s
```


All timings on sage.math.


---

Comment by PolyBoRi created at 2010-01-21 11:19:25

Hi!
I did not try it.
But I am pleased about the refactorizations of the function interface:
append_... returns leftv.
Regarding the passing of the attributes: 
I had something like that in mind. This is exactly, what is needed.

Regarding the option handling. Maybe we should use Pythons with statement:

```
with new_options:
    ...
```


Here an example from PolyBoRi with rings instead of options

```
...
def __enter__(self):
       old_ring=Ring()
       class ContextGuard(object):
           def __exit__(self, type, value, traceback):
               old_ring.set()
               return False
       return ContextGuard()

```


But this would affect the whole interface of the option class (not immediately setting options in singular...)
So, this is just a naive thought...

Cheers,
Michael


---

Comment by AlexGhitza created at 2010-01-21 12:07:41

Passes tests for me.

I tried to play with this a little bit, which lead to some questions:

1. Is there any way to get tab-completion to work in this situation:


```
sage: groebner = sage.libs.singular.ff.gro<TAB>  ? cannot open `__members__.lib`
   ? cannot open `__methods__.lib`
   ? cannot open `trait_names.lib`
   ? cannot open `_getAttributeNames.lib`
```


(If yes, maybe this should be a new ticket.)

2. After I got over my laziness, I typed in the whole thing:


```
sage: groebner = sage.libs.singular.ff.groebner
sage: P.<x, y> = QQ[]
sage: I = P.ideal(x^2-y, x+y)
sage: groebner(I)
   ? error occurred in standard.lib::groebner line 850: `parameter def i_par; parameter  list #;  `
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/home/ghitza/<ipython console> in <module>()

SystemError: NULL result without error in PyObject_Call
sage: groebner(I, ring=P)
   skipping text from `parameter` error at token `;`
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/home/ghitza/<ipython console> in <module>()

SystemError: NULL result without error in PyObject_Call
sage: from sage.libs.singular.function import SingularLibraryFunction
sage: f = SingularLibraryFunction("groebner")
sage: f(I)
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/home/ghitza/<ipython console> in <module>()

SystemError: NULL result without error in PyObject_Call
```


Is this a bug?  Or am I doing something silly?  If it's the latter, it would be good if there were an easy way for me to get help from the documentation.  I tried groebner? and groebner?? (which give very different results) but I couldn't get an answer quickly.


So I feel a little clueless at the moment.  I'm hoping your answers will help me out, and I'll look at this again.

(I still think it's terrific stuff, though!)


---

Comment by AlexGhitza created at 2010-01-21 12:07:41

Changing status from needs_review to needs_info.


---

Comment by malb created at 2010-01-21 12:29:15

Replying to [comment:11 AlexGhitza]:
> 1. Is there any way to get tab-completion to work in this situation:

Yes, that should be possible since `ff` is just an object (so it only needs trait names or however this function is called).

Do you like the name "ff" by the way (function factory)? It should be short but precise. "factory" is out, because there is a module in Singular called factory (for factorisation).
 
> 2. After I got over my laziness, I typed in the whole thing:
> 
> {{{
> sage: groebner = sage.libs.singular.ff.groebner
> sage: P.<x, y> = QQ[]
> sage: I = P.ideal(x^2-y, x+y)
> sage: groebner(I)
> }}}

Works for me, I just tried it.
 
> I tried groebner? and groebner?? (which give very different results) but I couldn't get an 
answer quickly.

`groebner?` will show you the Singular help while `groebner??` will show you the generic Singular function interface docstring. Maybe we should merge them in `groebner?`? Let me know in what order, and I can implement it.

> (I still think it's terrific stuff, though!)


---

Comment by malb created at 2010-01-21 12:34:01

Replying to [comment:10 PolyBoRi]:
> Regarding the passing of the attributes: 
> I had something like that in mind. This is exactly, what is needed.

Actually, the interface should be: ` {obj:{'isSB':1}} ` because right now we don't support e.g. "rank" which takes an integer. I should probably change that before this patch goes in.
 
> Regarding the option handling. Maybe we should use Pythons with statement:
> {{{
> with new_options:
>     ...
> }}}
> But this would affect the whole interface of the option class (not immediately setting options in singular...)

We do that for the `redSB` context, so you can enforce reduced GBs within a context. So an example session could be?


```
sage: opt = sage.libs.options.libsingular_options()
sage: opt['redTail'] = True
sage: with opt:
...     blah?
```


Mhh, does Cython support this yet?


---

Comment by PolyBoRi created at 2010-01-21 12:49:01

> We do that for the `redSB` context, so you can enforce reduced GBs within a context. So an example session could be?
> 
> {{{
> sage: opt = sage.libs.options.libsingular_options()
> sage: opt['redTail'] = True
> sage: with opt:
> ...     blah?
> }}}
> 

That would awesome and exception safe.

> Mhh, does Cython support this yet?

Good question.

Cheers,
Michael


---

Comment by AlexGhitza created at 2010-01-21 12:57:49

Replying to [comment:12 malb]:
> Do you like the name "ff" by the way (function factory)? It should be short but precise. "factory" is out, because there is a module in Singular called factory (for factorisation).

Well, the other possibility that springs to mind is "funfact" :)  Seriously, I think "ff" is fine.

> 
> Works for me, I just tried it.

And now it also works for me.  I restarted sage and tried it again and it seems fine.  I'm not sure what triggered it before.  I'll let you know if I happen to run into it again.

>  
> > I tried groebner? and groebner?? (which give very different results) but I couldn't get an 
> answer quickly.
> 
> `groebner?` will show you the Singular help while `groebner??` will show you the generic Singular function interface docstring. Maybe we should merge them in `groebner?`? Let me know in what order, and I can implement it.

Here is what I get when I do these two:

With `groebner?` I get the Singular help followed by


```
Call def:       groebner(self, *args, ring=None, interruptible=True, attributes=None)

Call docstring:
    
            Call this function with the provided arguments ``args`` in the
            ring ``R``.
    
            INPUT:
    
            - ``args`` - a list of arguments
    
            - ``ring`` - a multivariate polynomial ring
    
            - ``interruptible`` - if ``True`` pressing Ctrl-C during the
                                  execution of this function will
                                  interrupt the computation (default: ``True``)
    
            - ``attributes`` - a dictionary of optional Singular
                               attributes assigned to Singular objects (default: ``None``)
    
            EXAMPLE::
    
                sage: from sage.libs.singular.function import singular_function
                sage: size = singular_function('size')
                sage: P.<a,b,c> = PolynomialRing(QQ)
                sage: size(a, ring=P)
                1
                sage: size(2r,ring=P)
                1
                sage: size(2, ring=P)
                1
                sage: size(2)
                Traceback (most recent call last):
                ...
                ValueError: Could not detect ring.   
                sage: size(Ideal([a*b + c, a + 1]), ring=P)
                2
                sage: size(Ideal([a*b + c, a + 1]))
                2
                sage: size(1,2, ring=P)
                Traceback (most recent call last):                                          
                ...
                RuntimeError
    
                sage: size('foobar', ring=P)
                6
    
            Show the usage of the optional ``attributes`` parameter::
    
                sage: P.<x,y,z> = PolynomialRing(QQ)
                sage: I = Ideal([x^3*y^2 + 3*x^2*y^2*z + y^3*z^2 + z^5])
                sage: I = Ideal(I.groebner_basis())
                sage: hilb = sage.libs.singular.ff.hilb
                sage: hilb(I) # Singular will print // ** _ is no standard basis
    
            So we tell Singular that ``I`` is indeed a Groebner basis::
    
                sage: hilb(I,attributes={I:('isSB',)}) # no complaint from Singular
```


If I do `groebner??` I get


```
Type:           SingularLibraryFunction
Base Class:     <type 'sage.libs.singular.function.SingularLibraryFunction'>
String Form:    groebner (singular function)
Namespace:      Interactive
File:           /home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/libs/singular/function.so
Definition:     groebner(self, *args, ring=None, interruptible=True, attributes=None)
Source:
cdef class SingularLibraryFunction(SingularFunction):
    """
    EXAMPLES::

        sage: from sage.libs.singular.function import SingularLibraryFunction
        sage: R.<x,y> = PolynomialRing(QQ, order='lex')
        sage: I = R.ideal(x, x+1)
        sage: f = SingularLibraryFunction("groebner")
        sage: f(I)
        [1]
    """
    def __init__(self, name):
        """
        Construct a new Singular kernel function.

        EXAMPLES::

            sage: from sage.libs.singular.function import SingularLibraryFunction
            sage: R.<x,y> = PolynomialRing(QQ, order='lex')
            sage: I = R.ideal(x + 1, x*y + 1)
            sage: f = SingularLibraryFunction("groebner")
            sage: f(I)
            [y - 1, x + 1]
        """
        super(SingularLibraryFunction,self).__init__(name)
        self.call_handler = self.get_call_handler()

    cdef BaseCallHandler get_call_handler(self):
        cdef idhdl* singular_idhdl = ggetid(self._name, 0)
        if singular_idhdl==NULL:
            raise NameError("Function '%s' is not defined."%self._name)
        if singular_idhdl.typ!=PROC_CMD:
            raise ValueError("Not a procedure")

        cdef LibraryCallHandler res = LibraryCallHandler()
        res.proc_idhdl = singular_idhdl
        return res

    cdef bint function_exists(self):
        cdef idhdl* singular_idhdl = ggetid(self._name, 0)
        return singular_idhdl!=NULLCall def:    groebner(self, *args, ring=None, interruptible=True, attributes=None)

Call docstring:
    
            Call this function with the provided arguments ``args`` in the
            ring ``R``.
    
            INPUT:
    
            - ``args`` - a list of arguments
    
            - ``ring`` - a multivariate polynomial ring
    
            - ``interruptible`` - if ``True`` pressing Ctrl-C during the
                                  execution of this function will
                                  interrupt the computation (default: ``True``)
    
            - ``attributes`` - a dictionary of optional Singular
                               attributes assigned to Singular objects (default: ``None``)
    
            EXAMPLE::
    
                sage: from sage.libs.singular.function import singular_function
                sage: size = singular_function('size')
                sage: P.<a,b,c> = PolynomialRing(QQ)
                sage: size(a, ring=P)
                1
                sage: size(2r,ring=P)
                1
                sage: size(2, ring=P)
                1
                sage: size(2)
                Traceback (most recent call last):
                ...
                ValueError: Could not detect ring.   
                sage: size(Ideal([a*b + c, a + 1]), ring=P)
                2
                sage: size(Ideal([a*b + c, a + 1]))
                2
                sage: size(1,2, ring=P)
                Traceback (most recent call last):                                          
                ...
                RuntimeError
    
                sage: size('foobar', ring=P)
                6
    
            Show the usage of the optional ``attributes`` parameter::
    
                sage: P.<x,y,z> = PolynomialRing(QQ)
                sage: I = Ideal([x^3*y^2 + 3*x^2*y^2*z + y^3*z^2 + z^5])
                sage: I = Ideal(I.groebner_basis())
                sage: hilb = sage.libs.singular.ff.hilb
                sage: hilb(I) # Singular will print // ** _ is no standard basis
    
            So we tell Singular that ``I`` is indeed a Groebner basis::
    
                sage: hilb(I,attributes={I:('isSB',)}) # no complaint from Singular
```


(Sorry these are a bit long.)  But it looks like the first includes part, but not all, of the second.

What would I like to see?  (I'm not sure if this is feasible without a lot of work, but here goes.)  If I type `groebner?` I want to know how to use `groebner` from Sage.  For instance, seeing the example


```
sage: groebner = sage.libs.singular.ff.groebner
sage: P.<x, y> = PolynomialRing(QQ)
sage: I = P.ideal(x^2-y, y+x)
sage: groebner(I)
[x + y, y^2 - y]
```


and maybe a couple more showing other arguments/options would get me started with using the function.  So I would think that it's more useful and natural to have something like the above, followed by the Singular help that shows all the options, bells, and whistles.  Again, I don't know if this is feasible, but it would be nice.

If that's not possible, maybe have a docstring that shows how to use some of the more popular Singular functions from Sage.  If that's followed by the Singular help for the particular function I'm looking at at the moment, I should be able to put the two together and understand how to do things.


---

Comment by PolyBoRi created at 2010-01-21 13:13:17

> What would I like to see?  (I'm not sure if this is feasible without a lot of work, but here goes.)  If I type `groebner?` I want to know how to use `groebner` from Sage.  For instance, seeing the example
> 
> {{{
> sage: groebner = sage.libs.singular.ff.groebner
> sage: P.<x, y> = PolynomialRing(QQ)
> sage: I = P.ideal(x^2-y, y+x)
> sage: groebner(I)
> [x + y, y^2 - y]
> }}}
> 
> and maybe a couple more showing other arguments/options would get me started with using the function.  So I would think that it's more useful and natural to have something like the above, followed by the Singular help that shows all the options, bells, and whistles.  Again, I don't know if this is feasible, but it would be nice.
> 
> If that's not possible, maybe have a docstring that shows how to use some of the more popular Singular functions from Sage.  If that's followed by the Singular help for the particular function I'm looking at at the moment, I should be able to put the two together and understand how to do things.

IMHO Sage specific documentation belongs in the layer around this generic Singular interface.
You can construct singular functions add wrap them in Sage functions/methods of Sage classes...
This means having orthogonality: The LibSingularFunction is responsible for calling Singular and gives Singulars original docs.
In the wrapper around you can do the Sage specific stuff, which includes documentation, but also making the interface more Pythonic.
E.g. for groebner you might like to introduce keyword args.


```
Singular:
groebner(i,"par2var","slimgb");

```


```
Pythonic:
groebner(i,algorithms=["slimgb", "std"])
```

But that would be the responsible of another layer;-).


---

Comment by malb created at 2010-01-21 14:11:45

Replying to [comment:14 PolyBoRi]:
> That would awesome and exception safe.
> 
> > Mhh, does Cython support this yet?
> 
> Good question.

It seems it does.


---

Comment by malb created at 2010-01-21 14:15:27

Replying to [comment:15 AlexGhitza]:

For `groebner??` I get the call docstring for the `SingularFunction`.

> What would I like to see?  (I'm not sure if this is feasible without a lot of work, but here goes.)  If I type `groebner?` I want to know how to use `groebner` from Sage.  For instance, seeing the example
> 
> {{{
> sage: groebner = sage.libs.singular.ff.groebner
> sage: P.<x, y> = PolynomialRing(QQ)
> sage: I = P.ideal(x^2-y, y+x)
> sage: groebner(I)
> [x + y, y^2 - y]
> }}}
> 
> and maybe a couple more showing other arguments/options would get me started with using the function.  So I would think that it's more useful and natural to have something like the above, followed by the Singular help that shows all the options, bells, and whistles.  Again, I don't know if this is feasible, but it would be nice.
> 
> If that's not possible, maybe have a docstring that shows how to use some of the more popular Singular functions from Sage.  If that's followed by the Singular help for the particular function I'm looking at at the moment, I should be able to put the two together and understand how to do things.

It seems the second option is feasible.


---

Comment by malb created at 2010-01-21 14:18:37

The list of ToDos I can see is:
 * move singular options to the with statement syntax
 * allow tab completion on `ff`
 * make the docstring of Singular functions nicer (also for the pexect stuff)
 * fix the attributes parameter to support more than "isSB"
 * include this stuff in the reference manual (which is actually another ticket, but we can take care of this here)

I will work on this soon-ish, let me know if there are other issues I should address.


---

Comment by PolyBoRi created at 2010-01-21 15:00:43

Hmmm, tab completion is probably hard.
You might be interested to know, that there
exists
listvar(proc) in Singular
which is no function but a special command as proc is no first class object.

I followed its trace to grammar.y:

```
LISTVAR_CMD '(' PROC_CMD ')'
          {
            list_cmd(PROC_CMD,NULL,"// ",TRUE);
          }
```

I actually prints something...


---

Comment by malb created at 2010-01-21 15:04:51

We use that already for the pexpect interface, I was thinking about only calling that but that wouldn't update the list once a new library is loaded in libsingular but not in Singular itself.


```python
    def trait_names(self):
        """
         Return a list of all Singular commands.

         EXAMPLES::

             sage: singular.trait_names()
             ['exteriorPower',
              ...
              'stdfglm']
         """
        p = re.compile("// *([a-z0-9A-Z_]*).*") #compiles regular expression
        proclist = self.eval("listvar(proc)").splitlines()
        return [p.match(line).group(int(1)) for line in proclist]
```



---

Comment by PolyBoRi created at 2010-01-21 15:10:35

Martin, you know Singular better than most of my collegues in KL.
Okay, list_cmd is defined in
ipshell.cc.
It looks like an ugly students exercise to simplify it for our case,
typ: proc_cmd, no packages
and remove the printing...
Looking at the code now, I have no idea, what would remain...
Cheers,
Michael


---

Comment by PolyBoRi created at 2010-01-21 15:50:10

probably it comes down to


```
idhdl h=IDROOT;
while (h!=NULL)
  {
  
 if (PROC_CMD == IDTYP(h))
    {
        do something...
      }
      h=IDNEXT(h);
      
      }
```


I seem already to be infected by the Singular code...


---

Comment by malb created at 2010-01-21 17:23:50

This is such a fun way of not working on my thesis.

The updated patch improves the following things:
 * attributes interface more sensible now
 * tab completion for `sage.libs.singular.ff`
 * slightly improved docs (so it can go in the reference manual)
 * nicer docstrings for functions.

I didn't address the singular options interface yet (next on my list).


---

Comment by malb created at 2010-01-22 10:01:28

Changing status from needs_info to needs_review.


---

Comment by malb created at 2010-01-22 10:01:28

The attached updated patch should take care of all remaining known outstanding issues. 

For instance, you can now do this:


```python
sage: P.<a,b,c,d,e> = PolynomialRing(GF(127))
sage: I = sage.rings.ideal.Cyclic(P)
sage: std = sage.libs.singular.ff.std

sage: from sage.libs.singular.option import opt, opt_ctx
sage: opt['redTail']
True

sage: std(I)[-1]
d^2*e^6 + 28*b*c*d + ...

sage: with opt_ctx(redTail=False,redSB=False):
...      std(I)[-1]
d^2*e^6 + 8*c^3 + ...

sage: opt['redTail']
True
```



---

Comment by malb created at 2010-01-22 11:01:34

Fixing doctest issues.


---

Comment by AlexGhitza created at 2010-01-22 20:39:20

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2010-01-22 20:39:20

With the latest patch, I'm now seeing


```
sage -t -long "libs/singular/__init__.py"                   
	 [0.1 s]
sage -t -long "libs/singular/function.pyx"                  
	 [2.9 s]
sage -t -long "libs/singular/function_factory.py"           
**********************************************************************
File "/opt/sage-4.3.1/devel/sage-main/sage/libs/singular/function_factory.py", line 51:
    sage: "std" in sage.list.singular.ff.trait_names()
Exception raised:
    Traceback (most recent call last):
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        "std" in sage.list.singular.ff.trait_names()###line 51:
    sage: "std" in sage.list.singular.ff.trait_names()
    AttributeError: 'module' object has no attribute 'list'
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_function_factory.py
	 [1.5 s]
exit code: 1024
sage -t -long "libs/singular/groebner_strategy.pyx"         
	 [1.5 s]
sage -t -long "libs/singular/option.pyx"                    
**********************************************************************
File "/opt/sage-4.3.1/devel/sage-main/sage/libs/singular/option.pyx", line 340:
    sage: libsingular_verb_options
Expected:
    verbosity options for libSingular (current value 0x02000082)
Got:
    verbosity options for libSingular (current value 0x00002851)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_option.py
	 [2.3 s]
exit code: 1024
sage -t -long "libs/singular/polynomial.pyx"                
	 [1.5 s]
sage -t -long "libs/singular/ring.pyx"                      
	 [1.8 s]
sage -t -long "libs/singular/singular-cdefs.pxi"            
	 [1.4 s]
sage -t -long "libs/singular/singular.pxi"                  
	 [0.1 s]
sage -t -long "libs/singular/singular.pyx"                  
	 [1.6 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "libs/singular/function_factory.py"
	sage -t -long "libs/singular/option.pyx"
Total time for all tests: 14.4 seconds
```



---

Attachment

That's because I uploaded the wrong file somehow. Now it should be the right one.


---

Comment by AlexGhitza created at 2010-01-23 12:09:15

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2010-01-23 12:09:15

This looks good to me.  There are only a few typos that are fixed by the small referee patch.  One last question: in `rings/polynomial/multi_polynomial_ideal.py`, you left a handful of lines commented out.  Was this by purpose, or just an oversight?

Anyway, positive review for the updated spkg and Martin's patch.  If someone can have a quick look at the referee patch, we're done.

In terms of the original motivation for this ticket (what was it already?): the file `rings/polynomial/multi_polynomial_ideal.py` passes long doctests in 45 seconds now on my laptop -- not bad for 582 tests.  I ran it with -verbose and didn't see anything that was outrageous in terms of time.


---

Comment by AlexGhitza created at 2010-01-23 12:10:14

apply after the previous patch


---

Attachment

Alex's patch looks good.


---

Comment by malb created at 2010-01-23 12:30:44

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-01-23 12:36:39

Replying to [comment:29 AlexGhitza]:
>One last question: in `rings/polynomial/multi_polynomial_ideal.py`, you left a handful of 
> lines commented out.  Was this by purpose, or just an oversight?

I was a bit split about leaving the pexpect interface stuff in or throwing it out completely. Singular supports some of its ideal operations over the complex numbers, although they probably don't make much sense there (rounding errors, 0 != 0 etc.). libSingular does not support complex numbers yet (although it is implemented in #7577 and waits for input on a design decision) and thus theoretical we are loosing some functionality. Then again, we are loosing functionality which does not really make much sense (e.g. you want to be careful about computing a Gröbner basis to get the variety of an ideal over CC) This is why I only half hearted removed the pexpect stuff (which supports CC).


---

Comment by mvngu created at 2010-01-24 17:38:54

Merged patches in this order:

 1. [mpoly_ideal_libsingular.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7939/mpoly_ideal_libsingular.patch)
 1. [trac_7939-referee.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7939/trac_7939-referee.patch)

Merged [singular-3-1-0-4-20100120.spkg](http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20100120.spkg) in the standard spkg repository.


---

Comment by mvngu created at 2010-01-24 17:38:54

Resolution: fixed
