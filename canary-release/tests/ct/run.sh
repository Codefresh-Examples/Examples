#! /bin/sh -x
# Component test for the products service.
# Very dumb - create an product and verify there's an product for this product id.
# Assumes a fresh environment

curl -s -X POST -H "Content-Type:application/json" -d '{"name": "Black Cockatoo", "clade_id": 13, "habitat": "Australia", "population" : 30000 }' http://${APP_URL}:5000/specie
curl -s http://${APP_URL}:5000/specie | grep Cockatoo
