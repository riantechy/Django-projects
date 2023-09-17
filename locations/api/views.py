from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from locations.models import County, SubCounty, Locality
# it was not picking this  file
class LocationHierarchyAPIView(generics.GenericAPIView):
    queryset = Locality.objects.none()  # Provide a dummy queryset
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        location_hierarchy = self.create_location_hierarchy()
        return Response(location_hierarchy)

    def create_location_hierarchy(self):
        all_counties = County.objects.all()
        location_hierarchy = []

        for county in all_counties:
            county_data = {"county": county.name, "subcounties": []}

            for subcounty in SubCounty.objects.filter(county=county):
                subcounty_data = {"subcounty": subcounty.name, "localities": []}

                for locality in Locality.objects.filter(subcounty=subcounty):
                    locality_data = {"locality": locality.name}
                    subcounty_data["localities"].append(locality_data)

                county_data["subcounties"].append(subcounty_data)

            location_hierarchy.append(county_data)

        return location_hierarchy