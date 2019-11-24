
import requests

def detect_item(image):
    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/36e94415-4dc2-4317-a56f-0cf8810fe563/LabelFile/'

    data = {'file': open(image, 'rb')}

    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('JkTsYcPBGxfIM2-rqRsUWSSgKiGcGUSZ', ''), files=data)

    return (response.text)