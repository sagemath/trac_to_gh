# Issue 8380: Implement an interface to GAP3

archive/issues_008380.json:
```json
{
    "body": "Assignee: Franco Saliola\n\nCC:  sage-combinat joyner slabbe jmichel@math.jussieu.fr\n\nKeywords: gap3, chevie, specht, gap, sage-combinat\n\nIt would be great to have an interface to GAP3 so that one can use GAP3 packages that have not been ported to GAP4. Of particular interest are the packages (sage-devel occasionally receives questions about integrating these packages):\n\n* CHEVIE: Finite reflection groups and their root systems, braid groups, Iwahori-Hecke algebras, and Kazhdan-Lusztig polynomials. \n* Specht: Specht: Decomposition matrices for the Hecke algebras of type A.\n\nFor a list of other GAP3 packages, check out [http://www.gap-system.org/Gap3/Packages3/packages.html](http://www.gap-system.org/Gap3/Packages3/packages.html).\n\nTo be clear, I am not suggesting distributing GAP3 with Sage. This would be just an to GAP3.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8380\n\n",
    "created_at": "2010-02-26T17:20:39Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "Implement an interface to GAP3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8380",
    "user": "saliola"
}
```
Assignee: Franco Saliola

CC:  sage-combinat joyner slabbe jmichel@math.jussieu.fr

Keywords: gap3, chevie, specht, gap, sage-combinat

It would be great to have an interface to GAP3 so that one can use GAP3 packages that have not been ported to GAP4. Of particular interest are the packages (sage-devel occasionally receives questions about integrating these packages):

* CHEVIE: Finite reflection groups and their root systems, braid groups, Iwahori-Hecke algebras, and Kazhdan-Lusztig polynomials. 
* Specht: Specht: Decomposition matrices for the Hecke algebras of type A.

