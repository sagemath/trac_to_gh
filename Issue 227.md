# Issue 227: cython: should use NULL instead of 0

archive/issues_000227.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\na.c.junker@gmail.com\n\n  While I understand that it's best for the Pyrex code to be the main\nreference, and for the C code to be re-generated at compilation\ntime, I can see situations where that won't happen - for example if\ngcc is an admin-supported compiler, and thus part of some automated\nbuild system, by pyrexc is not. The generated C might then be used\nas the reference, and portions could be extracted and used elsewhere,\nperhaps without proper prototyping. Or perhaps there is some new\nversion of a library, and the functions you are using are no longer\ndeclared in the header files you've included - this would be picked up\nby pyrexc, but not by the automated gcc build system.\n \n## \n\n  Now suppose that you have some function that takes a pointer, and\nthe generated code passes it a 0 instead of a NULL. In the absence\nof a prototype, the 0 is an integer by default, whereas NULL is a void *.\nSuppose further that you're compiling on a platform on which integers\nand pointers have different storage sizes, which is becoming more\ncommon as memory sizes increase while integers are often left at\n32 bits. This scenario would lead to corruption of the stack, in a way\nthat will be hard to find - especially if you aren't aware of the storage\nsize mismatch - though easy to fix.\n \n  While it is somebody else's stupid mistake that causes the problem,\nit is my code that would get a bad reputation as a result.\n \n  I do realize that this is a pedantic point here, but there is a difference\nbetween 0 and NULL, and there is a \"correct\" way to do this, and since\nPyrex already recognizes that NULL is a special case, the least it could\ndo would be to preserve it.\n \nThanks.\n \nOn 1/26/07, Greg Ewing <greg.ewing@canterbury.ac.nz> wrote:\n> Adapted Cat wrote:\n> > Even though NULL is a reserved word in Pyrex, the generated C\n> > code uses 0.\n> >\n> > Could the NULL be preserved in the C code, please?\n>  \n> Why? The only situation I know of where it could make\n> a difference is if you were using old K&R-style function\n> headers, which Pyrex doesn't.\n>  \n> > Also, it seems that there is no way to declare a C array pre-filled\n> > with directly in Pyrex.\n>  \n> That's true. It's on my list, but it doesn't have a\n> very high priority at the moment.\n>  \n> --\n> Greg\n>  \n>  \n \n_______________________________________________\nPyrex mailing list\nPyrex@lists.copyleft.no\nhttp://lists.copyleft.no/mailman/listinfo/pyrex\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/227\n\n",
    "closed_at": "2007-08-29T02:09:30Z",
    "created_at": "2007-01-28T20:27:53Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "cython: should use NULL instead of 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/227",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
a.c.junker@gmail.com

  While I understand that it's best for the Pyrex code to be the main
reference, and for the C code to be re-generated at compilation
time, I can see situations where that won't happen - for example if
gcc is an admin-supported compiler, and thus part of some automated
build system, by pyrexc is not. The generated C might then be used
as the reference, and portions could be extracted and used elsewhere,
perhaps without proper prototyping. Or perhaps there is some new
version of a library, and the functions you are using are no longer
declared in the header files you've included - this would be picked up
by pyrexc, but not by the automated gcc build system.
 
## 

  Now suppose that you have some function that takes a pointer, and
the generated code passes it a 0 instead of a NULL. In the absence
of a prototype, the 0 is an integer by default, whereas NULL is a void *.
Suppose further that you're compiling on a platform on which integers
and pointers have different storage sizes, which is becoming more
common as memory sizes increase while integers are often left at
32 bits. This scenario would lead to corruption of the stack, in a way
that will be hard to find - especially if you aren't aware of the storage
size mismatch - though easy to fix.
 
  While it is somebody else's stupid mistake that causes the problem,
it is my code that would get a bad reputation as a result.
 
  I do realize that this is a pedantic point here, but there is a difference
between 0 and NULL, and there is a "correct" way to do this, and since
Pyrex already recognizes that NULL is a special case, the least it could
do would be to preserve it.
 
Thanks.
 
On 1/26/07, Greg Ewing <greg.ewing@canterbury.ac.nz> wrote:
> Adapted Cat wrote:
> > Even though NULL is a reserved word in Pyrex, the generated C
> > code uses 0.
> >
> > Could the NULL be preserved in the C code, please?
>  
> Why? The only situation I know of where it could make
> a difference is if you were using old K&R-style function
> headers, which Pyrex doesn't.
>  
> > Also, it seems that there is no way to declare a C array pre-filled
> > with directly in Pyrex.
>  
> That's true. It's on my list, but it doesn't have a
> very high priority at the moment.
>  
> --
> Greg
>  
>  
 
_______________________________________________
Pyrex mailing list
Pyrex@lists.copyleft.no
http://lists.copyleft.no/mailman/listinfo/pyrex
```

Issue created by migration from https://trac.sagemath.org/ticket/227





---

archive/issue_events_000466.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T21:24:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/227#event-466"
}
```



---

archive/issue_comments_001006.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-18T23:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/227#issuecomment-1006",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001007.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-08-18T23:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/227#issuecomment-1007",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_events_000467.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T02:02:54Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/227#event-467"
}
```



---

archive/issue_events_000468.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T02:02:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/227#event-468"
}
```



---

archive/issue_events_000469.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T02:03:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/227#event-469"
}
```



---

archive/issue_events_000470.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T02:03:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/227#event-470"
}
```



---

archive/issue_comments_001008.json:
```json
{
    "body": "This input code\n\n```\n%cython\n\ncdef void* bar():\n    return NULL\n```\n\ngenerates this output code\n\n```\nstatic void (*__pyx_f_61_home_was_sage_notebook_worksheets_admin_34_code_sage4_spyx_0_bar(void)) {\n  void (*__pyx_r);\n\n  /* \"/home/was/.sage/temp/ubuntu/32525/spyx/_home_was_sage_notebook_worksheets_admin_34_code_sage4_spyx/_home_was_sage_not\nebook_worksheets_admin_34_code_sage4_spyx_0.pyx\":7\n * include \"cdefs.pxi\"\n * cdef void* bar():\n *     return NULL             # <<<<<<<<<<<<<<\n */\n  __pyx_r = NULL;\n  goto __pyx_L0;\n\n  __pyx_L0:;\n  return __pyx_r;\n}\n```\n\nSo this issue is fixed.",
    "created_at": "2007-08-29T02:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/227#issuecomment-1008",
    "user": "https://github.com/williamstein"
}
```

This input code

```
%cython

cdef void* bar():
    return NULL
```

generates this output code

```
static void (*__pyx_f_61_home_was_sage_notebook_worksheets_admin_34_code_sage4_spyx_0_bar(void)) {
  void (*__pyx_r);

  /* "/home/was/.sage/temp/ubuntu/32525/spyx/_home_was_sage_notebook_worksheets_admin_34_code_sage4_spyx/_home_was_sage_not
ebook_worksheets_admin_34_code_sage4_spyx_0.pyx":7
 * include "cdefs.pxi"
 * cdef void* bar():
 *     return NULL             # <<<<<<<<<<<<<<
 */
  __pyx_r = NULL;
  goto __pyx_L0;

  __pyx_L0:;
  return __pyx_r;
}
```

So this issue is fixed.



---

archive/issue_comments_001009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T02:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/227#issuecomment-1009",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000471.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T02:09:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/227",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/227#event-471"
}
```
