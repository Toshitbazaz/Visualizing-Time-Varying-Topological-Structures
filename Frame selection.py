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
v1 = input("Enter the frame number:\n")
v1 = int(v1)
Message1 = "Error! Frame out of bound\n"
while((v1<0)or(v1>49)):
  Message1
  v1 = input("Enter the frame number:\n")
  v1 = int(v1)
if v1<=3:
 v1 = 3
elif v1>=47:
 v1 = 47
name = 'Extremum/sample_graph_' + str(v1-2) + '.vtp'
name1 = 'Extremum/sample_graph_' + str(v1-1) + '.vtp'
name2 = 'Extremum/sample_graph_' + str(v1) + '.vtp'
name3 = 'Extremum/sample_graph_' + str(v1+1) + '.vtp'
name4 = 'Extremum/sample_graph_' + str(v1+2) + '.vtp'
Name = 'Correspondence/sample_'+ str(v1-2) +'.vtk'
Name1 = 'Correspondence/sample_' + str(v1-1) + '.vtk'
Name2 = 'Correspondence/sample_' + str(v1) + '.vtk'
Name3 = 'Correspondence/sample_' + str(v1+1) + '.vtk'
Name4 = 'Correspondence/sample_' + str(v1+2) + '.vtk' 
sample_graph_ = XMLPolyDataReader(FileName=[name,name1,name2,name3,name4])
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
sample_graph_ = XMLPolyDataReader(FileName=[name,name1,name2,name3,name4])
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
sample_ = LegacyVTKReader(FileNames=[Name,Name1,Name2,Name3,Name4])
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
sample_ = LegacyVTKReader(FileNames=[Name,Name1,Name2,Name3,Name4])
sample_graph_Display1 = Show(sample_, renderView2, 'GeometryRepresentation')
sample_graph_Display1.Representation = 'Surface'
sample_graph_Display1.RenderLinesAsTubes = 1
sample_graph_Display1.LineWidth = 2.0
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