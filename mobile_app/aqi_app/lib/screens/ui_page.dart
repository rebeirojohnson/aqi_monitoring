import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import '../models/weather_info.dart';
import 'dart:convert';
import './radialgauge.dart';
import '../data/api_values.dart';
import 'package:intl/intl.dart';

class UiPage extends StatefulWidget {
  @override
  State<UiPage> createState() => _UiPageState();
}

class _UiPageState extends State<UiPage> {
  @override
  String name = '';
  String country = '';
  String temp_c = '';
  String iconImage = '';
  String humidity = '';
  String cond = '';
  String wind_dir = '';
  String pm = '';
  String no2 = '';
  String no = '';
  String so2 = '';
  String formatted = '';

  var isLoading = false;

  Future<void> getData() async {
    try {
      final DateFormat formatter = DateFormat('yyyy-MM-dd');
      formatted = formatter.format(DateTime.now());
      //const url = 'http://139.59.64.29:9999/api/get-weather/';
      const url = 'http://www.greedandfear.fun:9999/api/get-weather/';
      var response = await http.post(Uri.parse(url), body: {"date": formatted});
      var responseData = json.decode(response.body);

      AqiApi apiData = AqiApi(
        aqi: responseData['aqi'].toString(),
        pm: responseData['pm'].toString(),
        no: responseData['no'].toString(),
        no2: responseData['no2'].toString(),
        so2: responseData['so2'].toString(),
      );

      print(responseData);
      // to display values in app

      pm = apiData.pm;
      no = apiData.no;
      no2 = apiData.no2;
      so2 = apiData.no2;

      print(pm);
      print(no);
      print(no2);
      print(so2);
    } catch (e) {
      showDialog(
          context: context,
          builder: (context) {
            return AlertDialog(
              title: const Text('Something went wrong'),
              actions: [
                GestureDetector(
                  onTap: () => Navigator.of(context).pop(),
                  child: const Padding(
                    padding: EdgeInsets.all(8.0),
                    child: Text(
                      "Ok",
                      style: TextStyle(color: Colors.blue, fontSize: 16),
                    ),
                  ),
                )
              ],
            );
          });
      print(e.toString());
    }
  }

  List<WeatherInfo> weatherData = [];

  Future<List<WeatherInfo>> getRequest() async {
    try {
      final response = await http.get(
          Uri.parse('http://www.greedandfear.fun:9999/api/today-weather/'));
      var responseData = json.decode(response.body);
      print(responseData);

      WeatherInfo weaDatas = WeatherInfo(
        name: responseData['name'],
        temp_c: responseData['aqi'].toString(),
        humidity: responseData['sosecond'].toString(),
        cond: responseData['text'],
        wind_dir: responseData['pmsecond'].toString(),
      );
      final DateFormat formatter = DateFormat('yyyy-MM-dd');
      formatted = formatter.format(DateTime.now());

      name = weaDatas.name;

      temp_c = weaDatas.temp_c;

      humidity = weaDatas.humidity;
      cond = weaDatas.cond;
      wind_dir = weaDatas.wind_dir;

      weatherData.add(weaDatas);
      print(temp_c);
      print(cond);
      print(wind_dir);
    } catch (e) {
      print(e.toString());
    }

    return weatherData;
  }

