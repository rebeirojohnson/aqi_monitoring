import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';

class Testpage extends StatelessWidget {
  DateTime dateTime = DateTime.now();

  Future<void> getData() async {
    try {
      const url = 'http://139.59.64.29:9999/api/get-weather/';
      // var response = await http.get(Uri.parse(url));
      var response = await http.post(Uri.parse(url), body: {"date": ""});
      print(response.body.toString());
    } catch (e) {
      print(e.toString());
    }
  }

  void printVal() {
    print(DateFormat.YEAR_MONTH_DAY);
  }

  @override
  Widget build(BuildContext context) {
    void checkDate() {
      showDatePicker(
          context: context,
          initialDate: DateTime.now(),
          firstDate: DateTime(2000),
          lastDate: DateTime(2060));
      print(DateTime.now());
    }

    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            ElevatedButton(
              onPressed: printVal,
              child: const Text('Get Data'),
            ),
            ElevatedButton(
              onPressed: getData,
              child: const Text('Get Data'),
            ),
          ],
        ),
      ),
    );
  }
}


// import 'dart:convert';
// import './models/weather_info.dart';
// import 'package:flutter/material.dart';
// import 'package:http/http.dart' as http;

// class TEstPage extends StatefulWidget {
//   const TEstPage({super.key});

//   @override
//   State<TEstPage> createState() => _TEstPageState();
// }

// class _TEstPageState extends State<TEstPage> {
//   String name = '';
//   String country = '';
//   String temp_c = '';
//   String iconImage = '';
//   String humidity = '';
//   String cond = '';
//   String wind_dir = '';

//   @override
//   void initState() {
//     super.initState();
//   }

//   // buildwidget(String name, String country, String humditiy) {
//   //   return Row(
//   //     mainAxisAlignment: MainAxisAlignment.spaceBetween,
//   //     children: [
//   //       Text(name),
//   //       Text(country),
//   //       Text(humditiy),
//   //     ],
//   //   );
//   // }

//   late WeatherInfo _weatherInfo;

//   // Future<void> getData() async {
//   //   // var response =
//   //   //     await http.get(Uri.parse('http://127.0.0.1:8000/api/verify/'));
//   //   try {
//   //     var response = await http.get(Uri.parse(
//   //         "https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no"));
//   //     final extractedData = json.decode(response.body);
//   //     print(extractedData);
//   //     //_weatherInfo = WeatherInfo(name: response.body[]);
//   //     _weatherInfo = WeatherInfo(
//   //         name: extractedData['location']['name'],
//   //         country: extractedData['location']['country'],
//   //         iconImage: extractedData['current']['condition']['icon'],
//   //         humidity: extractedData['current']['humidity']);
//   //     print(_weatherInfo);

//   //     //print('Weather Info:' + _weatherInfo.toString());
//   //     // print(response.body.toString());
//   //   } catch (e) {
//   //     print(e.toString());
//   //   }
//   // }

//   // List<Welcome> weaData = [];

//   // Future<List<Welcome>> getNewData() async {
//   //   final response = await http.get(Uri.parse(
//   //       'https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no'));
//   //   var data = jsonDecode(response.body.toString());
//   //   if (response.statusCode == 200) {
//   //     for (Map index in data) {
//   //       weaData.add(Welcome.fromJson(index));
//   //     }
//   //   }
//   // }

//   List<WeatherInfo> weatherData = [];

//   Future<List<WeatherInfo>> getRequest() async {
//     final response = await http.get(Uri.parse(
//         'https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no'));
//     var responseData = json.decode(response.body);
//     print(responseData);
//     print(responseData['current']['temp_c']);

//     WeatherInfo weaDatas = WeatherInfo(
//       name: responseData['location']['name'],
//       country: responseData['location']['country'],
//       iconImage: responseData['current']['condition']['icon'],
//       temp_c: responseData['current']['temp_c'].toString(),
//       humidity: responseData['current']['humidity'].toString(),
//       cond: responseData['current']['condition']['text'],
//       wind_dir: responseData['current']['wind_dir'],
//     );

//     print('1 ' + weaDatas.name);
//     name = weaDatas.name;
//     country = weaDatas.country;
//     temp_c = weaDatas.temp_c;
//     iconImage = 'http:${weaDatas.iconImage}';
//     print(iconImage.toString());
//     humidity = weaDatas.humidity;
//     cond = weaDatas.cond;
//     wind_dir = weaDatas.wind_dir;

//     weatherData.add(weaDatas);

//     // for (var extractData in responseData) {
//     //   WeatherInfo newWeatherData = WeatherInfo(
//     //       name: extractData['location']['name'],
//     //       country: extractData['location']['country'],
//     //       iconImage: extractData['current']['condition']['icon'],
//     //       humidity: extractData['current']['humidity']);
//     //   weatherData.add(newWeatherData);
//     //   print(weatherData);
//     // }
//     return weatherData;
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: SafeArea(
//         child: Center(
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: [
//               Container(
//                 padding: const EdgeInsets.all(20), //inside
//                 margin: const EdgeInsets.all(20), //outside
//                 height: 300,
//                 decoration: BoxDecoration(
//                     borderRadius: BorderRadius.circular(12),
//                     color: Colors.grey[300]),
//                 child: FutureBuilder(
//                     future: getRequest(),
//                     builder: (context, snapshot) {
//                       if (snapshot.data == null) {
//                         return const Text('Loading....');
//                       } else {
//                         return Column(
//                           children: [
//                             Column(
//                               children: [
//                                 Container(
//                                   height: 100,
//                                   width: 100,
//                                   decoration: BoxDecoration(
//                                       borderRadius: BorderRadius.circular(12),
//                                       color: Colors.white),
//                                   child: ClipRRect(
//                                       child: Image.network(
//                                     iconImage,
//                                     fit: BoxFit.fill,
//                                   )),
//                                 ),
//                               ],
//                             ),
//                             const SizedBox(
//                               height: 20,
//                             ),
//                             Row(
//                               mainAxisAlignment: MainAxisAlignment.spaceBetween,
//                               children: [
//                                 Text(name),
//                                 Text(country),
//                                 Text(temp_c),
//                               ],
//                             ),

//                             // buildwidget(
//                             //     weatherData.map((val) => val.name).toList().toString(),
//                             //     'country',
//                             //     'humditiy')
//                             // buildwidget(
//                             //     weaDatas.name, weaDatas.country, weaDatas.humidity)
//                           ],
//                         );
//                       }
//                     }),
//               ),
//               ElevatedButton(
//                   onPressed: getRequest, child: const Text('Get value'))
//             ],
//           ),
//         ),
//       ),
//     );
//   }
// }
