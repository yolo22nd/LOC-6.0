from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import csv


# Create your views here.

class FetchAllData(APIView):
    def get(self, request):
        csv_file_path = 'C:/Codes/Django_Codes/loc/LOC-6.0/flipkart_data_2022_06_sample.csv'  # Path to your CSV file
        data = fetch_data_all(csv_file_path)
        for i in data:
            if i["images"]:
                i["images"] = i["images"].split(" | ")
        return Response({"data" : data[0-5]})


def fetch_data_all(csv_file_path):
    # Read CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


class FetchFilteredData(APIView):
    def get(self, request):
        csv_file_path = 'C:/Codes/Django_Codes/loc/LOC-6.0/flipkart_data_2022_06_sample.csv'  # Path to your CSV file
        data = fetch_data_filtered(csv_file_path, request.data)
        for i in data:
            if i["images"]:
                i["images"] = i["images"].split(" | ")
        
        return Response({"data" : data})


def fetch_data_filtered(csv_file_path, request_data):
    # Read CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Process request data and filter data from CSV
    filtered_data = []
    for row in data:
        # Implement your logic to match request data and filter rows accordingly
        if row['category'] == request_data['category'] or row['price'] == request_data['price'] or row['discount'] == request_data['discount'] or row['title'] == request_data['title']:
            filtered_data.append(row)

    # Return filtered data
    return filtered_data