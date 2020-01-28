from applications.api_ppm.models import internetIP, internetInterface, PeerType, coreIP, coreInterface, ServiceType
import django
import os
import time
import datetime
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.configuration.local")

django.setup()


from_zone = tz.tzutc()
to_zone = tz.tzlocal()

def dataInternetInterface():
    inicio = datetime.datetime.utcnow().replace(tzinfo=from_zone).astimezone(to_zone)
    print("Inicio: "+time.strftime("%c"))
    devices = internetIP.objects.all().values()
    peeres = PeerType.objects.all().values()
    for device in devices:
        ip_address = device['ip']
        print(ip_address)
        fqdn = '&FQDN=Node%3D{}'
        url = 'https://aquiroga:Cl4r0peru51@172.19.212.8:4440/ppm/rest/reports/Transport+Statistics/Interface/Interface+Utilization%2FBit+Rates?outputType=jsonv2&durationSelect=lastHour&intervalTypeKey=FIVE_MINUTE&maxPageSize=200000' + fqdn
        response_data = requests.get(url.format(ip_address), verify=False).json()[
            "report"]["data"]
        for interface in response_data:
            deviceIndex = device['name'] + interface[3]

            if float(interface[8].replace(',', '')) > float(interface[7].replace(',', '')):
                gbpsmax = (float(interface[8].replace(',', '')))/1000000000
            else:
                gbpsmax = (float(interface[7].replace(',', '')))/1000000000

            if float(interface[6].replace(',', '')) > float(interface[5].replace(',', '')):
                utilization = float(interface[6].replace(',', ''))
            else:
                utilization = float(interface[5].replace(',', ''))

            if 'Eth-Trunk' in interface[0]:
                index_int = interface[0].rfind('Eth-Trunk')
                len_int = len(interface[0])
                interf = interface[0][index_int:len_int]
            elif 'Bundle-Ether' in interface[0]:
                index_int = interface[0].rfind('Bundle-Ether')
                len_int = len(interface[0])
                interf = interface[0][index_int:len_int]
            else:
                index_int = interface[0].rfind('-') + 1
                len_int = len(interface[0])
                interf = interface[0][index_int:len_int]

            for peer in peeres:
                if peer['name'] in interface[0]:
                    peerType = PeerType.objects.get(id=peer['id'])
                    break
                peerType = None

            if ('Giga' in interface[0]) or ('GE' in interface[0]) or ('Bundle' in interface[0]) or ('Trunk' in interface[0]) or ('GigE' in interface[0]):
                data = internetInterface.objects.get_or_create(
                    device=device['name'], description=interface[0], gbpsrx=(
                        float(interface[8].replace(',', '')))/1000000000,
                    gbpstx=(float(interface[7].replace(',', '')))/1000000000, utilizationrx=float(interface[6].replace(',', '')),
                    utilizationtx=float(interface[5].replace(',', '')), capacityInterface=(float(interface[4].replace(',', '')))/1000000000,
                    bpsTime=interface[1], deviceIndex=deviceIndex, gbpsmax=gbpsmax, utilization=utilization, peerType=peerType, port=interf)[0]
                data.save()
    fin = datetime.datetime.utcnow().replace(tzinfo=from_zone).astimezone(to_zone)
    transcurrido = fin - inicio
    print("Tiempo transcurrido: "+str(transcurrido))
    print("Reporte completo!!! :D")


def dataCoreInterface():
    inicio = datetime.datetime.utcnow().replace(tzinfo=from_zone).astimezone(to_zone)
    print("Inicio: "+time.strftime("%c"))
    devices = coreIP.objects.all().values()
    services = ServiceType.objects.all().values()
    print(devices)
    print(services)
    for device in devices:
        ip_address = device['ip']
        print(ip_address)
        fqdn = '&FQDN=Node%3D{}'
        url = 'https://aquiroga:Cl4r0peru51@172.19.212.8:4440/ppm/rest/reports/Transport+Statistics/Interface/Interface+Utilization%2FBit+Rates?outputType=jsonv2&durationSelect=lastHour&intervalTypeKey=FIVE_MINUTE&maxPageSize=200000' + fqdn
        response_data = requests.get(url.format(ip_address), verify=False).json()[
            "report"]["data"]
        print(response_data)
        for interface in response_data:
            deviceIndex = device['name'] + interface[3]

            if float(interface[8].replace(',', '')) > float(interface[7].replace(',', '')):
                gbpsmax = (float(interface[8].replace(',', '')))/1000000000
            else:
                gbpsmax = (float(interface[7].replace(',', '')))/1000000000

            if float(interface[6].replace(',', '')) > float(interface[5].replace(',', '')):
                utilization = float(interface[6].replace(',', ''))
            else:
                utilization = float(interface[5].replace(',', ''))

            if 'Eth-Trunk' in interface[0]:
                index_int = interface[0].rfind('Eth-Trunk')
                len_int = len(interface[0])
                interf = interface[0][index_int:len_int]
            elif 'Bundle-Ether' in interface[0]:
                index_int = interface[0].rfind('Bundle-Ether')
                len_int = len(interface[0])
                interf = interface[0][index_int:len_int]
            else:
                index_int = interface[0].rfind('-') + 1
                len_int = len(interface[0])
                interf = interface[0][index_int:len_int]

            for service in services:
                if service['name'] in interface[0]:
                    serviceType = ServiceType.objects.get(id=service['id'])
                    break
                serviceType = None

            if ('Giga' in interface[0]) or ('GE' in interface[0]) or ('Bundle' in interface[0]) or ('Trunk' in interface[0]) or ('GigE' in interface[0]):
                data = coreInterface.objects.get_or_create(
                    device=device['name'], description=interface[0], gbpsrx=(
                        float(interface[8].replace(',', '')))/1000000000,
                    gbpstx=(float(interface[7].replace(',', '')))/1000000000, utilizationrx=float(interface[6].replace(',', '')),
                    utilizationtx=float(interface[5].replace(',', '')), capacityInterface=(float(interface[4].replace(',', '')))/1000000000,
                    bpsTime=interface[1], deviceIndex=deviceIndex, gbpsmax=gbpsmax, utilization=utilization, serviceType=serviceType, port=interf)[0]
                data.save()
    fin = datetime.datetime.utcnow().replace(tzinfo=from_zone).astimezone(to_zone)
    print("Fin: "+time.strftime("%c"))
    transcurrido = fin - inicio
    print("Tiempo transcurrido: "+str(transcurrido))
    print("Reporte completo!!! :D")

