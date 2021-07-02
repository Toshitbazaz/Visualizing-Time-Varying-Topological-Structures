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
file1 = open("1.csv","r")
line = file1.readline()
line = file1.readline()
file1.close()
L = list(map(str, line.split(',')))
a=L[0]
b=L[1]
c=L[2]
A = a + ' ' + b + ' ' + c
flag = 0
for i in range(49):
 if i== 48:
  break
 name1 = 'Temporal_Edges\edge_list_' + str(i+1) + '_' + str(i+2) + '.txt' 
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
   flag = 1
   M = list(map(str, line.split(')')))
   M = M[1]
   M = list(map(str, M.split(' ')))
   M = M[1]
   M = list(map(str, M.split('\n')))
   M = M[0]
   name = 'Extremum\sample_graph_' + M + '.vtp' 
   reader = OpenDataFile(name)
   sample_graph_Display = Show(reader)
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
   reader = OpenDataFile(name)
   sample_graph_Display = Show(reader)
   sample_graph_Display.Representation = 'Surface'
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
   L = list(map(str, line.split('(')))
   L = L[1]
   L = list(map(str, L.split(')')))
   L = L[0]
   L = list(map(str, L.split(',')))
   a = L[0]
   b = L[1]
   b = list(map(str, b.split(' ')))
   b = b[1]
   c = L[2]
   c = list(map(str, c.split(' ')))
   c = c[1]
   a = float(a)
   b = float(b)
   c = float(c)
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
   b1 = list(map(str, b1.split(' ')))
   b1 = b1[1]
   c1 = L[2]
   c1 = list(map(str, c1.split(' ')))
   c1 = c1[1]
   a1 = float(a1)
   b1 = float(b1)
   c1 = float(c1)
   pts = vtk.vtkPoints()
   # Create three points. Join (Origin and P0) with a red line and
   # (Origin and P1) with a green line
   p0 = [a,b,c]
   p1 = [a1,b1,c1]
   # Create a vtkPoints object and store the points in it
   pts.InsertNextPoint(p0)
   pts.InsertNextPoint(p1)
   white = [255]
   # Setup the colors array
   colors = vtk.vtkUnsignedCharArray()
   colors.SetNumberOfComponents(1)
   colors.SetName("Colors")
   if vtk.VTK_MAJOR_VERSION < 7:
    colors.InsertNextTupleValue(white)
    colors.InsertNextTupleValue(white)
   else:
    colors.InsertNextTypedTuple(white);
    colors.InsertNextTypedTuple(white);
   line0 = vtk.vtkLine()
   line0.GetPointIds().SetId(0,0) # the second 0 is the index of the Origin in the vtkPoints
   line0.GetPointIds().SetId(1,1) # the second 1 is the index of P0 in the vtkPoints
   lines = vtk.vtkCellArray()
   lines.InsertNextCell(line0)
   linesPolyData = vtk.vtkPolyData()
   # Add the points to the dataset
   linesPolyData.SetPoints(pts)
   # Add the lines to the dataset
   linesPolyData.SetLines(lines)
   # Color the lines - associate the first component (red) of the
   # colors array with the first component of the cell array (line 0)
   # and the second component (green) of the colors array with the
   # second component of the cell array (line 1)
   linesPolyData.GetCellData().SetScalars(colors)
   # Visualize
   mapper = vtk.vtkPolyDataMapper()
   if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(linesPolyData)
   else:
    mapper.SetInputData(linesPolyData)
   actor = vtk.vtkActor()
   actor.SetMapper(mapper)
   writer = vtk.vtkPolyDataWriter()
   writer.SetInputData(linesPolyData)
   savefile = 'a_' + str(i) + '.vtk'
   writer.SetFileName(savefile)
   writer.Update()
   a = a1
   b = b1
   c = c1
   for x in range(i+1,49):
    if(x==49):
     break
    name1 = 'Temporal_Edges\edge_list_' + str(x+1) + '_' + str(x+2) + '.txt' 
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
     b1 = list(map(str, b1.split(' ')))
     b1 = b1[1]
     c1 = L[2]
     c1 = list(map(str, c1.split(' ')))
     c1 = c1[1]
     a1 = float(a1)
     b1 = float(b1)
     c1 = float(c1)
     if(a==a1 and b==b1 and c==c1): 
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
      b1 = list(map(str, b1.split(' ')))
      b1 = b1[1]
      c1 = L[2]
      c1 = list(map(str, c1.split(' ')))
      c1 = c1[1]
      a1 = float(a1)
      b1 = float(b1)
      c1 = float(c1)
      pts = vtk.vtkPoints()
      # Create three points. Join (Origin and P0) with a red line and
      # (Origin and P1) with a green line
      p0 = [a,b,c]
      p1 = [a1,b1,c1]
      # Create a vtkPoints object and store the points in it
      pts.InsertNextPoint(p0)
      pts.InsertNextPoint(p1)
      white = [255]
      # Setup the colors array
      colors = vtk.vtkUnsignedCharArray()
      colors.SetNumberOfComponents(1)
      colors.SetName("Colors")
      if vtk.VTK_MAJOR_VERSION < 7:
       colors.InsertNextTupleValue(white)
       colors.InsertNextTupleValue(white)
      else:
       colors.InsertNextTypedTuple(white);
       colors.InsertNextTypedTuple(white);
      line0 = vtk.vtkLine()
      line0.GetPointIds().SetId(0,0) # the second 0 is the index of the Origin in the vtkPoints
      line0.GetPointIds().SetId(1,1) # the second 1 is the index of P0 in the vtkPoints
      lines = vtk.vtkCellArray()
      lines.InsertNextCell(line0)
      linesPolyData = vtk.vtkPolyData()
      # Add the points to the dataset
      linesPolyData.SetPoints(pts)
      # Add the lines to the dataset
      linesPolyData.SetLines(lines)
      # Color the lines - associate the first component (red) of the
      # colors array with the first component of the cell array (line 0)
      # and the second component (green) of the colors array with the
      # second component of the cell array (line 1)
      linesPolyData.GetCellData().SetScalars(colors)
      # Visualize
      mapper = vtk.vtkPolyDataMapper()
      if vtk.VTK_MAJOR_VERSION <= 5:
       mapper.SetInput(linesPolyData)
      else:
       mapper.SetInputData(linesPolyData)
      actor = vtk.vtkActor()
      actor.SetMapper(mapper)
      writer = vtk.vtkPolyDataWriter()
      writer.SetInputData(linesPolyData)
      savefile = 'a_' + str(x) + '.vtk'
      writer.SetFileName(savefile)
      writer.Update()
      a = a1
      b = b1
      c = c1
      break
   names = []
   for j in range(i,x+1):
    names.append('a_'+ str(j) +'.vtk')
   sample_ = LegacyVTKReader(FileNames=names)
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
   # trace defaults for the display properties.
   groupTimeSteps5Display.Representation = 'Surface'
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
   Hide(sample_, renderView2)
   # update the view to ensure updated data information
   renderView2.Update()
   # set scalar coloring
   ColorBy(groupTimeSteps5Display, ('FIELD', 'vtkBlockColors'))
   # show color bar/color legend
   groupTimeSteps5Display.SetScalarBarVisibility(renderView2, True)
   # get color transfer function/color map for 'vtkBlockColors'
   vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
   # get opacity transfer function/opacity map for 'vtkBlockColors'
   vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
   # set scalar coloring
   ColorBy(groupTimeSteps5Display, ('POINTS', 'vertexColors'))
   # Hide the scalar bar for this color map if no visible data is colored by it.
   HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView2)
   # rescale color and/or opacity maps used to include current data range
   groupTimeSteps5Display.RescaleTransferFunctionToDataRange(True, False)
   # show color bar/color legend
   groupTimeSteps5Display.SetScalarBarVisibility(renderView2, True)
   # get color transfer function/color map for 'vertexColors'
   vertexColorsLUT = GetColorTransferFunction('vertexColors')
   # get opacity transfer function/opacity map for 'vertexColors'
   vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
   # Properties modified on groupTimeSteps5Display
   groupTimeSteps5Display.RenderLinesAsTubes = 1
   # Properties modified on groupTimeSteps5Display
   groupTimeSteps5Display.LineWidth = 2.0
   # set active source
   SetActiveSource(sample_)
   # create a new 'Group Time Steps'
   groupTimeSteps6 = GroupTimeSteps(Input=sample_)
   # show data in view
   groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')
   # trace defaults for the display properties.
   groupTimeSteps6Display.Representation = 'Surface'
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
   Hide(sample_, renderView2)
   # update the view to ensure updated data information
   renderView2.Update()
   # set scalar coloring
   ColorBy(groupTimeSteps6Display, ('FIELD', 'vtkBlockColors'))
   # show color bar/color legend
   groupTimeSteps6Display.SetScalarBarVisibility(renderView2, True)
   # change representation type
   groupTimeSteps6Display.SetRepresentationType('Points')
   # set scalar coloring
   ColorBy(groupTimeSteps6Display, ('POINTS', 'vertexColors'))
   # Hide the scalar bar for this color map if no visible data is colored by it.
   HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView2)
   # rescale color and/or opacity maps used to include current data range
   groupTimeSteps6Display.RescaleTransferFunctionToDataRange(True, False)
   # show color bar/color legend
   groupTimeSteps6Display.SetScalarBarVisibility(renderView2, True)
   # Properties modified on groupTimeSteps6Display
   groupTimeSteps6Display.RenderPointsAsSpheres = 1
   # Properties modified on groupTimeSteps6Display
   groupTimeSteps6Display.PointSize = 5.0
   break