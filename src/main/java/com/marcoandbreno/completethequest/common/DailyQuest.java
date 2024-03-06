package com.marcoandbreno.completethequest.common;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.json.JSONObject;

public class DailyQuest {
  public static String answer;
  public static String question;

  public DailyQuest() {
    loadQuestionFromFile();
  }

  private void loadQuestionFromFile() {
    // Get the path to the directory where the JAR file is located
    String jarDirectory = new File(".").getAbsolutePath();

    // Construct the file path to the question file, assuming the file extension is now .json
    String questionFilePath =
      jarDirectory + File.separator + "daily_quest.json";

    try {
      // Read the entire file content into a String
      String content = new String(
        Files.readAllBytes(Paths.get(questionFilePath))
      );

      // Parse the content as JSON
      JSONObject jsonObject = new JSONObject(content);

      // Extract the question property value
      DailyQuest.question = jsonObject.getString("question");
      DailyQuest.answer = jsonObject.getString("answer");
    } catch (IOException e) {
      // Handle file reading errors
      e.printStackTrace();
    } catch (Exception e) {
      // Handle any other exceptions, e.g., JSON parsing errors
      e.printStackTrace();
    }
  }
}
