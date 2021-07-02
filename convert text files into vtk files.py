for i in range(119):
 name = "Edge_list_" + str(i+1) + "_" + str(i+2) + ".txt"
 Name = "Edge_list_" + str(i+1) + ".py"
 file = open(name,"r")
 file1 = open(Name,"w")
 file1.write("#!/usr/bin/env python")
 file1.write("\n")
 file1.write("import vtk")
 file1.write("\n")
 file1.write("pts = vtk.vtkPoints()")
 file1.write("\n")
 file1.write("\n")
 temp = 0
 count = -1
 while(True):
  line = file.readline()
  if not line:
   break
  count = count + 1
  L = list(map(str, line.split('(')))
  L = L[1]
  L = list(map(str, L.split(')')))
  L = L[0]
  L1 = list(map(str, L.split(',')))
  a = L1[0]
  a = float(a)
  b = L1[1]
  b = list(map(str, b.split(' ')))
  b = b[1]
  b = float(b)
  c = L1[2]
  c = list(map(str, c.split(' ')))
  c = c[1]
  c = float(c)
  if(a>15 and a<85):
   if(b>15 and b<85):
    if((a-50)**2)+((b-50)**2)<1225:
     if count%2==0:
      line = file.readline()
      if not line:
       break
      count = count + 1
      L1 = list(map(str, line.split('(')))
      L1 = L1[1]
      L1 = list(map(str, L1.split(')')))
      L1 = L1[0]
      L2 = list(map(str, L1.split(',')))
      a = L2[0]
      a = float(a)
      b = L2[1]
      b = list(map(str, b.split(' ')))
      b = b[1]
      b = float(b)
      c = L2[2]
      c = list(map(str, c.split(' ')))
      c = c[1]
      c = float(c)
      if(a>15 and a<85):
       if(b>15 and b<85):
        if((a-50)**2)+((b-50)**2)<1225:
         W = "p" + str(temp) + " = [" + L + "] "
         temp = temp + 1
         file1.write(W)
         file1.write("\n")
         W = "p" + str(temp) + " = [" + L1 + "] "
         temp = temp + 1
         file1.write(W)
         file1.write("\n")  
 file1.write("\n")
 temp1 = int((temp+1)/2)
 if temp1==0:
  W2 = "sample1_" + str(i) + ".vtk"
  file1.write("writer.SetFileName(\"" + W2 + "\")")
  file1.write("\n")
  file1.write("writer.Update()")
  file1.write("\n")
  file.close()
  file1.close()
 else:
  for j in range(temp):
   W1 = "pts.InsertNextPoint(p" + str(j) + ")"
   file1.write(W1)
   file1.write("\n")
  file1.write("\n")
  file1.write("red = [255, 0, 0]")
  file1.write("\n")
  file1.write("green = [0, 255, 0]")
  file1.write("\n")
  file1.write("\n")
  file1.write("white = [255, 255, 255]")
  file1.write("\n")
  file1.write("\n")
  file1.write("colors = vtk.vtkUnsignedCharArray()")
  file1.write("\n")
  W1 = "colors.SetNumberOfComponents(" + str(3) +")"
  file1.write(W1)
  file1.write("\n")
  file1.write("colors.SetName(\"Colors\")")
  file1.write("\n")
  file1.write("\n")
  file1.write("if vtk.VTK_MAJOR_VERSION < 7:")
  file1.write("\n")
  for j in range(temp1):
   file1.write(" colors.InsertNextTupleValue(white)")
   file1.write("\n")
  file1.write("else:")
  file1.write("\n")
  for j in range(temp1):
   file1.write(" colors.InsertNextTypedTuple(white);")
   file1.write("\n")
  file1.write("\n")
  for j in range(temp1):
   W2 = "line" + str(j) + "= vtk.vtkLine()"
   file1.write(W2)
   file1.write("\n")
   W2 = "line" + str(j) + ".GetPointIds().SetId(0," + str(2*j)+ ")"
   file1.write(W2)
   file1.write("\n")
   W2 = "line" + str(j) + ".GetPointIds().SetId(1," + str(2*j+1) + ")"
   file1.write(W2)
   file1.write("\n")
  file1.write("\n")
  file1.write("lines = vtk.vtkCellArray()")
  file1.write("\n")
  for j in range(temp1):
   W2 = "lines.InsertNextCell(line" + str(j) + ")" 
   file1.write(W2)
   file1.write("\n")
  file1.write("\n")
  file1.write("linesPolyData = vtk.vtkPolyData()")
  file1.write("\n")
  file1.write("\n")
  file1.write("linesPolyData.SetPoints(pts)")
  file1.write("\n")
  file1.write("\n")
  file1.write("linesPolyData.SetLines(lines)")
  file1.write("\n")
  file1.write("\n")
  file1.write("linesPolyData.GetCellData().SetScalars(colors)")
  file1.write("\n")
  file1.write("\n")
  file1.write("mapper = vtk.vtkPolyDataMapper()")
  file1.write("\n")
  file1.write("if vtk.VTK_MAJOR_VERSION <= 5:")
  file1.write("\n")
  file1.write(" mapper.SetInput(linesPolyData)")
  file1.write("\n")
  file1.write("else:")
  file1.write("\n")
  file1.write(" mapper.SetInputData(linesPolyData)")
  file1.write("\n")
  file1.write("\n")
  file1.write("actor = vtk.vtkActor()")
  file1.write("\n")
  file1.write("actor.SetMapper(mapper)")
  file1.write("\n")
  file1.write("\n")
  file1.write("writer = vtk.vtkPolyDataWriter()")
  file1.write("\n")
  file1.write("writer.SetInputData(linesPolyData)")
  file1.write("\n")
  W2 = "sample1_" + str(i) + ".vtk"
  file1.write("writer.SetFileName(\"" + W2 + "\")")
  file1.write("\n")
  file1.write("writer.Update()")
  file1.write("\n")
  file.close()
  file1.close() 

for i in range(119):
 Name = "Edge_list_" + str(i+1) + ".py"
 execfile(Name)
