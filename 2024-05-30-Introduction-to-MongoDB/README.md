# Introduction to MongoDB

Supportive material for my *Introduction to MongoDB* talk at Gen™ from 2024-05-30.

* [Slides](https://github.com/s3rvac/talks/raw/master/2024-05-30-Introduction-to-MongoDB/slides.pdf)
* Examples: See below.

## Installation

Note: The following instructions are for Ubuntu 22.04. If you use a different OS, please [download](https://www.mongodb.com/try/download/community) the appropriate binaries instead.

Download the `mongod` server:
```bash
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2204-7.0.11.tgz
tar xf mongodb-linux-x86_64-ubuntu2204-7.0.11.tgz
```

Download the `mongosh` client:
```bash
mkdir mongosh
cd mongosh
wget https://downloads.mongodb.com/compass/mongodb-mongosh_2.2.6_amd64.deb
ar x mongosh/mongodb-mongosh_2.2.6_amd64.deb
tar xf data.tar.xz
cd ..
```

Download the `mongoimport` tool for importing a dataset:
```bash
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2204-x86_64-100.9.4.tgz
tar xf mongodb-database-tools-ubuntu2204-x86_64-100.9.4.tgz
```

## Running the server

```bash
mongodb-linux-x86_64-ubuntu2204-7.0.11/bin/mongod --config mongod.conf
```
where `mongod.conf` is [this file](mongod.conf).

## Loading a sample database

```bash
wget https://raw.githubusercontent.com/neelabalan/mongodb-sample-dataset/main/sample_supplies/sales.json
mongodb-database-tools-ubuntu2204-x86_64-100.9.4/bin/mongoimport -d test -c sales sales.json
```

## Connecting to the server

```bash
mongosh/usr/bin/mongosh
```

## Example queries

Basics:
```javascript
use test
db.people.insertOne({name: "John Doe", age: 32})
db.people.insertOne({name: "Jane Doe", favoriteColors: ["green", "yellow"]})
db.people.find()
db.people.findOne({_id: ObjectId("[..]")}) // Use the ObjectID from the first record
db.people.find({}, {_id: 0, name: 1}) // Projection
db.people.updateOne({_id: ObjectId("[..]")}, {$set: {age: 33}})
db.people.updateOne({_id: ObjectId("[..]")}, {$inc: {age: 1}})
db.people.deleteOne({_id: ObjectId("[..]")})
```

Getting the time when a record was inserted:
```javascript
record = ...
record._id.getTimestamp()
```

Getting all sales in Denver by people under 30:
```javascript
db.sales.find({storeLocation: "Denver", "customer.age": {$lt: 30}})
db.sales.find({storeLocation: "Denver", "customer.age": {$lt: 30}}).count()
```

Getting all sales where a laptop was purchased:
```javascript
db.sales.find({"items.name": "laptop"})
```

Getting the total price for all sold laptops:
```javascript
db.sales.aggregate([
    // Create a single document for each item (recall that `items` is an array).
    {$unwind: "$items"},
    // Keep only laptops.
    {$match: {"items.name": "laptop"}},
    // Obtain the total price.
    {$group: {_id: "result", total: {$sum: {$multiply: ["$items.quantity", "$items.price"]}}}}
])
```

## Indexes

Getting indexes for a collection:
```javascript
db.sales.getIndexes()
```

Analyzing a query:
```javascript
db.sales.find({storeLocation: "Denver"}).explain()
```

Adding an index on `storeLocation`:
```javascript
db.sales.createIndex({storeLocation: 1})
```

Re-analyzing the query:
```javascript
db.sales.find({storeLocation: "Denver"}).explain()
```

Obtaining execution statistics (e.g. how long the query took):
```javascript
db.sales.find({storeLocation: "Denver"}).explain("executionStats")
```
