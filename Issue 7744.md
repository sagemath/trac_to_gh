# Issue 7744: STL Export -- Allows for 3d printing of surfaces

archive/issues_007744.json:
```json
{
    "body": "Assignee: colah\n\nCC:  @nilesjohnson @kcrisman @jdemeyer tmonteil\n\nKeywords: 3D-Printing STL\n\n\n```\ndef surface_to_stl(surface):\n    \"\"\"\n    Return an STL representation of the surface.\n    \n    INPUT:\n        - `surface` -- any surface, eg. output of a 3d plot function.\n    \n    OUTPUT:\n        A string that represents the surface in the STL format.\n    \n    COMMENTS:\n        (1) You must view the surface before plotting it.\n            Otherwise, this will not work.\n        (2) In order to do 3d printing with this, you will need to\n            convert it into gcode. Skeinforge is an open-source\n            program that can do this.\n        (3) The size of the surface is not normalized in export.\n            Sage's units will become the units of the STL \n            description. These seem to be ~0.05 cm (at least when \n            printed using skeinforge -> replicatorg -> hacklab.to's \n            cupcake).\n        (4) Be aware of the overhang limits of your 3d printer; \n            most printers can only handle an overhang of Pi/2 (45*) \n            before your model will start drooping.\n    \n    EXAMPLES:\n        sage: x,y,z = var('x,y,z')\n        sage: a = implicit_plot3d(x^2+y^2+z^2-9, [x,-5,5], [y,-5,5],[z,-5,5])\n        sage: a\n        sage: f=file.open(\"foo.stl\",'w')\n        sage: f.write(surface_to_stl(a))\n        sage: f.close()\n    \"\"\"\n \n    out =  \"solid mathsurface\\n\"\n    for i in surface.face_list():\n        n = ( i[1][1]*i[2][2] - i[2][1]*i[1][2],\n              i[1][2]*i[2][0] - i[1][0]*i[2] 2],\n              i[1][0]*i[2][1] - i[2][0]*i[1][1] )\n        abs = (n[0]^2+n[1]^2+n[2]^2)^0.5\n        n= (n[0]/abs,n[1]/abs,n[2]/abs)\n        out += \"  facet normal \" + repr(n[0])  + \" \" + repr(n[1])    + \" \" + repr(n[2])\n        out += \"    outer loop\\n\"\n        out += \"      vertex \" + repr(i[0][0]) + \" \" + repr(i[0][1]) + \" \" + repr(i[0][2]) + \"\\n\"\n        out += \"      vertex \" + repr(i[1][0]) + \" \" + repr(i[1][1]) + \" \" + repr(i[1][2]) + \"\\n\"\n        out += \"      vertex \" + repr(i[2][0]) + \" \" + repr(i[2][1]) + \" \" + repr(i[2][2]) + \"\\n\"\n        out += \"    endloop\\n\"\n        out += \"  endfacet\\n\"\n    out += \"endsolid surface\\n\"\n    return out\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7744\n\n",
    "created_at": "2009-12-20T17:07:34Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "STL Export -- Allows for 3d printing of surfaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7744",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```
Assignee: colah

CC:  @nilesjohnson @kcrisman @jdemeyer tmonteil

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

archive/issue_comments_066507.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-01T10:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66507",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066508.json:
```json
{
    "body": "Useful for 3D printers, see http://www.thingiverse.com/thing:12784 for an interesting use case.\n\nI have mostly rewritten the code for better efficiency.\n\nMaybe this could be added in some way to the options of `.save` ?\n\n\nAnd it would be much better to use the binary STL format instead.\n----\nNew commits:",
    "created_at": "2014-08-01T10:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66508",
    "user": "https://github.com/fchapoton"
}
```

Useful for 3D printers, see http://www.thingiverse.com/thing:12784 for an interesting use case.

I have mostly rewritten the code for better efficiency.

Maybe this could be added in some way to the options of `.save` ?


And it would be much better to use the binary STL format instead.
----
New commits:



---

