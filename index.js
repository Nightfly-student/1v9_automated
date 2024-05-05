const express = require('express');

const app = express();
const port = 8080 || process.env.PORT;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('1v9 automated acc checker');
});

app.listen(port, () => {
  console.log(`Example app listening at ${port}`);
});

app.post('/check', async (req, res) => {
  var csv;
  const { spawn } = require('child_process');

  const python = spawn('python', [
    __dirname + '/script/slc.py',
    req.body.region,
    req.body.user,
  ]);

  python.stdout.on('data', (data) => {
    const holder = data.toString();
    if (data !== null && holder.length > 0 && holder.includes('R')) {
      csv = data.toString();
    }
  });

  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    console.log(csv);

    res.send(csvJSON(csv));
  });
});

function csvJSON(csv) {
  var lines = csv.split('\n');

  var result = [];

  var headers = lines[0].split(',');

  for (var i = 1; i < lines.length; i++) {
    var obj = {};
    var currentline = lines[i].split(',');

    for (var j = 0; j < headers.length; j++) {
      obj[headers[j].replaceAll(' ', '')] = currentline[j];
    }

    result.push(obj);
  }

  //return result; //JavaScript object

  if (result.length === 0 || (result[0] && result[0].EmailStatus)) {
    return null;
  }

  return {
    region: result[0].Region,
    access: result[0].EmailStatus.toUpperCase(),
    characters: result[0].Champions,
    skins: result[0].Skins,
    currentrank:
      result[0].CurrentSoloRank.split(' ')[0] +
      ' ' +
      result[0].CurrentSoloRank.split(' ')[1],
    previousrank: result[0].PreviousSoloRank,
    flexrank:
      result[0].CurrentSoloRank.split(' ')[0] +
      ' ' +
      result[0].CurrentSoloRank.split(' ')[1],
    be: result[0].BE,
    level: result[0].Level,
    rp: result[0].RP,
  }; //JSON
}
