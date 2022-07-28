class carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get('carro')
        if not carro:
            self.carro=self.session['carro']={}
        else:
            self.carro=carro
    
    def agregar(self,producto):
        if (str(producto.ID_producto) not in self.carro.keys()):
            self.carro[producto.ID_producto]={
                'producto_id':producto.ID_producto,
                'cantidad':1,
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.ID_producto):
                    value['cantidad']+=1
                    break
        self.guardar_carro()
    
    def restar(self,producto):
        for key, value in self.carro():
            if key==str(producto.ID_producto):
                value['cantidad']-=1
                if value['cantidad']<1:
                    self.eliminar(producto)
                self.guardar_carro

    def guardar_carro(self):
        self.session['carro']=self.carro
        self.session.modified=True
    
    def eliminar(self,producto):
        producto.ID_producto=str(producto.ID_producto)
        if producto.ID_producto in self.carro:
            del self.carro[producto.ID_producto]
            self.guardar_carro()

    def limpiar(self):
        self.carro={}