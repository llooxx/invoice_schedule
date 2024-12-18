import datetime
from PIL import Image
import pdfplumber
import pdfplumber.display
from pyzbar import pyzbar
import re
import rmbTrans

invoice_types = {
    "04": "增值税普通纸质发票",
    "10": "增值税普通电子发票",
    "01": "增值税专用发票",
    "11": "增值税卷票",
}
zh_daxie = "⊗零壹贰叁肆伍陆柒捌玖拾佰仟萬亿圆角分正整"


def is_valid_date(date_str: str) -> bool:
    if len(date_str) != 8:
        return False
    try:
        # 尝试按照 YYYYMMDD 的格式解析日期字符串
        datetime.datetime.strptime(date_str, "%Y%m%d")
        return True
    except ValueError:
        # 如果解析失败，返回 False
        return False


class Invoice:
    total = None  # 价税合计
    price = None  # 开票金额
    tax = None  # 税额
    amount = None  # 开票金额
    max_shuilv = None  # 税率
    code = None  # 发票代码
    number = None  # 发票号码
    date = None  # 开票日期
    company = None  # 销方名称
    type = None  # 发票类型
    check = None  # 发票校验码
    taxpayer_id = None  # 纳税人识别号
    img: Image.Image | None = None

    def __init__(self, qrcode: str, page_text: str):
        # 二维码
        res: list[str] = [e.strip() for e in qrcode.split(",")]
        self.type = res[1] + (invoice_types[res[1]] if res[1] in invoice_types else "增值税普通电子发票")
        self.code = res[2]
        self.number = res[3]
        if self.type != "增值税卷票":
            self.amount = res[4]
            self.date = res[5]
            self.check = res[6]
        # 解析文字
        words = re.split(r"\n| |\r", page_text)
        words = [e.strip() for e in words if e]
        # 纳税人识别号
        re_taxpayer_id = re.findall(r"[0-9a-zA-Z]{18}", page_text)
        if len(re_taxpayer_id) == 1:
            self.taxpayer_id = re_taxpayer_id[0]
        elif len(re_taxpayer_id) > 1:  # 有多个的时候判断中间是否有日期，有日期的位身份证，跳过
            for e in re_taxpayer_id:
                if is_valid_date(e[6:14]):
                    continue
                self.taxpayer_id = e
        # 销方名称
        companys = [e for e in words if "公司" in e and "开户" not in e]
        self.company = companys[0] if len(companys) >= 0 else None
        if re.search(r"[：|:]", self.company):
            self.company = re.split(r"[：|:]", self.company)[1].strip()

        # 税率
        shuilvs = [e.replace("%", "") for e in words if e.endswith("%")]
        shuilvs = [int(e) for e in shuilvs if e]
        self.max_shuilv = max(shuilvs) if len(shuilvs) > 0 else 0
        # 金额
        prices = [e.replace("¥", "").replace("（小写）", "") for e in words if e.startswith("¥")]
        prices = [e for e in prices if e]
        # 从page_text中解析大写中文，即zh_daxie里的中文
        daxie_price = re.search(r"[⊗零壹贰叁肆伍陆柒捌玖拾佰仟萬亿圆角分正整]{2,}", page_text).group()
        daxie_price = "{:.2f}".format(rmbTrans.trans(daxie_price))
        # prices去重
        prices.append(str(self.amount))
        prices.append(daxie_price)
        prices = list(set(prices))
        if len(prices) == 3 or len(prices) == 2:
            self.tax = prices[0]
            self.total = prices[0]
            for e in prices:
                if float(self.tax) > float(e):
                    self.tax = e
                if float(self.total) < float(e):
                    self.total = e
            prices.remove(self.tax)
            prices.remove(self.total)
            self.price = prices[0] if len(prices) == 1 else self.total
        elif len(prices) == 1:
            self.price = prices[0]
            self.total = prices[0]
            self.tax = "0.00"
        else:
            print(prices)
            print("读取金额有问题")

    def __str__(self):
        res = ""
        if self.type is not None and self.type != "":
            res += f"发票类型：{self.type}"
        if self.code is not None and self.code != "":
            res += f"\n发票代码：{self.code}"
        if self.number is not None and self.number != "":
            res += f"\n发票号码：{self.number}"
        if self.type != "增值税卷票":
            res += f"\n开票日期：{self.date}"
        if self.check is not None and self.check != "":
            res += f"\n校验码：{self.check}"
        if self.total is not None:
            res += f"\n价税合计：¥{self.total}"
        if self.price is not None:
            res += f"\n金额：¥{self.price}"
        if self.tax is not None:
            res += f"\n税额：¥{self.tax}"
        res += f"\n税率：{self.max_shuilv if self.max_shuilv is not None else 0}%"
        if self.company is not None:
            res += f"\n销方名称：{self.company}"
        if self.taxpayer_id is not None:
            res += f"\n纳税人识别号：{self.taxpayer_id}"
        return res

    def __repr__(self):
        return str(self)


def readPDF(file_path: str) -> None | Invoice:
    with pdfplumber.open(file_path) as pdf:
        # 读取PDF文档第1页
        page = pdf.pages[0]
        # 分辨率200
        img: Image.Image = page.to_image(resolution=200).original
        # 裁剪1/4
        width, height = img.size
        barcodes = pyzbar.decode(img.crop((0, 0, width / 4, height / 4)), symbols=[pyzbar.ZBarSymbol.QRCODE])
        if len(barcodes) == 0:
            return None
        else:
            invoice = Invoice(qrcode=str(barcodes[0].data.decode("utf-8")), page_text=page.extract_text())
            invoice.img = img
            return invoice


if __name__ == "__main__":
    from pathlib import Path

    base_dir = "/Users/linorz/workspace/document/发票清单"
    # base_dir = "/Users/linorz/workspace/document/11月发票/发票清单/"
    owner_name = "李隆欣"
    for e in Path(base_dir).rglob("*.pdf"):
        print(e)
        fapiao = readPDF(e)
        print(fapiao)
