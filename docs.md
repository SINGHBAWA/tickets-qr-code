#Authorization

To use authorization we have to pass a value as a header.
Here we can get auth_token while login and use that token to authorize again and again.

__Syntax__
```
"Authorization": "Token auth_token"
```
##Login

POST api/scanner/auth/login

Login to electric soul app. It get or create a token associated with user. Subsequent requests should have `Authorization` header
with value `Token <token-key>`.

__Parameters__

Name | Type | Description
-----------|---------|---------------------------------------------
username | string | Email or Username of user.
password | string | Password for user.

__Response__

`200 Success`

```
{
"id": "d03b41fd-bbda-4099-8f79-e7834090e968",
"email": "test@example.com",
"username": "test",
"auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCMzQwOKkC_8r4E5JI-D61maN6F9HYlQ",
"fb_id": "",
"image": {
"thumbnail_small": "http://localhost:8000/media/__sized__/users/user/Ig2ypiIiR0ezxl9F4VtJ9g-thumbnail-90x90.jpg",
"thumbnail": "http://localhost:8000/media/__sized__/users/user/Ig2ypiIiR0ezxl9F4VtJ9g-thumbnail-210x210.jpg",
"full_size": "http://localhost:8000/media/users/user/Ig2ypiIiR0ezxl9F4VtJ9g.jpg"
},
"cover_image": {
"thumbnail": "http://localhost:8000/media/__sized__/users/user/QAwZk0CTR9W-FWDqmxPeag-thumbnail-400x400.jpg",
"full_size": "http://localhost:8000/media/users/user/QAwZk0CTR9W-FWDqmxPeag.jpg"
}
}
```

## Password Change

```
POST /api/me/password_change (requires authorization)
```

Change current user's password.

__Parameters__

Name | Type | Description
---------------|---------|---------------------------------------------
old_password | string | Current password of user.
new_password1 | string | New password for user.
new_password2 | string | New password again for user.

__Response__

`200 Success`

```
{
"success": "New password has been saved."
}
```




## Password Reset

```
POST /api/auth/password_reset
```

Reset password of user. It sends a verification email to the user's email with password reset link.

__Parameters__

Name | Type | Description
---------------|---------|---------------------------------------------
email | email | Email of user.

__Response__

`200 Success`
```
{"success":"Password reset e-mail has been sent."}
```



## Contact us

```
POST /api/scanner/scanner_contact
```

Name | Type | Description
---------------|---------|---------------------------------------------
email | email | Email of user.
first_name | string | valid string
last_name | string | Valid string
phone_number | string | Valid phone number
company | string | Valid string as name
message | string | valid string

__Response__

`200 Success`

```
{"success":True}
```




#Events

##List of all upcoming events: (authorization required)

```
GET api/scanner/events (requires authorization)
```

__Response__