For a list of other GAP3 packages, check out [http://www.gap-system.org/Gap3/Packages3/packages.html](http://www.gap-system.org/Gap3/Packages3/packages.html).

To be clear, I am not suggesting distributing GAP3 with Sage. This would be just an to GAP3.

Issue created by migration from https://trac.sagemath.org/ticket/8380





---

archive/issue_comments_074933.json:
```json
{
    "body": "Here are two patches. Make sure you apply the correct patch for you version of Sage.\n\nOf course, you need to have GAP3 installed in order to use GAP3, and all doctests are marked optional.\n\nThe interface behaves very much like the GAP4 interface: tab completion works, one can access the GAP3 help documentation, etc.\n\nNotes for the reviewer:\n\n1. To run the GAP3 doctests:\n   {{{\n   sage -testall -only-optional=gap3\n   }}}\n\n2. I refactored the GAP4 interface code; basically, I separated the `Gap` class into two new classes `Gap_generic` and `GapElement_generic`.\n\n3. I've tested that the patches apply cleanly and all doctests pass on the following systems:\n\n   a. sage.math\n   b. Ubuntu 9.10, amd 64",
    "created_at": "2010-02-26T17:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74933",
    "user": "saliola"
}
```

Here are two patches. Make sure you apply the correct patch for you version of Sage.

Of course, you need to have GAP3 installed in order to use GAP3, and all doctests are marked optional.

The interface behaves very much like the GAP4 interface: tab completion works, one can access the GAP3 help documentation, etc.

Notes for the reviewer:

1. To run the GAP3 doctests:
   {{{
   sage -testall -only-optional=gap3
   }}}

2. I refactored the GAP4 interface code; basically, I separated the `Gap` class into two new classes `Gap_generic` and `GapElement_generic`.

3. I've tested that the patches apply cleanly and all doctests pass on the following systems:

   a. sage.math
   b. Ubuntu 9.10, amd 64



---

archive/issue_comments_074934.json:
```json
{
    "body": "IGNORE THIS PATCH",
    "created_at": "2010-02-26T23:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74934",
    "user": "saliola"
}
```

IGNORE THIS PATCH



---

archive/issue_comments_074935.json:
```json
{
    "body": "Attachment\n\nThis updated patch catches GAP3's syntax error messages.\n\nThe interface seems pretty robust now, so its ready for review. Please try it out.",
    "created_at": "2010-03-02T03:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74935",
    "user": "saliola"
}
```

Attachment

This updated patch catches GAP3's syntax error messages.

The interface seems pretty robust now, so its ready for review. Please try it out.



---

archive/issue_comments_074936.json:
```json
{
    "body": "Attachment\n\nPatch for Sage version 4.3.2 only.",
    "created_at": "2010-03-02T03:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74936",
    "user": "saliola"
}
```

Attachment

Patch for Sage version 4.3.2 only.



---

archive/issue_comments_074937.json:
```json
{
    "body": "Attachment\n\nPatch for Sage version 4.3.3 only.",
    "created_at": "2010-03-02T03:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74937",
    "user": "saliola"
}
```

Attachment

Patch for Sage version 4.3.3 only.



---

archive/issue_comments_074938.json:
```json
{
    "body": "Attachment\n\nDocumentation",
    "created_at": "2010-03-02T03:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74938",
    "user": "saliola"
}
```

Attachment

Documentation



---

archive/issue_comments_074939.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T03:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74939",
    "user": "saliola"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074940.json:
```json
{
    "body": "If you're a GAP3 user interested in trying the new interface, then you can follow the instructions below to patch your version of Sage. These instructions are just a summary of the procedure described at: [http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch](http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch). (Alternatively, your can just install all the sage-combinat patches using the command `\"sage -combinat install\"`, which includes the GAP3 interface patch.)\n\n1. First, create a branch of your Sage library (you can later switch between the main branch and the new gap3 branch with the commands `\"sage -b main\"` and `\"sage -b gap3\"`):\n   {{{\nsage -clone gap3\n}}}\n\n2. Next, start Sage and run one of the following commands, depending on the version of Sage you have installed.\n\n* For sage-4.3.2:\n\n```\nsage: hg_sage.apply(\"http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8380/gap3_interface_v4.3.2.patch\")\n```\n\n\n* For sage-4.3.3:\n\n```\nsage: hg_sage.apply(\"http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8380/gap3_interface_v4.3.3.patch\")\n```\n\n\n3. Finally, exist Sage and run the following command.\n\n```\nsage -br\n```\n\n\nYou should be up and running now.\n\nI've also generated the documentation and posted it as a PDF file. You can find it in the \"Attachments\" section.",
    "created_at": "2010-03-02T03:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74940",
    "user": "saliola"
}
```

If you're a GAP3 user interested in trying the new interface, then you can follow the instructions below to patch your version of Sage. These instructions are just a summary of the procedure described at: [http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch](http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch). (Alternatively, your can just install all the sage-combinat patches using the command `"sage -combinat install"`, which includes the GAP3 interface patch.)

1. First, create a branch of your Sage library (you can later switch between the main branch and the new gap3 branch with the commands `"sage -b main"` and `"sage -b gap3"`):
   {{{
sage -clone gap3
}}}

2. Next, start Sage and run one of the following commands, depending on the version of Sage you have installed.

* For sage-4.3.2:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8380/gap3_interface_v4.3.2.patch")
```


