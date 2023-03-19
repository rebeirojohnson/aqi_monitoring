import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

class RadialGauge extends StatefulWidget {
  const RadialGauge({super.key});

  @override
  State<RadialGauge> createState() => _RadialGaugeState();
}

class _RadialGaugeState extends State<RadialGauge> {
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
          child: Container(
              child: SfRadialGauge(axes: <RadialAxis>[
            RadialAxis(minimum: 0, maximum: 500, ranges: <GaugeRange>[
              GaugeRange(startValue: 0, endValue: 50, color: Colors.green),
              GaugeRange(startValue: 50, endValue: 100, color: Colors.yellow),
              GaugeRange(startValue: 100, endValue: 150, color: Colors.orange),
              GaugeRange(startValue: 150, endValue: 200, color: Colors.red),
              GaugeRange(startValue: 200, endValue: 300, color: Colors.purple),
              GaugeRange(
                  startValue: 300,
                  endValue: 500,
                  color: const Color.fromARGB(255, 171, 78, 78)),
            ], pointers: const <GaugePointer>[
              NeedlePointer(value: 70)
            ], annotations: <GaugeAnnotation>[
              GaugeAnnotation(
                  widget: Container(
                      child: const Text('70.0',
                          style: TextStyle(
                              fontSize: 25, fontWeight: FontWeight.bold))),
                  angle: 90,
                  positionFactor: 0.5)
            ])
          ])),
        )));
  }
}
