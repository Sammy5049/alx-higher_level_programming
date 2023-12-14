#!/usr/bin/node

const nbOccur = (list, searchElement) => list.filter((element) => searchElement === element).length;

module.exports = { nbOccur };