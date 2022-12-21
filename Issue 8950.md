# Issue 8950: new function for sage.calculus.desolve module

Issue created by migration from Trac.

Original creator: uri

Original creation time: 2010-05-11 15:51:19

Assignee: burcin

Keywords: desolve

I've done a new function, named desolve_numerical, that solves a system of first order differential equations numerically. It seems to be quite more efficient than the function desolve_system_rk4, included in the same module. It can be seen in the following example (Lotka-Volterra Equations):

sage: x,y,t=var('x,y,t') 
sage: des=[x*(1-y),-y*(1-x)]
sage: ics=[1,0.5] 
sage: times=srange(0,10.1,0.1)

With the new function we get: 

sage: timeit('desolve_numerical(des,ics,times,(x,y))') 
125 loops, best of 3: *5.81 ms per loop*

while with desolve_system_rk4 the result is:

sage: timeit('desolve_system_rk4(des,[x,y],ics=[0,1,0.5],ivar=t)') 
5 loops, best of 3: *558 ms per loop*


---

Attachment

Is this ready for review?


---

Comment by uri created at 2010-05-12 08:56:43

Yes, I think so. I've been using it for a while and I didn't find any problem. Automatic testing works also.

Replying to [comment:1 mvngu]:

> Is this ready for review?


---

Comment by mvngu created at 2010-05-12 10:53:06

Changing status from new to needs_review.


---

Comment by wdj created at 2010-05-12 21:20:50

Changing status from needs_review to needs_info.


---

Comment by wdj created at 2010-05-12 21:20:50

Just as a point of convention, typically new sage methods should have docstrings which illustrate all the options avaialble. So if there are optional arguments x, y, z, then there should be docstring examples illustrating these with non-default arguments. This method is great in the sense that it has a huge number of optional arguments. However, only a few of them are used in the examples. Could you please expand the examples to illustrate more of the optional variables?


---

Comment by uri created at 2010-05-16 19:33:11

Changing status from needs_info to needs_review.


---

Attachment

Ok, I added information of the optional parameters and an example using non default ones.

Replying to [comment:4 wdj]:

> Just as a point of convention, typically new sage methods should have docstrings which illustrate all the options avaialble. So if there are optional arguments x, y, z, then there should be docstring examples illustrating these with non-default arguments. This method is great in the sense that it has a huge number of optional arguments. However, only a few of them are used in the examples. Could you please expand the examples to illustrate more of the optional variables?


---

Comment by burcin created at 2010-05-24 11:42:15

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-05-24 11:42:15

Thanks for the patch, it looks like a good start.

Here are a few comments (not a formal review):

 * You should change your code to conform to the Python coding conventions: http://sagemath.org/doc/developer/conventions.html#python-coding-conventions
  In particular,
  * use 4 spaces for indentation
  * try not to have lines exceeding 80 characters (some of us use old fashioned command line editors)
  * change the ComputeJacobian argument.
 * Your function doesn't seem to do anything, comparing with the previous attachment:desolve_numerical.py a whole chunk of code starting with the `else` clause corresponding to the second `if` statement seems to be missing
 * You should use y[:] to copy a list
 * Other functions in the same file also solve differential equations numerically. Choosing a more specific name for your function might be more appropriate.

Someone who uses this functionality more often should comment on the content and the name of the function.


---

Attachment


---

Comment by uri created at 2010-06-30 08:59:40

After a while, I've been able to make the changes proposed by burcin (by the way, thanks for your suggestions):

 * use 4 spaces for indentation -> Done
 * try not to have lines exceeding 80 characters (some of us use old fashioned command line editors) -> Done, except for a line in the examples. I couldn't break that line, because then the automatic testing wouldn't work. I guess it's not a big deal, since it is not part of the code, though.
 * change the ComputeJacobian argument -> Done
 * Your function doesn't seem to do anything, comparing with the previous[attachment:desolve_numerical.py attachment:desolve_numerical.py] a whole chunk of code starting with the `else` clause corresponding to the second `if` statement seems to be missing -> I don't get your point here... I think there's no problem with the second if statement. Could you be more precise?
 * You should use y[:] to copy a list -> Done
 * Other functions in the same file also solve differential equations numerically. Choosing a more specific name for your function might be more appropriate. -> You're right. I changed the name to *desolve_odeint*, since the it uses the integrate function from odeint module (from scipy).



