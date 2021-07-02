v2 = input("Enter the frame number:\n")
v2 = int(v2)
Message1 = "Error! Frame out of bound\n"
while((v2<0)or(v2>119)):
  Message1
  v2 = input("Enter the frame number:\n")
  v2 = int(v2)
if(v2<2):
 v2 = 2
elif(v2>116):
 v2 = 116
name = 'Viscousfingerextremum\sample_' + str(v2-2) + '.vtk'
name1 = 'Viscousfingerextremum\sample_' + str(v2-1) + '.vtk'
name2 = 'Viscousfingerextremum\sample_' + str(v2) + '.vtk'
name3 = 'Viscousfingerextremum\sample_' + str(v2+1) + '.vtk'
name4 = 'Viscousfingerextremum\sample_' + str(v2+2) + '.vtk'
Name = 'New\Correspondence\sample1_'+ str(v2-2) +'.vtk'
Name1 = 'New\Correspondence\sample1_' + str(v2-1) + '.vtk'
Name2 = 'New\Correspondence\sample1_' + str(v2) + '.vtk'
Name3 = 'New\Correspondence\sample1_' + str(v2+1) + '.vtk' 
Name4 = 'New\Correspondence\sample1_' + str(v2+2) + '.vtk'
sample_graph_ = LegacyVTKReader(FileNames=[name,name1,name2,name3,name4])
sample_graph_Display = Show(sample_graph_, view1, 'GeometryRepresentation')
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
sample_graph_ = LegacyVTKReader(FileNames=[name,name1,name2,name3,name4])
sample_graph_Display1 = Show(sample_graph_, view1, 'GeometryRepresentation')
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
sample_graph_Display1.SetScalarBarVisibility(view1, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render()
sample_ = LegacyVTKReader(FileNames=[Name,Name1,Name2,Name3,Name4])
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
sample_ = LegacyVTKReader(FileNames=[Name,Name1,Name2,Name3,Name4])
sample_graph_Display1 = Show(sample_, view1, 'GeometryRepresentation')
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
sample_graph_Display1.SetScalarBarVisibility(view1, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render()