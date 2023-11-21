# Code Craft
### A REST API for code execution

<p align="center">
  <img src="https://media.giphy.com/media/JqmupuTVZYaQX5s094/giphy.gif">
</p>

## What Is Code Craft?
Code Craft is a REST API to execute your code in a chosen language.
You can simple send in a POST request with the code you want to run and the language it is written in.
The server will execute it and return the output along with the exit code.

## How To Use It?
In order to execute your code, make a POST request with the **body form data** containing 2 fields: `language` and `code`.
After processing the request, the API will return the result of the code execution if the request is valid, or the error
message if the request is invalid.

### Input
As mentioned, the request must contain body form data with 2 required fields `language` and `code`.

#### Language Input Field
The value for this field is a string representing the language your code is written in.
Currently, the API accept the following values:
`c` (C), `cpp` (C++), `csharp` (C#), `java` (Java), `javascript` (JavaScript), `python` (Python3), `ruby` (Ruby).
<br/><br/>
The API would return an error if the provided value does not match any of the languages listed above.

#### Code Input Field
The value for this field is the code you would want to be executed.

### Response
In case the request is valid, the API will return stdout, stderr, and the exit code of the code execution.
In case the request is not valid, the API will return the error message.