I will be grateful for any other comments!


---

Comment by uri created at 2010-06-30 08:59:40

Changing status from needs_work to needs_review.


---

Comment by pang created at 2010-07-20 06:46:28

Oriol, it seems that your trac_8950_desolve_numerical.2.patch is exactly the same as trac_8950_desolve_numerical.patch.


---

Comment by uri created at 2010-07-22 14:57:43

Thanks, I hadn't realised I just uploaded the old patch... 

I'll upload the correct one now, I hope I do it right this time :)


---

Comment by pang created at 2010-07-22 21:04:08

I got an error when applying your patch:


```
applying trac_8950_desolve_odeint.patch abort: malformed patch
```


The patch says: 


```
diff -r eb27a39a6df4 -r 15f9c1da9cc9 sage/calculus/desolvers.py
--- a/sage/calculus/desolvers.py	Wed Jan 20 15:09:32 2010 -0800
+++ b/sage/calculus/desolvers.py	Wed Jun 30 10:47:17 2010 +0200
`@``@` -1053,3 +1053,270 `@``@`
     sol.extend(sol_2)
 
     return sol
+
+def desolve_odeint(des, ics, times, dvars, ivar=None, compute_jac=False, args=()
```



but the file desolvers.py has now more lines, and sol.extend is now on line 1220, not on line 1053. I'm not an expert on version control, but this makes me think that the patch was not applied because I'm using a more recent version of Sage than the one you used when you exported the patch. Maybe if you upgrade before exporting the patch I'll be able to apply it. I've tried to modify the patch manually but failed.


---

Attachment

You were right, I had an old version of Sage. Now I've created the patch in the last version (4.5), so I think it should work. Please, let me know if everything is allright this time.

Thanks for your time!


---

Comment by pang created at 2010-07-28 19:48:14

The patch is a little weird now: it contains first the old one and then the same code, but with instructions to include it in a different place. I couldn't use it, and I think trac has trouble with it, too, because it doesn't render the patch if you click on it, like it does usually. I can produce a patch from a fresh install if you want, but let's talk about the content first:

It pretty much works, but:

1. I'm concerned about using the variable 't' if the argument ivar is not set explicitely. Is it safe to assume that nobody would use the name 't' for a dependent variable? Is it safe to assume that everybody would use the name 't' for the independent variable? I would prefer either of these two approaches:

 * Always require the parameter ivar
 * Use some code like in `desolve_system_rk4` to try to guess the independent var:

 1. compute all variables used in the functions passed as arguments:


```
all_vars = set([])

for de in des:
    all_vars.update(set(de.variables()))
```

 2. if there is exactly one variable in all_vars not in dvars, assume it is the independent var:
 2. if all_vars is contained in dvars, create an adhoc independent variable that is not used elsewhere. I've thought of a safe way to pick up a new var, which maybe overkill. It seems like this is not necessary thanks to the particular way in which fast_float works, but IMHO it's better to be on the safe side:
 2. otherwise raise an error


```
...
ivars = all_vars - set(dvars)
if len(ivars) == 1:
    ivar = ivars.pop()
elif not ivars:
    safe_name = 't_' + str(dvars)
    ivar = var(safe_name)
else:
    raise ...

```

Oriol: what's your opinion on this issue? 

2. I'd use:


```
J=diff(des,dvars)
```


instead of


```
J=jacobian(des,dvars)
J=J[0][0]
```


3. In my opinion, the parameters to ``odeint`` mu and ml should not be used. Those parameters do not make sense if you don't pass Dfun as an argument. But please correct me if I'm wrong.

4. I've introduced a few ``is_SymbolicVariable(dvars)`` tests. I think the test ``len(dvars)==0`` is a lousy test for a Symbolic Variable.

5. The documentation wasn't building correctly. Sphinx is a bit rigid, and we need to follow the indentation rules, etc. I've fixed that already.

I'm attaching a patch file with the changes above included. It probably won't merge cleanly into your Sage install, so I'm attaching the plain file desolvers.py directly. Please tell me what you think, and then we will ask for another reviewer.


---

Comment by pang created at 2010-07-28 19:48:14

Changing status from needs_review to needs_work.


---

Attachment


---

Attachment


---

Attachment