* For sage-4.3.3:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8380/gap3_interface_v4.3.3.patch")
```


3. Finally, exist Sage and run the following command.

```
sage -br
```


You should be up and running now.

I've also generated the documentation and posted it as a PDF file. You can find it in the "Attachments" section.



---

archive/issue_comments_074941.json:
```json
{
    "body": "Nicolas Thiery has posted some code on the sage-combinat patch server that uses this interface to construct Coxeter groups using the GAP3 package CHEVIE. Here is a link to his code: [http://combinat.sagemath.org/hgwebdir.cgi/patches/file/e800cdb481fb/trac_8359-coxeter-groups-permutation-nt.patch#l1](http://combinat.sagemath.org/hgwebdir.cgi/patches/file/e800cdb481fb/trac_8359-coxeter-groups-permutation-nt.patch#l1)",
    "created_at": "2010-03-02T03:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74941",
    "user": "saliola"
}
```

Nicolas Thiery has posted some code on the sage-combinat patch server that uses this interface to construct Coxeter groups using the GAP3 package CHEVIE. Here is a link to his code: [http://combinat.sagemath.org/hgwebdir.cgi/patches/file/e800cdb481fb/trac_8359-coxeter-groups-permutation-nt.patch#l1](http://combinat.sagemath.org/hgwebdir.cgi/patches/file/e800cdb481fb/trac_8359-coxeter-groups-permutation-nt.patch#l1)



---

archive/issue_comments_074942.json:
```json
{
    "body": "I tested it on my sage-4.3.3 running mac OS X 10.5.8. I had already the gap3 together with the chevie package. With the patch applied, I obtain All test passed! with the command `sage -t -long`. I also obtain All test passed with the command `sage -testall -only-optional=gap3`. The documentation builds without warning and is very complete.\n\nBefore giving a positive review, I would like one person used with interface code to take a look at the patch.\n\nGood work Franco!",
    "created_at": "2010-03-02T14:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74942",
    "user": "slabbe"
}
```

I tested it on my sage-4.3.3 running mac OS X 10.5.8. I had already the gap3 together with the chevie package. With the patch applied, I obtain All test passed! with the command `sage -t -long`. I also obtain All test passed with the command `sage -testall -only-optional=gap3`. The documentation builds without warning and is very complete.

Before giving a positive review, I would like one person used with interface code to take a look at the patch.

Good work Franco!



---

archive/issue_comments_074943.json:
```json
{
    "body": "Hi!\n\nWith Jean Michel, I just made an experimental spkg for gap3 + chevie + all other gap3 packages not available on gap4: \n\n    http://sage.math.washington.edu/home/nthiery/gap3-jm0.spkg\n\nPlease test and report! Then we will submit this for submission in experimental/optional",
    "created_at": "2010-04-02T14:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74943",
    "user": "nthiery"
}
```

Hi!

With Jean Michel, I just made an experimental spkg for gap3 + chevie + all other gap3 packages not available on gap4: 

    http://sage.math.washington.edu/home/nthiery/gap3-jm0.spkg

Please test and report! Then we will submit this for submission in experimental/optional



---

archive/issue_comments_074944.json:
```json
{
    "body": "Replying to [comment:7 nthiery]:\n\n> Hi! With Jean Michel, I just made an experimental spkg for gap3 + chevie + all other gap3 packages not available on gap4:  Please test and report! Then we will submit this for submission in experimental/optional\n\nUpdated package rebased on gap3-jm1 from http://www.math.jussieu.fr/~jmichel/gap3/ :\n\n  http://sage.math.washington.edu/home/nthiery/gap3-jm1.spkg",
    "created_at": "2010-04-06T21:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74944",
    "user": "nthiery"
}
```

Replying to [comment:7 nthiery]:

> Hi! With Jean Michel, I just made an experimental spkg for gap3 + chevie + all other gap3 packages not available on gap4:  Please test and report! Then we will submit this for submission in experimental/optional

Updated package rebased on gap3-jm1 from http://www.math.jussieu.fr/~jmichel/gap3/ :

  http://sage.math.washington.edu/home/nthiery/gap3-jm1.spkg



---

archive/issue_comments_074945.json:
```json
{
    "body": "[\u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u043d\u0430 \u0440\u0430\u0431\u043e\u0447\u0438\u0439](http://rapidshare.in.ua/)",
    "created_at": "2010-04-27T12:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74945",
    "user": "bascorp"
}
```

[бесплатно картинки на рабочий](http://rapidshare.in.ua/)



---

archive/issue_comments_074946.json:
```json
{
    "body": "Attachment\n\ndoctest output",
    "created_at": "2010-05-04T20:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74946",
    "user": "burcin"
}
```

Attachment

doctest output



---

archive/issue_comments_074947.json:
```json
{
    "body": "I tested attachment:gap3_interface_v4.3.3.patch on Sage-4.4.1 with gap3 installed using [Frank Luebeck's distribution](http://www.math.rwth-aachen.de:8001/~Frank.Luebeck/gap/GAP3/index.html). The patch applies cleanly, but there are many doctest failures. This could be due to the fact that optional packages like chevie are not included in this distribution of GAP3.\n\nHere is my review for the patch:\n* There is no doctest for the change in `sage/interfaces/expect.py`\n* The method `load_package()` in `sage/interfaces/gap.py` doesn't have a doctest. I understand that this is copied as is from the old version, but if there is any package that is included by default in the GAP4 distribution (or one which we include in our package), we should add a test.\n* In `sage/interfaces/gap3.py`\n  * Is the bug in the pexpect interface mentioned around line 42 reported on trac? Can you mention the ticket number in that comment. Is this specific to the GAP interface?\n  * does the GAP3 banner depend on the specific package installed?\n  * There are some doctests that depend on chevie, (`RequirePackage('\"chevie\"')` and `load_package(\"chevie\")`), these should be optional.\n  * The docstring for `GAP3Record.__getattr__` ends with \" :: \" then an empty line. There are many places where there is an empty line at the end of the docstring, or right after.\n\n\nThe optional package for gap3 in comment:9 looks good in general. Maybe the fact that it's binary only can be made more obvious, for example by adding a `bin` to the package name. \n\nBTW, it's not possible to install the version of GAP3 downloaded from the main web site (http://www.gap-system.org/Gap3/Download3/download.html) easily. I suggest moving the link to Frank Luebeck's distribution to the first place, and putting this option last.",
    "created_at": "2010-05-04T21:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74947",
    "user": "burcin"
}
```

I tested attachment:gap3_interface_v4.3.3.patch on Sage-4.4.1 with gap3 installed using [Frank Luebeck's distribution](http://www.math.rwth-aachen.de:8001/~Frank.Luebeck/gap/GAP3/index.html). The patch applies cleanly, but there are many doctest failures. This could be due to the fact that optional packages like chevie are not included in this distribution of GAP3.

Here is my review for the patch:
* There is no doctest for the change in `sage/interfaces/expect.py`
* The method `load_package()` in `sage/interfaces/gap.py` doesn't have a doctest. I understand that this is copied as is from the old version, but if there is any package that is included by default in the GAP4 distribution (or one which we include in our package), we should add a test.
* In `sage/interfaces/gap3.py`
  * Is the bug in the pexpect interface mentioned around line 42 reported on trac? Can you mention the ticket number in that comment. Is this specific to the GAP interface?
  * does the GAP3 banner depend on the specific package installed?
  * There are some doctests that depend on chevie, (`RequirePackage('"chevie"')` and `load_package("chevie")`), these should be optional.
  * The docstring for `GAP3Record.__getattr__` ends with " :: " then an empty line. There are many places where there is an empty line at the end of the docstring, or right after.


The optional package for gap3 in comment:9 looks good in general. Maybe the fact that it's binary only can be made more obvious, for example by adding a `bin` to the package name. 

BTW, it's not possible to install the version of GAP3 downloaded from the main web site (http://www.gap-system.org/Gap3/Download3/download.html) easily. I suggest moving the link to Frank Luebeck's distribution to the first place, and putting this option last.



---

archive/issue_comments_074948.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-04T21:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74948",
    "user": "burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074949.json:
```json
{
    "body": "Replying to [comment:11 burcin]:\n> I tested attachment:gap3_interface_v4.3.3.patch on Sage-4.4.1 with gap3 installed using [Frank Luebeck's distribution](http://www.math.rwth-aachen.de:8001/~Frank.Luebeck/gap/GAP3/index.html). The patch applies cleanly, but there are many doctest failures. This could be due to the fact that optional packages like chevie are not included in this distribution of GAP3.\n\nI downloaded Frank Luebeck's distribution and compiled it, but it is not working well on my machine:\n\n```\ngap>  SymmetricGroup(5);\nGasman: last bag of type +12 and size     16 has overwritten the free bag.\n```\n\nAs a result, I am getting several doctest errors. I wonder if this is the problem you are having: can you at least check that the above command works on your machine? I'll remark that Luebeck's distribution also includes a binary, and all the doctests but one (the banner) pass if I use that binary.",
    "created_at": "2010-05-05T14:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74949",
    "user": "saliola"
}
```

Replying to [comment:11 burcin]:
> I tested attachment:gap3_interface_v4.3.3.patch on Sage-4.4.1 with gap3 installed using [Frank Luebeck's distribution](http://www.math.rwth-aachen.de:8001/~Frank.Luebeck/gap/GAP3/index.html). The patch applies cleanly, but there are many doctest failures. This could be due to the fact that optional packages like chevie are not included in this distribution of GAP3.

I downloaded Frank Luebeck's distribution and compiled it, but it is not working well on my machine:

```
gap>  SymmetricGroup(5);
Gasman: last bag of type +12 and size     16 has overwritten the free bag.
```

As a result, I am getting several doctest errors. I wonder if this is the problem you are having: can you at least check that the above command works on your machine? I'll remark that Luebeck's distribution also includes a binary, and all the doctests but one (the banner) pass if I use that binary.



---

archive/issue_comments_074950.json:
```json
{
    "body": "Replying to [comment:12 saliola]:\n> I downloaded Frank Luebeck's distribution and compiled it, but it is not working well on my machine:\n {{{\n gap>  SymmetricGroup(5);\n Gasman: last bag of type +12 and size     16 has overwritten the free bag.\n }}}\n\nYou're right, I get the same error. Sorry for the noise.\n\nUsing the binary, I get only one doctest failure:\n\n\n```\n**********************************************************************\nFile \"/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/interfaces/gap3.py\", line 169:\n    sage: gap3.RequirePackage('\"chevie\"')              #optional - gap3\nExpected:\n    Welcome  to  the  CHEVIE  package, ...\nGot:\n    WELCOME  to  the  CHEVIE  package,  Version 3  (Dec  1996)\n    <BLANKLINE>\n          Meinolf Geck,  Frank Luebeck,   Gerhard Hiss, \n          Gunter Malle,  Jean Michel, and Goetz Pfeiffer,\n              Lehrstuhl D fuer Mathematik, RWTH Aachen,\n              IWR der Universitaet Heidelberg,\n              University of St. Andrews and\n              Universite Paris VII\n    <BLANKLINE>\n       This replaces the former weyl package. For first help type\n    <BLANKLINE>\n              ?CHEVIE Version 3 -- a short introduction\n**********************************************************************\n```\n",
    "created_at": "2010-05-05T15:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74950",
    "user": "burcin"
}
```

Replying to [comment:12 saliola]:
> I downloaded Frank Luebeck's distribution and compiled it, but it is not working well on my machine:
 {{{
 gap>  SymmetricGroup(5);
 Gasman: last bag of type +12 and size     16 has overwritten the free bag.
 }}}

You're right, I get the same error. Sorry for the noise.

Using the binary, I get only one doctest failure:


```
**********************************************************************
File "/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/interfaces/gap3.py", line 169:
    sage: gap3.RequirePackage('"chevie"')              #optional - gap3
