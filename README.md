# data-cleaner-lite

CSV 数据清洗：去重、修剪空白、缺失值统计、清洗报告。零第三方依赖（csv 标准库）。

## 功能简介

- `clean_csv(text)` 返回清洗后行 + 报告；
- 报告含 rows_in/out、去重数、缺失单元格数、列名。

## 快速开始

```bash
python3 data_cleaner.py --file data.csv
printf 'name,age\n张三,20\n张三,20\n' | python3 data_cleaner.py
```

## 无 API key 如何运行

纯本地 csv 处理，**不需要任何 API key**。

## 目录结构

```
data-cleaner-lite/
├── data_cleaner.py
├── tests/test_data_cleaner.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
