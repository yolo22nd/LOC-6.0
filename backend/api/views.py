from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.

class FetchAllData(APIView):
    def post(self, request):
        csv_file_path = 'C:/Users/Parushi/Desktop/loc4/LOC-6.0/flipkart_data_2022_06_sample.csv'  # Path to your CSV file
        data = fetch_data_all(csv_file_path)
        for i in data:
            if i["images"]:
                i["images"] = i["images"].split(" | ")
        return Response({"data" : data[0-5]})


def fetch_data_all(csv_file_path, request_data):
    # Read CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    filtered_data = []
    for row in data:
        request_data['search'].lower() in row['title'].lower()
    return data


class FetchFilteredData(APIView):
    def post(self, request):
        csv_file_path = 'C:/Users/Parushi/Desktop/loc4/LOC-6.0/flipkart_data_2022_06_sample.csv'  # Path to your CSV file
        data = fetch_data_filtered(csv_file_path, request.data)
        for i in data:
            if i["images"]:
                i["images"] = i["images"].split(" | ")

        return Response({"data" : data})

#minimum maximum
def fetch_data_filtered(csv_file_path, request_data):
    # Read CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Process request data and filter data from CSV
    # filtered_data = []
        
    filtered_data1 = filter_title(data, request_data)

    try:
        if  request_data['filters']['price_min'] or request_data['filters']['price_max']:
            filtered_data2 = filter_price(filtered_data1, request_data)
            print('u')
        else:
            filtered_data2 = filtered_data1
            print('y')
    except KeyError:
        filtered_data2 = filtered_data1
    print('4')

    try:
        if  request_data['filters']['discount']:
            filtered_data3 = filter_discount(filtered_data2, request_data)
        else:
            filtered_data3 = filtered_data2
    except KeyError:
        filtered_data3 = filtered_data2
    print('5')

    try:
        if  request_data['filters']['ratings']:
            filtered_data4 = filter_ratings(filtered_data3, request_data)
        else:
            filtered_data4 = filtered_data3
    except KeyError:
        filtered_data4 = filtered_data3

    try:
        if  request_data['filters']['offers']:
            filtered_data5 = filter_offers(filtered_data4, request_data)
        else:
            filtered_data5 = filtered_data4
    except KeyError:
        filtered_data5 = filtered_data4

    try:
        if  request_data['filters']['offers']:
            filtered_data6 = filter_size(filtered_data5, request_data)
        else:
            filtered_data6 = filtered_data5
    except KeyError:
        filtered_data6 = filtered_data5

    try:
        if  request_data['filters']['offers']:
            filtered_data7 = filter_variations(filtered_data6, request_data)
        else:
            filtered_data7 = filtered_data6
    except KeyError:
        filtered_data7 = filtered_data6
    try:
        if request_data['filters']['sort_by'] and request_data['filters']['sort_order']:
            if request_data['filters']['sort_by'] == 'title':
                if request_data['filters']['sort_order'] == 'ascending':
                    filtered_data7 = sorted(filtered_data7, key=lambda x: x['title'])
                elif request_data['filters']['sort_order'] == 'descending':
                    filtered_data7 = sorted(filtered_data7, key=lambda x: x['title'], reverse=True)
            elif request_data['filters']['sort_by'] == 'price':
                if request_data['filters']['sort_order'] == 'ascending':
                    filtered_data7 = sorted(filtered_data7, key=lambda x: x['price'])
                elif request_data['filters']['sort_order'] == 'descending':
                    filtered_data7 = sorted(filtered_data7, key=lambda x: x['price'], reverse=True)
    except KeyError:
        pass

    return filtered_data7




#filter title
def filter_title(data, request_data):
    filtered_data = []
    for row in data:
        if request_data['search'].lower() in row['title'].lower():
            filtered_data.append(row.copy())
    return filtered_data


#filter price
def filter_price(data, request_data):
    filtered_data = []
    print('q')
    for row in data:
        print('w')
        if 'price_min' in request_data['filters'] and 'price_max' in request_data['filters']:
            if request_data['filters']['price_min'] <= row['price'] <= request_data['filters']['price_max']:
                print('1')
                filtered_data.append(row.copy())

        elif 'price_min' in request_data['filters']:
            if row['price'] >= request_data['filters']['price_min']:
                print('2')
                filtered_data.append(row.copy())
                
        elif 'price_max' in request_data['filters']:
            if row['price'] <= request_data['filters']['price_max']:
                print('3')
                filtered_data.append(row.copy())

    return filtered_data


#filter discount
def filter_discount(data, request_data):
    filtered_data = []
    for row in data:
        if row['discount'] == request_data['filters']['discount']:
            filtered_data.append(row.copy())
    return filtered_data


#filter ratings
def filter_ratings(data, request_data):
    filtered_data = []
    for row in data:
        if row['ratings'] >= request_data['filters']['ratings']:
            filtered_data.append(row.copy())
    return filtered_data


#filter offers
def filter_offers(data, request_data):
    filtered_data = []
    for row in data:
        if row['offers'] == request_data['filters']['offers']:
            filtered_data.append(row.copy())
    return filtered_data


#filter size
def filter_size(data, request_data):
    filtered_data = []
    for row in data:
        if row['size'] == request_data['filters']['size']:
            filtered_data.append(row.copy())
    return filtered_data


#filter cvariations
def filter_variations(data, request_data):
    filtered_data = []
    for row in data:
        if row['variations'] == request_data['filters']['variations']:
            filtered_data.append(row.copy())
    return filtered_data


class SearchView(APIView, LoginRequiredMixin):
    def post(self, request):
        data = {
            'query' : request.data.get('query'),
            'timestamp' : timezone.now()
        }
        serializer = SearchHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            return Response({'message' : 'error'})
        

class ProductComparison(APIView):
    def post(self, request):
        data = {
            'product1': request.data.get('product1'),
            'product2': request.data.get('product2'),
            'timestamp' : timezone.now()
        }

        serializer = ProductComparisonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'message' : 'error'})
        
        product1_data = self.get_product_data_from_csv(request.data.get('product1'))
        product2_data = self.get_product_data_from_csv(request.data.get('product2'))
        
        if not product1_data or not product2_data:
            return Response({'message': 'Product data not found'}, status=status.HTTP_404_NOT_FOUND)
        
        comparison_data = []
        for attribute in product1_data.keys():
            comparison_data.append([attribute, product1_data[attribute], product2_data.get(attribute)])
        
        return Response({'comparison_data': comparison_data})

    def get_product_data_from_csv(self, product_id):
        print(product_id)
        csv_file_path = 'C:/Users/Parushi/Desktop/loc4/LOC-6.0/flipkart_data_2022_06_sample.csv'
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # data = list(reader)
            for row in reader:
                print(product_id)
                # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', row)
                if int(row['index']) == product_id:
                    return row  # Return the product data as a dictionary
        return None
       


class WishlistAdd(APIView):
    authentication_classes = [] 
    permission_classes = [AllowAny]
    def post(self, request):
        user = request.user
        product_id = request.data.get('product_id')

        # Check if the product is already in the wishlist
        if Wishlist.objects.filter(user=user, product_id=int(product_id)).exists():
            return Response({'message': 'Product already in wishlist'}, status=status.HTTP_400_BAD_REQUEST)

        # Add the product to the wishlist
        Wishlist.objects.create(user=user, product_id=product_id)

        return Response({'message': 'Product added to wishlist'}, status=status.HTTP_201_CREATED)

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer