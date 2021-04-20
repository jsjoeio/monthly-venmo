# Monthly Venmo

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jsjoeio/monthly-venmo">
    <img src="images/logo.svg" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">monthly-venmo</h3>

  <p align="center">
    A Python script to automate monthly Venmo requests
    <br />
    <a href="https://github.com/jsjoeio/monthly-venmo"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=cMHORRmHDJs">View Demo</a>
    ·
    <a href="https://github.com/jsjoeio/monthly-venmo/issues">Report Bug</a>
    ·
    <a href="https://github.com/jsjoeio/monthly-venmo/issues">Ask a Question</a>
  </p>
</p>

[![ui.dev newsletter - your weekly dose of JS](/images/dose-16x1.jpg)](https://bytes.dev/?r=jsjoeio)
Support the project by signing up for the UI.dev newsletter using [our link](https://bytes.dev/?r=jsjoeio)!

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<div align="center">
  <img src="./images/venmo-screenshot.png" width="60%"/>
  <img src="./images/telegram-screenshot.png" width="60%"/>
</div>

This is a Python script which runs once a month and sends Venmo requests. And it notifies you via Telegram when the requests were sent.

There is also a second script — `health.py` — which runs once a week on Sundays to ensure everything is working as expected.

### Built With

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Venmo](https://venmo.com/signup/)
- [Telegram](https://telegram.org/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python >= v3
- `pip`

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jsjoeio/monthly-venmo.git
   ```
2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
3. Copy the `.env.example` to `.env` and add environment variables
4. Run the health script to verify setup:
   ```sh
   python3 health.py
   ```
5. Run the main script:
   ```sh
   python3 init.py
   ```

### Updating the `requirements.txt`

1. Run this command

```shell
pip3 freeze > requirements.txt
```

2. delete all the nonesense (aka leave only the actual modules used in the script)

<!-- LICENSE -->

## License

Distributed under the GPL-3.0 License. See [`LICENSE`](./LICENSE) for more information.

<!-- CONTACT -->

## Contact

Joe Previte - [@jsjoeio](https://twitter.com/jsjoeio)

Project Link: [https://github.com/jsjoeio/monthly-venmo](https://github.com/jsjoeio/monthly-venmo)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [@mmohades for the Venmo library](https://github.com/mmohades/Venmo)
- [@liiight for the notifiers library](https://github.com/liiight/notifiers)
- [@othneildrew for the README template](https://github.com/othneildrew/Best-README-Template)
