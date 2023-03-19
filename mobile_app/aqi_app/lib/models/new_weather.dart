// To parse this JSON data, do
//
//     final welcome = welcomeFromJson(jsonString);

import 'dart:convert';

Welcome welcomeFromJson(String str) => Welcome.fromJson(json.decode(str));

String welcomeToJson(Welcome data) => json.encode(data.toJson());

class Welcome {
  Welcome({
    required this.location,
    required this.current,
  });

  Location location;
  Current current;

  factory Welcome.fromJson(Map<String, dynamic> json) => Welcome(
        location: Location.fromJson(json["location"]),
        current: Current.fromJson(json["current"]),
      );

  Map<String, dynamic> toJson() => {
        "location": location.toJson(),
        "current": current.toJson(),
      };
}

class Current {
  Current({
    required this.humidity,
    required this.cloud,
    required this.tempC,
  });

  int tempC;

  int humidity;
  int cloud;

  factory Current.fromJson(Map<String, dynamic> json) => Current(
        humidity: json["humidity"],
        cloud: json["cloud"],
        tempC: json["tempC"],
      );

  Map<String, dynamic> toJson() => {
        "temp_c": tempC,
        "humidity": humidity,
        "cloud": cloud,
      };
}

class Condition {
  Condition({
    required this.text,
    required this.icon,
    required this.code,
  });

  String text;
  String icon;
  int code;

  factory Condition.fromJson(Map<String, dynamic> json) => Condition(
        text: json["text"],
        icon: json["icon"],
        code: json["code"],
      );

  Map<String, dynamic> toJson() => {
        "text": text,
        "icon": icon,
        "code": code,
      };
}

class Location {
  Location({
    required this.name,
    required this.region,
    required this.country,
  });

  String name;
  String region;
  String country;

  factory Location.fromJson(Map<String, dynamic> json) => Location(
        name: json["name"],
        region: json["region"],
        country: json["country"],
      );

  Map<String, dynamic> toJson() => {
        "name": name,
        "region": region,
        "country": country,
      };
}