```
{
  "status": true,
  "message": "",
  "events_upcoming": [...],
  "events_past": [
    {
      "id": "96674dd4-d8e2-427a-a931-086b12c6383f",
      "name": "Test Event",
      "cover_image": {
        "thumbnail_medium2": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-600x600-70.jpg",
        "full_size": "https://electric-soul-prod.s3.amazonaws.com/events/event/uphxBlHVT_-IB_wbMkcbIA.jpg",
        "thumbnail": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-400x400-70.jpg",
        "thumbnail_medium": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-800x800-70.jpg"
      },
      "start": "2019-11-11T23:31:00Z",
      "end": "2019-11-11T23:34:01Z",
      "description": "William Sami Étienne Grigahcine (French: [wiljam sami etjɛn ɡʁiɡasin]; born 13 June 1986), known professionally as DJ Snake, is a French DJ, record producer, and music programmer from Paris.\r\n\r\nDJ Snake debuted into the international scene with singles \"Bird Machine\" and \"Turn Down for What\" in 2013.[1][6][7] \"Bird Machine\" is a collaboration with fellow French musician Alesia. The single was picked up by Mad Decent, a Los Angeles-based record label run by Diplo, and released in February 2013. In June 2013, DJ Snake was invited by Diplo to do a live mix on his radio show, \"Diplo & Friends\", which airs on BBC Radio \r\n\r\nDJ Snake was announced to be working on a collaboration with Diplo, originally slated to debut in 2014; it eventually released in 2015 as the single \"Lean On\" in collaboration with MØ and Diplo's Major Lazer.[9][10][11] On 30 April 2014, DJ Snake was labeled as an \"Artist to Watch\" by FoxWeekly.[12] He and Dillon Francis were announced as alternating supporting artists for the summer Mothership Tour 2014 with Skrillex.[13] In March 2018, Billboard named DJ Snake as number nine on their 2018 ranking of dance musicians titled Billboard Dance 100.",
      "remark": null,
      "promoter": null,
      "address": {
        "id": "55580a9e-7d17-42e8-a752-de7a8cf9853f",
        "address1": "147 E. Pender St (at Main) in Chinatown, Vancouver, British Columbia V6A 1T5",
        "address2": null,
        "zipcode": null,
        "city": {
          "id": "7a90ed9a-2cb5-4e66-b2ba-a2052248444f",
          "name": "Vancouver",
          "city_code": "BC",
          "state": "British Columbia",
          "country": "Canada",
          "slug": "vancouver",
          "meta_title": "Vancouver Events - Electric Soul",
          "meta_description": "Vancouver - Discover all the upcoming Electronic Music Events in Vancouver. Get your EDM, House & Techno tickets with Electric Soul now.",
          "for_festival": false
        },
        "google_map_url": "https://www.google.com/maps/place/147+E.+Pender+St+%28at+Main%29+in+Chinatown%2C+Vancouver%2C+British+Columbia+V6A+1T5"
      },
      "attendees_count": 9,
      "meta_title": "DJ Snake 2020 - Vancouver - Electric Soul",
      "meta_description": "Find your tickets for DJ Snake. Attend the hottest Electronic Music Events and Festivals in Vancouver with Electric Soul now!",
      "total_tickets": 174,
      "used_tickets": 18,
      "event_type": "past"
    }
  ],
  "events_ongoing": [...]
}
```

##List of all upcoming events: (authorization required)

```
GET api/scanner/events_upcoming (requires authorization)
```

__Response__

```{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "96674dd4-d8e2-427a-a931-086b12c6383f",
      "name": "Test Event",
      "cover_image": {
        "thumbnail_medium2": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-600x600-70.jpg",
        "full_size": "https://electric-soul-prod.s3.amazonaws.com/events/event/uphxBlHVT_-IB_wbMkcbIA.jpg",
        "thumbnail": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-400x400-70.jpg",
        "thumbnail_medium": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-800x800-70.jpg"
      },
      "start": "2019-11-11T23:31:00Z",
      "end": "2019-11-11T23:34:01Z",
      "description": "William Sami Étienne Grigahcine (French: [wiljam sami etjɛn ɡʁiɡasin]; born 13 June 1986), known professionally as DJ Snake, is a French DJ, record producer, and music programmer from Paris.\r\n\r\nDJ Snake debuted into the international scene with singles \"Bird Machine\" and \"Turn Down for What\" in 2013.[1][6][7] \"Bird Machine\" is a collaboration with fellow French musician Alesia. The single was picked up by Mad Decent, a Los Angeles-based record label run by Diplo, and released in February 2013. In June 2013, DJ Snake was invited by Diplo to do a live mix on his radio show, \"Diplo & Friends\", which airs on BBC Radio \r\n\r\nDJ Snake was announced to be working on a collaboration with Diplo, originally slated to debut in 2014; it eventually released in 2015 as the single \"Lean On\" in collaboration with MØ and Diplo's Major Lazer.[9][10][11] On 30 April 2014, DJ Snake was labeled as an \"Artist to Watch\" by FoxWeekly.[12] He and Dillon Francis were announced as alternating supporting artists for the summer Mothership Tour 2014 with Skrillex.[13] In March 2018, Billboard named DJ Snake as number nine on their 2018 ranking of dance musicians titled Billboard Dance 100.",
      "remark": null,
      "promoter": null,
      "address": {
        "id": "55580a9e-7d17-42e8-a752-de7a8cf9853f",
        "address1": "147 E. Pender St (at Main) in Chinatown, Vancouver, British Columbia V6A 1T5",
        "address2": null,
        "zipcode": null,
        "city": {
          "id": "7a90ed9a-2cb5-4e66-b2ba-a2052248444f",
          "name": "Vancouver",
          "city_code": "BC",
          "state": "British Columbia",
          "country": "Canada",
          "slug": "vancouver",
          "meta_title": "Vancouver Events - Electric Soul",
          "meta_description": "Vancouver - Discover all the upcoming Electronic Music Events in Vancouver. Get your EDM, House & Techno tickets with Electric Soul now.",
          "for_festival": false
        },
        "google_map_url": "https://www.google.com/maps/place/147+E.+Pender+St+%28at+Main%29+in+Chinatown%2C+Vancouver%2C+British+Columbia+V6A+1T5"
      },
      "attendees_count": 9,
      "meta_title": "DJ Snake 2020 - Vancouver - Electric Soul",
      "meta_description": "Find your tickets for DJ Snake. Attend the hottest Electronic Music Events and Festivals in Vancouver with Electric Soul now!",
      "total_tickets": 174,
      "used_tickets": 18,
      "event_type": "upcoming"
    }
  ]
}
```






