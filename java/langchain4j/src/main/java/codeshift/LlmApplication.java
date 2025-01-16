package codeshift;

import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.googleai.GoogleAiGeminiChatModel;

public class LlmApplication {

  private static final String MODEL_NAME = "gemini-2.0-flash-exp";

  public static void main(String[] args) {
    ChatLanguageModel model = GoogleAiGeminiChatModel.builder()
      .apiKey(System.getenv("GEMINI_API_KEY"))
      .modelName(MODEL_NAME)
      .temperature(0.1)
      .build();

    String response = model.generate("Tell me a joke");

    System.out.println(response);
    System.exit(0);
  }
}
