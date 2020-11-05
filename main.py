# -*- coding: UTF-8 -*-
import sys
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
import maya.mel as mel
import maya.api.OpenMayaUI as OpenMayaUI

reload(sys)
sys.setdefaultencoding('utf-8')
# Fix Chinese
def utf_8String(StringT):
  utf_8String = StringT
  utf_8String.encode('utf-8')
  utf_8String = unicode(utf_8String, "utf-8")
  return utf_8String

def bakePivots():
  selection = cmds.ls(sl=1)
  for object in selection:
      pivot = cmds.xform( object, query=True, pivots=True, worldSpace=True )
      cmds.polyColorPerVertex( object, rgb=( pivot[0], pivot[1], pivot[2] ))

def bakePhaseID():
  selection = cmds.ls(sl=1)
  for object in selection:


def mainGui():
  window_name = 'Export_Wind_Parameters_Tool1.0'
  window_title = 'Export_Wind_Parameters_Tool1.0'
  explain_str = "Bake pivot to vertex color xyz"

  # Prevent duplicate windows
  try:
    cmds.deleteUI(window_name)
  except:
    pass

  window = cmds.window(window_name, title = window_title)
  form = cmds.formLayout()
  # editor = cmds.spNarrowPolyViewer()
  column = cmds.columnLayout(adjustableColumn=True)

  cmds.button(label="Bake Pivot",ann = explain_str, command='bakePivots()')
  cmds.button(label="Bake Phase ID", ann=explain_str, command='bakePivots()')

  cmds.showWindow(window)

mainGui()