archive/issue_comments_066509.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-01T13:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66509",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066510.json:
```json
{
    "body": "I have tested the STL export by loading the result in FreeCAD, and it works. I have now added the \"more modern\" xml-based AMF format, but not tested that it works sor far, as FreeCAD is not able to load that file format.\n\nIt is necessary to compress the AMF file with ZIP..",
    "created_at": "2014-08-01T14:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66510",
    "user": "https://github.com/fchapoton"
}
```

I have tested the STL export by loading the result in FreeCAD, and it works. I have now added the "more modern" xml-based AMF format, but not tested that it works sor far, as FreeCAD is not able to load that file format.

It is necessary to compress the AMF file with ZIP..



---

archive/issue_comments_066511.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-01T17:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66511",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066512.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-01T17:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66512",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066513.json:
```json
{
    "body": "Maybe one could add the json format ?",
    "created_at": "2014-08-04T12:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66513",
    "user": "https://github.com/fchapoton"
}
```

Maybe one could add the json format ?



---

archive/issue_comments_066514.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-05T07:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66514",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066515.json:
```json
{
    "body": "Let us forget about the json format, which is private between sage and sagenb.\n\nI think this ticket is ready for review now. It would be very useful to have it merged for use in #12212.",
    "created_at": "2014-08-05T19:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66515",
    "user": "https://github.com/fchapoton"
}
```

Let us forget about the json format, which is private between sage and sagenb.

I think this ticket is ready for review now. It would be very useful to have it merged for use in #12212.



---

archive/issue_comments_066516.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-10T13:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66516",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066517.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-20T08:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66517",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066518.json:
```json
{
    "body": "patchbot has turned green ! time for a review, anybody ?",
    "created_at": "2014-08-23T09:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66518",
    "user": "https://github.com/fchapoton"
}
```

patchbot has turned green ! time for a review, anybody ?



---

archive/issue_comments_066519.json:
```json
{
    "body": "I will take a look at it next week, when i will have my 3d printer available to check the output.",
    "created_at": "2014-08-25T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66519",
    "user": "https://github.com/miguelmarco"
}
```

I will take a look at it next week, when i will have my 3d printer available to check the output.



---

