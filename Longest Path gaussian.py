# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView2.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=2)
Name = []
for i in range(1,50):
 Name.append('Correspondence/sample_'+ str(i) +'.vtk')
sample_graph_ = XMLPolyDataReader(FileName=['Extremum/sample_graph_1.vtp'])
sample_graph_.PointArrayStatus = ['vertexColors']
sample_graph_Display = Show(sample_graph_, renderView2, 'GeometryRepresentation')
sample_graph_Display.Representation = 'Points'
sample_graph_Display.RenderPointsAsSpheres = 1
sample_graph_Display.PointSize = 5.0
sample_graph_Display.Opacity = 0.6
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
sample_graph_Display.SetScalarBarVisibility(renderView2, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render()
sample_graph_ = XMLPolyDataReader(FileName=['Extremum/sample_graph_1.vtp'])
sample_graph_.PointArrayStatus = ['vertexColors']
sample_graph_Display1 = Show(sample_graph_, renderView2, 'GeometryRepresentation')
sample_graph_Display1.Representation = 'Surface'
sample_graph_Display1.RenderLinesAsTubes = 1
sample_graph_Display1.LineWidth = 2.0
sample_graph_Display1.Opacity = 0.6
sample_graph_Display1.ColorArrayName = [None, '']
sample_graph_Display1.OSPRayScaleArray = 'vertexColors'
sample_graph_Display1.OSPRayScaleFunction = 'PiecewiseFunction'
sample_graph_Display1.SelectOrientationVectors = 'None'
sample_graph_Display1.ScaleFactor = 12.700000000000001
sample_graph_Display1.SelectScaleArray = 'None'
sample_graph_Display1.GlyphType = 'Arrow'
sample_graph_Display1.GlyphTableIndexArray = 'None'
sample_graph_Display1.GaussianRadius = 0.635
sample_graph_Display1.SetScaleArray = ['POINTS', 'vertexColors']
sample_graph_Display1.ScaleTransferFunction = 'PiecewiseFunction'
sample_graph_Display1.OpacityArray = ['POINTS', 'vertexColors']
sample_graph_Display1.OpacityTransferFunction = 'PiecewiseFunction'
sample_graph_Display1.DataAxesGrid = 'GridAxesRepresentation'
sample_graph_Display1.PolarAxes = 'PolarAxesRepresentation'
# set scalar coloring
ColorBy(sample_graph_Display1, ('POINTS', 'vertexColors'))
# rescale color and/or opacity maps used to include current data range
sample_graph_Display1.RescaleTransferFunctionToDataRange(True, False)
# show color bar/color legend
sample_graph_Display1.SetScalarBarVisibility(renderView2, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render()
sample_ = LegacyVTKReader(FileNames=Name)
sample_graph_Display = Show(sample_, renderView2, 'GeometryRepresentation')
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
sample_graph_Display.SetScalarBarVisibility(renderView2, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render() 
# create a new 'Group Time Steps'
groupTimeSteps5 = GroupTimeSteps(Input=sample_)
# show data in view
groupTimeSteps5Display = Show(groupTimeSteps5, renderView2, 'GeometryRepresentation')
# get color transfer function/color map for 'Colors'
colorsLUT = GetColorTransferFunction('Colors')
# trace defaults for the display properties.
groupTimeSteps5Display.Representation = 'Surface'
groupTimeSteps5Display.ColorArrayName = ['CELLS', 'Colors']
groupTimeSteps5Display.LookupTable = colorsLUT
groupTimeSteps5Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupTimeSteps5Display.SelectOrientationVectors = 'None'
groupTimeSteps5Display.ScaleFactor = 12.600000000000001
groupTimeSteps5Display.SelectScaleArray = 'Colors'
groupTimeSteps5Display.GlyphType = 'Arrow'
groupTimeSteps5Display.GlyphTableIndexArray = 'Colors'
groupTimeSteps5Display.GaussianRadius = 0.63
groupTimeSteps5Display.SetScaleArray = [None, '']
groupTimeSteps5Display.ScaleTransferFunction = 'PiecewiseFunction'
groupTimeSteps5Display.OpacityArray = [None, '']
groupTimeSteps5Display.OpacityTransferFunction = 'PiecewiseFunction'
groupTimeSteps5Display.DataAxesGrid = 'GridAxesRepresentation'
groupTimeSteps5Display.PolarAxes = 'PolarAxesRepresentation' 
# hide data in view
Hide(sample_, renderView2) 
# show color bar/color legend
groupTimeSteps5Display.SetScalarBarVisibility(renderView2, True) 
# update the view to ensure updated data information
renderView2.Update()
# get opacity transfer function/opacity map for 'Colors'
colorsPWF = GetOpacityTransferFunction('Colors') 
# Properties modified on groupTimeSteps5Display
groupTimeSteps5Display.RenderLinesAsTubes = 1
# Properties modified on groupTimeSteps5Display
groupTimeSteps5Display.LineWidth = 2.0
# set active source
SetActiveSource(sample_)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
# create a new 'Group Time Steps'
groupTimeSteps6 = GroupTimeSteps(Input=sample_)
# show data in view
groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')   
# trace defaults for the display properties.
groupTimeSteps6Display.Representation = 'Surface'
groupTimeSteps6Display.ColorArrayName = ['CELLS', 'Colors']
groupTimeSteps6Display.LookupTable = colorsLUT
groupTimeSteps6Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupTimeSteps6Display.SelectOrientationVectors = 'None'
groupTimeSteps6Display.ScaleFactor = 12.600000000000001
groupTimeSteps6Display.SelectScaleArray = 'Colors'
groupTimeSteps6Display.GlyphType = 'Arrow'
groupTimeSteps6Display.GlyphTableIndexArray = 'Colors'
groupTimeSteps6Display.GaussianRadius = 0.63
groupTimeSteps6Display.SetScaleArray = [None, ''] 
groupTimeSteps6Display.ScaleTransferFunction = 'PiecewiseFunction'
groupTimeSteps6Display.OpacityArray = [None, '']
groupTimeSteps6Display.OpacityTransferFunction = 'PiecewiseFunction'
groupTimeSteps6Display.DataAxesGrid = 'GridAxesRepresentation'
groupTimeSteps6Display.PolarAxes = 'PolarAxesRepresentation'
# hide data in view 
Hide(sample_, renderView2)
# show color bar/color legend
groupTimeSteps6Display.SetScalarBarVisibility(renderView2, True) 
# update the view to ensure updated data information
renderView2.Update()
# change representation type
groupTimeSteps6Display.SetRepresentationType('Points')
# Properties modified on groupTimeSteps6Display
groupTimeSteps6Display.RenderPointsAsSpheres = 1
# Properties modified on groupTimeSteps6Display
groupTimeSteps6Display.PointSize = 3.0
# Properties modified on groupTimeSteps6Display
groupTimeSteps6Display.PointSize = 5.0