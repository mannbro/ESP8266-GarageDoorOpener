from utime import sleep_ms
from uselect import select

#The HTML that is returned if you go to /
def webPage():
  contentType='text/html'
  
  html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Garage Door</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="apple-touch-icon" sizes="128x128" href="data:image/png;base64,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"> 
            <style>
                html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                body{background-color: #1A2238;}
                p{font-size: 1.5rem;}
                .button{
                        display: block;
                        background-color: #FF6A3D;
                        border: none;
                        color: white;
                        width: 60vw;
                        height: 60vw;
                        border-radius: 40vw;
                        left: 20vw;
                        top: calc(40vh - 30vw);
                        font-size: 8vw;
                        cursor: pointer;
                        position: absolute;
                }
                .button:disabled{
                    background-color: #cccccc;
                }
                @media screen and (orientation: landscape) {
                    .button {
                        width: 60vh;
                        height: 60vh;
                        border-radius: 40vh;
                        left: calc(50vw - 30vh);
                        top: 10vh;
                        font-size: 8vh;
                    }
                }
        </style>
            <script>
                function controlRelay(command) {
                    controlButton=document.getElementById('controlbutton');
                    if(controlButton.disabled)
                        return;

                    controlButton.disabled=true;
                    fetch('/?'+command);
                    setTimeout(function(controlButton){
                        controlButton.disabled=false;    
                    }, 1000, controlButton)

                }
            </script>
        </head>
        <body>
            <button id="controlbutton" onclick="controlRelay('operateDoor');" class="button">START/STOP</button>
        </body>
    </html>"""
  return html, contentType

#The JSON return, for now hardcoded to success.
def startDoor():
    print('OPERATING DOOR...')
    led.value(0)
    relay.value(0)
    sleep_ms(500)
    led.value(1)
    relay.value(1)
    print('DONE')
    json='{"Success": true}'
    contentType='application/json'
    return json, contentType

#Handle an incoming request
def handleRequest(conn, address):
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)


    operateDoor=request.find('/?operateDoor')==6

    #If the request is to operate the door, start the door
    #Else show the webpage
    if(operateDoor):
        response, contentType = startDoor()
    else:
        response, contentType = webPage()
        
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: '+contentType+'\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

#Set up a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#Main Loop
while True:

    #The ESP8266 tends to drop connections, so check if wifi is connected, if not, reconnect
    if wifi.isconnected() == False:
        print('Connecting wifi...')
        connectWifi()

    #Handle incoming HTTP requests in a non-blocking way
    r, w, err = select((s,), (), (), 1)

    #Is there an incoming request? If so, handle the request
    if r:
        for readable in r:
            conn, addr = s.accept()
            try:
                handleRequest(conn, addr)
            except OSError as e:
                pass

    #Blink the LED each loop cycle too indicate that everything is OK
    led.value(0)
    sleep_ms(100)
    led.value(1)
    sleep_ms(400)
