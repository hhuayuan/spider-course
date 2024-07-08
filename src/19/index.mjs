import puppeteer from 'puppeteer';

async function getPage(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1024, height: 768 }); // 设置视口宽度和高度

  page.on('response', response => {
    if (response.status) {
      console.log(response.status());
    }
  });

  try{
    await page.goto(url, {
      waitUntil: 'networkidle2',
    });
  }catch(e){
    print(e);
    return {};
  }

  const pageTitle = await page.evaluate(() => {
    return document.title;
  }
  );
  console.log(pageTitle);
  // const html = await page.content();

  var screenshotFileName = "test.png";
  await page.screenshot({
    path: `${screenshotFileName}`,
    fullPage: true,
  });

  await page.close();
  await browser.close();
}

getPage("http://spiderbuf.cn");