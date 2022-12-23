# Issue 7744: STL Export -- Allows for 3d printing of surfaces

Issue created by migration from https://trac.sagemath.org/ticket/7744

Original creator: colah

Original creation time: 2009-12-20 17:07:34

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




---

Comment by chapoton created at 2014-08-01 10:21:06

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-08-01 10:21:06

Useful for 3D printers, see http://www.thingiverse.com/thing:12784 for an interesting use case.

I have mostly rewritten the code for better efficiency.

Maybe this could be added in some way to the options of `.save` ?


And it would be much better to use the binary STL format instead.
----
New commits:


---

Comment by git created at 2014-08-01 13:59:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-08-01 14:01:55

I have tested the STL export by loading the result in FreeCAD, and it works. I have now added the "more modern" xml-based AMF format, but not tested that it works sor far, as FreeCAD is not able to load that file format.

It is necessary to compress the AMF file with ZIP..


---

Comment by git created at 2014-08-01 17:01:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-01 17:37:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-08-04 12:27:48

Maybe one could add the json format ?


---

Comment by git created at 2014-08-05 07:32:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-08-05 19:47:33

Let us forget about the json format, which is private between sage and sagenb.

I think this ticket is ready for review now. It would be very useful to have it merged for use in #12212.


---

Comment by git created at 2014-08-10 13:11:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-20 08:03:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-08-23 09:26:53

patchbot has turned green ! time for a review, anybody ?


---

Comment by mmarco created at 2014-08-25 13:29:40

I will take a look at it next week, when i will have my 3d printer available to check the output.


---

Comment by chapoton created at 2014-09-26 07:57:40

Changing keywords from "3D-Printing STL" to "3D-Printing, STL, X3D".


---

Comment by chapoton created at 2014-09-26 07:57:40

Hello ! have you checked that the output is accepted by your 3d printer ?


---

Comment by mmarco created at 2014-09-27 20:56:32

Yes, it did work fine.


---

Comment by git created at 2014-09-28 11:53:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-10-09 19:03:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-10-21 15:57:08

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-11-02 20:27:44

Hello ? This one would be useful for #12212.


---

Comment by kcrisman created at 2014-11-03 13:40:54

I guess - this is pretty far outside my domain, anyway.  The changes here are not compatible with the ones at #16640, for what it's worth, though probably are easily taken into account.


---

Comment by chapoton created at 2014-12-27 09:50:43

ping ? anybody for a review ?


---

Comment by git created at 2015-03-06 21:21:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-03-06 21:23:51

Could please someone have a look at that ? it has already started rotting..


---

Comment by chapoton created at 2015-03-08 19:56:45

There are some people interested by this kind of stuff, see here : http://ask.sagemath.org/question/26075/transferring-3d-plots/


---

Comment by chapoton created at 2015-03-11 09:54:41

Still nobody for a review ?


---

Comment by git created at 2015-03-31 08:16:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-22 19:33:46

ping ?


---

Comment by chapoton created at 2015-07-22 13:02:19

please, is there anybody to have a look ? this is not that complicated, just a few text-writing routines.


---

Comment by mmarco created at 2015-07-22 19:02:03

I am looking at it.

Some comments:

Would there be some way to doctest the saving feature? Maybe saving to a temporary file, then reading it, showing some part of the content and erasing.

The warning about only working for triangulated surfaces should go in a Warning section

Otherwise the code looks good, although i am having some trouble to rebase it to latest version in order to test it.


---

Comment by chapoton created at 2015-07-23 07:15:52

Thanks. I am available, so one can hope to make progress together.

I will wait for your review, unless you want me to make the required changes myself right now.


---

Comment by mmarco created at 2015-07-23 14:41:36

If you make the changes i suggested, and also rebase it to the latest development branch, i can test it and give the positive review.


---

Comment by chapoton created at 2015-07-23 15:17:33

ok, I am doing that right now.


---

Comment by git created at 2015-07-23 15:31:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmarco created at 2015-07-24 10:22:21

Ok, it looks  good. Although i didn't have any software that could import the .amf file (.x3d, .stl and .ply import ok in Bllender). 

I failed to save a sphere() object, since it is a TransformGroup object. Maybe it would be a good idea to have support for triangulating that kind of objects, but it would be a matter for a different ticket.


---

Comment by mmarco created at 2015-07-24 10:22:21

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-07-27 15:16:02

Resolution: fixed
