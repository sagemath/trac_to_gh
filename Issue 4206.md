# Issue 4206: convert RDF and CDF vectors to use numpy

archive/issues_004206.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4206\n\n",
    "created_at": "2008-09-27T09:39:25Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "convert RDF and CDF vectors to use numpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4206",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/4206





---

archive/issue_comments_030465.json:
```json
{
    "body": "This is needed after #4205:\n\n```\n[02:20am] mabshoff: mk\n[02:21am] jason-:         cdef ndarray _n = numpy.array(list(self),dtype=numpy.dtype('float64'))\n[02:21am] jason-: #        temp = PyArray_SimpleNew(1, dims, NPY_DOUBLE)\n[02:21am] jason-: #        _n = temp\n[02:21am] jason-: #        for i from 0<=i<_V.v.size:\n[02:21am] jason-: #            _n[i] = float(_V.v.data[i])\n[02:21am] jason-: comment from that line down to the end of the function\n[02:21am] jason-: and replace it with the above numpy.array line.\n[02:21am] jason-: oh, and add import numpy above that.\n<SNIP>\n[02:24am] mabshoff: sage: sage: v = vector(RDF,4,range(4))\n[02:24am] mabshoff: sage: v.numpy()\n[02:24am] mabshoff: array([ 0.,  1.,  2.,  3.])\n[02:24am] mabshoff: sage: v\n[02:24am] mabshoff: (0.0, 1.0, 2.0, 3.0)\n[02:24am] mabshoff: so that works now\n[02:24am] jason-: can I just replace it?\n[02:24am] jason-: it's going to be really slow, but it works\n[02:25am] mabshoff: well, I guess for now we can live with that.\n[02:25am] jason-: well, I don't know how much slower\n[02:25am] jason-: can you do a timeit test?\n[02:25am] mabshoff: sure, in a minute\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T09:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is needed after #4205:

```
[02:20am] mabshoff: mk
[02:21am] jason-:         cdef ndarray _n = numpy.array(list(self),dtype=numpy.dtype('float64'))
[02:21am] jason-: #        temp = PyArray_SimpleNew(1, dims, NPY_DOUBLE)
[02:21am] jason-: #        _n = temp
[02:21am] jason-: #        for i from 0<=i<_V.v.size:
[02:21am] jason-: #            _n[i] = float(_V.v.data[i])
[02:21am] jason-: comment from that line down to the end of the function
[02:21am] jason-: and replace it with the above numpy.array line.
[02:21am] jason-: oh, and add import numpy above that.
<SNIP>
[02:24am] mabshoff: sage: sage: v = vector(RDF,4,range(4))
[02:24am] mabshoff: sage: v.numpy()
[02:24am] mabshoff: array([ 0.,  1.,  2.,  3.])
[02:24am] mabshoff: sage: v
[02:24am] mabshoff: (0.0, 1.0, 2.0, 3.0)
[02:24am] mabshoff: so that works now
[02:24am] jason-: can I just replace it?
[02:24am] jason-: it's going to be really slow, but it works
[02:25am] mabshoff: well, I guess for now we can live with that.
[02:25am] jason-: well, I don't know how much slower
[02:25am] jason-: can you do a timeit test?
[02:25am] mabshoff: sure, in a minute
```

Cheers,

Michael



---

archive/issue_comments_030466.json:
```json
{
    "body": "And this is needed in \n* cdef class ComplexDoubleVectorSpaceElement(free_module_element.FreeModuleElement)\n* cdef class RealDoubleVectorSpaceElement(free_module_element.FreeModuleElement)\n\nLook for the two comments like:\n\n```\n        # We should be using the C API here.  When upgrading to 1.2.0,\n        # we didn't get the C API to work for some reason on sage.math\n        # (64-bit) even though it worked fine on a 32-bit box.\n        cdef ndarray _n = numpy.array(list(self),dtype=numpy.dtype('float64'))\n```",
    "created_at": "2008-09-27T09:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And this is needed in 
* cdef class ComplexDoubleVectorSpaceElement(free_module_element.FreeModuleElement)
* cdef class RealDoubleVectorSpaceElement(free_module_element.FreeModuleElement)

Look for the two comments like:

```
        # We should be using the C API here.  When upgrading to 1.2.0,
        # we didn't get the C API to work for some reason on sage.math
        # (64-bit) even though it worked fine on a 32-bit box.
        cdef ndarray _n = numpy.array(list(self),dtype=numpy.dtype('float64'))
```



---

archive/issue_comments_030467.json:
```json
{
    "body": "I've attached some rough initial work based on the patches to RDF and CDF matrices.  Probably none of the docstrings are correct.  This patch will generate C code (in Sage 3.1.4), but won't compile.",
    "created_at": "2008-10-25T08:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30467",
    "user": "https://github.com/jasongrout"
}
```

I've attached some rough initial work based on the patches to RDF and CDF matrices.  Probably none of the docstrings are correct.  This patch will generate C code (in Sage 3.1.4), but won't compile.



---

archive/issue_comments_030468.json:
```json
{
    "body": "Updated code; now sage builds and passes all doctests in the old *_double_vector.pyx files.\n\nTODO: \n* Make the real_roots and timeseries files use the Cython buffer interface\n* Update doctests to be for the vector code\n* One last runthrough to make sure the code looks reasonable\n* doctest everything.",
    "created_at": "2008-11-11T09:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30468",
    "user": "https://github.com/jasongrout"
}
```

Updated code; now sage builds and passes all doctests in the old *_double_vector.pyx files.

TODO: 
* Make the real_roots and timeseries files use the Cython buffer interface
* Update doctests to be for the vector code
* One last runthrough to make sure the code looks reasonable
* doctest everything.



---

archive/issue_comments_030469.json:
```json
{
    "body": "> Make the real_roots and timeseries files use the Cython buffer interface \n\n\nIf you do that to timeseries, please do not degrade performance at all.  The whole point of timeseries is \"blazing speed\" -- many of the functions are easily 10-15 times faster than the same functions in matlab/numpy, and part of this is because of using a simple data structure (double*).",
    "created_at": "2008-11-11T20:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30469",
    "user": "https://github.com/williamstein"
}
```

> Make the real_roots and timeseries files use the Cython buffer interface 


If you do that to timeseries, please do not degrade performance at all.  The whole point of timeseries is "blazing speed" -- many of the functions are easily 10-15 times faster than the same functions in matlab/numpy, and part of this is because of using a simple data structure (double*).



---

archive/issue_comments_030470.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> > Make the real_roots and timeseries files use the Cython buffer interface \n\n> \n> If you do that to timeseries, please do not degrade performance at all.  The whole point of timeseries is \"blazing speed\" -- many of the functions are easily 10-15 times faster than the same functions in matlab/numpy, and part of this is because of using a simple data structure (double*). \n\n\nIf I understand this patch correctly the buffer interface in Cython to numpy avoids copying data. Since the data are stored as double* there should be a small increase in performance and the use of the buffer interface does not imply that functionality gets moved from something else to numpy.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-11T20:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:6 was]:
> > Make the real_roots and timeseries files use the Cython buffer interface 

> 
> If you do that to timeseries, please do not degrade performance at all.  The whole point of timeseries is "blazing speed" -- many of the functions are easily 10-15 times faster than the same functions in matlab/numpy, and part of this is because of using a simple data structure (double*). 


If I understand this patch correctly the buffer interface in Cython to numpy avoids copying data. Since the data are stored as double* there should be a small increase in performance and the use of the buffer interface does not imply that functionality gets moved from something else to numpy.

Cheers,

Michael



---

archive/issue_comments_030471.json:
```json
{
    "body": "Michael, \n\nYep, that's the idea.  If the buffer interface doesn't work, then just work with the raw double C array that underlies a (sufficiently nice) numpy array.\n\nThe patch currently does horrible performance things with timeseries just to get it to not depend on gsl.  The final version will access the numpy double array either using the buffer interface (preferably) or with straight C.",
    "created_at": "2008-11-11T21:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30471",
    "user": "https://github.com/jasongrout"
}
```

Michael, 

Yep, that's the idea.  If the buffer interface doesn't work, then just work with the raw double C array that underlies a (sufficiently nice) numpy array.

The patch currently does horrible performance things with timeseries just to get it to not depend on gsl.  The final version will access the numpy double array either using the buffer interface (preferably) or with straight C.



