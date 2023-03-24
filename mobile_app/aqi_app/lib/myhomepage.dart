import 'dart:core';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'dart:convert';
import './screens/displayPage.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var newVal = true;
  final _controller = TextEditingController();

  void _saveForm() {
    final isValid = _formKey.currentState!.save();
    // if (!isValid) {
    //   return;
    // }
    _formKey.currentState!.save();
    setState(
      () {
        newVal = false;
      },
    );
  }

  Future<void> getData() async {
    final url = 'http://${_controller.text}:8000/api/verify/';
    //const newurl = 'http://127.0.0.1:8000/api/verify/';
    //const url = 'https://jsonplaceholder.typicode.com/albums';
    try {
      final response = await http.get(Uri.parse(url));
      final extractedData = json.decode(response.body);
      if (extractedData == null) {
        return showDialog(
            context: context,
            builder: (_) => AlertDialog(
                  content: Text('Please verify address'),
                ));
      } else {
        print(extractedData);
        print('extractedData');
        if (extractedData == '2') {
          Navigator.of(context)
              .push(MaterialPageRoute(builder: (_) => DispalyPage()));
        } else {
          print('not working');
          showDialog(
              context: context,
              builder: (_) => AlertDialog(
                    content: Text('Please verify address'),
                  ));
        }
        // Navigator.of(context)
        //     .push(MaterialPageRoute(builder: (_) => DispalyPage()));
      }

      if (response.statusCode == 200) {
        print(response);
      }
    } catch (e) {
      print(e.toString());
      showDialog(
          context: context,
          builder: (_) => const AlertDialog(
                content: Text('Please verify address'),
              ));
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
      appBar: AppBar(),
      backgroundColor: Colors.white,
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
            Padding(
              padding: const EdgeInsets.all(15.0),
              child: Form(
                key: _formKey,
                child: TextFormField(
                    controller: _controller,
                    validator: (value) {
                      if (value!.isEmpty) {
                        return "Please enter valid I.P address";
                      }
                      return null;
                    },
                    onSaved: (newValue) {
                      print(newValue);
                    },
                    decoration: InputDecoration(
                        iconColor: Colors.white,
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(15)))),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Padding(
                  padding: const EdgeInsets.only(right: 8.0),
                  child: newVal
                      ? ElevatedButton(
                          onPressed: getData, child: const Text('Update'))
                      : IconButton(
                          onPressed: () {
                            Navigator.of(context).push(MaterialPageRoute(
                                builder: (_) => DispalyPage()));
                          },
                          icon: const Icon(
                            Icons.navigate_next,
                          )),
                ),
              ],
            ),
            //ElevatedButton(onPressed: postDate, child: Text('post')),
            // IconButton(
            //     onPressed: () {
            //       Navigator.of(context)
            //           .push(MaterialPageRoute(builder: (_) => DispalyPage()));
            //     },
            //     icon: const Icon(
            //       Icons.navigate_next,
            //     )),
          ],
        ),
      ),
    );
  }
}
