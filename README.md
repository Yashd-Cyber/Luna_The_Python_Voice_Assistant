# Luna - Personal Voice Assistant

Luna is a Python-based voice assistant that can perform various tasks including sending emails, taking notes, searching Wikipedia, fetching weather information, and much more using voice commands.

## Features
- **Voice Commands**: Communicate with the assistant through speech.
- **Task Automation**: Send emails, search Wikipedia, take notes, open websites, and more.
- **Weather Information**: Get real-time weather updates.
- **System Control**: Shutdown or restart your computer.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/luna-voice-assistant.git
cd luna-voice-assistant
```

### 2. Install dependencies:

Make sure you have Python installed, then install the required libraries:

```bash
pip install pyttsx3 SpeechRecognition wikipedia requests pyttsx3
```

### 3. Set Up Email (Optional):
For email functionality, replace `'your_email@gmail.com'` and `'your_password'` with your actual Gmail credentials. If you use Gmail with 2FA, create an app-specific password.

### 4. Set Up Weather API (Optional):
Replace `your_api_key_here` with a valid API key from [OpenWeatherMap](https://openweathermap.org/).

## Usage

1. **Run the Assistant**:

   Execute the script:

   ```bash
   python luna_assistant.py
   ```

2. **Interaction**:

   - The assistant will greet you and wait for voice commands.
   - You can ask for the weather, take notes, send an email, open websites, and more.

3. **Voice Commands**:

   - **"Hello"** or **"Hi"**: Greet the assistant.
   - **"Note"**: Take notes and save them.
   - **"Email"**: Send an email.
   - **"Search"**: Search Wikipedia.
   - **"Weather"**: Get weather updates for a specific city.
   - **"Shutdown"** or **"Restart"**: Shutdown or restart the computer.
   - **"Thank you"** or **"Bye"**: End the session.

## Notes
- Ensure your microphone is set up properly and working.
- The assistant uses Google’s Speech Recognition for commands, so an internet connection is required.
- To fetch weather information, you’ll need a valid API key from OpenWeatherMap.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

