import Tfhka
def testF():
    impresora = Tfhka.Tfhka()
    print(impresora)
    puerto = impresora.OpenFpctrl("COM4")
    status = impresora.ReadFpStatus()
    # reporteX=impresora.GetXReport()
    # reporteX=impresora.PrintXReport()
    print(status)
    # print(reporteX)
    newStatus= impresora.SendCmd("STX-STATUS-ETX-LRC")
    print(newStatus)
    impresora.CloseFpctrl()
    return status

def cargarImpresora(PORT):
    impresora = Tfhka.Tfhka()
    impresora.OpenFpctrl(PORT)
    return impresora

def configurarPueto():
    impresora = Tfhka.Tfhka()
    puerto=0
    while puerto<=8:
        portName="COM"+str(puerto)
  
        try:
            impresora.OpenFpctrl(portName)
            status = impresora.ReadFpStatus()
            print(status)
            impresora.CloseFpctrl()
            return portName
        except Exception as e:
            print('No conecto Ojo: '+ portName) 
        puerto = puerto+ 1
    return None

def ReporteXPrint(PORT):
    impresora = cargarImpresora(PORT)
    impresora.PrintXReport()
    impresora.CloseFpctrl()
    return True
   
def datosReporteX1(PORT):
    impresora = cargarImpresora(PORT)
    datos = impresora.GetXReport()
    impresora.CloseFpctrl()
    return datos

def datosReporteX2(PORT):
    impresora = cargarImpresora(PORT)
    datos = impresora.GetX2Report()
    impresora.CloseFpctrl()
    return datos

def datosReporteX4(PORT):
    impresora = cargarImpresora(PORT)
    datos = impresora.GetX4Report()
    impresora.CloseFpctrl()
    return datos

def datosReporteX5(PORT):
    impresora = cargarImpresora(PORT)
    datos = impresora.GetX5Report()
    impresora.CloseFpctrl()
    return datos

def datosReporteX7(PORT):
    impresora = cargarImpresora(PORT)
    datos = impresora.GetX7Report()
    impresora.CloseFpctrl()
    return datos

