import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';
import '../data/api_values.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';

class RadialGauge extends StatefulWidget {
  const RadialGauge({super.key});

  @override
  State<RadialGauge> createState() => _RadialGaugeState();
}

class _RadialGaugeState extends State<RadialGauge> {
  // final _date = GetApiVal();
  DateTime? dateTime = DateTime.now();
  DateFormat dateformater = DateFormat('yyyy-MM-dd');
  String formatted = '';
  String aqiVal = '';
  double needlevalue = 0;

  void checkDate() {
    showDatePicker(
            context: context,
            initialDate: DateTime.now(),
            firstDate: DateTime(2000),
            lastDate: DateTime(2060))
        .then((value) {
      setState(() {
        // dateTime = value;
        final DateFormat formatter = DateFormat('yyyy-MM-dd');
        formatted = formatter.format(value!);
      });
    });
    // dateTime = formatted as DateTime?;
    print(formatted);
  }

  Future<void> getData() async {
    try {
      //const url = 'http://139.59.64.29:9999/api/get-weather/';
      const url = 'http://www.greedandfear.fun:9999/api/get-weather/';
      var response = await http.post(Uri.parse(url), body: {"date": formatted});
      var responseData = json.decode(response.body);
      AqiApi apiData = AqiApi(aqi: responseData['aqi'].toString());
      setState(() {
        needlevalue = double.parse(apiData.aqi);
      });

      print(responseData);
      aqiVal = apiData.aqi;
      print(aqiVal);
    } catch (e) {
      showDialog(
          context: context,
          builder: (context) {
            return AlertDialog(
              title: const Text('Please Select the date first!'),
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.grey[200],
        appBar: AppBar(
          leading: IconButton(
              onPressed: Navigator.of(context).pop,
              icon: const Icon(
                Icons.arrow_back,
                color: Colors.black,
              )),
          elevation: 0,
          backgroundColor: Colors.transparent,
        ),
        body: Center(
            child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 8.0),
          child: Column(
            //mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Today date: ${dateformater.format(dateTime!)} ',
                style: TextStyle(fontSize: 20),
              ),
              const SizedBox(height: 60),
              Text(
                'Choose date to get aqi:  $formatted',
                style: const TextStyle(fontSize: 20),
              ),
              const SizedBox(height: 60),
              Container(
                  child: SfRadialGauge(axes: <RadialAxis>[
                RadialAxis(minimum: 0, maximum: 500, ranges: <GaugeRange>[
                  GaugeRange(startValue: 0, endValue: 50, color: Colors.green),
                  GaugeRange(
                      startValue: 50, endValue: 100, color: Colors.yellow),
                  GaugeRange(
                      startValue: 100, endValue: 150, color: Colors.orange),
                  GaugeRange(startValue: 150, endValue: 200, color: Colors.red),
                  GaugeRange(
                      startValue: 200, endValue: 300, color: Colors.purple),
                  GaugeRange(
                      startValue: 300,
                      endValue: 500,
                      color: const Color.fromARGB(255, 171, 78, 78)),
                ], pointers: <GaugePointer>[
                  NeedlePointer(value: needlevalue)
                ], annotations: <GaugeAnnotation>[
                  GaugeAnnotation(
                      widget: Container(
                          child: Text(aqiVal,
                              style: const TextStyle(
                                  fontSize: 25, fontWeight: FontWeight.bold))),
                      angle: 90,
                      positionFactor: 0.5)
                ])
              ])),
              const SizedBox(height: 60),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton(
                    onPressed: checkDate,
                    child: const Text('Choose Date'),
                  ),
                  ElevatedButton(
                    onPressed: getData,
                    child: const Text('Get Data'),
                  ),
                ],
              ),
            ],
          ),
        )));
  }
}
