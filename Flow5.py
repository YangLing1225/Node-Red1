[{"id":"c79a8309.14fa6","type":"tab","label":"Flow 5","disabled":false,"info":""},{"id":"5d618ea7.db66c","type":"inject","z":"c79a8309.14fa6","name":"","topic":"","payload":"","payloadType":"date","repeat":"5","crontab":"","once":true,"onceDelay":0.1,"x":130,"y":160,"wires":[["d96aef84.77272"]]},{"id":"d96aef84.77272","type":"function","z":"c79a8309.14fa6","name":"Payload","func":"msg.headers={\n    deviceKey:\"PoTAOlvLBK5U9FUr\"\n};\nmsg.payload = \"Temperature,,12\";\nreturn msg;","outputs":1,"noerr":0,"x":300,"y":160,"wires":[["736c17ef.5afdd8"]]},{"id":"736c17ef.5afdd8","type":"http request","z":"c79a8309.14fa6","name":"","method":"POST","ret":"txt","paytoqs":false,"url":"https://api.mediatek.com/mcs/v2/devices/Dw50zW9r/datapoints.csv","tls":"","proxy":"","authType":"","x":480,"y":160,"wires":[["353c4f3f.40884","acfed9d5.b04568"]]},{"id":"353c4f3f.40884","type":"http response","z":"c79a8309.14fa6","name":"","statusCode":"","headers":{},"x":640,"y":160,"wires":[]},{"id":"acfed9d5.b04568","type":"debug","z":"c79a8309.14fa6","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":640,"y":260,"wires":[]}]
