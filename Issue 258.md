# Issue 258: gp2c -- integrate into SAGE

archive/issues_000258.json:
```json
{
    "body": "Assignee: was\n\nCreate a command in SAGE based on the gp2c program of Bill Alombert.\n\nI envision something like this:\n\n\n```\nsage: gp = Gp()   # new instead of gp interacitve interpreter\nsage: gp.ceval(\"\"\"\na block of code\n\"\"\")\n...\n   at this point the gp2c translator is called and the resulting\n   shared object library is loaded into this instance of gp.\n...\nsage: gp('code that uses new functions defined in the above block of code')\n          resulting code runs faster since it is compiled. \n```\n\n\nThis will give yet another way of writing fast compiled code from interactive/interpreter SAGE. The ways would then be:\n* SageX\n* weave\n* gp2c\n\nThe web page for gp2c:\n\n  http://pari.math.u-bordeaux.fr/download.html#gp2c\n\nIssue created by migration from https://trac.sagemath.org/ticket/258\n\n",
    "created_at": "2007-02-11T20:51:22Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "gp2c -- integrate into SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/258",
    "user": "was"
}
```
Assignee: was

Create a command in SAGE based on the gp2c program of Bill Alombert.

I envision something like this:


```
sage: gp = Gp()   # new instead of gp interacitve interpreter
sage: gp.ceval("""
a block of code
""")
...
   at this point the gp2c translator is called and the resulting
   shared object library is loaded into this instance of gp.
...
sage: gp('code that uses new functions defined in the above block of code')
          resulting code runs faster since it is compiled. 
