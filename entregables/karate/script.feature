Feature: API Testing SW 1 - GRUPO SIGNTALK
Scenario:
    * url 'https://httpbin.org/anything'
    * request { myKey: 'myValue' }
    * method post
    * status 200 
    * match response.json == { myKey: 'myValue' } 