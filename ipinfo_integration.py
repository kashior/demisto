import requests
import ipaddress

API_USED = 'http://ipinfo.io/'


# using ipaddress package, validating the IP
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        raise (Exception('Invalid IP Address(either ipv4 or ipv6)'))


# get ip as an input and returns a JSON dictionary with the details for the markdown table
def get_ip_information(ip):
    # first, validate the IP
    is_valid_ip(ip)

    # using requests package and the 'ipinfo' API, get the information about the IP provided
    r = requests.get(API_USED + ip)
    if not r.status_code == requests.codes.ok:
        r.raise_for_status()

    # turn the object into a JSON dict
    info = r.json()

    # update the longitude and latitude values seperately
    if 'loc' in info.keys():
        location = info['loc'].split(',')
        info['latitude'] = location[0]
        info['longitude'] = location[1]

    return info


# manual building of markdown, when we get as an input the json dict , parsed from the IP
def build_markdown(json_dict):
    # fill the desired variables from the input
    country = json_dict.get('country','NA')
    region = json_dict.get('region','   NA   ')
    city = json_dict.get('city','  NA  ')
    latitude = json_dict.get('latitude','  NA   ')
    longitude = json_dict.get('longitude','   NA    ')
    organization = json_dict.get('org','   NA')

    markdown = (
        "IP provided: {ip}"
        "\n"
        "         Location\n"
        "\n"
        "| Country | Region | City |\n"
        "|---------|--------|------|\n"
        "|    {country}   |{region}|{city}|\n"
        "\n"
        "         Coordinates\n\n"
        "| Latitude | Longitude |\n"
        "|----------|-----------|\n"
        "|  {latitude} | {longitude} | \n"
        "\n"
        "         Organizations\n\n"
        "    {organization}"
    ).format(ip=json_dict['ip'], country=country,
             region=region, city=city,
             latitude=latitude,
             longitude=longitude,
             organization=organization)
    return markdown


def main(ip):
    dic = get_ip_information(ip)
    res = build_markdown(dic)
    print(res)
