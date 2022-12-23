# Issue 9482: implicit_plot3d gives "Out of memory allocating triangulation" when plotting an empty surface

Issue created by migration from https://trac.sagemath.org/ticket/9482

Original creator: cwitty

Original creation time: 2010-07-12 17:07:10

Assignee: cwitty

CC:  kcrisman

When you construct an implicit_plot3d that doesn't actually contain any surface, you get a `MemoryError` (because it tries to allocate 0 memory to hold the vertices and faces, gets a NULL pointer, and decides that's an out-of-memory condition).

Here's one example:


```
sage: implicit_plot3d(x*x + y*y + z*z - 5000, (x, -5, 5), (y, -5, 5), (z, -5, 5))
```

... long traceback, ending:

```
/home/cwitty/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_surface.so in sage.plot.plot3d.implicit_surface.ImplicitSurface.jmol_repr (sage/plot/plot3d/implicit_surface.c:10893)()

/home/cwitty/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_surface.so in sage.plot.plot3d.implicit_surface.ImplicitSurface.triangulate (sage/plot/plot3d/implicit_surface.c:11290)()

/home/cwitty/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.realloc (sage/plot/plot3d/index_face_set.c:3662)()

MemoryError: Out of memory allocating triangulation for <type 'sage.plot.plot3d.implicit_surface.ImplicitSurface'>
```



---

Comment by mhansen created at 2010-07-12 17:31:32

Nice catch, Carl!  I had been curious about these out of memory errors, but never had the chance to look into it.


---

Comment by cwitty created at 2010-07-18 02:51:34

Changing status from new to needs_review.


---

Attachment

The patch prevents the above error, all doctests pass.

JMOL doesn't like the resulting file; it gives errors about #faces must be positive, or something.  My vote would be to fix that error when we try to create the JMOL-formatted file.  (We could raise an error here, but then sum([implicit_plot3d(...) for i in range(10)]) might break unnecessarily.)


---

Comment by kcrisman created at 2010-08-06 00:49:50

I think someone who knows Cython/C well should give a final review on how the NULL pointer thing should work, but the logic of the new code makes sense and it seems to not break anything on my computers.

However, on my systems (Mac OS X 10.4 and OS X 10.6) I do NOT get any traceback with the original code.  In fact, on the 10.6 system I even get a Jmol applet, just with no graphic, in both circumstances.  What's up with that?


---

Comment by cwitty created at 2010-08-06 02:22:25

According to "man malloc":

  If  size is 0, then malloc()
  returns either NULL, or a unique pointer value that can later  be  
  successfully passed to free().

I guess under Linux malloc(0) returns NULL and under OSX it returns "a unique pointer value that can later be successfully passed to free()".


---

Comment by kcrisman created at 2010-08-06 14:00:30

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-08-06 14:00:30

Replying to [comment:5 cwitty]:
> According to "man malloc":
> 
>   If  size is 0, then malloc()
>   returns either NULL, or a unique pointer value that can later  be  
>   successfully passed to free().
> 
> I guess under Linux malloc(0) returns NULL and under OSX it returns "a unique pointer value that can later be successfully passed to free()".

Interestingly, the Mac malloc man page is different.

```
The malloc() function allocates size bytes of memory and returns a pointer to the allocated memory.
<snip>
If successful, calloc(), malloc(), realloc(), reallocf(), and valloc() functions return a pointer to
     allocated memory.  If there is an error, they return a NULL pointer and set errno to ENOMEM.
```


Anyway, a good [FAQ](http://c-faq.com/ansi/malloc0.html) points out "Portable code must either take care not to call malloc(0), or be prepared for the possibility of a null return."  So I think your changes make sense.  

Incidentally, I am having trouble finding the following:
1. Definition of `point_c` - it isn't in `point_c.pxi` nor in the ext directory, as far as I can tell.
2. Online references to this angle bracket asterisk notation `<point_c *>` and friends.  None of the search engines take these characters into account, and neither of my C tutorials have this notation.  I think I get what it does, but it would be nice to know for sure.

Final result: this is an improvement over the previous situation, but for positive review and inclusion, one should open a ticket for the Jmol problem you indicate.   I can't figure out exactly what you mean by that, though I do get

```
sage: G.jmol_repr(G.default_render_params())
<snip>
AttributeError: 'RenderParams' object has no attribute 'output_archive'
```

if that's what you are referring to.  I get that other places, too, though I have no examples currently.


---

Comment by mpatel created at 2010-08-09 09:42:27

Resolution: fixed