```


This will give yet another way of writing fast compiled code from interactive/interpreter SAGE. The ways would then be:
* SageX
* weave
* gp2c

The web page for gp2c:

  http://pari.math.u-bordeaux.fr/download.html#gp2c

Issue created by migration from https://trac.sagemath.org/ticket/258





---

archive/issue_comments_001154.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-08T04:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1154",
    "user": "pdenapo"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001155.json:
```json
{
    "body": "Changing assignee from was to pdenapo.",
    "created_at": "2008-01-08T04:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1155",
    "user": "pdenapo"
}
```

Changing assignee from was to pdenapo.



---

archive/issue_comments_001156.json:
```json
{
    "body": "I've succeded in creating a gp2c package (for gp2c-0.0.5pl6), that I'm uploading. In order for the script gp2c-run to work, it is needed a miror modification to the pari package so that the file pari.cfg gets installed.\n\nI will try to do the integration with Sage, next (probably more difficult)\n\nI've upload it to\n\nhttp://pdenapo.googlepages.com/gp2c-0.0.5pl6.spkg\n\nI'm submitting also the correspondig spkg-install file.\n\nHere is my modified pari package:\n\nhttp://pdenapo.googlepages.com/pari-2.3.3.p1.spkg\n\nI'm submitting also: the patch needed for modifying spkg-install\n\nNote: gp2c uses perl for compilation, if found. It would be possible to pass --with-perl=no\nparameter to configure, if we don't want that (and use the precompiled descriptions for pari-2.3)",
    "created_at": "2008-01-08T04:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1156",
    "user": "pdenapo"
}
```

I've succeded in creating a gp2c package (for gp2c-0.0.5pl6), that I'm uploading. In order for the script gp2c-run to work, it is needed a miror modification to the pari package so that the file pari.cfg gets installed.

I will try to do the integration with Sage, next (probably more difficult)

I've upload it to

http://pdenapo.googlepages.com/gp2c-0.0.5pl6.spkg

I'm submitting also the correspondig spkg-install file.

Here is my modified pari package:

http://pdenapo.googlepages.com/pari-2.3.3.p1.spkg

I'm submitting also: the patch needed for modifying spkg-install

Note: gp2c uses perl for compilation, if found. It would be possible to pass --with-perl=no
parameter to configure, if we don't want that (and use the precompiled descriptions for pari-2.3)



---

archive/issue_comments_001157.json:
```json
{
    "body": "A patch showing the required modifications to spkg-install in pari package",
    "created_at": "2008-01-08T04:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1157",
    "user": "pdenapo"
}
```

A patch showing the required modifications to spkg-install in pari package



---

archive/issue_comments_001158.json:
```json
{
    "body": "Attachment\n\nspkg-install file for gp2c",
    "created_at": "2008-01-08T04:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1158",
    "user": "pdenapo"
}
```

Attachment

spkg-install file for gp2c



---

archive/issue_comments_001159.json:
```json
{
    "body": "Attachment\n\nMy second version of the attachment corrects a minor bash syntax-error (the packages worked either way, but fails to report an error message if pari.cfg was not there)",
    "created_at": "2008-01-08T04:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1159",
    "user": "pdenapo"
}
```

Attachment

My second version of the attachment corrects a minor bash syntax-error (the packages worked either way, but fails to report an error message if pari.cfg was not there)



---

archive/issue_comments_001160.json:
```json
{
    "body": "By suggestion from MichaelAbshoff (on irc), I've created a unified package for pari\nang gp2c, you can downloaded at\n\nhttp://pdenapo.googlepages.com/pari-2.3.3.p2.spkg\n\nI agree with him in that his is a better solution since gp2c needs some changes in Pari (installing configuration file), and includes precompiled descriptions for an specific version of pari). \n\nThis new version uses --with-perl=no when compiling gp2c (used precompiled descriptions for pari-2.3)\n\nI also have included a README.Sage file explaning this.",
    "created_at": "2008-01-15T15:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1160",
    "user": "pdenapo"
}
```

By suggestion from MichaelAbshoff (on irc), I've created a unified package for pari
ang gp2c, you can downloaded at

http://pdenapo.googlepages.com/pari-2.3.3.p2.spkg

I agree with him in that his is a better solution since gp2c needs some changes in Pari (installing configuration file), and includes precompiled descriptions for an specific version of pari). 

This new version uses --with-perl=no when compiling gp2c (used precompiled descriptions for pari-2.3)

I also have included a README.Sage file explaning this.



---

archive/issue_comments_001161.json:
```json
{
    "body": "Attachment\n\nspkg-install file for the unified pari/gp2c package",
    "created_at": "2008-01-15T15:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1161",
    "user": "pdenapo"
}
```

Attachment

spkg-install file for the unified pari/gp2c package



---

archive/issue_comments_001162.json:
```json
{
    "body": "Readme file for the unified pari/gp2c package",
    "created_at": "2008-01-15T15:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1162",
    "user": "pdenapo"
}
```

Readme file for the unified pari/gp2c package



---

archive/issue_comments_001163.json:
```json
{
    "body": "Attachment\n\nI submit a patch for the integration of gp2c into sage\n\nThis patch implements two functions for the Gp object:  gp2c_compile_file and gp2c\n\nThe first one compiles a file using gp2c-run and load its into the instance \nof the Gp intepreter asociated to the Gp object.\n(is like the ceval function proposed in the description at the begining, but I think that\ngp2c would be a better name). Also note that you cannot use it to evaluate arbitrary gp\nexpressions, just to define functions (in a syntax valid for gp2c, for example: avoid C identifiers)\n\nYou can use it to do something like:\n\nG=Gp()\nG.gp2c('f(x)=2*x')\nG.eval('f(2)')\n'4'\n\nThe second one takes a string, save it to a temporary file and compiles it using \ngp2c_compile_file\n\nThe temporary files are deleted when the Gp object is destroyed.\n\n(This patch also generalizes the function delete_tmpfiles() from misc/misc.py\nsince I need it to delete the temporary files that gp2c patch creates)",
    "created_at": "2008-01-15T15:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1163",
    "user": "pdenapo"
}
```

Attachment

I submit a patch for the integration of gp2c into sage

This patch implements two functions for the Gp object:  gp2c_compile_file and gp2c

The first one compiles a file using gp2c-run and load its into the instance 
of the Gp intepreter asociated to the Gp object.
(is like the ceval function proposed in the description at the begining, but I think that
gp2c would be a better name). Also note that you cannot use it to evaluate arbitrary gp
expressions, just to define functions (in a syntax valid for gp2c, for example: avoid C identifiers)

You can use it to do something like:

G=Gp()
G.gp2c('f(x)=2*x')
G.eval('f(2)')
'4'

The second one takes a string, save it to a temporary file and compiles it using 
gp2c_compile_file

The temporary files are deleted when the Gp object is destroyed.

(This patch also generalizes the function delete_tmpfiles() from misc/misc.py
since I need it to delete the temporary files that gp2c patch creates)



---

archive/issue_comments_001164.json:
```json
{
    "body": "Attachment\n\npatch: gp2c integration into sage",
    "created_at": "2008-01-15T15:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1164",
    "user": "pdenapo"
}
```

Attachment

patch: gp2c integration into sage



---

archive/issue_comments_001165.json:
```json
{
    "body": "This is a comment *on this ticket* from Bill Allombert, who is the author of gp2c:\n\n```\nOn Tue, Jan 15, 2008 at 08:34:43AM -0800, William Stein wrote:\n> You might have comments about this:\n>\n> http://trac.sagemath.org/sage_trac/ticket/258\n\nOne issue I see is that you can load modules in GP but not unload them.\n\nI do not think it is necessary to merge pari and gp2c. If you install\nPARI properly (with make install), you get all the files needed for\ncompiling GP2C:\n$prefix/lib/pari/pari.cfg\n$prefix/share/pari/pari.desc\nThere is no need to change PARI itself, you just need to add a\ndependency to GP2C.\nSince PARI and GP2C have very different release schedule, merging\nthem will cause you unnecessary trouble.\n\nCheers,\nBill.\n\n```\n",
    "created_at": "2008-01-15T21:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1165",
    "user": "was"
}
```

This is a comment *on this ticket* from Bill Allombert, who is the author of gp2c:

```
On Tue, Jan 15, 2008 at 08:34:43AM -0800, William Stein wrote:
> You might have comments about this:
>
> http://trac.sagemath.org/sage_trac/ticket/258

