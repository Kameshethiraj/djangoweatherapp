from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_url = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zipcode) + "&distance=5&API_KEY=3319340B-DFF0-4D80-84B9-26FB84313FF7"

        api_request = requests.get(api_url)
        try:  
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        category_name = api[0]['Category']['Name']
        if category_name == 'Good':
            category_description = "No risk till Air quality all fine"
            category_color = "bg-success"  # Bootstrap class for green
        elif category_name == 'Moderate':
            category_description = "Air quality is Acceptable however there is some unusual"
            category_color = "bg-warning"  # Bootstrap class for yellow
        elif category_name == 'Unhealthy for Sensitive Groups':
            category_description = "Some can be affected"
            category_color = "bg-orange"  # Custom color, define in CSS
        elif category_name == 'Unhealthy':
            category_description = "Air quality is in risk. Older people and children health are in risk"
            category_color = "bg-danger"  # Bootstrap class for red
        elif category_name == 'Very Unhealthy':
            category_description = "The air quality is in bad condition. Please put mask and go outside or else it should be risky"
            category_color = "bg-purple"  # Custom color, define in CSS
        elif category_name == 'Hazardous':
            category_description = "Air quality is completely hazardous. Dont go outside. Stay at home"
            category_color = "bg-dark"  # Bootstrap class for dark
        else:
            category_description = "Unknown category"
            category_color = "bg-secondary"  # Bootstrap class for gray

         # Use a default if no zipcode is provided
    else:
        api_url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=3319340B-DFF0-4D80-84B9-26FB84313FF7"

        api_request = requests.get(api_url)
        try:  
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        category_name = api[0]['Category']['Name']
        if category_name == 'Good':
            category_description = "No risk till Air quality all fine"
            category_color = "bg-success"  # Bootstrap class for green
        elif category_name == 'Moderate':
            category_description = "Air quality is Acceptable however there is some unusual"
            category_color = "bg-warning"  # Bootstrap class for yellow
        elif category_name == 'Unhealthy for Sensitive Groups':
            category_description = "Some can be affected"
            category_color = "bg-orange"  # Custom color, define in CSS
        elif category_name == 'Unhealthy':
            category_description = "Air quality is in risk. Older people and children health are in risk"
            category_color = "bg-danger"  # Bootstrap class for red
        elif category_name == 'Very Unhealthy':
            category_description = "The air quality is in bad condition. Please put mask and go outside or else it should be risky"
            category_color = "bg-purple"  # Custom color, define in CSS
        elif category_name == 'Hazardous':
            category_description = "Air quality is completely hazardous. Dont go outside. Stay at home"
            category_color = "bg-dark"  # Bootstrap class for dark
        else:
            category_description = "Unknown category"
            category_color = "bg-secondary"  # Bootstrap class for gray

    return render(request, 'home.html', {
        'api': api,
        'category_description': category_description,
        'category_color': category_color,
        
    })

def about(request):
    return render(request, 'about.html', {})
