% Simple Voice Assistant Knowledge Base

response(hello, 'Hello, how can I help you?').
response(time, 'You can check the system time.').
response(name, 'I am a Prolog voice assistant.').
response(bye, 'Goodbye! Have a nice day.').

chat(Input, Response) :-
    response(Input, Response).