I just made a mistake you might find funny: I exported the patch to a file without deleting the file first, and then the changes were appended to the existing file. The resulting patch: ``trac_8950_desolve_odeint_2.patch`` contains duplicated information.

The patch ``trac_8950_desolve_odeint_3.patch`` is correct.


---

Comment by uri created at 2010-08-02 11:49:33

Thanks pang, I think the changes you've done are great! Here's my opinion:

Replying to [comment:12 pang]:

> 1. I'm concerned about using the variable 't' if the argument ivar is not set explicitely. Is it safe to assume that nobody would use the name 't' for a dependent variable? Is it safe to assume that everybody would use the name 't' for the independent variable? 

Yes, I think you're right, it's not safe to use the name 't' as default for the independent variable.


> I would prefer either of these two approaches:
> 
>  * Always require the parameter ivar
>  * Use some code like in `desolve_system_rk4` to try to guess the independent var:

I prefer the second approach, because in a lot of cases the independent variable is in fact (almost) meaningless. Besides, the code you've written is great, and I think it should work perfectly (well I've made a small correction, I'll explain later).


> 2. I'd use:
> 
> {{{
> J=diff(des,dvars)
> }}}
> 
> instead of
> 
> {{{
> J=jacobian(des,dvars)
> J=J[0][0]
> }}}

I agree, I just didn't think about that.


> 3. In my opinion, the parameters to ``odeint`` mu and ml should not be used. Those parameters do not make sense if you don't pass Dfun as an argument. But please correct me if I'm wrong.

Again, totally agree.


> 4. I've introduced a few ``is_SymbolicVariable(dvars)`` tests. I think the test ``len(dvars)==0`` is a lousy test for a Symbolic Variable.

I still don't really understand why you don't like the test ``len(dvars)==0``, but it's true that the ``is_SymbolicVariable(dvars)`` test is more elegant. By the way, the first ``len(dvars)==0`` test is still there; is there any reason why the other one cannot be used?


> 5. The documentation wasn't building correctly. Sphinx is a bit rigid, and we need to follow the indentation rules, etc. I've fixed that already.

Thanks, I didn't know that.


I attach a new patch (trac_8950_odeint_4.patch), because I made some small changes:

1. In the documentation, the description of 'ivar' said ' default is t', which is not anymore, so I changed it to just 'optional'.

2. In one of the examples there was a mistake, because it used the time vector 'times' which was defined in a previous example and not the one that was defined in it, which was called 't'.

3. At the beggining there was:


```
if ivar==None:
    if len(dvars)==0 or len(dvars)==1:
        all_vars = set(des.variables())
    else:
        ...
```


However, in the case that ``len(dvars)==1`` is true, 'des.variables()' will give an error. So instead I wrote:

```
if ivar==None:
    if len(dvars)==0 or len(dvars)==1:
        if len(dvars)==1:
            des=des[0]
            dvars=dvars[0]
        all_vars = set(des.variables())
    else:
        ...
```


As the redefinition 'dvars=dvars[0]' was already done afterwards, I moved it to here for simplicity.

Please, let me know your opinion. And thanks again for your work!


---

Attachment


---

Comment by uri created at 2010-08-03 16:23:26

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-06 19:28:36

Is it possible to have a unified patch?  It is very difficult to follow exactly what is happening for someone who just discovered this ticket :)  

Also, this is the Scipy one, correct?  Is there also a GSL desolver which could be wrapped and put here (I think the current ones are all from Maxima)?  That would be very natural, or perhaps as an `algorithm=` argument.


---

Comment by uri created at 2010-08-09 14:40:55

Replying to [comment:16 kcrisman]:
> Is it possible to have a unified patch?  It is very difficult to follow exactly what is happening for someone who just discovered this ticket :)  

I attached the file trac_8950_desolve_odeint_unified_4.patch, it contains all the changes contained in the previous patches. I'll be glad to hear your opinion!

> Also, this is the Scipy one, correct?  Is there also a GSL desolver which could be wrapped and put here (I think the current ones are all from Maxima)?  That would be very natural, or perhaps as an `algorithm=` argument.

Yes, this is the Scipy one. I think the class ode_solver uses the GSL desolver. I'm not sure if it's necessary to put it here too... however, I did a routine to initialize this class (from my point of view the initialization is a little bit tedious, particularly if you want to use symbolic functions but still want it to be fast). It needs some improvement though, when I finish it I'll tell you :)


