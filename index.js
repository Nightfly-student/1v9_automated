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
    res.send(csvJSON(data.toString()));
  });
});

// async function findSLCReborn() {
//   const windowRef = await getWindows();

//   const lookingFor = "SLC Checker - Reborn";
//   var window = null;

//   for await (let i of windowRef) {
//     if ((await i.getTitle()) === lookingFor) {
//       window = i;
//       break;
//     }
//   }

//   if (window === null) {
//     console.log("Window not found");
//     throw new Error("Window not found");
//   }

//   await window.focus();

//   return window;
// }

// async function moveToFile(window) {
//   const file = await screen.find(
//     await imageResource("/images/fileButton.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center = await centerOf(file);

//   await mouse.setPosition(center);

//   await mouse.leftClick();
// }

// async function moveToClipboard(window) {
//   const copy = await screen.find(await imageResource("/images/clipboard.png"), {
//     confidence: 0.5,
//   });

//   const center = await centerOf(copy);

//   await mouse.setPosition(center);

//   await mouse.leftClick();
// }

// async function regionSelect(region) {
//   await keyboard.pressKey("tab");
//   await keyboard.pressKey("tab");

//   const file = await screen.find(
//     await imageResource("/images/regionSelect.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center = await centerOf(file);

//   await mouse.setPosition(center);

//   await right(100);

//   await mouse.leftClick();

//   //   await keyboard.pressKey("A");
//   //   await keyboard.pressKey("A");
//   //   await keyboard.pressKey("A");
//   //   await keyboard.pressKey("A");

//   //   await sleep(500);

//   //   if (region === "EUW") {
//   //     await keyboard.pressKey("e");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "NA") {
//   //     await keyboard.pressKey("n");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "EUNE") {
//   //     await keyboard.pressKey("e");
//   //     await keyboard.pressKey("e");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "OCE") {
//   //     await keyboard.pressKey("o");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "LAN") {
//   //     await keyboard.pressKey("l");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "LAS") {
//   //     await keyboard.pressKey("l");
//   //     await keyboard.pressKey("l");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "BR") {
//   //     await keyboard.pressKey("b");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "TR") {
//   //     await keyboard.pressKey("t");
//   //     await keyboard.pressKey("r");

//   //     await keyboard.pressKey("enter");
//   //   }

//   //   if (region === "RU") {
//   //     await keyboard.pressKey("r");
//   //     await keyboard.pressKey("u");

//   //     await keyboard.pressKey("enter");
//   //   }
// }

// async function importAccount() {
//   const file = await screen.find(await imageResource("/images/import.JPG"), {
//     confidence: 0.5,
//   });

//   const center = await centerOf(file);

//   await mouse.setPosition(center);

//   await mouse.leftClick();
//   await mouse.leftClick();
// }

// async function startChecking() {
//   const file = await screen.find(
//     await imageResource("/images/checkerButton.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center = await centerOf(file);

//   await mouse.setPosition(center);

//   await mouse.leftClick();

//   await sleep(500);

//   const file2 = await screen.find(
//     await imageResource("/images/checkerStart.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center2 = await centerOf(file2);

//   await mouse.setPosition(center2);

//   await mouse.leftClick();
// }

// async function waitForFinish() {
//   return new Promise((resolve) => {
//     const interval = setInterval(async () => {
//       await screen
//         .find(await imageResource("/images/finished.JPG"), {
//           confidence: 0.5,
//         })
//         .then((file) => {
//           if (file) {
//             clearInterval(interval);
//             console.log("Finished");
//             resolve();
//           }
//         })
//         .catch((err) => {
//           console.log("waiting...");
//         });
//     }, 5000);
//   });
// }

// async function exportAccount() {
//   const file = await screen
//     .find(await imageResource("/images/toAccount.JPG"), {
//       confidence: 0.5,
//     })
//     .catch((err) => {
//       throw new Error("Could not find the account");
//     });

//   const center = await centerOf(file);

//   await mouse.setPosition(center);

//   await mouse.rightClick();

//   const file2 = await screen.find(await imageResource("/images/copyInfo.JPG"), {
//     confidence: 0.5,
//   });

//   const center2 = await centerOf(file2);

//   await mouse.setPosition(center2);

//   await sleep(500);

//   const file3 = await screen.find(
//     await imageResource("/images/copyFormat.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center3 = await centerOf(file3);

//   await mouse.setPosition(center3);

//   await sleep(500);

//   const file4 = await screen.find(
//     await imageResource("/images/exportToCSV.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center4 = await centerOf(file4);

//   await mouse.setPosition(center4);

//   await mouse.leftClick();

//   await sleep(500);
// }

// async function removeAccount() {
//   const file = await screen.find(await imageResource("/images/edit.JPG"), {
//     confidence: 0.5,
//   });

//   const center = await centerOf(file);

//   await mouse.setPosition(center);

//   await mouse.leftClick();

//   const file2 = await screen.find(
//     await imageResource("/images/clearAccount.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center2 = await centerOf(file2);

//   await mouse.setPosition(center2);

//   await mouse.leftClick();

//   await sleep(500);

//   const file3 = await screen.find(
//     await imageResource("/images/clearAccountAccept.JPG"),
//     {
//       confidence: 0.5,
//     }
//   );

//   const center3 = await centerOf(file3);

//   await mouse.setPosition(center3);

//   await mouse.leftClick();
// }

function csvJSON(csv) {
  var lines = csv.split('\n');

  var result = [];

  // NOTE: If your columns contain commas in their values, you'll need
  // to deal with those before doing the next step
  // (you might convert them to &&& or something, then covert them back later)
  // jsfiddle showing the issue https://jsfiddle.net/
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
  return result; //JSON
}
