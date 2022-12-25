# Issue 9128: Sphinx should be aware of all.py to find its links

archive/issues_009128.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @nthiery @nexttime @novoselt @mwhansen\n\nKeywords: Sphinx links\n\nThough sphinx is perfectly working with target in the local module he isn't\nable to find reference target from other modules even if they are exported in\nall.py. For example, if I want to link Parent from anywhere but parent.pyx, I\nhave to write the full path (ie. `:class:`~sage.structure.parent.Parent``)\neven if it is imported in my module. I find this extremely annoying since, in\nthe task of improving the category doc, I'm setting up a lot of huge cross\nreferences such as:\n\n```\n    :meth:`Algebras.ParentMethods.algebra_generators()\n    <sage.categories.algebras.Algebras.ParentMethods.algebra_generators>`.\n```\nI would be very happy if I had to write only\n\n```\n    :meth:`Algebras.ParentMethods.algebra_generators`\n```\nThe following patch should solve this issue\n\nIssue created by migration from https://trac.sagemath.org/ticket/9128\n\n",
    "created_at": "2010-06-03T12:47:46Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Sphinx should be aware of all.py to find its links",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9128",
    "user": "https://github.com/hivert"
}
```
Assignee: mvngu

CC:  @nthiery @nexttime @novoselt @mwhansen

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

Issue created by migration from https://trac.sagemath.org/ticket/9128





---

archive/issue_comments_084790.json:
```json
{
    "body": "The patch here is a prototype, not yet ready for review. Comments or suggestions are mostly welcome.",
    "created_at": "2010-06-03T12:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84790",
    "user": "https://github.com/hivert"
}
```

The patch here is a prototype, not yet ready for review. Comments or suggestions are mostly welcome.



---

archive/issue_comments_084791.json:
```json
{
    "body": "Changing assignee from mvngu to @hivert.",
    "created_at": "2010-06-03T12:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84791",
    "user": "https://github.com/hivert"
}
```

Changing assignee from mvngu to @hivert.



---

archive/issue_comments_084792.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-03T12:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84792",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084793.json:
```json
{
    "body": "The submitted patch seems to behave as I want. So I put needs review. However if I receive some good advice on sage-devel or sphinx-users I may still change it. Anyway, Please comment.",
    "created_at": "2010-06-03T22:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84793",
    "user": "https://github.com/hivert"
}
```

The submitted patch seems to behave as I want. So I put needs review. However if I receive some good advice on sage-devel or sphinx-users I may still change it. Anyway, Please comment.



---

archive/issue_comments_084794.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-03T22:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84794",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084795.json:
```json
{
    "body": "I have just upgraded an installation of sage-4.4.2 to 4.4.3, applied this patch, set SAGE_DOC_WARN_DANGLING_LINKS to 1, and then got the following error:\n\n```\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -docbuild reference html\nsphinx-build -b html -d /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/doctrees/en/reference    /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/en/reference /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference\nRunning Sphinx v0.6.3\nloading pickled environment... done\nbuilding [html]: targets for 798 source files that are out of date\nupdating environment: [config changed] 802 added, 0 changed, 0 removed\nreading sources... [100%] structure\n/mnt/usb1/scratch/novoselt/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [  0%] coercion\nException occurred:\n  File \"/mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/conf.py\", line 444, in find_sage_dangling_links\n    fromdocname = getattr(sys.modules[modname], basename).__module__\nKeyError: None\nThe full traceback has been saved in /tmp/sphinx-err-Unu279.log, if you want to report the issue to the author.\nPlease also report this if it was a user error, so that a better error message can be provided next time.\nSend reports to sphinx-dev@googlegroups.com. Thanks!\nBuild finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$\n```\nThen I removed this patch, built documentation successfully, pushed this and some other patches and now it seems to work fine. Perhaps it was an unreproducible glitch unrelated to the patch. In general it seems to work as expected and showed me a couple of mistakes in my modules.\n\nI hesitate to switch status to positive review because of the error above and because I don't really understand the code, but I think that this is a great addition and will use this patch from now on!",
    "created_at": "2010-06-07T02:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84795",
    "user": "https://github.com/novoselt"
}
```

I have just upgraded an installation of sage-4.4.2 to 4.4.3, applied this patch, set SAGE_DOC_WARN_DANGLING_LINKS to 1, and then got the following error:

```
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -docbuild reference html
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
Send reports to sphinx-dev@googlegroups.com. Thanks!
Build finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$
```
Then I removed this patch, built documentation successfully, pushed this and some other patches and now it seems to work fine. Perhaps it was an unreproducible glitch unrelated to the patch. In general it seems to work as expected and showed me a couple of mistakes in my modules.

I hesitate to switch status to positive review because of the error above and because I don't really understand the code, but I think that this is a great addition and will use this patch from now on!



---

archive/issue_comments_084796.json:
```json
{
    "body": "I tried the same thing on my own computer - upgraded from 4.4.2 to 4.4.3, applied this patch and tried to build documentation (without setting the environment variable this time). Same error repeatedly, but after popping the patch out everything goes OK. So something has to be done ;-)",
    "created_at": "2010-06-07T02:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84796",
    "user": "https://github.com/novoselt"
}
```

I tried the same thing on my own computer - upgraded from 4.4.2 to 4.4.3, applied this patch and tried to build documentation (without setting the environment variable this time). Same error repeatedly, but after popping the patch out everything goes OK. So something has to be done ;-)



---

archive/issue_comments_084797.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-07T02:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84797",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084798.json:
```json
{
    "body": "Hi Andrey\n\nReplying to [comment:7 novoselt]:\n> I tried the same thing on my own computer - upgraded from 4.4.2 to 4.4.3, applied this patch and tried to build documentation (without setting the environment variable this time). Same error repeatedly, but after popping the patch out everything goes OK. So something has to be done ;-)\n\n\nThanks for looking at that. My patch was working for `.py` and `.pyx`\nfile but not `.rst` file. The new updated file should work. I didn't get\nany comment from `#sphinx-devel` except that `missing-reference` is\nthe good entry point. So except if some expert pop up and suggest some more\nimprovements, I consider this proposal as a good one. Please review.",
    "created_at": "2010-06-07T16:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84798",
    "user": "https://github.com/hivert"
}
```

Hi Andrey

Replying to [comment:7 novoselt]:
> I tried the same thing on my own computer - upgraded from 4.4.2 to 4.4.3, applied this patch and tried to build documentation (without setting the environment variable this time). Same error repeatedly, but after popping the patch out everything goes OK. So something has to be done ;-)


Thanks for looking at that. My patch was working for `.py` and `.pyx`
file but not `.rst` file. The new updated file should work. I didn't get
any comment from `#sphinx-devel` except that `missing-reference` is
the good entry point. So except if some expert pop up and suggest some more
improvements, I consider this proposal as a good one. Please review.



---

archive/issue_comments_084799.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-07T16:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84799",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084800.json:
```json
{
    "body": "Now I upgraded from 4.4.3 to 4.4.4.alpha0. The new patch works better, but not perfect:\n\n```\nWARNING: undefined symbol :meth:`dual` in module sage.categories.dual\nwriting output... [ 13%] sage/categories/examples/algebras_with_basis\nException occurred:\n  File \"/mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/conf.py\", line 453, in find_sage_dangling_links\n    current_module = sys.modules[modname]\nKeyError: u'sage.categories.examples.algebras_with_basis'\nThe full traceback has been saved in /tmp/sphinx-err-rFQQUv.log, if you want to report the issue to the author.\nPlease also report this if it was a user error, so that a better error message can be provided next time.\nSend reports to sphinx-dev@googlegroups.com. Thanks!\nBuild finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference\n```",
    "created_at": "2010-06-07T20:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84800",
    "user": "https://github.com/novoselt"
}
```

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
Send reports to sphinx-dev@googlegroups.com. Thanks!
Build finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference
```



---

