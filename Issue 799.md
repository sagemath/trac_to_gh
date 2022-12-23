# Issue 799: tachyon bug

Issue created by migration from https://trac.sagemath.org/ticket/799

Original creator: was

Original creation time: 2007-10-03 06:25:14

Assignee: was


```

I think I may have found a bug.

When using Tachyon and defining a texture, the seventh parameter you
can set is texfunc.
If that value is set to anything but zero, then no picture is
generated.

As an example:

t = Tachyon(xres=800, yres=600, camera_center=(2,7,4),
look_at=(2,0,0), raydepth=24)
t.light((10,3,4), 1, (1,1,1))
t.light((10,-3,4), 1, (1,1,1))
t.texture('black', color=(0,0,0))
t.texture('mirror', ambient=0.05, diffuse=0.05, specular=.9,
opacity=1.0, color=(.9,.9,.9))
t.texture('grey', color=(.8,.8,.8), texfunc=0)
t.plane((0,0,0),(0,0,1),'grey')
t.cylinder((0,0,0),(1,0,0),.013,'black')
t.cylinder((0,0,0),(0,1,0),.013,'black')
t.sphere((4,-1,1), 1, 'mirror')
t.save()

The above produces a nice picture.  If you change to "texfunc=2" in
line 6, then there is no output.

Texfunc should have the following allowed values

Value for TEXFUNC    Mapping and Texture Description
-----------------
----------------------------------------------------------------
     0              No special texture, plain shading
     1              3D checkerboard function, like a rubik's cube
     2              Grit Texture, randomized surface color
     3              3D marble texture, uses object's base color
     4              3D wood texture, light and dark brown, not very
good yet
     5              3D gradient noise function (can't remember what
it look like
     6              Don't remember
     7              Cylindrical Image Map, requires ppm filename
     8              Spherical Image Map, requires ppm filename
     9              Planar Image Map, requires ppm filename

I'm sorry if this is really a bug in Tachyon and not a problem with
how Sage talks with Tachyon.  I am just not (yet) skilled enough to
tell the difference.  I need to figure out how to run Tachyon stand-
alone and see if the bug still exists.  But, I don't know how yet.
So, my apologies if this should be reported to the Tachyon developers.
```


Many thanks for your bug report. 

By the way, even if it is a Tachyon bug, we really want to know about
it, so we can program around it and/or fix it.

William


---

Comment by was created at 2007-11-28 13:30:55


```
From Leif Hille 

I dunno if this is the right way to comment on bugs however, I ran into the same problem as the ticket's author. This "bug" ticket is part bug, part user error (or poor documentation).  

(1) The user error part: In order to create a texture using a number other than zero, you have to pass in a .texfunc() object.  

(2) The bug part: There is a problem with the plot/tachyon.py function that prevents additional key parameters from being passed in.  

Explanation:
    t.texture('grey', color=(.5,.5,.5), texfunc=0)  --> this works
    t.texture('dk_grey', color=(0.8,0.8,0.8),textfunc=1) --> this causes subsequent t.show() command to fail.  

Solution:
(1) While the t.texture(...) function allows for 'texfunc=0' as an argument, for any number greater than 0, it expects a texfunc object.

ie:
r=t.texfunc(2)
t.texture('grey', color=(.5,.5,.5), texfunc=r)

This is not evident from the inline help & the interface doesn't complain when it's passed bad input - it just fails when t.show() is called (verbose mode reveals the tachyon parser's complaints).

(2) The bug is that some of the predefined numbered textures require additional string input (eg. a file name for a texture map image/data) immediately after the texture number.  The texture number is passed in as a number.  I've made a workaround, making the "type" parameter into a string(see changes below), allowing for filenames to be specified when the texture number calls for it.  This is still a little troublesome in that because it's not obvious to me how to reference filenames of graphics created within Sage (maybe there should there be a toplevel "fileref" method to get a filesystem path reference to existing graphic image or dataset).  The same filereference problem presents if the user wants to use another graphic or datafile as a texture map.  

##from : .../plot/tachyon.py...
 class Texfunc:
  def __init__(self, type=0,center=(0,0,0), rotate=(0,0,0), scale=(1,1,1)):
     self._type = type
     self._center = center
     self._rotate = rotate
     self._scale = scale

  def str(self):
     if type == 0:
          return "0"
#  Old Code
#     return """%d center %s rotate %s scale %s"""%(self._type,          # <-- number
#                                                   >tostr(self._center),
#                                                   >tostr(self._rotate),
#                                                    tostr(self._scale))
# new code:
     return """%s center %s rotate %s scale %s"""%(tostr(self._type),          # <-- string
                                                   >tostr(self._center),
                                                   >tostr(self._rotate),
                                                    tostr(self._scale))
```



---

Attachment


---

Attachment


---

Comment by cwitty created at 2007-12-02 07:19:10

These patches are definitely an improvement, and should go in.

There's still some more work to be done (documentation at least, perhaps some code too) to be able to use the full power of tachyon (like texture maps); but that can wait for later.


---

Comment by mabshoff created at 2007-12-02 07:23:44

Merged in 2.8.15.alpha2.


---

Comment by mabshoff created at 2007-12-02 07:23:44

Resolution: fixed
