# Issue 9482: implicit_plot3d gives "Out of memory allocating triangulation" when plotting an empty surface

archive/issues_009482.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @kcrisman\n\nWhen you construct an implicit_plot3d that doesn't actually contain any surface, you get a `MemoryError` (because it tries to allocate 0 memory to hold the vertices and faces, gets a NULL pointer, and decides that's an out-of-memory condition).\n\nHere's one example:\n\n```\nsage: implicit_plot3d(x*x + y*y + z*z - 5000, (x, -5, 5), (y, -5, 5), (z, -5, 5))\n```\n... long traceback, ending:\n\n```\n/home/cwitty/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_surface.so in sage.plot.plot3d.implicit_surface.ImplicitSurface.jmol_repr (sage/plot/plot3d/implicit_surface.c:10893)()\n\n/home/cwitty/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_surface.so in sage.plot.plot3d.implicit_surface.ImplicitSurface.triangulate (sage/plot/plot3d/implicit_surface.c:11290)()\n\n/home/cwitty/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.realloc (sage/plot/plot3d/index_face_set.c:3662)()\n\nMemoryError: Out of memory allocating triangulation for <type 'sage.plot.plot3d.implicit_surface.ImplicitSurface'>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9482\n\n",
    "created_at": "2010-07-12T17:07:10Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "implicit_plot3d gives \"Out of memory allocating triangulation\" when plotting an empty surface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9482",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

CC:  @kcrisman

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

Issue created by migration from https://trac.sagemath.org/ticket/9482





---

archive/issue_comments_090884.json:
```json
{
    "body": "Nice catch, Carl!  I had been curious about these out of memory errors, but never had the chance to look into it.",
    "created_at": "2010-07-12T17:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90884",
    "user": "https://github.com/mwhansen"
}
```

Nice catch, Carl!  I had been curious about these out of memory errors, but never had the chance to look into it.



---

archive/issue_comments_090885.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-18T02:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90885",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090886.json:
```json
{
    "body": "Attachment [trac_9482-implicit-plot-out-of-memory.patch](tarball://root/attachments/some-uuid/ticket9482/trac_9482-implicit-plot-out-of-memory.patch) by cwitty created at 2010-07-18 02:51:34\n\nThe patch prevents the above error, all doctests pass.\n\nJMOL doesn't like the resulting file; it gives errors about #faces must be positive, or something.  My vote would be to fix that error when we try to create the JMOL-formatted file.  (We could raise an error here, but then sum([implicit_plot3d(...) for i in range(10)]) might break unnecessarily.)",
    "created_at": "2010-07-18T02:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90886",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac_9482-implicit-plot-out-of-memory.patch](tarball://root/attachments/some-uuid/ticket9482/trac_9482-implicit-plot-out-of-memory.patch) by cwitty created at 2010-07-18 02:51:34

The patch prevents the above error, all doctests pass.

JMOL doesn't like the resulting file; it gives errors about #faces must be positive, or something.  My vote would be to fix that error when we try to create the JMOL-formatted file.  (We could raise an error here, but then sum([implicit_plot3d(...) for i in range(10)]) might break unnecessarily.)



---

archive/issue_comments_090887.json:
```json
{
    "body": "I think someone who knows Cython/C well should give a final review on how the NULL pointer thing should work, but the logic of the new code makes sense and it seems to not break anything on my computers.\n\nHowever, on my systems (Mac OS X 10.4 and OS X 10.6) I do NOT get any traceback with the original code.  In fact, on the 10.6 system I even get a Jmol applet, just with no graphic, in both circumstances.  What's up with that?",
    "created_at": "2010-08-06T00:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90887",
    "user": "https://github.com/kcrisman"
}
```

I think someone who knows Cython/C well should give a final review on how the NULL pointer thing should work, but the logic of the new code makes sense and it seems to not break anything on my computers.

However, on my systems (Mac OS X 10.4 and OS X 10.6) I do NOT get any traceback with the original code.  In fact, on the 10.6 system I even get a Jmol applet, just with no graphic, in both circumstances.  What's up with that?



---

archive/issue_comments_090888.json:
```json
{
    "body": "According to \"man malloc\":\n\n  If  size is 0, then malloc()\n  returns either NULL, or a unique pointer value that can later  be  \n  successfully passed to free().\n\nI guess under Linux malloc(0) returns NULL and under OSX it returns \"a unique pointer value that can later be successfully passed to free()\".",
    "created_at": "2010-08-06T02:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90888",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

According to "man malloc":

  If  size is 0, then malloc()
  returns either NULL, or a unique pointer value that can later  be  
  successfully passed to free().

I guess under Linux malloc(0) returns NULL and under OSX it returns "a unique pointer value that can later be successfully passed to free()".



---

archive/issue_comments_090889.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-06T14:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90889",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090890.json:
```json
{
    "body": "Replying to [comment:5 cwitty]:\n> According to \"man malloc\":\n> \n>   If  size is 0, then malloc()\n>   returns either NULL, or a unique pointer value that can later  be  \n>   successfully passed to free().\n> \n> I guess under Linux malloc(0) returns NULL and under OSX it returns \"a unique pointer value that can later be successfully passed to free()\".\n\n\nInterestingly, the Mac malloc man page is different.\n\n```\nThe malloc() function allocates size bytes of memory and returns a pointer to the allocated memory.\n<snip>\nIf successful, calloc(), malloc(), realloc(), reallocf(), and valloc() functions return a pointer to\n     allocated memory.  If there is an error, they return a NULL pointer and set errno to ENOMEM.\n```\n\nAnyway, a good [FAQ](http://c-faq.com/ansi/malloc0.html) points out \"Portable code must either take care not to call malloc(0), or be prepared for the possibility of a null return.\"  So I think your changes make sense.  \n\nIncidentally, I am having trouble finding the following:\n1. Definition of `point_c` - it isn't in `point_c.pxi` nor in the ext directory, as far as I can tell.\n2. Online references to this angle bracket asterisk notation `<point_c *>` and friends.  None of the search engines take these characters into account, and neither of my C tutorials have this notation.  I think I get what it does, but it would be nice to know for sure.\n\nFinal result: this is an improvement over the previous situation, but for positive review and inclusion, one should open a ticket for the Jmol problem you indicate.   I can't figure out exactly what you mean by that, though I do get\n\n```\nsage: G.jmol_repr(G.default_render_params())\n<snip>\nAttributeError: 'RenderParams' object has no attribute 'output_archive'\n```\nif that's what you are referring to.  I get that other places, too, though I have no examples currently.",
    "created_at": "2010-08-06T14:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90890",
    "user": "https://github.com/kcrisman"
}
```

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

archive/issue_comments_090891.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9482#issuecomment-90891",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023509.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:42:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9482",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9482#event-23509"
}
```