  reloadData() {
    setState(() {
      isLoading = true;
    });
    CircularProgressIndicator();
    getRequest();
    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      body: Container(
        child: FutureBuilder(
            future: getRequest(),
            builder: (context, snapshot) {
              if (snapshot.data == null) {
                return const Center(child: CircularProgressIndicator());
              } else {
                return Column(
                  children: [
                    Container(
                        padding: const EdgeInsets.only(top: 45),
                        margin: const EdgeInsets.symmetric(horizontal: 10),
                        height: size.height * 0.75,
                        width: size.width,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(40),
                          gradient: const LinearGradient(
                              colors: [Color(0xff955cd1), Color(0xff3fa2fa)],
                              begin: Alignment.bottomCenter,
                              end: Alignment.topCenter,
                              stops: [0.2, 0.85]),
                        ),
                        child: isLoading
                            ? Center(child: CircularProgressIndicator())
                            : Column(
                                children: [
                                  Text(
                                    name,
                                    style: const TextStyle(
                                        fontSize: 35, color: Colors.white),
                                  ),
                                  const SizedBox(
                                    height: 10,
                                  ),
                                  //DateTime.
                                  Text(
                                    formatted,
                                    style: const TextStyle(
                                        fontSize: 16, color: Colors.white),
                                  ),
                                  const SizedBox(
                                    height: 10,
                                  ),
                                  Container(
                                      height: size.height * 0.2,
                                      width: size.width * 0.5,
                                      decoration: BoxDecoration(
                                          borderRadius:
                                              BorderRadius.circular(12),
                                          color: Colors.transparent),
                                      child: Image.asset(
                                        'assets/icons/clouds.png',
                                        color: Colors.white,
                                        fit: BoxFit.cover,
                                      )),
                                  Text(
                                    cond,
                                    style: const TextStyle(
                                        fontSize: 30,
                                        color: Colors.white,
                                        fontWeight: FontWeight.w600),
                                  ),
                                  const SizedBox(
                                    height: 5,
                                  ),
                                  Text(
                                    temp_c,
                                    style: const TextStyle(
                                        fontSize: 60,
                                        color: Colors.white,
                                        fontWeight: FontWeight.w800),
                                  ),
                                  const SizedBox(
                                    height: 10,
                                  ),
                                  Row(
                                    children: [
                                      Expanded(
                                          child: Column(
                                        children: [
                                          Image.asset(
                                            'assets/icons/humidity.png',
                                            width: size.width * 0.13,
                                          ),
                                          const SizedBox(
                                            height: 10,
                                          ),
                                          Text(
                                            humidity,
                                            style: const TextStyle(
                                                fontSize: 21,
                                                color: Colors.white,
                                                fontWeight: FontWeight.bold),
                                          ),
                                          const SizedBox(
                                            height: 5,
                                          ),
                                          const Text(
                                            'Sulfur',
                                            style: TextStyle(
                                                fontSize: 20,
                                                color: Colors.white,
                                                fontWeight: FontWeight.normal),
                                          ),
                                        ],
                                      )),
                                      Expanded(
                                          child: Column(
                                        children: [
                                          Image.asset(
                                            'assets/icons/wind-direction.png',
                                            width: size.width * 0.13,
                                          ),
                                          const SizedBox(
                                            height: 10,
                                          ),
                                          Text(
                                            wind_dir,
                                            style: const TextStyle(
                                                fontSize: 21,
                                                color: Colors.white,
                                                fontWeight: FontWeight.bold),
                                          ),
                                          const SizedBox(
                                            height: 5,
                                          ),
                                          const Text(
                                            'PM2.5',
                                            style: TextStyle(
                                                fontSize: 20,
                                                color: Colors.white,
                                                fontWeight: FontWeight.normal),
                                          ),
                                        ],
                                      )),
                                    ],
                                  ),
                                ],
                              )),
                    const SizedBox(
                      height: 10,
                    ),
                    Padding(
                      padding: const EdgeInsets.all(15.0),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          GestureDetector(
                            onTap: reloadData,
                            child: Container(
                              alignment: Alignment.center,
                              height: size.height * 0.07,
                              width: size.width * 0.37,
                              decoration: BoxDecoration(
                                  color: Colors.purpleAccent,
                                  borderRadius: BorderRadius.circular(15)),
                              child: const Text(
                                'GET WEATHER',
                                style: TextStyle(
                                    color: Colors.white, fontSize: 18),
                              ),
                            ),
                          ),
                          GestureDetector(
                            onTap: () => Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (buildrContext) =>
                                        const RadialGauge())),
                            child: Container(
                              alignment: Alignment.center,
                              height: size.height * 0.07,
                              width: size.width * 0.37,
                              decoration: BoxDecoration(
                                  color: Colors.purpleAccent,
                                  borderRadius: BorderRadius.circular(15)),
                              child: const Text(
                                'AQI',
                                style: TextStyle(
                                    color: Colors.white, fontSize: 18),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                );
              }
            }),
      ),
    );
  }
}