---

archive/issue_comments_030472.json:
```json
{
    "body": "I guess I should make clear that the only reason I am touching the time series and the real roots files are because they rather heavily used the GSL structures underlying RDF and CDF vectors.  If the authors want to change it to numpy or to their own double array structure, they are more than welcome.  Needless to say, if I end up doing it, we should call for the original authors' comments before putting this patch in.",
    "created_at": "2008-11-11T21:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30472",
    "user": "https://github.com/jasongrout"
}
```

I guess I should make clear that the only reason I am touching the time series and the real roots files are because they rather heavily used the GSL structures underlying RDF and CDF vectors.  If the authors want to change it to numpy or to their own double array structure, they are more than welcome.  Needless to say, if I end up doing it, we should call for the original authors' comments before putting this patch in.



---

archive/issue_comments_030473.json:
```json
{
    "body": "This is pretty painful to see.  Basically your patch will make create a real_double_dense vector from a TimeSeries extremely slow.   (I.e., the function .vector() becomes way slower.) Fortunately, it appears I don't use that function anywhere else in the file.  It would be good for you to either fix this, or put\na large WARNING in the docstring for that function that it is slow and a pointer to a trac ticket about fixing that problem.  I say this because one of the design constraints (clearly stated I hope in the time_series.pyx file) is that every function in there be nearly \"optimal\". \n\n```\n220\t \t        cdef RealDoubleVectorSpaceElement x = RealDoubleVectorSpaceElement(V, 0) \n221\t \t        memcpy(x.v.data, self._values, sizeof(double)*self._length) \n \t222\t        cdef Vector_real_double_dense x = Vector_real_double_dense(V, 0) \n \t223\t        cdef int i \n \t224\t        for i from 0 <= i < self._length: \n \t225\t            x.set_unsafe(i, self._values[i]) \n \t226\t#        cdef int i \n \t227\t#        for i from 0<=i<self._length: \n \t228\t#            x.set_unsafe(i,self._values[i]) \n \t229\t \n \t230\t#        memcpy(x._matrix_numpy.data, self._values, sizeof(double)*self._length) \n```",
    "created_at": "2008-11-12T03:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30473",
    "user": "https://github.com/williamstein"
}
```

This is pretty painful to see.  Basically your patch will make create a real_double_dense vector from a TimeSeries extremely slow.   (I.e., the function .vector() becomes way slower.) Fortunately, it appears I don't use that function anywhere else in the file.  It would be good for you to either fix this, or put
a large WARNING in the docstring for that function that it is slow and a pointer to a trac ticket about fixing that problem.  I say this because one of the design constraints (clearly stated I hope in the time_series.pyx file) is that every function in there be nearly "optimal". 

```
220	 	        cdef RealDoubleVectorSpaceElement x = RealDoubleVectorSpaceElement(V, 0) 
221	 	        memcpy(x.v.data, self._values, sizeof(double)*self._length) 
 	222	        cdef Vector_real_double_dense x = Vector_real_double_dense(V, 0) 
 	223	        cdef int i 
 	224	        for i from 0 <= i < self._length: 
 	225	            x.set_unsafe(i, self._values[i]) 
 	226	#        cdef int i 
 	227	#        for i from 0<=i<self._length: 
 	228	#            x.set_unsafe(i,self._values[i]) 
 	229	 
 	230	#        memcpy(x._matrix_numpy.data, self._values, sizeof(double)*self._length) 
```



---

archive/issue_comments_030474.json:
```json
{
    "body": "I guess the other thing I should make perfectly clear is that the changes I made to the timeseries and the real_roots files were *only* to get `sage -br` to work so that I could concentrate on the doctests in the vector code.  If the authors don't beat me to it, I plan to go through each of those changes and make them optimally access the numpy array (which should be just about as fast as the previous C double array access to the GSL vector).  That's why the patch is \"needs work\"--it's a work-in-progress that I wanted to post to trac to (a) back up and (b) expose to a wider audience.\n\nThat said, I really appreciate your comments.  I'll pay particular attention to optimizing these (if someone else doesn't beat me to it).",
    "created_at": "2008-11-12T14:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30474",
    "user": "https://github.com/jasongrout"
}
```

I guess the other thing I should make perfectly clear is that the changes I made to the timeseries and the real_roots files were *only* to get `sage -br` to work so that I could concentrate on the doctests in the vector code.  If the authors don't beat me to it, I plan to go through each of those changes and make them optimally access the numpy array (which should be just about as fast as the previous C double array access to the GSL vector).  That's why the patch is "needs work"--it's a work-in-progress that I wanted to post to trac to (a) back up and (b) expose to a wider audience.

That said, I really appreciate your comments.  I'll pay particular attention to optimizing these (if someone else doesn't beat me to it).



---

archive/issue_comments_030475.json:
```json
{
    "body": "Okay, after spending some time optimizing the time_series.pyx code, we are *faster* (for interesting big cases):\n\nbefore patch:\n\n```\nsage: v = finance.TimeSeries([1..1e3])\nsage: %timeit v.vector()\n10000 loops, best of 3: 132 \u00b5s per loop\nsage: v = finance.TimeSeries([1..1e4])\nsage: %timeit v.vector()\n1000 loops, best of 3: 198 \u00b5s per loop\nsage: v = finance.TimeSeries([1..1e5])\nsage: %timeit v.vector()\n100 loops, best of 3: 2.02 ms per loop\nsage: v = finance.TimeSeries([1..1e6])\n%timeit v.vector()\nsage: %timeit v.vector()\n10 loops, best of 3: 17.1 ms per loop\n```\n\nafter patch:\n\n```\nsage: v = finance.TimeSeries([1..1e3])\nsage: %timeit v.vector()\n10000 loops, best of 3: 148 \u00b5s per loop\nsage: v = finance.TimeSeries([1..1e4])\nsage: %timeit v.vector()\n1000 loops, best of 3: 222 \u00b5s per loop\nsage: v = finance.TimeSeries([1..1e5])\nsage: %timeit v.vector()\n1000 loops, best of 3: 1.26 ms per loop\nsage: v = finance.TimeSeries([1..1e6])\nsage: %timeit v.vector()\n100 loops, best of 3: 10.1 ms per loop\n```",
    "created_at": "2008-11-22T22:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30475",
    "user": "https://github.com/jasongrout"
}
```

Okay, after spending some time optimizing the time_series.pyx code, we are *faster* (for interesting big cases):

before patch:

```
sage: v = finance.TimeSeries([1..1e3])
sage: %timeit v.vector()
10000 loops, best of 3: 132 µs per loop
sage: v = finance.TimeSeries([1..1e4])
sage: %timeit v.vector()
1000 loops, best of 3: 198 µs per loop
sage: v = finance.TimeSeries([1..1e5])
sage: %timeit v.vector()
100 loops, best of 3: 2.02 ms per loop
sage: v = finance.TimeSeries([1..1e6])
%timeit v.vector()
sage: %timeit v.vector()
10 loops, best of 3: 17.1 ms per loop
```

after patch:

```
sage: v = finance.TimeSeries([1..1e3])
sage: %timeit v.vector()
10000 loops, best of 3: 148 µs per loop
sage: v = finance.TimeSeries([1..1e4])
sage: %timeit v.vector()
1000 loops, best of 3: 222 µs per loop
sage: v = finance.TimeSeries([1..1e5])
sage: %timeit v.vector()
1000 loops, best of 3: 1.26 ms per loop
sage: v = finance.TimeSeries([1..1e6])
sage: %timeit v.vector()
100 loops, best of 3: 10.1 ms per loop
```



---

archive/issue_comments_030476.json:
```json
{
    "body": "Okay, I updated all the docstrings; all tests pass.\n\nMy one concern is that in sage/rings/polynomial/real_roots.pyx, I tried to use the new cython buffer interface, but at compile-time, I got a maximum recursion depth exceeded error in the find_buffer_type function (I think that was the name).  Right now, real_roots uses the slow standard python __getitem__ method.\n\nEither the Cython buffer issue should be fixed or we should make the real_roots access the vector in a faster way (preferably using the numpy C API or exposing that with, say, a get_unsafe_python function in the vector_double_dense file).",
    "created_at": "2008-11-23T06:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30476",
    "user": "https://github.com/jasongrout"
}
```

Okay, I updated all the docstrings; all tests pass.

My one concern is that in sage/rings/polynomial/real_roots.pyx, I tried to use the new cython buffer interface, but at compile-time, I got a maximum recursion depth exceeded error in the find_buffer_type function (I think that was the name).  Right now, real_roots uses the slow standard python __getitem__ method.

Either the Cython buffer issue should be fixed or we should make the real_roots access the vector in a faster way (preferably using the numpy C API or exposing that with, say, a get_unsafe_python function in the vector_double_dense file).



---

archive/issue_comments_030477.json:
```json
{
    "body": "This patch depends on #4570.",
    "created_at": "2008-11-23T06:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30477",
    "user": "https://github.com/jasongrout"
}
```

This patch depends on #4570.



---

archive/issue_comments_030478.json:
```json
{
    "body": "Regarding the max recursion error mentioned above:\n\n```\nDag Sverre Seljebotn wrote:\n> Seems like an issue with circular cimports? Which means those aren't tested in the test framework. Anyway I was unable to provoke the behaviour with a testcase myself, but \"coding in blind\" then I assume that the following patch should fix it.\n>\n> Jason: To answer the question in the wiki about what to do for SAGE, I assume that we can quite quickly release a Cython 0.10.2 that incorporates this patch. Though Robert would be the one to give a real answer.\n>\n> diff -r 04e83ffd8ea2 Cython/Compiler/Buffer.py\n> --- a/Cython/Compiler/Buffer.py Fri Nov 07 06:55:37 2008 +0100\n> +++ b/Cython/Compiler/Buffer.py Sun Nov 23 16:58:15 2008 +0100\n> @@ -710,7 +710,11 @@ def use_py2_buffer_functions(env):\n>\n>      # Search all types for __getbuffer__ overloads\n>      types = []\n> +    visited_scopes = set()\n>      def find_buffer_types(scope):\n> +        if scope in visited_scopes:\n> +            return\n> +        visited_scopes.add(scope)\n>          for m in scope.cimported_modules:\n>              find_buffer_types(m)\n>          for e in scope.type_entries:\n>\n\nThis patch made it compile and all the doctests pass.\n\nCan we get this patch (or an equivalent one) into Sage as soon as possible?\n\n\nThanks,\n\nJason\n```",
    "created_at": "2008-11-24T16:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30478",
    "user": "https://github.com/jasongrout"
}
```

Regarding the max recursion error mentioned above:

```
Dag Sverre Seljebotn wrote:
> Seems like an issue with circular cimports? Which means those aren't tested in the test framework. Anyway I was unable to provoke the behaviour with a testcase myself, but "coding in blind" then I assume that the following patch should fix it.
>
> Jason: To answer the question in the wiki about what to do for SAGE, I assume that we can quite quickly release a Cython 0.10.2 that incorporates this patch. Though Robert would be the one to give a real answer.
>
> diff -r 04e83ffd8ea2 Cython/Compiler/Buffer.py
> --- a/Cython/Compiler/Buffer.py Fri Nov 07 06:55:37 2008 +0100
> +++ b/Cython/Compiler/Buffer.py Sun Nov 23 16:58:15 2008 +0100
> @@ -710,7 +710,11 @@ def use_py2_buffer_functions(env):
>
>      # Search all types for __getbuffer__ overloads
>      types = []
> +    visited_scopes = set()
>      def find_buffer_types(scope):
> +        if scope in visited_scopes:
> +            return
> +        visited_scopes.add(scope)
>          for m in scope.cimported_modules:
>              find_buffer_types(m)
>          for e in scope.type_entries:
>

