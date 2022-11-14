
 Please register patchbots below, giving contact details
(e.g. a Sage Trac username) for the owner of each patchbot.

This helps contact the owner when a patchbot is stuck.

```
patchbot name           owner
-------------           -----
andromeda               jkroeker
arando                  jdemeyer
ark                     rws
athena                  kdilks
btm2x13                 mderickx
bunion                  etn40ff (this is a laptop so it will be running sporadically)
cristal                 Bouillaguet
debian_jessie_32        tmonteil
eddy                    Vincent.Neri (LRI, Orsay, Paris-Sud)
fermat                  cremona, davidloeffler
findstat                stumpc5
geom                    dimpase
groebner                jkroeker
hades                   klee
icj-laptop              chapoton
kepler                  nilesjohnson
kevin-Virtualbox        kdilks
mangouste               vdelecroix
manifold                egourgoulhon
martin-Laptop           mantepse
mercury                 kdilks
panke                   gh-kliem
pascaline               slelievre
pbua                    novoselt
pc72-math               dkrenn (and behackl and cheuberg)
pell                    galipnik
petitbonum              chapoton
poseidon                kdilks
quasar                  vdelecroix
rk02-math               cheuberg (and dkrenn)
sage4                   jdemeyer
sardonis                jdemeyer
silence                 ncohen
steenrod                ​jhpalmieri
tmonteil-*              tmonteil (various arch/OS/releases; contact me to run a 32-bit patchbot on a particular ticket)
ubuntu_vivid_64         tmonteil
vogon.jeltz(32Bit)      jkroeker
x200t-ThinkPad-*        jkroeker
zorn                    agd
44e979ad077a            embray (docker installation)
```

Instructions for running a patchbot are on the [[patchbot]] page of this wiki.

When running a patchbot, its name is defined by the `HOSTNAME`
environment variable. To check what name your patchbot will have,
run `echo $HOSTNAME` in a terminal. To set the name to `something_else`,
run `HOSTNAME=something_else` before launching it.

Patchbot owners are encouraged to associate their real name to their
Sage Trac username in the list of Sage developers present on the
[main page of the Sage Trac server](https://trac.sagemath.org/#AccountNamesMappedtoRealNames). That list is a good
place to add a link to their homepage which ideally will contain some
way to contact them (e.g. email address) should the need arise.