Expected:
    Welcome  to  the  CHEVIE  package, ...
Got:
    WELCOME  to  the  CHEVIE  package,  Version 3  (Dec  1996)
    <BLANKLINE>
          Meinolf Geck,  Frank Luebeck,   Gerhard Hiss, 
          Gunter Malle,  Jean Michel, and Goetz Pfeiffer,
              Lehrstuhl D fuer Mathematik, RWTH Aachen,
              IWR der Universitaet Heidelberg,
              University of St. Andrews and
              Universite Paris VII
    <BLANKLINE>
       This replaces the former weyl package. For first help type
    <BLANKLINE>
              ?CHEVIE Version 3 -- a short introduction
**********************************************************************
```




---

archive/issue_comments_074951.json:
```json
{
    "body": "I managed to make an spkg that compiles on 64bits machines. See ticket #8906",
    "created_at": "2010-05-06T14:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74951",
    "user": "mrobado"
}
```

I managed to make an spkg that compiles on 64bits machines. See ticket #8906



---

archive/issue_comments_074952.json:
```json
{
    "body": "first apply gap3_interface_v4.3.3.patch, then this",
    "created_at": "2010-05-12T03:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74952",
    "user": "saliola"
}
```

first apply gap3_interface_v4.3.3.patch, then this



---

archive/issue_comments_074953.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-12T03:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74953",
    "user": "saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074954.json:
```json
{
    "body": "Attachment\n\nI've uploaded my changes in a separate patch to ease the review. Apply the patches in this order:\n\n* attachment:gap3_interface_v4.3.3.patch\n* attachment:gap3_interface_patch2.patch\n\n\nReplying to [comment:11 burcin]:\n\n> Here is my review for the patch:\n>  * There is no doctest for the change in `sage/interfaces/expect.py`\n\nThe problem here was that a variable name could be overwritten; before the\npatch:\n\n```\nsage: x = gap(3)\nsage: gap.clear(x.name())\nsage: gap.clear(x.name())\nsage: x = gap(3); x\n3\nsage: y = gap(4); y\n4\nsage: x # this should be 3!\n4\n```\n\nThis is now corrected, and I added the above as a doctest.\n\n>  * The method `load_package()` in `sage/interfaces/gap.py` doesn't have a doctest. I understand that this is copied as is from the old version, but if there is any package that is included by default in the GAP4 distribution (or one which we include in our package), we should add a test.\n\nNeither Sage nor Gap seem to distribute any packages (see the\n`$SAGE_ROOT/local/lib/gap-4.4.12/pkg` directory). I did, however,\nadd a test that at least tests that it raises an appropriate exception.\n\n>  * In `sage/interfaces/gap3.py`\n>   * Is the bug in the pexpect interface mentioned around line 42 reported on trac? Can you mention the ticket number in that comment. Is this specific to the GAP interface?\n\nYes, it is #8471. I added the ticket number to the comment, and\ncross-referenced that ticket to this one.\n\nIt is not specific to the GAP interface. It is an issue with any\n`Expect` instance. See #8471 for details.\n\n>   * does the GAP3 banner depend on the specific package installed?\n\nIt shouldn't since the software is so old. Note that when the banners are\nprinted in the documentation, it is only for illustration purposes. Those\ncommands are not tested because each spawns a console (which would require\nuser input to quit).\n\n>   * There are some doctests that depend on chevie, (`RequirePackage('\"chevie\"')` and `load_package(\"chevie\")`), these should be optional.\n\nI've marked them as `#optional - gap3chevie` instead of just\n`#optional - gap3`.\n\n>   * The docstring for `GAP3Record.__getattr__` ends with \" :: \" then an empty line. There are many places where there is an empty line at the end of the docstring, or right after.\n\nCorrected.\n\n> The optional package for gap3 in comment:9 looks good in general. Maybe the fact that it's binary only can be made more obvious, for example by adding a `bin` to the package name. \n\nThe discussion surrounding spkgs should be moved to #8906, which proposes\na source gap3 spkg instead.\n\n> BTW, it's not possible to install the version of GAP3 downloaded from the main web site (http://www.gap-system.org/Gap3/Download3/download.html) easily. I suggest moving the link to Frank Luebeck's distribution to the first place, and putting this option last.\n\nDone. I listed ticket #8906 as the first option (it should be changed when\nthat ticket is resolved).",
    "created_at": "2010-05-12T03:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74954",
    "user": "saliola"
}
```

Attachment

I've uploaded my changes in a separate patch to ease the review. Apply the patches in this order:

* attachment:gap3_interface_v4.3.3.patch
* attachment:gap3_interface_patch2.patch


Replying to [comment:11 burcin]:

> Here is my review for the patch:
>  * There is no doctest for the change in `sage/interfaces/expect.py`

The problem here was that a variable name could be overwritten; before the
patch:

```
sage: x = gap(3)
sage: gap.clear(x.name())
sage: gap.clear(x.name())
sage: x = gap(3); x
3
sage: y = gap(4); y
4
sage: x # this should be 3!
4
```

This is now corrected, and I added the above as a doctest.

>  * The method `load_package()` in `sage/interfaces/gap.py` doesn't have a doctest. I understand that this is copied as is from the old version, but if there is any package that is included by default in the GAP4 distribution (or one which we include in our package), we should add a test.

Neither Sage nor Gap seem to distribute any packages (see the
`$SAGE_ROOT/local/lib/gap-4.4.12/pkg` directory). I did, however,
add a test that at least tests that it raises an appropriate exception.

>  * In `sage/interfaces/gap3.py`
>   * Is the bug in the pexpect interface mentioned around line 42 reported on trac? Can you mention the ticket number in that comment. Is this specific to the GAP interface?

Yes, it is #8471. I added the ticket number to the comment, and
cross-referenced that ticket to this one.

It is not specific to the GAP interface. It is an issue with any
`Expect` instance. See #8471 for details.

>   * does the GAP3 banner depend on the specific package installed?

It shouldn't since the software is so old. Note that when the banners are
printed in the documentation, it is only for illustration purposes. Those
commands are not tested because each spawns a console (which would require
user input to quit).

>   * There are some doctests that depend on chevie, (`RequirePackage('"chevie"')` and `load_package("chevie")`), these should be optional.

I've marked them as `#optional - gap3chevie` instead of just
`#optional - gap3`.

