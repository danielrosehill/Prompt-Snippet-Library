# Model Identification Snippet

## Text Version
```
Please identify yourself by stating your model name and version (e.g., "Claude 3.5 Sonnet", "Gemini Pro 2.5").
```

## JSON Integration Example
```json
{
  "system_prompt": "You are an AI assistant. Please identify yourself by stating your model name and version (e.g., 'Claude 3.5 Sonnet', 'Gemini Pro 2.5'). [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Place this at the beginning of system prompts when model identification is required
- Expected responses: "Claude 3.5 Sonnet", "Gemini Pro 2.5", etc.
- Useful for logging, debugging, and model-specific workflow routing