##List of all upcoming events (authorization required)

```
GET api/scanner/events_past
```

__Response__

```
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "96674dd4-d8e2-427a-a931-086b12c6383f",
      "name": "Test Event",
      "cover_image": {
        "thumbnail_medium2": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-600x600-70.jpg",
        "full_size": "https://electric-soul-prod.s3.amazonaws.com/events/event/uphxBlHVT_-IB_wbMkcbIA.jpg",
        "thumbnail": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-400x400-70.jpg",
        "thumbnail_medium": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-800x800-70.jpg"
      },
      "start": "2019-11-11T23:31:00Z",
      "end": "2019-11-11T23:34:01Z",
      "description": "William Sami Étienne Grigahcine (French: [wiljam sami etjɛn ɡʁiɡasin]; born 13 June 1986), known professionally as DJ Snake, is a French DJ, record producer, and music programmer from Paris.\r\n\r\nDJ Snake debuted into the international scene with singles \"Bird Machine\" and \"Turn Down for What\" in 2013.[1][6][7] \"Bird Machine\" is a collaboration with fellow French musician Alesia. The single was picked up by Mad Decent, a Los Angeles-based record label run by Diplo, and released in February 2013. In June 2013, DJ Snake was invited by Diplo to do a live mix on his radio show, \"Diplo & Friends\", which airs on BBC Radio \r\n\r\nDJ Snake was announced to be working on a collaboration with Diplo, originally slated to debut in 2014; it eventually released in 2015 as the single \"Lean On\" in collaboration with MØ and Diplo's Major Lazer.[9][10][11] On 30 April 2014, DJ Snake was labeled as an \"Artist to Watch\" by FoxWeekly.[12] He and Dillon Francis were announced as alternating supporting artists for the summer Mothership Tour 2014 with Skrillex.[13] In March 2018, Billboard named DJ Snake as number nine on their 2018 ranking of dance musicians titled Billboard Dance 100.",
      "remark": null,
      "promoter": null,
      "address": {
        "id": "55580a9e-7d17-42e8-a752-de7a8cf9853f",
        "address1": "147 E. Pender St (at Main) in Chinatown, Vancouver, British Columbia V6A 1T5",
        "address2": null,
        "zipcode": null,
        "city": {
          "id": "7a90ed9a-2cb5-4e66-b2ba-a2052248444f",
          "name": "Vancouver",
          "city_code": "BC",
          "state": "British Columbia",
          "country": "Canada",
          "slug": "vancouver",
          "meta_title": "Vancouver Events - Electric Soul",
          "meta_description": "Vancouver - Discover all the upcoming Electronic Music Events in Vancouver. Get your EDM, House & Techno tickets with Electric Soul now.",
          "for_festival": false
        },
        "google_map_url": "https://www.google.com/maps/place/147+E.+Pender+St+%28at+Main%29+in+Chinatown%2C+Vancouver%2C+British+Columbia+V6A+1T5"
      },
      "attendees_count": 9,
      "meta_title": "DJ Snake 2020 - Vancouver - Electric Soul",
      "meta_description": "Find your tickets for DJ Snake. Attend the hottest Electronic Music Events and Festivals in Vancouver with Electric Soul now!",
      "total_tickets": 174,
      "used_tickets": 18,
      "event_type": "past"
    }
  ]
}
```



