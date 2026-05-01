Weather Forcast https://open-meteo.com/en/docs#api_documentation
The API endpoint /v1/forecast accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days. Time always starts at 0:00 today and contains 168 hours. If &forecast_days=16 is set, up to 16 days of forecast can be returned. All URL parameters are listed below:

Parameter	Format	Required	Default	Description
latitude, longitude	Floating point	Yes		Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location_id. For North and South America locations use negative longitudes, because they lie west of Greenwich.
elevation	Floating point	No		The elevation used for statistical downscaling. Per default, a 90 meter digital elevation model is used. You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated.
hourly	String array	No		A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used.
daily	String array	No		A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required.
current	String array	No		A list of weather variables to get current conditions.
temperature_unit	String	No	celsius	If fahrenheit is set, all temperature values are converted to Fahrenheit.
wind_speed_unit	String	No	kmh	Other wind speed speed units: ms, mph and kn
precipitation_unit	String	No	mm	Other precipitation amount units: inch
timeformat	String	No	iso8601	If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc_offset_seconds again to get the correct date.
timezone	String	No	GMT	If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the time zone database is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.
past_days	Integer (0-92)	No	0	If past_days is set, yesterday or the day before yesterday data are also returned.
forecast_days	Integer (0-16)	No	7	Per default, only 7 days are returned. Up to 16 days of forecast are possible.
forecast_hours
forecast_minutely_15
past_hours
past_minutely_15	Integer (>0)	No		Similar to forecast_days, the number of timesteps of hourly and 15-minutely data can controlled. Instead of using the current day as a reference, the current hour or the current 15-minute time-step is used.
start_date
end_date	String (yyyy-mm-dd)	No		The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-06-30).
start_hour
end_hour
start_minutely_15
end_minutely_15	String (yyyy-mm-ddThh:mm)	No		The time interval to get weather data for hourly or 15 minutely data. Time must be specified as an ISO8601 date (e.g. 2022-06-30T12:00).
models	String array	No	auto	Manually select one or more weather models. Per default, the best suitable weather models will be combined.
cell_selection	String	No	land	Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with similar elevation to the requested coordinates using a 90-meter digital elevation model. sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.
apikey	String	No		Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See pricing for more information.
Additional optional URL parameters will be added. For API stability, no required parameters will be added in the future!

Hourly Parameter Definition
The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as an average or sum.

