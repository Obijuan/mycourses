import FreeCAD

print("Probando scripts en Freecad!!!")

# Obtener el documento activo
doc = App.ActiveDocument

# Anadir varios cubos
for i in range(7):

    # -- Anadir Cubo i
    doc.addObject("Part::Box", "Box{}".format(i))

    # -- Cambiar su posicion
    o = FreeCAD.ActiveDocument.getObject("Box{}".format(i))
    o.Placement.Base.x = i*10

doc.recompute()