---

Comment by mhampton created at 2010-08-30 20:51:58

This looks good to me - applied cleanly on sage-4.5.3.alpha1, seems to work well, documentation for the reference manual looks fine.

I am going to give this a positive review, but if you previously reviewed this you might want to take a final look and make sure I'm not missing anything.


---

Comment by mhampton created at 2010-08-30 20:51:58

Changing status from needs_review to positive_review.


---

Comment by uri created at 2010-08-31 11:34:01

Replying to [comment:18 mhampton]:
> This looks good to me - applied cleanly on sage-4.5.3.alpha1, seems to work well, documentation for the reference manual looks fine.
> 
> I am going to give this a positive review, but if you previously reviewed this you might want to take a final look and make sure I'm not missing anything.

Great, thanks. Maybe pang or kcrisman have some comments still.


---

Comment by mpatel created at 2010-09-05 03:40:35

Which patch(es) should the release manager merge?  The attachment [attachment:trac_8950_desolve_odeint_unified_4.patch] is missing a Mercurial header.  In case it helps: [This wiki page](http://wiki.sagemath.org/MercurialQueues) shows how to fold together multiple patches.

Also, can someone fill in the "Reviewer(s)" field?


---

Comment by mpatel created at 2010-09-05 03:40:35

Changing status from positive_review to needs_work.


---

Comment by uri created at 2010-09-07 14:24:58

Changing status from needs_work to needs_review.


---

Comment by uri created at 2010-09-07 14:24:58

Replying to [comment:20 mpatel]:
> Which patch(es) should the release manager merge?  The attachment [attachment:trac_8950_desolve_odeint_unified_4.patch] is missing a Mercurial header.  In case it helps: [This wiki page](http://wiki.sagemath.org/MercurialQueues) shows how to fold together multiple patches.

Thanks for the help. Now [attachment:trac_8950_desolve_odeint_unified_4.patch] contains the Mercurial header. This is the patch that the release manager should merge.


---

Comment by mpatel created at 2010-09-07 14:44:03

Replying to [comment:21 uri]:
> Thanks for the help. Now [attachment:trac_8950_desolve_odeint_unified_4.patch] contains the Mercurial header. This is the patch that the release manager should merge.

Could you check this?  I still see a header-less patch.


---

Comment by uri created at 2010-09-07 15:12:32

Replying to [comment:22 mpatel]:
> Replying to [comment:21 uri]:
> > Thanks for the help. Now [attachment:trac_8950_desolve_odeint_unified_4.patch] contains the Mercurial header. This is the patch that the release manager should merge.
> 
> Could you check this?  I still see a header-less patch.

You're right, I must have re-uploaded the old patch, sorry. Now it's the correct one.


---

Comment by mpatel created at 2010-09-07 15:16:47

Great!  Could you fix the commit string so that the first line contains the ticket number and a brief (< 80 characters) summary of the changes?  We need to do this to keep `hg log` output informative.  Of course, additional explanatory lines are definitely allowed in the commit string; they'll be displayed by `hg log -p`.


---

Attachment

Replying to [comment:24 mpatel]:
> Great!  Could you fix the commit string so that the first line contains the ticket number and a brief (< 80 characters) summary of the changes?  We need to do this to keep `hg log` output informative.  Of course, additional explanatory lines are definitely allowed in the commit string; they'll be displayed by `hg log -p`.

I'm not sure I did what you asked for: I created the patch again but edited the commit string using the "-e" command. Is that correct?


---

Comment by mpatel created at 2010-09-07 15:46:14

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-07 15:46:14

Replying to [comment:25 uri]:
> Replying to [comment:24 mpatel]:
> > Great!  Could you fix the commit string so that the first line contains the ticket number and a brief (< 80 characters) summary of the changes?  We need to do this to keep `hg log` output informative.  Of course, additional explanatory lines are definitely allowed in the commit string; they'll be displayed by `hg log -p`.
> 
> I'm not sure I did what you asked for: I created the patch again but edited the commit string using the "-e" command. Is that correct?

Yes, that works.  Thanks!


---

Comment by mpatel created at 2010-09-15 11:13:32

Resolution: fixed
