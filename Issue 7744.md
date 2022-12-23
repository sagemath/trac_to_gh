# Issue 7744: STL Export -- Allows for 3d printing of surfaces

archive/issues_007744.json:
```json
{
    "body": "Assignee: colah\n\nCC:  niles kcrisman jdemeyer tmonteil\n\nKeywords: 3D-Printing STL\n\n\n```\ndef surface_to_stl(surface):\n    \"\"\"\n    Return an STL representation of the surface.\n    \n    INPUT:\n        - `surface` -- any surface, eg. output of a 3d plot function.\n    \n    OUTPUT:\n        A string that represents the surface in the STL format.\n    \n    COMMENTS:\n        (1) You must view the surface before plotting it.\n            Otherwise, this will not work.\n        (2) In order to do 3d printing with this, you will need to\n            convert it into gcode. Skeinforge is an open-source\n            program that can do this.\n        (3) The size of the surface is not normalized in export.\n            Sage's units will become the units of the STL \n            description. These seem to be ~0.05 cm (at least when \n            printed using skeinforge -> replicatorg -> hacklab.to's \n            cupcake).\n        (4) Be aware of the overhang limits of your 3d printer; \n            most printers can only handle an overhang of Pi/2 (45*) \n            before your model will start drooping.\n    \n    EXAMPLES:\n        sage: x,y,z = var('x,y,z')\n        sage: a = implicit_plot3d(x^2+y^2+z^2-9, [x,-5,5], [y,-5,5],[z,-5,5])\n        sage: a\n        sage: f=file.open(\"foo.stl\",'w')\n        sage: f.write(surface_to_stl(a))\n        sage: f.close()\n    \"\"\"\n \n    out =  \"solid mathsurface\\n\"\n    for i in surface.face_list():\n        n = ( i[1][1]*i[2][2] - i[2][1]*i[1][2],\n              i[1][2]*i[2][0] - i[1][0]*i[2] 2],\n              i[1][0]*i[2][1] - i[2][0]*i[1][1] )\n        abs = (n[0]^2+n[1]^2+n[2]^2)^0.5\n        n= (n[0]/abs,n[1]/abs,n[2]/abs)\n        out += \"  facet normal \" + repr(n[0])  + \" \" + repr(n[1])    + \" \" + repr(n[2])\n        out += \"    outer loop\\n\"\n        out += \"      vertex \" + repr(i[0][0]) + \" \" + repr(i[0][1]) + \" \" + repr(i[0][2]) + \"\\n\"\n        out += \"      vertex \" + repr(i[1][0]) + \" \" + repr(i[1][1]) + \" \" + repr(i[1][2]) + \"\\n\"\n        out += \"      vertex \" + repr(i[2][0]) + \" \" + repr(i[2][1]) + \" \" + repr(i[2][2]) + \"\\n\"\n        out += \"    endloop\\n\"\n        out += \"  endfacet\\n\"\n    out += \"endsolid surface\\n\"\n    return out\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7744\n\n",
    "created_at": "2009-12-20T17:07:34Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "STL Export -- Allows for 3d printing of surfaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7744",
    "user": "colah"
}
```
Assignee: colah

CC:  niles kcrisman jdemeyer tmonteil

Keywords: 3D-Printing STL


```
def surface_to_stl(surface):
    """
    Return an STL representation of the surface.
    
    INPUT:
        - `surface` -- any surface, eg. output of a 3d plot function.
    
    OUTPUT:
        A string that represents the surface in the STL format.
    
    COMMENTS:
        (1) You must view the surface before plotting it.
            Otherwise, this will not work.
        (2) In order to do 3d printing with this, you will need to
            convert it into gcode. Skeinforge is an open-source
            program that can do this.
        (3) The size of the surface is not normalized in export.
            Sage's units will become the units of the STL 
            description. These seem to be ~0.05 cm (at least when 
            printed using skeinforge -> replicatorg -> hacklab.to's 
            cupcake).
        (4) Be aware of the overhang limits of your 3d printer; 
            most printers can only handle an overhang of Pi/2 (45*) 
            before your model will start drooping.
    
    EXAMPLES:
        sage: x,y,z = var('x,y,z')
        sage: a = implicit_plot3d(x^2+y^2+z^2-9, [x,-5,5], [y,-5,5],[z,-5,5])
        sage: a
        sage: f=file.open("foo.stl",'w')
        sage: f.write(surface_to_stl(a))
        sage: f.close()
    """
 
    out =  "solid mathsurface\n"
    for i in surface.face_list():
        n = ( i[1][1]*i[2][2] - i[2][1]*i[1][2],
              i[1][2]*i[2][0] - i[1][0]*i[2] 2],
              i[1][0]*i[2][1] - i[2][0]*i[1][1] )
        abs = (n[0]^2+n[1]^2+n[2]^2)^0.5
        n= (n[0]/abs,n[1]/abs,n[2]/abs)
        out += "  facet normal " + repr(n[0])  + " " + repr(n[1])    + " " + repr(n[2])
        out += "    outer loop\n"
        out += "      vertex " + repr(i[0][0]) + " " + repr(i[0][1]) + " " + repr(i[0][2]) + "\n"
        out += "      vertex " + repr(i[1][0]) + " " + repr(i[1][1]) + " " + repr(i[1][2]) + "\n"
        out += "      vertex " + repr(i[2][0]) + " " + repr(i[2][1]) + " " + repr(i[2][2]) + "\n"
        out += "    endloop\n"
        out += "  endfacet\n"
    out += "endsolid surface\n"
    return out
