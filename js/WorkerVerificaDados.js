const fs = require("fs");
const path = require("path");
const puppeteer = require("puppeteer");
const baseDir = path.resolve(__dirname, "..");
const filePath = path.join(baseDir, "json", "json_clientes.json");
const jsonData = fs.readFileSync(filePath, "utf-8");
const url = "https://www.yamaha-motor.com.br/";
const clientes = JSON.parse(jsonData);
let pessoasOK = [];
let pessoasRevisao = [];

async function main() {
    const browser = await puppeteer.launch({
        headless: false,
        args: [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-blink-features=AutomationControlled",
        "--disable-infobars",
        "--start-maximized",
        ],
        defaultViewport: null,
    });
    const page = await browser.newPage();
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " + "(KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36");
    console.log("Acessando a página da Yamaha...");
    await page.goto(url, { waitUntil: "networkidle2" });
    /*
        puppetter como worker que verifica se os dados do nome/cpf pesquisado batem, 
        se bater, adiciona em pessoas com dados OK, 
        Se não bater vai para pessoas para revisar, 
        dai faz o próximo tratamento, de ou arrumar com base no site ou não sei oq
    */
   await browser.close();
}
main();