##List of all ongoing events (authorization required)
```
GET api/scanner/events_ongoing
```

__Response__

```
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "96674dd4-d8e2-427a-a931-086b12c6383f",
      "name": "Test Event",
      "cover_image": {
        "thumbnail_medium2": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-600x600-70.jpg",
        "full_size": "https://electric-soul-prod.s3.amazonaws.com/events/event/uphxBlHVT_-IB_wbMkcbIA.jpg",
        "thumbnail": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-400x400-70.jpg",
        "thumbnail_medium": "https://electric-soul-prod.s3.amazonaws.com/__sized__/events/event/uphxBlHVT_-IB_wbMkcbIA-thumbnail-800x800-70.jpg"
      },
      "start": "2019-11-11T23:31:00Z",
      "end": "2019-11-11T23:34:01Z",
      "description": "William Sami Étienne Grigahcine (French: [wiljam sami etjɛn ɡʁiɡasin]; born 13 June 1986), known professionally as DJ Snake, is a French DJ, record producer, and music programmer from Paris.\r\n\r\nDJ Snake debuted into the international scene with singles \"Bird Machine\" and \"Turn Down for What\" in 2013.[1][6][7] \"Bird Machine\" is a collaboration with fellow French musician Alesia. The single was picked up by Mad Decent, a Los Angeles-based record label run by Diplo, and released in February 2013. In June 2013, DJ Snake was invited by Diplo to do a live mix on his radio show, \"Diplo & Friends\", which airs on BBC Radio \r\n\r\nDJ Snake was announced to be working on a collaboration with Diplo, originally slated to debut in 2014; it eventually released in 2015 as the single \"Lean On\" in collaboration with MØ and Diplo's Major Lazer.[9][10][11] On 30 April 2014, DJ Snake was labeled as an \"Artist to Watch\" by FoxWeekly.[12] He and Dillon Francis were announced as alternating supporting artists for the summer Mothership Tour 2014 with Skrillex.[13] In March 2018, Billboard named DJ Snake as number nine on their 2018 ranking of dance musicians titled Billboard Dance 100.",
      "remark": null,
      "promoter": null,
      "address": {
        "id": "55580a9e-7d17-42e8-a752-de7a8cf9853f",
        "address1": "147 E. Pender St (at Main) in Chinatown, Vancouver, British Columbia V6A 1T5",
        "address2": null,
        "zipcode": null,
        "city": {
          "id": "7a90ed9a-2cb5-4e66-b2ba-a2052248444f",
          "name": "Vancouver",
          "city_code": "BC",
          "state": "British Columbia",
          "country": "Canada",
          "slug": "vancouver",
          "meta_title": "Vancouver Events - Electric Soul",
          "meta_description": "Vancouver - Discover all the upcoming Electronic Music Events in Vancouver. Get your EDM, House & Techno tickets with Electric Soul now.",
          "for_festival": false
        },
        "google_map_url": "https://www.google.com/maps/place/147+E.+Pender+St+%28at+Main%29+in+Chinatown%2C+Vancouver%2C+British+Columbia+V6A+1T5"
      },
      "attendees_count": 9,
      "meta_title": "DJ Snake 2020 - Vancouver - Electric Soul",
      "meta_description": "Find your tickets for DJ Snake. Attend the hottest Electronic Music Events and Festivals in Vancouver with Electric Soul now!",
      "total_tickets": 174,
      "used_tickets": 18,
      "event_type": "ongoing"
    }
  ]
}
```




##To scan the ticket and marked as checked in (authorization required)
```
POST api/scanner/scan_ticket
```

__Parameters__

