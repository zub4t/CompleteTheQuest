# Complete The Quest


## Prerequisites
Before you begin, ensure you have met the following requirements:
- Java JDK 17 or higher installed
- Gradle (if you prefer not to use the included Gradle wrapper)

## Getting Started

### Building the Project
To build the project, follow these steps:

1. Open your terminal.
2. Navigate to the root directory of the project.
3. Run the following command to assemble the project using the Gradle wrapper included in the project:

    ```
    ./gradlew assemble
    ```

    If you are on Windows, use:

    ```
    gradlew.bat assemble
    ```

This command compiles the source code, and packages the project into a JAR file.

### Running the Project
After building the project, you need to move the JAR file to the root of the project and run it. Follow these steps:

1. Navigate to the `build/libs` directory where the JAR file is located.
2. Move the JAR file to the root of the project using the following command:

    ```
    cp complete-the-quest-0.0.1-SNAPSHOT.jar ../../
    ```

3. Go back to the root directory of the project.
4. Run the JAR file with the following command:

    ```
    java -jar complete-the-quest-0.0.1-SNAPSHOT.jar
    ```


Your application should now be running. You can access it on ```localhost:8080```.

