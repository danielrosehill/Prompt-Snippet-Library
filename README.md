# Prompt Snippet Library

A curated collection of reusable prompt snippets for system prompts, workflows, and AI agents. Each snippet includes both text and JSON integration examples.

## Repository Structure

### 📋 Model Identification
- **model-identification.md** - Snippet for requesting model name and version identification

### 🔄 Workflow Control
- **single-turn-workflow.md** - Ensures definitive, complete responses without follow-up questions

### 🎨 Formatting Instructions
- **raw-markdown.md** - Raw markdown output formatting
- **gmail-safe-html.md** - Email-client safe HTML formatting
- **csv-output.md** - CSV data formatting within code blocks
- **sql-output.md** - Valid SQL statement formatting

### 🔗 Source Handling
- **sources-section.md** - Dedicated sources section with simple hyperlinks

### 📝 Output Structure
- **prompt-summary.md** - Begin output with improved summary of user's prompt
- **verbatim-prompt.md** - Begin output with exact reproduction of user's prompt
- **timestamp.md** - Add timestamp to start of every output

## Alphabetical Index

- **CSV Output** - This snippet formats output as CSV data within a code block, producing immediately importable data that is compatible with Excel, Google Sheets, and database import tools.
- **Gmail Safe HTML** - This Gmail-safe HTML formatting snippet is designed for email marketing templates and automated email generation, ensuring compatibility with major email clients while avoiding security issues and style stripping.
- **Model Identification** - This prompt snippet is used to require users to identify their model version, facilitating logging, debugging, and route-specific workflows for models that support this functionality.
- **Prompt Summary** - This prompt snippet helps generate a clear summary of the user's request, improving communication clarity and providing a structured output format for professional or documentation purposes.
- **Raw Markdown** - This prompt snippet helps you generate clean and compatible raw markdown output for documentation systems like README files, reducing HTML injection risks and ensuring proper formatting.
- **Single Turn Workflow** - This single-turn workflow ensures comprehensive, definitive responses without back-and-forth by providing clear instructions for model output, ideal for automated workflows with batch processing or API integrations.
- **Sources Section** - This prompt snippet provides guidance on how to structure and integrate sources within written content, ensuring accessibility and readability across various systems.
- **SQL Output** - This snippet generates immediately executable SQL code with proper syntax highlighting and protection against SQL injection, ideal for database administration and data analysis tasks.
- **Timestamp** - This snippet provides a structured way to embed current date and time into user responses for logging, auditing, and time-sensitive purposes.
- **Verbatim Prompt** - This prompt snippet ensures that user requests are accurately recorded and preserved, providing a clear audit trail for conversation logging, debugging, and maintaining accountability in automated systems.

## Usage

Each snippet file contains:
1. **Text Version** - Ready-to-use prompt text
2. **JSON Integration Example** - How to integrate into JSON-based systems
3. **Usage Notes** - Context and best practices

## Integration Examples

### System Prompt Integration
```json
{
  "system_prompt": "[snippet text] [your additional instructions...]",
  "user_prompt": "Your user prompt here"
}
```

### Workflow Chaining
Combine multiple snippets for complex workflows:
```
[Model Identification] + [Single Turn Workflow] + [Formatting Instructions]
```

## Contributing

When adding new snippets:
1. Create appropriately named folders for categories
2. Include both text and JSON examples
3. Add usage notes and context
4. Update this README with the new snippet location
