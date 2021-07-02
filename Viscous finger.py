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
tv_ = ImageReader(FileNames=['C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_1.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_2.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_3.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_4.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_5.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_6.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_7.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_8.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_9.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_10.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_11.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_12.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_13.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_14.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_15.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_16.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_17.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_18.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_19.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_20.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_21.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_22.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_23.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_24.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_25.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_26.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_27.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_28.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_29.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_30.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_31.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_32.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_33.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_34.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_35.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_36.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_37.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_38.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_39.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_40.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_41.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_42.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_43.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_44.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_45.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_46.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_47.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_48.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_49.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_50.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_51.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_52.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_53.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_54.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_55.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_56.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_57.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_58.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_59.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_60.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_61.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_62.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_63.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_64.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_65.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_66.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_67.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_68.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_69.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_70.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_71.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_72.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_73.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_74.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_75.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_76.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_77.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_78.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_79.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_80.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_81.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_82.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_83.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_84.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_85.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_86.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_87.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_88.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_89.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_90.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_91.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_92.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_93.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_94.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_95.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_96.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_97.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_98.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_99.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_100.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_101.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_102.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_103.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_104.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_105.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_106.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_107.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_108.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_109.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_110.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_111.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_112.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_113.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_114.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_115.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_116.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_117.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_118.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_119.raw', 'C:\\Users\\Toshit\\Desktop\\Project\\ViscourFingerRawData\\tv_120.raw'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on tv_
tv_.DataScalarType = 'float'
tv_.DataByteOrder = 'LittleEndian'
tv_.DataExtent = [0, 100, 0, 100, 0, 100]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1058, 524]

# get layout
layout1 = GetLayout()

# show data in view
tv_Display = Show(tv_, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tv_Display.Representation = 'Outline'
tv_Display.ColorArrayName = ['POINTS', '']
tv_Display.OSPRayScaleArray = 'ImageFile'
tv_Display.OSPRayScaleFunction = 'PiecewiseFunction'
tv_Display.SelectOrientationVectors = 'ImageFile'
tv_Display.ScaleFactor = 10.0
tv_Display.SelectScaleArray = 'ImageFile'
tv_Display.GlyphType = 'Arrow'
tv_Display.GlyphTableIndexArray = 'ImageFile'
tv_Display.GaussianRadius = 0.5
tv_Display.SetScaleArray = ['POINTS', 'ImageFile']
tv_Display.ScaleTransferFunction = 'PiecewiseFunction'
tv_Display.OpacityArray = ['POINTS', 'ImageFile']
tv_Display.OpacityTransferFunction = 'PiecewiseFunction'
tv_Display.DataAxesGrid = 'GridAxesRepresentation'
tv_Display.PolarAxes = 'PolarAxesRepresentation'
tv_Display.ScalarOpacityUnitDistance = 1.7320508075688772
tv_Display.IsosurfaceValues = [109.17794799804688]
tv_Display.SliceFunction = 'Plane'
tv_Display.Slice = 50

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tv_Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 218.35589599609375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tv_Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 218.35589599609375, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
tv_Display.SliceFunction.Origin = [50.0, 50.0, 50.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tv_Display, ('POINTS', 'ImageFile'))

# rescale color and/or opacity maps used to include current data range
tv_Display.RescaleTransferFunctionToDataRange(True, True)

# change representation type
tv_Display.SetRepresentationType('Volume')

# get color transfer function/color map for 'ImageFile'
imageFileLUT = GetColorTransferFunction('ImageFile')

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = GetOpacityTransferFunction('ImageFile')

# create a new 'Outline'
outline1 = Outline(Input=tv_)

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
sample_graph_ = LegacyVTKReader(FileNames=['C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_0.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_1.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_2.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_3.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_4.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_5.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_6.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_7.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_8.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_9.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_10.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_11.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_12.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_13.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_14.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_15.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_16.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_17.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_18.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_19.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_20.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_21.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_22.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_23.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_24.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_25.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_26.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_27.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_28.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_29.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_30.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_31.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_32.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_33.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_34.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_35.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_36.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_37.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_38.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_39.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_40.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_41.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_42.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_43.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_44.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_45.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_46.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_47.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_48.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_49.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_50.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_51.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_52.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_53.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_54.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_55.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_56.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_57.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_58.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_59.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_60.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_61.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_62.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_63.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_64.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_65.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_66.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_67.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_68.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_69.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_70.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_71.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_72.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_73.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_74.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_75.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_76.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_77.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_78.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_79.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_80.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_81.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_82.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_83.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_84.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_85.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_86.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_87.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_88.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_89.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_90.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_91.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_92.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_93.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_94.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_95.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_96.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_97.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_98.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_99.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_100.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_101.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_102.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_103.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_104.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_105.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_106.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_107.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_108.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_109.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_110.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_111.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_112.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_113.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_114.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_115.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_116.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_117.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_118.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Viscousfingerextremum\\sample_119.vtk'])

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
sample_ = LegacyVTKReader(FileNames=['C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_0.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_1.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_2.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_3.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_4.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_5.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_6.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_7.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_8.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_9.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_10.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_11.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_12.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_13.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_14.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_15.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_16.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_17.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_18.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_19.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_20.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_21.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_22.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_23.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_24.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_25.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_26.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_27.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_28.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_29.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_30.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_31.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_32.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_33.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_34.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_35.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_36.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_37.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_38.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_39.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_40.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_41.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_42.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_43.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_44.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_45.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_46.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_47.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_48.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_49.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_50.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_51.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_52.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_53.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_54.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_55.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_56.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_57.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_58.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_59.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_60.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_61.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_62.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_63.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_64.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_65.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_66.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_67.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_68.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_69.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_70.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_71.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_72.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_73.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_74.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_75.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_76.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_77.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_78.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_79.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_80.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_81.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_82.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_83.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_84.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_85.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_86.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_87.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_88.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_89.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_90.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_91.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_92.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_93.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_94.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_95.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_96.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_97.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_98.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_99.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_100.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_101.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_102.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_103.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_104.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_105.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_106.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_107.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_108.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_109.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_110.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_111.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_112.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_113.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_114.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_115.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_116.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_117.vtk', 'C:\\Users\\Toshit\\Desktop\\Project\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\ParaView-5.8.1-Windows-Python3.7-msvc2015-64bit\\bin\\Temporal\\sample1_118.vtk'])

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

# turn off scalar coloring
ColorBy(groupTimeSteps3Display, None)

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

######Add Code Here####################################################
def func():
 name='Enter the type of selection:\n1. Single maxima selection\n2. Multiple maxima selection\n3. Frame selection\n4. Longest path in whole graph\n5. Longest path starting from particular frame\n6. Fingers only\n7. Graph with missing edges'
 v1 = input(name)
 v1 = int(v1)
 if v1==1:
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
      elif(i<93):
       end = 93
      elif(i<105):
       end = 105
      else:
       end = 119
     flag = 1
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
     sample_graph_Display.SetScalarBarVisibility(renderView2, True)
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
     sample_graph_Display.SetScalarBarVisibility(renderView2, True)
     # get color transfer function/color map for 'vertexColors'
     vertexColorsLUT = GetColorTransferFunction('vertexColors')
     # get opacity transfer function/opacity map for 'vertexColors'
     vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
     Render()
     names = []
     for j in range(start,end):
      names.append('Temporal\sample1_'+ str(j) +'.vtk')
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
     Hide(sample_, renderView2)
     # update the view to ensure updated data information
     renderView2.Update()
     # set active source
     SetActiveSource(sample_)
     # create a new 'Group Time Steps'
     groupTimeSteps6 = GroupTimeSteps(Input=sample_)
     # show data in view
     groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')
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
 elif v1==2:
  file10 = open("3.csv","r")
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
   c = list(map(str, c.split('\n')))
   c = c[0]
   A = a + ' ' + b + ' ' + c
   flag = 0
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
       elif(i<93):
        end = 93
       elif(i<105):
        end = 105
       else:
        end = 119
      flag = 1
      name = 'Viscousfingerextremum\sample_' + str(i) + '.vtk'  
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
      sample_graph_Display.SetScalarBarVisibility(renderView2, True)
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
      sample_graph_Display.SetScalarBarVisibility(renderView2, True)
      # get color transfer function/color map for 'vertexColors'
      vertexColorsLUT = GetColorTransferFunction('vertexColors')
      # get opacity transfer function/opacity map for 'vertexColors'
      vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
      Render()
      for j in range(start,end):
       names.append('Temporal\sample1_'+ str(j) +'.vtk')
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
      Hide(sample_, renderView2)
      # update the view to ensure updated data information
      renderView2.Update()
      # set active source
      SetActiveSource(sample_)
      # create a new 'Group Time Steps'
      groupTimeSteps6 = GroupTimeSteps(Input=sample_)
      # show data in view
      groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')
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
      Hide(sample_, renderView2)
      # update the view to ensure updated data information
      renderView2.Update()
      break
 elif v1==3:
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
  Name = 'Temporal\sample1_'+ str(v2-2) +'.vtk'
  Name1 = 'Temporal\sample1_' + str(v2-1) + '.vtk'
  Name2 = 'Temporal\sample1_' + str(v2) + '.vtk'
  Name3 = 'Temporal\sample1_' + str(v2+1) + '.vtk' 
  Name4 = 'Temporal\sample1_' + str(v2+2) + '.vtk'
  sample_graph_ = LegacyVTKReader(FileNames=[name,name1,name2,name3,name4])
  sample_graph_Display = Show(sample_graph_, renderView2, 'GeometryRepresentation')
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
  sample_graph_ = LegacyVTKReader(FileNames=[name,name1,name2,name3,name4])
  sample_graph_Display1 = Show(sample_graph_, renderView2, 'GeometryRepresentation')
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
  for i in range(13,48):
   Name.append('Temporal\Longest\sample_'+ str(i) +'.vtk')
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
  sample_graph_Display.SetScalarBarVisibility(renderView2, True)
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
  sample_graph_Display.SetScalarBarVisibility(renderView2, True)
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
  Hide(sample_, renderView2)
  # update the view to ensure updated data information
  renderView2.Update()
  # set active source
  SetActiveSource(sample_)
  # create a new 'Group Time Steps'
  groupTimeSteps6 = GroupTimeSteps(Input=sample_)
  # show data in view
  groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')
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
  Hide(sample_, renderView2)
  # update the view to ensure updated data information
  renderView2.Update()
 elif v1 == 5:
  v2 = input("Enter the frame number:\n")
  v2 = int(v2)
  Message1 = "Error! Frame out of bound\n" 
  while((v2<0)or(v2>119)):
   Message1
   v2 = input("Enter the frame number:\n")
   v2 = int(v2)
  if(v2<30):
   start = 13
   end = 48
  elif(v2<75):
   start = 67
   end = 85
  elif(v2<100):
   start = 94
   end = 105
  elif(v2<111):
   start = 107
   end = 113
  elif(v2<118):
   start = 114
   end = 117
  else:
   start = 118
   end = 119
  Name = []
  for i in range(start,end):
   Name.append('Temporal\Longest\sample_'+ str(i) +'.vtk')
  name = 'Viscousfingerextremum/sample_' + str(start) + '.vtk'
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
  sample_graph_Display.SetScalarBarVisibility(renderView2, True)
  # get color transfer function/color map for 'vertexColors'
  vertexColorsLUT = GetColorTransferFunction('vertexColors')
  # get opacity transfer function/opacity map for 'vertexColors'
  vertexColorsPWF = GetOpacityTransferFunction('vertexColors')
  Render()
  reader = OpenDataFile(name)
  sample_graph_Display1 = Show(reader)
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
  Hide(sample_, renderView2)
  # update the view to ensure updated data information
  renderView2.Update()
  # set active source
  SetActiveSource(sample_)
  # create a new 'Group Time Steps'
  groupTimeSteps6 = GroupTimeSteps(Input=sample_)
  # show data in view
  groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')
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
  Hide(sample_, renderView2)
  # update the view to ensure updated data information
  renderView2.Update()  
 elif v1 ==6:
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
 elif v1 == 7:
  Names = []
  for i in range(119):
   Names.append('Temporal\Re\Sample_'+ str(i) +'.vtk')
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
  # create a new 'Group Time Steps'
  groupTimeSteps5 = GroupTimeSteps(Input=sample_)
  # show data in view
  groupTimeSteps5Display = Show(groupTimeSteps5, renderView2, 'GeometryRepresentation')
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
  Hide(sample_, renderView2)
  # update the view to ensure updated data information
  renderView2.Update()
  # set active source
  SetActiveSource(sample_)
  # create a new 'Group Time Steps'
  groupTimeSteps6 = GroupTimeSteps(Input=sample_)
  # show data in view
  groupTimeSteps6Display = Show(groupTimeSteps6, renderView2, 'GeometryRepresentation')
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
  Hide(sample_, renderView2)
  # update the view to ensure updated data information
  renderView2.Update()
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