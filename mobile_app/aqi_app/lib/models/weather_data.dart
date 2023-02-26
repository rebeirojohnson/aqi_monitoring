import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';

class Weather {
  final String dateTime;

  Weather({required this.dateTime});
}


// {
// "List": "/task-list/",
// "Detail View": "/task-detail/<str:pk>/",
// "Create": "/task-create/",
// "Update": "/task-update/<str:pk>/",
// "Delete": "/task-delete/<str:pk>/"
// }


// {
// "date_time":"2022-09-31 11:00"
// }





// void main() async {
//   var result =
//       await waitTask("completed").timeout(const Duration(seconds: 10));
//   print(result); // Prints "completed" after 5 seconds.

//   result = await waitTask("completed")
//       .timeout(const Duration(seconds: 1), onTimeout: () => "timeout");
//   print(result); // Prints "timeout" after 1 second.

//   result = await waitTask("first").timeout(const Duration(seconds: 2),
//       onTimeout: () => waitTask("second"));
//   // Prints "second" after 7 seconds.

//   try {
//     await waitTask("completed").timeout(const Duration(seconds: 2));
//   } on TimeoutException {
//     print("throws"); // Prints "throws" after 2 seconds.
//   }

//   var printFuture = waitPrint();
//   await printFuture.timeout(const Duration(seconds: 2), onTimeout: () {
//     print("timeout");
//   });
//   // Prints "timeout" after 2 seconds.
//   await printFuture;
//   // Prints "printed" after additional 3 seconds.
// }

// // Returns [string] after five seconds.
// Future<String> waitTask(String string) async {
//   await Future.delayed(const Duration(seconds: 5));
//   return string;
// }

// // Prints "printed" after five seconds.
// Future<void> waitPrint() async {
//   await Future.delayed(const Duration(seconds: 5));
//   print("printed");
// }