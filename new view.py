#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1058, 524]

# get layout
layout1 = GetLayout()

# get layout
layout1_1 = GetLayout()

# split cell
layout1_1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# get the material library
materialLibrary1 = GetMaterialLibrary()

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
AssignViewToLayout(view=renderView2, layout=layout1_1, hint=2)

#### saving camera placements for all active views

# current camera placement for renderView1

# current camera placement for renderView2

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).