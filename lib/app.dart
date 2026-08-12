import 'package:flutter/material.dart';

import 'screens/splash_screen.dart';

class MiniAiAssistantApp extends StatelessWidget {
  const MiniAiAssistantApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Mini AI Assistant',
      theme: ThemeData(
        brightness: Brightness.dark,
        useMaterial3: true,
      ),
      home: const SplashScreen(),
    );
  }
}