Variable	Valid time	Unit	Description
temperature_2m	Instant	°C (°F)	Air temperature at 2 meters above ground
relative_humidity_2m	Instant	%	Relative humidity at 2 meters above ground
dew_point_2m	Instant	°C (°F)	Dew point temperature at 2 meters above ground
apparent_temperature	Instant	°C (°F)	Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation
pressure_msl
surface_pressure	Instant	hPa	Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.
cloud_cover	Instant	%	Total cloud cover as an area fraction
cloud_cover_low	Instant	%	Low level clouds and fog up to 3 km altitude
cloud_cover_mid	Instant	%	Mid level clouds from 3 to 8 km altitude
cloud_cover_high	Instant	%	High level clouds from 8 km altitude
wind_speed_10m
wind_speed_80m
wind_speed_120m
wind_speed_180m	Instant	km/h (mph, m/s, knots)	Wind speed at 10, 80, 120 or 180 meters above ground. Wind speed on 10 meters is the standard level.
wind_direction_10m
wind_direction_80m
wind_direction_120m
wind_direction_180m	Instant	°	Wind direction at 10, 80, 120 or 180 meters above ground
wind_gusts_10m	Preceding hour max	km/h (mph, m/s, knots)	Gusts at 10 meters above ground as a maximum of the preceding hour
shortwave_radiation	Preceding hour mean	W/m²	Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation
direct_radiation
direct_normal_irradiance	Preceding hour mean	W/m²	Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun)
diffuse_radiation	Preceding hour mean	W/m²	Diffuse solar radiation as average of the preceding hour
global_tilted_irradiance	Preceding hour mean	W/m²	Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west, ±180 north). If azimuth is set to "nan", the calculation assumes a vertical tracker (east-west). If tilt is set to "nan", it is assumed that the panel has a horizontal tracker (up-down). If both are set to "nan", a bi-axial tracker is assumed.
vapour_pressure_deficit	Instant	kPa	Vapour Pressure Deficit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases
cape	Instant	J/kg	Convective available potential energy. See Wikipedia.
evapotranspiration	Preceding hour sum	mm (inch)	Evapotranspration from land surface and plants that weather models assumes for this location. Available soil water is considered. 1 mm evapotranspiration per hour equals 1 liter of water per spare meter.
et0_fao_evapotranspiration	Preceding hour sum	mm (inch)	ET₀ Reference Evapotranspiration of a well watered grass field. Based on FAO-56 Penman-Monteith equations ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.
precipitation	Preceding hour sum	mm (inch)	Total precipitation (rain, showers, snow) sum of the preceding hour
snowfall	Preceding hour sum	cm (inch)	Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent
precipitation_probability	Preceding hour probability	%	Probability of precipitation with more than 0.1 mm of the preceding hour. Probability is based on ensemble weather models with 0.25° (~27 km) resolution. 30 different simulations are computed to better represent future weather conditions.
rain	Preceding hour sum	mm (inch)	Rain from large scale weather systems of the preceding hour in millimeter
showers	Preceding hour sum	mm (inch)	Showers from convective precipitation in millimeters from the preceding hour
weather_code	Instant	WMO code	Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details.
snow_depth	Instant	meters	Snow depth on the ground
freezing_level_height	Instant	meters	Altitude above sea level of the 0°C level
visibility	Instant	meters	Viewing distance in meters. Influenced by low clouds, humidity and aerosols.
soil_temperature_0cm
soil_temperature_6cm
soil_temperature_18cm
soil_temperature_54cm	Instant	°C (°F)	Temperature in the soil at 0, 6, 18 and 54 cm depths. 0 cm is the surface temperature on land or water surface temperature on water.
soil_moisture_0_to_1cm
soil_moisture_1_to_3cm
soil_moisture_3_to_9cm
soil_moisture_9_to_27cm
soil_moisture_27_to_81cm	Instant	m³/m³	Average soil water content as volumetric mixing ratio at 0-1, 1-3, 3-9, 9-27 and 27-81 cm depths.
is_day	Instant	Dimensionless	1 if the current time step has daylight, 0 at night.
15-Minutely Parameter Definition
The parameter &minutely_15= can be used to get 15-minutely data. This data is based on NOAA HRRR model for North America and DWD ICON-D2 and Météo-France AROME model for Central Europe. If 15-minutely data is requested for other regions data is interpolated from 1-hourly to 15-minutely.

15-minutely data can be requested for other weather variables that are available for hourly data, but will use interpolation.

Variable	Valid time	Unit	HRRR	ICON-D2	AROME
temperature_2m	Instant	°C (°F)	x		x
relative_humidity_2m	Instant	%	x		x
dew_point_2m	Instant	°C (°F)	x		x
apparent_temperature	Instant	°C (°F)	x		x
shortwave_radiation	Preceding 15 minutes mean	W/m²	x	x	
direct_radiation
direct_normal_irradiance	Preceding 15 minutes mean	W/m²	x	x	
global_tilted_irradiance
global_tilted_irradiance_instant	Preceding 15 minutes mean	W/m²	x	x	
diffuse_radiation	Preceding 15 minutes mean	W/m²	x	x	
sunshine_duration	Preceding 15 minutes sum	seconds	x	x	
lightning_potential	Instant	J/kg		x	
precipitation	Preceding 15 minutes sum	mm (inch)	x	x	x
snowfall	Preceding 15 minutes sum	cm (inch)	x	x	x
rain	Preceding 15 minutes sum	mm (inch)	x	x	x
showers	Preceding 15 minutes sum	mm (inch)		x	
snowfall_height	Instant	meters		x	
freezing_level_height	Instant	meters		x	
cape	Instant	J/kg	x	x	x
wind_speed_10m
wind_speed_80m	Instant	km/h (mph, m/s, knots)	x		x
wind_direction_10m
wind_direction_80m
Instant	°	x		x
wind_gusts_10m	Preceding 15 min max	km/h (mph, m/s, knots)	x		
visibility	Instant	meters	x		x
weather_code	Instant	WMO code	x	x	
Pressure Level Variables
Pressure level variables do not have fixed altitudes. Altitude varies with atmospheric pressure. 1000 hPa is roughly between 60 and 160 meters above sea level. Estimated altitudes are given below. Altitudes are in meters above sea level (not above ground). For precise altitudes, geopotential_height can be used.

