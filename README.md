# Analysis of Crossfit Opens Athletes 2020 with Streamlit 🎨

Interactive dashboard for analyzing RX athletes performance and demographics from the 2020 CrossFit Open qualifications.

[![Docker Hub](https://img.shields.io/badge/docker%20hub-julientoucoula17/mon--app--streamlit-blue?logo=docker)](https://hub.docker.com/r/julientoucoula17/mon-app-streamlit)
[![Python](https://img.shields.io/badge/python-3.X-blue.svg?logo=python)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/streamlit-latest-FF4B4B.svg?logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📊 Features

- 🌍 **Global participation**: Breakdown of 393,536 athletes by country
- 👥 **Demographics analysis**: Gender distribution and division categories
- 📈 **Physical metrics**: Average age, height, weight, and BMI calculations
- 🏋️ **Affiliate insights**: Box participation statistics per country
- 🎯 **Filtered dataset**: RX athletes only (scaled division excluded)

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
docker pull julientoucoula17/mon-app-streamlit:latest
docker run -p 8501:8501 -e PORT=8501 julientoucoula17/mon-app-streamlit:latest
```

Then open **http://localhost:8501** in your browser.


### Option 2: Local Python Setup

**Prerequisites**:
- Python 3.X (via Miniconda/Anaconda recommended)
- Dataset: [2020_opens_athletes.csv](https://www.kaggle.com/datasets/jeanmidev/crossfit-games?select=2020_opens_athletes.csv)

**Installation**:

```bash
# Clone repository
git clone https://github.com/julientoucoula17/crossfit_open-streamlit-docker.git
cd crossfit_open-streamlit-docker

# Install dependencies
pip install streamlit pandas numpy plotly altair pydeck

# Download dataset from Kaggle
# Place 2020_opens_athletes.csv in project root

# Run application
streamlit run app.py
```

Access at **http://localhost:8501**

## 📁 Project Structure

```
crossfit_open-streamlit-docker/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml     # GitHub Actions CI pipeline
├── app.py                      # Main Streamlit application
├── 2020_opens_athletes.csv     # Dataset (393K athletes, download separately)
├── Dockerfile                  # Docker configuration (Miniconda-based)
├── LICENSE                     # MIT License
└── README.md                   # This file
```

## 🗂️ Data

- **Source**: [Kaggle - CrossFit Games Dataset](https://www.kaggle.com/datasets/jeanmidev/crossfit-games)
- **Scope**: 2020 CrossFit Open leaderboard (qualification phase)
- **Size**: 393,536 RX athletes
- **Filter**: Scaled division athletes excluded (`is_scaled < 1`)

### Glossary
- **RX (Prescribed)**: Standard difficulty workouts without modifications
- **Scaled**: Modified/easier workout variations (not included in this analysis)
- **Division**: Age/gender category (e.g., Men 18-34, Women 35-39)
- **Affiliate**: Registered CrossFit box/gym

## 🐳 Docker Details

### Environment Variables

- `PORT`: Streamlit server port (default: 8501)

### Build Locally

```bash
docker build -t crossfit-dashboard .
docker run -p 8501:8501 -e PORT=8501 crossfit-dashboard
```

### Image Details
- **Base**: `continuumio/miniconda3` (Python 3.X)
- **Size**: ~1.5GB (includes Miniconda + scientific stack)
- **Includes**: Deta CLI (pre-installed for potential deployment)

## 🔄 Continuous Integration

Automated Docker image builds and publishing via GitHub Actions:

- **Trigger**: Push to `master` branch
- **Registry**: [Docker Hub](https://hub.docker.com/r/julientoucoula17/mon-app-streamlit)
- **Tags**: 
  - `:latest` (always points to most recent build)
  - `:<commit-sha>` (specific version)
- **Cache**: Build cache enabled for faster subsequent builds

### Required GitHub Secrets
```yaml
DOCKERHUB_USERNAME  # Your Docker Hub username
DOCKERHUB_TOKEN     # Docker Hub access token
```

## 🛠️ Development

### Dependencies

```bash
# Core
streamlit       # Dashboard framework
pandas          # Data manipulation
numpy           # Numerical operations
plotly          # Interactive visualizations

# Additional (included in Dockerfile)
altair          # Alternative plotting library
pydeck          # Geospatial visualizations
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Julien Toucoula**
- LinkedIn: [@julien-t-870b7613a](https://www.linkedin.com/in/julien-t-870b7613a/)
- GitHub: [@julientoucoula17](https://github.com/julientoucoula17)
- Docker Hub: [@julientoucoula17](https://hub.docker.com/u/julientoucoula17)

## 🙏 Acknowledgments

- Dataset provided by [jeanmidev on Kaggle](https://www.kaggle.com/datasets/jeanmidev/crossfit-games)
- Built with [Streamlit](https://streamlit.io)
- Visualizations powered by [Plotly](https://plotly.com)

---

⭐ **If you find this project useful, please consider giving it a star on GitHub!**