archive/issue_comments_084801.json:
```json
{
    "body": "Replying to [comment:9 novoselt]:\n> Now I upgraded from 4.4.3 to 4.4.4.alpha0. The new patch works better, but not perfect:\n\n\nHum ! I know how to workaround those problems but I don't understand why this is happening ! Unfortunately, I don't want to upgrade and I can't reproduce the bug... Can you try to remove the directory `$SAGE_ROOT/devel/sage/doc/output` and relaunch the compilation. Does it still bug ? \n\nFlorent",
    "created_at": "2010-06-07T20:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84801",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:9 novoselt]:
> Now I upgraded from 4.4.3 to 4.4.4.alpha0. The new patch works better, but not perfect:


Hum ! I know how to workaround those problems but I don't understand why this is happening ! Unfortunately, I don't want to upgrade and I can't reproduce the bug... Can you try to remove the directory `$SAGE_ROOT/devel/sage/doc/output` and relaunch the compilation. Does it still bug ? 

Florent



---

archive/issue_comments_084802.json:
```json
{
    "body": "Successful built with 552 warnings!",
    "created_at": "2010-06-07T22:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84802",
    "user": "https://github.com/novoselt"
}
```

Successful built with 552 warnings!



---

archive/issue_comments_084803.json:
```json
{
    "body": "While working on my patches, I am getting the following from this one:\n\n```\nWARNING: undefined symbol :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice` in module sage.geometry.cone \n```\nI don't understand what is wrong. There are no typos and this module does exist in my installation. Is it because I don't import this class/module? Or because it is an underscore method and so there is no record of it in the documentation? (In this case, I actually make a reference to the source code of this method, so I just want the name to be typeset in the same way as other methods, I don't care that the link will not work.)",
    "created_at": "2010-06-08T15:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84803",
    "user": "https://github.com/novoselt"
}
```

While working on my patches, I am getting the following from this one:

```
WARNING: undefined symbol :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice` in module sage.geometry.cone 
```
I don't understand what is wrong. There are no typos and this module does exist in my installation. Is it because I don't import this class/module? Or because it is an underscore method and so there is no record of it in the documentation? (In this case, I actually make a reference to the source code of this method, so I just want the name to be typeset in the same way as other methods, I don't care that the link will not work.)



---

archive/issue_comments_084804.json:
```json
{
    "body": "Replying to [comment:12 novoselt]:\n> While working on my patches, I am getting the following from this one:\n> \n> ```\n> WARNING: undefined symbol :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice` in module sage.geometry.cone \n> ```\n> I don't understand what is wrong. There are no typos and this module does exist in my installation. Is it because I don't import this class/module? Or because it is an underscore method and so there is no record of it in the documentation? (In this case, I actually make a reference to the source code of this method, so I just want the name to be typeset in the same way as other methods, I don't care that the link will not work.)\n\n\nHi Andrey,\n\nThanks for beta testing my patch ! It this module included in the documentation ? More precisely is there a link in some `.rst` file (probably `doc/en/reference/geometry.rst`) ? Because if it is not imported nor linked from the doc, Sphinx as no way to find it but importing the module. This is something I tried to avoid for performance reason... If you are still having some problem, can you please make your patch accessible so that I can debug with it. I don't care if the code is not working...\n\nYou probably already figured that out, but I must confess that I put this patch here for comment but it is clear that it has not sufficiently been shaken. So many thanks for helping me on that and sorry to cause some trouble.",
    "created_at": "2010-06-08T17:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84804",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:12 novoselt]:
> While working on my patches, I am getting the following from this one:
> 
> ```
> WARNING: undefined symbol :meth:`sage.geometry.fan.RationalPolyhedralFan._compute_cone_lattice` in module sage.geometry.cone 
> ```
> I don't understand what is wrong. There are no typos and this module does exist in my installation. Is it because I don't import this class/module? Or because it is an underscore method and so there is no record of it in the documentation? (In this case, I actually make a reference to the source code of this method, so I just want the name to be typeset in the same way as other methods, I don't care that the link will not work.)


Hi Andrey,

Thanks for beta testing my patch ! It this module included in the documentation ? More precisely is there a link in some `.rst` file (probably `doc/en/reference/geometry.rst`) ? Because if it is not imported nor linked from the doc, Sphinx as no way to find it but importing the module. This is something I tried to avoid for performance reason... If you are still having some problem, can you please make your patch accessible so that I can debug with it. I don't care if the code is not working...

You probably already figured that out, but I must confess that I put this patch here for comment but it is clear that it has not sufficiently been shaken. So many thanks for helping me on that and sorry to cause some trouble.



---

archive/issue_comments_084805.json:
```json
{
    "body": "Hi Florent!\n\nI have figured out that the problem is with the underscore - if I use a \"common\" method from the same non-imported patch, link is determined just fine.\n\nIt may be a good idea not to give warnings in such cases, but on the other hand it is probably quite rare and there is no need to make logic of this patch more convoluted. (In my case the docstring of one of the functions says \"see the source code of ... for more involved examples\", since those examples cannot be easily written as standalone code and I didn't want to write something \"involved, but artificial.\")\n\nSince I really like this functionality, I will continue using your patch (and its fresh versions if they become available) and report new problems, if there will be any. But for the final review we will need someone else, since I don't know how Sphinx works and cannot comment on the code itself.\n\nThank you!\nAndrey",
    "created_at": "2010-06-08T22:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84805",
    "user": "https://github.com/novoselt"
}
```

Hi Florent!

I have figured out that the problem is with the underscore - if I use a "common" method from the same non-imported patch, link is determined just fine.

It may be a good idea not to give warnings in such cases, but on the other hand it is probably quite rare and there is no need to make logic of this patch more convoluted. (In my case the docstring of one of the functions says "see the source code of ... for more involved examples", since those examples cannot be easily written as standalone code and I didn't want to write something "involved, but artificial.")

Since I really like this functionality, I will continue using your patch (and its fresh versions if they become available) and report new problems, if there will be any. But for the final review we will need someone else, since I don't know how Sphinx works and cannot comment on the code itself.

Thank you!
Andrey



---

archive/issue_comments_084806.json:
```json
{
    "body": "> It may be a good idea not to give warnings in such cases, but on the other hand it is probably quite rare and there is no need to make logic of this patch more convoluted. (In my case the docstring of one of the functions says \"see the source code of ... for more involved examples\", since those examples cannot be easily written as standalone code and I didn't want to write something \"involved, but artificial.\")\n\n\nCan you describe more precisely what's happening ? Maybe with a very small example... I'm not sure to understand what you are doing... I have the impression that you are requesting me to remove warnings about private methods (i.e.: starting with underscore). \n \n> Since I really like this functionality, I will continue using your patch (and its fresh versions if they become available) and report new problems, if there will be any. But for the final review we will need someone else, since I don't know how Sphinx works and cannot comment on the code itself.\n\n\nI'll try to ping some on sage-devel.",
    "created_at": "2010-06-11T15:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84806",
    "user": "https://github.com/hivert"
}
```

> It may be a good idea not to give warnings in such cases, but on the other hand it is probably quite rare and there is no need to make logic of this patch more convoluted. (In my case the docstring of one of the functions says "see the source code of ... for more involved examples", since those examples cannot be easily written as standalone code and I didn't want to write something "involved, but artificial.")


Can you describe more precisely what's happening ? Maybe with a very small example... I'm not sure to understand what you are doing... I have the impression that you are requesting me to remove warnings about private methods (i.e.: starting with underscore). 
 
> Since I really like this functionality, I will continue using your patch (and its fresh versions if they become available) and report new problems, if there will be any. But for the final review we will need someone else, since I don't know how Sphinx works and cannot comment on the code itself.


I'll try to ping some on sage-devel.



---

archive/issue_comments_084807.json:
```json
{
    "body": "I think that I want to have a distinction between \"totally wrong names\" and names which were successfully found in the Sage library (therefore, it makes sense to reference them), but do not have corresponding entries in the documentation files (therefore, it is not possible to convert them into a working hyperlink). Private/underscore methods are one example (I would like actually to seem them in the documentation \"on demand\", but maybe there are arguments against it), another is reference to objects in modules which are not included into documentation (maybe there will be no such modules eventually). I hope this is more clear, but in any way it is a small point.",
    "created_at": "2010-06-11T15:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84807",
    "user": "https://github.com/novoselt"
}
```

I think that I want to have a distinction between "totally wrong names" and names which were successfully found in the Sage library (therefore, it makes sense to reference them), but do not have corresponding entries in the documentation files (therefore, it is not possible to convert them into a working hyperlink). Private/underscore methods are one example (I would like actually to seem them in the documentation "on demand", but maybe there are arguments against it), another is reference to objects in modules which are not included into documentation (maybe there will be no such modules eventually). I hope this is more clear, but in any way it is a small point.



---

archive/issue_comments_084808.json:
```json
{
    "body": "Replying to [comment:16 novoselt]:\n> I think that I want to have a distinction between \"totally wrong names\" and names which were successfully found in the Sage library (therefore, it makes sense to reference them), but do not have corresponding entries in the documentation files (therefore, it is not possible to convert them into a working hyperlink). Private/underscore methods are one example (I would like actually to seem them in the documentation \"on demand\", but maybe there are arguments against it), another is reference to objects in modules which are not included into documentation (maybe there will be no such modules eventually). I hope this is more clear, but in any way it is a small point.\n\n\nThis should be exactly what I'm doing: I issue two different kinds of warning:\n \n- `undefined symbol :%s:`%s` in %s` \n- `symbol :%s:`%s` linked from %s is defined in %s but not documented`\n\nBu maybe sometime I fail finding a symbol and therefore issue the first warning instead of the second one... Is this happening for you ? \n\nFlorent",
    "created_at": "2010-06-11T15:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84808",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:16 novoselt]:
> I think that I want to have a distinction between "totally wrong names" and names which were successfully found in the Sage library (therefore, it makes sense to reference them), but do not have corresponding entries in the documentation files (therefore, it is not possible to convert them into a working hyperlink). Private/underscore methods are one example (I would like actually to seem them in the documentation "on demand", but maybe there are arguments against it), another is reference to objects in modules which are not included into documentation (maybe there will be no such modules eventually). I hope this is more clear, but in any way it is a small point.


This should be exactly what I'm doing: I issue two different kinds of warning:
 
- `undefined symbol :%s:`%s` in %s` 
- `symbol :%s:`%s` linked from %s is defined in %s but not documented`

Bu maybe sometime I fail finding a symbol and therefore issue the first warning instead of the second one... Is this happening for you ? 

Florent



---

archive/issue_comments_084809.json:
```json
{
    "body": "I get the first kind of warning and now the class is actually imported (although in the end of the module to avoid circular imports).\n\nI have just uploaded a fresh patch to #8987 (so fresh, that it is actually very raw ;-)) if you want to reproduce the issue. Beware that it is a chain of patches, I think it is possible to apply only those listed in #9062, #8986, and #8987 (especially if you are working with 4.4.4.alpha0, where all prerequisites but one are merged).",
    "created_at": "2010-06-11T19:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84809",
    "user": "https://github.com/novoselt"
}
```

I get the first kind of warning and now the class is actually imported (although in the end of the module to avoid circular imports).

I have just uploaded a fresh patch to #8987 (so fresh, that it is actually very raw ;-)) if you want to reproduce the issue. Beware that it is a chain of patches, I think it is possible to apply only those listed in #9062, #8986, and #8987 (especially if you are working with 4.4.4.alpha0, where all prerequisites but one are merged).



---

archive/issue_comments_084810.json:
```json
{
    "body": "I have discovered that\n\n```\n:class:`tuple`\n```\nin the documentation translates now into a black link\n\n```\n__builtin__.tuple\n```\nin the output. I think it would be better to display links exactly as they were written originally and \"expand\" only the actual link, if it is working.",
    "created_at": "2010-06-15T19:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84810",
    "user": "https://github.com/novoselt"
}
```

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

archive/issue_comments_084811.json:
```json
{
    "body": "Replying to [comment:19 novoselt]:\n> I have discovered that\n\n{{{\n:class:`tuple`\n}}}\n> in the documentation translates now into a black link\n\n{{{\n__builtin__.tuple\n}}}\n> in the output. I think it would be better to display links exactly as they were written originally and \"expand\" only the actual link, if it is working.\n\n\nYes ! That was before I know how to resolve those with `intersphinx`. See my new patches",
    "created_at": "2010-06-16T08:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84811",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:19 novoselt]:
> I have discovered that

{{{
:class:`tuple`
}}}
> in the documentation translates now into a black link

{{{
__builtin__.tuple
}}}
> in the output. I think it would be better to display links exactly as they were written originally and "expand" only the actual link, if it is working.


Yes ! That was before I know how to resolve those with `intersphinx`. See my new patches



---

archive/issue_comments_084812.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-16T10:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84812",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084813.json:
```json
{
    "body": "Replying to [comment:20 hivert]:\n> Yes ! That was before I know how to resolve those with `intersphinx`. See my new patches\n\n\nThere is still a problem: currently when linking to python, I raise a warning **before** intersphinx tries to find the link in Python's database.",
    "created_at": "2010-06-16T10:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84813",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:20 hivert]:
> Yes ! That was before I know how to resolve those with `intersphinx`. See my new patches


There is still a problem: currently when linking to python, I raise a warning **before** intersphinx tries to find the link in Python's database.



---

archive/issue_comments_084814.json:
```json
{
    "body": "> There is still a problem: currently when linking to python, I raise a warning **before** intersphinx tries to find the link in Python's database.\n\n\nSome update: It is not possible to achieve what I want in Sphinx 0.6 without hacking into sphinx. However Sphinx 1.0 should be out very soon (they released 1.0beta2 last week). At raising warning is builtin in sphinx 1.0 with the correct configuration option. So I'll probably wait until sphinx 1.0 is out to finish this one, unless someone insist to have it very soon.",
    "created_at": "2010-06-17T20:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84814",
    "user": "https://github.com/hivert"
}
```

> There is still a problem: currently when linking to python, I raise a warning **before** intersphinx tries to find the link in Python's database.


Some update: It is not possible to achieve what I want in Sphinx 0.6 without hacking into sphinx. However Sphinx 1.0 should be out very soon (they released 1.0beta2 last week). At raising warning is builtin in sphinx 1.0 with the correct configuration option. So I'll probably wait until sphinx 1.0 is out to finish this one, unless someone insist to have it very soon.



---

archive/issue_comments_084815.json:
```json
{
    "body": "My opinion is that upgrading Sphinx is the way to go, it may have other benefits (and hopefully no drawbacks). I really want this functionality but I am quite happy with the availability of these patches here, thank you for writing them, Florent! \n\nAndrey",
    "created_at": "2010-06-17T20:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84815",
    "user": "https://github.com/novoselt"
}
```

My opinion is that upgrading Sphinx is the way to go, it may have other benefits (and hopefully no drawbacks). I really want this functionality but I am quite happy with the availability of these patches here, thank you for writing them, Florent! 

Andrey



---

archive/issue_comments_084816.json:
```json
{
    "body": "For the record, here is another bad side effect of this patch: \n\n```\nsage: PolynomialRing?\n\nType:\t\tfunction\nBase Class:\t<type 'function'>\nString Form:\t<function PolynomialRing at 0x16a2758>\nNamespace:\tInteractive\nFile:\t\t/usr/devel/sage/sage/rings/polynomial/polynomial_ring_constructor.py\nDefinition:\tPolynomialRing(base_ring, arg1=None, arg2=None, sparse=False, order='degrevlex', names=None, name=None, implementation=None)\nDocstring:\n    <no docstring>\n```",
    "created_at": "2010-06-18T11:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84816",
    "user": "https://github.com/hivert"
}
```

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

archive/issue_comments_084817.json:
```json
{
    "body": "Is it possible to display line numbers in warnings about bad links?",
    "created_at": "2010-08-25T00:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84817",
    "user": "https://github.com/novoselt"
}
```

Is it possible to display line numbers in warnings about bad links?



---

archive/issue_comments_084818.json:
```json
{
    "body": "I guess it was expected: these patches do not work anymore in Sage-4.6.1.alpha3 due to Sphinx upgrade. On a fresh installation I got\n\n```\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$ hg qapplied\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$ hg qpush\napplying trac_9128-sphinx_links_all-fh.patch\nnow at: trac_9128-sphinx_links_all-fh.patch\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$ hg qpush\napplying trac_9128-intersphinx_python_database-fh.patch\nnow at: trac_9128-intersphinx_python_database-fh.patch\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -b\n...\nnovoselt@sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -docbuild reference html\nsphinx-build -b html -d /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/doctrees/en/reference    /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/en/reference /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference\nRunning Sphinx v1.0.4\nloading pickled environment... done\nloading intersphinx inventory from /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/python-inv.txt...\nbuilding [html]: targets for 1 source files that are out of date\nupdating environment: [extensions changed] 882 added, 0 changed, 0 removed\nreading sources... [100%] tensor                                                                                                                              \nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [  0%] coercion                                                                                                                             \nException occurred:\n  File \"/mnt/usb1/scratch/novoselt/sage/devel/sage/doc/common/conf.py\", line 446, in find_sage_dangling_links\n    modname = nodeattr['modname']\nKeyError: 'modname'\nThe full traceback has been saved in /tmp/sphinx-err-5Yrzg5.log, if you want to report the issue to the developers.\nPlease also report this if it was a user error, so that a better error message can be provided next time.\nEither send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,\nor report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!\nBuild finished.  The built documents can be found in /mnt/usb1/scratch/novoselt/sage/devel/sage/doc/output/html/en/reference\n```",
    "created_at": "2010-12-16T16:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84818",
    "user": "https://github.com/novoselt"
}
```

I guess it was expected: these patches do not work anymore in Sage-4.6.1.alpha3 due to Sphinx upgrade. On a fresh installation I got

```
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$ hg qapplied
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$ hg qpush
applying trac_9128-sphinx_links_all-fh.patch
now at: trac_9128-sphinx_links_all-fh.patch
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$ hg qpush
applying trac_9128-intersphinx_python_database-fh.patch
now at: trac_9128-intersphinx_python_database-fh.patch
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -b
...
novoselt@sage:/scratch/novoselt/sage/devel/sage-main$ ../../sage -docbuild reference html
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

archive/issue_comments_084819.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-27T21:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84819",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084820.json:
```json
{
    "body": "I upgraded my patch to the new sphinx. I'm not sure the patch is completely finished but I'd be very interesting to have feedback.",
    "created_at": "2011-04-27T21:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84820",
    "user": "https://github.com/hivert"
}
```

I upgraded my patch to the new sphinx. I'm not sure the patch is completely finished but I'd be very interesting to have feedback.



---

archive/issue_comments_084821.json:
```json
{
    "body": "Hi Florent,\n\nI have enjoyed using your patch in the past and I am going to start using it again but so far it does not apply to sage-4.7.rc0:\n\n```\nnovoselt@tx2-LM:~/sage/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9128/trac_9128-intersphinx_python_database-fh.patch\nadding trac_9128-intersphinx_python_database-fh.patch to series file\nnovoselt@tx2-LM:~/sage/devel/sage-main$ hg qpush\napplying trac_9128-intersphinx_python_database-fh.patch\nnow at: trac_9128-intersphinx_python_database-fh.patch\nnovoselt@tx2-LM:~/sage/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9128/trac_9128-sphinx_links_all-fh.patch\nadding trac_9128-sphinx_links_all-fh.patch to series file\nnovoselt@tx2-LM:~/sage/devel/sage-main$ hg qpush\napplying trac_9128-sphinx_links_all-fh.patch\npatching file doc/common/conf.py\nHunk #2 FAILED at 19\nHunk #3 succeeded at 97 with fuzz 2 (offset -7 lines).\n1 out of 6 hunks FAILED -- saving rejects to file doc/common/conf.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_9128-sphinx_links_all-fh.patch\nnovoselt@tx2-LM:~/sage/devel/sage-main$ \n```\nThis is on a just built installation without any other patches.",
    "created_at": "2011-04-30T04:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84821",
    "user": "https://github.com/novoselt"
}
```

Hi Florent,

I have enjoyed using your patch in the past and I am going to start using it again but so far it does not apply to sage-4.7.rc0:

```
novoselt@tx2-LM:~/sage/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9128/trac_9128-intersphinx_python_database-fh.patch
adding trac_9128-intersphinx_python_database-fh.patch to series file
novoselt@tx2-LM:~/sage/devel/sage-main$ hg qpush
applying trac_9128-intersphinx_python_database-fh.patch
now at: trac_9128-intersphinx_python_database-fh.patch
novoselt@tx2-LM:~/sage/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9128/trac_9128-sphinx_links_all-fh.patch
adding trac_9128-sphinx_links_all-fh.patch to series file
novoselt@tx2-LM:~/sage/devel/sage-main$ hg qpush
applying trac_9128-sphinx_links_all-fh.patch
patching file doc/common/conf.py
Hunk #2 FAILED at 19
Hunk #3 succeeded at 97 with fuzz 2 (offset -7 lines).
1 out of 6 hunks FAILED -- saving rejects to file doc/common/conf.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_9128-sphinx_links_all-fh.patch
novoselt@tx2-LM:~/sage/devel/sage-main$ 
```
This is on a just built installation without any other patches.



---

archive/issue_comments_084822.json:
```json
{
    "body": "Hi Andrey,\n\nReplying to [comment:30 novoselt]:\n> I have enjoyed using your patch in the past and I am going to start using it again but so far it does not apply to sage-4.7.rc0:\n\n\nOops !!! I should have said that this depend on #11251. Thanks for pointing it out and for testing my patch.",
    "created_at": "2011-04-30T13:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84822",
    "user": "https://github.com/hivert"
}
```

Hi Andrey,

Replying to [comment:30 novoselt]:
> I have enjoyed using your patch in the past and I am going to start using it again but so far it does not apply to sage-4.7.rc0:


Oops !!! I should have said that this depend on #11251. Thanks for pointing it out and for testing my patch.



---

archive/issue_comments_084823.json:
```json
{
    "body": "I updated a little my patch to make sure that the reference guide is compiled first. This is needed so that other documentation can link to the reference guide. Please review.",
    "created_at": "2011-05-02T13:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84823",
    "user": "https://github.com/hivert"
}
```

I updated a little my patch to make sure that the reference guide is compiled first. This is needed so that other documentation can link to the reference guide. Please review.



---

archive/issue_comments_084824.json:
```json
{
    "body": "Hi Mike, \n\nI just added you in CC remembering that you are the Sphinx expert. If you can be kind enough to give me some feedback on that one, I'd very appreciate. It was a very though one for me as sphinx doesn't expose the necessary interface. So I had to dig in the internal. I think it is very useful and it could greatly help improving the documentation. \n\nThanks for your help.",
    "created_at": "2011-06-13T20:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84824",
    "user": "https://github.com/hivert"
}
```

Hi Mike, 

I just added you in CC remembering that you are the Sphinx expert. If you can be kind enough to give me some feedback on that one, I'd very appreciate. It was a very though one for me as sphinx doesn't expose the necessary interface. So I had to dig in the internal. I think it is very useful and it could greatly help improving the documentation. 

Thanks for your help.



---

archive/issue_comments_084825.json:
```json
{
    "body": "By the way, note that #6495 also touches some of the same files, and for builder.py, in a conflicting way.  I think that #6495 could be rebased on top of this one.",
    "created_at": "2011-09-24T18:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84825",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, note that #6495 also touches some of the same files, and for builder.py, in a conflicting way.  I think that #6495 could be rebased on top of this one.



---

archive/issue_comments_084826.json:
```json
{
    "body": "Replying to [comment:35 jhpalmieri]:\n> By the way, note that #6495 also touches some of the same files, and for builder.py, in a conflicting way.  I think that #6495 could be rebased on top of this one.\n\n\n(Although I'm not sure, since #6495 completely changes how the reference manual is built.  Can you take a look at that one to see what you think and whether the two approaches can be combined?)",
    "created_at": "2011-09-24T18:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84826",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:35 jhpalmieri]:
> By the way, note that #6495 also touches some of the same files, and for builder.py, in a conflicting way.  I think that #6495 could be rebased on top of this one.


(Although I'm not sure, since #6495 completely changes how the reference manual is built.  Can you take a look at that one to see what you think and whether the two approaches can be combined?)



---

archive/issue_comments_084827.json:
```json
{
    "body": "Patches do not apply anymore on top of Sage-5.0.beta4. (Perhaps because of recent :trac: addition in another ticket?) What are actually the plans for this ticket?..",
    "created_at": "2012-02-15T22:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84827",
    "user": "https://github.com/novoselt"
}
```

Patches do not apply anymore on top of Sage-5.0.beta4. (Perhaps because of recent :trac: addition in another ticket?) What are actually the plans for this ticket?..



---

archive/issue_comments_084828.json:
```json
{
    "body": "Replying to [comment:37 novoselt]:\n> Patches do not apply anymore on top of Sage-5.0.beta4. (Perhaps because of recent :trac: addition in another ticket?) What are actually the plans for this ticket?..\n\n\nYes there is a conflict with :trac:. I have a rebased patch in the sage-combinat queue which should applies. However I didn't test if it still works. I check it tomorrow and repost it. I'll be more that happy to have a review for this one. It has been a huge pain to get to a working solution, so I'll end up very frustrated if it goes to the garbage.\n\nFlorent",
    "created_at": "2012-02-15T22:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84828",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:37 novoselt]:
> Patches do not apply anymore on top of Sage-5.0.beta4. (Perhaps because of recent :trac: addition in another ticket?) What are actually the plans for this ticket?..


Yes there is a conflict with :trac:. I have a rebased patch in the sage-combinat queue which should applies. However I didn't test if it still works. I check it tomorrow and repost it. I'll be more that happy to have a review for this one. It has been a huge pain to get to a working solution, so I'll end up very frustrated if it goes to the garbage.

Florent



---

archive/issue_comments_084829.json:
```json
{
    "body": "Hi there,\n\nI'm uploading two new patches:\n \n- `trac_9128-intersphinx_python_database-fh.patch` updated to Python 2.7\n \n- `trac_9128-sphinx_links_all-fh.patch` rebased for Sage-5.0.alpha4 and in particular on top of #12490 which was previously in this ticket.\n\nAs I already said, I'm not sure if this should enter Sage in the present status but I need a Sphinx expert (if not George Brandl himself) to try to polish and simplify my code. However, I think the feature is quite important in order to improve Sage's doc, so I suggest that if no expert jump up to let the code enter Sage as such and to improve it in a former ticket. I therefore leave it as need-review.",
    "created_at": "2012-02-18T11:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84829",
    "user": "https://github.com/hivert"
}
```

Hi there,

I'm uploading two new patches:
 
- `trac_9128-intersphinx_python_database-fh.patch` updated to Python 2.7
 
- `trac_9128-sphinx_links_all-fh.patch` rebased for Sage-5.0.alpha4 and in particular on top of #12490 which was previously in this ticket.

As I already said, I'm not sure if this should enter Sage in the present status but I need a Sphinx expert (if not George Brandl himself) to try to polish and simplify my code. However, I think the feature is quite important in order to improve Sage's doc, so I suggest that if no expert jump up to let the code enter Sage as such and to improve it in a former ticket. I therefore leave it as need-review.



---

archive/issue_comments_084830.json:
```json
{
    "body": "Attachment [trac_9128-intersphinx_python_database-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-intersphinx_python_database-fh.patch) by @nthiery created at 2012-02-18 14:27:20\n\n+1 on getting it merged in 5.0, that is as soon as possible! As it is, it already helps much improving the Sage documentation, and it can be improved later. Besides, we want to use it for working with the Sage-Combinat patches, but it's a pain to have it in the queue since it forces recompiling all the documentation.\n\nI have been through the patch, and it looks reasonnable, though I am not by far a Sphinx expert. Just a detail: several of the functions do not have doctests. Now I am not sure if it is anyway really possible to doctest them; if not, I guess that's ok as is.\n\nAndrei or John: would you agree to put a positive review?\n\nCheers,\n                           Nicolas",
    "created_at": "2012-02-18T14:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84830",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9128-intersphinx_python_database-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-intersphinx_python_database-fh.patch) by @nthiery created at 2012-02-18 14:27:20

+1 on getting it merged in 5.0, that is as soon as possible! As it is, it already helps much improving the Sage documentation, and it can be improved later. Besides, we want to use it for working with the Sage-Combinat patches, but it's a pain to have it in the queue since it forces recompiling all the documentation.

I have been through the patch, and it looks reasonnable, though I am not by far a Sphinx expert. Just a detail: several of the functions do not have doctests. Now I am not sure if it is anyway really possible to doctest them; if not, I guess that's ok as is.

Andrei or John: would you agree to put a positive review?

Cheers,
                           Nicolas



---

archive/issue_comments_084831.json:
```json
{
    "body": "I never tried to figure out how Sphinx works, so I cannot say much about the code itself. However, I have been following this ticket from the very beginning, having it on the top of my queue whenever it was cleanly applicable. I have never had any issues with it and it helped me to catch some dangling links. I didn't try to use it for short links in documentation, since I didn't want to be dependent on this ticket, but I surely do want to avoid figuring out and typing every full path. This also makes the documentation resistant to refactoring and moving functions around.\n\nSo - as a user I like this patch a lot, give it positive review, and vote for inclusion as is!",
    "created_at": "2012-02-18T15:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84831",
    "user": "https://github.com/novoselt"
}
```

I never tried to figure out how Sphinx works, so I cannot say much about the code itself. However, I have been following this ticket from the very beginning, having it on the top of my queue whenever it was cleanly applicable. I have never had any issues with it and it helped me to catch some dangling links. I didn't try to use it for short links in documentation, since I didn't want to be dependent on this ticket, but I surely do want to avoid figuring out and typing every full path. This also makes the documentation resistant to refactoring and moving functions around.

So - as a user I like this patch a lot, give it positive review, and vote for inclusion as is!



---

archive/issue_comments_084832.json:
```json
{
    "body": "> I have been through the patch, and it looks reasonnable, though I am not by far a Sphinx expert. Just a detail: several of the functions do not have doctests. Now I am not sure if it is anyway really possible to doctest them; if not, I guess that's ok as is.\n\n\nUnfortunately, I've no idea how to doctests those. As you can see from the\ncode, I wrote my patch using log backtrace and `pdb`. At several point,\nI'm using call to sphinx or docutils internal which are not really\ndocumented. So this is some kind of reverse engineering. I tried several time\nto ask for some help on sphinx-user and never got any answer on that. My\ndiagnostic is that Sphinx doesn't expose a sufficiently flexible API to\nachieve what we want.\n\nProbably a good solution would be to have a Sage-days whose subject is Sphinx\nand doc-compiling and invite George Brandl. We could also solve the Sphinx\nparallel build ticket at the same occasion. Unfortunately, I just organized a\nSage-days and I'm invited to two other until summer so I won't organize such a\ndays and if organized, I don't think I'll be able to attend.\n\nBy the way, I'll CC this on Sage-devel.",
    "created_at": "2012-02-18T18:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84832",
    "user": "https://github.com/hivert"
}
```

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

archive/issue_comments_084833.json:
```json
{
    "body": "I just added the following diff which should resolve many more dependance to python itself.\n\n```diff\ndiff --git a/doc/common/conf.py b/doc/common/conf.py\n--- a/doc/common/conf.py\n+++ b/doc/common/conf.py\n@@ -490,6 +490,11 @@ def call_intersphinx(app, env, node, con\n         debug_inf(app, \"---- Intersphinx: %s not Found\"%node['reftarget'])\n     return res\n \n+# lists of basic Python class which are documented as functions\n+base_class_as_func = [\n+    'bool', 'complex', 'dict', 'file', 'float',\n+    'frozenset', 'int', 'list', 'long', 'object',\n+    'set', 'slice', 'str', 'tuple', 'type', 'unicode', 'xrange']\n \n def find_sage_dangling_links(app, env, node, contnode):\n     \"\"\"\n@@ -507,9 +512,9 @@ def find_sage_dangling_links(app, env, n\n \n     debug_inf(app, \"Searching %s from %s\"%(reftarget, doc))\n \n-    # Workaround: in Python's doc 'object' is documented as a function rather\n-    # than a class\n-    if reftarget == 'object' and reftype == 'class':\n+    # Workaround: in Python's doc 'object', 'list', ... are documented as a\n+    # function rather than a class\n+    if reftarget in base_class_as_func and reftype == 'class':\n         node['reftype'] = 'func'\n \n     res = call_intersphinx(app, env, node, contnode)\n```",
    "created_at": "2012-02-18T19:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84833",
    "user": "https://github.com/hivert"
}
```

I just added the following diff which should resolve many more dependance to python itself.

```diff
diff --git a/doc/common/conf.py b/doc/common/conf.py
--- a/doc/common/conf.py
+++ b/doc/common/conf.py
@@ -490,6 +490,11 @@ def call_intersphinx(app, env, node, con
         debug_inf(app, "---- Intersphinx: %s not Found"%node['reftarget'])
     return res
 
+# lists of basic Python class which are documented as functions
+base_class_as_func = [
+    'bool', 'complex', 'dict', 'file', 'float',
+    'frozenset', 'int', 'list', 'long', 'object',
+    'set', 'slice', 'str', 'tuple', 'type', 'unicode', 'xrange']
 
 def find_sage_dangling_links(app, env, node, contnode):
     """
@@ -507,9 +512,9 @@ def find_sage_dangling_links(app, env, n
 
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

archive/issue_comments_084834.json:
```json
{
    "body": "The way we called Sphinx, it wasn't honoring the `SPHINXOPTS` environment variable anymore. As a consequence option `-n` wasn't working anymore. I just uploaded a patch which fixes this. Maybe this should be added to the dev-guide.",
    "created_at": "2012-02-19T00:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84834",
    "user": "https://github.com/hivert"
}
```

The way we called Sphinx, it wasn't honoring the `SPHINXOPTS` environment variable anymore. As a consequence option `-n` wasn't working anymore. I just uploaded a patch which fixes this. Maybe this should be added to the dev-guide.



---

archive/issue_comments_084835.json:
```json
{
    "body": "Ok, unless someone comments before that, I'll set a positive review tomorrow morning.",
    "created_at": "2012-02-19T10:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84835",
    "user": "https://github.com/nthiery"
}
```

Ok, unless someone comments before that, I'll set a positive review tomorrow morning.



---

archive/issue_comments_084836.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-20T14:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84836",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084837.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-20T15:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84837",
    "user": "https://github.com/hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084838.json:
```json
{
    "body": "There is a little problem in the handling of the environment + Usefull sphinx options should be better documented. I need to rework this a little.\n\nFlorent",
    "created_at": "2012-02-20T15:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84838",
    "user": "https://github.com/hivert"
}
```

There is a little problem in the handling of the environment + Usefull sphinx options should be better documented. I need to rework this a little.

Florent



---

archive/issue_comments_084839.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-20T17:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84839",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084840.json:
```json
{
    "body": "Attachment [trac_9128-doc_option-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-doc_option-fh.patch) by @hivert created at 2012-02-20 17:00:37\n\nHi there,\n\nI finalized the doc of this patch. I also took the chance to add a extra option 'warn-links' which make Sphinx complains for dangling links. To ease the review, I uploaded my changes in [attachment:trac_9128-doc_option-fh.patch]. Those changes are folded in [attachment:trac_9128-sphinx_links_all-fh.patch] so that you only need to apply this one and the database patch.",
    "created_at": "2012-02-20T17:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84840",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_9128-doc_option-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-doc_option-fh.patch) by @hivert created at 2012-02-20 17:00:37

Hi there,

I finalized the doc of this patch. I also took the chance to add a extra option 'warn-links' which make Sphinx complains for dangling links. To ease the review, I uploaded my changes in [attachment:trac_9128-doc_option-fh.patch]. Those changes are folded in [attachment:trac_9128-sphinx_links_all-fh.patch] so that you only need to apply this one and the database patch.



---

archive/issue_comments_084841.json:
```json
{
    "body": "Attachment [trac_9128-sphinx_links_all-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-sphinx_links_all-fh.patch) by @nthiery created at 2012-02-20 17:31:06",
    "created_at": "2012-02-20T17:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84841",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9128-sphinx_links_all-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-sphinx_links_all-fh.patch) by @nthiery created at 2012-02-20 17:31:06



---

archive/issue_comments_084842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-20T17:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84842",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084843.json:
```json
{
    "body": "I made two last minor changes to Florent's patch, with his agreement, and reposted it.\nGood to go!",
    "created_at": "2012-02-20T17:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84843",
    "user": "https://github.com/nthiery"
}
```

I made two last minor changes to Florent's patch, with his agreement, and reposted it.
Good to go!



---

archive/issue_comments_084844.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-22T14:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84844",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084845.json:
```json
{
    "body": "Unfortunately, this breaks the pdf reference manual:\n\n```\n! TeX capacity exceeded, sorry [main memory size=1500000].\n<argument> ...\\endcsname \\current@color {0.40,0.40\n                                                  ,0.40}\\set@color\nl.47055 ...1}\\PYG{o}{/}\\PYG{l+m+mf}{0.1}\\PYG{p}{)}\n\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on reference.log.\nmake[1]: *** [reference.pdf] Error 1\nmake[1]: Leaving directory `/mnt/usb1/scratch/jdemeyer/merger/sage-5.0.beta5-9128/devel/sage-main/doc/output/latex/en/reference'\nBuild finished.  The built documents can be found in /mnt/usb1/scratch/jdemeyer/merger/sage-5.0.beta5-9128/devel/sage/doc/output/pdf/en/reference\n```\n\nThis is using\n\n```\n$ latex --version\npdfTeX using libpoppler 3.141592-1.40.3-2.2 (Web2C 7.5.6)\nkpathsea version 3.5.6\nCopyright 2007 Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).\nKpathsea is copyright 2007 Karl Berry and Olaf Weber.\nThere is NO warranty.  Redistribution of this software is\ncovered by the terms of both the pdfTeX using libpoppler copyright and\nthe Lesser GNU General Public License.\nFor more information about these matters, see the file\nnamed COPYING and the pdfTeX using libpoppler source.\nPrimary author of pdfTeX using libpoppler: Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).\nKpathsea written by Karl Berry, Olaf Weber, and others.\n\nCompiled with libpng 1.2.15beta5; using libpng 1.2.15beta5\nCompiled with zlib 1.2.3.3; using zlib 1.2.3.3\nCompiled with libpoppler version 3.00\n\n```\n\nFrom Googling around, this might not even be fixable without recompiling LaTeX or at least changing LaTeX's configuration files.",
    "created_at": "2012-02-22T14:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84845",
    "user": "https://github.com/jdemeyer"
}
```

Unfortunately, this breaks the pdf reference manual:

```
! TeX capacity exceeded, sorry [main memory size=1500000].
<argument> ...\endcsname \current@color {0.40,0.40
                                                  ,0.40}\set@color
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

archive/issue_comments_084846.json:
```json
{
    "body": "Let me clarify that this happened on sage.math, where the memory size is set to 1500000.  On a different system with 3000000 as limit, it compiled.  The end of that pdflatex log file shows:\n\n```\nHere is how much of TeX's memory you used:\n 59038 strings out of 494632\n 2184818 string characters out of 3923881\n 1820512 words of memory out of 3000000\n 34726 multiletter control sequences out of 10000+50000\n 99604 words of font info for 164 fonts, out of 3000000 for 5000\n 298 hyphenation exceptions out of 8191\n 43i,25n,51p,6802b,946s stack positions out of 5000i,500n,10000p,200000b,50000s\n```\n\nI don't really see a solution besides requiring people to change their LaTeX installs, or splitting up the reference manual (would #6495 fix this?)",
    "created_at": "2012-02-22T16:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84846",
    "user": "https://github.com/jdemeyer"
}
```

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

archive/issue_comments_084847.json:
```json
{
    "body": "#6495 might fix this, since it breaks the reference manual up into smaller pieces.  The only question is whether the pieces are small enough...",
    "created_at": "2012-02-22T17:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84847",
    "user": "https://github.com/jhpalmieri"
}
```

#6495 might fix this, since it breaks the reference manual up into smaller pieces.  The only question is whether the pieces are small enough...



---

archive/issue_comments_084848.json:
```json
{
    "body": "Hi,\n\nReplying to [comment:51 jdemeyer]:\n> Let me clarify that this happened on sage.math, where the memory size is set\n> to 1500000.  On a different system with 3000000 as limit, it compiled.  The\n> end of that pdflatex log file shows:\n\n\n**`\\begin{GROUMPH}`**\nFirst of all, I need to express my feelings: Fucking Sphinx, Fucking\nLatex. None of these two software where seriously designed to scale to a\nproject of Sage size. That's a shame.\n\nWhile I'm at it, fucking Sagemath distro. It worked without any problem on my\nlaptop.\n**`\\end{GROUMPH}`**\n\nSorry for this non useful comment.\n\nI'm quite angry and frustrated because what my patch does is only to fix a\nhuge bunch of missing links in Sage doc way before they are sent to the\ndocutil writer for HTML or TeX. My patch is working at the level of docutil\nabstract syntax tree, but I could have fixed those link by editing Sage source\nas well.  This means that **if** the doc of Sage was correct, it **won't** compile\neither ! And now because I tried to fix the doc, I'm asked to fix LaTeX. I\ndon't think it is really fair.\n\n> I don't really see a solution besides requiring people to change their LaTeX\n> installs, or splitting up the reference manual (would #6495 fix this?)\n\n\nThis also means that, whether or not we apply this patch, we **will** hit the\nsame problem again, as the doc of Sage is expected to grow.\n\n---\n\nLet's try to be more constructive. I see several solution:\n\n- add a comment in Sage installation instructions saying that TeX limitation\nshould be enhanced to compile the PDF doc (by the way, are there any people\nreally using the PDF doc out there ?)\n\n- is it really a hard limitation. Couldn't this be fixed by a shell variable ?\nI had the following script in my `~/bin` when I was using `XY-pic`:\n\n```\npopcorn-*binat/doc/common $ cat ~/bin/hugetex\n#!/bin/sh\n#####################################\n# Boosted TeX to compile withc XY-pic\nexport extra_mem_bot=8000000; tex $*\n```\nJeroen: will you be so kind to try if this works ?\n\n- I can maybe disable my link fixing code when we are compiling to PDF, but I\nthink this is really a temporary bugware solution. Considering the time I\nalready lost on this ticket and the fact that this doesn't solve the problem\nbut barely hide it, I don't think this is an acceptable solution.\n\nFlorent",
    "created_at": "2012-02-22T19:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84848",
    "user": "https://github.com/hivert"
}
```

Hi,

Replying to [comment:51 jdemeyer]:
> Let me clarify that this happened on sage.math, where the memory size is set
> to 1500000.  On a different system with 3000000 as limit, it compiled.  The
> end of that pdflatex log file shows:


**`\begin{GROUMPH}`**
First of all, I need to express my feelings: Fucking Sphinx, Fucking
Latex. None of these two software where seriously designed to scale to a
project of Sage size. That's a shame.

While I'm at it, fucking Sagemath distro. It worked without any problem on my
laptop.
**`\end{GROUMPH}`**

Sorry for this non useful comment.

I'm quite angry and frustrated because what my patch does is only to fix a
huge bunch of missing links in Sage doc way before they are sent to the
docutil writer for HTML or TeX. My patch is working at the level of docutil
abstract syntax tree, but I could have fixed those link by editing Sage source
as well.  This means that **if** the doc of Sage was correct, it **won't** compile
either ! And now because I tried to fix the doc, I'm asked to fix LaTeX. I
don't think it is really fair.

> I don't really see a solution besides requiring people to change their LaTeX
> installs, or splitting up the reference manual (would #6495 fix this?)


This also means that, whether or not we apply this patch, we **will** hit the
same problem again, as the doc of Sage is expected to grow.

---

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

archive/issue_comments_084849.json:
```json
{
    "body": "Hi,\n\nReplying to [comment:51 jdemeyer]:\n> Let me clarify that this happened on sage.math, where the memory size is set\n> to 1500000.  On a different system with 3000000 as limit, it compiled.  The\n> end of that pdflatex log file shows:\n\n\n**`\\begin{GROUMPH}`**\n\nFirst of all, I need to express my feelings: Fucking Sphinx, Fucking\nLatex. None of these two software where seriously designed to scale to a\nproject of Sage's size. That's a shame.\n\nWhile I'm at it, fucking Sagemath distro. It worked without any problem on my\nlaptop.\n\n**`\\end{GROUMPH}`**\n\nSorry for this non useful comment.\n\nI'm quite angry and frustrated because what my patch does is only to fix a\nhuge bunch of missing links in Sage doc, way before they are sent to the\ndocutil writer for HTML or TeX. My patch is working at the level of docutil\nabstract syntax tree, but I could have fixed those link by editing Sage source\nas well.  This means that **if** the doc of Sage was correct, it\n**wouldn't** compile either ! And now because I tried to fix the doc, I'm\nasked to fix LaTeX. I don't think it is really fair.\n\n> I don't really see a solution besides requiring people to change their LaTeX\n> installs, or splitting up the reference manual (would #6495 fix this?)\n\n\nThis also means that, whether or not we apply this patch, we **will** hit the\nsame problem again, as the doc of Sage is expected to grow.\n\n---\n\nLet's try to be more constructive. I see several solutions:\n\n- add a comment in Sage installation instructions saying that TeX limitation\nshould be enhanced to compile the PDF doc (by the way, are there any people\nreally using the PDF doc out there ?)\n\n- is it really a hard limitation ? Couldn't this be fixed by a shell variable ?\nI had the following script in my `~/bin` when I was using `XY-pic`:\n\n```/bin/sh\n#####################################\n# Boosted TeX to compile withc XY-pic\nexport extra_mem_bot=8000000; tex $*\n```\nJeroen: will you be so kind to try if this works ?\n\n- I can maybe disable my link fixing code when we are compiling to PDF, but I\nthink this is really a temporary bugware solution. Considering the time I\nalready lost on this ticket and the fact that this doesn't solve the problem\nbut barely hide it under the carpet, I don't think this is an acceptable\nsolution.\n\nWhat do you think ?\n\nFlorent",
    "created_at": "2012-02-22T19:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84849",
    "user": "https://github.com/hivert"
}
```

Hi,

Replying to [comment:51 jdemeyer]:
> Let me clarify that this happened on sage.math, where the memory size is set
> to 1500000.  On a different system with 3000000 as limit, it compiled.  The
> end of that pdflatex log file shows:


**`\begin{GROUMPH}`**

First of all, I need to express my feelings: Fucking Sphinx, Fucking
Latex. None of these two software where seriously designed to scale to a
project of Sage's size. That's a shame.

While I'm at it, fucking Sagemath distro. It worked without any problem on my
laptop.

**`\end{GROUMPH}`**

Sorry for this non useful comment.

I'm quite angry and frustrated because what my patch does is only to fix a
huge bunch of missing links in Sage doc, way before they are sent to the
docutil writer for HTML or TeX. My patch is working at the level of docutil
abstract syntax tree, but I could have fixed those link by editing Sage source
as well.  This means that **if** the doc of Sage was correct, it
**wouldn't** compile either ! And now because I tried to fix the doc, I'm
asked to fix LaTeX. I don't think it is really fair.

> I don't really see a solution besides requiring people to change their LaTeX
> installs, or splitting up the reference manual (would #6495 fix this?)


This also means that, whether or not we apply this patch, we **will** hit the
same problem again, as the doc of Sage is expected to grow.

---

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

archive/issue_comments_084850.json:
```json
{
    "body": "Sorry for the double answer. Please only look at the second one.",
    "created_at": "2012-02-22T19:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84850",
    "user": "https://github.com/hivert"
}
```

Sorry for the double answer. Please only look at the second one.



---

archive/issue_comments_084851.json:
```json
{
    "body": "Replying to [comment:53 hivert]:\n> First of all, I need to express my feelings: Fucking Sphinx, Fucking\n> Latex.\n\nI never understood why [Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth), who has written so much about algorithms, apparently doesn't know about dynamic memory allocation...",
    "created_at": "2012-02-23T10:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84851",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:53 hivert]:
> First of all, I need to express my feelings: Fucking Sphinx, Fucking
> Latex.

I never understood why [Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth), who has written so much about algorithms, apparently doesn't know about dynamic memory allocation...



---

archive/issue_comments_084852.json:
```json
{
    "body": "Replying to [comment:54 hivert]:\n> export extra_mem_bot=8000000; tex $*\n\n>\n> Jeroen: will you be so kind to try if this works ?\n\n\nThis sort of works.  It builds the manual, but here's the strange thing: every run of pdflatex consumes more and more memory.  That is, if I run pdflatex 10 times in a row on `reference.tex` with that extra environment variable, I will certainly hit the error again.",
    "created_at": "2012-02-23T11:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84852",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:54 hivert]:
> export extra_mem_bot=8000000; tex $*

>
> Jeroen: will you be so kind to try if this works ?


This sort of works.  It builds the manual, but here's the strange thing: every run of pdflatex consumes more and more memory.  That is, if I run pdflatex 10 times in a row on `reference.tex` with that extra environment variable, I will certainly hit the error again.



---

archive/issue_comments_084853.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-02-23T11:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84853",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_084854.json:
```json
{
    "body": "With extra_mem_top=2000000 (note bot vs. top), it seems to work as it should:\n\n```\nHere is how much of TeX's memory you used:\n 57776 strings out of 94101\n 2165001 string characters out of 3915810\n 1541607 words of memory out of 2966904\n 33568 multiletter control sequences out of 10000+50000\n 99604 words of font info for 164 fonts, out of 1200000 for 2000\n 638 hyphenation exceptions out of 8191\n 38i,25n,51p,6802b,946s stack positions out of 5000i,500n,6000p,200000b,50000s\n```\n\nSee #12572.",
    "created_at": "2012-02-23T11:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84854",
    "user": "https://github.com/jdemeyer"
}
```

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

archive/issue_comments_084855.json:
```json
{
    "body": "The new Sphinx spkg to add extra memory to latex is ready for review at #12572.",
    "created_at": "2012-02-29T10:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84855",
    "user": "https://github.com/jdemeyer"
}
```

The new Sphinx spkg to add extra memory to latex is ready for review at #12572.



---

archive/issue_comments_084856.json:
```json
{
    "body": "The files\n\n```\ndoc/common/python.inv\ndoc/common/update-python-inv.sh\n```\nshould be put in `SAGE_ROOT/devel/sage/MANIFEST.in`",
    "created_at": "2012-02-29T11:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84856",
    "user": "https://github.com/jdemeyer"
}
```

The files

```
doc/common/python.inv
doc/common/update-python-inv.sh
```
should be put in `SAGE_ROOT/devel/sage/MANIFEST.in`



---

archive/issue_comments_084857.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-01T17:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84857",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084858.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-04T22:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84858",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084859.json:
```json
{
    "body": "Attachment [trac_9128-MANIFEST-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-MANIFEST-fh.patch) by @hivert created at 2012-03-04 22:19:19\n\nReplying to [comment:60 jdemeyer]:\n> The files\n\n{{{\ndoc/common/python.inv\ndoc/common/update-python-inv.sh\n}}}\n> should be put in `SAGE_ROOT/devel/sage/MANIFEST.in`\n\n\nThanks for pointing this out. I just added a patch [attachment:trac_9128-MANIFEST-fh.patch] which should do that. Please double check as I don't really know what should be there.\n\nFlorent",
    "created_at": "2012-03-04T22:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84859",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_9128-MANIFEST-fh.patch](tarball://root/attachments/some-uuid/ticket9128/trac_9128-MANIFEST-fh.patch) by @hivert created at 2012-03-04 22:19:19

Replying to [comment:60 jdemeyer]:
> The files

{{{
doc/common/python.inv
doc/common/update-python-inv.sh
}}}
> should be put in `SAGE_ROOT/devel/sage/MANIFEST.in`


Thanks for pointing this out. I just added a patch [attachment:trac_9128-MANIFEST-fh.patch] which should do that. Please double check as I don't really know what should be there.

Florent



---

archive/issue_comments_084860.json:
```json
{
    "body": "This looks good. Back to positive review!",
    "created_at": "2012-03-06T12:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84860",
    "user": "https://github.com/nthiery"
}
```

This looks good. Back to positive review!



---

archive/issue_comments_084861.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-06T12:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84861",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022422.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-13T08:21:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9128#event-22422"
}
```



---

archive/issue_comments_084862.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-13T08:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84862",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_084863.json:
```json
{
    "body": "Yippee, a good thing done! \n\nThanks Florent for all the energy you put into this ticket :-)\nThanks everyone for the review and support.",
    "created_at": "2012-03-13T08:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84863",
    "user": "https://github.com/nthiery"
}
```

Yippee, a good thing done! 

Thanks Florent for all the energy you put into this ticket :-)
Thanks everyone for the review and support.



---

archive/issue_comments_084864.json:
```json
{
    "body": "See #12849 for a blocker follow-up: The argspecs of extension function/methods is broken in the Sphinx documentation.",
    "created_at": "2012-04-18T18:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84864",
    "user": "https://github.com/jdemeyer"
}
```

See #12849 for a blocker follow-up: The argspecs of extension function/methods is broken in the Sphinx documentation.



---

archive/issue_comments_084865.json:
```json
{
    "body": "See #13057 for a speed regression followup. It seems that this ticket slowed down introspection quite a bit.",
    "created_at": "2012-05-29T10:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84865",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

See #13057 for a speed regression followup. It seems that this ticket slowed down introspection quite a bit.



---

archive/issue_comments_084866.json:
```json
{
    "body": "This ticket also introduced a memory leak - 56 MB per docstring lookup. See #13057 and [sage-devel](http://thread.gmane.org/gmane.comp.mathematics.sage.devel/59498).",
    "created_at": "2012-05-31T18:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9128#issuecomment-84866",
    "user": "https://github.com/kini"
}
```

This ticket also introduced a memory leak - 56 MB per docstring lookup. See #13057 and [sage-devel](http://thread.gmane.org/gmane.comp.mathematics.sage.devel/59498).
