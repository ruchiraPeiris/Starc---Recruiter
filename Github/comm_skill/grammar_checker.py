import er

tool = er.LanguageTool('en-GB')
text = 'This are bad.'
matches = tool.check(text)
len(matches)