from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmissionRecord
from .serializers import EmissionRecordSerializer

import csv
from io import TextIOWrapper


# GET ALL RECORDS
@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all().order_by('-id')

    serializer = EmissionRecordSerializer(records, many=True)

    return Response(serializer.data)


# UPDATE STATUS
@api_view(['POST'])
def update_status(request, pk):

    try:
        record = EmissionRecord.objects.get(id=pk)

        status = request.data.get('status')

        record.status = status

        record.save()

        return Response({"message": "Status updated"})

    except EmissionRecord.DoesNotExist:

        return Response({"error": "Record not found"})


# UPLOAD CSV
@api_view(['POST'])
def upload_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file uploaded"})

    decoded_file = TextIOWrapper(file.file, encoding='utf-8')

    reader = csv.DictReader(decoded_file)

    for row in reader:

        EmissionRecord.objects.create(

            source_type=row['source_type'],

            source_name=row['source_name'],

            value=float(row['value']),

            unit=row['unit'],

            status=row['status'],

            original_file=file.name
        )

    return Response({"message": "CSV uploaded successfully"})