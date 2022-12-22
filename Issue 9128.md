# Issue 9128: Sphinx should be aware of all.py to find its links

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-06-03 12:47:46

Assignee: mvngu

CC:  nthiery leif novoselt mhansen

Keywords: Sphinx links

Though sphinx is perfectly working with target in the local module he isn't
able to find reference target from other modules even if they are exported in
all.py. For example, if I want to link Parent from anywhere but parent.pyx, I
have to write the full path (ie. `:class:`~sage.structure.parent.Parent``)
even if it is imported in my module. I find this extremely annoying since, in
the task of improving the category doc, I'm setting up a lot of huge cross
references such as:

```
    :meth:`Algebras.ParentMethods.algebra_generators()
    <sage.categories.algebras.Algebras.ParentMethods.algebra_generators>`.
```

I would be very happy if I had to write only

```
    :meth:`Algebras.ParentMethods.algebra_generators`
```

The following patch should solve this issue


---

Comment by hivert created at 2010-06-03 12:51:26

The patch here is a prototype, not yet ready for review. Comments or suggestions are mostly welcome.


---

Comment by hivert created at 2010-06-03 12:51:26

Changing assignee from mvngu to hivert.


---

Comment by hivert created at 2010-06-03 12:51:33

Changing status from new to needs_work.


---

Comment by hivert created at 2010-06-03 22:22:30

The submitted patch seems to behave as I want. So I put needs review. However if I receive some good advice on sage-devel or sphinx-users I may still change it. Anyway, Please comment.


---

Comment by hivert created at 2010-06-03 22:22:30

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-06-07 02:14:02

I have just upgraded an installation of sage-4.4.2 to 4.4.3, applied this patch, set SAGE_DOC_WARN_DANGLING_LINKS to 1, and then got the following error:

```
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -docbuild reference html
sphinx-build -b html -d /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/doctrees/en/reference    /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/en/reference /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 798 source files that are out of date
updating environment: [config changed] 802 added, 0 changed, 0 removed
reading sources... [100%] structure
/mnt/usb1/scratch/novoselt/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [  0%] coercion
Exception occurred:
  File "/mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/conf.py", line 444, in find_sage_dangling_links
    fromdocname = getattr(sys.modules[modname], basename).__module__
KeyError: None
The full traceback has been saved in /tmp/sphinx-err-Unu279.log, if you want to report the issue to the author.
Please also report this if it was a user error, so that a better error message can be provided next time.
Send reports to sphinx-dev`@`googlegroups.com. Thanks!
Build finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$
```

Then I removed this patch, built documentation successfully, pushed this and some other patches and now it seems to work fine. Perhaps it was an unreproducible glitch unrelated to the patch. In general it seems to work as expected and showed me a couple of mistakes in my modules.

I hesitate to switch status to positive review because of the error above and because I don't really understand the code, but I think that this is a great addition and will use this patch from now on!


---

Comment by novoselt created at 2010-06-07 02:53:52

I tried the same thing on my own computer - upgraded from 4.4.2 to 4.4.3, applied this patch and tried to build documentation (without setting the environment variable this time). Same error repeatedly, but after popping the patch out everything goes OK. So something has to be done ;-)


---

Comment by novoselt created at 2010-06-07 02:53:52

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-06-07 16:06:55

Hi Andrey

Replying to [comment:7 novoselt]:
> I tried the same thing on my own computer - upgraded from 4.4.2 to 4.4.3, applied this patch and tried to build documentation (without setting the environment variable this time). Same error repeatedly, but after popping the patch out everything goes OK. So something has to be done ;-)

Thanks for looking at that. My patch was working for `.py` and `.pyx`
file but not `.rst` file. The new updated file should work. I didn't get
any comment from `#sphinx-devel` except that `missing-reference` is
the good entry point. So except if some expert pop up and suggest some more
improvements, I consider this proposal as a good one. Please review.


---

Comment by hivert created at 2010-06-07 16:06:55

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-06-07 20:00:45

Now I upgraded from 4.4.3 to 4.4.4.alpha0. The new patch works better, but not perfect:

```
WARNING: undefined symbol :meth:`dual` in module sage.categories.dual
writing output... [ 13%] sage/categories/examples/algebras_with_basis
Exception occurred:
  File "/mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/conf.py", line 453, in find_sage_dangling_links
    current_module = sys.modules[modname]
KeyError: u'sage.categories.examples.algebras_with_basis'
The full traceback has been saved in /tmp/sphinx-err-rFQQUv.log, if you want to report the issue to the author.
Please also report this if it was a user error, so that a better error message can be provided next time.
Send reports to sphinx-dev`@`googlegroups.com. Thanks!
Build finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
```



---

Comment by hivert created at 2010-06-07 20:36:36

Replying to [comment:9 novoselt]:
> Now I upgraded from 4.4.3 to 4.4.4.alpha0. The new patch works better, but not perfect:

Hum ! I know how to workaround those problems but I don't understand why this is happening ! Unfortunately, I don't want to upgrade and I can't reproduce the bug... Can you try to remove the directory `$SAGE_ROOT/devel/sage/doc/output` and relaunch the compilation. Does it still bug ? 

Florent


---

Comment by novoselt created at 2010-06-07 22:34:03

Successful built with 552 warnings!


---

Comment by novoselt created at 2010-06-08 15:33:40

While working on my patches, I am getting the following from this one:

```
WARNING: undefined symbol :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice` in module sage.geometry.cone 
```

I don't understand what is wrong. There are no typos and this module does exist in my installation. Is it because I don't import this class/module? Or because it is an underscore method and so there is no record of it in the documentation? (In this case, I actually make a reference to the source code of this method, so I just want the name to be typeset in the same way as other methods, I don't care that the link will not work.)


---

Comment by hivert created at 2010-06-08 17:03:07

Replying to [comment:12 novoselt]:
> While working on my patches, I am getting the following from this one:
> {{{
> WARNING: undefined symbol :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice` in module sage.geometry.cone 
> }}}
> I don't understand what is wrong. There are no typos and this module does exist in my installation. Is it because I don't import this class/module? Or because it is an underscore method and so there is no record of it in the documentation? (In this case, I actually make a reference to the source code of this method, so I just want the name to be typeset in the same way as other methods, I don't care that the link will not work.)

Hi Andrey,

Thanks for beta testing my patch ! It this module included in the documentation ? More precisely is there a link in some `.rst` file (probably `doc/en/reference/geometry.rst`) ? Because if it is not imported nor linked from the doc, Sphinx as no way to find it but importing the module. This is something I tried to avoid for performance reason... If you are still having some problem, can you please make your patch accessible so that I can debug with it. I don't care if the code is not working...

You probably already figured that out, but I must confess that I put this patch here for comment but it is clear that it has not sufficiently been shaken. So many thanks for helping me on that and sorry to cause some trouble.


---

Comment by novoselt created at 2010-06-08 22:14:34

Hi Florent!

I have figured out that the problem is with the underscore - if I use a "common" method from the same non-imported patch, link is determined just fine.

It may be a good idea not to give warnings in such cases, but on the other hand it is probably quite rare and there is no need to make logic of this patch more convoluted. (In my case the docstring of one of the functions says "see the source code of ... for more involved examples", since those examples cannot be easily written as standalone code and I didn't want to write something "involved, but artificial.")

Since I really like this functionality, I will continue using your patch (and its fresh versions if they become available) and report new problems, if there will be any. But for the final review we will need someone else, since I don't know how Sphinx works and cannot comment on the code itself.

Thank you!
Andrey


---

Comment by hivert created at 2010-06-11 15:27:23

> It may be a good idea not to give warnings in such cases, but on the other hand it is probably quite rare and there is no need to make logic of this patch more convoluted. (In my case the docstring of one of the functions says "see the source code of ... for more involved examples", since those examples cannot be easily written as standalone code and I didn't want to write something "involved, but artificial.")

Can you describe more precisely what's happening ? Maybe with a very small example... I'm not sure to understand what you are doing... I have the impression that you are requesting me to remove warnings about private methods (i.e.: starting with underscore). 
 
> Since I really like this functionality, I will continue using your patch (and its fresh versions if they become available) and report new problems, if there will be any. But for the final review we will need someone else, since I don't know how Sphinx works and cannot comment on the code itself.

I'll try to ping some on sage-devel.


---

Comment by novoselt created at 2010-06-11 15:42:55

I think that I want to have a distinction between "totally wrong names" and names which were successfully found in the Sage library (therefore, it makes sense to reference them), but do not have corresponding entries in the documentation files (therefore, it is not possible to convert them into a working hyperlink). Private/underscore methods are one example (I would like actually to seem them in the documentation "on demand", but maybe there are arguments against it), another is reference to objects in modules which are not included into documentation (maybe there will be no such modules eventually). I hope this is more clear, but in any way it is a small point.


---

Comment by hivert created at 2010-06-11 15:56:42

Replying to [comment:16 novoselt]:
> I think that I want to have a distinction between "totally wrong names" and names which were successfully found in the Sage library (therefore, it makes sense to reference them), but do not have corresponding entries in the documentation files (therefore, it is not possible to convert them into a working hyperlink). Private/underscore methods are one example (I would like actually to seem them in the documentation "on demand", but maybe there are arguments against it), another is reference to objects in modules which are not included into documentation (maybe there will be no such modules eventually). I hope this is more clear, but in any way it is a small point.

This should be exactly what I'm doing: I issue two different kinds of warning:
 
 - `undefined symbol :%s:`%s` in %s` 
 - `symbol :%s:`%s` linked from %s is defined in %s but not documented`

Bu maybe sometime I fail finding a symbol and therefore issue the first warning instead of the second one... Is this happening for you ? 

Florent


---

Comment by novoselt created at 2010-06-11 19:12:03

I get the first kind of warning and now the class is actually imported (although in the end of the module to avoid circular imports).

I have just uploaded a fresh patch to #8987 (so fresh, that it is actually very raw ;-)) if you want to reproduce the issue. Beware that it is a chain of patches, I think it is possible to apply only those listed in #9062, #8986, and #8987 (especially if you are working with 4.4.4.alpha0, where all prerequisites but one are merged).


---

Comment by novoselt created at 2010-06-15 19:15:13

I have discovered that

```
:class:`tuple`
```

in the documentation translates now into a black link

```
__builtin__.tuple
```

in the output. I think it would be better to display links exactly as they were written originally and "expand" only the actual link, if it is working.


---

Comment by hivert created at 2010-06-16 08:28:32

Replying to [comment:19 novoselt]:
> I have discovered that

```
:class:`tuple`
```

> in the documentation translates now into a black link

```
__builtin__.tuple
```

> in the output. I think it would be better to display links exactly as they were written originally and "expand" only the actual link, if it is working.

Yes ! That was before I know how to resolve those with `intersphinx`. See my new patches


---

Comment by hivert created at 2010-06-16 10:57:15

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-06-16 10:57:15

Replying to [comment:20 hivert]:
> Yes ! That was before I know how to resolve those with `intersphinx`. See my new patches

There is still a problem: currently when linking to python, I raise a warning *before* intersphinx tries to find the link in Python's database.


---

Comment by hivert created at 2010-06-17 20:37:45

> There is still a problem: currently when linking to python, I raise a warning *before* intersphinx tries to find the link in Python's database.

Some update: It is not possible to achieve what I want in Sphinx 0.6 without hacking into sphinx. However Sphinx 1.0 should be out very soon (they released 1.0beta2 last week). At raising warning is builtin in sphinx 1.0 with the correct configuration option. So I'll probably wait until sphinx 1.0 is out to finish this one, unless someone insist to have it very soon.


---

Comment by novoselt created at 2010-06-17 20:47:09

My opinion is that upgrading Sphinx is the way to go, it may have other benefits (and hopefully no drawbacks). I really want this functionality but I am quite happy with the availability of these patches here, thank you for writing them, Florent! 

Andrey


---

Comment by hivert created at 2010-06-18 11:59:41

For the record, here is another bad side effect of this patch: 

```
sage: PolynomialRing?

Type:		function
Base Class:	<type 'function'>
String Form:	<function PolynomialRing at 0x16a2758>
Namespace:	Interactive
File:		/usr/devel/sage/sage/rings/polynomial/polynomial_ring_constructor.py
Definition:	PolynomialRing(base_ring, arg1=None, arg2=None, sparse=False, order='degrevlex', names=None, name=None, implementation=None)
Docstring:
    <no docstring>
```



---

Comment by novoselt created at 2010-08-25 00:33:46

Is it possible to display line numbers in warnings about bad links?


---

Comment by novoselt created at 2010-12-16 16:15:37

I guess it was expected: these patches do not work anymore in Sage-4.6.1.alpha3 due to Sphinx upgrade. On a fresh installation I got

```
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$ hg qapplied
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$ hg qpush
applying trac_9128-sphinx_links_all-fh.patch
now at: trac_9128-sphinx_links_all-fh.patch
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$ hg qpush
applying trac_9128-intersphinx_python_database-fh.patch
now at: trac_9128-intersphinx_python_database-fh.patch
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -b
...
novoselt`@`sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -docbuild reference html
sphinx-build -b html -d /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/doctrees/en/reference    /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/en/reference /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
Running Sphinx v1.0.4
loading pickled environment... done
loading intersphinx inventory from /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/python-inv.txt...
building [html]: targets for 1 source files that are out of date
updating environment: [extensions changed] 882 added, 0 changed, 0 removed
reading sources... [100%] tensor                                                                                                                              
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [  0%] coercion                                                                                                                             
Exception occurred:
  File "/mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/conf.py", line 446, in find_sage_dangling_links
    modname = nodeattr['modname']
KeyError: 'modname'
The full traceback has been saved in /tmp/sphinx-err-5Yrzg5.log, if you want to report the issue to the developers.
Please also report this if it was a user error, so that a better error message can be provided next time.
Either send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,
or report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!
Build finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
```



---

Comment by hivert created at 2011-04-27 21:17:25

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2011-04-27 21:17:25

I upgraded my patch to the new sphinx. I'm not sure the patch is completely finished but I'd be very interesting to have feedback.


---

Comment by novoselt created at 2011-04-30 04:27:09

Hi Florent,

I have enjoyed using your patch in the past and I am going to start using it again but so far it does not apply to sage-4.7.rc0:

```
novoselt`@`tx2-LM:~/sage/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9128/trac_9128-intersphinx_python_database-fh.patch
adding trac_9128-intersphinx_python_database-fh.patch to series file
novoselt`@`tx2-LM:~/sage/devel/sage-main$ hg qpush
applying trac_9128-intersphinx_python_database-fh.patch
now at: trac_9128-intersphinx_python_database-fh.patch
novoselt`@`tx2-LM:~/sage/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9128/trac_9128-sphinx_links_all-fh.patch
adding trac_9128-sphinx_links_all-fh.patch to series file
novoselt`@`tx2-LM:~/sage/devel/sage-main$ hg qpush
applying trac_9128-sphinx_links_all-fh.patch
patching file doc/common/conf.py
Hunk #2 FAILED at 19
Hunk #3 succeeded at 97 with fuzz 2 (offset -7 lines).
1 out of 6 hunks FAILED -- saving rejects to file doc/common/conf.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_9128-sphinx_links_all-fh.patch
novoselt`@`tx2-LM:~/sage/devel/sage-main$ 
```

This is on a just built installation without any other patches.


---

Comment by hivert created at 2011-04-30 13:21:40

Hi Andrey,

Replying to [comment:30 novoselt]:
> I have enjoyed using your patch in the past and I am going to start using it again but so far it does not apply to sage-4.7.rc0:

Oops !!! I should have said that this depend on #11251. Thanks for pointing it out and for testing my patch.


---

Comment by hivert created at 2011-05-02 13:15:47

I updated a little my patch to make sure that the reference guide is compiled first. This is needed so that other documentation can link to the reference guide. Please review.


---

Comment by hivert created at 2011-06-13 20:28:50

Hi Mike, 

I just added you in CC remembering that you are the Sphinx expert. If you can be kind enough to give me some feedback on that one, I'd very appreciate. It was a very though one for me as sphinx doesn't expose the necessary interface. So I had to dig in the internal. I think it is very useful and it could greatly help improving the documentation. 

Thanks for your help.


---

Comment by jhpalmieri created at 2011-09-24 18:10:31

By the way, note that #6495 also touches some of the same files, and for builder.py, in a conflicting way.  I think that #6495 could be rebased on top of this one.


---

Comment by jhpalmieri created at 2011-09-24 18:12:02

Replying to [comment:35 jhpalmieri]:
> By the way, note that #6495 also touches some of the same files, and for builder.py, in a conflicting way.  I think that #6495 could be rebased on top of this one.

(Although I'm not sure, since #6495 completely changes how the reference manual is built.  Can you take a look at that one to see what you think and whether the two approaches can be combined?)


---

Comment by novoselt created at 2012-02-15 22:27:42

Patches do not apply anymore on top of Sage-5.0.beta4. (Perhaps because of recent :trac: addition in another ticket?) What are actually the plans for this ticket?..


---

Comment by hivert created at 2012-02-15 22:34:12

Replying to [comment:37 novoselt]:
> Patches do not apply anymore on top of Sage-5.0.beta4. (Perhaps because of recent :trac: addition in another ticket?) What are actually the plans for this ticket?..

Yes there is a conflict with :trac:. I have a rebased patch in the sage-combinat queue which should applies. However I didn't test if it still works. I check it tomorrow and repost it. I'll be more that happy to have a review for this one. It has been a huge pain to get to a working solution, so I'll end up very frustrated if it goes to the garbage.

Florent


---

Comment by hivert created at 2012-02-18 11:11:46

Hi there,

I'm uploading two new patches:
 
 - `trac_9128-intersphinx_python_database-fh.patch` updated to Python 2.7
 
 - `trac_9128-sphinx_links_all-fh.patch` rebased for Sage-5.0.alpha4 and in particular on top of #12490 which was previously in this ticket.

As I already said, I'm not sure if this should enter Sage in the present status but I need a Sphinx expert (if not George Brandl himself) to try to polish and simplify my code. However, I think the feature is quite important in order to improve Sage's doc, so I suggest that if no expert jump up to let the code enter Sage as such and to improve it in a former ticket. I therefore leave it as need-review.


---

Attachment

+1 on getting it merged in 5.0, that is as soon as possible! As it is, it already helps much improving the Sage documentation, and it can be improved later. Besides, we want to use it for working with the Sage-Combinat patches, but it's a pain to have it in the queue since it forces recompiling all the documentation.

I have been through the patch, and it looks reasonnable, though I am not by far a Sphinx expert. Just a detail: several of the functions do not have doctests. Now I am not sure if it is anyway really possible to doctest them; if not, I guess that's ok as is.

Andrei or John: would you agree to put a positive review?

Cheers,
                           Nicolas


---

Comment by novoselt created at 2012-02-18 15:51:49

I never tried to figure out how Sphinx works, so I cannot say much about the code itself. However, I have been following this ticket from the very beginning, having it on the top of my queue whenever it was cleanly applicable. I have never had any issues with it and it helped me to catch some dangling links. I didn't try to use it for short links in documentation, since I didn't want to be dependent on this ticket, but I surely do want to avoid figuring out and typing every full path. This also makes the documentation resistant to refactoring and moving functions around.

So - as a user I like this patch a lot, give it positive review, and vote for inclusion as is!


---

Comment by hivert created at 2012-02-18 18:54:26

> I have been through the patch, and it looks reasonnable, though I am not by far a Sphinx expert. Just a detail: several of the functions do not have doctests. Now I am not sure if it is anyway really possible to doctest them; if not, I guess that's ok as is.

Unfortunately, I've no idea how to doctests those. As you can see from the
code, I wrote my patch using log backtrace and `pdb`. At several point,
I'm using call to sphinx or docutils internal which are not really
documented. So this is some kind of reverse engineering. I tried several time
to ask for some help on sphinx-user and never got any answer on that. My
diagnostic is that Sphinx doesn't expose a sufficiently flexible API to
achieve what we want.

Probably a good solution would be to have a Sage-days whose subject is Sphinx
and doc-compiling and invite George Brandl. We could also solve the Sphinx
parallel build ticket at the same occasion. Unfortunately, I just organized a
Sage-days and I'm invited to two other until summer so I won't organize such a
days and if organized, I don't think I'll be able to attend.

By the way, I'll CC this on Sage-devel.


---

Comment by hivert created at 2012-02-18 19:54:46

I just added the following diff which should resolve many more dependance to python itself.

```diff
diff --git a/doc/common/conf.py b/doc/common/conf.py
--- a/doc/common/conf.py
+++ b/doc/common/conf.py
`@``@` -490,6 +490,11 `@``@` def call_intersphinx(app, env, node, con
         debug_inf(app, "---- Intersphinx: %s not Found"%node['reftarget'])
     return res
 
+# lists of basic Python class which are documented as functions
+base_class_as_func = [
+    'bool', 'complex', 'dict', 'file', 'float',
+    'frozenset', 'int', 'list', 'long', 'object',
+    'set', 'slice', 'str', 'tuple', 'type', 'unicode', 'xrange']
 
 def find_sage_dangling_links(app, env, node, contnode):
     """
`@``@` -507,9 +512,9 `@``@` def find_sage_dangling_links(app, env, n
 
     debug_inf(app, "Searching %s from %s"%(reftarget, doc))
 
-    # Workaround: in Python's doc 'object' is documented as a function rather
-    # than a class
-    if reftarget == 'object' and reftype == 'class':
+    # Workaround: in Python's doc 'object', 'list', ... are documented as a
+    # function rather than a class
+    if reftarget in base_class_as_func and reftype == 'class':
         node['reftype'] = 'func'
 
     res = call_intersphinx(app, env, node, contnode)
```



---

Comment by hivert created at 2012-02-19 00:56:09

The way we called Sphinx, it wasn't honoring the `SPHINXOPTS` environment variable anymore. As a consequence option `-n` wasn't working anymore. I just uploaded a patch which fixes this. Maybe this should be added to the dev-guide.


---

Comment by nthiery created at 2012-02-19 10:37:27

Ok, unless someone comments before that, I'll set a positive review tomorrow morning.


---

Comment by nthiery created at 2012-02-20 14:58:50

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2012-02-20 15:55:43

Changing status from positive_review to needs_work.


---

Comment by hivert created at 2012-02-20 15:55:43

There is a little problem in the handling of the environment + Usefull sphinx options should be better documented. I need to rework this a little.

Florent


---

Comment by hivert created at 2012-02-20 17:00:37

Changing status from needs_work to needs_review.


---

Attachment

Hi there,

I finalized the doc of this patch. I also took the chance to add a extra option 'warn-links' which make Sphinx complains for dangling links. To ease the review, I uploaded my changes in [attachment:trac_9128-doc_option-fh.patch]. Those changes are folded in [attachment:trac_9128-sphinx_links_all-fh.patch] so that you only need to apply this one and the database patch.


---

Attachment


---

Comment by nthiery created at 2012-02-20 17:33:05

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2012-02-20 17:33:05

I made two last minor changes to Florent's patch, with his agreement, and reposted it.
Good to go!


---

Comment by jdemeyer created at 2012-02-22 14:49:24

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-22 14:49:24

Unfortunately, this breaks the pdf reference manual:

```
! TeX capacity exceeded, sorry [main memory size=1500000].
<argument> ...\endcsname \current`@`color {0.40,0.40
                                                  ,0.40}\set`@`color
l.47055 ...1}\PYG{o}{/}\PYG{l+m+mf}{0.1}\PYG{p}{)}

!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on reference.log.
make[1]: *** [reference.pdf] Error 1
make[1]: Leaving directory `/mnt/usb1/scratch/jdemeyer/merger/sage-5.0.beta5-9128/devel/sage-main/doc/output/latex/en/reference'
Build finished.  The built documents can be found in /mnt/usb1/scratch/jdemeyer/merger/sage-5.0.beta5-9128/devel/sage/doc/output/pdf/en/reference
```


This is using

```
$ latex --version
pdfTeX using libpoppler 3.141592-1.40.3-2.2 (Web2C 7.5.6)
kpathsea version 3.5.6
Copyright 2007 Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
Kpathsea is copyright 2007 Karl Berry and Olaf Weber.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the pdfTeX using libpoppler copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the pdfTeX using libpoppler source.
Primary author of pdfTeX using libpoppler: Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
Kpathsea written by Karl Berry, Olaf Weber, and others.

Compiled with libpng 1.2.15beta5; using libpng 1.2.15beta5
Compiled with zlib 1.2.3.3; using zlib 1.2.3.3
Compiled with libpoppler version 3.00

```


From Googling around, this might not even be fixable without recompiling LaTeX or at least changing LaTeX's configuration files.


---

Comment by jdemeyer created at 2012-02-22 16:25:13

Let me clarify that this happened on sage.math, where the memory size is set to 1500000.  On a different system with 3000000 as limit, it compiled.  The end of that pdflatex log file shows:

```
Here is how much of TeX's memory you used:
 59038 strings out of 494632
 2184818 string characters out of 3923881
 1820512 words of memory out of 3000000
 34726 multiletter control sequences out of 10000+50000
 99604 words of font info for 164 fonts, out of 3000000 for 5000
 298 hyphenation exceptions out of 8191
 43i,25n,51p,6802b,946s stack positions out of 5000i,500n,10000p,200000b,50000s
```


I don't really see a solution besides requiring people to change their LaTeX installs, or splitting up the reference manual (would #6495 fix this?)


---

Comment by jhpalmieri created at 2012-02-22 17:47:44

#6495 might fix this, since it breaks the reference manual up into smaller pieces.  The only question is whether the pieces are small enough...


---

Comment by hivert created at 2012-02-22 19:08:54

Hi,

Replying to [comment:51 jdemeyer]:
> Let me clarify that this happened on sage.math, where the memory size is set
> to 1500000.  On a different system with 3000000 as limit, it compiled.  The
> end of that pdflatex log file shows:

*`\begin{GROUMPH}`*
First of all, I need to express my feelings: Fucking Sphinx, Fucking
Latex. None of these two software where seriously designed to scale to a
project of Sage size. That's a shame.

While I'm at it, fucking Sagemath distro. It worked without any problem on my
laptop.
*`\end{GROUMPH}`*

Sorry for this non useful comment.

I'm quite angry and frustrated because what my patch does is only to fix a
huge bunch of missing links in Sage doc way before they are sent to the
docutil writer for HTML or TeX. My patch is working at the level of docutil
abstract syntax tree, but I could have fixed those link by editing Sage source
as well.  This means that *if* the doc of Sage was correct, it *won't* compile
either ! And now because I tried to fix the doc, I'm asked to fix LaTeX. I
don't think it is really fair.

> I don't really see a solution besides requiring people to change their LaTeX
> installs, or splitting up the reference manual (would #6495 fix this?)

This also means that, whether or not we apply this patch, we *will* hit the
same problem again, as the doc of Sage is expected to grow.

-------

Let's try to be more constructive. I see several solution:

- add a comment in Sage installation instructions saying that TeX limitation
should be enhanced to compile the PDF doc (by the way, are there any people
really using the PDF doc out there ?)

- is it really a hard limitation. Couldn't this be fixed by a shell variable ?
I had the following script in my `~/bin` when I was using `XY-pic`:

```
popcorn-*binat/doc/common $ cat ~/bin/hugetex
#!/bin/sh
#####################################
# Boosted TeX to compile withc XY-pic
export extra_mem_bot=8000000; tex $*
```

Jeroen: will you be so kind to try if this works ?

- I can maybe disable my link fixing code when we are compiling to PDF, but I
think this is really a temporary bugware solution. Considering the time I
already lost on this ticket and the fact that this doesn't solve the problem
but barely hide it, I don't think this is an acceptable solution.

Florent


---

Comment by hivert created at 2012-02-22 19:16:38

Hi,

Replying to [comment:51 jdemeyer]:
> Let me clarify that this happened on sage.math, where the memory size is set
> to 1500000.  On a different system with 3000000 as limit, it compiled.  The
> end of that pdflatex log file shows:

*`\begin{GROUMPH}`*

First of all, I need to express my feelings: Fucking Sphinx, Fucking
Latex. None of these two software where seriously designed to scale to a
project of Sage's size. That's a shame.

While I'm at it, fucking Sagemath distro. It worked without any problem on my
laptop.

*`\end{GROUMPH}`*

Sorry for this non useful comment.

I'm quite angry and frustrated because what my patch does is only to fix a
huge bunch of missing links in Sage doc, way before they are sent to the
docutil writer for HTML or TeX. My patch is working at the level of docutil
abstract syntax tree, but I could have fixed those link by editing Sage source
as well.  This means that *if* the doc of Sage was correct, it
*wouldn't* compile either ! And now because I tried to fix the doc, I'm
asked to fix LaTeX. I don't think it is really fair.

> I don't really see a solution besides requiring people to change their LaTeX
> installs, or splitting up the reference manual (would #6495 fix this?)

This also means that, whether or not we apply this patch, we *will* hit the
same problem again, as the doc of Sage is expected to grow.

-------

Let's try to be more constructive. I see several solutions:

- add a comment in Sage installation instructions saying that TeX limitation
should be enhanced to compile the PDF doc (by the way, are there any people
really using the PDF doc out there ?)

- is it really a hard limitation ? Couldn't this be fixed by a shell variable ?
I had the following script in my `~/bin` when I was using `XY-pic`:

```/bin/sh
#####################################
# Boosted TeX to compile withc XY-pic
export extra_mem_bot=8000000; tex $*
```

Jeroen: will you be so kind to try if this works ?

- I can maybe disable my link fixing code when we are compiling to PDF, but I
think this is really a temporary bugware solution. Considering the time I
already lost on this ticket and the fact that this doesn't solve the problem
but barely hide it under the carpet, I don't think this is an acceptable
solution.

What do you think ?

Florent


---

Comment by hivert created at 2012-02-22 19:17:52

Sorry for the double answer. Please only look at the second one.


---

Comment by jdemeyer created at 2012-02-23 10:38:09

Replying to [comment:53 hivert]:
> First of all, I need to express my feelings: Fucking Sphinx, Fucking
> Latex.
I never understood why [Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth), who has written so much about algorithms, apparently doesn't know about dynamic memory allocation...


---

Comment by jdemeyer created at 2012-02-23 11:23:58

Replying to [comment:54 hivert]:
> export extra_mem_bot=8000000; tex $*
>
> Jeroen: will you be so kind to try if this works ?

This sort of works.  It builds the manual, but here's the strange thing: every run of pdflatex consumes more and more memory.  That is, if I run pdflatex 10 times in a row on `reference.tex` with that extra environment variable, I will certainly hit the error again.


---

Comment by jdemeyer created at 2012-02-23 11:29:53

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-02-23 11:29:53

With extra_mem_top=2000000 (note bot vs. top), it seems to work as it should:

```
Here is how much of TeX's memory you used:
 57776 strings out of 94101
 2165001 string characters out of 3915810
 1541607 words of memory out of 2966904
 33568 multiletter control sequences out of 10000+50000
 99604 words of font info for 164 fonts, out of 1200000 for 2000
 638 hyphenation exceptions out of 8191
 38i,25n,51p,6802b,946s stack positions out of 5000i,500n,6000p,200000b,50000s
```


See #12572.


---

Comment by jdemeyer created at 2012-02-29 10:20:57

The new Sphinx spkg to add extra memory to latex is ready for review at #12572.


---

Comment by jdemeyer created at 2012-02-29 11:30:00

The files

```
doc/common/python.inv
doc/common/update-python-inv.sh
```

should be put in `SAGE_ROOT/devel/sage/MANIFEST.in`


---

Comment by jdemeyer created at 2012-03-01 17:19:01

Changing status from positive_review to needs_work.


---

Comment by hivert created at 2012-03-04 22:19:19

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:60 jdemeyer]:
> The files

```
doc/common/python.inv
doc/common/update-python-inv.sh
```

> should be put in `SAGE_ROOT/devel/sage/MANIFEST.in`

Thanks for pointing this out. I just added a patch [attachment:trac_9128-MANIFEST-fh.patch] which should do that. Please double check as I don't really know what should be there.

Florent


---

Comment by nthiery created at 2012-03-06 12:09:33

This looks good. Back to positive review!


---

Comment by nthiery created at 2012-03-06 12:09:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-13 08:21:27

Resolution: fixed


---

Comment by nthiery created at 2012-03-13 08:34:47

Yippee, a good thing done! 

Thanks Florent for all the energy you put into this ticket :-)
Thanks everyone for the review and support.


---

Comment by jdemeyer created at 2012-04-18 18:59:48

See #12849 for a blocker follow-up: The argspecs of extension function/methods is broken in the Sphinx documentation.


---

Comment by bober created at 2012-05-29 10:02:51

See #13057 for a speed regression followup. It seems that this ticket slowed down introspection quite a bit.


---

Comment by kini created at 2012-05-31 18:51:45

This ticket also introduced a memory leak - 56 MB per docstring lookup. See #13057 and [sage-devel](http://thread.gmane.org/gmane.comp.mathematics.sage.devel/59498).
