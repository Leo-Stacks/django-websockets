import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.serializers import serialize
from .models import Product

class ProductConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'product_updates'
        self.room_group_name = f'product_updates_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        product_id = data.get('product_id')
        price = data.get('price')
        if product_id:
            product = await self.update_product(product_id, price)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'product_update',
                    'product': serialize('json', [product])[1:-1]  # Serialize the product object
                }
            )

    @sync_to_async
    def update_product(self, product_id, price):
        # Implement your product update logic here
        product = Product.objects.get(id=product_id)
        product.price = price
        product.save()
        return product

    async def product_update(self, event):
        product_data = event['product']
        await self.send(text_data=product_data)
