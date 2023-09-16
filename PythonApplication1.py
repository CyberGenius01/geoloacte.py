import requests

def get_ip():
	response = requests.get('https://api64.ipify.org?format=json').json()
	return response["ip"]

def get_location():
	ip_addr = get_ip()
	response = requests.get(f'https://ipapi.co/{ip_addr}/json/').json()

	location_data = {
		"ip": ip_addr,
		"city": response.get("city"),
		"region": response.get("region"),
		"country": response.get("country_name"),
		"postal": response.get("postal")
	}
	return location_data

print(get_location())

