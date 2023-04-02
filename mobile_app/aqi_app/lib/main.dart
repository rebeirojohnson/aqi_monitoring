import 'package:flutter/material.dart';
import './screens/ui_page.dart';
import './screens/get_started.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(scaffoldBackgroundColor: const Color(0xff081b25)),
      debugShowCheckedModeBanner: false,
      home: const GetStarted(),
    );
  }
}