This patch made it compile and all the doctests pass.

Can we get this patch (or an equivalent one) into Sage as soon as possible?


Thanks,

Jason
```



---

archive/issue_comments_030479.json:
```json
{
    "body": "(when I say \"all the doctests\", I mean all the doctests in real_roots.pyx)",
    "created_at": "2008-11-24T16:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30479",
    "user": "https://github.com/jasongrout"
}
```

(when I say "all the doctests", I mean all the doctests in real_roots.pyx)



---

archive/issue_comments_030480.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-24T16:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30480",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030481.json:
```json
{
    "body": "Attachment [vector-RDF-CDF-numpy.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy.patch) by @jasongrout created at 2008-11-24 16:19:31\n\nTo review this patch:\n\n1. Start with sage-3.2\n2. Apply the patch at #4570\n3. Apply the following patch to /sage/local/lib/python2.5/site-packages/Cython/Compiler/Buffer.py:\n\n```\ndiff -r 04e83ffd8ea2 Cython/Compiler/Buffer.py\n--- a/Cython/Compiler/Buffer.py Fri Nov 07 06:55:37 2008 +0100\n+++ b/Cython/Compiler/Buffer.py Sun Nov 23 16:58:15 2008 +0100\n@@ -710,7 +710,11 @@ def use_py2_buffer_functions(env):\n     # Search all types for __getbuffer__ overloads\n     types = []\n+    visited_scopes = set()\n     def find_buffer_types(scope):\n+        if scope in visited_scopes:\n+            return\n+        visited_scopes.add(scope)\n         for m in scope.cimported_modules:\n             find_buffer_types(m)\n         for e in scope.type_entries:\n```\n4. Of course, do sage -br",
    "created_at": "2008-11-24T16:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30481",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector-RDF-CDF-numpy.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy.patch) by @jasongrout created at 2008-11-24 16:19:31

To review this patch:

1. Start with sage-3.2
2. Apply the patch at #4570
3. Apply the following patch to /sage/local/lib/python2.5/site-packages/Cython/Compiler/Buffer.py:

```
diff -r 04e83ffd8ea2 Cython/Compiler/Buffer.py
--- a/Cython/Compiler/Buffer.py Fri Nov 07 06:55:37 2008 +0100
+++ b/Cython/Compiler/Buffer.py Sun Nov 23 16:58:15 2008 +0100
@@ -710,7 +710,11 @@ def use_py2_buffer_functions(env):
     # Search all types for __getbuffer__ overloads
     types = []
+    visited_scopes = set()
     def find_buffer_types(scope):
+        if scope in visited_scopes:
+            return
+        visited_scopes.add(scope)
         for m in scope.cimported_modules:
             find_buffer_types(m)
         for e in scope.type_entries:
```
4. Of course, do sage -br



---

archive/issue_comments_030482.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2008-11-24T16:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30482",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_030483.json:
```json
{
    "body": "Oh, yeah, and step 3.5: apply the patch on this ticket :).",
    "created_at": "2008-11-24T16:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30483",
    "user": "https://github.com/jasongrout"
}
```

Oh, yeah, and step 3.5: apply the patch on this ticket :).



---

archive/issue_comments_030484.json:
```json
{
    "body": "Attachment [vector-rdf-doctest-correction.patch](tarball://root/attachments/some-uuid/ticket4206/vector-rdf-doctest-correction.patch) by @jasongrout created at 2008-11-24 20:28:06",
    "created_at": "2008-11-24T20:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30484",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector-rdf-doctest-correction.patch](tarball://root/attachments/some-uuid/ticket4206/vector-rdf-doctest-correction.patch) by @jasongrout created at 2008-11-24 20:28:06



---

archive/issue_comments_030485.json:
```json
{
    "body": "With the second patch on this ticket, \"make test\" passes in sage 3.2.",
    "created_at": "2008-11-24T20:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30485",
    "user": "https://github.com/jasongrout"
}
```

With the second patch on this ticket, "make test" passes in sage 3.2.



---

archive/issue_comments_030486.json:
```json
{
    "body": "The patch on this ticket solves #4491 as well.",
    "created_at": "2008-11-24T22:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30486",
    "user": "https://github.com/jasongrout"
}
```

The patch on this ticket solves #4491 as well.



---

archive/issue_comments_030487.json:
```json
{
    "body": "I'm rebasing this to merge after #4580 has been merged.",
    "created_at": "2008-11-26T17:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30487",
    "user": "https://github.com/jasongrout"
}
```

I'm rebasing this to merge after #4580 has been merged.



---

archive/issue_comments_030488.json:
```json
{
    "body": "Attachment [vector-RDF-CDF-numpy.2.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy.2.patch) by @jasongrout created at 2008-11-26 17:40:45\n\nRebased for sage-3.2.1.alpha1",
    "created_at": "2008-11-26T17:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30488",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector-RDF-CDF-numpy.2.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy.2.patch) by @jasongrout created at 2008-11-26 17:40:45