Level (hPa)	1000	975	950	925	900	850	800	700	600	500	400	300	250	200	150	100	70	50	30
Altitude	110 m	320 m	500 m	800 m	1000 m	1500 m	1900 m	3 km	4.2 km	5.6 km	7.2 km	9.2 km	10.4 km	11.8 km	13.5 km	15.8 km	17.7 km	19.3 km	22 km
All pressure levels have valid times of the indicated hour (instant).

Variable	Unit	Description
temperature_1000hPa
temperature_975hPa, ...	°C (°F)	Air temperature at the specified pressure level. Air temperatures decrease linearly with pressure.
relative_humidity_1000hPa
relative_humidity_975hPa, ...	%	Relative humidity at the specified pressure level.
dew_point_1000hPa
dew_point_975hPa, ...	°C (°F)	Dew point temperature at the specified pressure level.
cloud_cover_1000hPa
cloud_cover_975hPa, ...	%	Cloud cover at the specified pressure level. Cloud cover is approximated based on relative humidity using Sundqvist et al. (1989). It may not match perfectly with low, mid and high cloud cover variables.
wind_speed_1000hPa
wind_speed_975hPa, ...	km/h (mph, m/s, knots)	Wind speed at the specified pressure level.
wind_direction_1000hPa
wind_direction_975hPa, ...	°	Wind direction at the specified pressure level.
geopotential_height_1000hPa
geopotential_height_975hPa, ...	meter	Geopotential height at the specified pressure level. This can be used to get the correct altitude in meter above sea level of each pressure level. Be carefull not to mistake it with altitude above ground.
Daily Parameter Definition
Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

Variable	Unit	Description
temperature_2m_max
temperature_2m_mean
temperature_2m_min	°C (°F)	Maximum and minimum daily air temperature at 2 meters above ground
apparent_temperature_max
apparent_temperature_mean
apparent_temperature_min	°C (°F)	Maximum and minimum daily apparent temperature
precipitation_sum	mm	Sum of daily precipitation (including rain, showers and snowfall)
rain_sum	mm	Sum of daily rain
showers_sum	mm	Sum of daily showers
snowfall_sum	cm	Sum of daily snowfall
precipitation_hours	hours	The number of hours with rain
precipitation_probability_max
precipitation_probability_mean
precipitation_probability_min	%	Probability of precipitation
weather_code	WMO code	The most severe weather condition on a given day
sunrise
sunset	iso8601	Sun rise and set times
sunshine_duration	seconds	The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk.
daylight_duration	seconds	Number of seconds of daylight per day
wind_speed_10m_max
wind_gusts_10m_max	km/h (mph, m/s, knots)	Maximum wind speed and gusts on a day
wind_direction_10m_dominant	°	Dominant wind direction
shortwave_radiation_sum	MJ/m²	The sum of solar radiation on a given day in Megajoules
et0_fao_evapotranspiration	mm	Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field
uv_index_max
uv_index_clear_sky_max	Index	Daily maximum in UV Index starting from 0. uv_index_clear_sky_max assumes cloud free conditions. Please follow the official WMO guidelines for ultraviolet index.
JSON Return Object
On success a JSON object will be returned.