One issue I see is that you can load modules in GP but not unload them.

I do not think it is necessary to merge pari and gp2c. If you install
PARI properly (with make install), you get all the files needed for
compiling GP2C:
$prefix/lib/pari/pari.cfg
$prefix/share/pari/pari.desc
There is no need to change PARI itself, you just need to add a
dependency to GP2C.
Since PARI and GP2C have very different release schedule, merging
them will cause you unnecessary trouble.

Cheers,
Bill.

```




---

archive/issue_comments_001166.json:
```json
{
    "body": "About merging pari and gp2c: is like you prefer, my first idea was to have two separate\npackages (my integration patch works with whatever aproach you choose)\n\nMichael told me that integrating them could be better, to have less packages.\n(and since if we put gp2c as unstable package, there is no way in which it can trigger a pari \npackage update _which would be needed since it expects the pari.cfg to be installed)\n\nHowever, keeping two separeted packages could make easier to update them when a new \nversion of one of them is released, since as Bill says they have a very different release\nschedule. Perhaps it is better to follow his advice.\n\nAbout unloading modules, I don't know if that would be possible. Loading is implemented using\nthe \"install\" function in gp, is there a function like uninstall in Gp?",
    "created_at": "2008-01-15T22:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1166",
    "user": "pdenapo"
}
```

About merging pari and gp2c: is like you prefer, my first idea was to have two separate
packages (my integration patch works with whatever aproach you choose)

Michael told me that integrating them could be better, to have less packages.
(and since if we put gp2c as unstable package, there is no way in which it can trigger a pari 
package update _which would be needed since it expects the pari.cfg to be installed)

However, keeping two separeted packages could make easier to update them when a new 
version of one of them is released, since as Bill says they have a very different release
schedule. Perhaps it is better to follow his advice.

About unloading modules, I don't know if that would be possible. Loading is implemented using
the "install" function in gp, is there a function like uninstall in Gp?



---

archive/issue_comments_001167.json:
```json
{
    "body": "Okay, after some fundamental discussion at SD7 I would now suggest to have individual packages. \n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T22:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1167",
    "user": "mabshoff"
}
```

Okay, after some fundamental discussion at SD7 I would now suggest to have individual packages. 

Cheers,

Michael



---

archive/issue_comments_001168.json:
```json
{
    "body": "To use this feature, you need to:\n\n- apply the gp2c-instegration patch to sage. \n- install my pari spkg (which installs pari.cfg, needed for gp2c to compile) and then the gp2c spkg",
    "created_at": "2008-05-27T15:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1168",
    "user": "pdenapo"
}
```

To use this feature, you need to:

- apply the gp2c-instegration patch to sage. 
- install my pari spkg (which installs pari.cfg, needed for gp2c to compile) and then the gp2c spkg



---

archive/issue_comments_001169.json:
```json
{
    "body": "This has been sitting around for way too long, so let's sort it out soon. I am making myself editor of this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T12:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1169",
    "user": "mabshoff"
}
```

This has been sitting around for way too long, so let's sort it out soon. I am making myself editor of this ticket.

Cheers,

Michael



---

archive/issue_comments_001170.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-07T12:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1170",
    "user": "mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_001171.json:
```json
{
    "body": "I installed this with no problem, tried the examples and some of my own and it seems to work fine.  I only tried one-liners.\n\nI have a lot of gp experience and also some with gp2c.\n\nI think it would be excellent to have this in Sage.  +1",
    "created_at": "2008-07-21T19:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1171",
    "user": "cremona"
}
```

I installed this with no problem, tried the examples and some of my own and it seems to work fine.  I only tried one-liners.

I have a lot of gp experience and also some with gp2c.

I think it would be excellent to have this in Sage.  +1



---

archive/issue_comments_001172.json:
```json
{
    "body": "Hi,\n\nI have deleted the spkgs as attachment and instead linked them in the ticket description. I consider John's review a positive one, so I am changing the subject here. But we need a formal vote on sage-devel to get gp2c into the core of Sage.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T08:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1172",
    "user": "mabshoff"
}
```

Hi,

I have deleted the spkgs as attachment and instead linked them in the ticket description. I consider John's review a positive one, so I am changing the subject here. But we need a formal vote on sage-devel to get gp2c into the core of Sage.

Cheers,

Michael



---

archive/issue_comments_001173.json:
```json
{
    "body": "I think this is more or less wontfix at this point.",
    "created_at": "2009-06-13T23:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1173",
    "user": "ncalexan"
}
```

I think this is more or less wontfix at this point.



---

archive/issue_comments_001174.json:
```json
{
    "body": "> I think this is more or less wontfix at this point. \n\nThe consensus on the mailing list from both very short votes was that gp2c should be an optional spkg.  However, given that nobody but the author of the patch has every requested gp2c functionality for Sage, even once, as far as I know, I don't think there is sufficient demand to justify the maintenance load.  Note that currently there is really no \"maintenance load\" for optional spkg's, but this *will* change, since I wrote a system for doctesting individual optional spkg's, and I *will* be doctesting sage + official optional spkg's regularly in the near future.  And then every optional spkg will increase the work to do this.\n\nIt seems that the best thing to do would be to close this ticket as \"wontfix\" now, but if some users clamor for gp2c functionality, we reopen it and make it an optional spkg.",
    "created_at": "2009-06-14T07:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1174",
    "user": "was"
}
```

> I think this is more or less wontfix at this point. 

The consensus on the mailing list from both very short votes was that gp2c should be an optional spkg.  However, given that nobody but the author of the patch has every requested gp2c functionality for Sage, even once, as far as I know, I don't think there is sufficient demand to justify the maintenance load.  Note that currently there is really no "maintenance load" for optional spkg's, but this *will* change, since I wrote a system for doctesting individual optional spkg's, and I *will* be doctesting sage + official optional spkg's regularly in the near future.  And then every optional spkg will increase the work to do this.

It seems that the best thing to do would be to close this ticket as "wontfix" now, but if some users clamor for gp2c functionality, we reopen it and make it an optional spkg.



---

archive/issue_comments_001175.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-06-14T07:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1175",
    "user": "was"
}
```

