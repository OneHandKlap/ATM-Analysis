const puppeteer = require("puppeteer");
const fs = require("fs");

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto("https://online-service-corp.com/index.shtml", {
    waitUntil: "networkidle0"
  });
  await page.type(
    "body > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]",
    "slater"
  );
  await page.type(
    "body > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=password]",
    "atm"
  );
  await page.click(
    "body > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > a > input[type=submit]"
  );
  await page.click(
    "body > form > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(1) > a > input[type=submit]"
  );
  await page.evaluate(
    () =>
      (document.querySelector(
        "body > form > input[type=text]:nth-child(11)"
      ).value = "")
  );

  await page.type("body > form > input[type=text]:nth-child(11)", "12-8-2019");
  await page.click("body > form > a:nth-child(13) > input[type=submit]");

  const selector = "body > form > table:nth-child(20) > tbody tr";

  const data = await page.$$eval(selector, trs =>
    trs.map(tr => {
      const tds = [...tr.getElementsByTagName("td")];
      return tds.map(td => td.textContent);
    })
  );
  // var csv = data.join(",");
  // console.log(data);
  fs.writeFile("output.csv", data, err => {
    if (err) throw err;
  });

  await page.waitForNavigation();
})();