{
    "latitude": 52.52,
    "longitude": 13.419,
    "elevation": 44.812,
    "generationtime_ms": 2.2119,
    "utc_offset_seconds": 0,
    "timezone": "Europe/Berlin",
    "timezone_abbreviation": "CEST",
    "hourly": {
        "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
        "temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...]
    },
    "hourly_units": {
        "temperature_2m": "°C"
    }
}
Parameter	Format	Description
latitude, longitude	Floating point	WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometres away from the requested coordinate.
elevation	Floating point	The elevation from a 90 meter digital elevation model. This effects which grid-cell is selected (see parameter cell_selection). Statistical downscaling is used to adapt weather conditions for this elevation. This elevation can also be controlled with the query parameter elevation. If &elevation=nan is specified, all downscaling is disabled and the averge grid-cell elevation is used.
generationtime_ms	Floating point	Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements.
utc_offset_seconds	Integer	Applied timezone offset from the &timezone= parameter.
timezone
timezone_abbreviation	String	Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST)
current	Object	For every chosen current weather variable, the data is provided as a numeric value. In addition, time specifies the moment at which the data is valid. The interval represents the duration in seconds used for calculating backward-looking sums or averages. For instance, an interval of 900 seconds (15 minutes) means that aggregated metrics such as precipitation reflect the total from the previous 15 minutes.
hourly	Object	For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.
hourly_units	Object	For each selected weather variable, the unit will be listed here.
daily	Object	For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.
daily_units	Object	For each selected daily weather variable, the unit will be listed here.
Errors
In case an error occurs, for example a URL parameter is not correctly specified, a JSON error object is returned with a HTTP 400 status code.

{
    "error": true, 
    "reason": "Cannot initialize WeatherVariable from invalid String value
	    tempeture_2m for key hourly" 
}
Weather variable documentation
WMO Weather interpretation codes (WW)
Code	Description
0	Clear sky
1, 2, 3	Mainly clear, partly cloudy, and overcast
45, 48	Fog and depositing rime fog
51, 53, 55	Drizzle: Light, moderate, and dense intensity
56, 57	Freezing Drizzle: Light and dense intensity
61, 63, 65	Rain: Slight, moderate and heavy intensity
66, 67	Freezing Rain: Light and heavy intensity
71, 73, 75	Snow fall: Slight, moderate, and heavy intensity
77	Snow grains
80, 81, 82	Rain showers: Slight, moderate, and violent
85, 86	Snow showers slight and heavy
95 *	Thunderstorm: Slight or moderate
96, 99 *	Thunderstorm with slight and heavy hail
(*) Thunderstorm forecast with hail is only available in Central Europe



https://open-meteo.com/en/docs/historical-weather-api#api_documentation|
The API endpoint /v1/archive allows users to retrieve historical weather data for a specific location and time period. To use this endpoint, you can specify a geographical coordinate, a time interval, and a list of weather variables that they are interested in. The endpoint will then return the requested data in a format that can be easily accessed and used by applications or other software. This endpoint can be very useful for researchers and other users who need to access detailed historical weather data for specific locations and time periods.

All URL parameters are listed below:

Additional optional URL parameters will be added. For API stability, no required parameters will be added in the future.
Parameter	Format	Required	Default	Description
latitude
longitude	Floating point	Yes		Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location_id.
elevation	Floating point	No		The elevation used for statistical downscaling. Per default, a 90 meter digital elevation model is used. You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated.
start_date
end_date	String (yyyy-mm-dd)	Yes		The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-12-31).
hourly	String array	No		A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used.
daily	String array	No		A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required.
temperature_unit	String	No	celsius	If fahrenheit is set, all temperature values are converted to Fahrenheit.
wind_speed_unit	String	No	kmh	Other wind speed speed units: ms, mph and kn
precipitation_unit	String	No	mm	Other precipitation amount units: inch
timeformat	String	No	iso8601	If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date.
timezone	String	No	GMT	If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the time zone database is supported If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.
cell_selection	String	No	land	Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with similar elevation to the requested coordinates using a 90-meter digital elevation model. sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.
apikey	String	No		Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See pricing for more information.
Hourly Parameter Definition
The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as and average or sum.

