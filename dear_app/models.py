from django.db import models 
# Create your models here.
from .functions import separate
from colorfield.fields import ColorField

class Market(models.Model):
    name = models.CharField(max_length=200)
    articles = models.JSONField()
    
    def __str__(self):
        return self.name
    
def returning_message_markets(id_article,id_market):
    '''
    Esta función  recibe los parametros de id_article y id_market y regresará las llaves de los diccionarios de los 3 super_market disponibles, esto con el fin de ser usado en la función de la clase buyer declarada en la linea 150 (printing_count()), con la finalidad de que esta función de la clase buyer pueda acceder a los valores de los super_market con las llaves que le retorne esta misma función (returning_message_markets()).
    Si por ejemplo al invocar esta función se le pasasen parametros como returning_message_markets(2,3), lo que retornaría sería lo siguiente: 
    
    '''
    message = Market.objects.get(id=id_market)
    return list(message.articles.keys())[eval(id_article)-1]
    
class Product(models.Model):
    title = models.TextField(max_length=100, default='Prducto nuevo')
    price = models.FloatField(default=100)
    description = models.CharField(max_length=100,default='On sale')
    color = ColorField(null = True)
    seller = models.ForeignKey(Market,on_delete=models.CASCADE,null=True, blank=True)
    product_dimensions = models.TextField(default='[("Altura":20),("Anchura": 5),("Longitud": 8)]')
    slug = models.SlugField(db_index=True, blank = True,default='new-product')
    
    def __str__(self):
        return self.title
    
class ProductSec(models.Model):
    title = models.TextField(max_length=100, default='Prducto nuevo')
    price = models.FloatField(default=100)
    description = models.CharField(max_length=100,default='On sale')
    color = ColorField(null = True)
    product_dimensions = models.TextField(default='[("Altura":20),("Anchura": 5),("Longitud": 8)]')
    slug = models.SlugField(db_index=True, blank = True,default='new-product')
    
    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=200)
    credit_card = models.JSONField()
    tel = models.IntegerField()
    gmail = models.EmailField()
    shoping_cart = models.CharField(max_length=200)
    id_market = models.IntegerField()

    def __str__(self):
        '''
        Esta función al final lo que retornará será una lista de listas, cada una de sus listas con 2 elementos, de los cuales, cada uno 1ro tendrá el nombre del articulo,y el 2do elemento que será la cantidad de veces que se repite el articulo anterior de esa lista.
        Por ejemplo, si como parametros le pasaramos una lista como: [[1,2],[4,3]] (el shooping_cart) y un "2" (el id_market) nos tendrá que devolver lo siguiente:
        [['Pares de lentes', 4], ['Piernas de jamon', 7], ['Envases de yogurt', 5]]
        '''
        ticket_list = []
        cont = -1
        count = 0
        
        market = Market.objects.get(id=self.id_market).articles.copy()
        for article in eval(self.shoping_cart):
            if '1' == article[0]:
                count += market[returning_message_markets('1',self.id_market)]*article[1]
            elif '2' == article[0]:
                count += market[returning_message_markets('2',self.id_market)]*article[1]
            elif '3' == article[0]:
                count += market[returning_message_markets('3',self.id_market)]*article[1]
        
        def adding_ticket(id_article):
            '''
            Esta es una función anidada que esta completamente diseñada para el unico uso de esta misma función (printing_articles), la cual repite un unico proceso, que es el de tomar el parametro del id_article (que representá un indice del rango 1-3 de un articulo cualquiera de cualquier mercado) y envase a el, invocar a la función returning_message(), pero llendo al grano, el objetivo de esta función anidada será que por cada iteración que se le llame en el ciclo for de la linea 115, la lista ticket_list de la linea 96 se le agregará una nueva lista con dos elementos, el 1ro con un mensaje por parte de la función returning_message() dependiendo completamente de los parametros que tenga en ese momento, y el 2do elemento que contendrá un número determinado de veces que viene repetido el producto que indica el mensaje del primer elemento de la lista que se está agregando.
            '''
            ticket_list.append([])
            ticket_list[cont].append(returning_message_markets(id_article,self.id_market))
            ticket_list[cont].append(article[1])
            
        for article in eval(self.shoping_cart):
            cont += 1
            if '1' == article[0]:
                adding_ticket('1')
            elif '2' == article[0]:
                adding_ticket('2')
            elif '3' == article[0]:
                adding_ticket('3')
        
        return f'''El usuario se llama {self.name} 
esta sujeto a la tarjeta con la siguiente identificacion: {self.credit_card['no_card']}
Saldo del cliente: ${separate(str(self.credit_card['balance']))}
cuenta con los siguientes articulos en su carrito de compras: {ticket_list}
actualmente debe: ${count}'''