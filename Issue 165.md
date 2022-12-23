# Issue 165: pyrex weakref -- implement pyrex weakref support

Issue created by migration from https://trac.sagemath.org/ticket/165

Original creator: was

Original creation time: 2006-10-31 07:53:04

Assignee: somebody

Though Pyrex claims to have weakref support it doesn't, at least not
for Python 2.5, and not with c++ code.  Here are more details.
I need to implement this for SAGE for memory efficiency reasons,
since some rings/fields are implemented in Pyrex:


```
Hi David and Martin,

I just figured out what the deals is with FiniteField_givaro crashing for us.

I am making fields globally unique (so, e.g., arithmetic is faster and so SAGE is
very uniform), so I made Martin's FiniteField_givaro class weak referenceable,
since that way we can make the fields unique, yet if no references point
to one then it is deleted from the cache --- this could be important, e.g., 
if fields have big tables in them, and one does computation involving all fields
up to some big order. 

Anyway, having weakref support for a Pyrex extension calss is not automatic.
According to the Pyrex manual, you just add 

    cdef object __weakref__

to the class definition, and it works.   We'll it wasn't working with
FiniteField_givaro.  I carefully read the docs on weakref support via 
the Python/C API here: http://docs.python.org/ext/weakref-support.html
It says there that the __weakref__ attribute must be explicitly initialized
to NULL, and that this is the responsibility of the author at object
creation.   

I haven't had this problem with Pyrex C-compiled classes, but FiniteField_givaro
is C++, and I have this problem.  I tried explicitly editing the generated
cpp code and adding the initialization to NULL, and re-compiling my code, 
and it worked.  Evidently Pyrex doesn't generate code to initialize the
__weakref__ PyObject* to 0.  And, unfortunately, to use __weakref__ with
Pyrex, you have to use the notation 

    cdef object __weakref__

Once you do that, I think there is no way to write

    self.__weakref__ = NULL

wince NULL is not a Python object, and __weakref__ *has* to be one. 
So basically, I think it is a bug in Pyrex that initialization of
__weakref__ isn't part of the code it generates. 

Even setting self.__weakref__ = None  doesn't help at all. The only
thing that I've found that works is properly setting the __weakref__
C PyObject* pointer to 0.   

Currently Pyrex generates code like this:

    p->__weakref__ = Py_None;

But Py_None is just wrong.  And changing that to NULL does work. 

Thoughts?  I'll probably just have to fix this in Pyrex.  I bet
it won't be too hard. 

Moreover, according to the Python guide, one must call this code
in the destructor:

    if (inst->in_weakreflist != NULL)
        PyObject_ClearWeakRefs((PyObject *) inst);

Pyrex doesn't generate any code that has ClearWekRefs in it, so again
I think it's messed up regarding its support for weak references.

Anyway, it looks like maybe I'm going to have to implement weak reference
support for Pyrex.  This could be difficult... I don't know.  
In the meantime, I'm just going to cache finite fields without
doing the weakref thing, and make a note of it. 

William
```



---

Comment by was created at 2006-11-30 19:09:29


```
I'm trying to understand how (or whether) Pyrex supports weakly-referencable
objects.
 
According to the Pyrex docs, all that is required is to add "cdef object
__weakref__" to the class.  That seems to work only superficially for me.
I am able to create weak refs to instances, but I get mysterious crashes all
over the place if I actually use them.
 
According to this:
http://effbot.org/lib/weakref.html#weak-references-in-extension-types
there are 5 things that need to be done to make an extension type
weak-referenceable:
 
1) include a PyObject* field in the instance structure.
2) initialize it to NULL in the constructor
3) set the tp_weaklistoffset field of the type object
4) add Py_TPFLAGS_HAVE_WEAKREFS to the tp_flags slot
5) call PyObject_ClearWeakRefs in the dealloc function
 
As far as I can tell by looking at the generated C code, Pyrex only does 1)
and 3).  As for 2), it sets __weakref__ to Py_None instead of NULL (maybe
that's OK, I don't know).  It doesn't seem to do 4) or 5) at all.
 
Is this intentional?  I don't know much about writing extension types, so
it's entirely possible that the generated code is fine.  I would just like to
be sure before I spend more time hunting down the cause of the crash.
 
Thanks,
 
Chris Perkins
 }}}


---

Comment by was created at 2006-11-30 19:09:38

Changing component from basic arithmetic to packages.


---

Comment by was created at 2006-11-30 19:09:38

Changing assignee from somebody to was.


---

Comment by was created at 2006-11-30 19:11:27

I think at the least that the Py_None *must* be NULL instead.  I have
crashes because of exactly this, and found that changing the Py_None
to NULL stopped those crashes.  But presumably one should do 4 and 5
as well so that the weakref stuff actually works (rather than just
not crashing).


---

Comment by was created at 2006-12-03 00:12:38

From Greg Ewing:


```
Chris Perkins wrote:
 
> According to this:
> http://effbot.org/lib/weakref.html#weak-references-in-extension-types
> there are 5 things that need to be done to make an extension type
> weak-referenceable:
 
It's quite likely that I haven't done it right. Weak
reference support was only added recently and hasn't
been tested very well yet. I'll look into it.
 
> 4) add Py_TPFLAGS_HAVE_WEAKREFS to the tp_flags slot
 
Looking at object.h in the Python 2.3 distribution, it
seems that Py_TPFLAGS_DEFAULT already includes
Py_TPFLAGS_HAVE_WEAKREFS, which makes me think that
this list of requirements is not quite up to date.
 
Does anyone know more about what the requirements for
weakref support really are in 2.3 and later?
 
--
Greg
 }}}


---

Comment by was created at 2006-12-18 03:17:06

I applied the patch from Peter Johnson, which implements weakref support.


---

Comment by was created at 2006-12-18 03:17:06

Resolution: fixed
