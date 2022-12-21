# Issue 7916: change conjugate(X) to try X.conjugate()  [[this is easy!!]]

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-13 05:00:37

Assignee: burcin

CC:  rossk


```
On Tue, Jan 12, 2010 at 8:36 PM, jtyard <> wrote:
> Hi,
>
> I don't know if this counts as a bug, so sorry if I'm posting this to
> the wrong list.  Say I define a cyclotomic field in Sage as follows:
>
> sage: Q3 = CyclotomicField(3)
> sage: z3 = Q3.0
>
> Then Sage can compute the complex conjugate independent of an
> embedding into the complexes:
>
> sage: z3.conjugate()
> -zeta3 - 1
>
> But I get a different answer by typing:
>
> sage: conjugate(z3)
> conjugate(e^(2/3*I*pi))
>
> Wouldn't it make sense for these to do the same thing?  Another
> difference comes up as follows:
>
> sage: Q2.<s> = QuadraticField(-2)
> sage: s.conjugate()
> -s
> sage: conjugate(s)
> -I*sqrt(2)
>
> Yet, the problem doesn't exist with this slightly different
> definition:
>
> sage: QQ2.<ss> = QQ[sqrt(-2)]
> sage: ss.conjugate()
> -a
> sage: conjugate(ss)
> -a

Yes, I agree that this is a bug.  
What is happening is that the *symbolic* conjugate function is coercing its input X to the symbolic ring SR before applying itself.  It would be much better to test if X has a .conjugate method, and if so return that; if not, then return SR(X).conjugate().

Here's the beginning of the course code for conjugate(X):

sage: conjugate.__call__??
        # we want to convert the result to the original parent if the input
        # is not exact, so we store the parent here
        org_parent = parent(args[0])
```



---

Attachment


---

Comment by burcin created at 2010-01-17 11:39:50

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-01-18 02:20:38

Does [trac_7916-same_name_method.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.patch) depend on anything? I got one hunk failure when applying [trac_7916-same_name_method.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.patch) on top of Sage 4.3.1.rc0:

```
[mvngu`@`mod sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.1.rc0-7916/devel/sage-main
[mvngu`@`mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7916/trac_7916-same_name_method.patch
adding trac_7916-same_name_method.patch to series file
[mvngu`@`mod sage-main]$ hg qpush
applying trac_7916-same_name_method.patch
patching file sage/symbolic/function.pyx
Hunk #1 FAILED at 550
1 out of 1 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7916-same_name_method.patch
[mvngu`@`mod sage-main]$ cat sage/symbolic/function.pyx.rej
--- function.pyx
+++ function.pyx
`@``@` -551,10 +551,30 `@``@`
             # we should never end up here
             raise ValueError, "cannot read pickle"
 
-    def __call__(self, *args, coerce=True, hold=False):
+    def __call__(self, *args, coerce=True, hold=False,
+            dont_call_method_on_arg=False):
+        """
+        Evaluate this function on the given arguments and return the result.
+
+        EXAMPLES::
+
+            sage: exp(5)
+            e^5
+            sage: gamma(15)
+            87178291200
+        """
         # we want to convert the result to the original parent if the input
         # is not exact, so we store the parent here
         org_parent = parent_c(args[0])
+        
+        # if there is only one argument, and the argument has an attribute
+        # with the same name as this function, try to call it to get the result
+        # The argument dont_call_method_on_arg is used to prevent infinite loops
+        # when .exp(), .log(), etc. methods call this symbolic function on 
+        # themselves
+        if len(args) == 1 and not hold and not dont_call_method_on_arg and \
+                hasattr(args[0], self._name):
+            return getattr(args[0], self._name)()
 
         res = super(GinacFunction, self).__call__(*args, coerce=coerce,
                 hold=hold)
```



---

Comment by burcin created at 2010-01-18 04:14:58

Sorry for the inconvenience. My patch queue contains all the fixes from yesterday. I forgot to check dependencies.

This depends on #7822. You can apply the patch there now, it doesn't depend on any changes in pynac. The timing will be better with the new pynac spkg though.


---

Comment by burcin created at 2010-01-19 13:11:34

slightly faster - apply only this patch


---

Attachment

attachment:trac_7916-same_name_method.take2.patch is slightly faster than the previous one.


---

Comment by kcrisman created at 2010-01-28 21:25:22

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-28 21:25:22

A good solution.  The timing changes seem to be unavoidable, given that we don't want conjugate(e^(2/3*I*pi)) as the result, and they seem identical otherwise:

```
sage: %timeit z3.conjugate()
625 loops, best of 3: 469 µs per loop
sage: %timeit conjugate(z3)
625 loops, best of 3: 469 µs per loop
```



---

Comment by mvngu created at 2010-02-18 21:47:05

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 21:47:05

Merged [trac_7916-same_name_method.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.take2.patch).
