#!/usr/bin/node
const fsc = require('fs');

const fArg = fsc.readFileSync(process.argv[2]).toString();
const sArg = fsc.readFileSync(process.argv[3]).toString();
fsc.writeFileSync(process.argv[4], fArg + sArg);