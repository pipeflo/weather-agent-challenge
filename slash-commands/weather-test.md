# Weather Test Slash Command

## Command: /weather-test

### Description
Test the weather agent's API integration and response formatting locally.

### Usage
```
/weather-test [city]
```

### Parameters
- `city` (optional): City name to test. Defaults to "London" if not provided.

### Functionality
1. Check if OPENWEATHER_API_KEY environment variable is set
2. Test API connection with specified city
3. Validate response format and data structure
4. Display formatted weather information
5. Report any errors or issues found

### Example Output
```
🧪 Testing Weather API Integration
================================

✅ API Key: Configured
✅ API Connection: Success
✅ City: London, GB
✅ Temperature: 15°C (feels like 13°C)
✅ Conditions: Partly cloudy
✅ Response Format: Valid

Test completed successfully!
```

### Error Handling
- Missing API key: Provide setup instructions
- Invalid city: Suggest valid city names
- API errors: Display error codes and messages
- Network issues: Suggest troubleshooting steps

### Implementation
This command should:
- Import the weather agent's API functions
- Run test scenarios with different inputs
- Validate response structure and content
- Provide clear feedback on test results