>   * The docstring for `GAP3Record.__getattr__` ends with " :: " then an empty line. There are many places where there is an empty line at the end of the docstring, or right after.

Corrected.

> The optional package for gap3 in comment:9 looks good in general. Maybe the fact that it's binary only can be made more obvious, for example by adding a `bin` to the package name. 

The discussion surrounding spkgs should be moved to #8906, which proposes
a source gap3 spkg instead.

> BTW, it's not possible to install the version of GAP3 downloaded from the main web site (http://www.gap-system.org/Gap3/Download3/download.html) easily. I suggest moving the link to Frank Luebeck's distribution to the first place, and putting this option last.

Done. I listed ticket #8906 as the first option (it should be changed when
that ticket is resolved).



---

archive/issue_comments_074955.json:
```json
{
    "body": "Replying to [comment:15 saliola]:\n> \n> I've uploaded my changes in a separate patch to ease the review. Apply the patches in this order:\n> \n>  * attachment:gap3_interface_v4.3.3.patch\n>  * attachment:gap3_interface_patch2.patch\n\nIgnore that the patch name says 4.3.3; it should apply cleanly against recent versions of Sage.",
    "created_at": "2010-05-12T03:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74955",
    "user": "saliola"
}
```

Replying to [comment:15 saliola]:
> 
> I've uploaded my changes in a separate patch to ease the review. Apply the patches in this order:
> 
>  * attachment:gap3_interface_v4.3.3.patch
>  * attachment:gap3_interface_patch2.patch

