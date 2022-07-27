class carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get('carro')
        if not carro:
            carro=self.session['carro']={}
        else:
            self.carro=carro
    
    def agregar(self,producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                'producto_id':producto.id,
                'nombre':producto.nombre_producto,
                'precio':producto.precio_unitario,
                'cantidad':1,
                'imagen':producto.imagen.url,
                
            }