Rebased for sage-3.2.1.alpha1



---

archive/issue_comments_030489.json:
```json
{
    "body": "New instructions that should work for sage-3.2.1.alpha1:\n\n1. Apply, in order, vector-RDF-CDF-numpy.2.patch and vector-rdf-doctest-correction.patch\n\n2. Do sage -br\n\nEnjoy!",
    "created_at": "2008-11-26T17:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30489",
    "user": "https://github.com/jasongrout"
}
```

New instructions that should work for sage-3.2.1.alpha1:

1. Apply, in order, vector-RDF-CDF-numpy.2.patch and vector-rdf-doctest-correction.patch

2. Do sage -br

Enjoy!



---

archive/issue_comments_030490.json:
```json
{
    "body": "With either sage version, you might have to delete the Cython cache by removing the file SAGE_ROOT/devel/sage/.cython_deps before doing sage -br.  This is because I remove a Cython file in the patch.",
    "created_at": "2008-11-26T17:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30490",
    "user": "https://github.com/jasongrout"
}
```

With either sage version, you might have to delete the Cython cache by removing the file SAGE_ROOT/devel/sage/.cython_deps before doing sage -br.  This is because I remove a Cython file in the patch.



---

archive/issue_comments_030491.json:
```json
{
    "body": "Needs work.  The top of the file that implements complex double vectors starts out like this (matrices not vectors, and deletes all the old Complex double vector stuff). \n\n```\n        1       \"\"\" \n \t2\tDense matrices over the Real Double Field. \n \t3\t \n \t4\tMatrix operations using numpy. \n \t5\t \n \t6\tEXAMPLES: \n \t7\t    sage: b=Mat(RDF,2,3).basis() \n \t8\t    sage: b[0] \n \t9\t    [1.0 0.0 0.0] \n \t10\t    [0.0 0.0 0.0] \n \t11\t \n \t12\t \n \t13\tWe deal with the case of zero rows or zero columns: \n \t14\t    sage: m = MatrixSpace(RDF,0,3) \n \t15\t    sage: m.zero_matrix() \n \t16\t    [] \n \t17\t \n \t18\tTESTS: \n \t19\t    sage: a = matrix(RDF,2,range(4), sparse=False) \n \t20\t    sage: loads(dumps(a)) == a \n \t21\t    True \n \t22\t \n \t23\tAUTHORS: \n \t24\t    -- Jason Grout, Sep 2008: switch to numpy backend \n \t25\t    -- Josh Kantor \n \t26\t    -- William Stein: many bug fixes and touch ups. \n \t27\t\"\"\" \n \t28\t \n \t29\t############################################################################## \n \t30\t#       Copyright (C) 2004,2005,2006 Joshua Kantor <kantor.jm@gmail.com> \n \t31\t#  Distributed under the terms of the GNU General Public License (GPL) \n \t32\t#  The full text of the GPL is available at: \n \t33\t#                  http://www.gnu.org/licenses/ \n \t34\t############################################################################## \n \t35\tfrom sage.rings.complex_double import CDF \n \t36\t \n \t37\tcimport sage.ext.numpy as cnumpy \n \t38\t \n \t39\tnumpy=None \n \t40\t \n \t41\tcdef class Vector_complex_double_dense(vector_double_dense.Vector_double_dense): \n```",
    "created_at": "2008-11-27T05:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30491",
    "user": "https://github.com/williamstein"
}
```

Needs work.  The top of the file that implements complex double vectors starts out like this (matrices not vectors, and deletes all the old Complex double vector stuff). 

```
        1       """ 
 	2	Dense matrices over the Real Double Field. 
 	3	 
 	4	Matrix operations using numpy. 
 	5	 
 	6	EXAMPLES: 
 	7	    sage: b=Mat(RDF,2,3).basis() 
 	8	    sage: b[0] 
 	9	    [1.0 0.0 0.0] 
 	10	    [0.0 0.0 0.0] 
 	11	 
 	12	 
 	13	We deal with the case of zero rows or zero columns: 
 	14	    sage: m = MatrixSpace(RDF,0,3) 
 	15	    sage: m.zero_matrix() 
 	16	    [] 
 	17	 
 	18	TESTS: 
 	19	    sage: a = matrix(RDF,2,range(4), sparse=False) 
 	20	    sage: loads(dumps(a)) == a 
 	21	    True 
 	22	 
 	23	AUTHORS: 
 	24	    -- Jason Grout, Sep 2008: switch to numpy backend 
 	25	    -- Josh Kantor 
 	26	    -- William Stein: many bug fixes and touch ups. 
 	27	""" 
 	28	 
 	29	############################################################################## 
 	30	#       Copyright (C) 2004,2005,2006 Joshua Kantor <kantor.jm@gmail.com> 
 	31	#  Distributed under the terms of the GNU General Public License (GPL) 
 	32	#  The full text of the GPL is available at: 
 	33	#                  http://www.gnu.org/licenses/ 
 	34	############################################################################## 
 	35	from sage.rings.complex_double import CDF 
 	36	 
 	37	cimport sage.ext.numpy as cnumpy 
 	38	 
 	39	numpy=None 
 	40	 
 	41	cdef class Vector_complex_double_dense(vector_double_dense.Vector_double_dense): 
```



---

archive/issue_comments_030492.json:
```json
{
    "body": "Apparently I  concentrated so much on making the documentation in vector_double_dense.pyx good that I forgot to make sure the documentation in subclasses was up to par.  I based the implementation on CDF/RDF matrix code, but apparently forgot to change the docs.  I'll post a new patch today.",
    "created_at": "2008-11-27T15:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30492",
    "user": "https://github.com/jasongrout"
}
```

Apparently I  concentrated so much on making the documentation in vector_double_dense.pyx good that I forgot to make sure the documentation in subclasses was up to par.  I based the implementation on CDF/RDF matrix code, but apparently forgot to change the docs.  I'll post a new patch today.



---

archive/issue_comments_030493.json:
```json
{
    "body": "Attachment [vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch) by @jasongrout created at 2008-11-28 02:57:37",
    "created_at": "2008-11-28T02:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30493",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch) by @jasongrout created at 2008-11-28 02:57:37



---

archive/issue_comments_030494.json:
```json
{
    "body": "The patch vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch has been rebased to sage-3.2.1.alpha2 and takes care of the previous concerns.",
    "created_at": "2008-11-28T02:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30494",
    "user": "https://github.com/jasongrout"
}
```

The patch vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch has been rebased to sage-3.2.1.alpha2 and takes care of the previous concerns.



---

archive/issue_comments_030495.json:
```json
{
    "body": "It doesn't build for me:\n\n```\n\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nhg_sage.revesage: hg_sage.revert('--all')\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg revert --all\nreverting module_list.py\nforgetting sage/groups/multiplicative_wrapper.pxd\nforgetting sage/groups/multiplicative_wrapper.pyx\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4206/vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4206/vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch?format=raw\nLoading: [...........]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/15486/tmp_0.patch\"\napplying /home/was/.sage/temp/sage/15486/tmp_0.patch\nsage: \nExiting SAGE (CPU time 0m0.12s, Wall time 0m19.72s).\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage -br\n| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nBuilding modified file sage/modules/free_module_element.pyx.\nBuilding modified file sage/modules/vector_double_dense.pyx.\nBuilding modified file sage/modules/vector_complex_double_dense.pyx.\nBuilding modified file sage/modules/vector_real_double_dense.pyx.\nBuilding modified file sage/matrix/matrix_double_dense.pyx.\nBuilding sage/matrix/matrix_real_double_dense.pyx because it depends on sage/ext/numpy.pxd.\nBuilding sage/matrix/change_ring.pyx because it depends on sage/ext/numpy.pxd.\nBuilding sage/matrix/matrix_complex_double_dense.pyx because it depends on sage/ext/numpy.pxd.\nTraceback (most recent call last):\n  File \"setup.py\", line 486, in <module>\n    queue = compile_command_list(ext_modules, deps)\n  File \"setup.py\", line 456, in compile_command_list\n    dep_file, dep_time = deps.newest_dep(f)\n  File \"setup.py\", line 371, in newest_dep\n    for f in self.all_deps(filename):\n  File \"setup.py\", line 354, in all_deps\n    deps.update(self.all_deps(f, path))\n  File \"setup.py\", line 352, in all_deps\n    for f in self.immediate_deps(filename):\n  File \"setup.py\", line 334, in immediate_deps\n    self._deps[filename] = self.parse_deps(filename)\n  File \"setup.py\", line 290, in parse_deps\n    f = open(filename)\nIOError: [Errno 2] No such file or directory: 'sage/modules/real_double_vector.pxd'\nsage: There was an error installing modified sage library code.\n\n```",
    "created_at": "2008-11-28T21:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30495",
    "user": "https://github.com/williamstein"
}
```

It doesn't build for me:

```