Ignore that the patch name says 4.3.3; it should apply cleanly against recent versions of Sage.



---

archive/issue_comments_074956.json:
```json
{
    "body": "Attachment\n\nFranco's patch2 with a minor change",
    "created_at": "2010-05-22T09:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74956",
    "user": "burcin"
}
```

Attachment

Franco's patch2 with a minor change



---

archive/issue_comments_074957.json:
```json
{
    "body": "It seems the doctest framework doesn't like starting output lines with an ellipsis. The test for ` gap3.RequirePackage('\"chevie\"')` was failing for me saying that it didn't expect any output, so I changed the output to add `W` as the first character. attachment:trac_8380-gap3_interface_patch2.take2.patch is the same as Franco's second patch apart from this minor change.\n\nI'm changing this to positive review.\n\nPatches to be applied:\n* attachment:gap3_interface_v4.3.3.patch\n* attachment:trac_8380-gap3_interface_patch2.take2.patch",
    "created_at": "2010-05-22T09:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74957",
    "user": "burcin"
}
```

It seems the doctest framework doesn't like starting output lines with an ellipsis. The test for ` gap3.RequirePackage('"chevie"')` was failing for me saying that it didn't expect any output, so I changed the output to add `W` as the first character. attachment:trac_8380-gap3_interface_patch2.take2.patch is the same as Franco's second patch apart from this minor change.

