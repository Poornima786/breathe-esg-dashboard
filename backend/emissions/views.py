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

        return Response({
            "message": "Status updated"
        })

    except EmissionRecord.DoesNotExist:

        return Response({
            "error": "Record not found"
        })


# UPLOAD CSV
@api_view(['POST'])
def upload_csv(request):

    file = request.FILES.get('file')

    if not file:

        return Response({
            "error": "No file uploaded"
        })

    decoded_file = TextIOWrapper(
        file.file,
        encoding='utf-8'
    )

    reader = csv.DictReader(decoded_file)

    for row in reader:

        # AUTO SCOPE MAPPING
        scope_category = "SCOPE_1"

        if row['source_type'] == "UTILITY":

            scope_category = "SCOPE_2"

        elif row['source_type'] == "TRAVEL":

            scope_category = "SCOPE_3"


        # SUSPICIOUS VALUE DETECTION
        status = row['status']

        if float(row['value']) < 0:

            status = "FLAGGED"


        # DUPLICATE CHECK
        existing_record = EmissionRecord.objects.filter(
            source_type=row['source_type'],
            source_name=row['source_name'],
            value=float(row['value'])
        ).first()

        if existing_record:
            continue


        # CREATE RECORD
        EmissionRecord.objects.create(

            organization="Demo Enterprise",

            source_type=row['source_type'],

            scope_category=scope_category,

            source_name=row['source_name'],

            value=float(row['value']),

            unit=row['unit'],

            status=status,

            original_file=file.name
        )

    return Response({
        "message": "CSV uploaded successfully"
    })