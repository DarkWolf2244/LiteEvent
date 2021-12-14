# LiteEvent

## About
LiteEvent is a decorator-based lightweight and flexible event library for Python. Getting started is really simple.

## Getting Started
Simply import the `Events` class from `LiteEvent` and instantiate it.

    from LiteEvent import Events

	events = Events()

You can pass options here, like disabling the option to emit events that haven't been added yet with `allow_emitting_nonexistent_events=False`.

Use the `@events.on(event)` decorator on a handler.

    @events.on('idea')
	def idea_handler(the_idea):
		print(f"I just had an idea! {the_idea}")

To emit an event, just use `events.emit(event)` with optional arguments that will be passed to the handler:

    events.emit('idea', "Let's make a tiny computer that fits in your palm!")

That'll result in the event handler being called:

    Output:
	I just had an idea! Let's make a tiny computer that fits in your palm!

A full script would look like this:
	   
	from LiteEvent import  Events
	
	events  =  Events()
	
	@events.on('camera.picture')
	def camera_picture_before(announcement):
		print(f"We're about to take a picture! {announcement}")
	
	events.emit('camera.picture', "Say cheese!")

There is also `events.add([event1, event2, event3...])` which is used in tandem with the `allow_nonexistent_events` parameter. This lets LiteEvent know which events exist and which don't. This is optional.
## Optional parameters
Currently, these are the parameters that can modify the behaviour of the `Events` instance:

 - `allow_nonexistent_events`:  This is `True` by default. When `False`, LiteEvent will raise an exception when an event handler for an event that hasn't been added is registered.
 - `allow_emitting_nonexistent_events`: This is `True` by default. When `False`, LiteEvent will raise an exception when an event that hasn't been added is emitted.

	
