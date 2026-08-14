import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../services/ai_service.dart';

class ChatMessage {
  final String text;
  final bool isUser;

  ChatMessage({
    required this.text,
    required this.isUser,
  });
}

class ChatState {
  final List<ChatMessage> messages;
  final bool isLoading;

  ChatState({
    required this.messages,
    this.isLoading = false,
  });
}

class ChatNotifier extends Notifier<ChatState> {
  final AiService _aiService = AiService();

  @override
  ChatState build() {
    return ChatState(
      messages: [],
    );
  }

  Future<void> sendMessage(String text) async {
    if (text.trim().isEmpty || state.isLoading) return;

    state = ChatState(
      messages: [
        ...state.messages,
        ChatMessage(
          text: text,
          isUser: true,
        ),
      ],
      isLoading: true,
    );

    try {
      final response = await _aiService.sendMessage(text);

      state = ChatState(
        messages: [
          ...state.messages,
          ChatMessage(
            text: response,
            isUser: false,
          ),
        ],
        isLoading: false,
      );
    } catch (e) {
      state = ChatState(
        messages: [
          ...state.messages,
          ChatMessage(
            text: 'Something went wrong.',
            isUser: false,
          ),
        ],
        isLoading: false,
      );
    }
  }
}

final chatProvider =
    NotifierProvider<ChatNotifier, ChatState>(
  ChatNotifier.new,
);