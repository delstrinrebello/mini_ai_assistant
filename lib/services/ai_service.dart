import 'dart:convert';

import 'package:http/http.dart' as http;

class AiService {
  // static const String baseUrl = 'http://127.0.0.1:8000';
  static const String baseUrl = 'http://10.0.2.2:8000';

  Future<String> sendMessage(String message) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/chat'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode({
          'message': message,
        }),
      );

      print('Status code: ${response.statusCode}');
      print('Response body: ${response.body}');

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);

        return data['response'];
      }

      throw Exception(
        'Server returned ${response.statusCode}: ${response.body}',
      );
    } catch (e) {
      print('AI Service Error: $e');
      rethrow;
    }
  }
}