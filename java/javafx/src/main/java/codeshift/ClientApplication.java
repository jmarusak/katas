package codeshift;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.geometry.Pos;

public class ClientApplication extends Application {

  @Override
  public void start(Stage stage) {
    stage.setTitle("CodeShift");
    
    // Create text areas
    // Create input field and button
    TextField inputField = new TextField();
    inputField.setPromptText("Enter additional instructions...");
    
    Button processButton = new Button("Process");
    processButton.setOnAction(e -> {
        // TODO: Add processing logic here
    });
    
    TextArea leftTextArea = new TextArea();
    TextArea rightTextArea = new TextArea();
    
    // Set preferred size for text areas
    leftTextArea.setPrefRowCount(40);
    leftTextArea.setPrefColumnCount(30);
    rightTextArea.setPrefRowCount(40);
    rightTextArea.setPrefColumnCount(30);

    // Create vertical layout
    HBox headerHBox = new HBox(10);
    headerHBox.getChildren().addAll(processButton, inputField);
    headerHBox.setAlignment(Pos.CENTER_LEFT);
    
    // Create horizontal layout
    HBox textHBox = new HBox(10);
    textHBox.getChildren().addAll(leftTextArea, rightTextArea);
    textHBox.setAlignment(Pos.CENTER);

    VBox mainbox = new VBox(10);
    mainbox.getChildren().addAll(headerHBox, textHBox);
    mainbox.setPadding(new javafx.geometry.Insets(10));

    // Create scene with HBox
    Scene scene = new Scene(mainbox, 800, 600);
    stage.setScene(scene);
    stage.show();
  }

  public static void main(String[] args) {
    launch();
  }
}
