# Issue 8254: sage takes way too long to startup

archive/issues_008254.json:
```json
{
    "body": "Assignee: tbd\n\nSage still takes too long.  20 seconds, 30 seconds, 5 seconds, on various places... and it is all so painful.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8254\n\n",
    "created_at": "2010-02-13T00:27:52Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "sage takes way too long to startup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8254",
    "user": "was"
}
```
Assignee: tbd

Sage still takes too long.  20 seconds, 30 seconds, 5 seconds, on various places... and it is all so painful.

Issue created by migration from https://trac.sagemath.org/ticket/8254





---

archive/issue_comments_073020.json:
```json
{
    "body": "Could you provide some additional data?  Which platforms?  I assume that `sage -startuptime` does not help, or does it?",
    "created_at": "2010-02-14T02:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73020",
    "user": "mpatel"
}
```

Could you provide some additional data?  Which platforms?  I assume that `sage -startuptime` does not help, or does it?



---

archive/issue_comments_073021.json:
```json
{
    "body": "By \"help,\" I mean \"help to identify the problem(s).\"",
    "created_at": "2010-02-14T03:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73021",
    "user": "mpatel"
}
```

By "help," I mean "help to identify the problem(s)."



---

archive/issue_comments_073022.json:
```json
{
    "body": "OS X for one.",
    "created_at": "2010-02-15T19:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73022",
    "user": "robertwb"
}
```

OS X for one.



---

