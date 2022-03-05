# Mouse-and-Keyboard
## Event
* Happens while program is running
* Comes from outside the program
* Code reacts to the event
* Events include: * Quit button pressed (pygame.QUIT event) * Mouse clicked * Keyboard button pressed
## Events caused by mouse input
* pygame.MOUSEBUTTONDOWN when mouse button is clicked
* pygame.MOUSEBUTTONUP when mouse button is released
* Separate events because code might react differently
* Example: dragging has different behavior on mousedown and mouseup
## Other mouse based data that can be received
* bool_var = pygame.mouse.get_presed() gets whether the mouse button is being held down
* x, y = pygame.mouse.get_pos() gets the position of the mouse cursor
* pygame.mouse.set_visible(bool_var) sets the cursor to be visible or invisible (depending on boolean argument)
## Events caused by key input
* pygame.KEYDOWN when key is pressed
* pygame.KEYUP when key is released
* Caused by ANY key on the keyboard
* For specific keys, get more key-based data
## Other key-based data
* event.key contains which key was used in a key event
* Both require using key constants
* get_key_pressed takes a key constant as an argument
* get_key_pressed requires importing the tsk library
* event.key is tested to see if it's equal to a key constant
* event.key can only be used inside the event loop
## Constant
* Variable name in ALLCAPS
* Value inside constant doesn't change
* Name makes it easier to refer to
* Used for key names
* Used for event types
## Key constants
* Usually start with "K_" and then key name
* K_DOWN - down arrow
* K_UP - up arrow
* K_RIGHT - right arrow
* K_LEFT - left arrow
* K_RETURN - enter key
* K_SPACE - spacebar
* K_letter - a letter key (substitute "letter" with the key in question)
* K_number - a number key (substitute "number" with the key in question)
