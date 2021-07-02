# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import vtk
import time
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadPalette(paletteName='GrayBackground')

# create a new 'Image Reader'
gauss_3_D_data_Test_Path_128x128x128_ = ImageReader(FileNames=['C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_1.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_2.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_3.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_4.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_5.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_6.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_7.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_8.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_9.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_10.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_11.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_12.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_13.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_14.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_15.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_16.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_17.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_18.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_19.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_20.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_21.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_22.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_23.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_24.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_25.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_26.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_27.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_28.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_29.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_30.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_31.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_32.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_33.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_34.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_35.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_36.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_37.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_38.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_39.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_40.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_41.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_42.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_43.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_44.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_45.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_46.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_47.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_48.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_49.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\Gaussian_Data_v1\\Gauss_3_D_data_Test_Path_128x128x128_50.raw'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on gauss_3_D_data_Test_Path_128x128x128_
gauss_3_D_data_Test_Path_128x128x128_.DataScalarType = 'unsigned int'
gauss_3_D_data_Test_Path_128x128x128_.DataByteOrder = 'LittleEndian'
gauss_3_D_data_Test_Path_128x128x128_.DataExtent = [0, 127, 0, 127, 0, 127]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1058, 524]

# get layout
layout1 = GetLayout()

# show data in view
gauss_3_D_data_Test_Path_128x128x128_Display = Show(gauss_3_D_data_Test_Path_128x128x128_, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
gauss_3_D_data_Test_Path_128x128x128_Display.Representation = 'Outline'
gauss_3_D_data_Test_Path_128x128x128_Display.ColorArrayName = ['POINTS', '']
gauss_3_D_data_Test_Path_128x128x128_Display.OSPRayScaleArray = 'ImageFile'
gauss_3_D_data_Test_Path_128x128x128_Display.OSPRayScaleFunction = 'PiecewiseFunction'
gauss_3_D_data_Test_Path_128x128x128_Display.SelectOrientationVectors = 'ImageFile'
gauss_3_D_data_Test_Path_128x128x128_Display.ScaleFactor = 12.700000000000001
gauss_3_D_data_Test_Path_128x128x128_Display.SelectScaleArray = 'ImageFile'
gauss_3_D_data_Test_Path_128x128x128_Display.GlyphType = 'Arrow'
gauss_3_D_data_Test_Path_128x128x128_Display.GlyphTableIndexArray = 'ImageFile'
gauss_3_D_data_Test_Path_128x128x128_Display.GaussianRadius = 0.635
gauss_3_D_data_Test_Path_128x128x128_Display.SetScaleArray = ['POINTS', 'ImageFile']
gauss_3_D_data_Test_Path_128x128x128_Display.ScaleTransferFunction = 'PiecewiseFunction'
gauss_3_D_data_Test_Path_128x128x128_Display.OpacityArray = ['POINTS', 'ImageFile']
gauss_3_D_data_Test_Path_128x128x128_Display.OpacityTransferFunction = 'PiecewiseFunction'
gauss_3_D_data_Test_Path_128x128x128_Display.DataAxesGrid = 'GridAxesRepresentation'
gauss_3_D_data_Test_Path_128x128x128_Display.PolarAxes = 'PolarAxesRepresentation'
gauss_3_D_data_Test_Path_128x128x128_Display.ScalarOpacityUnitDistance = 1.7320508075688772
gauss_3_D_data_Test_Path_128x128x128_Display.IsosurfaceValues = [20.0]
gauss_3_D_data_Test_Path_128x128x128_Display.SliceFunction = 'Plane'
gauss_3_D_data_Test_Path_128x128x128_Display.Slice = 63

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gauss_3_D_data_Test_Path_128x128x128_Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gauss_3_D_data_Test_Path_128x128x128_Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
gauss_3_D_data_Test_Path_128x128x128_Display.SliceFunction.Origin = [63.5, 63.5, 63.5]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(gauss_3_D_data_Test_Path_128x128x128_Display, ('POINTS', 'ImageFile'))

# rescale color and/or opacity maps used to include current data range
gauss_3_D_data_Test_Path_128x128x128_Display.RescaleTransferFunctionToDataRange(True, True)

# change representation type
gauss_3_D_data_Test_Path_128x128x128_Display.SetRepresentationType('Volume')

# get color transfer function/color map for 'ImageFile'
imageFileLUT = GetColorTransferFunction('ImageFile')

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = GetOpacityTransferFunction('ImageFile')

# create a new 'Outline'
outline1 = Outline(Input=gauss_3_D_data_Test_Path_128x128x128_)

# show data in view
outline1Display = Show(outline1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
outline1Display.Representation = 'Surface'
outline1Display.ColorArrayName = [None, '']
outline1Display.OSPRayScaleFunction = 'PiecewiseFunction'
outline1Display.SelectOrientationVectors = 'None'
outline1Display.ScaleFactor = 12.700000000000001
outline1Display.SelectScaleArray = 'None'
outline1Display.GlyphType = 'Arrow'
outline1Display.GlyphTableIndexArray = 'None'
outline1Display.GaussianRadius = 0.635
outline1Display.SetScaleArray = [None, '']
outline1Display.ScaleTransferFunction = 'PiecewiseFunction'
outline1Display.OpacityArray = [None, '']
outline1Display.OpacityTransferFunction = 'PiecewiseFunction'
outline1Display.DataAxesGrid = 'GridAxesRepresentation'
outline1Display.PolarAxes = 'PolarAxesRepresentation'

# update the view to ensure updated data information
renderView1.Update()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

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

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitVertical(1, 0.33)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraFocalDisk = 1.0
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView3.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView3, layout=layout1, hint=4)

# create a new 'XML PolyData Reader'
sample_graph_ = XMLPolyDataReader(FileName=['C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_1.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_2.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_3.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_4.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_5.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_6.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_7.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_8.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_9.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_10.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_11.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_12.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_13.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_14.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_15.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_16.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_17.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_18.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_19.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_20.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_21.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_22.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_23.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_24.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_25.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_26.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_27.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_28.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_29.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_30.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_31.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_32.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_33.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_34.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_35.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_36.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_37.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_38.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_39.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_40.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_41.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_42.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_43.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_44.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_45.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_46.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_47.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_48.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_49.vtp', 'C:\\Users\\Toshit\\Desktop\\Project\\Extremum\\sample_graph_50.vtp'])
sample_graph_.PointArrayStatus = ['vertexColors']

# show data in view
sample_graph_Display = Show(sample_graph_, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
sample_graph_Display.Representation = 'Surface'
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

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sample_graph_Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sample_graph_Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView3.ResetCamera()

# update the view to ensure updated data information
renderView3.Update()

# create a new 'Group Time Steps'
groupTimeSteps1 = GroupTimeSteps(Input=sample_graph_)

# show data in view
groupTimeSteps1Display = Show(groupTimeSteps1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
groupTimeSteps1Display.Representation = 'Surface'
groupTimeSteps1Display.ColorArrayName = [None, '']
groupTimeSteps1Display.OSPRayScaleArray = 'vertexColors'
groupTimeSteps1Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupTimeSteps1Display.SelectOrientationVectors = 'None'
groupTimeSteps1Display.ScaleFactor = 12.700000000000001
groupTimeSteps1Display.SelectScaleArray = 'None'
groupTimeSteps1Display.GlyphType = 'Arrow'
groupTimeSteps1Display.GlyphTableIndexArray = 'None'
groupTimeSteps1Display.GaussianRadius = 0.635
groupTimeSteps1Display.SetScaleArray = ['POINTS', 'vertexColors']
groupTimeSteps1Display.ScaleTransferFunction = 'PiecewiseFunction'
groupTimeSteps1Display.OpacityArray = ['POINTS', 'vertexColors']
groupTimeSteps1Display.OpacityTransferFunction = 'PiecewiseFunction'
groupTimeSteps1Display.DataAxesGrid = 'GridAxesRepresentation'
groupTimeSteps1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
groupTimeSteps1Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
groupTimeSteps1Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(sample_graph_, renderView3)

# update the view to ensure updated data information
renderView3.Update()

# set scalar coloring
ColorBy(groupTimeSteps1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
groupTimeSteps1Display.SetScalarBarVisibility(renderView3, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# set scalar coloring
ColorBy(groupTimeSteps1Display, ('POINTS', 'vertexColors'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView3)

# rescale color and/or opacity maps used to include current data range
groupTimeSteps1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
groupTimeSteps1Display.SetScalarBarVisibility(renderView3, True)

# get color transfer function/color map for 'vertexColors'
vertexColorsLUT = GetColorTransferFunction('vertexColors')

# get opacity transfer function/opacity map for 'vertexColors'
vertexColorsPWF = GetOpacityTransferFunction('vertexColors')

# Properties modified on groupTimeSteps1Display
groupTimeSteps1Display.RenderLinesAsTubes = 1

# Properties modified on groupTimeSteps1Display
groupTimeSteps1Display.LineWidth = 2.0

# set active source
SetActiveSource(sample_graph_)

# create a new 'Group Time Steps'
groupTimeSteps2 = GroupTimeSteps(Input=sample_graph_)

# show data in view
groupTimeSteps2Display = Show(groupTimeSteps2, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
groupTimeSteps2Display.Representation = 'Surface'
groupTimeSteps2Display.ColorArrayName = [None, '']
groupTimeSteps2Display.OSPRayScaleArray = 'vertexColors'
groupTimeSteps2Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupTimeSteps2Display.SelectOrientationVectors = 'None'
groupTimeSteps2Display.ScaleFactor = 12.700000000000001
groupTimeSteps2Display.SelectScaleArray = 'None'
groupTimeSteps2Display.GlyphType = 'Arrow'
groupTimeSteps2Display.GlyphTableIndexArray = 'None'
groupTimeSteps2Display.GaussianRadius = 0.635
groupTimeSteps2Display.SetScaleArray = ['POINTS', 'vertexColors']
groupTimeSteps2Display.ScaleTransferFunction = 'PiecewiseFunction'
groupTimeSteps2Display.OpacityArray = ['POINTS', 'vertexColors']
groupTimeSteps2Display.OpacityTransferFunction = 'PiecewiseFunction'
groupTimeSteps2Display.DataAxesGrid = 'GridAxesRepresentation'
groupTimeSteps2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
groupTimeSteps2Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
groupTimeSteps2Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(sample_graph_, renderView3)

# update the view to ensure updated data information
renderView3.Update()

# set scalar coloring
ColorBy(groupTimeSteps2Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
groupTimeSteps2Display.SetScalarBarVisibility(renderView3, True)

# change representation type
groupTimeSteps2Display.SetRepresentationType('Points')

# set scalar coloring
ColorBy(groupTimeSteps2Display, ('POINTS', 'vertexColors'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView3)

# rescale color and/or opacity maps used to include current data range
groupTimeSteps2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
groupTimeSteps2Display.SetScalarBarVisibility(renderView3, True)

# Properties modified on groupTimeSteps2Display
groupTimeSteps2Display.RenderPointsAsSpheres = 1

# Properties modified on groupTimeSteps2Display
groupTimeSteps2Display.PointSize = 3.0

# set active source
SetActiveSource(outline1)

# show data in view
outline1Display_1 = Show(outline1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
outline1Display_1.Representation = 'Surface'
outline1Display_1.ColorArrayName = [None, '']
outline1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
outline1Display_1.SelectOrientationVectors = 'None'
outline1Display_1.ScaleFactor = 12.700000000000001
outline1Display_1.SelectScaleArray = 'None'
outline1Display_1.GlyphType = 'Arrow'
outline1Display_1.GlyphTableIndexArray = 'None'
outline1Display_1.GaussianRadius = 0.635
outline1Display_1.SetScaleArray = [None, '']
outline1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
outline1Display_1.OpacityArray = [None, '']
outline1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
outline1Display_1.DataAxesGrid = 'GridAxesRepresentation'
outline1Display_1.PolarAxes = 'PolarAxesRepresentation'

# split cell
layout1.SplitVertical(4, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraFocalDisk = 1.0
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView4.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView4, layout=layout1, hint=10)

# create a new 'Legacy VTK Reader'
sample_ = LegacyVTKReader(FileNames=['C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_1.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_2.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_3.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_4.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_5.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_6.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_7.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_8.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_9.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_10.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_11.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_12.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_13.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_14.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_15.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_16.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_17.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_18.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_19.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_20.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_21.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_22.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_23.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_24.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_25.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_26.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_27.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_28.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_29.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_30.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_31.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_32.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_33.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_34.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_35.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_36.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_37.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_38.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_39.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_40.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_41.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_42.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_43.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_44.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_45.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_46.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_47.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_48.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\Correspondence\\sample_49.vtk'])

# show data in view
sample_Display = Show(sample_, renderView4, 'GeometryRepresentation')

# get color transfer function/color map for 'Colors'
colorsLUT = GetColorTransferFunction('Colors')

# trace defaults for the display properties.
sample_Display.Representation = 'Surface'
sample_Display.ColorArrayName = ['CELLS', 'Colors']
sample_Display.LookupTable = colorsLUT
sample_Display.OSPRayScaleFunction = 'PiecewiseFunction'
sample_Display.SelectOrientationVectors = 'None'
sample_Display.ScaleFactor = 12.600000000000001
sample_Display.SelectScaleArray = 'Colors'
sample_Display.GlyphType = 'Arrow'
sample_Display.GlyphTableIndexArray = 'Colors'
sample_Display.GaussianRadius = 0.63
sample_Display.SetScaleArray = [None, '']
sample_Display.ScaleTransferFunction = 'PiecewiseFunction'
sample_Display.OpacityArray = [None, '']
sample_Display.OpacityTransferFunction = 'PiecewiseFunction'
sample_Display.DataAxesGrid = 'GridAxesRepresentation'
sample_Display.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView4.ResetCamera()

#changing interaction mode based on data extents
renderView4.InteractionMode = '2D'
renderView4.CameraPosition = [10063.5, 64.0, 63.5]
renderView4.CameraFocalPoint = [63.5, 64.0, 63.5]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]

# show color bar/color legend
sample_Display.SetScalarBarVisibility(renderView4, True)

# update the view to ensure updated data information
renderView4.Update()

# get opacity transfer function/opacity map for 'Colors'
colorsPWF = GetOpacityTransferFunction('Colors')

#change interaction mode for render view
renderView4.InteractionMode = '3D'

# hide data in view
Hide(sample_, renderView4)

# set active source
SetActiveSource(sample_)

# show data in view
sample_Display = Show(sample_, renderView4, 'GeometryRepresentation')

# show color bar/color legend
sample_Display.SetScalarBarVisibility(renderView4, True)

# reset view to fit data
renderView4.ResetCamera()

# create a new 'Group Time Steps'
groupTimeSteps3 = GroupTimeSteps(Input=sample_)

# show data in view
groupTimeSteps3Display = Show(groupTimeSteps3, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
groupTimeSteps3Display.Representation = 'Surface'
groupTimeSteps3Display.ColorArrayName = ['CELLS', 'Colors']
groupTimeSteps3Display.LookupTable = colorsLUT
groupTimeSteps3Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupTimeSteps3Display.SelectOrientationVectors = 'None'
groupTimeSteps3Display.ScaleFactor = 12.600000000000001
groupTimeSteps3Display.SelectScaleArray = 'Colors'
groupTimeSteps3Display.GlyphType = 'Arrow'
groupTimeSteps3Display.GlyphTableIndexArray = 'Colors'
groupTimeSteps3Display.GaussianRadius = 0.63
groupTimeSteps3Display.SetScaleArray = [None, '']
groupTimeSteps3Display.ScaleTransferFunction = 'PiecewiseFunction'
groupTimeSteps3Display.OpacityArray = [None, '']
groupTimeSteps3Display.OpacityTransferFunction = 'PiecewiseFunction'
groupTimeSteps3Display.DataAxesGrid = 'GridAxesRepresentation'
groupTimeSteps3Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(sample_, renderView4)

# show color bar/color legend
groupTimeSteps3Display.SetScalarBarVisibility(renderView4, True)

# update the view to ensure updated data information
renderView4.Update()

# Properties modified on groupTimeSteps3Display
groupTimeSteps3Display.RenderLinesAsTubes = 1

# Properties modified on groupTimeSteps3Display
groupTimeSteps3Display.LineWidth = 2.0

# set active source
SetActiveSource(sample_)

# create a new 'Group Time Steps'
groupTimeSteps4 = GroupTimeSteps(Input=sample_)

# show data in view
groupTimeSteps4Display = Show(groupTimeSteps4, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
groupTimeSteps4Display.Representation = 'Surface'
groupTimeSteps4Display.ColorArrayName = ['CELLS', 'Colors']
groupTimeSteps4Display.LookupTable = colorsLUT
groupTimeSteps4Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupTimeSteps4Display.SelectOrientationVectors = 'None'
groupTimeSteps4Display.ScaleFactor = 12.600000000000001
groupTimeSteps4Display.SelectScaleArray = 'Colors'
groupTimeSteps4Display.GlyphType = 'Arrow'
groupTimeSteps4Display.GlyphTableIndexArray = 'Colors'
groupTimeSteps4Display.GaussianRadius = 0.63
groupTimeSteps4Display.SetScaleArray = [None, '']
groupTimeSteps4Display.ScaleTransferFunction = 'PiecewiseFunction'
groupTimeSteps4Display.OpacityArray = [None, '']
groupTimeSteps4Display.OpacityTransferFunction = 'PiecewiseFunction'
groupTimeSteps4Display.DataAxesGrid = 'GridAxesRepresentation'
groupTimeSteps4Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(sample_, renderView4)

# show color bar/color legend
groupTimeSteps4Display.SetScalarBarVisibility(renderView4, True)

# update the view to ensure updated data information
renderView4.Update()

# change representation type
groupTimeSteps4Display.SetRepresentationType('Points')

# Properties modified on groupTimeSteps4Display
groupTimeSteps4Display.RenderPointsAsSpheres = 1

# Properties modified on groupTimeSteps4Display
groupTimeSteps4Display.PointSize = 3.0

# set active view
SetActiveView(renderView1)

# link cameras in two views
AddCameraLink(renderView1, renderView3, 'CameraLink0')

# set active view
SetActiveView(renderView3)

# set active view
SetActiveView(renderView1)

# link cameras in two views
AddCameraLink(renderView1, renderView4, 'CameraLink1')

# set active view
SetActiveView(renderView4)

# set active view
SetActiveView(renderView1)

# link cameras in two views
AddCameraLink(renderView1, renderView2, 'CameraLink2')

# set active view
SetActiveView(renderView2)


# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(outline1)

# show data in view
outline1Display = Show(outline1, renderView1, 'GeometryRepresentation')

# set active view
SetActiveView(renderView3)

# set active source
SetActiveSource(groupTimeSteps1)

# show data in view
groupTimeSteps1Display = Show(groupTimeSteps1, renderView3, 'GeometryRepresentation')

# show color bar/color legend
groupTimeSteps1Display.SetScalarBarVisibility(renderView3, True)

# reset view to fit data
renderView3.ResetCamera()

# set active source
SetActiveSource(groupTimeSteps2)

# show data in view
groupTimeSteps2Display = Show(groupTimeSteps2, renderView3, 'GeometryRepresentation')

# show color bar/color legend
groupTimeSteps2Display.SetScalarBarVisibility(renderView3, True)

# set active source
SetActiveSource(sample_)

# show data in view
sample_Display_1 = Show(sample_, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
sample_Display_1.Representation = 'Surface'
sample_Display_1.ColorArrayName = ['CELLS', 'Colors']
sample_Display_1.LookupTable = colorsLUT
sample_Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
sample_Display_1.SelectOrientationVectors = 'None'
sample_Display_1.ScaleFactor = 12.600000000000001
sample_Display_1.SelectScaleArray = 'Colors'
sample_Display_1.GlyphType = 'Arrow'
sample_Display_1.GlyphTableIndexArray = 'Colors'
sample_Display_1.GaussianRadius = 0.63
sample_Display_1.SetScaleArray = [None, '']
sample_Display_1.ScaleTransferFunction = 'PiecewiseFunction'
sample_Display_1.OpacityArray = [None, '']
sample_Display_1.OpacityTransferFunction = 'PiecewiseFunction'
sample_Display_1.DataAxesGrid = 'GridAxesRepresentation'
sample_Display_1.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
sample_Display_1.SetScalarBarVisibility(renderView3, True)

# hide data in view
Hide(sample_, renderView3)

# set active view
SetActiveView(renderView4)

# set active source
SetActiveSource(groupTimeSteps3)

# show data in view
groupTimeSteps3Display = Show(groupTimeSteps3, renderView4, 'GeometryRepresentation')

# show color bar/color legend
groupTimeSteps3Display.SetScalarBarVisibility(renderView4, True)

# reset view to fit data
renderView4.ResetCamera()

# set active source
SetActiveSource(groupTimeSteps3)

# set active source
SetActiveSource(groupTimeSteps4)

# show data in view
groupTimeSteps4Display = Show(groupTimeSteps4, renderView4, 'GeometryRepresentation')

# show color bar/color legend
groupTimeSteps4Display.SetScalarBarVisibility(renderView4, True)

# set active source
SetActiveSource(outline1)

# show data in view
outline1Display_2 = Show(outline1, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
outline1Display_2.Representation = 'Surface'
outline1Display_2.ColorArrayName = [None, '']
outline1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
outline1Display_2.SelectOrientationVectors = 'None'
outline1Display_2.ScaleFactor = 12.700000000000001
outline1Display_2.SelectScaleArray = 'None'
outline1Display_2.GlyphType = 'Arrow'
outline1Display_2.GlyphTableIndexArray = 'None'
outline1Display_2.GaussianRadius = 0.635
outline1Display_2.SetScaleArray = [None, '']
outline1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
outline1Display_2.OpacityArray = [None, '']
outline1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
outline1Display_2.DataAxesGrid = 'GridAxesRepresentation'
outline1Display_2.PolarAxes = 'PolarAxesRepresentation'

# set active view
SetActiveView(renderView3)

# show data in view
outline1Display_1 = Show(outline1, renderView3, 'GeometryRepresentation')

# set active view
SetActiveView(renderView2)

def func():
 name='Enter the type of selection:\n1. Single maxima selection\n2. Multiple maxima selection\n3. Frame selection\n4. Longest path in whole graph\n5. Longest path starting from particular frame\n6. Longest path in range of frame\n'
 v1 = input(name)
 v1 = int(v1)
 if v1==1:
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
 elif v1==2:
  file10 = open("2.csv","r")
  line = file10.readline()
  nameext = []
  count = -1
  while True:
   line = file10.readline()
   if not line:   
    file10.close()
    break
   count = count + 1
   names = []
   L = list(map(str, line.split(',')))
   a=L[0]
   b=L[1]
   c=L[2]
   A = a + ' ' + b + ' ' + c
   flag = 0
   for i in range(49):
    if i == 48:
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
      if name not in nameext:
       nameext.append(name) 
      L = list(map(str, line.split('(')))
      L = L[1]
      L = list(map(str, L.split(')')))
      L  = L[0]
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
      savefile = 'b_' + str(count) + '_' + str(i) + '.vtk'
      writer.SetFileName(savefile)
      writer.Update()
      if savefile not in names:
       names.append('b_' + str(count) + '_' + str(i) +'.vtk')
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
         savefile = 'b_' + str(count) + '_'  + str(x) + '.vtk'
         writer.SetFileName(savefile)
         writer.Update()
         if savefile not in names:
          names.append('b_' + str(count) + '_'  + str(x) +'.vtk')
         a = a1
         b = b1
         c = c1
         break   
      break
   if ((len(nameext)!=0) and (len(names)!=0)):  
    sample_graph_ = XMLPolyDataReader(FileName=nameext)
    sample_graph_.PointArrayStatus = ['vertexColors']
    # show data in view
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
    sample_graph_ = XMLPolyDataReader(FileName=nameext)
    sample_graph_.PointArrayStatus = ['vertexColors']
    # show data in view
    sample_graph_Display = Show(sample_graph_, renderView2, 'GeometryRepresentation')
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
    Render()
 elif v1==3:
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
 elif v1 == 4:
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
 elif v1 == 5:
  v1 = input("Enter the frame number:\n")
  v1 = int(v1)
  Message1 = "Error! Frame out of bound\n" 
  while((v1<=0)or(v1>49)):
   Message1
   v1 = input("Enter the frame number:\n")
   v1 = int(v1)
  Name = []
  for i in range(v1,50):
   Name.append('Correspondence/sample_'+ str(i) +'.vtk')
  name = 'Extremum/sample_graph_' +str(v1) + '.vtp'
  sample_graph_ = XMLPolyDataReader(FileName=[name])
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
  sample_graph_ = XMLPolyDataReader(FileName=[name])
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
 elif v1 == 6:
  v1 = input("Enter starting frame number:\n")
  v1 = int(v1) 
  Message1 = "Error! Frame out of bound\n"
  while((v1<=0)or(v1>49)):
   Message1
   v1 = input("Enter starting frame number:\n")
   v1 = int(v1)
  v2 = input("Enter ending frame number:\n")
  v2  = int(v2) 
  while((v2<=0)or(v2>49)):
   Message1
   v2 = input("Enter ending frame number:\n")
   v2 = int(v2)
  Message = "Error! Starting frame greater than ending frame\n"
  while(v1>v2):
   Message
   v1 = input("Enter starting frame number:\n")
   v1 = int(v1) 
   while((v1<=0)or(v1>49)):
    Message1
    v1 = input("Enter starting frame number:\n")
    v1 = int(v1)
   v2 = input("Enter ending frame number:\n")
   v2 = int(v2) 
   while((v2<=0)or(v2>49)):
    Message1
    v2 = input("Enter ending frame number:\n")
    v2 = int(v2)
  Name = []
  for i in range(v1,v2+1):
   Name.append('Correspondence/sample_'+ str(i) +'.vtk')
  name = 'Extremum/sample_graph_' +str(v1) + '.vtp'
  sample_graph_ = XMLPolyDataReader(FileName=[name])
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
  sample_graph_ = XMLPolyDataReader(FileName=[name])
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
 else:
  Message = "Error! Wrong input\n"
  Message  
  func()
 # set active source
 SetActiveSource(outline1)
 # show data in view
 outline1Display_1 = Show(outline1, renderView2, 'GeometryRepresentation')
 # trace defaults for the display properties.
 outline1Display_1.Representation = 'Surface'
 outline1Display_1.ColorArrayName = [None, '']
 outline1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
 outline1Display_1.SelectOrientationVectors = 'None'
 outline1Display_1.ScaleFactor = 12.700000000000001
 outline1Display_1.SelectScaleArray = 'None'
 outline1Display_1.GlyphType = 'Arrow'
 outline1Display_1.GlyphTableIndexArray = 'None'
 outline1Display_1.GaussianRadius = 0.635
 outline1Display_1.SetScaleArray = [None, '']
 outline1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
 outline1Display_1.OpacityArray = [None, '']
 outline1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
 outline1Display_1.DataAxesGrid = 'GridAxesRepresentation'
 outline1Display_1.PolarAxes = 'PolarAxesRepresentation'
 #time.sleep(30)
 #func()

#### saving camera placements for all active views 
# current camera placement for renderView1
renderView1.CameraPosition = [64.5, 64.0, 406.39686597059693]
renderView1.CameraFocalPoint = [64.5, 64.0, 63.5]
renderView1.CameraParallelScale = 88.74823941915693

# current camera placement for renderView2
renderView2.CameraPosition = [64.5, 64.0, 406.39686597059693]
renderView2.CameraFocalPoint = [64.5, 64.0, 63.5]
renderView2.CameraParallelScale = 88.74823941915693

# current camera placement for renderView3
renderView3.CameraPosition = [64.5, 64.0, 406.39686597059693]
renderView3.CameraFocalPoint = [64.5, 64.0, 63.5]
renderView3.CameraParallelScale = 88.74823941915693

# current camera placement for renderView4
renderView4.CameraPosition = [64.5, 64.0, 406.39686597059693]
renderView4.CameraFocalPoint = [64.5, 64.0, 63.5]
renderView4.CameraParallelScale = 88.74823941915693

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).