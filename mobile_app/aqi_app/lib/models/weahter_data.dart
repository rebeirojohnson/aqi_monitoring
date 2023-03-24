import 'package:flutter/material.dart';

import './weather_info.dart';
import 'package:provider/provider.dart';

class WeatherData with ChangeNotifier {
  List<WeatherInfo> _weatherData = [];

  List<WeatherInfo> get newWeatherData {
    return [..._weatherData];
  }
}