```



Issue created by migration from https://trac.sagemath.org/ticket/7744





---

archive/issue_comments_066623.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-01T10:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66623",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066624.json:
```json
{
    "body": "Useful for 3D printers, see http://www.thingiverse.com/thing:12784 for an interesting use case.\n\nI have mostly rewritten the code for better efficiency.\n\nMaybe this could be added in some way to the options of `.save` ?\n\n\nAnd it would be much better to use the binary STL format instead.\n----\nNew commits:",
    "created_at": "2014-08-01T10:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66624",
    "user": "chapoton"
}
```

Useful for 3D printers, see http://www.thingiverse.com/thing:12784 for an interesting use case.

I have mostly rewritten the code for better efficiency.

Maybe this could be added in some way to the options of `.save` ?


And it would be much better to use the binary STL format instead.
----
New commits:



---

archive/issue_comments_066625.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-01T13:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66625",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066626.json:
```json
{
    "body": "I have tested the STL export by loading the result in FreeCAD, and it works. I have now added the \"more modern\" xml-based AMF format, but not tested that it works sor far, as FreeCAD is not able to load that file format.\n\nIt is necessary to compress the AMF file with ZIP..",
    "created_at": "2014-08-01T14:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66626",
    "user": "chapoton"
}
```

I have tested the STL export by loading the result in FreeCAD, and it works. I have now added the "more modern" xml-based AMF format, but not tested that it works sor far, as FreeCAD is not able to load that file format.

It is necessary to compress the AMF file with ZIP..



---

archive/issue_comments_066627.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-01T17:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66627",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066628.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-01T17:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66628",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066629.json:
```json
{
    "body": "Maybe one could add the json format ?",
    "created_at": "2014-08-04T12:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66629",
    "user": "chapoton"
}
```

Maybe one could add the json format ?



---

archive/issue_comments_066630.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-05T07:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66630",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066631.json:
```json
{
    "body": "Let us forget about the json format, which is private between sage and sagenb.\n\nI think this ticket is ready for review now. It would be very useful to have it merged for use in #12212.",
    "created_at": "2014-08-05T19:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66631",
    "user": "chapoton"
}
```

Let us forget about the json format, which is private between sage and sagenb.

I think this ticket is ready for review now. It would be very useful to have it merged for use in #12212.



---

archive/issue_comments_066632.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-10T13:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66632",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066633.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-20T08:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66633",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066634.json:
```json
{
    "body": "patchbot has turned green ! time for a review, anybody ?",
    "created_at": "2014-08-23T09:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66634",
    "user": "chapoton"
}
```

patchbot has turned green ! time for a review, anybody ?



---

archive/issue_comments_066635.json:
```json
{
    "body": "I will take a look at it next week, when i will have my 3d printer available to check the output.",
    "created_at": "2014-08-25T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66635",
    "user": "mmarco"
}
```

I will take a look at it next week, when i will have my 3d printer available to check the output.



---

archive/issue_comments_066636.json:
```json
{
    "body": "Changing keywords from \"3D-Printing STL\" to \"3D-Printing, STL, X3D\".",
    "created_at": "2014-09-26T07:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66636",
    "user": "chapoton"
}
```

Changing keywords from "3D-Printing STL" to "3D-Printing, STL, X3D".



---

archive/issue_comments_066637.json:
```json
{
    "body": "Hello ! have you checked that the output is accepted by your 3d printer ?",
    "created_at": "2014-09-26T07:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66637",
    "user": "chapoton"
}
```

Hello ! have you checked that the output is accepted by your 3d printer ?



---

archive/issue_comments_066638.json:
```json
{
    "body": "Yes, it did work fine.",
    "created_at": "2014-09-27T20:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66638",
    "user": "mmarco"
}
```

Yes, it did work fine.



---

archive/issue_comments_066639.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-09-28T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66639",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066640.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-10-09T19:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66640",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066641.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-10-21T15:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66641",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066642.json:
```json
{
    "body": "Hello ? This one would be useful for #12212.",
    "created_at": "2014-11-02T20:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66642",
    "user": "chapoton"
}
```

Hello ? This one would be useful for #12212.



---

archive/issue_comments_066643.json:
```json
{
    "body": "I guess - this is pretty far outside my domain, anyway.  The changes here are not compatible with the ones at #16640, for what it's worth, though probably are easily taken into account.",
    "created_at": "2014-11-03T13:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66643",
    "user": "kcrisman"
}
```

I guess - this is pretty far outside my domain, anyway.  The changes here are not compatible with the ones at #16640, for what it's worth, though probably are easily taken into account.



---

archive/issue_comments_066644.json:
```json
{
    "body": "ping ? anybody for a review ?",
    "created_at": "2014-12-27T09:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66644",
    "user": "chapoton"
}
```

ping ? anybody for a review ?



---

archive/issue_comments_066645.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-06T21:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66645",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066646.json:
```json
{
    "body": "Could please someone have a look at that ? it has already started rotting..",
    "created_at": "2015-03-06T21:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66646",
    "user": "chapoton"
}
```

Could please someone have a look at that ? it has already started rotting..



---

archive/issue_comments_066647.json:
```json
{
    "body": "There are some people interested by this kind of stuff, see here : http://ask.sagemath.org/question/26075/transferring-3d-plots/",
    "created_at": "2015-03-08T19:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66647",
    "user": "chapoton"
}
```

There are some people interested by this kind of stuff, see here : http://ask.sagemath.org/question/26075/transferring-3d-plots/



---

archive/issue_comments_066648.json:
```json
{
    "body": "Still nobody for a review ?",
    "created_at": "2015-03-11T09:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66648",
    "user": "chapoton"
}
```

Still nobody for a review ?



---

archive/issue_comments_066649.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-31T08:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66649",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066650.json:
```json
{
    "body": "ping ?",
    "created_at": "2015-05-22T19:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66650",
    "user": "chapoton"
}
```

ping ?



---

archive/issue_comments_066651.json:
```json
{
    "body": "please, is there anybody to have a look ? this is not that complicated, just a few text-writing routines.",
    "created_at": "2015-07-22T13:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66651",
    "user": "chapoton"
}
```

please, is there anybody to have a look ? this is not that complicated, just a few text-writing routines.



---

archive/issue_comments_066652.json:
```json
{
    "body": "I am looking at it.\n\nSome comments:\n\nWould there be some way to doctest the saving feature? Maybe saving to a temporary file, then reading it, showing some part of the content and erasing.\n\nThe warning about only working for triangulated surfaces should go in a Warning section\n\nOtherwise the code looks good, although i am having some trouble to rebase it to latest version in order to test it.",
    "created_at": "2015-07-22T19:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66652",
    "user": "mmarco"
}
```

I am looking at it.

Some comments:

Would there be some way to doctest the saving feature? Maybe saving to a temporary file, then reading it, showing some part of the content and erasing.

The warning about only working for triangulated surfaces should go in a Warning section

Otherwise the code looks good, although i am having some trouble to rebase it to latest version in order to test it.



---

archive/issue_comments_066653.json:
```json
{
    "body": "Thanks. I am available, so one can hope to make progress together.\n\nI will wait for your review, unless you want me to make the required changes myself right now.",
    "created_at": "2015-07-23T07:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66653",
    "user": "chapoton"
}
```

Thanks. I am available, so one can hope to make progress together.

I will wait for your review, unless you want me to make the required changes myself right now.



---

archive/issue_comments_066654.json:
```json
{
    "body": "If you make the changes i suggested, and also rebase it to the latest development branch, i can test it and give the positive review.",
    "created_at": "2015-07-23T14:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66654",
    "user": "mmarco"
}
```

If you make the changes i suggested, and also rebase it to the latest development branch, i can test it and give the positive review.



---

archive/issue_comments_066655.json:
```json
{
    "body": "ok, I am doing that right now.",
    "created_at": "2015-07-23T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66655",
    "user": "chapoton"
}
```

ok, I am doing that right now.



---

archive/issue_comments_066656.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-23T15:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66656",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066657.json:
```json
{
    "body": "Ok, it looks  good. Although i didn't have any software that could import the .amf file (.x3d, .stl and .ply import ok in Bllender). \n\nI failed to save a sphere() object, since it is a TransformGroup object. Maybe it would be a good idea to have support for triangulating that kind of objects, but it would be a matter for a different ticket.",
    "created_at": "2015-07-24T10:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66657",
    "user": "mmarco"
}
```

Ok, it looks  good. Although i didn't have any software that could import the .amf file (.x3d, .stl and .ply import ok in Bllender). 

I failed to save a sphere() object, since it is a TransformGroup object. Maybe it would be a good idea to have support for triangulating that kind of objects, but it would be a matter for a different ticket.



---

archive/issue_comments_066658.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-07-24T10:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66658",
    "user": "mmarco"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066659.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-07-27T15:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66659",
    "user": "vbraun"
}
```

Resolution: fixed
