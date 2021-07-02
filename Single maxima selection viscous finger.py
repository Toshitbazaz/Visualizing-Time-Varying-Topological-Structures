from paraview.simple import *
import vtk
view = GetActiveViewOrCreate('RenderView')
layout1 = GetLayout()
layout1.SplitHorizontal(0, 0.5)
view1 = CreateView('RenderView')
AssignViewToLayout(view=view1, layout=layout1, hint=2)
file1 = open("3.csv","r")
line = file1.readline()
line = file1.readline()
file1.close()
L = list(map(str, line.split(',')))
a=L[0]
b=L[1]
c=L[2]
c = list(map(str, c.split('\n')))
c = c[0]
A = a + ' ' + b + ' ' + c
flag = 0
start = 0
for i in range(119):
 name1 = 'New\Correspondence\Edge_list_' + str(i+1) + '_' + str(i+2) + '.txt' 
 file = open(name1,"r")
 while True:
  line = file.readline()
  if not line:
   break
  L = list(map(str, line.split('(')))
  L = L[1]
  L = list(map(str, L.split(')')))
  L = L[0]
  L = list(map(str, L.split(',')))
  a1 = L[0]
  b1 = L[1]
  c1 = L[2]
  A1 = a1 + b1 + c1
  if(A==A1):
   if(flag==0):
    start = i
    if(i<11):
     end = 11
    elif(i<48):
     end = 48
    elif(i<54):
     end = 54
    elif(i<66):
     end = 66
    elif(i<85):
     end = 85
    elif(i<105):
     end = 105
    elif(i<113):
     end = 113
    else:
     end = 119
   flag = 1
   M = list(map(str, line.split(')')))
   M = M[1]
   M = list(map(str, M.split(' ')))
   M = M[1]
   M = list(map(str, M.split('\n')))
   M = M[0]
   name = 'Viscousfingerextremum\sample_' + str(i) + '.vtk' 
   reader = OpenDataFile(name)
   sample_graph_Display = Show(reader)
   sample_graph_Display.Representation = 'Points'
   sample_graph_Display.RenderPointsAsSpheres = 1
   sample_graph_Display.PointSize = 5.0
   sample_graph_Display.Opacity = 1.0
   sample_graph_Display.ColorArrayName = [None, '']
   sample_graph_Display.OSPRayScaleArray = 'vertexColors'
   sample_graph_Display.OSPRayScaleFunction = 'PiecewiseFunction'
   sample_graph_Display.SelectOrientationVectors = 'None'
   sample_graph_Display.ScaleFactor = 12.700000000000001
   sample_graph_Display.SelectScaleArray = 'None'
   sample_graph_Display.GlyphType = 'Arrow'
   sample_graph_Display.GlyphTableIndexArray = 'None'
   sample_graph_Display.GaussianRadius = 0.635
   sample_graph_Display.SetScaleArray = ['POINTS', 'vertexColors']
   sample_graph_Display.ScaleTransferFunction = 'PiecewiseFunction'
   sample_graph_Display.OpacityArray = ['POINTS', 'vertexColors']
   sample_graph_Display.OpacityTransferFunction = 'PiecewiseFunction'
   sample_graph_Display.DataAxesGrid = 'GridAxesRepresentation'
   sample_graph_Display.PolarAxes = 'PolarAxesRepresentation'
   # set scalar coloring
   ColorBy(sample_graph_Display, ('POINTS', 'vertexColors'))
   # rescale color and/or opacity maps used to include current data range
   sample_graph_Display.RescaleTransferFunctionToDataRange(True, False)
   # show color bar/color legend
   sample_graph_Display.SetScalarBarVisibility(view1, True)
   # get color transfer function/color map for 'vertexColors'
   vertexColorsLUT = GetColorTransferFunction('vertexColors')
   # get opacity transfer function/opacity map for 'vertexColors'
   vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
   Render()
   reader = OpenDataFile(name)
   sample_graph_Display = Show(reader)
   sample_graph_Display.Representation = 'Surface' 
   sample_graph_Display.RenderLinesAsTubes = 1
   sample_graph_Display.LineWidth = 2.0
   sample_graph_Display.ColorArrayName = [None, '']
   sample_graph_Display.OSPRayScaleArray = 'vertexColors'
   sample_graph_Display.OSPRayScaleFunction = 'PiecewiseFunction'
   sample_graph_Display.SelectOrientationVectors = 'None'
   sample_graph_Display.ScaleFactor = 12.700000000000001
   sample_graph_Display.SelectScaleArray = 'None'
   sample_graph_Display.GlyphType = 'Arrow'
   sample_graph_Display.GlyphTableIndexArray = 'None'
   sample_graph_Display.GaussianRadius = 0.635
   sample_graph_Display.SetScaleArray = ['POINTS', 'vertexColors']
   sample_graph_Display.ScaleTransferFunction = 'PiecewiseFunction'
   sample_graph_Display.OpacityArray = ['POINTS', 'vertexColors']
   sample_graph_Display.OpacityTransferFunction = 'PiecewiseFunction'
   sample_graph_Display.DataAxesGrid = 'GridAxesRepresentation'
   sample_graph_Display.PolarAxes = 'PolarAxesRepresentation'
   # set scalar coloring
   ColorBy(sample_graph_Display, ('POINTS', 'vertexColors'))
   # rescale color and/or opacity maps used to include current data range
   sample_graph_Display.RescaleTransferFunctionToDataRange(True, False)
   # show color bar/color legend
   sample_graph_Display.SetScalarBarVisibility(view1, True)
   # get color transfer function/color map for 'vertexColors'
   vertexColorsLUT = GetColorTransferFunction('vertexColors')
   # get opacity transfer function/opacity map for 'vertexColors'
   vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
   Render()
   names = []
   for j in range(start,end):
    names.append('New\Correspondence\sample1_'+ str(j) +'.vtk')
   sample_ = LegacyVTKReader(FileNames=names)
   sample_graph_Display = Show(sample_, view1, 'GeometryRepresentation')
   sample_graph_Display.Representation = 'Points'
   sample_graph_Display.RenderPointsAsSpheres = 1
   sample_graph_Display.PointSize = 5.0
   sample_graph_Display.ColorArrayName = [None, '']
   sample_graph_Display.OSPRayScaleArray = 'vertexColors'
   sample_graph_Display.OSPRayScaleFunction = 'PiecewiseFunction'
   sample_graph_Display.SelectOrientationVectors = 'None'
   sample_graph_Display.ScaleFactor = 12.700000000000001
   sample_graph_Display.SelectScaleArray = 'None'
   sample_graph_Display.GlyphType = 'Arrow'
   sample_graph_Display.GlyphTableIndexArray = 'None'
   sample_graph_Display.GaussianRadius = 0.635
   sample_graph_Display.SetScaleArray = ['POINTS', 'vertexColors']
   sample_graph_Display.ScaleTransferFunction = 'PiecewiseFunction'
   sample_graph_Display.OpacityArray = ['POINTS', 'vertexColors']
   sample_graph_Display.OpacityTransferFunction = 'PiecewiseFunction'
   sample_graph_Display.DataAxesGrid = 'GridAxesRepresentation'
   sample_graph_Display.PolarAxes = 'PolarAxesRepresentation'
   # set scalar coloring
   ColorBy(sample_graph_Display, ('POINTS', 'vertexColors'))
   # rescale color and/or opacity maps used to include current data range
   sample_graph_Display.RescaleTransferFunctionToDataRange(True, False)
   # show color bar/color legend
   sample_graph_Display.SetScalarBarVisibility(view1, True)
   # get color transfer function/color map for 'vertexColors'
   vertexColorsLUT = GetColorTransferFunction('vertexColors')
   # get opacity transfer function/opacity map for 'vertexColors'
   vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
   Render()
   # create a new 'Group Time Steps'
   groupTimeSteps5 = GroupTimeSteps(Input=sample_)
   # show data in view
   groupTimeSteps5Display = Show(groupTimeSteps5, view1, 'GeometryRepresentation')
   # trace defaults for the display properties.
   groupTimeSteps5Display.Representation = 'Surface'
   groupTimeSteps5Display.RenderLinesAsTubes = 1
   groupTimeSteps5Display.LineWidth = 2.0
   groupTimeSteps5Display.ColorArrayName = [None, '']
   groupTimeSteps5Display.OSPRayScaleArray = 'vertexColors'
   groupTimeSteps5Display.OSPRayScaleFunction = 'PiecewiseFunction'
   groupTimeSteps5Display.SelectOrientationVectors = 'None'
   groupTimeSteps5Display.ScaleFactor = 12.700000000000001
   groupTimeSteps5Display.SelectScaleArray = 'None' 
   groupTimeSteps5Display.GlyphType = 'Arrow'
   groupTimeSteps5Display.GlyphTableIndexArray = 'None'
   groupTimeSteps5Display.GaussianRadius = 0.635
   groupTimeSteps5Display.SetScaleArray = ['POINTS', 'vertexColors']
   groupTimeSteps5Display.ScaleTransferFunction = 'PiecewiseFunction'
   groupTimeSteps5Display.OpacityArray = ['POINTS', 'vertexColors']
   groupTimeSteps5Display.OpacityTransferFunction = 'PiecewiseFunction'
   groupTimeSteps5Display.DataAxesGrid = 'GridAxesRepresentation'
   groupTimeSteps5Display.PolarAxes = 'PolarAxesRepresentation'
   # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
   groupTimeSteps5Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
   # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
   groupTimeSteps5Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
   # hide data in view
   Hide(sample_, view1)
   # update the view to ensure updated data information
   view1.Update()
   # set active source
   SetActiveSource(sample_)
   # create a new 'Group Time Steps'
   groupTimeSteps6 = GroupTimeSteps(Input=sample_)
   # show data in view
   groupTimeSteps6Display = Show(groupTimeSteps6, view1, 'GeometryRepresentation')
   # trace defaults for the display properties.
   groupTimeSteps6Display.Representation = 'Points'
   groupTimeSteps6Display.RenderPointsAsSpheres = 1
   groupTimeSteps6Display.PointSize = 5.0
   groupTimeSteps6Display.ColorArrayName = [None, '']
   groupTimeSteps6Display.OSPRayScaleArray = 'vertexColors'
   groupTimeSteps6Display.OSPRayScaleFunction = 'PiecewiseFunction'
   groupTimeSteps6Display.SelectOrientationVectors = 'None'
   groupTimeSteps6Display.ScaleFactor = 12.700000000000001
   groupTimeSteps6Display.SelectScaleArray = 'None'
   groupTimeSteps6Display.GlyphType = 'Arrow'
   groupTimeSteps6Display.GlyphTableIndexArray = 'None'
   groupTimeSteps6Display.GaussianRadius = 0.635
   groupTimeSteps6Display.SetScaleArray = ['POINTS', 'vertexColors']
   groupTimeSteps6Display.ScaleTransferFunction = 'PiecewiseFunction'
   groupTimeSteps6Display.OpacityArray = ['POINTS', 'vertexColors']
   groupTimeSteps6Display.OpacityTransferFunction = 'PiecewiseFunction'
   groupTimeSteps6Display.DataAxesGrid = 'GridAxesRepresentation'
   groupTimeSteps6Display.PolarAxes = 'PolarAxesRepresentation'
   # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
   groupTimeSteps6Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
   # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
   groupTimeSteps6Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
   break
