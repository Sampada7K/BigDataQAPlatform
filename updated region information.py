from model import RegionData

regions= [{'Stations': [{'Lat': 38.0012, 'StationCode': 'sfbccwq', 'Lon': -122.4604, 'StationName': 'China Camp'}], 'RegionId': 1, 'RegionName': 'San Francisco Bay, CA'}, {'Stations': [{'Lat': 36.8179, 'StationCode': 'elksmwq', 'Lon': -121.7394, 'StationName': 'Soth March'}, {'Lat': 36.8457, 'StationCode': 'elkapwq', 'Lon': -121.7538, 'StationName': 'Azevedo Pond'}, {'Lat': 36.8111, 'StationCode': 'elkvmwq', 'Lon': -121.7792, 'StationName': 'Vierra Moth'}, {'Lat': 36.8346, 'StationCode': 'elknmwq', 'Lon': -121.7384, 'StationName': 'North Marsh'}], 'RegionId': 2, 'RegionName': 'Elkhorn Slogh, CA'}, {'Stations': [{'Lat': 32.5595, 'StationCode': 'tjrbrwq', 'Lon': -117.1288, 'StationName': 'Boca Rio'}, {'Lat': 32.59612, 'StationCode': 'tjrprwq', 'Lon': -117.11822, 'StationName': 'Pond Eleven Restored'}, {'Lat': 32.600136, 'StationCode': 'tjrsbwq', 'Lon': -117.115692, 'StationName': 'Soth Bay'}, {'Lat': 32.56829, 'StationCode': 'tjroswq', 'Lon': -117.13127, 'StationName': 'Oneonta Slogh'}], 'RegionId': 3, 'RegionName': 'Tijana River, CA'}, {'Stations': [{'Lat': 43.296501, 'StationCode': 'sosecwq', 'Lon': -124.310729, 'StationName': 'Elliot Creek'}, {'Lat': 43.3377, 'StationCode': 'soschwq', 'Lon': -124.320533, 'StationName': 'Charleston Bridge'}, {'Lat': 43.27615, 'StationCode': 'soswiwq', 'Lon': -124.3197528, 'StationName': 'Winchester Arm'}, {'Lat': 43.317217, 'StationCode': 'sosvawq', 'Lon': -124.321633, 'StationName': 'Valino Island'}], 'RegionId': 4, 'RegionName': 'Soth Slogh, OR'}, {'Stations': [{'Lat': 48.496139, 'StationCode': 'pdbbywq', 'Lon': -122.502114, 'StationName': 'Bayview Channel'}, {'Lat': 48.556322, 'StationCode': 'pdbbpwq', 'Lon': -122.530894, 'StationName': 'Ploeg Channel'}, {'Lat': 48.518264, 'StationCode': 'pdbjewq', 'Lon': -122.474189, 'StationName': 'Joe Leary Estary'}], 'RegionId': 5, 'RegionName': 'Padilla Bay, WA'}, {'Stations': [{'Lat': 59.44099, 'StationCode': 'kacsdwq', 'Lon': -151.72096, 'StationName': 'Seldovia Deep'}, {'Lat': 59.60201, 'StationCode': 'kachdwq', 'Lon': -151.40878, 'StationName': 'Homer Dolphin Deep'}, {'Lat': 59.44099, 'StationCode': 'kacsswq', 'Lon': -151.72096, 'StationName': 'Seldovia Surface'}, {'Lat': 59.60205, 'StationCode': 'kach3wq', 'Lon': -151.40942, 'StationName': 'Homer Surface 3'}], 'RegionId': 6, 'RegionName': 'Kachemak Bay, Alaska'}, {'Stations': [{'Lat': 27.9798, 'StationCode': 'marabwq', 'Lon': -97.0287, 'StationName': 'Aransas Bay'}, {'Lat': 28.1323, 'StationCode': 'marcewq', 'Lon': -97.0344, 'StationName': 'Copano bay East'}, {'Lat': 27.83811, 'StationCode': 'marscwq', 'Lon': -97.05022, 'StationName': 'Ship Channel'}, {'Lat': 28.1384, 'StationCode': 'marmbwq', 'Lon': -96.8285, 'StationName': 'Mesquite Bay'}, {'Lat': 28.0841, 'StationCode': 'marcwwq', 'Lon': -97.2009, 'StationName': 'Copano Bay West'}], 'RegionId': 7, 'RegionName': 'Mission Aransas, TX'}, {'Stations': [{'Lat': 46.721772, 'StationCode': 'lksbawq', 'Lon': -92.06352, 'StationName': "Barker's Island"}, {'Lat': 46.65685, 'StationCode': 'lksolwq', 'Lon': -92.20166, 'StationName': 'Oliver Bridge'}], 'RegionId': 8, 'RegionName': 'Lake Superior, WI'}, {'Stations': [{'Lat': 41.3825, 'StationCode': 'owcwmwq', 'Lon': -82.515, 'StationName': 'State Route 6'}, {'Lat': 41.3819, 'StationCode': 'owcolwq', 'Lon': -82.5142, 'StationName': 'Lower Estuary'}, {'Lat': 41.3483, 'StationCode': 'owcbrwq', 'Lon': -82.5083, 'StationName': 'Berlin Road'}, {'Lat': 41.364978, 'StationCode': 'owcdrwq', 'Lon': -82.504739, 'StationName': 'Darrow Road'}], 'RegionId': 9, 'RegionName': 'Old Woman Creek, OH'}, {'Stations': [{'Lat': 17.930317, 'StationCode': 'job20wq', 'Lon': -66.211472, 'StationName': 'Station 20'}, {'Lat': 17.942914, 'StationCode': 'job19wq', 'Lon': -66.228825, 'StationName': 'Station 19'}, {'Lat': 17.938611, 'StationCode': 'job10wq', 'Lon': -66.257736, 'StationName': 'Station 10'}, {'Lat': 17.943022, 'StationCode': 'job09wq', 'Lon': -66.238511, 'StationName': 'Station 9'}], 'RegionId': 10, 'RegionName': 'Jobos Bay, Puerto Rico'}, {'Stations': [{'Lat': 30.3571, 'StationCode': 'gndblwq', 'Lon': -88.4629, 'StationName': 'Bangs Lake'}, {'Lat': 30.4178, 'StationCode': 'gndbhwq', 'Lon': -88.4054, 'StationName': 'Bayou Heron'}, {'Lat': 30.3836, 'StationCode': 'gndbcwq', 'Lon': -88.4364, 'StationName': 'Bayou Cumbest'}, {'Lat': 30.3486, 'StationCode': 'gndpcwq', 'Lon': -88.4185, 'StationName': 'Point Aux Chenes Bay'}], 'RegionId': 11, 'RegionName': 'Grand Bay, MS'}, {'Stations': [{'Lat': 30.4162, 'StationCode': 'wkbfrwq', 'Lon': -87.8228, 'StationName': 'Fish River'}, {'Lat': 30.3961, 'StationCode': 'wkbmbwq', 'Lon': -87.8335, 'StationName': 'Middle Bay'}, {'Lat': 30.39, 'StationCode': 'wkbmrwq', 'Lon': -87.8177, 'StationName': 'Magnolia River'}, {'Lat': 30.3808, 'StationCode': 'wkbwbwq', 'Lon': -87.832, 'StationName': 'Weeks Bay'}], 'RegionId': 12, 'RegionName': 'Weeks Bay, AL'}, {'Stations': [{'Lat': 29.7858, 'StationCode': 'apaebwq', 'Lon': -84.8752, 'StationName': 'East Bay Bottom'}, {'Lat': 29.6747, 'StationCode': 'apadbwq', 'Lon': -85.0583, 'StationName': 'Dry Bar'}, {'Lat': 29.7021, 'StationCode': 'apacpwq', 'Lon': -84.8802, 'StationName': 'Cat Point'}, {'Lat': 29.7858, 'StationCode': 'apaeswq', 'Lon': -84.8752, 'StationName': 'East Bay Surface'}], 'RegionId': 13, 'RegionName': 'Apalachicola, FL'}, {'Stations': [{'Lat': 26.0257, 'StationCode': 'rkblhwq', 'Lon': -81.7332, 'StationName': 'Lower Henderson Creek'}, {'Lat': 25.9343, 'StationCode': 'rkbmbwq', 'Lon': -81.5946, 'StationName': 'Middle Blackwater River'}, {'Lat': 25.9005, 'StationCode': 'rkbfuwq', 'Lon': -81.5159, 'StationName': 'Faka Union Bay'}, {'Lat': 25.8922, 'StationCode': 'rkbfbwq', 'Lon': -81.477, 'StationName': 'Faka Hatchee Bay'}], 'RegionId': 14, 'RegionName': 'Rookery Bay, FL'}, {'Stations': [{'Lat': 29.667071, 'StationCode': 'gtmpcwq', 'Lon': -81.257403, 'StationName': 'Pellicer Creek'}, {'Lat': 30.050857, 'StationCode': 'gtmpiwq', 'Lon': -81.367465, 'StationName': 'Pine Island'}, {'Lat': 29.737041, 'StationCode': 'gtmfmwq', 'Lon': -81.245953, 'StationName': 'Fort Matanzas'}, {'Lat': 29.868851, 'StationCode': 'gtmsswq', 'Lon': -81.307428, 'StationName': 'San Sebastian'}], 'RegionId': 15, 'RegionName': 'Guana Tolomato Matanzas, FL'}, {'Stations': [{'Lat': 31.4786, 'StationCode': 'saphdwq', 'Lon': -81.2731, 'StationName': 'Hunt Dock'}, {'Lat': 31.417942, 'StationCode': 'sapldwq', 'Lon': -81.296047, 'StationName': 'Lower Duplin'}, {'Lat': 31.4437, 'StationCode': 'sapcawq', 'Lon': -81.2399, 'StationName': 'Cabretta Creek'}, {'Lat': 31.3896, 'StationCode': 'sapdcwq', 'Lon': -81.2789, 'StationName': 'Dean Creek'}], 'RegionId': 16, 'RegionName': 'Sapelo Island, GA'}, {'Stations': [{'Lat': 32.5279, 'StationCode': 'acespwq', 'Lon': -80.3615, 'StationName': 'St. Pierre'}, {'Lat': 32.5558, 'StationCode': 'acemcwq', 'Lon': -80.438, 'StationName': 'Mosquito Creek'}, {'Lat': 32.6358, 'StationCode': 'acefcwq', 'Lon': -80.3655, 'StationName': 'Fishing Creek'}], 'RegionId': 17, 'RegionName': 'ACE Basin, SC'}, {'Stations': [{'Lat': 33.3493511, 'StationCode': 'niwolwq', 'Lon': -79.1888819, 'StationName': 'Oyster Landing'}, {'Lat': 33.3601486, 'StationCode': 'niwdcwq', 'Lon': -79.1674572, 'StationName': 'Debidue Creek'}, {'Lat': 33.3338636, 'StationCode': 'niwcbwq', 'Lon': -79.1930411, 'StationName': 'Clambank'}, {'Lat': 33.2991461, 'StationCode': 'niwtawq', 'Lon': -79.2560564, 'StationName': 'Thousand Acre'}], 'RegionId': 18, 'RegionName': 'North Inlet Winyah Bay, SC'}, {'Stations': [{'Lat': 34.156, 'StationCode': 'nocrcwq', 'Lon': -77.8499, 'StationName': 'Research Creek'}, {'Lat': 33.9547, 'StationCode': 'noczbwq', 'Lon': -77.935, 'StationName': "Zeke's Basin"}, {'Lat': 34.1722, 'StationCode': 'noclcwq', 'Lon': -77.8328, 'StationName': 'Loosin Creek'}, {'Lat': 33.9399, 'StationCode': 'nocecwq', 'Lon': -77.9411, 'StationName': 'East Cribbing'}], 'RegionId': 19, 'RegionName': 'North Carolina, NC'}, {'Stations': [{'Lat': 37.57138, 'StationCode': 'cbvshwq', 'Lon': -76.88424, 'StationName': 'Sweethall'}, {'Lat': 37.215796, 'StationCode': 'cbvgiwq', 'Lon': -76.392675, 'StationName': 'Goodwin Island'}, {'Lat': 37.346665, 'StationCode': 'cbvcbwq', 'Lon': -76.611263, 'StationName': 'Claybank'}, {'Lat': 37.414986, 'StationCode': 'cbvtcwq', 'Lon': -76.71442, 'StationName': 'Taskinas Creek'}], 'RegionId': 20, 'RegionName': 'Chesapeake Bay, VA'}, {'Stations': [{'Lat': 39.4507, 'StationCode': 'cbmocwq', 'Lon': -76.2746, 'StationName': 'Otter Point Creek'}, {'Lat': 38.7813, 'StationCode': 'cbmrrwq', 'Lon': -76.7137, 'StationName': 'Railroad'}, {'Lat': 38.7433, 'StationCode': 'cbmmcwq', 'Lon': -76.7074, 'StationName': 'Mataponi Creek'}, {'Lat': 38.796, 'StationCode': 'cbmipwq', 'Lon': -76.7208, 'StationName': 'Iron Pot Landing'}], 'RegionId': 21, 'RegionName': 'Chesapeake Bay, MD'}, {'Stations': [{'Lat': 39.08498, 'StationCode': 'delslwq', 'Lon': -75.46058, 'StationName': 'Scotton Landing'}, {'Lat': 39.1637, 'StationCode': 'deldswq', 'Lon': -75.5191, 'StationName': 'Division Street'}, {'Lat': 39.38876, 'StationCode': 'delblwq', 'Lon': -75.636, 'StationName': 'Blackbird Landing'}, {'Lat': 39.1144, 'StationCode': 'delllwq', 'Lon': -75.4992, 'StationName': 'Lebanon Landing'}], 'RegionId': 22, 'RegionName': 'Delaware, DE'}, {'Stations': [{'Lat': 39.5479, 'StationCode': 'jacnewq', 'Lon': -74.4608, 'StationName': 'Chestnut Neck'}, {'Lat': 39.5079, 'StationCode': 'jacb6wq', 'Lon': -74.3385, 'StationName': 'Buoy 126'}, {'Lat': 39.5937, 'StationCode': 'jacbawq', 'Lon': -74.5515, 'StationName': 'Lower Bank'}], 'RegionId': 23, 'RegionName': 'Jacques Cousteau, NJ'}, {'Stations': [{'Lat': 42.0365457, 'StationCode': 'hudtnwq', 'Lon': -73.925324, 'StationName': 'Tivoli North Bay'}, {'Lat': 42.0171722, 'StationCode': 'hudskwq', 'Lon': -73.9149611, 'StationName': 'Saw Kill'}, {'Lat': 42.0463, 'StationCode': 'hudscwq', 'Lon': -73.9108, 'StationName': 'Stony Creek'}, {'Lat': 42.0270378, 'StationCode': 'hudtswq', 'Lon': -73.9259569, 'StationName': 'Tivoli South Bay'}], 'RegionId': 24, 'RegionName': 'Hudson River, NY'}, {'Stations': [{'Lat': 41.578361, 'StationCode': 'nartbwq', 'Lon': -71.321125, 'StationName': 'T-Wharf Bottom'}, {'Lat': 41.578361, 'StationCode': 'nartswq', 'Lon': -71.321125, 'StationName': 'T-Wharf Surface'}, {'Lat': 41.62485, 'StationCode': 'narncwq', 'Lon': -71.324283, 'StationName': 'Nag Creek'}, {'Lat': 41.64055, 'StationCode': 'narpcwq', 'Lon': -71.340881, 'StationName': 'Potters Cove'}], 'RegionId': 25, 'RegionName': 'Narragansett Bay, RI'}, {'Stations': [{'Lat': 41.5526, 'StationCode': 'wqbmhwq', 'Lon': -70.5485, 'StationName': 'Menauhant'}, {'Lat': 41.5798, 'StationCode': 'wqbcrwq', 'Lon': -70.5309, 'StationName': 'Childs River'}, {'Lat': 41.5689, 'StationCode': 'wqbmpwq', 'Lon': -70.5216, 'StationName': 'Metoxit Point'}, {'Lat': 41.5542, 'StationCode': 'wqbslwq', 'Lon': -70.5102, 'StationName': 'Sage Lot'}], 'RegionId': 26, 'RegionName': 'Wquoit Bay, MA'}, {'Stations': [{'Lat': 43.134, 'StationCode': 'grborwq', 'Lon': -70.911, 'StationName': 'Oyster River'}, {'Lat': 43.08, 'StationCode': 'grblrwq', 'Lon': -70.9344, 'StationName': 'Lamprey River'}, {'Lat': 43.0921, 'StationCode': 'grbgbwq', 'Lon': -70.8642, 'StationName': 'Great Bay'}, {'Lat': 43.052403, 'StationCode': 'grbsqwq', 'Lon': -70.911811, 'StationName': 'Squamscott River'}], 'RegionId': 27, 'RegionName': 'Great Bay, NH'}, {'Stations': [{'Lat': 43.320089, 'StationCode': 'welinwq', 'Lon': -70.563442, 'StationName': 'Inlet'}, {'Lat': 43.344711, 'StationCode': 'welsmwq', 'Lon': -70.549217, 'StationName': 'Skinner Mill'}, {'Lat': 43.298347, 'StationCode': 'welhtwq', 'Lon': -70.587094, 'StationName': 'Head of Tide'}, {'Lat': 43.340153, 'StationCode': 'wellmwq', 'Lon': -70.540603, 'StationName': 'Little River Mout'}], 'RegionId': 28, 'RegionName': 'Wells, ME'}]


obj = RegionData()
obj.insertRegionInfoIntoDB(regions)