Resolution: wontfix



---

archive/issue_comments_001176.json:
```json
{
    "body": "Replying to [comment:15 was]:\n> > I think this is more or less wontfix at this point. \n> \n> The consensus on the mailing list from both very short votes was that gp2c should be an optional spkg.  However, given that nobody but the author of the patch has every requested gp2c functionality for Sage, even once, as far as I know, I don't think there is sufficient demand to justify the maintenance load.  Note that currently there is really no \"maintenance load\" for optional spkg's, but this *will* change, since I wrote a system for doctesting individual optional spkg's, and I *will* be doctesting sage + official optional spkg's regularly in the near future.  And then every optional spkg will increase the work to do this.\n> \n> It seems that the best thing to do would be to close this ticket as \"wontfix\" now, but if some users clamor for gp2c functionality, we reopen it and make it an optional spkg.  \n\nAs someone who originally voted for this, let me say that I am happy not to proceed with it.  There are very few gp scripts Sage uses now anyway.  The point about gp2c is that with it you can convert gp functions into pari library functions.  But the best way to do that anyway would be for the gp script's author to do it outside of Sage, as the result is a C program which can be compiled and linked with the pari library and then used in Sage.  There's no need for Sage itself to have gp2c.",
    "created_at": "2009-06-14T09:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1176",
    "user": "cremona"
}
```

