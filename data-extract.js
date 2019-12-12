const puppeteer = require("puppeteer");

payload = {
  user: "slater",
  pass: "atm"
};
(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto("https://online-service-corp.com/index.shtml");
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
    "body > form > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(1) > a > input[type=submit]"
  );
  await page.type(
    "body > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]",
    "12-11-2016"
  );

  await page.waitForNavigation();
})();