I'm changing this to positive review.

Patches to be applied:
* attachment:gap3_interface_v4.3.3.patch
* attachment:trac_8380-gap3_interface_patch2.take2.patch



---

archive/issue_comments_074958.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-22T09:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74958",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074959.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-05T22:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74959",
    "user": "mhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074960.json:
```json
{
    "body": "I get the following failure\n\n\n```\n\nsage -t  \"devel/sage/sage/interfaces/expect.py\"\n**********************************************************************\nFile \"/virtual/scratch/mhansen/release/4.4.4/alpha0/sage-4.4.4.alpha0/devel/sage/sage/interfaces/expect.py\", line 1213:\n    sage: x\nExpected:\n    3\nGot:\n    4\n**********************************************************************\n```\n",
    "created_at": "2010-06-05T22:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74960",
    "user": "mhansen"
}
```

I get the following failure


```

sage -t  "devel/sage/sage/interfaces/expect.py"
**********************************************************************
File "/virtual/scratch/mhansen/release/4.4.4/alpha0/sage-4.4.4.alpha0/devel/sage/sage/interfaces/expect.py", line 1213:
    sage: x
Expected:
    3
Got:
    4
**********************************************************************
```




---

archive/issue_comments_074961.json:
```json
{
    "body": "Replying to [comment:18 mhansen]:\n> I get the following failure\n\nVery bizarre; this passes in a sage session (but it fails while doctesting):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: x = gap(3); x\n3\nsage: gap.clear(x.name())\nsage: gap.clear(x.name())\nsage: x = gap(3); x\n3\nsage: y = gap(4); y\n4\nsage: x\n3\nsage: \n```\n",
    "created_at": "2010-06-07T18:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74961",
    "user": "saliola"
}
```

Replying to [comment:18 mhansen]:
> I get the following failure

Very bizarre; this passes in a sage session (but it fails while doctesting):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: x = gap(3); x
3
sage: gap.clear(x.name())
sage: gap.clear(x.name())
sage: x = gap(3); x
3
sage: y = gap(4); y
4
sage: x
3
sage: 
```




