[{"id":"6d1379ff.9a1bb8","type":"tab","label":"Flow 4","disabled":false,"info":""},{"id":"65c4b5b2.34eb6c","type":"inject","z":"6d1379ff.9a1bb8","name":"","topic":"","payload":"","payloadType":"date","repeat":"5","crontab":"","once":true,"onceDelay":0.1,"x":210,"y":160,"wires":[["42616c16.3f1e94"]]},{"id":"42616c16.3f1e94","type":"function","z":"6d1379ff.9a1bb8","name":"Payload","func":"msg.headers={\n    deviceKey:\"PoTAOlvLBK5U9FUr\"\n};\nreturn msg;","outputs":1,"noerr":0,"x":380,"y":160,"wires":[["6b193195.eacfd"]]},{"id":"6b193195.eacfd","type":"http request","z":"6d1379ff.9a1bb8","name":"","method":"GET","ret":"txt","paytoqs":false,"url":"http://api.mediatek.com/mcs/v2/devices/Dw50zW9r/datachannels/Temperature/datapoints.csv","tls":"","proxy":"","authType":"","x":560,"y":160,"wires":[["f9b254c.0d94da8","c95aae3e.56e58"]]},{"id":"f9b254c.0d94da8","type":"http response","z":"6d1379ff.9a1bb8","name":"","statusCode":"","headers":{},"x":720,"y":160,"wires":[]},{"id":"c95aae3e.56e58","type":"debug","z":"6d1379ff.9a1bb8","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":720,"y":260,"wires":[]}]
