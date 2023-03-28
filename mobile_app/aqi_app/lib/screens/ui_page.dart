import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import '../models/weather_info.dart';
import 'dart:convert';
import './radialgauge.dart';
import '../myhomepage.dart';

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
  var isLoading = false;

  List<WeatherInfo> weatherData = [];

  Future<List<WeatherInfo>> getRequest() async {
    try {
      final response = await http.get(Uri.parse(
          'https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no'));
      var responseData = json.decode(response.body);
      print(responseData);
      print(responseData['current']['temp_c']);

      WeatherInfo weaDatas = WeatherInfo(
        name: responseData['location']['name'],
        country: responseData['location']['country'],
        iconImage: responseData['current']['condition']['icon'],
        temp_c: responseData['current']['temp_c'].toString(),
        humidity: responseData['current']['humidity'].toString(),
        cond: responseData['current']['condition']['text'],
        wind_dir: responseData['current']['wind_dir'],
      );

      name = weaDatas.name;
      country = weaDatas.country;
      temp_c = weaDatas.temp_c;
      iconImage = 'http:${weaDatas.iconImage}';

      humidity = weaDatas.humidity;
      cond = weaDatas.cond;
      wind_dir = weaDatas.wind_dir;

      weatherData.add(weaDatas);
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
                                    DateTime.now().toString(),
                                    style: const TextStyle(
                                        fontSize: 15, color: Colors.white),
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
                                      child: Image.network(
                                        iconImage,
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
                                    '$temp_c° C',
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
                                            'Humdity',
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
                                            'Wind Direction',
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
                            // onTap: reloadData,
                            onTap: () => Navigator.of(context).push(
                                MaterialPageRoute(
                                    builder: (context) => const MyHomePage())),
                            child: Container(
                              alignment: Alignment.center,
                              height: size.height * 0.07,
                              width: size.width * 0.37,
                              decoration: BoxDecoration(
                                  color: Colors.purpleAccent,
                                  borderRadius: BorderRadius.circular(15)),
                              child: const Text(
                                'Connect',
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
                          'Reload Data',
                          style: TextStyle(color: Colors.white, fontSize: 18),
                        ),
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
