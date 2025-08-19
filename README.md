# Hajfish

User thread:
- take user input and feed it to the shell thread
- streams "rational"

Shell thread: is the agent, generates shell commands, runs them, then processes the output
- make a list of commands to run
- modifies the list based on output of the previous command
	- [command1, command2, command3]
	- after command1 gets popped from list, feedback the output from command1 as well as the command list
	- command is a json object in the following format: {command: "command", arguments: [arg1, arg2, arg3]}
		- pray the the LLM can generate the docs properly
- commands run through the python pipe