archive/issue_comments_066520.json:
```json
{
    "body": "Changing keywords from \"3D-Printing STL\" to \"3D-Printing, STL, X3D\".",
    "created_at": "2014-09-26T07:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66520",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "3D-Printing STL" to "3D-Printing, STL, X3D".



---

archive/issue_comments_066521.json:
```json
{
    "body": "Hello ! have you checked that the output is accepted by your 3d printer ?",
    "created_at": "2014-09-26T07:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66521",
    "user": "https://github.com/fchapoton"
}
```

Hello ! have you checked that the output is accepted by your 3d printer ?



---

archive/issue_comments_066522.json:
```json
{
    "body": "Yes, it did work fine.",
    "created_at": "2014-09-27T20:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66522",
    "user": "https://github.com/miguelmarco"
}
```

Yes, it did work fine.



---

archive/issue_comments_066523.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-09-28T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66523",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066524.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-10-09T19:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66524",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066525.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-10-21T15:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66525",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066526.json:
```json
{
    "body": "Hello ? This one would be useful for #12212.",
    "created_at": "2014-11-02T20:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66526",
    "user": "https://github.com/fchapoton"
}
```

Hello ? This one would be useful for #12212.



---

archive/issue_comments_066527.json:
```json
{
    "body": "I guess - this is pretty far outside my domain, anyway.  The changes here are not compatible with the ones at #16640, for what it's worth, though probably are easily taken into account.",
    "created_at": "2014-11-03T13:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66527",
    "user": "https://github.com/kcrisman"
}
```

I guess - this is pretty far outside my domain, anyway.  The changes here are not compatible with the ones at #16640, for what it's worth, though probably are easily taken into account.



---

archive/issue_comments_066528.json:
```json
{
    "body": "ping ? anybody for a review ?",
    "created_at": "2014-12-27T09:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66528",
    "user": "https://github.com/fchapoton"
}
```

ping ? anybody for a review ?



---

archive/issue_comments_066529.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-06T21:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66529",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066530.json:
```json
{
    "body": "Could please someone have a look at that ? it has already started rotting..",
    "created_at": "2015-03-06T21:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66530",
    "user": "https://github.com/fchapoton"
}
```

Could please someone have a look at that ? it has already started rotting..



---

archive/issue_comments_066531.json:
```json
{
    "body": "There are some people interested by this kind of stuff, see here : http://ask.sagemath.org/question/26075/transferring-3d-plots/",
    "created_at": "2015-03-08T19:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66531",
    "user": "https://github.com/fchapoton"
}
```

There are some people interested by this kind of stuff, see here : http://ask.sagemath.org/question/26075/transferring-3d-plots/



---

archive/issue_comments_066532.json:
```json
{
    "body": "Still nobody for a review ?",
    "created_at": "2015-03-11T09:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66532",
    "user": "https://github.com/fchapoton"
}
```

Still nobody for a review ?



---

archive/issue_comments_066533.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-31T08:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66533",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066534.json:
```json
{
    "body": "ping ?",
    "created_at": "2015-05-22T19:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66534",
    "user": "https://github.com/fchapoton"
}
```

ping ?



---

archive/issue_comments_066535.json:
```json
{
    "body": "please, is there anybody to have a look ? this is not that complicated, just a few text-writing routines.",
    "created_at": "2015-07-22T13:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66535",
    "user": "https://github.com/fchapoton"
}
```

please, is there anybody to have a look ? this is not that complicated, just a few text-writing routines.



---

archive/issue_comments_066536.json:
```json
{
    "body": "I am looking at it.\n\nSome comments:\n\nWould there be some way to doctest the saving feature? Maybe saving to a temporary file, then reading it, showing some part of the content and erasing.\n\nThe warning about only working for triangulated surfaces should go in a Warning section\n\nOtherwise the code looks good, although i am having some trouble to rebase it to latest version in order to test it.",
    "created_at": "2015-07-22T19:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66536",
    "user": "https://github.com/miguelmarco"
}
```

I am looking at it.

Some comments:

Would there be some way to doctest the saving feature? Maybe saving to a temporary file, then reading it, showing some part of the content and erasing.

The warning about only working for triangulated surfaces should go in a Warning section

Otherwise the code looks good, although i am having some trouble to rebase it to latest version in order to test it.



---

archive/issue_comments_066537.json:
```json
{
    "body": "Thanks. I am available, so one can hope to make progress together.\n\nI will wait for your review, unless you want me to make the required changes myself right now.",
    "created_at": "2015-07-23T07:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66537",
    "user": "https://github.com/fchapoton"
}
```

Thanks. I am available, so one can hope to make progress together.

I will wait for your review, unless you want me to make the required changes myself right now.



---

archive/issue_comments_066538.json:
```json
{
    "body": "If you make the changes i suggested, and also rebase it to the latest development branch, i can test it and give the positive review.",
    "created_at": "2015-07-23T14:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66538",
    "user": "https://github.com/miguelmarco"
}
```

If you make the changes i suggested, and also rebase it to the latest development branch, i can test it and give the positive review.



---

archive/issue_comments_066539.json:
```json
{
    "body": "ok, I am doing that right now.",
    "created_at": "2015-07-23T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66539",
    "user": "https://github.com/fchapoton"
}
```

ok, I am doing that right now.



---

archive/issue_comments_066540.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-23T15:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66540",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_066541.json:
```json
{
    "body": "Ok, it looks  good. Although i didn't have any software that could import the .amf file (.x3d, .stl and .ply import ok in Bllender). \n\nI failed to save a sphere() object, since it is a TransformGroup object. Maybe it would be a good idea to have support for triangulating that kind of objects, but it would be a matter for a different ticket.",
    "created_at": "2015-07-24T10:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66541",
    "user": "https://github.com/miguelmarco"
}
```

Ok, it looks  good. Although i didn't have any software that could import the .amf file (.x3d, .stl and .ply import ok in Bllender). 

I failed to save a sphere() object, since it is a TransformGroup object. Maybe it would be a good idea to have support for triangulating that kind of objects, but it would be a matter for a different ticket.



---

archive/issue_comments_066542.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-07-24T10:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66542",
    "user": "https://github.com/miguelmarco"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-07-27T15:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7744#issuecomment-66543",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
