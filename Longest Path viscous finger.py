from paraview.simple import *
import vtk
view = GetActiveViewOrCreate('RenderView')
layout1 = GetLayout()
layout1.SplitHorizontal(0, 0.5)
view1 = CreateView('RenderView')
AssignViewToLayout(view=view1, layout=layout1, hint=2)
Name = []
for i in range(13,48):
 Name.append('New\Correspondence\sample1_'+ str(i) +'.vtk')
name = 'Viscousfingerextremum\sample_13.vtk'
reader = OpenDataFile(name)
sample_graph_Display = Show(reader)
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
sample_ = LegacyVTKReader(FileNames=Name)
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
# hide data in view
Hide(sample_, view1)
# update the view to ensure updated data information
view1.Update()
