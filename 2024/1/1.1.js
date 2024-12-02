nums = require('fs').readFileSync(0).toString().split('\n').slice(0, -1)
let [a, b] = [0, 1].map(i => nums.map(n => n.split('   ')[i]).sort())
console.log(a.map((e, i) => Math.abs(e - b[i])).reduce((x, y) => x+y))
