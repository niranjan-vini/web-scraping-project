import requests
import smtplib,ssl

api_key="cd41d1786233a43540c6d8173cba6452"
def get_data(place,forecast_days):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    data1=requests.get(url)
    data=data1.json()
    filter_data=data["list"]
    nr_values=8*forecast_days
    filter_data=filter_data[:nr_values]

    return filter_data


print(get_data(place="India",forecast_days=7,))