Replying to [comment:15 was]:
> > I think this is more or less wontfix at this point. 
> 
> The consensus on the mailing list from both very short votes was that gp2c should be an optional spkg.  However, given that nobody but the author of the patch has every requested gp2c functionality for Sage, even once, as far as I know, I don't think there is sufficient demand to justify the maintenance load.  Note that currently there is really no "maintenance load" for optional spkg's, but this *will* change, since I wrote a system for doctesting individual optional spkg's, and I *will* be doctesting sage + official optional spkg's regularly in the near future.  And then every optional spkg will increase the work to do this.
> 
> It seems that the best thing to do would be to close this ticket as "wontfix" now, but if some users clamor for gp2c functionality, we reopen it and make it an optional spkg.  

As someone who originally voted for this, let me say that I am happy not to proceed with it.  There are very few gp scripts Sage uses now anyway.  The point about gp2c is that with it you can convert gp functions into pari library functions.  But the best way to do that anyway would be for the gp script's author to do it outside of Sage, as the result is a C program which can be compiled and linked with the pari library and then used in Sage.  There's no need for Sage itself to have gp2c.



---

archive/issue_comments_001177.json:
```json
{
    "body": "Replying to [comment:17 cremona]:\n> There's no need for Sage itself to have gp2c.\nDo you still stand by that opinion?\n\nOne advantage would be calling GP scripts using the PARI library interface instead of GP.\n\nSee also #15809.",
    "created_at": "2015-07-09T09:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1177",
    "user": "jdemeyer"
}
```

Replying to [comment:17 cremona]:
> There's no need for Sage itself to have gp2c.
Do you still stand by that opinion?

One advantage would be calling GP scripts using the PARI library interface instead of GP.

See also #15809.



---

archive/issue_comments_001178.json:
```json
{
    "body": "Changing component from interfaces to packages: optional.",
    "created_at": "2015-07-09T09:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1178",
    "user": "jdemeyer"
}
```

Changing component from interfaces to packages: optional.



---

archive/issue_comments_001179.json:
```json
{
    "body": "Changing keywords from \"editor_mabshoff\" to \"\".",
    "created_at": "2015-07-09T09:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1179",
    "user": "jdemeyer"
}
```

Changing keywords from "editor_mabshoff" to "".



---

archive/issue_comments_001180.json:
```json
{
    "body": "What I said before is still true for the remaining  gp scripts used in Sage (which will probably reduce further in number soon -- the new lfun stuff in Pari will make ComputeL largely redundant), but as one who currently calls other gp sctiprs from within Sage it would be very good if that could easily be done via gp2c.  I would be happy to test such a set-up.",
    "created_at": "2015-07-09T11:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1180",
    "user": "cremona"
}
```

What I said before is still true for the remaining  gp scripts used in Sage (which will probably reduce further in number soon -- the new lfun stuff in Pari will make ComputeL largely redundant), but as one who currently calls other gp sctiprs from within Sage it would be very good if that could easily be done via gp2c.  I would be happy to test such a set-up.



---

archive/issue_comments_001181.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2015-07-09T12:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1181",
    "user": "jdemeyer"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_001182.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2015-07-09T12:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1182",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_001183.json:
```json
{
    "body": "There is one testsuite failure, I asked upstream PARI about it. But other than that, the package seems to work fine.\n----\nNew commits:",
    "created_at": "2015-07-09T12:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1183",
    "user": "jdemeyer"
}
```

There is one testsuite failure, I asked upstream PARI about it. But other than that, the package seems to work fine.
----
New commits:



---

archive/issue_comments_001184.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-07-09T12:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1184",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001185.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-07-09T12:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1185",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001186.json:
```json
{
    "body": "Bill said I should use the git version of gp2c.",
    "created_at": "2015-07-09T12:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1186",
    "user": "jdemeyer"
}
```

Bill said I should use the git version of gp2c.