was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hg_sage.revesage: hg_sage.revert('--all')
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg revert --all
reverting module_list.py
forgetting sage/groups/multiplicative_wrapper.pxd
forgetting sage/groups/multiplicative_wrapper.pyx
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4206/vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4206/vector-RDF-CDF-numpy-sage-3.2.1.alpha2.patch?format=raw
Loading: [...........]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15486/tmp_0.patch"
applying /home/was/.sage/temp/sage/15486/tmp_0.patch
sage: 
Exiting SAGE (CPU time 0m0.12s, Wall time 0m19.72s).
was@sage:~/build/sage-3.2.1.alpha1$ ./sage -br
| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/modules/free_module_element.pyx.
Building modified file sage/modules/vector_double_dense.pyx.
Building modified file sage/modules/vector_complex_double_dense.pyx.
Building modified file sage/modules/vector_real_double_dense.pyx.
Building modified file sage/matrix/matrix_double_dense.pyx.
Building sage/matrix/matrix_real_double_dense.pyx because it depends on sage/ext/numpy.pxd.
Building sage/matrix/change_ring.pyx because it depends on sage/ext/numpy.pxd.
Building sage/matrix/matrix_complex_double_dense.pyx because it depends on sage/ext/numpy.pxd.
Traceback (most recent call last):
  File "setup.py", line 486, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 456, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 371, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 354, in all_deps
    deps.update(self.all_deps(f, path))
  File "setup.py", line 352, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 334, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 290, in parse_deps
    f = open(filename)
IOError: [Errno 2] No such file or directory: 'sage/modules/real_double_vector.pxd'
sage: There was an error installing modified sage library code.