Variable	Valid time	Unit	Description
temperature_2m	Instant	°C (°F)	Air temperature at 2 meters above ground
relative_humidity_2m	Instant	%	Relative humidity at 2 meters above ground
dew_point_2m	Instant	°C (°F)	Dew point temperature at 2 meters above ground
apparent_temperature	Instant	°C (°F)	Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation
pressure_msl
surface_pressure	Instant	hPa	Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.
precipitation	Preceding hour sum	mm (inch)	Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision. If precipitation data is summed up to monthly sums, there might be small inconsistencies with the total precipitation amount.
rain	Preceding hour sum	mm (inch)	Only liquid precipitation of the preceding hour including local showers and rain from large scale systems.
snowfall	Preceding hour sum	cm (inch)	Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent
cloud_cover	Instant	%	Total cloud cover as an area fraction
cloud_cover_low	Instant	%	Low level clouds and fog up to 2 km altitude
cloud_cover_mid	Instant	%	Mid level clouds from 2 to 6 km altitude
cloud_cover_high	Instant	%	High level clouds from 6 km altitude
shortwave_radiation	Preceding hour mean	W/m²	Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation
direct_radiation
direct_normal_irradiance	Preceding hour mean	W/m²	Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun)
diffuse_radiation	Preceding hour mean	W/m²	Diffuse solar radiation as average of the preceding hour
global_tilted_irradiance	Preceding hour mean	W/m²	Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west, ±180 north). If azimuth is set to "nan", the calculation assumes a vertical tracker (east-west). If tilt is set to "nan", it is assumed that the panel has a horizontal tracker (up-down). If both are set to "nan", a bi-axial tracker is assumed.
sunshine_duration	Preceding hour sum	Seconds	Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition.
wind_speed_10m
wind_speed_100m	Instant	km/h (mph, m/s, knots)	Wind speed at 10 or 100 meters above ground. Wind speed on 10 meters is the standard level.
wind_direction_10m
wind_direction_100m	Instant	°	Wind direction at 10 or 100 meters above ground
wind_gusts_10m	Instant	km/h (mph, m/s, knots)	Gusts at 10 meters above ground of the indicated hour. Wind gusts in CERRA are defined as the maximum wind gusts of the preceding hour. Please consult the ECMWF IFS documentation for more information on how wind gusts are parameterized in weather models.
et0_fao_evapotranspiration	Preceding hour sum	mm (inch)	ET₀ Reference Evapotranspiration of a well watered grass field. Based on FAO-56 Penman-Monteith equations ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.
weather_code	Instant	WMO code	Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. Weather code is calculated from cloud cover analysis, precipitation and snowfall. As barely no information about atmospheric stability is available, estimation about thunderstorms is not possible.
snow_depth	Instant	meters	Snow depth on the ground. Snow depth in ERA5-Land tends to be overestimated. As the spatial resolution for snow depth is limited, please use it with care.
vapour_pressure_deficit	Instant	kPa	Vapor Pressure Deificit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases
soil_temperature_0_to_7cm
soil_temperature_7_to_28cm
soil_temperature_28_to_100cm
soil_temperature_100_to_255cm	Instant	°C (°F)	Average temperature of different soil levels below ground.
soil_moisture_0_to_7cm
soil_moisture_7_to_28cm
soil_moisture_28_to_100cm
soil_moisture_100_to_255cm	Instant	m³/m³	Average soil water content as volumetric mixing ratio at 0-7, 7-28, 28-100 and 100-255 cm depths.
Daily Parameter Definition
Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

Variable	Unit	Description
weather_code	WMO code	The most severe weather condition on a given day
temperature_2m_max
temperature_2m_min	°C (°F)	Maximum and minimum daily air temperature at 2 meters above ground
apparent_temperature_max
apparent_temperature_min	°C (°F)	Maximum and minimum daily apparent temperature
precipitation_sum	mm	Sum of daily precipitation (including rain, showers and snowfall)
rain_sum	mm	Sum of daily rain
snowfall_sum	cm	Sum of daily snowfall
precipitation_hours	hours	The number of hours with rain
sunrise
sunset	iso8601	Sun rise and set times
sunshine_duration	seconds	The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk.
daylight_duration	seconds	Number of seconds of daylight per day
wind_speed_10m_max
wind_gusts_10m_max	km/h (mph, m/s, knots)	Maximum wind speed and gusts on a day
wind_direction_10m_dominant	°	Dominant wind direction
shortwave_radiation_sum	MJ/m²	The sum of solar radiaion on a given day in Megajoules
et0_fao_evapotranspiration	mm	Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field
JSON Return Object
On success a JSON object will be returned.