archive/issue_comments_073023.json:
```json
{
    "body": "FWIW, Sage 4.3.3 (with some mods to get it to build on Solaris) takes 8 seconds to start on a Sun Blade 1000, with 2 x 900 MHz CPUs and 2 GB RAM. That machine has 15,000 rpm 2 Gbit/s fibre channel FC-AL disks. \n\nConsidering the age of that machine, I'm not overly concerned over that one. Although this machine is quite old, the disks are quite high spec. I don't know if that gives any clues. File systems are local. \n\nThe doc test \n\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/symmetric_ideal.py\" \n```\n\n\ntakes 459.4 seconds to run on that machine, so this is no quick machine - I had to increase SAGE_TIMEOUT just to get some doctests to pass. \n\nDave",
    "created_at": "2010-02-28T17:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73023",
    "user": "drkirkby"
}
```

FWIW, Sage 4.3.3 (with some mods to get it to build on Solaris) takes 8 seconds to start on a Sun Blade 1000, with 2 x 900 MHz CPUs and 2 GB RAM. That machine has 15,000 rpm 2 Gbit/s fibre channel FC-AL disks. 

Considering the age of that machine, I'm not overly concerned over that one. Although this machine is quite old, the disks are quite high spec. I don't know if that gives any clues. File systems are local. 

The doc test 


```
sage -t  "devel/sage/sage/rings/polynomial/symmetric_ideal.py" 
```


takes 459.4 seconds to run on that machine, so this is no quick machine - I had to increase SAGE_TIMEOUT just to get some doctests to pass. 

Dave



---

archive/issue_comments_073024.json:
```json
{
    "body": "Given the startup time for me, on that SPARC, and the fact I have a quicker SPARC, I'm not overly concerned by this myself. \n\nBut those interested in fixing it might like to look at using 'iostat', 'vmstat' and 'sar' to see what the system is doing. \n\nDave",
    "created_at": "2010-02-28T18:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73024",
    "user": "drkirkby"
}
```

Given the startup time for me, on that SPARC, and the fact I have a quicker SPARC, I'm not overly concerned by this myself. 

But those interested in fixing it might like to look at using 'iostat', 'vmstat' and 'sar' to see what the system is doing. 

Dave



---

archive/issue_comments_073025.json:
```json
{
    "body": "PS, that Blade 1000 of mine is using UFS disks, not ZFS. Using ZFS would take more memory from a machine that already has very little. \n\nI suspect the startup time has more to do with disk & file-system performance than it does with CPU speed. \n\nDave",
    "created_at": "2010-02-28T18:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73025",
    "user": "drkirkby"
}
```

PS, that Blade 1000 of mine is using UFS disks, not ZFS. Using ZFS would take more memory from a machine that already has very little. 

I suspect the startup time has more to do with disk & file-system performance than it does with CPU speed. 

Dave



---

archive/issue_comments_073026.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-02-28T18:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73026",
    "user": "drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_073027.json:
```json
{
    "body": "Remove assignee drkirkby.",
    "created_at": "2010-02-28T18:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73027",
    "user": "drkirkby"
}
```

Remove assignee drkirkby.



---

archive/issue_comments_073028.json:
```json
{
    "body": "Shaves off about 0.3 seconds for me. Depends on #8456",
    "created_at": "2010-03-06T09:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73028",
    "user": "robertwb"
}
```

Shaves off about 0.3 seconds for me. Depends on #8456



---

archive/issue_comments_073029.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-03T04:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73029",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073030.json:
```json
{
    "body": "Attachment [8254-lazy-schemes-import.patch](tarball://root/attachments/some-uuid/ticket8254/8254-lazy-schemes-import.patch) by was created at 2010-11-03 04:38:43\n\nI talked to Robert today and he told me thought he had marked this \"needs review\", but he hadn't.  So I am.",
    "created_at": "2010-11-03T04:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73030",
    "user": "was"
}
```

Attachment [8254-lazy-schemes-import.patch](tarball://root/attachments/some-uuid/ticket8254/8254-lazy-schemes-import.patch) by was created at 2010-11-03 04:38:43

I talked to Robert today and he told me thought he had marked this "needs review", but he hadn't.  So I am.



---

archive/issue_comments_073031.json:
```json
{
    "body": "Yep, this is ready for review (assuming it hasn't bitrotted). Regarding Davve Kirkby's comment, I agree that disk access is probably the main bottleneck, and this addresses that by loading fewer modules.",
    "created_at": "2010-11-03T08:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73031",
    "user": "robertwb"
}
```

Yep, this is ready for review (assuming it hasn't bitrotted). Regarding Davve Kirkby's comment, I agree that disk access is probably the main bottleneck, and this addresses that by loading fewer modules.



---

archive/issue_comments_073032.json:
```json
{
    "body": "The patch applies to 4.6 after rebasing #8456\n\nIn my computer, from a first running (disc access is necessary), Sage passes from 12.059 seconds to 11.290 So, a save less than 10%\n\nIf I further lazy import doing a \nlazy import for every * imports and running sage.misc.lazy_import.save_cache_file() the time drops to 10.259\n\nIf I run Sage with the initialitation files in RAM (disc acces is not necessary) the time with lazy_importing all * drops from 1.123 to 0.907\n\nSo, still, with lazy imports, disc access is too high.\n\n\nwith Robert patch I get the following doctest failures:\nsage-devel -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/generators_for_rings.rst\nsage-devel -t  -long -force_lib devel/sage/sage/structure/coerce_actions.pyx\nsage-devel -t  -long -force_lib devel/sage/sage/modular/cusps.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/hecke/module.py \nsage-devel -t  -long -force_lib devel/sage/sage/modular/hecke/hecke_operator.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/modsym/heilbronn.pyx\nsage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/arithgroup_element.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gammaH.py \nsage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_sl2z.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gamma0.py \nsage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gamma1.py \nsage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_generic.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/modform/space.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/modform/find_generators.py\nsage-devel -t  -long -force_lib devel/sage/sage/modular/modform/cuspidal_submodule.py",
    "created_at": "2010-11-04T13:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73032",
    "user": "lftabera"
}
```

The patch applies to 4.6 after rebasing #8456

In my computer, from a first running (disc access is necessary), Sage passes from 12.059 seconds to 11.290 So, a save less than 10%

If I further lazy import doing a 
lazy import for every * imports and running sage.misc.lazy_import.save_cache_file() the time drops to 10.259

If I run Sage with the initialitation files in RAM (disc acces is not necessary) the time with lazy_importing all * drops from 1.123 to 0.907

So, still, with lazy imports, disc access is too high.


with Robert patch I get the following doctest failures:
sage-devel -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/generators_for_rings.rst
sage-devel -t  -long -force_lib devel/sage/sage/structure/coerce_actions.pyx
sage-devel -t  -long -force_lib devel/sage/sage/modular/cusps.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/hecke/module.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/hecke/hecke_operator.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modsym/heilbronn.pyx
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/arithgroup_element.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gammaH.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_sl2z.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gamma0.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gamma1.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_generic.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modform/space.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modform/find_generators.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modform/cuspidal_submodule.py



---

archive/issue_comments_073033.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-04T18:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73033",
    "user": "robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073034.json:
```json
{
    "body": "The first import * (after every sage -b) needs to import the modules to get the names. However, if there's only a 10% gain, I should take another look and make sure something isn't accidentally still pulling it in. (A lot has changed since I wrote this patch...)",
    "created_at": "2010-11-04T18:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73034",
    "user": "robertwb"
}
```

The first import * (after every sage -b) needs to import the modules to get the names. However, if there's only a 10% gain, I should take another look and make sure something isn't accidentally still pulling it in. (A lot has changed since I wrote this patch...)



---

archive/issue_comments_073035.json:
```json
{
    "body": "I've attached a patch that seems to get some of the worst offenders for wasteful imports in 4.6.  I haven't run doctests yet, though...",
    "created_at": "2010-11-05T03:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73035",
    "user": "jason"
}
```

I've attached a patch that seems to get some of the worst offenders for wasteful imports in 4.6.  I haven't run doctests yet, though...



---

archive/issue_comments_073036.json:
```json
{
    "body": "From a warm file cache, my patch seems to shave off about 1.4% of the startup time (times averaged over 5 runs).  From a cold file cache, my guess is that it would be more than that because the unnecessary imports I take care of touch a lot of files.",
    "created_at": "2010-11-05T03:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73036",
    "user": "jason"
}
```

From a warm file cache, my patch seems to shave off about 1.4% of the startup time (times averaged over 5 runs).  From a cold file cache, my guess is that it would be more than that because the unnecessary imports I take care of touch a lot of files.



---

archive/issue_comments_073037.json:
```json
{
    "body": "Another issue I have found with this patch. With the lazy_imports in all.py, the namespace used in the instances is not the global namespace.\n\n(after several runnings of sage, so it uses the cached database of functions)\n\n\n```\nsage: sloane_sequence\n<sage.misc.lazy_import.LazyImport object at 0x3e4d950>\nsage: sloane_sequence._get_object()\n<function sloane_sequence at 0x51a7230>\nsage: sloane_sequence\n<sage.misc.lazy_import.LazyImport object at 0x3e4d950>\n```\n\n\nIt does not introduce sloane_sequence function in the global namespace but in sloane_sequence._namespace that seems to not be the global one.",
    "created_at": "2010-11-05T08:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73037",
    "user": "lftabera"
}
```

Another issue I have found with this patch. With the lazy_imports in all.py, the namespace used in the instances is not the global namespace.

(after several runnings of sage, so it uses the cached database of functions)


```
sage: sloane_sequence
<sage.misc.lazy_import.LazyImport object at 0x3e4d950>
sage: sloane_sequence._get_object()
<function sloane_sequence at 0x51a7230>
sage: sloane_sequence
<sage.misc.lazy_import.LazyImport object at 0x3e4d950>
```


It does not introduce sloane_sequence function in the global namespace but in sloane_sequence._namespace that seems to not be the global one.



---

archive/issue_comments_073038.json:
```json
{
    "body": "Okay, I guess because of the ticket title, I attached my patch.  But the ticket title is way too general.  I've made the title more descriptive, and moved my much simpler patch to #10220",
    "created_at": "2010-11-05T12:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73038",
    "user": "jason"
}
```

Okay, I guess because of the ticket title, I attached my patch.  But the ticket title is way too general.  I've made the title more descriptive, and moved my much simpler patch to #10220



---

archive/issue_comments_073039.json:
```json
{
    "body": "Concerning the input on the global namespace in sage.all.py one can write\n\n\n```\nimport __builtin__\nG = __builtin__.__dict__\ndel __builtin__\n```\n\n\nand insert everything in the dictionary G.\n\nBut his looks like a very ugly hack.",
    "created_at": "2011-03-03T10:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73039",
    "user": "lftabera"
}
```

Concerning the input on the global namespace in sage.all.py one can write


```
import __builtin__
G = __builtin__.__dict__
del __builtin__
```


and insert everything in the dictionary G.

But his looks like a very ugly hack.



---

archive/issue_comments_073040.json:
```json
{
    "body": "What I wrote above is nonsense. I am adding names to the __builtin__ namespace. Instead it should be _ip.user_ns, the namespace of the IPython session.\n\nIf we only do lazy_imports from sage.all we will not get an usable enviroment that load fasts.\n\nIf we add lazy_imports in other all.py files we will get problems messing with namespaces.\n\nSuppose the following:\n\nin sage.all:[br]\nfrom sage.rings.all import *\n\nin sage.rings.all:[br]\nfrom sage.rings.polynomial.all import *\n\nIf we lazy_import sage.rings.polynomial.all names in sage.rings.all then we have to choose a namespace.\n\nIf the namespace chosen is the top one. When inserting the real object, it will be inserted in the main namespace, so, in the module sage.rings.all we will always have the lazy_import object.\n\nIf the namespace chosen is sage.rings.all then we will always have the lazy_object in the main namespace...\n\nThis is too technical for me to offer a solution at module level. One idea is to add other files called lazy_all.py. these will be modules that import/lazy_import names in the IPython top namespace. They are not intended for the library code, only to have a more fine grain control on what are lazy_importing or not at the start.\n\nComments? It is worth to give it a try?",
    "created_at": "2011-03-03T22:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73040",
    "user": "lftabera"
}
```

What I wrote above is nonsense. I am adding names to the __builtin__ namespace. Instead it should be _ip.user_ns, the namespace of the IPython session.

If we only do lazy_imports from sage.all we will not get an usable enviroment that load fasts.

If we add lazy_imports in other all.py files we will get problems messing with namespaces.

Suppose the following:

in sage.all:[br]
from sage.rings.all import *

in sage.rings.all:[br]
from sage.rings.polynomial.all import *

If we lazy_import sage.rings.polynomial.all names in sage.rings.all then we have to choose a namespace.

If the namespace chosen is the top one. When inserting the real object, it will be inserted in the main namespace, so, in the module sage.rings.all we will always have the lazy_import object.

If the namespace chosen is sage.rings.all then we will always have the lazy_object in the main namespace...

This is too technical for me to offer a solution at module level. One idea is to add other files called lazy_all.py. these will be modules that import/lazy_import names in the IPython top namespace. They are not intended for the library code, only to have a more fine grain control on what are lazy_importing or not at the start.

Comments? It is worth to give it a try?



---

archive/issue_comments_073041.json:
```json
{
    "body": "If we do a lazy_import of x in sage.foo, and then someone does \"from sage.foo import x\" in m, I don't see any way to resolve the original x in m. It may be worth registering a \"top-level\" namespace that substitutions would be made into. \n\nNote, however, that lazy imports are for library code as well.",
    "created_at": "2011-03-04T05:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73041",
    "user": "robertwb"
}
```

If we do a lazy_import of x in sage.foo, and then someone does "from sage.foo import x" in m, I don't see any way to resolve the original x in m. It may be worth registering a "top-level" namespace that substitutions would be made into. 

Note, however, that lazy imports are for library code as well.



---

archive/issue_comments_073042.json:
```json
{
    "body": "I'm making this ticket into a meta-ticket, link from here to various speedups.",
    "created_at": "2011-03-26T09:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73042",
    "user": "robertwb"
}
```

I'm making this ticket into a meta-ticket, link from here to various speedups.



---

archive/issue_comments_073043.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73043",
    "user": "was"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_073044.json:
```json
{
    "body": "See [https://bugs.python.org/issue34690](https://bugs.python.org/issue34690) for a quite different approach to (significantly) speed up start-up time. It avoids file stats to speed up as well, so I suspect it would be a particularly suitable speed-up for sage (where we're stat-ing loads of files). If we can use this somehow, we'd probably need some tuning parameters to choose which parts of the library are cached and which are loaded fresh.",
    "created_at": "2019-09-16T18:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8254#issuecomment-73044",
    "user": "nbruin"
}
```

See [https://bugs.python.org/issue34690](https://bugs.python.org/issue34690) for a quite different approach to (significantly) speed up start-up time. It avoids file stats to speed up as well, so I suspect it would be a particularly suitable speed-up for sage (where we're stat-ing loads of files). If we can use this somehow, we'd probably need some tuning parameters to choose which parts of the library are cached and which are loaded fresh.
