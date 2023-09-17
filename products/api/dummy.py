
class AllProductsAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        
        products = []

        for business in businesses:
            appliances = ApplianceFilter(data={'search': search}, queryset=Appliance.objects.all()).qs
            baby_products = BabyProductFilter(data={'search': search}, queryset=BabyProduct.objects.all()).qs
            computersandaccessories = ComputingFilter(data={'search': search}, queryset=Computing.objects.all()).qs
            fashion = FashionFilter(data={'search': search}, queryset=Fashion.objects.all()).qs
            gaming = GamingFilter(data={'search': search}, queryset=Gaming.objects.all()).qs
            groceries = GroceryFilter(data={'search': search}, queryset=Grocery.objects.all()).qs
            health_and_beauty = Health_BeautyFilter(data={'search': search}, queryset=Health_Beauty.objects.all()).qs
            home_and_office = Home_OfficeFilter(data={'search': search}, queryset=Home_Office.objects.all()).qs
            other_products = Other_ProductFilter(data={'search': search}, queryset=Other_Product.objects.all()).qs
            phone_and_tablet = Phone_TabletFilter(data={'search': search}, queryset=Phone_Tablet.objects.all()).qs
            sporting_goods = Sport_GoodingFilter(data={'search': search}, queryset=Sport_Gooding.objects.all()).qs
            tv_and_audio = Tv_AudioFilter(data={'search': search}, queryset=Tv_Audio.objects.all()).qs

            appliances_serializer = ApplianceSerializer(appliances, many=True, context={'request': request})
            baby_products_serializer = BabyProductSerializer(baby_products, many=True, context={'request': request})
            computersandaccessories_serializer = ComputingSerializer(computersandaccessories, many=True, context={'request': request})
            fashion_serializer = FashionSerializer(fashion, many=True, context={'request': request})
            gaming_serializer = GamingSerializer(gaming, many=True, context={'request': request})
            groceries_serializer = GrocerySerializer(groceries, many=True, context={'request': request})
            health_and_beauty_serializer = Health_BeautySerializer(health_and_beauty, many=True, context={'request': request})
            home_and_office_serializer = Home_OfficeSerializer(home_and_office, many=True, context={'request': request})
            other_products_serializer = Other_ProductSerializer(other_products, many=True, context={'request': request})
            phone_and_tablet_serializer = Phone_TabletSerializer(phone_and_tablet, many=True, context={'request': request})
            sporting_goods_serializer = Sport_GoodingSerializer(sporting_goods, many=True, context={'request': request})
            tv_and_audio_serializer = Tv_AudioSerializer(tv_and_audio, many=True, context={'request': request})

            products += (
                appliances_serializer.data +
                baby_products_serializer.data +
                computersandaccessories_serializer.data +
                fashion_serializer.data +
                gaming_serializer.data +
                groceries_serializer.data +
                health_and_beauty_serializer.data +
                home_and_office_serializer.data +
                other_products_serializer.data +
                phone_and_tablet_serializer.data +
                sporting_goods_serializer.data +
                tv_and_audio_serializer.data
            )

        return Response(products, status=status.HTTP_200_OK)