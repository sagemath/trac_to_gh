# Issue 5227: add next batch of 14 people to devmap

Issue created by migration from https://trac.sagemath.org/ticket/5227

Original creator: mvngu

Original creation time: 2009-02-10 07:56:34

Assignee: tba

CC:  schilly gmoroz

Keywords: devmap

As the subject says. This is a joint project with Michael Abshoff and Harald Schilly. The devmap in question is the site



http://www.sagemath.org/development-map.html



---

Attachment

alphabetize the current devmap


---

Attachment

add 14 people to devmap


---

Attachment

update info for Simon King and Georg S. Weber


---

Attachment

update info for Arnaud Bergeron, David Loeffler and Jason Merrill


---

Comment by mvngu created at 2009-02-10 08:38:02

The attached file `contributors.xml` is an updated XML file for the development map. For those folks who like to view diffs, I've attached the relevant diffs produced using Mercurial. The patch `trac_5227-alphabetize.patch` re-organizes the current devmap XML file, in particular, alphabetizing the names list except for William Stein. The patch `trac_5227-14-new-people.patch` adds the following people to the devmap:
  1. Maite Aranes
  1. Tom Denton
  1. Amy Glen
  1. Daniel Gordon
  1. Alexander Hupfer
  1. Yann Laigle-Chapuy
  1. Matthias Meulien
  1. Ronan Paixão
  1. David Perkinson
  1. Pearu Peterson
  1. Blair Sutton
  1. Griffen Thoma
  1. Georg S. Weber
  1. Bin Zhang

The patches `trac_5227-update-info-1.patch` and `trac_5227-update-info-2.patch` update information for the following people:
  1. Arnaud Bergeron
  1. Simon King
  1. David Loeffler
  1. Jason Merrill


---

Comment by mvngu created at 2009-02-10 08:52:07

If my counting is correct, the updated XML file shows information for *141* Sage developers around the world.


---

Comment by zimmerma created at 2009-02-12 11:20:31

to my best knowledge, the location of Guillaume Moroz is wrong: instead of being in the middle
of France, it should be in Paris (LIP6 is in Paris). The best is to check with him of course.


---

Comment by mabshoff created at 2009-02-12 11:34:26

Well, 

the flag being in the middle of a country usually indicates that the address in the XML file is not resolvable by Google.

Cheers,

Michael


---

Comment by schilly created at 2009-02-12 11:48:31

Replying to [comment:3 zimmerma]:
> to my best knowledge, the location of Guillaume Moroz is wrong: instead of being in the middle
> of France, it should be in Paris (LIP6 is in Paris). The best is to check with him of course.

the location is feed into maps.google.com. if you go there, enter the location string 1:1 and hit search and the first hit is wrong, it will be also wrong on the devmap! from my experience, changing a word or some details is enough to get it right.

behind the scenes, offline: all location strings are extrcted and a script creates a mapping from each uniqe string to the lat/long coordinates that are then used online by the map-javascript when loading the page and placing the markers.


---

Comment by zimmerma created at 2009-02-12 11:57:07

"Guillaume Moroz LIP6" on maps.google.com finds only one location, which is the correct one.
However I don't know how to give that hint to the devmap.


---

Comment by schilly created at 2009-02-12 12:02:18

Replying to [comment:7 zimmerma]:
> "Guillaume Moroz LIP6" on maps.google.com finds only one location...

well, i wasn't honest, google maps already narrows down the possible hits, if you have zoomed into a location. for this location, i think "Guillaume Moroz LIP6, Paris, Fr" is ok.


---

Comment by GeorgSWeber created at 2009-02-15 20:39:45

(Try to adjust the Summary so that this ticket shows up on the radar, especially View tickets "10")


---

Comment by GeorgSWeber created at 2009-02-15 20:40:37

Yep, it's now (and only now) visible under "http://trac.sagemath.org/sage_trac/report/10"


---

Comment by GeorgSWeber created at 2009-02-15 20:51:35

Hi Minh,

could you please change line 148 (my own personal entry) to:

```
<contributor name="Georg S. Weber" location="NÃŒrnberg, Germany" description="reviews, bug fixing, documentation"/>
```

since I would like to ask first at my institute before it is published here (more a formality than anything else, but nevertheless); I updated also the description.

Thanks for your work!!

Cheers, gsw


---

Comment by schilly created at 2009-02-15 20:54:50

just a short note, drop a message when this ready for upload to the website. so far the xml file looks good...


---

Comment by mabshoff created at 2009-02-16 05:01:02

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael


---

Comment by mvngu created at 2009-02-17 03:33:37

update information for Georg S. Weber


---

Attachment

the updated XML file after applying the attached 5 patches


---

Comment by mvngu created at 2009-02-17 03:41:49

The patch `trac_5227-update-info-3.patch` updates information for Georg S. Weber as he has requested. This is handy for folks who want to view Mercurial diffs. I've updated an updated `contributors.xml` file containing changes in the attached 5 patches. I'm sorry, folks, for taking so long to fix this issue.



`@`Harald


Just a friendly reminder that you should use `contributors.xml` for the devmap, instead of the Mercurial patches.


---

Comment by schilly created at 2009-02-17 13:28:37

Hi, i've uploaded the `contributors.xml` file. There were some issues:
 * the geocode api doesn't understand non-ascii characters for locations, that's easy 
 * i had problems with the location of Yann Laigle-Chapuy ... it wasn't found, mabye new adress or some contradiction.


---

Comment by mabshoff created at 2009-02-17 13:32:14

Resolution: fixed


---

Comment by mabshoff created at 2009-02-17 13:32:14

Ok, looks good to me. We can fix the remaining issues via a followup ticket.

Cheers,

Michael


---

Comment by schilly created at 2009-02-17 13:34:06

And yes, i'm also for closing this ticket.

The `contributors.xml` that's now online is here:
http://www.sagemath.org/res/contributors.xml

Use this as a base for future updates, as usual,. and thanks for collecting all those details! :)


---

Comment by mabshoff created at 2009-02-17 13:38:51

Ok, I have updated the wiki page at 

  http://wiki.sagemath.org/DevMapNewPeople

with the info merged here today.

Cheers,

Michael
