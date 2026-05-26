RUN_INDENTED = True

message = 'running unindented'

if RUN_INDENTED:
    message = 'runnin idented'

print(message)

def ident_function():
    greet = "hello identation"
    return greet

print(ident_function())