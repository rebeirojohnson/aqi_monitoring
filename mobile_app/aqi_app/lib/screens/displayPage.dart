import 'dart:core';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'dart:convert';

class DispalyPage extends StatefulWidget {
  const DispalyPage({super.key});

  @override
  State<DispalyPage> createState() => _DispalyPageState();
}

class _DispalyPageState extends State<DispalyPage> {
  @override
  var newVal = true;
  final _controller = TextEditingController();

  void _saveForm() {
    final isValid = _formKey.currentState!.save();

    _formKey.currentState!.save();
    setState(
      () {
        newVal = true;
      },
    );
  }

  Future<void> getData() async {
    final url = 'http://${_controller.text}:8000/api';
    const newurl = 'http://192.168.10.239:8000/api';
    //const url = 'https://jsonplaceholder.typicode.com/albums';
    try {
      final response = await http.get(Uri.parse(url));
      final extractedData = json.decode(response.body);
      if (extractedData == null) {
        return;
      } else {
        print(extractedData);
        print('extractedData');
      }

      if (response.statusCode == 200) {
        print(response);
      }
    } catch (e) {
      print(e.toString());
    }
  }

  Future<void> postDate() async {
    const url = 'http://192.168.10.239:8000/api/get-weather/2022-09-31 11:00';

    //const url = 'https://jsonplaceholder.typicode.com/albums';
    try {
      final response = await http.get(Uri.parse(url));
      final extractedData = json.decode(response.body);
      if (extractedData == null) {
        return;
      } else {
        print(extractedData.toString());
        print('extractedData');
      }

      if (response.statusCode == 200) {
        print(response);
      }
    } catch (e) {
      print(e.toString());
    }
  }

  final _formKey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(
              height: 22,
            ),
            const Padding(
              padding: EdgeInsets.only(left: 15.0),
              child: Text(
                'Please connect with I.P',
                style: TextStyle(fontSize: 24),
              ),
            ),
            ElevatedButton(onPressed: postDate, child: const Text('post'))
          ],
        ),
      ),
    );
  }
}
