import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
// import './view/location_screens.dart';
import './models/weahter_data.dart';

import './screens/radialgauge.dart';
import 'testpage.dart';
import './screens/ui_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => WeatherData(),
      child: MaterialApp(
        theme: ThemeData(scaffoldBackgroundColor: const Color(0xff081b25)),
        debugShowCheckedModeBanner: false,
        home: UiPage(),
      ),
    );
  }
}
