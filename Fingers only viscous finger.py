Names = []
for i in range(120):
 Names.append('u\sample_'+ str(i) +'.vtk')
# create a new 'Legacy VTK Reader' 
sample_ = LegacyVTKReader(FileNames=Names)
# show data in view
sample_Display = Show(sample_, renderView2, 'GeometryRepresentation')
# trace defaults for the display properties.
sample_Display.Representation = 'Surface'
sample_Display.RenderLinesAsTubes = 1
sample_Display.LineWidth = 2.0
sample_Display.ColorArrayName = [None, '']
sample_Display.OSPRayScaleArray = 'vertexColors'
sample_Display.OSPRayScaleFunction = 'PiecewiseFunction'
sample_Display.SelectOrientationVectors = 'None'
sample_Display.ScaleFactor = 12.700000000000001
sample_Display.SelectScaleArray = 'None'
sample_Display.GlyphType = 'Arrow'
sample_Display.GlyphTableIndexArray = 'None'
sample_Display.GaussianRadius = 0.635
sample_Display.SetScaleArray = ['POINTS', 'vertexColors']
sample_Display.ScaleTransferFunction = 'PiecewiseFunction'
sample_Display.OpacityArray = ['POINTS', 'vertexColors']
sample_Display.OpacityTransferFunction = 'PiecewiseFunction'
sample_Display.DataAxesGrid = 'GridAxesRepresentation'
sample_Display.PolarAxes = 'PolarAxesRepresentation'
# set scalar coloring
ColorBy(sample_Display, ('POINTS', 'vertexColors'))
# rescale color and/or opacity maps used to include current data range
sample_Display.RescaleTransferFunctionToDataRange(True, False)
# show color bar/color legend
sample_Display.SetScalarBarVisibility(renderView2, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render()
sample1_ = LegacyVTKReader(FileNames=Names)
# show data in view
sample_Display1 = Show(sample1_, renderView2, 'GeometryRepresentation')
# trace defaults for the display properties.
sample_Display1.Representation = 'Points'
sample_Display1.RenderPointsAsSpheres = 1
sample_Display1.PointSize = 5.0
sample_Display1.ColorArrayName = [None, '']
sample_Display1.OSPRayScaleArray = 'vertexColors'
sample_Display1.OSPRayScaleFunction = 'PiecewiseFunction'
sample_Display1.SelectOrientationVectors = 'None'
sample_Display1.ScaleFactor = 12.700000000000001
sample_Display1.SelectScaleArray = 'None'
sample_Display1.GlyphType = 'Arrow'
sample_Display1.GlyphTableIndexArray = 'None'
sample_Display1.GaussianRadius = 0.635
sample_Display1.SetScaleArray = ['POINTS', 'vertexColors']
sample_Display1.ScaleTransferFunction = 'PiecewiseFunction'
sample_Display1.OpacityArray = ['POINTS', 'vertexColors']
sample_Display1.OpacityTransferFunction = 'PiecewiseFunction'
sample_Display1.DataAxesGrid = 'GridAxesRepresentation'
sample_Display1.PolarAxes = 'PolarAxesRepresentation'
# set scalar coloring
ColorBy(sample_Display1, ('POINTS', 'vertexColors'))
# rescale color and/or opacity maps used to include current data range
sample_Display1.RescaleTransferFunctionToDataRange(True, False)
# show color bar/color legend
sample_Display1.SetScalarBarVisibility(renderView2, True)
# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')
# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
Render()