---

archive/issue_comments_001187.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-09T12:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1187",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001188.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-07-09T12:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1188",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001189.json:
```json
{
    "body": "Added upstream fixes from gp2c git repo, now passes testsuite.",
    "created_at": "2015-07-09T12:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1189",
    "user": "jdemeyer"
}
```

Added upstream fixes from gp2c git repo, now passes testsuite.



---

archive/issue_comments_001190.json:
```json
{
    "body": "No time to etst this week, I'm in Oberwolfach, but so is Karim (a few metres from where I sit) so if there issues you would like me to raise with him, let me know.",
    "created_at": "2015-07-09T13:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1190",
    "user": "cremona"
}
```

No time to etst this week, I'm in Oberwolfach, but so is Karim (a few metres from where I sit) so if there issues you would like me to raise with him, let me know.



---

archive/issue_comments_001191.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-10T08:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1191",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001192.json:
```json
{
    "body": "I confirm that it passes testsuite on my computer (Debian wheezy amd64).",
    "created_at": "2015-08-15T11:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1192",
    "user": "vdelecroix"
}
```

I confirm that it passes testsuite on my computer (Debian wheezy amd64).



---

archive/issue_comments_001193.json:
```json
{
    "body": "Because there is an obsolete patchbot loop-testing this ticket, I temporarily change its status.",
    "created_at": "2015-08-22T16:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1193",
    "user": "chapoton"
}
```

Because there is an obsolete patchbot loop-testing this ticket, I temporarily change its status.



---

archive/issue_comments_001194.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-08-22T16:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1194",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_001195.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-08-23T20:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1195",
    "user": "jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_001196.json:
```json
{
    "body": "Replying to [comment:32 chapoton]:\n> Because there is an obsolete patchbot loop-testing this ticket\nWhy is that a problem?\n\nThis ticket still needs review, despite what the patchbots think about it.",
    "created_at": "2015-08-23T20:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1196",
    "user": "jdemeyer"
}
```

Replying to [comment:32 chapoton]:
> Because there is an obsolete patchbot loop-testing this ticket
Why is that a problem?

This ticket still needs review, despite what the patchbots think about it.



---

archive/issue_comments_001197.json:
```json
{
    "body": "Yes, yes, but please, could you update \"sage4\" ?",
    "created_at": "2015-08-23T20:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1197",
    "user": "chapoton"
}
```

Yes, yes, but please, could you update "sage4" ?



---

archive/issue_comments_001198.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-10-21T20:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1198",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001199.json:
```json
{
    "body": "Could you give more explanations in `SPKG.txt` about the two patches (`20150326.patch` and `global.patch`).",
    "created_at": "2015-10-21T20:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1199",
    "user": "vdelecroix"
}
```

Could you give more explanations in `SPKG.txt` about the two patches (`20150326.patch` and `global.patch`).



---

archive/issue_comments_001200.json:
```json
{
    "body": "I cannot really give much more explanation, these are patches from upstream to fix some issues which came up while testing this ticket. See the two `gp2c` threads on [http://pari.math.u-bordeaux.fr/archives/pari-dev-1507/threads.html](http://pari.math.u-bordeaux.fr/archives/pari-dev-1507/threads.html)\n\nI can instead try to use the upstream git repo without patches. Let me know if you prefer this.",
    "created_at": "2015-10-22T07:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1200",
    "user": "jdemeyer"
}
```

I cannot really give much more explanation, these are patches from upstream to fix some issues which came up while testing this ticket. See the two `gp2c` threads on [http://pari.math.u-bordeaux.fr/archives/pari-dev-1507/threads.html](http://pari.math.u-bordeaux.fr/archives/pari-dev-1507/threads.html)

I can instead try to use the upstream git repo without patches. Let me know if you prefer this.



---

archive/issue_comments_001201.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-10-22T09:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1201",
    "user": "vdelecroix"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_001202.json:
```json
{
    "body": "Is \"upstream stable + patches\" always better than \"upstream develop\"? Yes.",
    "created_at": "2015-10-22T09:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1202",
    "user": "vdelecroix"
}
```

Is "upstream stable + patches" always better than "upstream develop"? Yes.



---

archive/issue_comments_001203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-10-23T17:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/258#issuecomment-1203",
    "user": "vbraun"
}
```

Resolution: fixed
