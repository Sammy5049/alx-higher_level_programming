#!/usr/bin/node

const { dict } = require('./101-data');

const convertArr = Object.entries(dict);

const newObj = {};

convertArr.forEach(element => {
  newObj[element[1]] ? newObj[element[1]].push(element[0]) : newObj[element[1]] = [element[0]];
});

console.log(newObj);