```



---

archive/issue_comments_030496.json:
```json
{
    "body": "The above is a bug in the cython dependency checking code.  I'll do a full rebuild.\n\nThat said, I can't imagine that unpickling real double vectors could work because that should call the real_double_vector module.  We shall see :-)",
    "created_at": "2008-11-28T21:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30496",
    "user": "https://github.com/williamstein"
}
```

The above is a bug in the cython dependency checking code.  I'll do a full rebuild.

That said, I can't imagine that unpickling real double vectors could work because that should call the real_double_vector module.  We shall see :-)



---

archive/issue_comments_030497.json:
```json
{
    "body": "This patch seems to totally get rid of the real_double_vector module.  After applying it and making sure to delete all traces of it from the build directory, I get the following on startup of sage:\n\n{{\n/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/modules/free_quadratic_module.py in <module>()\n     92 import sage.rings.integer\n     93 import sage.structure.parent_gens as gens\n---> 94 import sage.modules.real_double_vector\n     95 import sage.modules.complex_double_vector\n     96 from sage.misc.randstate import current_randstate\n\nImportError: No module named real_double_vector\n}}}",
    "created_at": "2008-11-28T22:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30497",
    "user": "https://github.com/williamstein"
}
```

This patch seems to totally get rid of the real_double_vector module.  After applying it and making sure to delete all traces of it from the build directory, I get the following on startup of sage:

{{
/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/modules/free_quadratic_module.py in <module>()
     92 import sage.rings.integer
     93 import sage.structure.parent_gens as gens
---> 94 import sage.modules.real_double_vector
     95 import sage.modules.complex_double_vector
     96 from sage.misc.randstate import current_randstate

ImportError: No module named real_double_vector
}}}



---

archive/issue_comments_030498.json:
```json
{
    "body": "Reviewer -- make sure that the attached file v.sobj can be loaded after this patch is applied and all traces of old real_double_vector* stuff is deleted from SAGE_ROOT/devel/sage/build/...",
    "created_at": "2008-11-28T22:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30498",
    "user": "https://github.com/williamstein"
}
```

Reviewer -- make sure that the attached file v.sobj can be loaded after this patch is applied and all traces of old real_double_vector* stuff is deleted from SAGE_ROOT/devel/sage/build/...



---

archive/issue_comments_030499.json:
```json
{
    "body": "Attachment [v.sobj](tarball://root/attachments/some-uuid/ticket4206/v.sobj) by @jasongrout created at 2008-12-03 17:31:58\n\nThe updated (sage-3.2.1) patch deletes the real_double_vector.pyx and complex_double_vector.pyx files and instead creates (real|complex)_double_vector.py files, which basically contain references to the unpickling functions and make the old classes aliases for the new classes.  We could just as well make the old classes = None (and I think unpickling old things will still work), but this way there is some sort of backwards compatibility for people still using the old class names.",
    "created_at": "2008-12-03T17:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30499",
    "user": "https://github.com/jasongrout"
}
```

Attachment [v.sobj](tarball://root/attachments/some-uuid/ticket4206/v.sobj) by @jasongrout created at 2008-12-03 17:31:58

The updated (sage-3.2.1) patch deletes the real_double_vector.pyx and complex_double_vector.pyx files and instead creates (real|complex)_double_vector.py files, which basically contain references to the unpickling functions and make the old classes aliases for the new classes.  We could just as well make the old classes = None (and I think unpickling old things will still work), but this way there is some sort of backwards compatibility for people still using the old class names.



---

archive/issue_comments_030500.json:
```json
{
    "body": "I updated the patch to address a doctest failure.  The updated patch now passes doctests in sage/modules/*.(py|pyx) and also passes doctests in sage/structure/sage_object.pyx.\n\nThis should be ready to be reviewed again.\n\nThe only patch you need to apply is vector-RDF-CDF-numpy-sage-3.2.1.patch to sage 3.2.1.",
    "created_at": "2008-12-03T17:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30500",
    "user": "https://github.com/jasongrout"
}
```

I updated the patch to address a doctest failure.  The updated patch now passes doctests in sage/modules/*.(py|pyx) and also passes doctests in sage/structure/sage_object.pyx.

This should be ready to be reviewed again.

The only patch you need to apply is vector-RDF-CDF-numpy-sage-3.2.1.patch to sage 3.2.1.



---

archive/issue_comments_030501.json:
```json
{
    "body": "To review this patch, you need to delete the real_double_vector.* and complex_double_vector.* files out of sage/build/ directories.  One way to do this is:\n\ncd $SAGE_ROOT/devel/sage/build\nfind . | grep real_double_vector | xargs rm\nfind . | grep complex_double_vector | xargs rm\n\nThen do sage -br after applying the patch.  Then you should be ready to test the patch.",
    "created_at": "2008-12-03T17:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30501",
    "user": "https://github.com/jasongrout"
}
```

To review this patch, you need to delete the real_double_vector.* and complex_double_vector.* files out of sage/build/ directories.  One way to do this is:

cd $SAGE_ROOT/devel/sage/build
find . | grep real_double_vector | xargs rm
find . | grep complex_double_vector | xargs rm

Then do sage -br after applying the patch.  Then you should be ready to test the patch.



---

archive/issue_comments_030502.json:
```json
{
    "body": "Jason asked me to look in particular at the real_roots.pyx parts of this patch, so I did:\n\nThe changes to real_roots.pyx look good.  Also, I ran a couple of my standard benchmarks, and the pre- and post-patch timings are not measurably different.\n\nPositive review for real_roots.pyx portion of the patch.",
    "created_at": "2008-12-05T02:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30502",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Jason asked me to look in particular at the real_roots.pyx parts of this patch, so I did:

The changes to real_roots.pyx look good.  Also, I ran a couple of my standard benchmarks, and the pre- and post-patch timings are not measurably different.

Positive review for real_roots.pyx portion of the patch.



---

archive/issue_comments_030503.json:
```json
{
    "body": "A reminder that once this is closed, close #4491 as well.",
    "created_at": "2008-12-06T05:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30503",
    "user": "https://github.com/jasongrout"
}
```

A reminder that once this is closed, close #4491 as well.



---

archive/issue_comments_030504.json:
```json
{
    "body": "I was unable to build this after applying it to sage-3.2.2.alpha0:\n\n```\nbuilding 'sage.rings.polynomial.real_roots' extension\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/was/build/sage-3.2.2.alpha0/local//include -I/home/was/build/sage-3.2.2\n.alpha0/local//include/csage -I/home/was/build/sage-3.2.2.alpha0/devel//sage/sage/ext -I/home/was/build/sage-3.2.2.alpha0/local/include/python2.5 -c sage/rings/\npolynomial/real_roots.c -o build/temp.linux-x86_64-2.5/sage/rings/polynomial/real_roots.o -w\nsage/rings/polynomial/real_roots.c:119:31: error: numpy/arrayobject.h: No such file or directory\nsage/rings/polynomial/real_roots.c:388: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_int8_t\u2019\nsage/rings/polynomial/real_roots.c:390: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_int16_t\u2019\nsage/rings/polynomial/real_roots.c:392: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_int32_t\u2019\nsage/rings/polynomial/real_roots.c:394: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_int64_t\u2019\nsage/rings/polynomial/real_roots.c:396: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_uint8_t\u2019\nsage/rings/polynomial/real_roots.c:398: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_uint16_t\u2019\nsage/rings/polynomial/real_roots.c:400: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_uint32_t\u2019\nsage/rings/polynomial/real_roots.c:402: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_uint64_t\u2019\nsage/rings/polynomial/real_roots.c:404: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_float32_t\u2019\nsage/rings/polynomial/real_roots.c:406: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_float64_t\u2019\nsage/rings/polynomial/real_roots.c:408: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_int_t\u2019\nsage/rings/polynomial/real_roots.c:410: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_long_t\u2019\nsage/rings/polynomial/real_roots.c:412: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_uint_t\u2019\nsage/rings/polynomial/real_roots.c:414: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_ulong_t\u2019\nsage/rings/polynomial/real_roots.c:416: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_float_t\u2019\nsage/rings/polynomial/real_roots.c:418: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_double_t\u2019\nsage/rings/polynomial/real_roots.c:420: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_longdouble_t\u2019\nsage/rings/polynomial/real_roots.c:422: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_cfloat_t\u2019\nsage/rings/polynomial/real_roots.c:424: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_cdouble_t\u2019\nsage/rings/polynomial/real_roots.c:426: error: expected \u2018=\u2019, \u2018,\u2019, \u2018;\u2019, \u2018asm\u2019 or \u2018__attribute__\u2019 before \u2018__pyx_t_5numpy_clongdouble_t\u2019\nsage/rings/polynomial/real_roots.c:998: error: field \u2018_numpy_dtypeint\u2019 has incomplete type\nsage/rings/polynomial/real_roots.c:1002: error: expected specifier-qualifier-list before \u2018PyArrayObject\u2019\nsage/rings/polynomial/real_roots.c:2274: error: expected declaration specifiers or \u2018...\u2019 before \u2018PyArrayObject\u2019\n```\n\nThis is on 64-bit sage.math.",
    "created_at": "2008-12-06T22:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30504",
    "user": "https://github.com/williamstein"
}
```

I was unable to build this after applying it to sage-3.2.2.alpha0:

```
building 'sage.rings.polynomial.real_roots' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/was/build/sage-3.2.2.alpha0/local//include -I/home/was/build/sage-3.2.2
.alpha0/local//include/csage -I/home/was/build/sage-3.2.2.alpha0/devel//sage/sage/ext -I/home/was/build/sage-3.2.2.alpha0/local/include/python2.5 -c sage/rings/
polynomial/real_roots.c -o build/temp.linux-x86_64-2.5/sage/rings/polynomial/real_roots.o -w
sage/rings/polynomial/real_roots.c:119:31: error: numpy/arrayobject.h: No such file or directory
sage/rings/polynomial/real_roots.c:388: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_int8_t’
sage/rings/polynomial/real_roots.c:390: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_int16_t’
sage/rings/polynomial/real_roots.c:392: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_int32_t’
sage/rings/polynomial/real_roots.c:394: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_int64_t’
sage/rings/polynomial/real_roots.c:396: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_uint8_t’
sage/rings/polynomial/real_roots.c:398: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_uint16_t’
sage/rings/polynomial/real_roots.c:400: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_uint32_t’
sage/rings/polynomial/real_roots.c:402: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_uint64_t’
sage/rings/polynomial/real_roots.c:404: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_float32_t’
sage/rings/polynomial/real_roots.c:406: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_float64_t’
sage/rings/polynomial/real_roots.c:408: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_int_t’
sage/rings/polynomial/real_roots.c:410: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_long_t’
sage/rings/polynomial/real_roots.c:412: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_uint_t’
sage/rings/polynomial/real_roots.c:414: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_ulong_t’
sage/rings/polynomial/real_roots.c:416: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_float_t’
sage/rings/polynomial/real_roots.c:418: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_double_t’
sage/rings/polynomial/real_roots.c:420: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_longdouble_t’
sage/rings/polynomial/real_roots.c:422: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_cfloat_t’
sage/rings/polynomial/real_roots.c:424: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_cdouble_t’
sage/rings/polynomial/real_roots.c:426: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘__pyx_t_5numpy_clongdouble_t’
sage/rings/polynomial/real_roots.c:998: error: field ‘_numpy_dtypeint’ has incomplete type
sage/rings/polynomial/real_roots.c:1002: error: expected specifier-qualifier-list before ‘PyArrayObject’
sage/rings/polynomial/real_roots.c:2274: error: expected declaration specifiers or ‘...’ before ‘PyArrayObject’
```

This is on 64-bit sage.math.



---

archive/issue_comments_030505.json:
```json
{
    "body": "I get the same error stream as was on intel atom.",
    "created_at": "2008-12-06T23:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30505",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

I get the same error stream as was on intel atom.



---

archive/issue_comments_030506.json:
```json
{
    "body": "Attachment [real_roots-import.patch](tarball://root/attachments/some-uuid/ticket4206/real_roots-import.patch) by @jasongrout created at 2008-12-07 03:41:54\n\nI attached a patch which should take care of the problem.  The problem was manifest on a system that does not have a system numpy; the include directories were not set up properly for real_roots.pyx.  So now, apply vector-RDF-CDF-numpy-sage-3.2.1.patch and then apply real_roots-import.patch.\n\nLet me know if the problem still persists.",
    "created_at": "2008-12-07T03:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30506",
    "user": "https://github.com/jasongrout"
}
```

Attachment [real_roots-import.patch](tarball://root/attachments/some-uuid/ticket4206/real_roots-import.patch) by @jasongrout created at 2008-12-07 03:41:54

I attached a patch which should take care of the problem.  The problem was manifest on a system that does not have a system numpy; the include directories were not set up properly for real_roots.pyx.  So now, apply vector-RDF-CDF-numpy-sage-3.2.1.patch and then apply real_roots-import.patch.

Let me know if the problem still persists.



---

archive/issue_comments_030507.json:
```json
{
    "body": "Overall the design looks good to me and the interface with numpy looks good. A few things I noticed. \n\n1. For large arrays around a million, object creation is ever so slightly slower than the old class it seems, I'm guessing thats numpy's falt, there is maybe nothing you can do about that.\n\n\n2. More seriously the fft function is quite a bit slower. \nFor example it takes about 15 seconds to do fft on a vector of lenth a million. Scipy only takes 0.72 to do the fft, and the old class also only took about a second. I'll look and see if I have any suggestions about the bottle neck, this probably should be fixed. It seemed most other operations were about the same speed but it might be good to double check this. \n\n3. One suggestion, I think it would cool if in vector_double_dense.pxd you make the _vector_numpy array public as in\n\n```\ncdef public cnumpy.ndarray _vector_numpy\n```\nthen it is possible to do something like\n\n```\nv=vector(RDF,[1,2,3])\nv._vector_numpy[0]=3\n```\nthis could be useful to pass something to scipy without having to copy. You could make it readonly instead of public if you don't want people to be able to modify through that mechanism.",
    "created_at": "2008-12-07T08:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30507",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Overall the design looks good to me and the interface with numpy looks good. A few things I noticed. 

1. For large arrays around a million, object creation is ever so slightly slower than the old class it seems, I'm guessing thats numpy's falt, there is maybe nothing you can do about that.


2. More seriously the fft function is quite a bit slower. 
For example it takes about 15 seconds to do fft on a vector of lenth a million. Scipy only takes 0.72 to do the fft, and the old class also only took about a second. I'll look and see if I have any suggestions about the bottle neck, this probably should be fixed. It seemed most other operations were about the same speed but it might be good to double check this. 

3. One suggestion, I think it would cool if in vector_double_dense.pxd you make the _vector_numpy array public as in

```
cdef public cnumpy.ndarray _vector_numpy
```
then it is possible to do something like

```
v=vector(RDF,[1,2,3])
v._vector_numpy[0]=3
```
this could be useful to pass something to scipy without having to copy. You could make it readonly instead of public if you don't want people to be able to modify through that mechanism.



---

archive/issue_comments_030508.json:
```json
{
    "body": "> Scipy only takes 0.72 to do the fft,\n\n\nWhy don't we use scipy to do the fft, then?",
    "created_at": "2008-12-07T19:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30508",
    "user": "https://github.com/williamstein"
}
```

> Scipy only takes 0.72 to do the fft,


Why don't we use scipy to do the fft, then?



---

archive/issue_comments_030509.json:
```json
{
    "body": "This is a little puzzling since the code *does* use scipy to do fft.  Here is the relevant call:\n\n```\n            return v._new(scipy.fft(v._vector_numpy))\n```\n\nThe thing that I see is that above this, I do:\n\n```\n        cdef Vector_double_dense v = self.complex_vector()\n```\n\nI think the wasted time is in one of those two calls.  I can look at this later.",
    "created_at": "2008-12-08T13:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30509",
    "user": "https://github.com/jasongrout"
}
```

This is a little puzzling since the code *does* use scipy to do fft.  Here is the relevant call:

```
            return v._new(scipy.fft(v._vector_numpy))
```

The thing that I see is that above this, I do:

```
        cdef Vector_double_dense v = self.complex_vector()
```

I think the wasted time is in one of those two calls.  I can look at this later.



---

archive/issue_comments_030510.json:
```json
{
    "body": "I changed the behavior of the fft function in the vector_fft patch.  It now does a complex fft over a CDF vector, but a *real* fft over an RDF vector.  I also streamlined it, so now we get the following timings (after the patch):\n\n\n```\nsage: v=vector(RDF, range(1000000r))\nsage: n=v.numpy()\nsage: import scipy; import scipy.fftpack\nsage: timeit('a=v.fft()')\n5 loops, best of 3: 96.8 ms per loop\nsage: timeit('b=scipy.fftpack.rfft(n)')\n5 loops, best of 3: 98.3 ms per loop\nsage: timeit('a=v.inv_fft()')\n5 loops, best of 3: 106 ms per loop\nsage: timeit('b=scipy.fftpack.irfft(n)')\n5 loops, best of 3: 106 ms per loop\nsage: v=vector(CDF, range(1000000r))\nsage: n=v.numpy()\nsage: timeit('a=v.fft()')\n5 loops, best of 3: 182 ms per loop\nsage: timeit('b=scipy.fftpack.fft(n)')\n5 loops, best of 3: 181 ms per loop\nsage: timeit('a=v.inv_fft()')\n5 loops, best of 3: 207 ms per loop\nsage: timeit('b=scipy.fftpack.ifft(n)')\n5 loops, best of 3: 207 ms per loop\n```\n\nSince the behavior of the fft function is changed, I'm putting this as \"needs review\".  What I'm looking for is someone to pass off on the use of the real fft for RDF vectors.",
    "created_at": "2008-12-08T18:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30510",
    "user": "https://github.com/jasongrout"
}
```

I changed the behavior of the fft function in the vector_fft patch.  It now does a complex fft over a CDF vector, but a *real* fft over an RDF vector.  I also streamlined it, so now we get the following timings (after the patch):


```
sage: v=vector(RDF, range(1000000r))
sage: n=v.numpy()
sage: import scipy; import scipy.fftpack
sage: timeit('a=v.fft()')
5 loops, best of 3: 96.8 ms per loop
sage: timeit('b=scipy.fftpack.rfft(n)')
5 loops, best of 3: 98.3 ms per loop
sage: timeit('a=v.inv_fft()')
5 loops, best of 3: 106 ms per loop
sage: timeit('b=scipy.fftpack.irfft(n)')
5 loops, best of 3: 106 ms per loop
sage: v=vector(CDF, range(1000000r))
sage: n=v.numpy()
sage: timeit('a=v.fft()')
5 loops, best of 3: 182 ms per loop
sage: timeit('b=scipy.fftpack.fft(n)')
5 loops, best of 3: 181 ms per loop
sage: timeit('a=v.inv_fft()')
5 loops, best of 3: 207 ms per loop
sage: timeit('b=scipy.fftpack.ifft(n)')
5 loops, best of 3: 207 ms per loop
```

Since the behavior of the fft function is changed, I'm putting this as "needs review".  What I'm looking for is someone to pass off on the use of the real fft for RDF vectors.



---

archive/issue_comments_030511.json:
```json
{
    "body": "On IRC, we decided to instead follow the convention in matlab and return a complex vector (and do a complex fft), even if we start out with a real vector.\n\nSo I'll make that change and then consider this a positive review (since then the functionality won't have changed, but the timing will still be good).",
    "created_at": "2008-12-08T23:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30511",
    "user": "https://github.com/jasongrout"
}
```

On IRC, we decided to instead follow the convention in matlab and return a complex vector (and do a complex fft), even if we start out with a real vector.

So I'll make that change and then consider this a positive review (since then the functionality won't have changed, but the timing will still be good).



---

archive/issue_comments_030512.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2008-12-09T06:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30512",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_030513.json:
```json
{
    "body": "Attachment [vector_fft.patch](tarball://root/attachments/some-uuid/ticket4206/vector_fft.patch) by @jasongrout created at 2008-12-09 06:49:36\n\nOkay, updated the vector_fft.patch. The new timing comparison is:\n\n```\nsage: v=vector(RDF, range(1000000r))\nn=v.numpy()\nsage: n=v.numpy()\nsage: import scipy; import scipy.fftpack\nsage: timeit('a=v.fft()')\n5 loops, best of 3: 342 ms per loop\nsage: timeit('b=scipy.fft(n)')\n5 loops, best of 3: 316 ms per loop\nsage: timeit('a=v.inv_fft()')\n5 loops, best of 3: 442 ms per loop\nsage: timeit('b=scipy.ifft(n)')\n5 loops, best of 3: 416 ms per loop\nsage: v=vector(CDF, range(1000000r))\nsage: n=v.numpy()\nsage: timeit('a=v.fft()')\n5 loops, best of 3: 346 ms per loop\nsage: timeit('b=scipy.fft(n)')\n5 loops, best of 3: 319 ms per loop\nsage: timeit('a=v.inv_fft()')\n5 loops, best of 3: 470 ms per loop\nsage: timeit('b=scipy.ifft(n)')\n5 loops, best of 3: 419 ms per loop\n```\n\nSince the timing issue is addressed, I'm marking this as positive review as directed in jkantor's comment.",
    "created_at": "2008-12-09T06:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30513",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector_fft.patch](tarball://root/attachments/some-uuid/ticket4206/vector_fft.patch) by @jasongrout created at 2008-12-09 06:49:36

Okay, updated the vector_fft.patch. The new timing comparison is:

```
sage: v=vector(RDF, range(1000000r))
n=v.numpy()
sage: n=v.numpy()
sage: import scipy; import scipy.fftpack
sage: timeit('a=v.fft()')
5 loops, best of 3: 342 ms per loop
sage: timeit('b=scipy.fft(n)')
5 loops, best of 3: 316 ms per loop
sage: timeit('a=v.inv_fft()')
5 loops, best of 3: 442 ms per loop
sage: timeit('b=scipy.ifft(n)')
5 loops, best of 3: 416 ms per loop
sage: v=vector(CDF, range(1000000r))
sage: n=v.numpy()
sage: timeit('a=v.fft()')
5 loops, best of 3: 346 ms per loop
sage: timeit('b=scipy.fft(n)')
5 loops, best of 3: 319 ms per loop
sage: timeit('a=v.inv_fft()')
5 loops, best of 3: 470 ms per loop
sage: timeit('b=scipy.ifft(n)')
5 loops, best of 3: 419 ms per loop
```

Since the timing issue is addressed, I'm marking this as positive review as directed in jkantor's comment.



---

archive/issue_comments_030514.json:
```json
{
    "body": "Positive review. I would like the making the internal numpy array cdef public as a separate minor patch after this initial one is accepted.",
    "created_at": "2008-12-09T07:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30514",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Positive review. I would like the making the internal numpy array cdef public as a separate minor patch after this initial one is accepted.



---

archive/issue_comments_030515.json:
```json
{
    "body": "There is some slight reject issue with the first patch:\n\n```\n***************\n*** 93,100 ****\n  import sage.rings.integer\n  from sage.rings.real_double import RDF\n  from sage.rings.complex_double import CDF\n- \n- #from sage.matrix.matrix cimport Matrix\n  \n  def is_FreeModuleElement(x):\n      return isinstance(x, FreeModuleElement)\n--- 93,98 ----\n  import sage.rings.integer\n  from sage.rings.real_double import RDF\n  from sage.rings.complex_double import CDF\n  \n  def is_FreeModuleElement(x):\n      return isinstance(x, FreeModuleElement)\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-12-09T07:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is some slight reject issue with the first patch:

```
***************
*** 93,100 ****
  import sage.rings.integer
  from sage.rings.real_double import RDF
  from sage.rings.complex_double import CDF
- 
- #from sage.matrix.matrix cimport Matrix
  
  def is_FreeModuleElement(x):
      return isinstance(x, FreeModuleElement)
--- 93,98 ----
  import sage.rings.integer
  from sage.rings.real_double import RDF
  from sage.rings.complex_double import CDF
  
  def is_FreeModuleElement(x):
      return isinstance(x, FreeModuleElement)
```

Cheers,

Michael



---

archive/issue_comments_030516.json:
```json
{
    "body": "Attachment [vector-RDF-CDF-numpy-sage-3.2.1.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy-sage-3.2.1.patch) by @jasongrout created at 2008-12-09 08:06:40\n\ndeleted reject hunk from file; the three patches should work now.",
    "created_at": "2008-12-09T08:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30516",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector-RDF-CDF-numpy-sage-3.2.1.patch](tarball://root/attachments/some-uuid/ticket4206/vector-RDF-CDF-numpy-sage-3.2.1.patch) by @jasongrout created at 2008-12-09 08:06:40

deleted reject hunk from file; the three patches should work now.



---

archive/issue_comments_030517.json:
```json
{
    "body": "This patch needs doctest fixes. This is on sage.math:\n\n```\nsage -t -long \"devel/sage/sage/finance/fractal.pyx\"         \n\ndrfft:howmany=726335489\ndrfft:howmany=644245095\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/finance/fractal.pyx\", line 109, in __main__.example_1\nFailed example:\n    sim = finance.stationary_gaussian_simulation(s, N)[Integer(0)]###line 66:_sage_    >>> sim = finance.stationary_gaussian_simulation(s, N)[0]\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[6]>\", line 1, in <module>\n        sim = finance.stationary_gaussian_simulation(s, N)[Integer(0)]###line 66:_sage_    >>> sim = finance.stationary_gaussian_simulation(s, N)[0]\n      File \"fractal.pyx\", line 111, in sage.finance.fractal.stationary_gaussian_simulation (sage/finance/fractal.c:642)\n      File \"time_series.pyx\", line 2172, in sage.finance.time_series.TimeSeries.fft (sage/finance/time_series.c:12114)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/scipy/fftpack/basic.py\", line 179, in rfft\n        return _raw_fft(tmp,n,axis,1,overwrite_x,work_function)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/scipy/fftpack/basic.py\", line 49, in _raw_fft\n        r = work_function(x,n,direction,overwrite_x=overwrite_x)\n    error: (n*howmany==size(x)) failed for hidden howmany\n**********************************************************************\n<SNIP>\n```\nAnd\n\n```\nsage -t -long \"devel/sage/sage/finance/time_series.pyx\"     \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/finance/time_series.pyx\", line 427, in __main__.example_15\nFailed example:\n    F = v.autoregressive_fit(Integer(100))###line 532:_sage_    >>> F = v.autoregressive_fit(100)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_15[4]>\", line 1, in <module>\n        F = v.autoregressive_fit(Integer(100))###line 532:_sage_    >>> F = v.autoregressive_fit(100)\n      File \"time_series.pyx\", line 557, in sage.finance.time_series.TimeSeries.autoregressive_fit (sage/finance/time_series.c:4388)\n      File \"time_series.pyx\", line 2378, in sage.finance.time_series.autoregressive_fit (sage/finance/time_series.c:12648)\n      File \"time_series.pyx\", line 1865, in sage.finance.time_series.TimeSeries.numpy (sage/finance/time_series.c:10977)\n    MemoryError\n**********************************************************************\n<SNIP>\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-12-09T08:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30517",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch needs doctest fixes. This is on sage.math:

```
sage -t -long "devel/sage/sage/finance/fractal.pyx"         

drfft:howmany=726335489
drfft:howmany=644245095
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/finance/fractal.pyx", line 109, in __main__.example_1
Failed example:
    sim = finance.stationary_gaussian_simulation(s, N)[Integer(0)]###line 66:_sage_    >>> sim = finance.stationary_gaussian_simulation(s, N)[0]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        sim = finance.stationary_gaussian_simulation(s, N)[Integer(0)]###line 66:_sage_    >>> sim = finance.stationary_gaussian_simulation(s, N)[0]
      File "fractal.pyx", line 111, in sage.finance.fractal.stationary_gaussian_simulation (sage/finance/fractal.c:642)
      File "time_series.pyx", line 2172, in sage.finance.time_series.TimeSeries.fft (sage/finance/time_series.c:12114)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/scipy/fftpack/basic.py", line 179, in rfft
        return _raw_fft(tmp,n,axis,1,overwrite_x,work_function)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/scipy/fftpack/basic.py", line 49, in _raw_fft
        r = work_function(x,n,direction,overwrite_x=overwrite_x)
    error: (n*howmany==size(x)) failed for hidden howmany
**********************************************************************
<SNIP>
```
And

```
sage -t -long "devel/sage/sage/finance/time_series.pyx"     
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/finance/time_series.pyx", line 427, in __main__.example_15
Failed example:
    F = v.autoregressive_fit(Integer(100))###line 532:_sage_    >>> F = v.autoregressive_fit(100)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[4]>", line 1, in <module>
        F = v.autoregressive_fit(Integer(100))###line 532:_sage_    >>> F = v.autoregressive_fit(100)
      File "time_series.pyx", line 557, in sage.finance.time_series.TimeSeries.autoregressive_fit (sage/finance/time_series.c:4388)
      File "time_series.pyx", line 2378, in sage.finance.time_series.autoregressive_fit (sage/finance/time_series.c:12648)
      File "time_series.pyx", line 1865, in sage.finance.time_series.TimeSeries.numpy (sage/finance/time_series.c:10977)
    MemoryError
**********************************************************************
<SNIP>
```

Cheers,

Michael



---

archive/issue_comments_030518.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2008-12-09T08:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30518",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_030519.json:
```json
{
    "body": "Attachment [timeseries-64bit.patch](tarball://root/attachments/some-uuid/ticket4206/timeseries-64bit.patch) by mabshoff created at 2008-12-09 09:02:28\n\nPositive review for the last patch.\n\nMerge\n\n* vector-RDF-CDF-numpy-sage-3.2.1.patch\n* real_roots-import.patch\n* vector_fft.patch \n* timeseries-64bit.patch \n\nCheers,\n\nMichael",
    "created_at": "2008-12-09T09:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30519",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [timeseries-64bit.patch](tarball://root/attachments/some-uuid/ticket4206/timeseries-64bit.patch) by mabshoff created at 2008-12-09 09:02:28

Positive review for the last patch.

Merge

* vector-RDF-CDF-numpy-sage-3.2.1.patch
* real_roots-import.patch
* vector_fft.patch 
* timeseries-64bit.patch 

Cheers,

Michael



---

archive/issue_events_009531.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-09T09:40:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4206#event-9531"
}
```



---

archive/issue_comments_030520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-09T09:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030521.json:
```json
{
    "body": "Merged the above four patches in Sage 3.2.2.alpha1",
    "created_at": "2008-12-09T09:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4206#issuecomment-30521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged the above four patches in Sage 3.2.2.alpha1
