import maya.cmds as mc

 

# get shape node of selected curves

thethings = mc.ls(selection=True)

thethingsShapes = mc.listRelatives(thethings, s=True)

print thethingsShapes

 

# freeze transforms of selected curves

mc.makeIdentity( thethings, apply=True, t=True, r=True, s=True )

 

# create null transform to parent shapes to

pooper = mc.group(em=True, name="newCombinedCtl")

 

# parent shapes to null

mc.parent(thethingsShapes, pooper, s=True, r=True)

 

# remove old transforms

mc.delete(thethings)