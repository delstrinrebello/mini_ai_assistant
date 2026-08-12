import 'package:flutter_riverpod/flutter_riverpod.dart';

class ChatMessage {
  final String text;
  final bool isUser;

  ChatMessage({
    required this.text,
    required this.isUser,
  });
}

class ChatNotifier extends Notifier<List<ChatMessage>> {
  @override
  List<ChatMessage> build() {
    return [];
  }

  void sendMessage(String text) {
    if (text.trim().isEmpty) return;

    state = [
      ...state,
      ChatMessage(
        text: text,
        isUser: true,
      ),
    ];

    state = [
      ...state,
      ChatMessage(
        text: 'You said: $text',
        isUser: false,
      ),
    ];
  }
}

final chatProvider =
    NotifierProvider<ChatNotifier, List<ChatMessage>>(
  ChatNotifier.new,
);