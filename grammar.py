import language_tool_python

tool = language_tool_python.LanguageTool("en-US")


def check_grammar(text):

    matches = tool.check(text)

    corrected_text = language_tool_python.utils.correct(text, matches)

    total_errors = len(matches)

    suggestions = []

    for match in matches:

        message = match.message

        if match.replacements:
            replacement = ", ".join(match.replacements[:3])
        else:
            replacement = "No suggestion"

        # Correct attribute name
        rule = match.rule_id

        suggestion = (
            f"Rule : {rule}\n"
            f"Message : {message}\n"
            f"Suggestion : {replacement}"
        )

        suggestions.append(suggestion)

    return corrected_text, total_errors, suggestions