---

archive/issue_comments_074962.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-08T03:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74962",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_074963.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-08T03:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74963",
    "user": "saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074964.json:
```json
{
    "body": "The bit of code in `expect.py` I changed was meant to fix what I thought was a small bug. Unfortunately, it seems this bug runs deeper than I originally thought (I still haven't completely tracked down the problem), so instead I created a new ticket to track this particular issue: #9183. (Fixing this bug is independent of the gap3 interface code.)\n\nI have attached another patch that reverts the changes to `expect.py`.\n\nPatches to be applied:\n\n* attachment:gap3_interface_v4.3.3.patch\n* attachment:trac_8380-gap3_interface_patch2.take2.patch\n* attachment:trac_8380-revert_changes_to_expect.patch",
    "created_at": "2010-06-08T03:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74964",
    "user": "saliola"
}
```

The bit of code in `expect.py` I changed was meant to fix what I thought was a small bug. Unfortunately, it seems this bug runs deeper than I originally thought (I still haven't completely tracked down the problem), so instead I created a new ticket to track this particular issue: #9183. (Fixing this bug is independent of the gap3 interface code.)

I have attached another patch that reverts the changes to `expect.py`.

Patches to be applied:

* attachment:gap3_interface_v4.3.3.patch
* attachment:trac_8380-gap3_interface_patch2.take2.patch
* attachment:trac_8380-revert_changes_to_expect.patch



---

archive/issue_comments_074965.json:
```json
{
    "body": "The first two patches above have already been positively reviewed, so just the last patch above needs to be dealt with.",
    "created_at": "2010-06-08T03:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74965",
    "user": "saliola"
}
```

The first two patches above have already been positively reviewed, so just the last patch above needs to be dealt with.



---

archive/issue_comments_074966.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-08T08:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74966",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074967.json:
```json
{
    "body": "I agree that the expect bug shouldn't hold this patch back. I'm changing this to a positive review.\n\nIt would be great if this can be merged for the next release. AFAIK, the upcoming combinat meeting will have some CHEVIE developers.",
    "created_at": "2010-06-08T08:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74967",
    "user": "burcin"
}
```

I agree that the expect bug shouldn't hold this patch back. I'm changing this to a positive review.

It would be great if this can be merged for the next release. AFAIK, the upcoming combinat meeting will have some CHEVIE developers.



---

archive/issue_comments_074968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8380#issuecomment-74968",
    "user": "mhansen"
}
```

Resolution: fixed