Name              | Type     | Description
------------------|----------|------------------
event_id          | string   | valid event id
scanner_event_id  | string   | valid event id
ticket_id         | string   | valid ticket id for an event


__Response__

`200 Success`

```
{

    "status":true,
    "tokens_left":0,
    "checkin_time":"2019-06-20T14:57:48.745144Z",
    "event":{
        "start":"2019-06-21T10:41:28Z",
        "end":"2019-06-23T19:18:33Z",
        "address":{
            "address1":"Newyork city",
            "address2":"NY",
            "google_map_url":"https://www.google.com/maps",
            "zipcode":"134544",
            "city":"NewYork"
        }
    },
    "message":"",
    "ticket":{
        "city":"yfhfhfhf",
        "contact_number":"353535",
        "dob":null,
        "country":"hfhfhfyfyf",
        "state":"fufyuf",
        "address":"hfyfyfy",
        "id":"tuttu"
    },
    "attandee":{
        "email":"amansinghbawa@gmail.com",
        "id":"e59be30b-9292-40ba-aef8-d245125428be",
        "name":" "
    },
    "organiser":"Aman Singh "

}
```



##To scan the ticket and marked as checked in (authorization required)

```
POST api/scanner/ticket_details
```

__Parameters__

Name | Type | Description
--------------|----------|---------------------------------------------
ticket_id | string | valid ticket id for an event


__Response__

`200 Success`

```
{

    "status":true,
    "tokens_left":0,
    "checkin_time":"2019-06-20T14:57:48.745144Z",
    "event":{
        "start":"2019-06-21T10:41:28Z",
        "end":"2019-06-23T19:18:33Z",
        "address":{
            "address1":"Newyork city",
            "address2":"NY",
            "google_map_url":"https://www.google.com/maps",
            "zipcode":"134544",
            "city":"NewYork"
        }
    },
    "message":"",
    "ticket":{
        "city":"yfhfhfhf",
        "contact_number":"353535",
        "dob":null,
        "country":"hfhfhfyfyf",
        "state":"fufyuf",
        "address":"hfyfyfy",
        "id":"tuttu"
    },
    "attandee":{
        "email":"amansinghbawa@gmail.com",
        "id":"e59be30b-9292-40ba-aef8-d245125428be",
        "name":" "
    },
    "organiser":"Aman Singh "

}
```



##To scan the drinks QR code and get the purchased drinks (authorization required)
POST api/scanner/scan_drinks



__Parameters__

Name | Type | Description
-------------------------------|----------|---------------------------------------------
event_id | string | valid event id
scanner_event_id | string | valid event id
wallet_transaction_id | string | valid wallet_transaction_id

__Response__

`200 Success`

```
{

    "count":2,
    "next":null,
    "previous":null,
    "results":[
        {
            "id":"2ad1ee7f-0e32-4139-975c-0d901ff0d1d6",
            "drink_item":null,
            "drink_menu":{
                "id":"f47d20b1-ca6a-4619-94e9-a50592d48eec",
                "name":"Special style"
            },
            "quantity":3,
            "token":3,
            "status":"COM"
        },
        {
            "id":"2d66885c-e379-4f78-8800-a54696e019ab",
            "drink_item":{
                "id":"63561d7f-c76d-4450-926a-b7477d5188cb",
                "name":"Coke"
            },
            "drink_menu":null,
            "quantity":2,
            "token":5,
            "status":"COM"
        }
    ]

}
```
__Response__

`400 Bad Request`

```
{
    "status": false,
    "message": "Already Redeemed @ 2019-06-20 11:33:27.295863+00:00"
}
```




##List of all guest users (authorization required)

```
GET /api/scanner/event_guest?event_id=<event-id>
```
__Response__

`200 Success`

```
{

    "count":3,
    "result":[
        {
            "status":"manual",
            "first_name":"Shiv",
            "last_name":"shankar",
            "ticket_type":"Guest",
            "email":"shiv@yopmail.com",
            "id":"8c0e78c4-5732-447f-88ad-6bf12755c52c"
        },
        {
            "status":"manual",
            "first_name":"Chandigarh",
            "last_name":"Kumar",
            "ticket_type":"Guest",
            "email":"abu@yopmail.com",
            "id":"6091ae2b-d0fa-4b70-99bb-519302eb4fea"
        },
        {
            "status":"manual",
            "first_name":"Durga",
            "last_name":"Prasad",
            "ticket_type":"Guest",
            "email":"prasad@yopmail.com",
            "id":"445bc859-5dc6-4d5e-9547-02a752f4d342"
        }
    ],
    "success":true

}
```