{
    "latitude": 52.52,
    "longitude": 13.419,
    "elevation": 44.812,
    "generationtime_ms": 2.2119,
    "utc_offset_seconds": 0,
    "timezone": "Europe/Berlin",
    "timezone_abbreviation": "CEST",
    "hourly": {
        "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
        "temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...]
    },
    "hourly_units": {
        "temperature_2m": "°C"
    }
}
Parameter	Format	Description
latitude, longitude	Floating point	WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometres away from the requested coordinate.
elevation	Floating point	The elevation from a 90 meter digital elevation model. This effects which grid-cell is selected (see parameter cell_selection). Statistical downscaling is used to adapt weather conditions for this elevation. This elevation can also be controlled with the query parameter elevation. If &elevation=nan is specified, all downscaling is disabled and the averge grid-cell elevation is used.
generationtime_ms	Floating point	Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements.
utc_offset_seconds	Integer	Applied timezone offset from the &timezone= parameter.
timezone
timezone_abbreviation	String	Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST)
hourly	Object	For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.
hourly_units	Object	For each selected weather variable, the unit will be listed here.
daily	Object	For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.
daily_units	Object	For each selected daily weather variable, the unit will be listed here.
Errors
In case an error occurs, for example a URL parameter is not correctly specified, a JSON error object is returned with a HTTP 400 status code.

{
    "error": true, 
    "reason": "Cannot initialize WeatherVariable from invalid String value
	    tempeture_2m for key hourly" 
}



Data Sources https://open-meteo.com/en/docs/historical-forecast-api#data_sources
The weather data precisely aligns with the weather forecast API, created by continuously integrating weather forecast model data. Each update from the weather models' initial hours is compiled into a seamless time series. This extensive dataset is ideal for training machine learning models and combining them with forecast data to generate optimised predictions.

Weather models are initialized using data from weather stations, satellites, radar, airplanes, soundings, and buoys. With high update frequencies of 1, 3, or 6 hours, the resulting time series is nearly as accurate as direct measurements and offers global coverage. In regions like North America and Central Europe, the difference from local weather stations is minimal. However, for precise values such as precipitation, local measurements are preferable when available.

The Historical Forecast API archives comprehensive data, including atmospheric pressure levels, from all accessible weather forecast models. Depending on the model and public archive availability, data is available starting from 2021 or 2022.

The default Best Match option selects the most suitable high-resolution weather models for any global location, though users can also manually specify the weather model. Open-Meteo utilises the following weather forecast models:

