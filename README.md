# tama-web
## URL
- development: 192.168.1.76

## API
### Test
#### Request
```
GET /api HTTP/1.1
Host: 192.168.1.76
User-Agent: curl/7.64.1
Accept: */*
```

#### Response
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 31
Server: Werkzeug/1.0.1 Python/3.7.4
Date: Mon, 16 Nov 2020 04:38:05 GMT

{
  "message": "hello world"
}
```

#### Sample
```
 curl 192.168.1.76/api
```

### Passages
#### Request
```
POST /api/passages HTTP/1.1
Host: 192.168.1.76
User-Agent: curl/7.64.1
Accept: */*
Content-Length: 217
Content-Type: multipart/form-data; boundary=------------------------a8d4592c429e51b4

Filename: passage
```

#### Sample
```
 curl -X POST -F passage=@./sample.csv 192.168.1.76/api/passages
```

#### Response
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 7
Server: Werkzeug/1.0.1 Python/3.7.4
Date: Mon, 16 Nov 2020 04:26:06 GMT

{
  "message": "success"
}
```

### Trajectories
#### Request
```
POST /api/trajectories HTTP/1.1
Host: 192.168.1.76
User-Agent: curl/7.64.1
Accept: */*
Content-Length: 220
Content-Type: multipart/form-data; boundary=------------------------0a0ab684e769e9fe

Filename: trajectory
```

#### Sample
```
 curl -X POST -F trajectory=@./sample.csv 192.168.1.76/api/trajectories
```

#### Response
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/1.0.1 Python/3.7.4
Date: Mon, 16 Nov 2020 04:36:00 GMT

{
  "message": "success"
}
```

## File Format
### Passage
#### Format
```
name: string
xbegin: float  # x coordinate of beginning of this passage 
ybegin: float  # y coordinate of beginning of this passage
xend: float  # x coordinate of end of this passage
yend: float  # y coordinate of end of this passage
```

#### Sample
```
name,xbegin,ybegin,xend,yend
p0,0,0,-9.19,0
p1,0,0,0,8.81
p2,-3.12,0,-3.12,8.81
p3,-6.23,0,-6.23,8.14
p4,-9.23,0,-9.23,7.48
p5,-9.23,0.29,-15.48,0.29
p6,-9.23,2.69,-15.48,2.69
p7,-10.71,2.69,-10.71,6.69
p8,-10.71,4.5,-15.41,4.5
p9,-10.71,6.73,-15.41,6.73
p10,-15.41,4.5,-15.41,6.73
p11,-6.23,7.48,-9.23,7.48
p12,-3.12,8.14,-6.23,8.14
p13,0,8.81,-3.12,8.81
```

### Trajectory
#### Format
```
time: string
x: float
y: float
z: float
rssi: float
```

#### Sample
```
time,x,y,z,rssi
20:13:0:323,0,0,0
20:13:0:828,0,0,0
20:13:1:326,0,0,0
20:13:1:828,0.004244604,0.2383296,0.06238639
20:13:2:323,0.03010574,0.4804483,0.09722187
20:13:2:826,0.03604501,0.6682818,0.176365
20:13:3:327,0.06094734,0.8935412,0.2170048
20:13:3:820,0.06315795,1.186143,0.2163748
20:13:4:302,0.1238422,1.460158,0.2108815
20:13:4:802,0.1657804,1.745667,0.2265325
20:13:5:299,0.1618076,1.989787,0.2164187
20:13:5:799,0.2084528,2.24684,0.185979
```
