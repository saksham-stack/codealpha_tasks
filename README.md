# 🎯 CodeAlpha Tasks Repository

> A collection of modern Python projects featuring async APIs, real-time financial data, and interactive visualizations.

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Last Updated](https://img.shields.io/badge/Updated-June%202026-blueviolet?style=flat-square)](README.md)

---

## 📁 What's Inside

### 1. **🎲 Task1.py** - Random Word & Definition Fetcher
A powerful async Python script that fetches random English words and their definitions from the Datamuse API.

**✨ Key Features:**
- ⚡ Async HTTP requests for non-blocking operations
- 🔍 Fetches random 6-letter English nouns with detailed definitions
- 🛡️ Intelligent fallback mechanism for offline usage
- 🎛️ Customizable word length via wildcard patterns
- 🚀 Production-ready error handling

**📡 API:** [Datamuse API](https://www.datamuse.com/api)

**Example Output:**
```
📡 Connecting to Datamuse API to fetch a secret word...
✅ Word Found: PYTHON
Definition: A large snake found in tropical regions
```

---

### 2. **📊 Task2.py** - Real-Time Portfolio Visualizer
An interactive CLI application that analyzes your investment portfolio with real-time stock prices and generates beautiful charts.

**✨ Key Features:**
- 💰 Real-time stock price fetching from Yahoo Finance
- 🖥️ Interactive command-line interface
- 📈 Professional horizontal bar charts
- 💼 Automatic portfolio value calculation
- 💾 CSV export functionality
- 🎨 Customized styling with seaborn

**📡 API:** Yahoo Finance (via yfinance library)

**Example Output:**
```
📊 Launching visual engine window...
[Displays interactive portfolio allocation chart]
```

---

### 3. **📄 visual_portfolio_manifest.csv**
Sample portfolio data file demonstrating the expected CSV format.

**Contents:**
- NVDA: 45 units @ $209.05 = $9,407.25
- AAPL: 30 units @ $303.84 = $9,115.20
- **Total Portfolio Value:** $18,522.45

---

---

## � Requirements

### 🐍 Python Version
- **Python 3.7+** (recommended: Python 3.10 or higher)

### 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `httpx` | >= 0.23.0 | Async HTTP requests (Task1) |
| `yfinance` | >= 0.1.70 | Yahoo Finance data retrieval (Task2) |
| `matplotlib` | >= 3.5.0 | Data visualization (Task2) |

**Optional but recommended:**
- `pandas` - Advanced data manipulation
- `aiohttp` - Alternative async HTTP library
- `requests` - Synchronous HTTP fallback

### 💻 System Requirements
- ✅ Windows, macOS, or Linux
- ✅ Internet connection (required for live API calls)
- ✅ Display capability (for matplotlib visualizations)
- ✅ 50MB+ free disk space

---

## 🚀 Quick Start

### ⚙️ Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/saksham-stack/codealpha-tasks.git
   cd codealpha-tasks
   ```

2. **Install dependencies**
   ```bash
   pip install httpx yfinance matplotlib
   ```
   
   Or install from requirements file (if available):
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python -c "import httpx, yfinance, matplotlib; print('✅ All dependencies installed!')"
   ```

---

### 📖 Usage Guide

#### 🎲 Running Task1.py - Word Fetcher
```bash
python Task1.py
```

**What it does:**
- Connects to Datamuse API
- Fetches a random 6-letter English noun
- Displays the word with its definition
- Falls back to local dictionary if offline

**Requirements:** Internet connection

**Sample Run:**
```
📡 Connecting to Datamuse API to fetch a secret word...
✅ Word Found: WHISPER
Definition: Soft, hushed speech or voice
```

---

#### 📊 Running Task2.py - Portfolio Visualizer
```bash
python Task2.py
```

**Step-by-Step Walkthrough:**
```
=========================================
   VISUAL LIVE-TICKING ASSET ANALYTICS   
=========================================
Type 'done' when you have finished entering your positions.

1️⃣  Enter ticker symbol: AAPL
2️⃣  Enter quantity held: 30
3️⃣  Enter unit price (optional, or press Enter for live fetch): [Press Enter]
    ✅ Asset recorded: AAPL @ $303.84 (30 units)

4️⃣  Enter ticker symbol: NVDA
5️⃣  Enter quantity held: 45
6️⃣  Enter unit price (optional, or press Enter for live fetch): [Press Enter]
    ✅ Asset recorded: NVDA @ $209.05 (45 units)

7️⃣  Enter ticker symbol: done
📊 Launching visual engine window...
💾 Data exported to: visual_portfolio_manifest.csv
```

**Output Files:**
- Interactive chart visualization
- `visual_portfolio_manifest.csv` - Portfolio data export

**Requirements:** Internet connection for real-time prices

---

## � Troubleshooting

### ❌ "API Connection Failed"
**Cause:** Network connectivity issue or API downtime  
**Solution:**
```bash
# Check internet connection
ping google.com

# Verify API is online (Task1)
curl https://api.datamuse.com/words?sp="?????"

# Try again in a few moments
```

### ❌ ModuleNotFoundError: No module named 'httpx'
**Cause:** Dependencies not installed  
**Solution:**
```bash
pip install --upgrade httpx yfinance matplotlib
```

### ❌ TimeoutError
**Cause:** API response is slow  
**Solution:**
- Check your internet speed
- Try running the script again
- Increase timeout in code (advanced users)

### ❌ Matplotlib Display Issues
**Cause:** Display backend not configured  
**Solution:**
Add this to the top of Task2.py:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg', 'Agg', etc.
```

### ❌ Invalid Ticker Symbol
**Cause:** Typo in stock symbol  
**Solution:**
- Verify ticker on [Yahoo Finance](https://finance.yahoo.com)
- Use uppercase (e.g., AAPL not aapl)

---

## � Common Issues & FAQs

| Issue | Solution |
|-------|----------|
| **No internet?** | Task1 has offline fallback; Task2 requires internet |
| **Charts not showing?** | Try different matplotlib backend (TkAgg, Qt5Agg, Agg) |
| **Slow API response?** | Normal during market hours; try off-peak times |
| **CSV not generated?** | Ensure write permissions in the directory |

---

## 🎨 Customization

### Modify Task1.py Word Length
Change the wildcard pattern in line 15:
```python
"sp": "??????",     # 6-letter words (6 question marks)
"sp": "?????",      # 5-letter words
"sp": "????????",   # 8-letter words
```

### Customize Task2.py Chart Colors
Modify the color scheme in line 24:
```python
bars = ax.barh(tickers, values, color='#2ca02c', edgecolor='#1a611a', height=0.6)
# Change '#2ca02c' to any hex color code
```

---

## � Project Structure

```
codealpha-tasks/
├── README.md                          # This file
├── Task1.py                           # Word fetcher script
├── Task2.py                           # Portfolio visualizer script
├── visual_portfolio_manifest.csv      # Sample data file
└── requirements.txt                   # (Optional) Dependency file
```

---

## 💡 Learning Outcomes

By using these projects, you'll learn:
- ✅ **Async Programming** - Understanding asyncio and async/await patterns
- ✅ **REST APIs** - Consuming external APIs (Datamuse, Yahoo Finance)
- ✅ **Data Visualization** - Creating professional charts with matplotlib
- ✅ **CLI Development** - Building interactive command-line applications
- ✅ **Error Handling** - Implementing fallbacks and exception handling
- ✅ **CSV Operations** - Reading and writing CSV files

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Report Issues** - Found a bug? [Create an issue](https://github.com/yourusername/codealpha-tasks/issues)
2. **Submit PRs** - Have improvements? Send a pull request
3. **Improve Docs** - Help us improve this README
4. **Share Ideas** - Suggest new features in the discussions

---

## 📄 License

These tasks are part of the **CodeAlpha Training Program**.  
Licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Datamuse** - For the amazing word/definition API
- **Yahoo Finance** - For real-time stock market data
- **Python Community** - For incredible libraries like httpx, yfinance, and matplotlib
- **CodeAlpha** - For the opportunity to build these projects

---

## 📞 Support & Contact

- 💬 **Questions?** Check the [FAQ](#-common-issues--faqs) section
- 🐛 **Found a bug?** [Report it here](https://github.com/saksham-stack/codealpha-tasks/issues)
- 💡 **Feature request?** [Suggest it](https://github.com/saksham-stack/codealpha-tasks/discussions)

---

## 📈 Project Stats

| Metric | Value |
|--------|-------|
| **Language** | Python 3.7+ |
| **Lines of Code** | ~250 (combined) |
| **External APIs** | 2 |
| **Core Dependencies** | 3 |
| **Last Updated** | June 2026 |

---

<div align="center">

### ⭐ If you find this useful, please star this repository!

**Made with ❤️ for the CodeAlpha Community**

[🔝 Back to Top](#-codealpha-tasks-repository)

</div>

