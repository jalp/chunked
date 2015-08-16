# Chunked
Minimal code to test transfer coding chuncked. Flask is not able to obtain the body information with header
  Transfer-encoding: chunked

## Testing
Firstly, run it:
  docker-compose build && docker-compose up -d

Curl commnand (change the ip to your docker-machine ip):
  curl -XPOST http://192.168.99.101/items -d @d.json -H"Content-type:application/json" -H"Transfer-encoding: chunked" -v
It should return in logs:
  web_1   | INFO in app [app.py:15]:
  web_1   | b'{"markers": [\t\t{\t\t\t"point":new GLatLng(40.266044,-74.718479), \t\t\t"homeTeam":"Lawrence Library",\t\t\t"awayTeam":"LUGip",\t\t\t"markerImage":"images/red.png",\t\t\t"information": "Linux users group meets second Wednesday of each month.",\t\t\t"fixture":"Wednesday 7pm",\t\t\t"capacity":"",\t\t\t"previousScore":""\t\t},\t\t{\t\t\t"point":new GLatLng(40.211600,-74.695702),\t\t\t"homeTeam":"Hamilton Library",\t\t\t"awayTeam":"LUGip HW SIG",\t\t\t"markerImage":"images/white.png",\t\t\t"information": "Linux users can meet the first Tuesday of the month to work out harward and configuration issues.",\t\t\t"fixture":"Tuesday 7pm",\t\t\t"capacity":"",\t\t\t"tv":""\t\t},\t\t{\t\t\t"point":new GLatLng(40.294535,-74.682012),\t\t\t"homeTeam":"Applebees",\t\t\t"awayTeam":"After LUPip Mtg Spot",\t\t\t"markerImage":"images/newcastle.png",\t\t\t"information": "Some of us go there after the main LUGip meeting, drink brews, and talk.",\t\t\t"fixture":"Wednesday whenever",\t\t\t"capacity":"2 to 4 pints",\t\t\t"tv":""\t\t},] }'
  web_1   | --------------------------------------------------------------------------------
  web_1   | 172.17.0.70 - - [16/Aug/2015 21:14:57] "POST /items HTTP/1.1" 200 -

If you call directly Flask:
  curl -XPOST http://192.168.99.101:5000/items -d @d.json -H"Content-type:application/json" -H"Transfer-encoding: chunked" -v
the result is quite different:
  web_1   | INFO in app [app.py:15]:
  web_1   | b''
  web_1   | --------------------------------------------------------------------------------
  web_1   | 192.168.99.1 - - [16/Aug/2015 21:28:27] "POST /items HTTP/1.1" 200 -
## Solution
Nginx is able to solve it only indicating:
  proxy_http_version 1.1;
or even with:
  proxy_buffering off;
