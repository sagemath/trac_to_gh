# Issue 2333: [easy to implement] hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2245/sage-2245.patch') should be made to work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-27 17:53:10

Assignee: was


```


On Wed, Feb 27, 2008 at 8:32 AM, Simon King <king`@`mathematik.uni-jena.de> wrote:
> 
>  Dear team,
>  
>  i started to work with Mercurial and tried to understand
>  http://modular.math.washington.edu/sage/doc/html/prog/node72.html
>  
>  I changed to a new branch, i.e.
>  > sage -clone myrep
>  > sage -b myrep
>  
>  Meanwhile i also learned (more or less) how to create a patch.
>  
>  But what shall i do in order to apply a patch downloaded from that
>  trac system?
>  I tried
>  sage:  hg_sage.import_patch('../work/SingularElementCopy.patch')
>  
>  However, this was aborted with the comment "no diffs found".
>  
>  What does that mean? How can one apply a patch?
>  
>  Suggestion: The "Quick Mercurial tutorial for Sage" could also say a
>  few words about the trac system.

To apply a patch from trac, e.g., the one here:
     http://trac.sagemath.org/sage_trac/ticket/2245
do this:

 1. Click on the patch.
 2. Go to the bottom of the screen and copy and paste the url for "Original format",
e.g., right click and say "copy".
 3. Paste the result into hg_sage.apply(...), e.g.,
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2245/sage-2245.patch?format=raw')

--

It would also be nice if hg_sage were smart enough to automatically detect the
non-raw url (that you click on in step 1 above) and automatically get the raw file
instead.  E.g., this could be made to work

sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2245/sage-2245.patch')

This would be easy to implement -- if ever the input to apply contains
   http://[anything]attachment/ticket/2245/[anything]
and doesn't end in ?format=raw, just append it.   That would make it easy to 
completely skip the step where you have to find the raw format link.

Since this is so trivial to implement I've made it a trac ticket:
  

```



---

Comment by mabshoff created at 2008-02-28 01:17:37

I can't get it to work:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2333/2333.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/2333/2333.patch
Loading: [.]
cd "/scratch/mabshoff/release-cycle/sage-2.10.3.rc0/devel/sage" && hg status
cd "/scratch/mabshoff/release-cycle/sage-2.10.3.rc0/devel/sage" && hg status
cd "/scratch/mabshoff/release-cycle/sage-2.10.3.rc0/devel/sage" && hg import   "/home/mabshoff/.sage/temp/sage/2132/tmp_1.patch"
applying /home/mabshoff/.sage/temp/sage/2132/tmp_1.patch
abort: no diffs found
sage:
Exiting SAGE (CPU time 0m0.15s, Wall time 0m56.24s).
```


Cheers,

Michael


---

Attachment


---

Attachment


---

Attachment

All three patches should be applied in order.


---

Comment by mabshoff created at 2008-03-02 20:49:03

The subject screws with the wrapping of the ticket view, so change it :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 12:31:22

Merged all three patches in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-03 12:31:22

Resolution: fixed