##Scanner scanned tokens for an event (Transaction History) (authorization required)

```
GET /api/scanner/scanner_transactions
```
__Parameters__

   Name | Type | Description
--------------|----------|---------------------------------------------
event_id | string | valid event id

__Response__

`200 Success`

```
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "6b0cb314-4865-4cdd-8e08-e1d2993870eb",
      "wallet_transaction": {
        "id": "0e7dab5e-dae2-4cdc-b32f-77fd83951543",
        "token": 1,
        "wallet": {
          "token": 47
        },
        "status": true,
        "qrcode": "http://api.qrserver.com/v1/create-qr-code/?size=100x100&data={\"wallet_transaction_id\":\"0e7dab5e-dae2-4cdc-b32f-77fd83951543\",\"event_id\":\"96674dd4-d8e2-427a-a931-086b12c6383f\"}",
        "created": "2019-10-31T12:12:29.720812Z",
        "drinks": [
          {
            "token": 1,
            "name": "burger",
            "quantity": 1
          }
        ],
        "drink_status": "completed"
      },
      "created": "2019-10-31T12:12:33.735420Z",
      "modified": "2019-10-31T12:12:33.737301Z",
      "token": 1,
      "scanner": "64ff3009-8115-4a05-9580-335d3b40b2b4",
      "guest_user": "b80617e5-4bc5-4529-9595-1f50cba491e5",
      "event": "96674dd4-d8e2-427a-a931-086b12c6383f"
    }
  ]
}
```

##User’s spent tokens for an event (Transaction History) (authorization required)

```
GET /api/scanner/user_transactions
```

__Parameters__

   Name | Type | Description
--------------|----------|---------------------------------------------
event_id | string | valid event id
attandee_id | string | valid user id who is attending the event



__Response__

`200 Success`

```
{

    "count":8,
    "next":"http://127.0.0.1:8000/api/scanner/user_transactions?attandee_id=e59be30b929240baaef8d245125428be&event_id=eee33372-786d-4bd4-8714-ae7cf726ddeb&page=3&per_page=2",
    "previous":"http://127.0.0.1:8000/api/scanner/user_transactions?attandee_id=e59be30b929240baaef8d245125428be&event_id=eee33372-786d-4bd4-8714-ae7cf726ddeb&per_page=2",
    "results":[
        {
            "id":"0d8debdf-4b87-4b4e-b163-76cf80f2e5c1",
            "created":"2019-06-20T13:16:10.557013Z",
            "modified":"2019-06-20T13:16:10.561118Z",
            "token":47,
            "scanner":"e59be30b-9292-40ba-aef8-d245125428be",
            "guest_user":"e59be30b-9292-40ba-aef8-d245125428be",
            "event":"eee33372-786d-4bd4-8714-ae7cf726ddeb"
        },
        {
            "id":"c3db8f7d-b7bb-493a-83b5-f33abc07a596",
            "created":"2019-06-20T13:23:38.587200Z",
            "modified":"2019-06-20T13:23:38.597669Z",
            "token":47,
            "scanner":"e59be30b-9292-40ba-aef8-d245125428be",
            "guest_user":"e59be30b-9292-40ba-aef8-d245125428be",
            "event":"eee33372-786d-4bd4-8714-ae7cf726ddeb"
        }
    ]

}
```


## Scan guest user
```
POST /api/scanner/scan_guest_user
```

__Parameters__


   Name | Type | Description
--------------|----------|---------------------------------------------
event_id | string | valid event id
guest_id | string | valid user id who is attending the event
guest_type | string | valid  type of user who is attending the event (manual / app_user)


__RESPONSE__


`Status 200`

```
{
    "status": true,
    "message": "scanned successfully !!!",
}
```

