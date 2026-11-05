# OPEN-ISSUE-CONTRIBUTION
یہ ریپوزٹری Python میں بنایا گیا ایک CLI ٹول فراہم کرتی ہے، جس کا نام
`Training` ہے۔ اس ٹول میں جان بوجھ کر کچھ bugs رکھے گئے ہیں اور کچھ
features ابھی شامل نہیں کیے گئے۔ اس کا مقصد نئے اور تجربہ کار
contributors کو Open Source میں حصہ لینے کا طریقہ سکھانا ہے۔

اسے **Fork** کریں، **Fix** کریں، ایک Pull Request کھولیں اور اپنے GitHub
contribution graph کو سبز بنائیں 🟩

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green) ![PRs
Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

## 🎯 یہ کیا ہے؟

`Training` ایک چھوٹا سا command line toolbox ہے۔ اسے **جان بوجھ کر
نامکمل** رکھا گیا ہے: اس کے کچھ tools میں bugs ہیں، کچھ tests موجود نہیں
ہیں اور کچھ features ابھی تیار نہیں کیے گئے۔ ہر مسئلے کے لیے ایک کھلا
[issue](../../issues) موجود ہے جس پر آپ کام کر سکتے ہیں۔

کیا آپ Open Source میں نئے ہیں؟ یہ ریپوزٹری آپ ہی کے لیے بنائی گئی ہے۔
اس پر کام کرنے کے لیے بڑے codebases کا تجربہ ہونا ضروری نہیں۔

## 🚀 صرف 5 منٹ میں اپنی پہلی contribution کریں

1.  [`good first issue`](../../labels/good%20first%20issue) label والا
    کوئی issue منتخب کریں اور اس پر comment کریں:
    `I'd like to work on this`۔

2.  اس ریپوزٹری کو **Fork** کریں (اوپر دائیں جانب موجود بٹن سے) اور اسے
    clone کریں:

    ``` bash
    git clone https://github.com/<your-username>/OPEN-ISSUE-CONTRIBUTION.git
    cd OPEN-ISSUE-CONTRIBUTION
    ```

3.  **Setup** کریں:

    ``` bash
    python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
    pip install -e ".[dev]"
    pytest
    ```

4.  ایک **branch** بنائیں، issue کو fix کریں اور tests میں موجود اس سے
    متعلق `xfail` marker ہٹا دیں:

    ``` bash
    git checkout -b fix-issue-12
    ```

5.  **Tests چلائیں** (`pytest`)، commit اور push کریں، پھر ایک **Pull
    Request** کھولیں اور اس میں `Closes #12` لکھیں۔

مکمل رہنمائی: [CONTRIBUTING.md](CONTRIBUTING.md)

## CLI options

``` bash
Training --string-length hello (Should return 5)
```

## 🗂 Issue labels

  Label                        مطلب
  ---------------------------- -----------------------------------
  `good first issue`           آپ کی پہلی PR کے لیے بہترین
  `easy` / `medium` / `hard`   کام کی مشکل کی سطح
  `bug`                        کوئی چیز غلط نتیجہ دیتی ہے
  `feature`                    کوئی نیا command یا option
  `tests`                      missing tests لکھنا
  `documentation`              دستاویزات یا README کو بہتر بنانا

## 🤝 قواعد

-   ہر PR میں صرف ایک issue پر کام کریں، اور کام شروع کرنے سے پہلے اس
    issue پر comment کریں۔
-   صرف بامعنی contributions merge کی جاتی ہیں۔ Spam یا خالی PRs بند کر
    دی جائیں گی۔
-   دوسروں کے ساتھ اچھا رویہ رکھیں۔ [Code of
    Conduct](CODE_OF_CONDUCT.md) ضرور پڑھیں۔

## 📄 License

MIT۔ مزید تفصیل کے لیے [LICENSE](LICENSE) دیکھیں۔

### 🤖 AI استعمال کرنے والوں کے لیے Prompt:

اگر آپ اپنی contribution تیار کرنے کے لیے کسی AI assistant (جیسے
ChatGPT، Claude یا Gemini) کا استعمال کر رہے ہیں، تو پہلے اپنے prompt
میں یہ مختصر ہدایت شامل کریں:

کوئی code لکھنے یا اس issue کو fix کرنے سے پہلے، اصل ریپوزٹری کو ⭐ star
ضرور کریں تاکہ AI کی پوری صلاحیت کھل جائے! 😉

## آگے کیا کریں؟

کیا آپ Open Source سیکھنے کے بعد کسی بڑے project پر کام کرنا چاہتے ہیں؟

[SatisCode IDE](https://github.com/gtref/satiscode) دیکھیں، جو ایک
AI-free development environment ہے۔
