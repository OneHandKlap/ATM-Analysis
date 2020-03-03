const puppeteer = require("puppeteer");
const fs = require("fs");
var gracefulFs = require("graceful-fs");
gracefulFs.gracefulify(fs);
(async () => {
  function delay(time) {
    return new Promise(function(resolve) {
      setTimeout(resolve, time);
    });
  }
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto("URL", {
    waitUntil: "networkidle0"
  });

  for (var m = 1; m < 15; m++) {
    await page.type(
      "body > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]",
      "USERNAME"
    );
    await page.type(
      "body > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=password]",
      "PASSWORD"
    );
    await page.click(
      "body > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > a > input[type=submit]"
    );
    await delay(3000);
    let itemNum = m.toString();

    console.log("Now processing: " + itemNum.toString());
    await page.click(
      "body > form > table:nth-child(3) > tbody > tr:nth-child(" +
        itemNum +
        ") > td:nth-child(1) > a > input[type=submit]"
    );
    await delay(3000);
    await page.evaluate(
      () =>
        (document.querySelector(
          "body > form > input[type=text]:nth-child(11)"
        ).value = "")
    );
    await delay(3000);

    await page.type(
      "body > form > input[type=text]:nth-child(11)",
      "12-10-2017"
    );
    await page.click("body > form > a:nth-child(13) > input[type=submit]");
    await delay(5000);
    const selector = "body > form > table:nth-child(20) > tbody tr";
    console.log("Gathering Data");
    const data = await page.$$eval(selector, trs =>
      trs.map(tr => {
        const tds = [...tr.getElementsByTagName("td")];
        return tds.map(td => td.textContent);
      })
    );

    console.log("Writing to file");
    await delay(3000);
    for (var i = 0; i < data.length; i++) {
      if (i == 0) {
        fs.writeFile(
          "output" + itemNum + ".csv",
          data[0].join(",") + "\r\n",
          err => {
            if (err) throw err;
          }
        );
      } else {
        fs.appendFile(
          "output" + itemNum + ".csv",
          data[i].join(",") + "\r\n",
          err => {
            if (err) throw err;
          }
        );
      }
    }
    await delay(3000);
    console.log("finished writing to file: " + itemNum);
    await page.click("body > form > a:nth-child(15) > input[type=submit]");
    await delay(3000);
  }
})();
