import lcddriver
import time
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
display = lcddriver.lcd()
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('index.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('datos')
def datos(json, methods=['GET', 'POST']):
	print(str(json))
	display.lcd_clear()
	if len(str(json)) >16 and len(str(json)) <31:
		x=str(json)[0:16]
		y=str(json)[16:32]
		display.lcd_display_string(x,1)
		display.lcd_display_string(y,2)

	if len(str(json))>32:
		display.lcd_display_string('error',1)
		display.lcd_display_string('error',2)

	if len(str(json)) <16:
		display.lcd_display_string(str(json),1)

    





#try:

	#x= raw_input("introduce texto: ")
	#y= raw_input("Introduce mas texto; ")
# Main body of code

    	#while True:
        	# Remember that your sentences can only be 16 characters long!
        	#print("Writing to display")
        	#display.lcd_display_string(x, 1) # Write line of text to first line of display
        	#display.lcd_display_string(y, 2) # Write line of text to second line of display
        	#time.sleep(2)                                     # Give time for the message to be read
        	#display.lcd_display_string("Soy un display!", 1)  # Refresh the first line of display with a different message
        	#time.sleep(2)                                     # Give time for the message to be read
        	#display.lcd_clear()                               # Clear the display of any data
        	#time.sleep(2)                                     # Give time for the message to be read

#except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    #print("Cleaning up!")
    #display.lcd_clear()

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0',port=5000)