National Weather Provider	Weather Model	Region	Spatial Resolution	Temporal Resolution	Update Frequency	Available Since
Deutscher Wetterdienst (DWD)	ICON	Global	0.1° (~11 km)	Hourly	Every 6 hours	2022-11-24
ICON-EU	Europe	0.0625° (~7 km)	Hourly	Every 3 hours	2022-11-24
ICON-D2	Central Europe	0.02° (~2 km)	Hourly	Every 3 hours	2022-11-24
NOAA NCEP	GFS	Global	0.11° (~13 km)	Hourly	Every 6 hours	2021-03-23
GFS Pressure Variables	Global	0.25° (~25 km)	Hourly	Every 6 hours	2021-03-23
HRRR	U.S. Conus	3 km	Hourly	Every hour	2018-01-01
NAM	U.S. Conus	3 km	Hourly	Every 6 hours	2025-09-01
NBM	U.S. Conus	3 km	Hourly	Every hour	2024-10-08
GFS GraphCast	Global	0.25° (~25 km)	6-Hourly	Every 6 hours	2024-02-05
AIGFS	Global	0.25° (~25 km)	6-Hourly	Every 6 hours	2026-01-07
HGEFS	Global	0.25° (~25 km)	6-Hourly	Every 6 hours	2026-01-07
Météo-France	ARPEGE World	Global	0.25° (~25 km)	Hourly	Every 6 hours	2024-01-02
ARPEGE Europe	Europe	0.1° (~11 km)	Hourly	Every 6 hours	2022-11-13
AROME France	France	0.025° (~2.5 km)	Hourly	Every 3 hours	2024-01-02
AROME France HD	France	0.01° (~1.5 km)	Hourly	Every 3 hours	2022-11-13
ECMWF	IFS 0.4°	Global	0.4° (~44 km)	3-Hourly	Every 6 hours	2022-11-07
IFS 0.25°	Global	0.25° (~25 km)	3-Hourly	Every 6 hours	2024-02-03
AIFS 0.25° Single	Global	0.25° (~25 km)	6-Hourly	Every 6 hours	2025-02-20
IFS HRES	Global	9 km (O1280 grid)	Hourly	Every 6 hours	2017-01-01
UK Met Office	UKMO Global	Global	0.09° (~10 km)	Hourly	Every 6 hours	2022-03-01
UKMO UKV	UK and Ireland	2 km	Hourly	Every hour	2022-03-01
JMA	GSM	Global	0.5° (~55 km)	6-Hourly	Every 6 hours	2016-01-01
MSM	Japan	0.05° (~5 km)	Hourly	Every 3 hours	2016-01-01
MET Norway	MET Nordic	Norway, Denmark, Sweden, Finland	1 km	Hourly	Every hour	2022-11-15
Canadian Weather Service	GEM Global	Global	0.15° (~15 km)	3-Hourly	Every 12 hours	2022-11-23
GEM Regional	North America, North Pole	10 km	Hourly	Every 6 hours	2022-11-23
HRDPS Continental	Canada, Nothern US	2.5 km	Hourly	Every 6 hours	2023-03-03
China Meteorological Administration (CMA)	GFS GRAPES	Global	0.125° (~15 km)	3-hourly	Every 6 hours	2023-12-31
Australian Bureau of Meteorology (BOM)	ACCESS-G	Global	0.15° (~15 km)	Hourly	Every 6 hours	2024-01-18
ItaliaMeteo ItaliaMeteo-ARPAE	ICON 2I	Southern Europe	2 km	Hourly	Every 12 hours	2025-04-13
DMI	HARMONIE AROME DINI	Central & Northern Europe	2 km	Hourly	Every 3 hours	2024-07-01
KNMI	HARMONIE AROME Netherlands	Netherlands, Belgium	2 km	Hourly	Every hour	2024-07-01
HARMONIE AROME Europe	Central & Northern Europe up to Iceland	5.5 km	Hourly	Every hour	2024-07-01
MeteoSwiss	ICON CH1	Central Europe	1 km	Hourly	Every 3 hours	2025-07-29
ICON CH2	Central Europe	2 km	Hourly	Every 6 hours	2025-07-29
Which Historical Weather Data to Use?
Open-Meteo provides various datasets for historical weather data: the Historical Weather API and the Historical Forecast API. For novice users expecting a single, definitive source of weather data, this can be confusing. In reality, only a small fraction of the Earth's surface is covered by weather stations with accurate and consistent measurements. To address this gap, numerical weather models are used to approximate past global weather.

Historical Weather API: This dataset is based on reanalysis weather models, particularly ERA5. It offers data from 1940 onwards with reasonable consistency throughout the time series, making it ideal for analyzing weather trends and climate change. The focus here is on consistency rather than pinpoint accuracy, with a spatial resolution ranging from 9 to 25 kilometres.
Historical Forecast API: This dataset is constructed by continuously assembling weather forecasts, concatenating the first hours of each model update. Initialized with actual measurements, it closely mirrors local measurements but provides global coverage. However, it only includes data from the past 2-5 years and lacks long-term consistency due to evolving weather models and better initialization data over time.
Previous Runs API: Similar to the Historical Forecast API, this dataset archives high-resolution weather models but includes data with a lead time offset of 1, 2, 3, 4, or more days. This makes it ideal for analyzing forecast performance several days into the future. Due to the vast amount of data, only common weather variables are stored, with data processing beginning in early 2024.
Choosing the Right Dataset:
For analyzing weather trends or climate change over decades, use the Historical Weather API with reanalysis data from 1940 onwards.
For higher accuracy over the past few years, the Historical Forecast API with high-resolution forecasts is more suitable.
To optimize weather forecasts using machine learning, it's essential to use data from the same high-resolution weather models, available through both the Historical Forecast API and the Previous Runs API.
API Endpoint
As the API is identical to the Forecast API, please refer to the Weather Forecast API documentation for all available variables and parameters. The only notable difference is the API host "historical-forecast-api.open-meteo.com" as historical data is moved to a different set of servers with access to a large storage system.

