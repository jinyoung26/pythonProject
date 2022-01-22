# my_info = {'name':'paul', 'phone':'01012345678', 'birth':'0714'}
#
# print(my_info)
# print(my_info['name'])
# print(my_info.get('name'))

my_station = ['야탑','모란','이매','선릉','한티','왕십리']

def station_list(station_list):
    for station in my_station:
        print(station)

station_list(my_station)

def station_point(station_point):
    for station in my_station:
        if station == '선릉':
            print(station)

station_point(my_station)