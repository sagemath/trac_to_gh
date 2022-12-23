# Issue 4480: [with patch, needs review] cython dependancy checking is too slow

Issue created by migration from https://trac.sagemath.org/ticket/4480

Original creator: robertwb

Original creation time: 2008-11-09 12:45:56

Assignee: mabshoff

CC:  tornaria

The attached patch builds the entire dependency tree from scratch in 0.6 seconds, and caches it to disk so subsequent dependency checking takes 0.05 seconds to verify. 


---

Attachment


---

Comment by craigcitro created at 2008-11-09 16:08:35

So Gonzalo and I are in the middle of writing the build process in `setup.py`. Luckily, the business of finding includes is the one piece of code we were reusing! So I'll review/merge this into our patch once we're done, which should be today.


---

Attachment

Here we go! So this patch applies on top of `rc0` + the patch at #4500, because it was a needed fix. With this patch in, we've got it all: fast cached dependency checking, parallel calls to Cython, and dozens of small improvements to the build system thrown in, too. I also reorganized `setup.py` and created a `module_list.py` to have the list of extension modules. 

Robert, I've looked at (probably every line of) your code which is now in here -- can you review the rest? I did make small changes to one or two of your functions; in particular, `parse_deps`, I think.

I've run it through some paces, but I'm happy to fix any bugs that pop up.

Credit should go to Rob, Gonzalo, and me.


---

Comment by craigcitro created at 2008-11-13 13:42:14

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-13 13:42:14

Changing assignee from mabshoff to craigcitro.


---

Comment by craigcitro created at 2008-11-13 13:42:25

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-13 16:43:41

I am giving a positive review to all the changes that move the extensions to the new file. But we need a formal review for Robert's changes and since Craig was involved here, too, I am not so sure who would review what portion of those.

I am testing a vanilla tree with the fixes here and #4500 applied, so I should be able to at least see if everything works as expected when combining all pieces into a virgin  build.

Thoughts?

Cheers,

Michael


---

Comment by robertwb created at 2008-11-13 18:03:01

I'll look at this today. I only apply the last patch, right?


---

Comment by mabshoff created at 2008-11-13 18:05:26

Yes, but you should also apply 

http://trac.sagemath.org/sage_trac/attachment/ticket/4500/trac-4500.patch

in this context. I found an issue when building from vanilla with both the last patch here and trac-4500.patch applied and there is an issue that I mentioned on the other ticket with a work around fix, but I am not sure if it is the correct fix. It does work, but that does not mean that it is either elegant or proper.

Cheers,

Michael


---

Comment by robertwb created at 2008-11-13 22:27:10

It looks good to me...this is a much needed cleanup! 

I think mabshoff's fix proposed #4500 is good, and should also be applied.


---

Comment by craigcitro created at 2008-11-13 22:36:04

Ditto on mabshoff's fix at #4500.


---

Comment by craigcitro created at 2008-11-14 00:31:51

In addition to mabshoff's fix at #4500, I think we should add the following:


```
diff -r c543000d6447 setup.py
--- a/setup.py  Thu Nov 13 05:32:07 2008 -0800
+++ b/setup.py  Thu Nov 13 16:26:41 2008 -0800
@@ -13,11 +13,11 @@
 else:
     sdist = False
 
-# uncomment to turn warnings off
-# import distutils.sysconfig
-# NO_WARN = True
-# if NO_WARN and distutils.sysconfig.get_config_var('CC').startswith("gcc"):
-#     extra_compile_args = ['-w']
+# comment these four lines out to turn on warnings from gcc
+import distutils.sysconfig
+NO_WARN = True
+if NO_WARN and distutils.sysconfig.get_config_var('CC').startswith("gcc"):
+    extra_compile_args = ['-w']
 
 if not os.environ.has_key('SAGE_ROOT'):
     print "    ERROR: The environment variable SAGE_ROOT must be defined."
```


This just turns warnings back off -- as William points out, it's a lot of output for the unsuspecting. Michael and I had discussed this when we changed it, and it would be good to sit down and actually look at the warnings once to see if anything interesting is being turned up. In the interim, though, let's not spam. ;)


---

Comment by robertwb created at 2008-11-14 01:17:35

I'm OK with that.


---

Comment by mabshoff created at 2008-11-14 03:38:38

Can somebody post a cumulative patch here?

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 04:02:40

Resolution: fixed


---

Attachment

Merged trac-4480-cumulative.patch in Sage 3.2.rc1


---

Comment by craigcitro created at 2008-11-14 05:02:21

okay, maybe it only feels like part 18. :)


---

Attachment

Merged trac-4480-pt18.patch in Sage 3.2.rc1.

Thanks Craig.

Cheers,

Michael
