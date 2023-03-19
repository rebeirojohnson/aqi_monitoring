import 'package:flutter/material.dart';

class WeatherInfo {
  final String name;
  final String country;
  final String iconImage;
  final String temp_c;
  final String humidity;
  final String cond;
  final String wind_dir;

  WeatherInfo({
    required this.name,
    required this.country,
    required this.iconImage,
    required this.temp_c,
    required this.humidity,
    required this.cond,
    required this.wind_dir,
  });
}
