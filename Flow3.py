[{"id":"eee2be39.a99c","type":"tab","label":"Flow 3","disabled":false,"info":""},{"id":"1484a196.ead7ae","type":"rpi-gpio in","z":"eee2be39.a99c","name":"","pin":"7","intype":"up","debounce":"25","read":false,"x":160,"y":240,"wires":[["acd17337.d8bc9","fded5637.2b3288"]]},{"id":"fded5637.2b3288","type":"switch","z":"eee2be39.a99c","name":"","property":"payload","propertyType":"msg","rules":[{"t":"eq","v":"0","vt":"str"},{"t":"eq","v":"1","vt":"str"}],"checkall":"true","repair":false,"outputs":2,"x":320,"y":260,"wires":[["90217959.35fbe8"],["bf626801.ad2de8"]]},{"id":"acd17337.d8bc9","type":"debug","z":"eee2be39.a99c","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":510,"y":160,"wires":[]},{"id":"2759143a.74880c","type":"rpi-gpio out","z":"eee2be39.a99c","name":"LED","pin":"29","set":"","level":"0","freq":"","out":"out","x":690,"y":280,"wires":[]},{"id":"90217959.35fbe8","type":"change","z":"eee2be39.a99c","name":"change to 0","rules":[{"t":"set","p":"payload","pt":"msg","to":"0","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":490,"y":240,"wires":[["2759143a.74880c"]]},{"id":"bf626801.ad2de8","type":"change","z":"eee2be39.a99c","name":"change to 1","rules":[{"t":"set","p":"payload","pt":"msg","to":"1","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":490,"y":320,"wires":[["2759143a.74880c"]]}]
