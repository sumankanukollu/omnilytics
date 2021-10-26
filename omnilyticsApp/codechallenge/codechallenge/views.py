from django.shortcuts import render
from .omnilytics import Generate,Analyze_Report
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'codechallenge/home_page.html', context={'generate_process': False, 'file_name': None})


def generate(request):
    print('### You are in generate function')
    file_name = Generate().dump_generated_data()
    print('### You are in generate function is done')
    return render(request, 'codechallenge/home_page.html', context={'showLink': True, 'file_name': file_name})


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'omni_log_2.txt'
    # Define the full file path
    filepath = os.path.join(BASE_DIR, filename) # Path.cwd()/'omni_log_2.txt' 
    print(f'### File path is : {filepath}')
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def report(request):
    report = Analyze_Report().analyze()
    report['display_report'] = True
    report['showLink'] = True
    print(f'### Report is  : {report}')
    return render(request, 'codechallenge/home_page.html', context=report) #{'':report,'display_report' : True})